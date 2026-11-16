"""Independent transfer calculation in Z[z]/(z^3-1) of ternary Fourier counts.
No enumeration of proper colourings; uses path transfer and integer convolution.
"""
from itertools import combinations_with_replacement,product
import json

def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def shift(a,k):return tuple(a[(j-k)%3] for j in range(3))
def conv(a,b):return tuple(sum(a[i]*b[(j-i)%3] for i in range(3)) for j in range(3))
ONE=(1,0,0);ZERO=(0,0,0)

def spectrum(lengths):
    N=sum(lengths)-1
    # Branch labels: terminal vertices 0 and 1, disjoint internal vertices.
    paths=[];node=2
    for L in lengths:
        p=list(range(node,node+L-1));node+=L-1;paths.append(p)
    assert node==N
    def path_factor(p,left,right,k):
        # Transport along internal vertices followed by the terminal right.
        d=[ZERO,ZERO,ZERO];d[left]=ONE
        for vertex in p:
            nd=[ZERO,ZERO,ZERO]
            for previous in range(3):
                for colour in range(3):
                    if previous!=colour:
                        nd[colour]=plus(nd[colour],shift(d[previous],k[vertex]*colour))
            d=nd
        z=ZERO
        for previous in range(3):
            if previous!=right:z=plus(z,d[previous])
        return z
    out=[]
    for k in product(range(3),repeat=N):
        ans=ZERO
        for left in range(3):
            for right in range(3):
                z=ONE
                for p in paths:z=conv(z,path_factor(p,left,right,k))
                ans=plus(ans,shift(z,k[0]*left+k[1]*right))
        out.append(ans)
    return out

def run():
    summary=[]
    for lengths in combinations_with_replacement(range(2,8),3):
        if sum(lengths)>9:continue
        N=sum(lengths)-1
        f=spectrum(lengths)
        proper=sum(f[0])
        degree=[0]*(N+1)
        for k,v in zip(product(range(3),repeat=N),f):
            z=(v[0]==v[1]==v[2]);bal=(sum(k)%3==0)
            assert z if not bal else True
            if z and bal:degree[sum(t!=0 for t in k)]+=1
        extra=sum(degree);rank=3**(N-1)-extra
        assert (extra,proper)==((584,162) if lengths==(2,3,4) else (0,proper))
        summary.append({'paths':list(lengths),'n':N,'proper':proper,
                        'balanced_zeros':extra,'nonzero_multipliers':rank,
                        'zero_by_degree':degree})
    assert len(summary)==7
    return summary

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,separators=(',',':')))
