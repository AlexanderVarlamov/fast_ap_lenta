import uvicorn
from fastapp import get_app

app = get_app()

if __name__ == '__main__':
    uvicorn.run(app, port=5008, log_level='debug')