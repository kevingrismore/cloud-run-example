from prefect import flow
from prefect_gcp import BigQueryWarehouse


@flow(log_prints=True)
def query_bigquery(corpus: str, min_word_count: int):
    with BigQueryWarehouse.load("my-warehouse") as warehouse:
        operation = """
            SELECT word, word_count
            FROM `bigquery-public-data.samples.shakespeare`
            WHERE corpus = %(corpus)s
            AND word_count >= %(min_word_count)s
            ORDER BY word_count DESC
            LIMIT 6;
        """
        parameters = {
            "corpus": corpus,
            "min_word_count": min_word_count,
        }
        for _ in range(0, 3):
            result = warehouse.fetch_many(operation, parameters=parameters, size=2)
            print(result)


if __name__ == "__main__":
    query_bigquery("romeoandjuliet", 250)
