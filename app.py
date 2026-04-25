from flask import Flask, request, render_template, send_file
import os

from src.loader import load_data
from src.cleaner import clean_data
from src.analyzer import generate_kpis, generate_insights
from src.visualizer import generate_charts
from src.report import generate_pdf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']

        if not file:
            return render_template("error.html", error="No file uploaded")

        path = os.path.join("data", file.filename)
        file.save(path)

        df = load_data(path)
        df = clean_data(df)

        kpis = generate_kpis(df)
        insights = generate_insights(df)
        charts = generate_charts(df)

        generate_pdf(kpis, insights, charts)

        return render_template("preview.html", kpis=kpis, insights=insights, charts=charts)

    except Exception as e:
        return render_template("error.html", error=str(e))


@app.route('/download')
def download():
    return send_file("reports/report.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)