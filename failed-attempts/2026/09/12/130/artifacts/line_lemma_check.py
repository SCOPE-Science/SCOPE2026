# Exhaustive check (small p): every F_p-line lies in at most 2 restricted planes
# (normals on Gamma0: X^2+Y^2=Z^2), counting over ALL restricted planes.
from itertools import product

def proj_reps(p):
    seen=set(); reps=[]
    for a in range(p):
        for b in range(p):
            for c in range(p):
                if (a,b,c)==(0,0,0): continue
                if (a*a+b*b-c*c)%p!=0: continue
                v=(a,b,c)
                for i in range(3):
                    if v[i]%p!=0:
                        inv=pow(v[i],p-2,p)
                        v=tuple((x*inv)%p for x in v)
                        break
                if v not in seen:
                    seen.add(v); reps.append(v)
    return reps

def check(p):
    normals=proj_reps(p)
    assert len(normals)==p+1, (p,len(normals))
    # directions: projective P^2 (line directions)
    dirs=proj_reps(p)  # same enumeration trick works for all of P^2? No: need all dirs, so enumerate:
    seen=set(); dirs=[]
    for a in range(p):
        for b in range(p):
            for c in range(p):
                if (a,b,c)==(0,0,0): continue
                v=(a,b,c)
                for i in range(3):
                    if v[i]%p!=0:
                        inv=pow(v[i],p-2,p)
                        v=tuple((x*inv)%p for x in v)
                        break
                if v not in seen:
                    seen.add(v); dirs.append(v)
    worst=0; worst_ex=[]
    for v in dirs:
        n_orth=[n for n in normals if (n[0]*v[0]+n[1]*v[1]+n[2]*v[2])%p==0]
        worst=max(worst,len(n_orth))
        if len(n_orth)>2: worst_ex.append((v,n_orth))
    print(f"p={p}: #normals={len(normals)}, max restricted planes containing a line = {worst}")
    assert worst<=2, worst_ex[:3]
    print(f"p={p}: LINE LEMMA VERIFIED (K_{{2,3}}-free holds)")

for p in [3,5,7]:
    check(p)
