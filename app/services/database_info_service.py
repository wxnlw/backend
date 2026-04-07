from pathlib import Path

from sqlalchemy import Engine, text


def load_database_info(engine: Engine) -> tuple[str, str, str]:
    driver = engine.dialect.name

    if driver == "sqlite":
        with engine.connect() as connection:
            server_version = str(connection.execute(text("SELECT sqlite_version()")).scalar_one())

        db_path = engine.url.database
        if not db_path:
            database_name = ":memory:"
        else:
            database_name = Path(db_path).name
        return driver, server_version, database_name

    with engine.connect() as connection:
        row = connection.execute(
            text("SELECT version() AS server_version, current_database() AS database_name")
        ).mappings().one()

    server_version = str(row["server_version"])
    database_name = str(row["database_name"])
    return driver, server_version, database_name
