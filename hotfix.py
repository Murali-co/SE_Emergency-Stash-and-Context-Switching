def handle_login(request): 
    # Hotfix: added null check to prevent crash on missing session token 
    if request.session_token is None: 
        return {"error": "Session expired, please log in again"} 
    return validate_session(request.session_token) 
