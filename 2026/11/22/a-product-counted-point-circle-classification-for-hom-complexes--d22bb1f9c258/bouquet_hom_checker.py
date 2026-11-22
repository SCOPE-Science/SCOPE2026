from itertools import combinations, product
from collections import Counter, defaultdict

def sector_words(n,q):
    out=defaultdict(list)
    for k in range(n+1):
        wnum=2*k-n
        if wnum%q:continue
        w=wnum//q
        for inds in combinations(range(n),k):
            x=sum(1<<j for j in inds)
            out[w].append(x)
    return dict(out)

def states_and_edges(lengths,q):
    W=[sector_words(n,q) for n in lengths]
    all_data=[]
    for ws in product(*(list(x) for x in W)):
        vars=[W[i][w] for i,w in enumerate(ws)]
        verts=[(h,)+p for h in range(q) for p in product(*vars)]
        ids={v:i for i,v in enumerate(verts)}
        moves=[]
        for v in verts:
            h=v[0]; masks=list(v[1:]); neighbors=[]
            for i,n in enumerate(lengths):
                x=masks[i]
                for j in range(1,n):
                    if ((x>>(j-1))&1)!=((x>>j)&1):
                        y=masks.copy();y[i]=x^((1<<(j-1))|(1<<j))
                        neighbors.append(ids[(h,)+tuple(y)])
            sig=[]
            for i,n in enumerate(lengths):
                x=masks[i]
                a=(x&1)!=0
                b=((x>>(n-1))&1)!=0
                if a==b:break
                sig.append(a)
            if len(sig)==len(lengths) and len(set(sig))==1:
                y=[x^((1<<n-1)|1) for x,n in zip(masks,lengths)]
                hh=(h+(2 if sig[0] else -2))%q
                neighbors.append(ids[(hh,)+tuple(y)])
            moves.append(neighbors)
        e2i={}
        for i, nei in enumerate(moves):
            for j in nei:
                e2i[tuple(sorted((i,j)))]=0
        e2i={e:k for k,e in enumerate(e2i)}
        parent=list(range(len(verts)))
        def find(a):
            while parent[a]!=a:
                parent[a]=parent[parent[a]];a=parent[a]
            return a
        for a,b in e2i:parent[find(a)]=find(b)
        comp=Counter(find(i) for i in range(len(verts)))
        rank2=0; piv={};sqseen=set()
        for a,nei in enumerate(moves):
            for b,c in combinations(nei,2):
                ds=set(moves[b]).intersection(moves[c])
                for d in ds:
                    if d==a:continue
                    s=tuple(sorted((a,b,c,d)))
                    if s in sqseen:continue
                    sqseen.add(s)
                    edges=[(a,b),(a,c),(b,d),(c,d)]
                    bit=0
                    for e in edges:
                        bit^=1<<e2i[tuple(sorted(e))]
                    while bit:
                        j=bit.bit_length()-1
                        if j not in piv:
                            piv[j]=bit;rank2+=1;break
                        bit^=piv[j]
        b1=len(e2i)-len(verts)+len(comp)-rank2
        predicted_circle=all(abs(q*w)<n for w,n in zip(ws,lengths))
        predicted_c=(1 if q%2 else 2) if predicted_circle else q
        all_data.append((ws,len(verts),len(e2i),len(sqseen),len(comp),b1,predicted_c, predicted_c if predicted_circle else 0))
    return all_data

if __name__=='__main__':
  tested=0
  for lengths,q in [((6,6),5),((7,7),5),((5,7),5),((4,4),6),((6,6),6),((4,6),5),((8,4),6),((8,6),6),((4,4,4),5),((4,4,4),6),((6,6),7),((7,7),7),((5,6),6)]:
    d=states_and_edges(lengths,q)
    tested+=1
    failures=[e for e in d if e[4]!=e[6] or e[5]!=e[7]]
    assert not failures, (lengths,q,failures[:3])
    print('PASS', lengths, q, 'sectors',len(d),'vertices',sum(e[1] for e in d),'components',sum(e[4] for e in d),'H1_F2',sum(e[5] for e in d),flush=True)
  print("ALL_BOUQUET_HOM_TESTS_PASS cases="+str(tested))
