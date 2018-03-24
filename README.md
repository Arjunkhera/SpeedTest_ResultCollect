# Script to collect speedtest results and export as csv and png

### Purpose

The script runs download and upload tests from the speedtest.net site autmatically, from the terminal at specified intervals, stores the results in a text and csv file, and also generates a graph for the same in the form of a png file.

It can be used to test the stability of internet connection.

I designed it being frustrated by the fact that I failed to provide the proof of frequent disconnection to my ISP. Now I have complete records for speedtests without having to check manually each time.

### Prerequisite
speedtest-cli
```bash
sudo apt install speedtest-cli
speedtest-cli
```

### Running the script:
```bash
/bin/bash speedtest.sh
```

### Important
1. All result files are stored by the name "logddmmyy", eg log240318.

2. Results are sampled every ten minutes, though you can change this limit in the srcipt sleep function.

3. Servers are by default chosen nearest to you, again the cli command can be modified to test against a specific server. The list of speedtest servers is availaible [here](http://www.speedtest.net/speedtest-servers.php)

4. The number of samples can be modified by changing the counter in the for loop of the script.

5. After the completion of the script, a python program is run generating csv file and a png image of the results.

### Modifying the script

1. The jupyter notebook file for the python program has been provided in the source code, it generates matplotlib graphs and pandas DataFrame for the same.

### Possible Future Updates

1. Add some basic functionality in the form of agruments, such as the number of results to be produced, time interval between samples etc.
