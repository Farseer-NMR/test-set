# Base datasets

Different sets of FASTA files, peaklists and other data designed to test different functionalities.

## Templates

Template files that can be used to generate datasets.

## FASTA files

List of `.fasta` files generated; these are stored in each peaklist data set.

### fasta_0

- protein length: 100
- protein sequence is alphabetically ordered 3-letter code a.a., chaging every 5 residues: `AAAAARRRRRNNNNN...`
- residues 71 to 75 are Prolines, therefore _unassigned_.

## Peaklist datasets

### pkl_set_0

- uses: `fasta_0.fasta`
- at each step (peaklist) a residue multiple of 5 is missing:
    - `pkl_00.csv` all residues are present
    - `pkl_01.csv` residue 5 is missing
    - `pkl_02.csv` residue 5 and 10 are missing
    - `...`

### pkl_set_1

- 3 peaklists in each dimension
- protein fasta: `fasta_0.fasta`
