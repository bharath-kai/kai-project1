# Malware Analysis Auth GUI

This project provides a simple, user-friendly GUI tool for basic malware analysis using YARA rules and memory dump files. The tool is built with Python's Tkinter for the GUI and features user authentication (registration and login) for controlled access. It is intended as a demonstration or educational tool and not for production use.

## Features

- **User Registration and Login**: Secure authentication using bcrypt password hashing.
- **Memory Dump & YARA Rule Analysis**: Load a memory dump and scan it with user-supplied YARA rules.
- **Customizable Scan Size**: Specify the number of bytes to scan from the memory dump.
- **Results Display**: View YARA scan results in a scrollable text field.
- **Report Saving**: Save scan results to a text file.
- **Simple, Intuitive Interface**: Built with Tkinter for ease of use.

## Requirements

- Python 3.7+
- [bcrypt](https://pypi.org/project/bcrypt/)
- [yara-python](https://github.com/VirusTotal/yara-python)
- Tkinter (usually included with Python, but may require installation on some systems)

Install dependencies using pip:
```sh
pip install bcrypt yara-python
```

## Usage

1. **Run the Application**
    ```sh
    python malware_analysis_auth_gui.py
    ```
2. **Register or Login**
    - Enter a username and password to register, or login if you already have an account.

3. **Select Files**
    - Use "Browse" to select a memory dump file and a YARA rule file.

4. **Set Analysis Parameters**
    - Specify the number of bytes to analyze (default: 64).

5. **Analyze and View Results**
    - Click "Analyze" to run the scan.
    - Results are displayed in the Results section.

6. **Save the Report**
    - Click "Save Report" to save the analysis output.

## Security and Limitations

- **Authentication is In-Memory Only**: All users are stored in memory and lost when you close the program. For real applications, integrate with a database.
- **Not for Production**: This tool is for demonstration/learning; do not use as-is for critical or sensitive analysis.
- **Analysis is Limited**: Scans only the specified number of bytes from the memory dump.

## Example YARA Rule

Save the following as `example.yar`:
```
rule TestRule
{
    strings:
        $a = "malware"
    condition:
        $a
}
```

## License

This project is for educational/demonstration purposes.

## Author

- bharath-kai
