from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from textwrap import dedent
from mimetypes import guess_type
from os.path import isfile

app = FastAPI(title="api app")


#app.mount("/site", StaticFiles(directory="site", html = True), name="site")

@app.get("/site/{filename}")
async def get_site(filename):
  """Serve up static files"""
  filename = './site/' + filename

  if not isfile(filename):
    return Response(status_code=404)

  with open(filename) as f:
    content = f.read()

  content_type, _ = guess_type(filename)
  return Response(content, media_type=content_type)

@app.get("/", response_class=HTMLResponse)
async def home():
    return dedent("""
            <html>
              <body>
                <h1> This is a test </h1>
              </body>
            </html>
            """)
    
@app.get("/data")
async def data():
    return [{"name": "Empanada"}, {"name": "Arepa"}]

@app.get("/newlistitem", response_class=HTMLResponse)
async def newlistitem(nlines: int=0):
   return f"<li>new item {nlines} </li>"