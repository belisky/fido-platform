
from fastapi import FastAPI, Depends
from my_service.dependencies import get_token
from my_service.utils.logger import setup_logger
from fastapi import APIRouter


router = APIRouter(
    prefix="/arogocd",
    tags=["arogocd"],
)


logger = setup_logger()


app = FastAPI()



@router.get("/application_status")
async def application_status(token: str = Depends(get_token)):
    """Fetches all ArgoCD applications statuses

    Args:
        token (str, optional): _description_. Defaults to Depends(get_token).

    Returns:
        applications_data_conscise: concise application metadata json strucure
    """
    ##############################################################################
    # Please complete the fastapi route to get applications metadata from argocd #
    # Make sure to use argocd token for authentication                           #  
    ##############################################################################
    pass


@router.get("/list_projects")
async def list_projects(token: str = Depends(get_token)):
    """Fetches all argocd projects names and namespaces to which they are configured

    Args:
        token (str, optional): _description_. Defaults to Depends(get_token).
    Returns:
        projects_data_conscise: concise argocd projects metadata json strucure
    """

    ##########################################################################
    # Please complete the fastapi route to get projects metadata from argocd #
    # Make sure to use argocd token for authentication                       #  
    ##########################################################################

    pass
