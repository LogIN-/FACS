## Introduction
`FACS` is a FACS machine output analyzer. Facilitates conversion of percentages to absolute cell numbers. 
Flow cytometry absolute number calculator.

## Get started
Before using this program you need to install following:

 1. Install Python for your operating system (windows/linux) [Link here](https://www.python.org/downloads/)
 2. After installing Python you need to install two Python packages for reading and writing Excel files 
 `xlrd` and `xlwt`
Linux:
```bash
sudo apt-get install python-xlrd
sudo apt-get install python-xlwt
```
Windows:
```
1. Set up a directory called C:\installers (or some other name of your
choice).
2. Download xlrd - https://pypi.python.org/pypi/xlrd and
            xlwt - https://pypi.python.org/pypi/xlwt/0.7.5 into that directory.
3. Unzip it both.
4. Start up a Command Prompt window, and then do:
    prompt> cd C:\installers\xlrd
    prompt> c:\Python27\python setup.py install
```

Now your system is prepared to run our program.
 
You working directory is `./data`. Please follow this instructions:

 - Create file in the `./data` directory file `Sections_input.xls`.
    So you should have it like this: `./data/Sections_input.xls`

 - In that file `Sections_input.xls` you need to add total number of
    isolated cells. 

 - Number should be added in following format:
    {numberValue}{space}{exponent} - `21 6` meaning: `21000000`

 - Every row represents one animal/sample.
    Row no° 1. in this file needs to contain `file-name` of your experimental data
    exported from FACS machine or FlowJo like in example below:

### Examples:  
###### Multi files example demo:
P8R.xls  |P9R.xls  |P10R.xls  |P11R.xls  |P12R.xls  |
-------- |-------- |-------- |-------- |-------- |
1375 6   |775 6   |75 6   |375 6   |1235 6   |
21 6     |16 6     |2 6     |264 6     |236 6     |

## RUN
So you installed Python and two excel extensions, prepared FACS data and `Sections_input.xls` file
now you are ready to run our application like this from command-line/terminal:
`python main.py`
Calculations are done in a metter of second. New files will be created in ./data directory with our results.
Our demo result is `P8R.xls - _October_19_2014_05_38PM.xls`. 
You will see corresponding result file for every Column task you configured in `Sections_input.xls`

## Understanding the output

 - In 1. column you will see name of your samples.
 - In 2. column it will be name of cell population you are analyzing. 
     - In 3. column percentage of cells
     - In 4. column absolute number of cells
 - In the following columns you have the same properties analyzed for cell subsets

Notice:

Default analyzed depth is no° 4: 

Forward and side scatter population, duplicates, live dead exclusion, cell population of interest
If you want to change this number is fairly simple:

EDIT line: #55 in our main.py file and set it to desired level

## Support and Bugs
If you are having trouble, have found a bug, or want to contribute don't be shy.
[Open a ticket](https://github.com/LogIN-/ospnc/issues) on GitHub.

## License
`FACS` source-code uses the The MIT License (MIT), see our `LICENSE` file.
```
The MIT License (MIT)
Copyright (c) LogIN- 2014
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
