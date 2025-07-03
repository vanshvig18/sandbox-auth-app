import pandas as pd

def handle_uploaded_file(file):
    if file.name.endswith('.txt') or file.name.endswith('.mdv'):
        return file.read().decode('utf-8')
    elif file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        return pd.read_excel(file)
    else:
        return "Unsupported format"
