from deta import Deta


deta = Deta("projectKey")

users = deta.Base("users")

users.insert({
    "name": "ismats",
    "password":"abc"
})

fetch_res = users.fetch({"name":"ismats"})

for item in fetch_res.items:
    users.delete(item["key"])