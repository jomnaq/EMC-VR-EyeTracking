USING PLOTTING R SCRIPTS:

To use them, you'll need two folders of data, each that should have 15 tests that correspond to each other:

- eye_paths
- orb_paths

For each participant (set of 15 trials), copy and paste their csv files into the Gen_tests folder (deleting the previous files). Make sure you do not change or remove the RMarkdown files that are already in these folders(rewrite_eye and rewrite_orb).

Then, delete the current run each of the scripts rewrite_orb and rewrite_eye. If you previously have done this and have the "all_eye_paths" or "all_orb_paths" files in the Gen_Tests folder, they will be overwritten.

After rewriting all_eye_paths.csv and all_orb_paths.csv, run the plotter RMarkdown. This script has general plotting and exploration of the data. More details on the individual plots and animations are inside of the Markdown document. After running plotter, the folders down-tests, up-tests, and left-tests will have csv files of dataframes with only the tests going that respective direction. Whenever you run plotter with new data, you will want to rename these csv files so they do not get overwritten.

In each of the folders down-tests, up-tests, and left-tests there is a script that will average the position at each time for each test, and then plot the x and y components of these averages. 

OTHER FOLDERS

data: In order to keep track of all data used, the data folder will store all tests. Simply copy/paste the files from the data file into the proper folders for scripting.

archive: Stores the old tests we did before the new structuring!

