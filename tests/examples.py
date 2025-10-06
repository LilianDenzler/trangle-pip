import os
import sys
import shlex
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Optional
import tcrgeometry


def _run(cmd_list, cwd: Optional[str] = None):
    print(f"\n$ {' '.join(shlex.quote(str(x)) for x in cmd_list)}")
    proc = subprocess.run(
        cmd_list,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    print(proc.stdout, end="")
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed with exit code {proc.returncode}: {' '.join(cmd_list)}")

def run_trangle_pipeline(
    input_pdb: str,
    out_dir: str,
    md_traj: Optional[str] = None,
    md_out_dir: Optional[str] = None,
    change_dir: Optional[str] = None,
    change_args: Optional[Dict[str, str]] = None,
    extract_pdb: Optional[str] = None,
):
    """
    - trangle-calc --input_pdb <input_pdb> --out_path <out_dir>
    - trangle-calc-md --input_pdb <input_pdb> --input_md <md_traj> --out_path <md_out_dir>
    - trangle-change --input <input_pdb> --out_path <out_dir> [--BA ... --BC1 ... ...]
    - trangle-extract <extract_pdb or input_pdb>
    """
    input_pdb = str(Path(input_pdb).resolve())
    out_dir = str(Path(out_dir).resolve())
    os.makedirs(out_dir, exist_ok=True)

    # 1) trangle-calc

    _run(["tcr-calc", "--input_pdb", input_pdb, "--out_path", out_dir])


    md_traj = str(Path(md_traj).resolve())
    md_out_dir = str(Path(md_out_dir or (Path(out_dir) / "MD_test")).resolve())
    os.makedirs(md_out_dir, exist_ok=True)
    #_run(["tcr-calc-md", "--input_pdb", input_pdb, "--input_md", md_traj, "--out_path", md_out_dir])


    # Base args
    cmd = ["tcr-change", "--input", input_pdb, "--out_path", change_dir]
    # Append extra flags (e.g., {"--BA":"113","--BC1":"98.7",...})
    for k, v in change_args.items():
        cmd += [k, str(v)]
    _run(cmd)

    _run(["tcr-extract-anchor", input_pdb])


if __name__ == "__main__":
    # Example usage
    pdb_file="/mnt/larry/lilian/DATA/Cory_data/1KGC/1KGC.pdb"
    md_path="/mnt/larry/lilian/DATA/Cory_data/1KGC/1KGC_Prod.xtc"
    run_trangle_pipeline(
            input_pdb=pdb_file,
            out_dir="./out",
            md_traj=md_path,
            md_out_dir="./out/MD_test",
            change_dir="./out/change",
            change_args={"--BA":"113", "--BC1":"98.7", "--BC2":"9.3", "--AC1":"71.5", "--AC2":"154", "--dc":"24"},
        )

    calc_results = tcrgeometry.calc_tcr_geometry(pdb_file, out_path="./out")
    print(calc_results)

    changed_pdb=tcrgeometry.change_tcr_geometry(pdb_file, out_path="./out_change", BA=113, BC1=98.7, BC2=9.3, AC1=71.5, AC2=154, dc=24)
    print(changed_pdb)
    anchor_coords = tcrgeometry.get_anchor_coords(pdb_file)
    print(anchor_coords)
    md_results = tcrgeometry.calc_tcr_geometry_MD(pdb_file, md_path, out_path="./out/MD_test")
    print(md_results)