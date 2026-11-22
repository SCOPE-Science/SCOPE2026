"""Independently constructed adjacency, bit-mask update, Kahn cycle peeling."""
import json,collections,hashlib

n=14
pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
attachment=[10,11,12,13,13,13]

def make(switched):
    A=[0]*n
    def add(a,b):
        A[a]|=1<<b;A[b]|=1<<a
    for j,(a,b) in enumerate(pairs):
        if switched: a,b=tuple(z for z in range(4) if z not in (a,b))
        add(a,4+j);add(b,4+j)
    for d,e in enumerate(attachment,4):add(d,e)
    for a,b in ((10,11),(10,12),(11,12)):add(a,b)
    assert all(m.bit_count()==3 for m in A)
    return A

def evaluate(switched):
    A=make(switched);count=1<<n
    transitions=[0]*count;indeg=[0]*count
    for x in range(count):
        y=0
        for v in range(n):
            if (A[v]&x).bit_count() > 1:y|=1<<v
        transitions[x]=y
        indeg[y]+=1
    queue=collections.deque(v for v in range(count) if indeg[v]==0)
    peeled=[]
    while queue:
        a=queue.popleft();peeled.append(a)
        b=transitions[a];indeg[b]-=1
        if indeg[b]==0:queue.append(b)
    periods=[0]*count;depths=[0]*count
    for v in range(count):
        if indeg[v]<=0 or periods[v]:continue
        cyc=[];w=v
        while not periods[w]:
            periods[w]=-1;cyc.append(w);w=transitions[w]
        assert w==v
        p=len(cyc)
        for z in cyc:periods[z]=p
    for x in reversed(peeled):
        nxt=transitions[x]
        periods[x]=periods[nxt]
        depths[x]=depths[nxt]+1
    classes=collections.Counter(zip(periods,depths))
    assert sum(classes.values())==count
    assert set(periods)=={1,2}
    h=hashlib.sha256(bytes(16*p+d for p,d in zip(periods,depths))).hexdigest()
    return {"classes":{f"{p}:{d}":classes[p,d] for p,d in sorted(classes)},
            "fixed_points":classes[1,0],"primitive_two_cycles":classes[2,0]//2,
            "fixed_basin":sum(v for (p,d),v in classes.items() if p==1),
            "max_entry":max(depths),"max_entry_witness":depths.index(max(depths)),
            "classification_sha256":h}

if __name__=='__main__':
    print(json.dumps({"G":evaluate(False),"H":evaluate(True)},sort_keys=True,indent=2))
