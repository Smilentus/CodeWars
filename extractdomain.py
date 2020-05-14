# My implementation
def domain_name(url):
    nurl = url.replace('www.', '').replace('http://', '').replace('https://', '')
    return nurl[:nurl.index('.')]

# Best Solution
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]