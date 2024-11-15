from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
from typing import Annotated, Any, Dict
from requests import get, post

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: Annotated[str | None, Depends(oauth2_scheme)]):
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    url = f"http://user-service:8006/user_profile"
    headers = {"Authorization": f"Bearer {token}"}

    response = get(url, headers=headers)
<<<<<<< HEAD

=======
>>>>>>> 37deb645b9f12e3aa90dee167739129606757f1e
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    
    raise HTTPException(status_code=response.status_code, detail=f"{response.text}")
    
GetCurrentUserDep = Annotated[Dict[str, Any], Depends(get_current_user)]

def get_login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    url = f"http://user-service:8006/token"
    data = {
        "username":form_data.username,
        "password":form_data.password
    }
    response = post(url,data=data)
    if response.status_code == 200:
        return response.json()
    
    raise HTTPException(status_code=response.status_code,detail=f"{response.text}")

LoginForAccessTokenDep = Annotated[dict, Depends(get_login_for_access_token)]

def admin_required(current_user: Annotated[Dict[str, Any], Depends(get_current_user)]):
    print("Current User Data:", current_user)
    if current_user.get("role") != "admin":
<<<<<<< HEAD
        raise HTTPException(status_code=403, detail="Admin Privileges Required")
=======
<<<<<<<< HEAD:order-service/app/authentication/auth.py
        raise HTTPException(status_code=403, detail="Admin Privileges Required")
========
        raise HTTPException(status_code=403, detail="zAdmin privileges required")
>>>>>>>> 37deb645b9f12e3aa90dee167739129606757f1e:inventory-service/app/authentication/auth.py
>>>>>>> 37deb645b9f12e3aa90dee167739129606757f1e
    return current_user