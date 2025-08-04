# Automated CV Generator with LaTeX, Jinja2 and Python

This repository contains both my personal CV and the code that generates it from structured YAML content using a Jinja2-LaTeX template system.

The curriculum vitae is built upon a classic LaTeX template, enhanced to support two languages (currently Polish and English) and an optional GDPR clause, making it fully compliant with EU legal standards.

Email and phone number are censored in the public version, but feel free to reach out via GitHub or [LinkedIn](https://linkedin.com/in/binkowska-marta/) – I’d be happy to connect!

## Features

- CV generated automatically from YAML data
- Multi-language support
- GDPR clause optionally included
- Clean and minimal LaTeX design
- Fully reproducible build with Python and Jinja2

##  Tech Stack

- **Python 3.12.2** – for automation and logic
- **LaTeX** – for professional document layout and typography
- **Jinja2** – for templating dynamic LaTeX
- **YAML** – for clean and readable CV content

## Usage

To build the CV locally:

1. Clone the repository  
   ```bash
   git clone https://github.com/maarbin/cv_latex.git
   cd cv_latex
2. Install dependencies
    ```bash
    pip install -r requirements.txt
3. Adjust YAML files with your data

4. Build the CVs
    ```bash
    python build.py 
    ```
    By default, all four possible variants will be generated.

## Sample output

[My CV in English](https://maarbin.github.io/cv_latex/cv_en.pdf)