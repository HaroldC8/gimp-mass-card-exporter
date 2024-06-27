# gimp-mass-card-exporter
A gimp python script for exporting cards for printing based on a template and some provided data.

## Usage
- Create an empty folder
- Create a gimp file that you want to be used as a template
- Create a text file where your card data is stored
- Open gimp python console and paste in the code in main.py
- Type ```run("directory name")``` in the console and press enter

## Example
| Input | Output |
|-------|--------|
| <img src="https://github.com/HaroldC8/gimp-mass-card-exporter/assets/70860865/bbe78e1c-bc74-4c22-8612-c09fbbe50100" width="250" height="auto"> | <img src="https://github.com/HaroldC8/gimp-mass-card-exporter/assets/70860865/3de8366c-ce54-4b98-8d38-2bb389f90800" width="250" height="auto"> |

## Todo
- [x] Function to process gimp file based on text inputs and dynamically change the position of the durability
- [x] Open text input file and read from it
- [x] For each text input call function to process gimp file
- [x] Store outputs in new A4 page files for printing
- [x] Open image input file and use those images
