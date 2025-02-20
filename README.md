# Download Execute Report

Download Execute Report is a Python script that downloads an executable file, runs it, captures the output, and sends the results via email. This script demonstrates how to automate downloading, executing, and reporting processes using Python.

**This script is intended for educational purposes only to understand how automation works in cybersecurity and ethical hacking.**

## Features

- Downloads an executable file from a specified URL.
- Executes the downloaded file and captures its output.
- Sends the captured output via email.

## Prerequisites

- Python 3.x
- Windows operating system
- Internet connection (for downloading and sending emails)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Kasperone/download_execute_report.git
cd download_execute_report
```

## Usage

Run the script to download, execute, and report:

```bash
python3 download_execute_report.py
```

### Notes:

- Replace `john@gmail.com` and `password` in the script with your actual email credentials.
- Ensure that **Less Secure Apps** access is enabled on your Gmail account or use an app-specific password.
- Running this script requires administrator privileges to execute downloaded files properly.

## Example Output:

```
Downloading: laZagne.exe
Executing: laZagne.exe all
Sending report to email...
```

## Troubleshooting

- Ensure the download URL is accessible and the file exists.
- Verify your email credentials are correct.
- Run the script as administrator for proper execution.

## License

This project is licensed under the MIT License.

## About

This script is part of the course **"Learn Python & Ethical Hacking from Scratch"** on Udemy. The course covers Python scripting and its application in ethical hacking, network security, and more.

---

### Disclaimer:

**This script is for educational purposes only. Unauthorized downloading and execution of files is illegal and unethical. Use this script only on systems you have explicit permission to test.**