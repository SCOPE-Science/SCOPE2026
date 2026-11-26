"""Direct finite-prime-field verification of rank-one Lie Rota-Baxter census.
No external dependencies. Coordinates (e,f,h) for traceless two-by-two matrices.
"""
from itertools import product

def add(u,v,p): return tuple((a+b)%p for a,b in zip(u,v))
def neg(u,p): return tuple(-a%p for a in u)
def scalar(t,u,p): return tuple(t*a%p for a in u)
def bracket(u,v,p):
    x,y,z=u; X,Y,Z=v
    return (2*(z*X-x*Z)%p, 2*(y*Z-z*Y)%p, (x*Y-y*X)%p)
def tr(u,v,p):
    return (u[0]*v[1]+u[1]*v[0]+2*u[2]*v[2])%p

def is_rb_direct(a,b,p):
    basis=((1,0,0),(0,1,0),(0,0,1))
    for i in range(3):
      for j in range(i+1,3):
        u,v=basis[i],basis[j]
        ru=scalar(tr(b,u,p),a,p)
        rv=scalar(tr(b,v,p),a,p)
        rhs_arg=add(bracket(ru,v,p),bracket(u,rv,p),p)
        if bracket(ru,rv,p)!=scalar(tr(b,rhs_arg,p),a,p):return False
    return True

def proportional(x,y,p):
    return all((x[i]*y[j]-x[j]*y[i])%p==0 for i in range(3) for j in range(i+1,3))

def check(p):
    elems=[v for v in product(range(p),repeat=3) if any(v)]
    # Each rank-one endomorphism has exactly p-1 ordered factorizations.
    total_pairs=central=root=intersection=rb_sqs=rb_idem=0
    for a in elems:
      for b in elems:
        rb=is_rb_direct(a,b,p)
        commute=bracket(a,b,p)==(0,0,0)
        rootcond=(tr(b,b,p)==0 and proportional(bracket(a,b,p),b,p))
        theory=commute or rootcond
        if rb!=theory:
            raise AssertionError((p,a,b,rb,theory))
        if rb:
          total_pairs+=1
          central+=commute
          root+=rootcond
          intersection+=commute and rootcond
          rb_sqs+=(tr(a,b,p)==0)
          rb_idem+=(tr(a,b,p)==1)
    res={"q":p, "rank_one":total_pairs//(p-1), "central":central//(p-1),
       "root":root//(p-1),"intersection":intersection//(p-1),
       "square_zero":rb_sqs//(p-1),"idempotents":rb_idem//(p-1)}
    expected={"q":p,"rank_one":2*p**3-p-1,"central":p**3-1,
     "root":(p+1)*(p*p-1),"intersection":p*p-1,
     "square_zero":p**3+p*p-p-1,"idempotents":p*p}
    assert res==expected,(res,expected)
    return res

if __name__=='__main__':
    import json
    for p in (3,5,7):print(json.dumps(check(p),sort_keys=True))
    print('SL2_RANKONE_RB_DIRECT_PASS')
