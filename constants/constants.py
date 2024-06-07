from pathlib import Path

# Paths
HOME_DIR = Path.home()
PARSING_MODEL_DIR = HOME_DIR / ".local/share/bllipparser/GENIA+PubMed"

# Observation constants
CARDIOMEGALY = "Cardiomegaly"
ENLARGED_CARDIOMEDIASTINUM = "Enlarged Cardiomediastinum"
SUPPORT_DEVICES = "Support Devices"
NO_FINDING = "No Finding"
OBSERVATION = "observation"
CATEGORIES = [
    "No Finding", "Enlarged Cardiomediastinum", "Cardiomegaly", "Emphysema", "Fibrosis", "Hernia",
    "Lung Lesion", "Lung Opacity", "Edema", "Calcification", "Consolidation", "Mass",
    "Pneumonia", "Atelectasis", "Pneumothorax", "Pleural Effusion", "Tuberculosis", "Lung Parenchyma",
    "Pleural Other", "Air Bronchogram", "Fracture", "Support Devices"
]

# Numeric constants
POSITIVE = 1
NEGATIVE = 0
UNCERTAIN = -1

# Misc. constants
UNCERTAINTY = "uncertainty"
NEGATION = "negation"
REPORTS = "Reports"
