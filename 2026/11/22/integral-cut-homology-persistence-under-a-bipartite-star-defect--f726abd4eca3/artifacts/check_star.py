"""Independent exact face enumerator and GF(2) boundary check for star-deleted bicliques."""
import itertools, math, json
from collections import Counter

def c(n,k):return math.comb(n,k) if n>=k>=0 else 0

def rank_mod2(cols):
    piv={};r=0
    for x in cols:
        while x:
            i=x.bit_length()-1
            if i not in piv:
                piv[i]=x;r+=1;break
            x^=piv[i]
    return r

def invariants(a,b,t):
    n=a+b
    adj=[set() for _ in range(n)]
    for x in range(a):
        for z in range(b):
            if x==0 and z<t:continue
            adj[x].add(a+z);adj[a+z].add(x)
    def connected_triple(triple):
        u,v,w=triple
        return sum(int(v in adj[u])+int(w in adj[u])+int(w in adj[v]) for _ in [0]) >= 2
    bad={sum(1<<v for v in ss) for ss in itertools.combinations(range(n),3) if not connected_triple(ss)}
    faces={0}
    for F in range(1,1<<n):
        if not any((F&tri)==tri for tri in bad):faces.add(F)
    # independent decomposition: X with deleted special vertex and link
    X=set()
    L=set()
    for F in range(1<<n):
        Ap=sum((F>>i)&1 for i in range(1,a))
        B0=sum((F>>(a+i))&1 for i in range(t,b))
        Bt=sum((F>>(a+i))&1 for i in range(t))
        if (F&1)==0 and Ap<=2 and B0+Bt<=2:X.add(F)
        if (F&1)==0 and Ap<=1 and ((B0<=2 and Bt==0) or (Ap==0 and B0+Bt==1 and Bt==1)):
            # above misses empty and no-A and B0 2? included
            L.add(F)
    modeled=X|{F|1 for F in L}
    assert modeled==faces, (a,b,t,len(modeled^faces), sorted(modeled^faces)[:7])
    fs=Counter(F.bit_count()-1 for F in faces)
    boundaries={}
    for d in range(1,max(fs)+1):
        lower=sorted(F for F in faces if F.bit_count()==d)
        higher=sorted(F for F in faces if F.bit_count()==d+1)
        idx={F:i for i,F in enumerate(lower)}
        cols=[]
        for F in higher:
            x=0
            for v in range(n):
                if F>>v&1:x^=1<<idx[F^(1<<v)]
            cols.append(x)
        boundaries[d]=rank_mod2(cols)
    # include dimension zero via connected component formula
    betti={}
    for d in range(max(fs)+1):
        betti[d]=fs[d] - boundaries.get(d,0) - boundaries.get(d+1,0)
    betti[0]-=1
    target={1:t,3:c(a-2,2)*c(b-1,2)+(a-2)*c(b-t-1,2)}
    assert all(betti.get(k,0)==target.get(k,0) for k in set(betti)|set(target)),(a,b,t,betti,target)
    return dict(a=a,b=b,t=t,faces=len(faces),dimension=max(fs),reduced_betti={str(k):v for k,v in betti.items() if v},target_3=target[3])

def main():
    out=[]
    for a in range(3,6):
        for b in range(3,6):
            for t in range(1,b):
                out.append(invariants(a,b,t))
    print(json.dumps({'status':'PASS','cases':len(out),'range':'3<=a,b<=5; 1<=t<b','total_faces':sum(v['faces'] for v in out),'sample':[v for v in out if (v['a'],v['b'],v['t']) in [(3,3,1),(4,4,1),(4,4,2),(5,5,3)]]},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
