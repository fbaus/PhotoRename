# PhotoRename
Script to rename photos based on their exif tag

Organise all your pictures imported from different portable devices on your hard drive based on their date as reported in the exif tag.

The project started as a batch file calling exiftool, reading its output and renaming the picture based on that.

Issues to be solved:
- It takes about 2 sec/picture, can it be faster?
- sharing pictures via whatsapp creates duplicates, they should be indentified and only the original (the oldest picture should be kept)
-- a few ideas using python for matrix handling
