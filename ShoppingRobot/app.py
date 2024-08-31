from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def make_clickable(val):
    if isinstance(val, str) and val.startswith('http'):
        return f'<a href="{val}" target="_blank">{val}</a>'
    return val

@app.route('/')
def index():
    # Load the Excel file
    xls = pd.ExcelFile("final_project.xlsx")  # Update with the actual path to your file
    
    # Read each sheet into a DataFrame
    df_amazon = pd.read_excel(xls, 'Amazon')
    df_flipkart = pd.read_excel(xls, 'Flipkart')

    # Apply the make_clickable function to URL columns (assuming they are named 'URL')
    if 'URL' in df_amazon.columns:
        df_amazon['URL'] = df_amazon['URL'].apply(make_clickable)
    if 'URL' in df_flipkart.columns:
        df_flipkart['URL'] = df_flipkart['URL'].apply(make_clickable)

    # Convert the DataFrames to HTML
    amazon_html = df_amazon.to_html(classes='table table-striped table-hover', index=False, escape=False)
    flipkart_html = df_flipkart.to_html(classes='table table-striped table-hover', index=False, escape=False)
    
    return render_template('index.html', amazon_data=amazon_html, flipkart_data=flipkart_html)

if __name__ == '__main__':
    app.run(debug=True)
