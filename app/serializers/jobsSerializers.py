from app.serializers.userSerializers import embeddedUserResponse


def jobEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "job_name": post["job_name"],
        "company_name": post["company_name"],
        "job_full_text": post["job_full_text"],
        "post_url": post["post_url"],
        "post_apply_url": post["post_apply_url"],
    }


def populatedJobEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "job_name": post["job_name"],
        "company_name": post["company_name"],
        "job_full_text": post["job_full_text"],
        "post_url": post["post_url"],
        "post_apply_url": post["post_apply_url"],
    }


def jobListEntity(posts) -> list:
    return [populatedJobEntity(post) for post in posts]
