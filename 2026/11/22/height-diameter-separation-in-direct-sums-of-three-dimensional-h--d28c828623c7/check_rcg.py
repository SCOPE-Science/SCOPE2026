"""Finite-field, exhaustive check of symplectic-block RCG claims; external dependencies: none."""
from itertools import product
from collections import deque

def det(u,v,p): return (u[0]*v[1]-u[1]*v[0])%p

def dot_form(x,y,dims,p):
    offset=0
    for n in dims:
        s=sum(det(x[offset+2*i:offset+2*i+2], y[offset+2*i:offset+2*i+2],p) for i in range(n))%p
        if s: return False
        offset+=2*n
    return True

def span(vectors,p,d):
    basis={}
    for v in vectors:
        w=list(v)
        for i,b in sorted(basis.items()):
            if w[i]:
                a=w[i]
                w=[(z-a*t)%p for z,t in zip(w,b)]
        piv=next((i for i,x in enumerate(w) if x),None)
        if piv is not None:
            inv=pow(w[piv],-1,p)
            basis[piv]=tuple(x*inv%p for x in w)
    return len(basis)

def run(dims,p):
    d=2*sum(dims)
    P=[v for v in product(range(p),repeat=d) if any(v)]
    adj={u:{v for v in P if v!=u and dot_form(u,v,dims,p)} for u in P}
    h=[]
    depth3=0
    distances=[]
    for u in P:
        W={u};steps=0
        while True:
            # next is span of union of N(w), but we can find all vertices in span using linear span of generators via small enumeration
            vlist={w for w in P if span(W|{w},p,d)==span(W,p,d)}
            next_g=set(vlist)
            for w in vlist:
                next_g.add(w)
                next_g.update(adj[w])
            D=span(next_g,p,d)
            if D==span(W,p,d):break
            W=next_g;steps+=1
            assert steps<=d
        h.append(steps)
        dist={u:0};Q=deque([u])
        while Q:
            w=Q.popleft()
            for z in adj[w]:
                if z not in dist:dist[z]=dist[w]+1;Q.append(z)
        if len(dist)<len(P):distances.append(float('inf'))
        else: distances.append(max(dist.values()))
        for v,z in dist.items():
            if z==3:depth3+=1
    expected_h=0 if len(dims)==1 and dims[0]==1 else 2
    expected_d=(float('inf') if len(dims)==1 and dims[0]==1 else (3 if len(dims)>1 and all(n==1 for n in dims) else 2))
    assert max(h)==expected_h,(dims,p,'h',max(h),expected_h)
    assert max(distances)==expected_d,(dims,p,'diam',max(distances),expected_d)
    target=((p*p-1)*(p*p-p))**len(dims) if len(dims)>1 and all(n==1 for n in dims) else 0
    assert depth3==target,(dims,p,'distance3',depth3,target)
    print(f'case={dims}, field={p}, vertices={len(P)}, height={max(h)}, diameter={max(distances)}, ordered_distance3={depth3}: OK')

if __name__=='__main__':
    for dims,p in [((1,),2),((1,),3),((2,),2),((1,1),2),((1,1),3),((1,1,1),2),((2,1),2)]:run(dims,p)
    print('HEISENBERG_RCG_HEIGHT_DIAMETER_OK')
