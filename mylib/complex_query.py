"""Connect to  database and query the database"""
import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

# complex query function
def complex_query():
    """
    Connect to laliga database and the epl database.
    Get the top 5 teams with the highest number of yellow cards from each table, both home and away.
    Join the two tables and sort by number of home goals.
    """
    load_dotenv()  # Load the environment variables from the .env file in the outer directory
    server = os.getenv("SERVER")
    database = os.getenv("DATABASE")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    driver = os.getenv("DRIVER")
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        # get sql query from sql file
        with open("mylib/complex_query.sql") as f:
            sql = f.read()
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        result = [(team, yellow_cards) for team, yellow_cards in result]
        df = pd.DataFrame(result, columns=["Team", "Total Yellow Cards"])
        df = df.sort_values(by="Total Yellow Cards", ascending=False)
        print("Top 10 teams with the highest number of yellow cards:")
        print(df)
        cursor.close()
    return "success"