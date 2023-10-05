# GovDataLabeler 
## Live Link

[Click here to access the GovDataLabeler web app](https://huggingface.co/spaces/saurabhharak/GovDataLabeler)
## Introduction

The **GovDataLabeler** is a Streamlit-based web application tailored for naming datasets sourced from various departments of the Indian government. This tool streamlines the process of creating standardized and descriptive names for datasets, ensuring clarity and consistency in data management.

## Features

- Select data source and sector from predefined Indian government codes.
- Specify start and end years for your dataset.
- Choose granularity and frequency levels.
- Automatically generates a dataset name based on your inputs.
- Checks for name uniqueness to avoid duplicates.
- Saves dataset information to an Excel file.

## Data Source Codes

The following are the available data source codes for Indian government departments:

- **CABSEC:** Cabinet Secretariat
- **CAG:** Comptroller & Auditor General
- **DAE:** Department of Atomic Energy
- **DOS:** Department of Space
- **ECI:** Election Commission of India
- (and more...)

## Sector Codes

The app supports a wide range of sector codes representing different domains within the Indian government. These include:

- **AGRI:** Agriculture
- **BNK:** Banking
- **CLMT:** Climate & Weather
- **HLTH:** Health
- (and more...)

## Requirements

To run the GovDataLabeler, you'll need:

- Python 3.6 or higher.
- The following Python packages:
  - streamlit
  - pandas

You can install the required packages using `pip`:

```bash
pip install streamlit pandas
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/saurabhharak/GovDataLabeler.git
cd GovDataLabeler
```

2. Run the application:

```bash
streamlit run app.py
```

3. Open your web browser and navigate to `http://localhost:8501`.

4. Follow the on-screen instructions to generate dataset names.

## Example Usage

1. Select a data source and sector from the dropdown menus.
2. Enter start and end years.
3. Choose granularity and frequency levels.
4. The app will automatically generate a dataset name based on your inputs.

## Screenshot

![GovDataLabeler Screenshot](namingapp.jpg)
## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

## Contact

For questions or support, please contact [jobsforsaurabhharak@gmail.com](mailto:jobsforsaurabhharak@gmail.com).

---


