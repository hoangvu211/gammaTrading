from polygon import RESTClient

client = RESTClient("H_h_CeRmnkS4YzmIUGeC6f1nNtWpxcGo")

aggs = []
for a in client.list_aggs(
    "AAPL",
    1,
    "minute",
    "2022-10-01",
    "2024-10-03",
    limit=50000,
):
    aggs.append(a)

print(aggs)