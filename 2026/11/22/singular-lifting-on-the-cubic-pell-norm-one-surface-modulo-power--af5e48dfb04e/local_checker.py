"""Direct prime-power residue enumeration for the symmetric cubic Pell equation.

The count is computed from the original cubic expression, not the
factorization or a lifting recurrence. Intended to test the proof's exact
local counts and exceptional mod-3 specialization.
"""
import json

def count_mod(n):
    cubes=[pow(x,3,n) for x in range(n)]
    total=0; distribution=[0]*27 if n%3==0 else None
    # independent direct expression from polynomial definition
    for x in range(n):
        x3=cubes[x]
        for y in range(n):
            s=(x3+cubes[y])%n
            b=(3*x*y)%n
            for z in range(n):
                if (s+cubes[z]-b*z)%n==1:
                    total+=1
                    if distribution is not None:
                        distribution[9*(x%3)+3*(y%3)+(z%3)]+=1
    return total,distribution

def predicted(p,k):
    n=p**k
    if p==3:return n*n
    return (p-1)**2*p**(2*k-2) if p%3==1 else (p*p-1)*p**(2*k-2)

if __name__ == '__main__':
    entries=[]
    for p,stop in [(2,5),(3,5),(5,4),(7,3),(11,3),(13,3),(17,2)]:
        for k in range(1,stop):
            n=p**k
            actual,d= count_mod(n)
            assert actual==predicted(p,k),(p,k,actual,predicted(p,k))
            if p==3:
                if k==1:
                    assert sum(d)==9 and sum(v>0 for v in d)==9
                else:
                    nonzero=[(a,v) for a,v in enumerate(d) if v]
                    assert len(nonzero)==3,(p,k,nonzero)
                    expected={1*9,1*3,1}
                    assert {a for a,v in nonzero}==expected,(k,nonzero)
                    assert all(v==3**(2*k-1) for _,v in nonzero)
            entries.append({'p':p,'k':k,'n':n,'solutions':actual,
                         'mod3_positive_classes':sum(v>0 for v in d) if d else None})
    # Projection from modulus 3^(k+1) to 3^k. For each lower-level
    # solution we enumerate all 27 coordinate-digit refinements directly.
    lifts=[]
    for k in range(1,4):
        m=3**k; high=3*m
        eligible=0; solutions=0
        for x in range(m):
            for y in range(m):
                for z in range(m):
                    f=x*x*x+y*y*y+z*z*z-3*x*y*z
                    if (f-1)%m!=0:
                        continue
                    solutions+=1
                    cnt=0
                    for u in range(3):
                        xx=x+m*u
                        for v in range(3):
                            yy=y+m*v
                            for w in range(3):
                                zz=z+m*w
                                ff=xx*xx*xx+yy*yy*yy+zz*zz*zz-3*xx*yy*zz
                                if (ff-1)%high==0:
                                    cnt+=1
                    assert cnt in (0,27),(k,x,y,z,cnt)
                    if cnt==27:
                        eligible+=1
        assert solutions==3**(2*k)
        assert eligible==3**(2*k-1)
        lifts.append({'level':k,'solutions':solutions,'liftable':eligible,
                      'nonempty_fiber_size_verified':27})
    print(json.dumps({'status':'passed','cases':len(entries),
                      'results':entries,'lift_sieve':lifts},indent=2))
