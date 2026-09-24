# Placement Attendance Condonation Letter Generator

A lightweight Python utility that generates a **ready-to-submit attendance condonation letter in PDF format** for placement-related absences.

Instead of manually rewriting the letter for every placement activity, add the company and participation date to `names.txt`, enter the letter date, and the script automatically creates a professionally formatted PDF.

## ✨ Features

- 📄 Generates a formatted **A4 PDF** letter using ReportLab
- 🏢 Supports **one or multiple placement activities** in a single letter
- 📅 Reads company names and participation dates from `names.txt`
- 🧠 Automatically switches between singular and plural wording
- 🔤 Parses entries in the format `Company Name (Date)`
- 🗂️ Automatically generates a descriptive output filename
- ⚠️ Validates that `names.txt` exists and contains entries
- ⚙️ Keeps student and faculty details configurable directly in the script

## 🛠️ Tech Stack

- **Python 3**
- **ReportLab** – PDF generation
- **Regular Expressions (`re`)** – parsing company/date entries
- **OS / Sys** – file handling and command-line validation

## 📁 Project Structure

```text
placement_allowance_letter/
├── main.py                 # PDF generation script
├── names.txt               # Placement company/date entries
├── README.md               # Project documentation
└── .gitignore              # Git ignore rules (recommended)
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd placement_allowance_letter
```

### 2. Install Python

Make sure Python 3 is installed:

```bash
python3 --version
```

### 3. Install the dependency

Install ReportLab using pip:

```bash
pip3 install reportlab
```

If you are using a virtual environment, activate it first:

```bash
python3 -m venv venv
source venv/bin/activate
pip install reportlab
```

On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
pip install reportlab
```

## 📝 Configure Placement Details

Open `names.txt` and add one placement activity per line using:

```text
Company Name (Date)
```

For example:

```text
Infosys Workshop (August 31)
Unicourt Workshop (September 1)
```

The script accepts both full company names and activity descriptions because everything before the parentheses is treated as the activity/company name.

## ▶️ Generate the PDF

Run:

```bash
python3 main.py
```

The program will ask for the date of the letter:

```text
Enter letter date (e.g. 27th August 2026):
```

Enter the required date and the PDF will be generated automatically.

Example:

```text
PDF created successfully: condonation_InfosysWorkshop_UnicourtWorkshop_Infosys.pdf
```

## 📄 Generated Letter

The generated PDF contains:

- Faculty recipient details
- Letter date
- Subject: **Request for Condonation of Attendance**
- Formal request explaining the placement-related absence
- List of placement activities and dates
- Attendance condonation request
- Student name, USN, year, and section

The script automatically adjusts the wording depending on whether `names.txt` contains **one or multiple activities**.

### Single activity

```text
The details of the placement activity are as follows:
```

### Multiple activities

```text
The details of the placement activities are as follows:
```

## ⚙️ Customization

Student and faculty information is currently defined near the top of `main.py`:

```python
student_name = "Shaldon Barnes"
usn = "NNM23CSXXX"
year_section = "XXXX"
teacher_name = "YYYYyy"
teacher_designation = "Assistant Professor Gd. III"
college_name = "NMAM Institute of Technology, Nitte"
```

Update these values if the letter is being used by another student or for another faculty member.

You can also customize the PDF appearance through the ReportLab configuration in `main.py`, including:

- Font
- Font size
- Line spacing
- Margins
- Page size
- Paragraph spacing

## 🔍 Input Format

Each line in `names.txt` follows this pattern:

```text
<Company or Activity> (<Date>)
```

The script uses a regular expression to separate the name from the date.

If an entry does not contain parentheses, it is still accepted:

```text
Infosys
```

In that case, the activity is included without a participation date.

## 🛡️ Validation

The script checks for common input problems before generating the PDF.

If `names.txt` is missing:

```text
Could not find names.txt next to this script...
```

If `names.txt` contains no entries:

```text
names.txt is empty. Add at least one 'Company (Date)' entry.
```

This prevents the program from generating an incomplete letter.

## 💡 Why This Project?

Placement processes often require students to attend workshops, interviews, assessments, and other recruitment activities during regular class hours. Creating an individual attendance-condonation letter for every activity can become repetitive.

This project automates that administrative task by converting a simple list of placement activities into a properly formatted PDF letter.

## 🔮 Possible Improvements

- [ ] Add a command-line interface for student/faculty details
- [ ] Support a `.json` or `.yaml` configuration file
- [ ] Add automatic current-date selection
- [ ] Add university/college logo support
- [ ] Add signature placeholders
- [ ] Provide multiple letter templates
- [ ] Add a GUI for non-technical users
- [ ] Add automated PDF preview
- [ ] Add unit tests for input parsing and PDF generation

## 📜 License

This project is intended for educational and personal productivity use. Add a license file if you plan to distribute or reuse the project publicly.
