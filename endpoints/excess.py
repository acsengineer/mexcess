from fastapi import APIRouter
from fastapi import Request

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/excess",
    tags=["Excess"],
    responses={404: {"description": "Not found"}},
)

# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


#    @router.get("/")
#    async def root_redirect():
#        return RedirectResponse(url="/excess")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("excess.html", context={"request": request})
