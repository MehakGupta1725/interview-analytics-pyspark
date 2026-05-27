import pandas as pd
import random
from faker import Faker

fake = Faker()

categories = [
    "Technical",
    "HR",
    "System Design",
    "Data Science",
    "Cloud"
]

rows=[]

for i in range(100):

    rows.append({

        "Candidate":
        fake.first_name(),

        "Category":
        random.choice(categories),

        "Score":
        random.randint(50,100),

        "Confidence":
        random.randint(45,100),

        "Experience":
        random.randint(0,10),

        "Date":
        fake.date_between(
            start_date='-60d',
            end_date='today'
        )
    })

df=pd.DataFrame(rows)

df.to_csv(
    "sample_interview_data.csv",
    index=False
)

print(
    "Dataset Generated Successfully."
)