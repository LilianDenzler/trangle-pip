## Installation
This package can be installed via
```bash
pip install tcrgeometry
```

### Extra dependencies

For TCR numbering, `ANARCI` must be installed via bioconda:

```bash
conda install -c bioconda anarci
```

For visualization, `PyMOL` must be installed via bioconda:

```bash
conda install conda-forge::pymol-open-source
```
Alternatively you can also set up this environment:
### Set up environment
The file `environment.yml` specifies the dependencies required to run the TRangle package. You can create a conda environment using this file:

```bash
conda env create -f environment.yml
```
In the main project directory run
```bash
pip install -e .
```

## Measure angles of existing TCR structures
To measure angles in existing TCR structures, you can use the `new_calc.py` script provided in the TRangle package. This script allows you to calculate angles and distances in a TCR structure file.


```bash
trangle-calc --input_pdb file.pdb --out_path ./out
```
This will output a CSV file with the measured angles and distances.
It will also output a PDB of the extracted variable domain, was well as a visualiseation of the measured angles and distance saved as an image and a .pse file which can be opened in PyMOL.


## Measure angles of existing TCR trajectories
To measure angles in existing TCR trajectories, you can use the `new_calc_MD.py` script provided in the TRangle package. This script allows you to calculate angles and distances in a TCR trajectory file.

```bash
trangle-calc-md --input_pdb file.pdb --input_md trajectory.traj --out_path ./out/MD_test
```

## Change geometry of a TCR structure

To change the geometry of a TCR structure, you can use the `change_geometry.py` script provided in the TRangle package. This script allows you to modify angles and distances in a TCR structure based on a configuration file.

```bash
trangle-change --input file.pdb --out_path ./out --BA 113 --BC1 98.7 --BC2 9.3 --AC1 71.5 --AC2 154 --dc 24
```
This script will read the configuration file, apply the specified changes to the angles and distances, and output a new PDB file with the modified geometry. It will also generate a visualization of the modified structure for inspection.

## Extract loop anchor residue coordinates
To extract the coordinates of loop anchor residues from a TCR structure, you can use the `extract_loop_anchor.py` script provided in the TRangle package. This script allows you to specify the loop anchor residues and extract their coordinates from a TCR structure file.

```bash
trangle-extract path/to/your/input.pdb
```
This will output a CSV file containing the coordinates of the specified loop anchor residues, which can be used for input to the CDR loop diffusion model.



Dataset:
From STCRDB get non-redundant abTCR set of IMGT-numbered structures (resolution cutoff 3.0, sequence identity cutoff 70%)
