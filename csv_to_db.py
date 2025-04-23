import polars as pl
import psycopg
from sqlalchemy import create_engine


db_secrets = {
    "user": "",
    "password": "",
    "name": ""
}

for key in db_secrets.keys():
    with open(f"./secrets/db_{key}.txt", "r") as file:
        db_secrets[key] = file.read().strip()


engine_url = f"postgresql+psycopg://{db_secrets['user']}:" + \
    f"{db_secrets['password']}@localhost/{db_secrets['name']}"



file_write_data = [
    pl.Series("player", ["Michael Jordan", "Dennis Rodman", "Scottie Pipen"], dtype=pl.String),
    pl.Series("number", [23, 91, 33], dtype=pl.UInt8),
    pl.Series("position", ["shooting guard", "power foward", "small foward"], dtype=pl.Categorical),
    pl.Series("weights", [215.03, 210.02, 220.01], dtype=pl.Float32)
]

write_file_df = pl.DataFrame(file_write_data)
write_file_df.write_csv("bulls.csv", separator=",")


file_read_df = pl.read_csv("bulls.csv", separator=",")

file_read_df.write_database(
    table_name="bulls",
    connection=engine_url,
    if_table_exists="replace"
)



engine = create_engine(engine_url)
with engine.connect() as conn:
    result_df = pl.read_database("SELECT * FROM bulls", conn)

print(result_df)
