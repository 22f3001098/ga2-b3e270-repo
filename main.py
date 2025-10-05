from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List, Optional

# Load CSV once at startup
df = pd.read_csv("students.csv")

app = FastAPI()

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(None, alias="class")):
    """
    Returns all students or filters by classes if query parameters are provided.
    """
    filtered_df = df
    if class_:
        filtered_df = df[df['class'].isin(class_)]
    
    students = filtered_df.to_dict(orient="records")
    return {"students": students}
