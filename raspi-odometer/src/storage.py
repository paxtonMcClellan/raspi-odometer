import os

MILEAGE_PATH = os.path.join(os.path.dirname(__file__), "mileage.txt")


def load_mileage():
    try:
        with open(MILEAGE_PATH, "r") as f:
            return float(f.read())
    except Exception:
        return 0.0


def save_mileage(miles):
    # ensure directory exists (should, since __file__ directory exists)
    with open(MILEAGE_PATH, "w") as f:
        f.write(str(miles))