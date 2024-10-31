# Replace PDF

This is created to replace your PDF form with a new version.

For example, if you have filled out 5 PDF forms and then need to update the template you started with, with a new one you run the program and point out the folder where you have the 5 PDF Forms and then point out where to find the new template.

The program will create a new folder with all your forms replaced with the new one. The same folder structure will remain

## Command-Line arguments

````
python replace_pdf.py -s <sourcefolder> -t <template> -f <targetfolder>
OR as an executable
replace_pdf.exe -s <sourcefolder> -t <template> -f <targetfolder>
sourcefolder = the folder that has the PDF files that need to be replaced. Default = 'pdf'
template = the PDF form that are going to replace the old ones. Default = 'target.pdf'
targetfolder = where to put the newly replaced PDF forms. Default = '<sourcefolder>_new'
````

### Example

**Input**
````
replace_pdf.exe
````

**Output**
````
Source folder is "pdf"
Target file is "target.pdf"
Target folder is "pdf_new"
pdf\source_form.pdf pdf_new\source_form.pdf
pdf\Folder1\source_form.pdf pdf_new\Folder1\source_form.pdf
pdf\Folder2\source_form.pdf pdf_new\Folder2\source_form.pdf
pdf\Folder2\Subfolder1\bored_form - Copy.pdf pdf_new\Folder2\Subfolder1\bored_form - Copy.pdf
pdf\Folder2\Subfolder1\bored_form.pdf pdf_new\Folder2\Subfolder1\bored_form.pdf
````

## License

This is licensed under the MIT License