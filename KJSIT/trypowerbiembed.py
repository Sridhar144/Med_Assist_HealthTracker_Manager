import requests
import json
# Set the AAD access token obtained in the previous step
aad_access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCIsImtpZCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZDM2ZTI3YTUtNjQxYi00M2Q0LTg3ZTYtNjg3ZThkYmQ4ZTIwLyIsImlhdCI6MTcxNTczOTY2NCwibmJmIjoxNzE1NzM5NjY0LCJleHAiOjE3MTU3NDM1NjQsImFpbyI6IkUyTmdZQkRhTVBtSTUxSTV0cHJrRnlhZmxndFlBZ0E9IiwiYXBwaWQiOiI4YTQ2YWJmZi02MzJhLTRmZmItOTEwZi0yNmJhNWQ5MmQ5YmUiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9kMzZlMjdhNS02NDFiLTQzZDQtODdlNi02ODdlOGRiZDhlMjAvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI0ODk5ODkyYS1jMmUxLTRlOTItOGZhZS1mZjk5Y2Y0NGFiM2QiLCJyaCI6IjAuQWI0QXBTZHUweHRrMUVPSDVtaC1qYjJPSUFrQUFBQUFBQUFBd0FBQUFBQUFBQUMtQUFBLiIsInN1YiI6IjQ4OTk4OTJhLWMyZTEtNGU5Mi04ZmFlLWZmOTljZjQ0YWIzZCIsInRpZCI6ImQzNmUyN2E1LTY0MWItNDNkNC04N2U2LTY4N2U4ZGJkOGUyMCIsInV0aSI6ImRORGs2MzNLRTBPMnRkQ1BGMnZOQUEiLCJ2ZXIiOiIxLjAifQ.Fsdwz22JLIvLqYBelnPab0UYHBZAzXmTLcKbPAPdmTpyuckyiAuF_WYHltUzpGEDmGLRfDCWGcsW7Tf8WV1lChT8YEIZpjRPJPm-6mFBL9cRxlwVMfddtWcv0jQ0ac20JwEBR2yAhiFySHJif9bNDiQklhAzSJiC31Aji4tMJr7c0plB4DKRpVqMGfpD4jsYWTa-FVLKfYHN_Go5Y1w53pcwIaIFC9ztxz7DVa81iz4QnJDVWKPUy1CZPGPdKTYPIARCN5BrhojuaOWJ5TMgEAvJ8dHfzZ1AyZNefnVb8ahw0cQVOSLFLvZz-DWkokdtk22dLtvvszZlcoCuQ7k3Ow"

# # Set the Power BI token endpoint URL
# token_endpoint = "https://api.powerbi.com/v1.0/myorg/token"

# # Set the headers for the request
# headers = {
#     "Authorization": f"Bearer {aad_access_token}",
#     "Content-Type": "application/json"
# }

# # Send the GET request to the Power BI token endpoint
# response = requests.get(token_endpoint, headers=headers)

# # Check the response status code
# if response.status_code == 200:
#     # Parse the response JSON
#     response_json = response.json()
    
#     # Extract the Power BI access token from the response JSON
#     powerbi_access_token = response_json["accessToken"]
    
#     # Print the Power BI access token
#     print(powerbi_access_token)
# else:
#     # Print the error message
#     print(response.text)


# Generate embed token for the given report
embed_token_url = f"https://api.powerbi.com/v1.0/myorg/groups/fc46d0ec-ff4d-48e2-bdbf-232747fd3709/reports/784d1e8d-c0e5-4344-8ac0-a7f43e96c6b0/GenerateToken"
headers = {
    'Authorization': 'Bearer ' + "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCIsImtpZCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZDM2ZTI3YTUtNjQxYi00M2Q0LTg3ZTYtNjg3ZThkYmQ4ZTIwLyIsImlhdCI6MTcxNTc0NTk4NiwibmJmIjoxNzE1NzQ1OTg2LCJleHAiOjE3MTU3NDk4ODYsImFpbyI6IkUyTmdZS2o3bTNKejErTkVqVm1NeVVKeGR2ZERBUT09IiwiYXBwaWQiOiI4YTQ2YWJmZi02MzJhLTRmZmItOTEwZi0yNmJhNWQ5MmQ5YmUiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9kMzZlMjdhNS02NDFiLTQzZDQtODdlNi02ODdlOGRiZDhlMjAvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI0ODk5ODkyYS1jMmUxLTRlOTItOGZhZS1mZjk5Y2Y0NGFiM2QiLCJyaCI6IjAuQWI0QXBTZHUweHRrMUVPSDVtaC1qYjJPSUFrQUFBQUFBQUFBd0FBQUFBQUFBQUMtQUFBLiIsInN1YiI6IjQ4OTk4OTJhLWMyZTEtNGU5Mi04ZmFlLWZmOTljZjQ0YWIzZCIsInRpZCI6ImQzNmUyN2E1LTY0MWItNDNkNC04N2U2LTY4N2U4ZGJkOGUyMCIsInV0aSI6IlN3a1lqZmthQWtDUlIyelVmUmZ3QUEiLCJ2ZXIiOiIxLjAifQ.kN7kBR2hJTcZubBdnhfCSPBdf0Ymdq-qk8gyGTXgU40nce8vvI1lyUfE9Arp-Xfa4Ge-Q2yFHrOX83abBNdjLc3oyObLyDK0ssVUraVpohtQVR2iVuhhLlfC66bUjfrHKf4PHUtkNu6RpgSUAVnVFnEYfFn5ESdhUv21FWTIpf1Ez2T9k1YfJuguiT-GFMzdSYvtn-6uzY5CRUv2N_GrRUGt3SF0DfR0dqgwQaYF9mg49prCFJ2t7K-5Nc6BVK72ZAe0kAkdAdjbdtzriPWdRydPQLXVtxtKAH63L9ffhCntp7xq4foiO5JQNV2ZeekmVj-RZ6Hx3__a0b7sHOqclg",
    'Content-Type': 'application/json'
}
body = {
    'accessLevel': 'view'
}

response = requests.post(embed_token_url, headers=headers, data=json.dumps(body))
if response.status_code == 200:
    embed_token = response.json()['token']
    print (embed_token)
else:
    # Handle error
    print('rgeojgjjherjpj')
    print(response.text) 