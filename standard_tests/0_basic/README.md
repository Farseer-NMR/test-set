# 0_basic

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

- test along _x-axis_
- give fasta
- plot Bar Extended Horizontal

## test_2

- same as test_1
- without FASTA

## test_3

- same as test_1
- _missing_ residues set to `full`
- plots also 1H with scale 1.0 ppm

## test_4

- same as test_1
- with CSPs in some residues:
    - CSPs are 0.1 ppm added to each dimension
    - Ala1 in pkl_01
    - Lys60 in pkl_10
    - Lys60 in pkl_11 increased to 0.2 ppm per dimension.
    - Val100 reapears in pkl_19

## test_5

- same as test_4
- will all bar plots
