from datetime import datetime

from src.constants import TEST_DATA_FILE_PATH
from src.models.pydantic import ResultsAverageResponseModel
from src.operations.base_operation import BaseOperation
from src.utils import load_test_data


class GetResultsAverage(BaseOperation):
    """
    Operation to compute average benchmarking statistics for LLM responses.

    Args:
        start_time (datetime, optional): Start of the time range for filtering results.
        end_time (datetime, optional): End of the time range for filtering results.
    """

    def __init__(self, start_time: datetime = None, end_time: datetime = None):
        self.start_time = start_time
        self.end_time = end_time

    def execute(self) -> ResultsAverageResponseModel:
        data = load_test_data(TEST_DATA_FILE_PATH).benchmarking_results
        if self.start_time and self.end_time:
            data = self._filter_data_by_time_range(data)
        results = self._count_statistics(data)
        return ResultsAverageResponseModel(**results)

    def _count_statistics(self, data: list) -> dict:
        """
        Computes average values for key performance metrics from the given data.
        :param data: A list of benchmarking results.
        :return: A dictionary containing average statistics.
        """
        count = len(data)
        if count == 0:
            return {
                "average_token_count": 0.0,
                "average_time_to_first_token": 0.0,
                "average_time_per_output_token": 0.0,
                "average_total_generation_time": 0.0,
            }
        return {
            "average_token_count": sum(item.token_count for item in data) / count,
            "average_time_to_first_token": sum(
                item.time_to_first_token for item in data
            )
            / count,
            "average_time_per_output_token": sum(
                item.time_per_output_token for item in data
            )
            / count,
            "average_total_generation_time": sum(
                item.total_generation_time for item in data
            )
            / count,
        }

    def _filter_data_by_time_range(self, data: list) -> list:
        """
        Filters the benchmarking results by the specified time range.
        :param data: A list of benchmarking results.
        :return: Filtered list of results within the specified time range.
        """
        return [
            item for item in data if self.start_time <= item.timestamp <= self.end_time
        ]
