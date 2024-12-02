from src.errors.BadRequest import BadRequest
from src.errors.InvalidType import InvalidType
from typing import Dict

def error_handler(error: Exception) -> Dict:

    if isinstance(error, (BadRequest, InvalidType)):   
        return {
            "status_code": error.statusCode,
            "body": {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        }
    
    return {
        "status_code": 500,
        "body": {
            "errors": [{
                "title": "Server Internal Error",
                "detail": str(error)
            }]
        }
    }  