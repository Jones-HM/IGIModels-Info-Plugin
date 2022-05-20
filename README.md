# IGIModels-Info-Plugin
This is plugin for IGI-1 Editor which extracts all the models info for game levels for for [Project I.G.I](https://en.wikipedia.org/wiki/Project_I.G.I.) game.

This is plugin for [IGI 1 Editor](https://github.com/IGI-Research-Devs/I.G.I-1-Editor) and you should have installed this in your machine.

## Prerequisite.
- IGI 1 Editor Setup: [IGI 1 Editor](https://github.com/IGI-Research-Devs/I.G.I-1-Editor) download from here.
- QEditor **QSC** Files: You should have `.qsc` files in this path `%appdata%\QEditor\QFiles\IGI_QSC\` from editor setup.
- Python 3.0: Get [Python 3.0](https://www.python.org/downloads/) and setup in your machine.

## Application Commands.
This application is command line tool so you need to provide parameters to it like this.
Usage `python IGI-Models-Info.py level output-file output-format distinct-models` here `distinct-models` param is optional.</br></br>
Example for Level 1 Models in _CSV_ format: </br>
command : `python IGI-Models-Info.py 1 'Level1Models' 'csv'`</br>
output : `Level #1 Total Models: 84 A.I Count: 4`</br></br>
Example for Level 5 Models in _JSON_ format:</br>
command : `python IGI-Models-Info.py 1 'Level5Models' 'json' 'true'`</br>
output : `Level #5 Total Models: 83 A.I Count: 4`</br>

## Examples .
Folder `Examples` contains some example files generated using this _plugin_ 
- `Examples/Level1Models.csv` - Contains file containing Level 1 Models in _CSV_ format.
- `Examples/Level1Models.json` - Contains file containing Level 1 Models in _JSON_ format.
- `Examples/Level10Models-All.csv` - Contains file containing **ALL** Level 10 Models in _CSV_ format.

## Output .
### Output of Models for Level 1 in _CSV_ format.</br>
![](https://raw.githubusercontent.com/IGI-Research-Devs/IGIModels-Info-Plugin/main/resources/level_csv_format.png)</br></br></br>
### Output of Models for Level 1 in _JSON_ format.</br>
![](https://github.com/IGI-Research-Devs/IGIModels-Info-Plugin/blob/main/resources/level_json_format.png)</br>
