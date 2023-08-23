#!/usr/bin/env python
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from loguru import logger


uri = 'postgresql://finstar_user:finstar_pass@localhost:5432/finstar_db'

engine = create_engine(uri)


def init_db():
    logger.debug(f'Read file')
    df = pd.read_excel('data/test_sample.xlsx')

    df['week_number'] = df.rep_date.dt.isocalendar().week
    
    table_name = 'test_sample_data'
    logger.debug(f'Start init db')
    pg_conn = engine.connect()

    df.to_sql(table_name, pg_conn,
              if_exists='append', index=False,
              chunksize=1000, method='multi')

    pg_conn.close()


if __name__ == '__main__':
    init_db()
