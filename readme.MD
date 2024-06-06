# CSV Transformer App

This Streamlit app allows you to upload a CSV file, transform the data, and download the transformed CSV file. The transformation includes splitting patient names, mapping phone types, and adding additional rows for SMS notifications.

## Features

- Upload a CSV file with appointment data.
- Transform the data:
  - Split patient names into first and last names.
  - Convert service dates and times to a consistent format.
  - Map phone types to `sms` or `voice`.
  - Add additional rows for SMS notifications.
- Download the transformed CSV file.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/csv-transformer-app.git
   cd csv-transformer-app
