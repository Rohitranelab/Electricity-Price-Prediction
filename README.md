<div align="center">

# ⚡ Electricity Price Prediction

### End-to-End Machine Learning Pipeline for Forecasting Electricity Market Prices

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9.0-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![DVC](https://img.shields.io/badge/DVC-Data%20Version%20Control-945DD6?style=flat&logo=dvc&logoColor=white)](https://dvc.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Rohitranelab/Electricity-Price-Prediction?style=social)](https://github.com/Rohitranelab/Electricity-Price-Prediction/stargazers)

</div>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Demo](#-demo)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Workflow](#-workflow)
- [Dataset](#-dataset)
- [Data Preprocessing](#-data-preprocessing)
- [Models Used](#-models-used)
- [Model Performance](#-model-performance)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Prediction](#-example-prediction)
- [Configuration](#-configuration)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)
- [Why This Project Stands Out](#-why-this-project-stands-out)

---

## 🎯 Project Overview

**Electricity Price Prediction** is a complete, reproducible machine learning pipeline that predicts electricity market prices (`SMPEP2`) using historical weather, demand, and grid data such as system load, wind production forecasts, CO₂ intensity, and temperature.

**Why it matters:**
- Electricity prices are highly volatile and influenced by weather, renewable generation, and demand — accurate forecasts help utilities, traders, and grid operators plan more effectively.
- Reliable price forecasting supports smarter energy trading, demand-response planning, and renewable energy integration.

**Real-world applications:**
- Energy trading and market bidding strategy
- Grid load balancing and demand forecasting
- Renewable energy (wind) production planning
- Cost optimization for large-scale energy consumers

**Expected users:**
- Data scientists / ML engineers exploring time-series and regression pipelines
- Energy analysts and grid operators
- Recruiters and reviewers evaluating end-to-end MLOps practices

> 💡 **Note:** This project uses a real-world Irish electricity market dataset (SEM — Single Electricity Market) covering weather and grid metrics.

---

## 🎥 Demo

> 📸 *Add a screenshot of the web app here*
> `![App Screenshot](static/demo-screenshot.png)`

> 🎬 *Add a GIF walkthrough of the prediction flow here*

> 🌐 *Add a live deployment link here (if hosted)*

The project ships with a lightweight **Flask web app** (`app.py` + `templates/index.html`) where users can input weather and grid parameters and get an instant price prediction.

---

## ✨ Features

- ✅ Automated data ingestion from a remote CSV source
- ✅ Data cleaning & preprocessing pipeline
- ✅ Feature-based regression modeling
- ✅ Model training with `RandomForestRegressor`
- ✅ Model evaluation with multiple regression metrics
- ✅ Experiment tracking & metrics logging with **DVCLive**
- ✅ Fully reproducible pipeline via **DVC** (`dvc.yaml` / `dvc.lock`)
- ✅ Flask-based prediction web interface
- ✅ Dockerized for easy deployment
- ✅ Modular, stage-based project architecture

---

## 🛠 Tech Stack

**Languages**
- Python 3.13

**Libraries**
- pandas
- scikit-learn (`1.9.0`)

**Frameworks**
- Flask (web application)
- Gunicorn (production WSGI server)

**MLOps / Experiment Tracking**
- DVC (Data Version Control) — pipeline orchestration
- DVCLive — metrics & experiment logging

**Deployment**
- Docker

**Version Control**
- Git & GitHub

> ℹ️ No deep learning framework (TensorFlow/PyTorch) is used — this project is a classical ML regression pipeline built on scikit-learn.

---

## 📂 Project Structure

```
Electricity-Price-Prediction/
│
├── src/                          # Core ML pipeline source code
│   ├── data_ingestion.py         # Downloads raw data & splits train/test
│   ├── data_preprocessing.py     # Cleans & numeric-casts data
│   ├── model_building.py         # Trains RandomForestRegressor model
│   └── model_evaluation.py       # Evaluates model & logs metrics via DVCLive
│
├── static/
│   └── style.css                 # Styling for the Flask web app
│
├── templates/
│   └── index.html                # Web UI for entering inputs & viewing predictions
│
├── dvclive/                       # DVCLive experiment tracking outputs
│   ├── metrics.json               # Logged evaluation metrics
│   └── plots/                     # Auto-generated metric plots
│
├── .dvc/                          # DVC internal configuration
├── .dvcignore                     # Files ignored by DVC
├── .gitignore                     # Files ignored by Git
│
├── app.py                         # Flask application entry point
├── dvc.yaml                       # DVC pipeline stage definitions
├── dvc.lock                       # DVC pipeline lock file (hashes & outputs)
├── Dockerfile                     # Container build instructions
├── requirements.txt                # Python dependencies
├── LICENSE                        # MIT License
└── README.md                      # Project documentation
```

---

## 🔄 Workflow

```
Data Ingestion (remote CSV → train/test split)
        ↓
Data Preprocessing (cleaning, numeric coercion, missing-value removal)
        ↓
Model Building (RandomForestRegressor training)
        ↓
Model Evaluation (metrics computed & logged via DVCLive)
        ↓
Prediction (served through Flask web app)
```

---

## 📊 Dataset

| Detail | Description |
|---|---|
| **Source** | [amankharwal/Website-data — `electricity.csv`](https://raw.githubusercontent.com/amankharwal/Website-data/master/electricity.csv) (fetched automatically by `data_ingestion.py`) |
| **Domain** | Irish electricity market — weather & grid metrics |
| **Target Variable** | `SMPEP2` (System Marginal Price) |
| **Key Features** | `Day`, `Month`, `ForecastWindProduction`, `SystemLoadEA`, `ORKTemperature`, `ORKWindspeed`, `CO2Intensity`, `ActualWindProduction`, `SystemLoadEP2` |
| **Dropped Columns** | `DateTime`, `Holiday`, `HolidayFlag`, `DayOfWeek`, `WeekOfYear`, `Year`, `PeriodOfDay` |
| **Train/Test Split** | 80% train / 20% test (`random_state=42`) |
| **Missing Values** | Handled via row-wise removal (`dropna`) |

---

## 🔍 Exploratory Data Analysis

> 🔲 **Not implemented** — no dedicated EDA notebook or visualization scripts are present in this repository. Adding an EDA notebook (distribution plots, correlation heatmaps, seasonal trends) is listed under [Future Improvements](#-future-improvements).

---

## 🧹 Data Preprocessing

The pipeline applies the following preprocessing steps (`src/data_preprocessing.py`):

- **Missing Value Handling:** Rows containing any null values are dropped (`dropna()`), applied both before and after type coercion
- **Type Coercion:** All columns are forced to numeric types using `pd.to_numeric(..., errors='coerce')`, converting invalid/non-numeric entries to `NaN` (subsequently dropped)
- **Encoding:** Not required — irrelevant categorical columns (e.g., `Holiday`, `DayOfWeek`) are dropped during ingestion rather than encoded
- **Scaling:** *Not implemented* — Random Forest models do not require feature scaling
- **Feature Selection:** Handled implicitly by dropping non-predictive columns (`DateTime`, `HolidayFlag`, etc.) during ingestion
- **Outlier Treatment:** *Not implemented*
- **Train/Test Split:** Performed during ingestion stage — 80/20 split with a fixed random seed for reproducibility

---

## 🤖 Models Used

| Model | Purpose |
|---|---|
| **Random Forest Regressor** | Final model — predicts electricity price (`SMPEP2`) |

**Hyperparameters used:**
- `n_estimators = 500`
- `n_jobs = -1`
- `random_state = 42`

---

## 📈 Model Performance

Metrics logged from the most recent evaluation run (`dvclive/metrics.json`):

| Metric | Score |
|---|---|
| **R² Score** | 0.5962 |
| **Mean Absolute Error (MAE)** | 8.3033 |
| **Mean Squared Error (MSE)** | 388.2748 |
| **Root Mean Squared Error (RMSE)** | 19.7047 |

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/Rohitranelab/Electricity-Price-Prediction.git

# 2. Navigate into the project directory
cd Electricity-Price-Prediction

# 3. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### Run the full ML pipeline (DVC)

```bash
dvc repro
```

This executes all stages in order: `data_ingestion → data_preprocessing → model_building → model_evaluation`.

### Run individual stages manually

```bash
python src/data_ingestion.py
python src/data_preprocessing.py
python src/model_building.py
python src/model_evaluation.py
```

### Launch the Flask web app

```bash
python app.py
```

Then open your browser at:

```
http://127.0.0.1:5000
```

### Run with Docker

```bash
# Build the image
docker build -t electricity-price-prediction .

# Run the container
docker run -p 5000:5000 electricity-price-prediction
```

---

## 🔮 Example Prediction

**Input (via web form):**

| Field | Value |
|---|---|
| Day | 15 |
| Month | 6 |
| Forecast Wind Production | 450.0 |
| System Load EA | 3200.0 |
| ORK Temperature | 14.5 |
| ORK Windspeed | 12.0 |
| CO2 Intensity | 420.0 |
| Actual Wind Production | 430.0 |
| System Load EP2 | 3150.0 |
| SMPEP2 (reference) | 55.0 |

**Output:**

```
Predicted Electricity Price: 52.14
```


---

## 🖼 Visualizations

> 📊 *Add plots here, e.g. feature importance chart, actual vs. predicted price plot, or DVCLive-generated metric trend plots from `dvclive/plots/`.*

---

## 🔧 Configuration

Key configurable parameters (currently set directly in source files):

| Parameter | Location | Default |
|---|---|---|
| Data source URL | `src/data_ingestion.py` | Remote CSV (amankharwal/Website-data) |
| Train/test split ratio | `src/data_ingestion.py` | 0.8 / 0.2 |
| Random seed | `src/data_ingestion.py`, `model_building.py` | 42 |
| Model | `src/model_building.py` | `RandomForestRegressor` |
| `n_estimators` | `src/model_building.py` | 500 |
| Target column | `src/model_building.py`, `model_evaluation.py` | `SMPEP2` |
| Flask port | `app.py` | 5000 |

---

## 🗺 Future Improvements

- [ ] Web deployment (Render / AWS / Azure / GCP)
- [ ] `params.yaml`-based configuration for DVC pipeline parameters
- [ ] Hyperparameter tuning (GridSearchCV / Optuna)
- [ ] Baseline model comparison (Linear Regression, XGBoost)
- [ ] Dedicated EDA notebook with visual insights
- [ ] CI/CD pipeline for automated testing & deployment
- [ ] Model monitoring & drift detection in production
- [ ] Model explainability with SHAP / LIME
- [ ] Unit tests for pipeline stages
- [ ] API endpoint (REST/JSON) in addition to the HTML form

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create a new branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** and commit: `git commit -m "Add your feature"`
4. **Push** to your branch: `git push origin feature/your-feature-name`
5. **Open a Pull Request** describing your changes

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Rohit Rane**

- GitHub: [@Rohitranelab](https://github.com/Rohitranelab)

---

## 🙏 Acknowledgements

- Dataset sourced from [amankharwal/Website-data](https://github.com/amankharwal/Website-data)
- Built with [scikit-learn](https://scikit-learn.org/), [pandas](https://pandas.pydata.org/), and [Flask](https://flask.palletsprojects.com/)
- Experiment tracking powered by [DVC](https://dvc.org/) and [DVCLive](https://dvc.org/doc/dvclive)

---

## 🌟 Why This Project Stands Out

> ✔ End-to-end ML pipeline — from raw data to a deployable web app
> ✔ Clean, modular architecture (`src/` stage separation)
> ✔ Production-ready structure with Docker & Gunicorn support
> ✔ Reproducible experiments via DVC pipeline definitions
> ✔ Automated metrics tracking with DVCLive
> ✔ Professional documentation
> ✔ Well-organized, scalable repository layout