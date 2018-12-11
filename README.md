# test-set

**Dummy** and **controlled** datasets to test Farseer-NMR functionalities.

## Motivation

Farseer-NMR calculations generates lots of different files, many of which are not text files, for example PDFs. Though most of the Farseer-NMR methods can be tested individually, one feels the need to test the _whole_ against _dummy_ and _controlled_ datasets and make sure the desired functionally is properly implemented without breaking others. Why not real datasets? Simply because real datasets contain too many details for the eye to inspect properly without missing details.

## How to use

Find in this repository different peaklist datasets and different Farseer-NMR JSON config files for the different tests.

The `pkls_*` folders contain subfolders `0_*`, `1_*`, _etc_, that contain datasets of peaklists and config files; there are also `README` files explaining what is being tested and what to expect in each case.

Use Farseer-NMR in these tests to investigate the behaviour your of development branch and if it performs correctly.

## Useful

To test a branch, you can run the tests with the `master` branch and your `devel` branch, afterwards you can compare both `Backbone` folders with the following command (UNIX):

```bash
diff -I '#' folder1/ folder2/
```