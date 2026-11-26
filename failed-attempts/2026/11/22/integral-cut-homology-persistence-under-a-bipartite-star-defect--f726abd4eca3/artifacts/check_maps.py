"""Direct mod-two chain-map test for a natural star-edge deletion filtration."""
import itertools,math,json

def tri_conn(T,adj):
    a,b,c=T
    return int(b in adj[a])+int(c in adj[a])+int(c in adj[b])>=2

def faces(a,b,t):
    n=a+b; adj=[set() for _ in range(n)]
    for u in range(a):
        for v in range(b):
            if u==0 and v<t:continue
            adj[u].add(a+v);adj[a+v].add(u)
    bad=[sum(1<<v for v in T) for T in itertools.combinations(range(n),3) if not tri_conn(T,adj)]
    return {F for F in range(1<<n) if all((F&B)!=B for B in bad)}

def rank(vecs):
    piv={}
    for x in vecs:
        while x:
            k=x.bit_length()-1
            if k in piv:x ^= piv[k]
            else:piv[k]=x;break
    return len(piv)

def data(K,d):
    lo=sorted(F for F in K if F.bit_count()==d)
    hi=sorted(F for F in K if F.bit_count()==d+1)
    xp=sorted(F for F in K if F.bit_count()==d+2)
    lo_ix={F:i for i,F in enumerate(lo)}
    hi_ix={F:i for i,F in enumerate(hi)}
    def boundary(F,ix):
        out=0
        for v in range(F.bit_length()):
            if F>>v&1:out ^=1<<ix[F^(1<<v)]
        return out
    cols=[boundary(F,lo_ix) for F in hi]
    piv={};kern=[]
    for j,col in enumerate(cols):
        x=col;co=1<<j
        while x:
            k=x.bit_length()-1
            if k in piv:
                xx,cc=piv[k];x^=xx;co^=cc
            else:
                piv[k]=(x,co);break
        if x==0:kern.append(co)
    bounds=[boundary(F,hi_ix) for F in xp]
    return hi,kern,bounds

def check(a,b):
    out=[]
    for t in range(1,b):
        smaller=faces(a,b,t)
        larger=faces(a,b,t-1)
        assert smaller<=larger
        for dim in (1,3):
            hi,Ks,_=data(smaller,dim)
            hi_big,_,bounds_big=data(larger,dim)
            idx_big={F:j for j,F in enumerate(hi_big)}
            remap=[idx_big[f] for f in hi]
            imgs=[]
            for x in Ks:
                y=0
                for j,k in enumerate(remap):
                    if x>>j&1:y ^=1<<k
                imgs.append(y)
            imrank=rank(bounds_big+imgs)-rank(bounds_big)
            q=lambda t: math.comb(a-2,2)*math.comb(b-1,2)+(a-2)*(math.comb(b-t-1,2) if b-t-1>=2 else 0)
            target=t-1 if dim==1 else q(t)
            assert imrank==target,(a,b,t,dim,imrank,target)
            out.append((a,b,t,dim,imrank))
    return out

def main():
    out=[]
    for a in range(3,6):
        for b in range(3,6):out.extend(check(a,b))
    print(json.dumps({'status':'PASS','homology_inclusion_maps':len(out),'range':'3<=a,b<=5, 1<=t<b','examples':[x for x in out if x[:3] in [(4,4,1),(4,4,2),(5,5,3)]]},indent=2))
if __name__=='__main__':main()
