import json

from src.models.pydantic import BenchmarkResultsBatch


def load_test_data(file_path: str) -> BenchmarkResultsBatch:
    """
    The method is designed to load test data from json file in DEBUG mode
    """
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
    return BenchmarkResultsBatch(**data)
