# test-set

Dummy and controlled data sets to test Farseer-NMR functionalities.

# How to use

Find in this repository different peaklist dataset and different Farseer-NMR config JSON files for the different tests.

The `pkls_*` folders contain subfolders `0_*`, `1_*`, _etc_, that contain datasets of peaklists and config files; there is also README.md files explaining what is under test and what to expect.

Use Farseer-NMR in these tests to investigate the correct behaviour your of development branch.

# Useful

To test a branch, you can run the tests with the `master` branch and your `devel` branch, afterwards you can compare both `Backbone` folders with the following command (UNIX):

```bash
diff -I '#' folder1/ folder2/
```