import os
import cassio


def connect() -> None:
    """
    Initialize connection to Cassandra DB

    Args
    ----
        None
    Returns
    -------
        None
    """
    cassio.init(token=os.environ.get("ASTRA_DB_APPLICATION_TOKEN"),
                database_id=os.environ.get("ASTRA_DB_ID"))