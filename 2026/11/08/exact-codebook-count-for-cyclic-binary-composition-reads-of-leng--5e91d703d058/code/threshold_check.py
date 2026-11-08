#!/usr/bin/env python3
"""Independent exhaustive check of three-vs-four composition spectra at short lengths."""
def signature(word, maxk):
    n=len(word); out=[]
    for k in range(1,maxk+1):
        counts=[0]*(k+1)
        for i in range(n):
            counts[sum(word[(i+j)%n] for j in range(k))]+=1
        out.extend(counts)
    return tuple(out)
for n in range(1,9):
    classes={}
    for x in range(1<<n):
        bits=[(x>>j)&1 for j in range(n)]
        s3=signature(bits,3); s4=signature(bits,4)
        classes.setdefault(s3,set()).add(s4)
    separated=sum(len(v)>1 for v in classes.values())
    assert (separated==0)==(n<=7),(n,separated)
    print(n, 'length-three classes',len(classes),'separated-by-four',separated)
print('SHARP_READ_THRESHOLD_OK')
