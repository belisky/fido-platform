
from fastapi import FastAPI, Depends
from my_service.dependencies import get_token
from my_service.utils.logger import setup_logger
from fastapi import APIRouter
import requests


router = APIRouter(
    prefix="/argocd",
    tags=["argocd"],
)


logger = setup_logger()


app = FastAPI()
ARGOCD_API_URL = "https://argocd-server.argocd.svc.cluster.local/api/v1/applications"
ARGOCD_PROJECTS_URL = "https://argocd-server.argocd.svc.cluster.local/api/v1/projects"

def get_argocd_applications(token):     
    ARGOCD_AUTH_TOKEN = token
    try:
        headers = {"Authorization": f"Bearer {ARGOCD_AUTH_TOKEN}"}
        response = requests.get(ARGOCD_API_URL, headers=headers, verify=False)
        response.raise_for_status()
        apps = response.json()
        applications = [
            {
                "application_name": app["metadata"]["name"],
                "status": app["status"].get("sync", {}).get("status", "Unknown")
            }
            for app in apps.get("items", [])
        ]
        return {"applications": applications}
    except Exception as e:
        return {"error": str(e)}
    
def get_argocd_projects(token):
    ARGOCD_AUTH_TOKEN = token
    try:
        headers = {"Authorization": f"Bearer {ARGOCD_AUTH_TOKEN}"}
        response = requests.get(ARGOCD_PROJECTS_URL, headers=headers, verify=False)
        response.raise_for_status()
        projects = response.json()
        project_list = [
            {
                "project_name": project["metadata"]["name"],
                "namespace": project["metadata"].get("namespace", "argocd")
            }
            for project in projects.get("items", [])
        ]
        return {"projects": project_list}
    except Exception as e:
        return {"error": str(e)}


@router.get("/application_status")
async def application_status(token: str = Depends(get_token)):          
     return get_argocd_applications(token)

    # """Fetches all ArgoCD applications statuses

    # Args:
    #     token (str, optional): _description_. Defaults to Depends(get_token).

    # Returns:
    #     applications_data_conscise: concise application metadata json strucure
    # """
    ##############################################################################
    # Please complete the fastapi route to get applications metadata from argocd #
    # Make sure to use argocd token for authentication                           #  
    ##############################################################################
    # pass


@router.get("/list_projects")
async def list_projects(token: str = Depends(get_token)):
    return get_argocd_projects(token)
     
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

    # pass
