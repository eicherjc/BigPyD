def catalog(BidSess):
    r = BidSess.request("GET", url="https://localhost/api/v1/data-catalog/?format=json", headers=BidSess.headers, verify=False)
    return r.json()