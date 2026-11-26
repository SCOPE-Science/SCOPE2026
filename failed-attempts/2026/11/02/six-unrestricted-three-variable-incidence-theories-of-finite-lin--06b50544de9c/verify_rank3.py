"""Independent rank-three sentence signatures for finite point-line structures."""
from itertools import product, combinations
from collections import defaultdict

def vector_elements(kind,d,q):
    ambient=list(product(range(q),repeat=d+(kind=='PG')))
    if kind=='AG':
        points=ambient
        lines={frozenset(tuple((a[i]+u*b[i])%q for i in range(d)) for u in range(q)) for a in ambient for b in ambient if any(b)}
    else:
        def canon(x):
            z=next(i for i,c in enumerate(x) if c)
            v=pow(x[z],-1,q)
            return tuple((t*v)%q for t in x)
        points=sorted(set(canon(x) for x in ambient if any(x)))
        lines=set()
        for a,b in combinations(points,2):
            p=frozenset(canon(tuple((u*a[j]+v*b[j])%q for j in range(d+1))) for u in range(q) for v in range(q) if (u or v))
            if len(p)==q+1: lines.add(p)
    return points, list(lines)

# Recursive rank-r types of tuples with at most r added elements.
# Globally intern types so different structures share exactly the same IDs.
INTERN={}
def intern(x):
    if x not in INTERN:INTERN[x]=len(INTERN)
    return INTERN[x]

def rank3(kind,d,q):
    ps,ls=vector_elements(kind,d,q)
    n=len(ps);N=n+len(ls)
    inc=[{i for i,l in enumerate(ls) if p in l} for p in ps]
    def atom(t):
        s=tuple(int(u>=n) for u in t)
        eq=tuple(int(t[i]==t[j]) for i in range(len(t)) for j in range(i+1,len(t)))
        edges=tuple(int((t[i]<n and t[j]>=n and (t[j]-n) in inc[t[i]]) or
                        (t[j]<n and t[i]>=n and (t[i]-n) in inc[t[j]])) for i in range(len(t)) for j in range(i+1,len(t)))
        return intern(('atom',s,eq,edges))
    # Different from geometric profile: all labels are purely atomic; quantifiers build types.
    typ3=[[[atom((a,b,c)) for c in range(N)] for b in range(N)] for a in range(N)]
    typ2=[[intern(('1',atom((a,b)),tuple(sorted(set(typ3[a][b]))))) for b in range(N)] for a in range(N)]
    typ1=[intern(('2',atom((a,)),tuple(sorted(set(typ2[a]))))) for a in range(N)]
    out=intern(('3',tuple(sorted(set(typ1)))))
    return out,len(ps),len(ls),len(set(typ2[a][b] for a in range(N) for b in range(N)))

def edge_geometry(n):
    return list(range(n)),[frozenset(x) for x in combinations(range(n),2)]

def rank3_direct(ps,ls):
    n=len(ps);N=n+len(ls)
    inc=[{i for i,l in enumerate(ls) if p in l} for p in ps]
    def atom(t):
        s=tuple(int(u>=n) for u in t)
        eq=tuple(int(t[i]==t[j]) for i in range(len(t)) for j in range(i+1,len(t)))
        edges=tuple(int((t[i]<n and t[j]>=n and t[j]-n in inc[t[i]]) or (t[j]<n and t[i]>=n and t[i]-n in inc[t[j]])) for i in range(len(t)) for j in range(i+1,len(t)))
        return intern(('atom',s,eq,edges))
    typ3=[[[atom((a,b,c)) for c in range(N)] for b in range(N)] for a in range(N)]
    typ2=[[intern(('1',atom((a,b)),tuple(sorted(set(typ3[a][b]))))) for b in range(N)] for a in range(N)]
    typ1=[intern(('2',atom((a,)),tuple(sorted(set(typ2[a]))))) for a in range(N)]
    return intern(('3',tuple(sorted(set(typ1)))))

if __name__=='__main__':
    examples={
      'PG_2_2':vector_elements('PG',2,2),
      'PG_2_3':vector_elements('PG',2,3),
      'AG_2_2':vector_elements('AG',2,2),
      'AG_2_3':vector_elements('AG',2,3),
      'AG_3_2':vector_elements('AG',3,2),
      'PG_3_2':vector_elements('PG',3,2),
    }
    for n in range(3,8): examples[f'K_{n}']=edge_geometry(n)
    groups={}
    for name,(p,l) in examples.items():
        t=rank3_direct(p,l)
        groups.setdefault(t,[]).append(name)
        print(name,'points',len(p),'lines',len(l),'rank_three_type',t)
    assert len(groups)==4,groups
    assert any(set(names)>={'AG_2_3','AG_3_2','PG_3_2','K_5','K_6','K_7'} for names in groups.values())
    assert any(set(names)>={'AG_2_2','K_4'} for names in groups.values())
    assert any(set(names)>={'PG_2_2','PG_2_3'} for names in groups.values())
    for t,names in sorted(groups.items()): print('RANK_THREE_CLASS',t,','.join(sorted(names)))
    print('PASS: four rank-three sentence classes in the tested family')
