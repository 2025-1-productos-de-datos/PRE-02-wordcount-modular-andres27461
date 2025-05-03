import os
import subprocess

from ..src.wordcount import main


def test_migracion():

    try:
        subprocess.run(
            ["python", "-m", "homework", "data/input", "data/output"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    if not os.path.exists("data/output/results.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe.")

    results = {}
    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        results[key] = value

    assert results.get("computational", 0) == "3"
    assert results.get("analytics", 0) == "5"