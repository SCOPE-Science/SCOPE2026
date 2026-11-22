#!/usr/bin/env python3
"""Independent direct path-layer rerouting verification for all two-fault pairs."""
from collections import deque


def geodesics(n):
    allpaths=[]
    def grow(v, path):
        if v==(1<<n)-1:
            allpaths.append(tuple(path))
            return
        for bit in range(n):
            if not ((v>>bit)&1):
                grow(v|(1<<bit),path+[v|(1<<bit)])
    grow(0,[0])
    return allpaths


def main():
    for n in range(2,7):
        paths=geodesics(n)
        npaths=len(paths)
        internals=[tuple(p[1:-1]) for p in paths]
        adj=[[] for _ in paths]
        for i in range(npaths):
            for j in range(i):
                if sum(x!=y for x,y in zip(internals[i],internals[j]))==1:
                    adj[i].append(j)
                    adj[j].append(i)
        all_masks=range(1,(1<<n)-1)
        invalid=[]
        fault_cases=0
        candidates=[()] + [(a,) for a in all_masks] + [(a,b) for a in all_masks for b in range(a+1,(1<<n)-1)]
        for F in candidates:
                fault_cases+=1
                good={i for i,p in enumerate(internals) if not any(f in p for f in F)}
                seen=set()
                parts=[]
                for root in good:
                    if root in seen:continue
                    seen.add(root)
                    q=[root]
                    for x in q:
                        for y in adj[x]:
                            if y in good and y not in seen:
                                seen.add(y)
                                q.append(y)
                    parts.append(len(q))
                if len(parts)!=1:
                    invalid.append((F,sorted(parts)))
        if n==3:
            assert len(invalid)==3,invalid # complementary singleton--doubleton pairs
        if n>=4:
            assert not invalid,invalid
        print('n=%d paths=%d fault_cases=%d disconnected_cases=%d' % (n,npaths,fault_cases,len(invalid)))
    print('DIRECT_CUBE_PATHS_OK')

if __name__=='__main__':
    main()
