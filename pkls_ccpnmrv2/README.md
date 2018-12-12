# CCPNMR v2 peaklist formats

This folder contains dummy NMR peaklist files in the [CcpNmr Analysis v2](https://www.ccpn.ac.uk/v2-software/software/analysis) format.  

Peaklists represent a series of 2D (1H-15N) NMR experiments.

## 0_basic

Base peaklist dataset was build as follows:

- 20 peaklists, from: `pkl_00.csv` to `pkl_01.csv`
- protein length: 100
- protein sequence is alphabetically ordered 3-letter code a.a., chaging every 5 residues: `AAAAARRRRRNNNNN...`
    - fasta: `0_basic.fasta`
- residues 71 to 75 are Prolines, therefore _unassigned_.
- at each step (peaklist) a multiple of 5 residue is missing:
    - `pkl_00.csv` all residues are present
    - `pkl_01.csv` residue 5 is missing
    - `pkl_02.csv` residue 5 and 10 are missing
    - `...`

The tests are variatons of this dataset and confi file.
