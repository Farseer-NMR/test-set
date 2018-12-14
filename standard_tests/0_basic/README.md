# xx_axis

Routines performed along the _xx-axis_.

## test_1

- used pkl_set_0
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
    - Val95 reapears in pkl_19

## test_5

- same as test_4
- Phe70 in pkl_00 (makes CSPs in whole series)
- will all bar plots

## test_6

- same as test_5
- no FASTA

## test_7

- use pkl_set_2
