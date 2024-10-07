'''
 for a set of elements in an array with the shape [10, "google.com"]
 being the first element the number of hit for the second the domain
 get any sub domain in a given list of domains and the number of the
 specific subdomain hist, order does not matter:  

 result:
 [
   [10, "jsfiddle.com"], 
   [20, "maps.google.com"],
   [30, "photos.google.com"],
   [50, "google.com"],
   [60, "com"],
 ]
'''

Domain = list[int, str]
Result = dict[str, int]

data: [Domain] = [
    [10, "jsfiddle.com"],
    [20, "maps.google.com"],
    [30, "photos.google.com"]
] 

def getDicFromList(input: [Domain]) -> Result:
    return { key: value for [value, key] in input }

def getSubDomainsRecursively(input: list[str], acc: Result, ref: Result) -> Result: 
    domainName = '.'.join(input)
    result = acc.copy()
    domain = result.get(domainName)

    if(len(input) == 0):
        return result

    if(domain is None):
        domain = 0
        for k, v in ref.items():
            if (domainName in k):
                domain = domain + v

        result[domainName] = domain
        input.pop(0)
        return getSubDomainsRecursively(input, result, ref)

    return result


def main():
    obj = getDicFromList(data)
    result: Result;

    for k, v in obj.items():
        subDomains = k.split('.')
        result = getSubDomainsRecursively(subDomains[1:len(subDomains)], obj, obj)

    print(result)

main()
