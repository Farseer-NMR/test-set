# 1_zz_axis

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

Inside each `test_` folder there is a `spectra` folder and `JSON` configuration file with the variations of each test.

## test_1

- peaklists were copied to the respective dimension
- `.csv` files renamed to `pkl_00.csv` because names accross dimensions must be equal.
- without expanding `missing` on `zz`

## test_2

- same as test_1
- with `"expand_missing_zz": true`

# test_3

- same as test_2
- For Asn15, CSPs of 0.01 ppm in pkl_01 and 0.1 ppm in pkl_02, in each dimension.
