from app import create_app
import uvicorn
from config import settings

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app", 
        host=settings.HOST, 
        port=settings.PORT,
        reload=settings.DEBUG
    )
