from fastapi import FastAPI


app = FastAPI(
    title= "Project Management System API",
    version= "1.0.0"
)



@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "healthy"}