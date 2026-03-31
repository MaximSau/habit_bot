import os

class Config:
    def __init__(self) -> None:
        self.db_user = os.getenv("DB_USER", "postgres")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME", "db")
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_port = os.getenv("DB_PORT", "5432")
        self.bot_token = os.getenv("BOT_TOKEN")
        self.env = os.getenv("ENV", "dev")

        self._validate()

    def get_db_connection_string(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    def _validate(self) -> None:
        if not self.db_password:
            raise ValueError("DB_PASSWORD environment variable is not set")

        if not self.bot_token:
            raise ValueError("BOT_TOKEN environment variable is not set")
