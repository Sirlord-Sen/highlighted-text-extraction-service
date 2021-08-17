def BuildResponse(user, cleanHighlights):

    return {
        'message': "success", 
        "data": {
            "user" : {
                "id": user,
                "highlights": cleanHighlights
            }
        }
    }