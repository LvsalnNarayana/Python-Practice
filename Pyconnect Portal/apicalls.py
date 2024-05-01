import requests


def getAllUsers():
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    return users_response.json()


def getUserById(userId):
    user_by_id_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{userId}"
    )
    return user_by_id_response.json()


def getAllPosts():
    posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return posts_response.json()


def getPostsByUserId(userId):
    posts_by_userid_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{userId}/posts"
    )
    return posts_by_userid_response.json()


def getCommentsByPostId(postId):
    comments_by_postid_response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{postId}/comments"
    )
    return comments_by_postid_response.json()
