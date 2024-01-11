from fastapi import APIRouter, Depends
from auth.auth_config import current_user
from .tasks import send_email_report




router = APIRouter(prefix="/report")


@router.get("/send_email")
def get_report(user=Depends(current_user)):
    send_email_report.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }