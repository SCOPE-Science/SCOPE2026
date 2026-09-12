# Bounded recovery test: can small-field constructions beat exponent 13/9 ~ 1.444?
# (a) Grid S^3 with Pythagorean (conic) normals, all hitting planes.
# (b) Random P, random restricted Pi.
import math, random

def conic_dirs_small(p, H):
    """projective conic points with small integer rep max|.|<=H (as ints 0..p-1 mapped to symmetric)."""
    def sym(x): return x if x<=p//2 else x-p
    pts=[]
    for a in range(p):
        for b in range(p):
            for c in range(p):
                if (a,b,c)==(0,0,0): continue
                if (a*a+b*b-c*c)%p!=0: continue
                if max(abs(sym(a)),abs(sym(b)),abs(sym(c)))<=H:
                    # canonical projective rep
                    v=(a,b,c)
                    for i in range(3):
                        if v[i]%p!=0:
                            inv=pow(v[i],p-2,p)
                            v=tuple((x*inv)%p for x in v)
                            break
                    pts.append(v)
    return list(set(pts))

def grid_test(p, s, H):
    S=list(range(s))
    P={(x,y,z) for x in S for y in S for z in S}
    m=len(P)
    dirs=conic_dirs_small(p,H)
    def sym(x): return x if x<=p//2 else x-p
    I=0; n=0
    # use symmetric reps for geometry: convert projective rep to symmetric triple
    for d in dirs:
        a,b,c=[sym(v) for v in d]
        if (a,b,c)==(0,0,0): continue
        ds={a*x+b*y+c*z for (x,y,z) in P}
        n+=len(ds)
        # each point on exactly one plane per direction
        I+=m
    N=max(m,n)
    exp=math.log(I)/math.log(N) if N>1 and I>0 else 0
    return dict(p=p,s=s,H=H,m=m,n=n,I=I,exp=round(exp,4))

for (p,s,H) in [(13,4,5),(17,5,5),(19,6,6)]:
    print(grid_test(p,s,H))

# random test
random.seed(0)
for (p,N) in [(11,30),(13,40)]:
    P={(random.randrange(p),random.randrange(p),random.randrange(p)) for _ in range(N)}
    while len(P)<N: P.add((random.randrange(p),random.randrange(p),random.randrange(p)))
    P=list(P)
    # random restricted normals: param t -> (2t,1-t^2,1+t^2), plus [0:1:-1]? just sample
    norms=set()
    for t in range(p):
        a=(2*t)%p; b=(1-t*t)%p; c=(1+t*t)%p
        if (a,b,c)==(0,0,0): continue
        v=(a,b,c)
        for i in range(3):
            if v[i]%p!=0:
                inv=pow(v[i],p-2,p)
                v=tuple((x*inv)%p for x in v)
                break
        norms.add(v)
    norms=list(norms)
    Pi=[]
    for _ in range(N):
        nrm=random.choice(norms)
        d=random.randrange(p)
        Pi.append((nrm,d))
    I=sum(1 for (x,y,z) in P for ((a,b,c),d) in Pi if (a*x+b*y+c*z)%p==d%p)
    # note: projective scale: equation with rep is well-defined up to scale only if d scaled; use raw rep dot = d (choice of rep fixed per plane, fine)
    exp=math.log(max(I,1))/math.log(N)
    print(f"random p={p} N={N} I={I} exp~{exp:.3f} (vs 13/9=1.444)")
