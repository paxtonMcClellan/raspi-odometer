def load_mileage():
    try:
        with open("mileage.txt", "r") as f:
            return float(f.read())
    except:
        return 0.0


def save_mileage(miles):
    with open("mileage.txt", "w") as f:
        f.write(str(miles))