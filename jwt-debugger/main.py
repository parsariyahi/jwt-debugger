import jwt

from utils import read_token_unverified_header, read_token_data

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJyb2xlIjoxLCJleHAiOjE3MjM4OTYyOTV9.BMsVdBuOABEkuxdTo8Q6e_BxLKc-LfamPharj1YCy60"
algorithm = "HS256"
keys = ["u~xzxdw%uhq3E-vL_f$yo+j|HX91"]


# print(
#     jwt.decode(token, algorithms=[algorithm], options={"verify_signature": False})
# )

print(read_token_data(token))

print(read_token_unverified_header(token))