from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.user import LoginRequest, RefreshRequest, UserOut

router = APIRouter()


# =========================
# LOGIN
# =========================
@router.post("/login")
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    """
    TEMP TEST LOGIN
    """

    print("LOGIN HIT")
    print(payload.email)

    # Check if user exists
    result = await db.execute(
        select(User).where(
            User.email == payload.email,
            User.is_active == True
        )
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    # TEMP SUCCESS RESPONSE
    return {
        "access_token": "testtoken",
        "refresh_token": "testrefresh",
        "token_type": "bearer",
        "user_email": user.email
    }


# =========================
# REFRESH
# =========================
@router.post("/refresh")
async def refresh_token(payload: RefreshRequest):
    return {
        "access_token": "newtesttoken",
        "refresh_token": "newrefreshtoken",
        "token_type": "bearer",
    }


# =========================
# ME
# =========================
@router.get("/me")
async def get_me():
    return {
        "id": "test-user",
        "email": "admin@yourbusiness.com",
        "role": "admin"
    }
