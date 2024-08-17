import jwt


def read_token_unverified_header(token: str) -> dict:
    return jwt.get_unverified_header(token)


def read_token_data(token: str, algorithm: str = "HS256"):
    return jwt.decode(token, algorithms=[algorithm], options={"verify_signature": False})