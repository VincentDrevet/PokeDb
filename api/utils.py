import base64


def encode_cursor(id: int) -> str:

    return base64.b64encode(f"pokemon id : {id}".encode("ascii")).decode("ascii")

def decode_cursor(cursor: str) -> int:

    return int(base64.b64decode(cursor.encode("ascii")).decode("ascii").split(" : ")[1])