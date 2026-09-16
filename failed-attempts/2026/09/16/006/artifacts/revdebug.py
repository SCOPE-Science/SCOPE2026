import itertools
from flipsearch import stacked_chain, faceset_of, find_moves, apply_rev, check_valid
d=4; t=2
facets,colors,n=stacked_chain(d,t)
faces=faceset_of(facets)
fwd,rev=find_moves(facets,faces)
print('nrev',len(rev))
from collections import Counter
c=Counter()
msgs={}
for (B,A) in rev[:12]:
    new=apply_rev(facets,B,A)
    ok,msg=check_valid(new,d,colors)
    c[(ok,msg)]+=1
    if not ok:
        # diagnose ridge counts
        from collections import Counter as C2
        rc=C2()
        for F in new:
            for v in F: rc[F-frozenset((v,))]+=1
        bad=[(r,v) for r,v in rc.items() if v!=2]
        print('B=',sorted(B),'A=',sorted(A),'msg reconstruction check; nbad ridges=',len(bad))
        for r,v in bad[:6]: print('   ridge',sorted(r),'count',v)
print(c)
