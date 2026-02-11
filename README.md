# File-Identifier-Project
A Python-based file type identifier that analyzes magic numbers and file signatures to detect real file types, helping demonstrate file spoofing techniques and defensive security concepts.

## Project Progress

- [x] Path validation using pathlib
- [x] File vs directory handling
- [x] Binary header extraction
- [ ] Magic number signature matching
- [ ] ZIP container analysis (DOCX/XLSX)
- [ ] Heuristic detection (shebang, text)

## Reflection

February 9, 2026 

It has been a long time since I last programmed, and Python is coming back to me little by little. This project is particularly interesting because I was not previously aware that disguising a file’s true type can be used as an exploitation technique.

Building this program from A to Z allows me to become comfortable again with Python and its standard libraries, while also developing critical thinking skills. At the same time, the project helps me gain practical knowledge about vulnerabilities and defensive techniques related to file handling and content-based detection.


February 10, 2026 

Today’s progress focused on designing a clean and secure foundation for the project. I implemented full path validation using Python’s `pathlib` library, ensuring that user input is explicitly validated and that only real files (not directories) are accepted.

This step reinforced the importance of separating responsibilities in a program—handling user input, filesystem validation, and analysis logic independently. It also highlighted how small design decisions can improve both security and maintainability before any detection logic is implemented.


February 11, 2026 

Today’s work focused on building a secure and structured foundation for the file type identifier tool. I implemented full path validation using Python’s `pathlib` library, ensuring that only valid file paths are accepted and that directories or non-existent paths are rejected.

I redesigned the program flow to separate responsibilities clearly:

- User input and validation
- File header extraction (binary mode)
- Future signature detection logic

I also implemented a function to safely read the first N bytes of a file in binary mode. This establishes the basis for content-based file type detection using magic numbers rather than relying on file extensions.
