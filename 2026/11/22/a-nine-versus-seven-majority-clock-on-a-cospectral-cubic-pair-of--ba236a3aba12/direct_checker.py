"""Independent direct trajectory census; Python 3 standard library only."""
import collections, hashlib, json

G_EDGES = [(0,4),(0,5),(0,6),(1,4),(1,7),(1,8),
           (2,5),(2,7),(2,9),(3,6),(3,8),(3,9),
           (4,10),(5,11),(6,12),(7,13),(8,13),(9,13),
           (10,11),(10,12),(11,12)]
H_EDGES = [(0,7),(0,8),(0,9),(1,5),(1,6),(1,9),
           (2,4),(2,6),(2,8),(3,4),(3,5),(3,7),
           (4,10),(5,11),(6,12),(7,13),(8,13),(9,13),
           (10,11),(10,12),(11,12)]

def calculate(edges):
    nbrs = [[] for _ in range(14)]
    for a,b in edges:
        nbrs[a].append(b); nbrs[b].append(a)
    assert all(len(r)==3 for r in nbrs)
    def update(x):
        value=0
        for v, N in enumerate(nbrs):
            if sum(1 for j in N if x & (1<<j)) >= 2:
                value |= 1 << v
        return value
    data=[]
    counts=collections.Counter()
    witness={}
    for x in range(1<<14):
        seen={}
        y=x
        while y not in seen:
            seen[y]=len(seen)
            y=update(y)
        depth=seen[y]
        period=len(seen)-depth
        assert period in (1,2)
        counts[(period,depth)]+=1
        data.append((period,depth))
        witness[(period,depth)]=x
    h=hashlib.sha256(bytes(16*period+depth for period,depth in data)).hexdigest()
    return {"classes":{f"{p}:{d}":counts[(p,d)] for p,d in sorted(counts)},
            "fixed_points":counts[(1,0)],"primitive_two_cycles":counts[(2,0)]//2,
            "fixed_basin":sum(v for (p,d),v in counts.items() if p==1),
            "max_entry":max(d for p,d in counts),
            "max_entry_witness":min(x for x in range(1<<14) if data[x][1]==max(d for p,d in counts)),
            "classification_sha256":h}

if __name__=='__main__':
    print(json.dumps({"G":calculate(G_EDGES),"H":calculate(H_EDGES)},sort_keys=True,indent=2))
