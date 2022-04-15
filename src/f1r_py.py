from requests import get
from time import ctime

def error_log(error:str, function:str):
    Time = f"[{ctime()}]"
    open("f1r.log", "a+").write(f"{Time} - {function} - {error}\n")

def create_link(link:str,token:str,name="rand"):
    url = f"https://f1r.ir/api/new/{token}?url={link}&name={name}"
    try:
        response = get(url).json()
    except Exception as error:
        error_log(str(error), "create")
        return "error"

    if('description' in response):
        description = response['description']
    else:
        error_log("description no found", "create")
        return "description no found"
        
    if(description == "successful"):
        result = response["result"]
        result.pop("url")
        return result

    else:
        error_log(description, "create")
        return description

def get_view(name:str):
    url = f"https://f1r.ir/api/info?name={name}"
    try:
        response = get(url).json()
    except Exception as error:
        error_log(str(error), "create")
        return "error"

    if(not response["ok"]):
        if('description' in response):
            error_log(response['description'], "get")
            return response['description']
        else:
            return "description no found"

    else:
        return response["result"]
