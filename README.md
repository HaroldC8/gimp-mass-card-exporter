# gimp-mass-card-exporter
A gimp python script for exporting cards for printing based on a template and some provided data.

## Usage
- Create an empty folder
- Create a gimp file that you want to be used as a template
- Create a text file where your card data is stored
- Open gimp python console and paste in the code in main.py
- Type ```run("directory name")``` in the console and press enter

## Example
Input
![image](https://github.com/HaroldC8/gimp-mass-card-exporter/assets/70860865/bbe78e1c-bc74-4c22-8612-c09fbbe50100)
Output
![processed0](https://github.com/HaroldC8/gimp-mass-card-exporter/assets/70860865/67f2c569-7e36-4d45-a4c5-016447308db6)


## Todo
- [x] Function to process gimp file based on text inputs and dynamically change the position of the durability
- [x] Open text input file and read from it
- [x] For each text input call function to process gimp file
- [x] Store outputs in new A4 page files for printing
- [ ] Open image input file and use those images
- [ ] Randomize background texture position in range
