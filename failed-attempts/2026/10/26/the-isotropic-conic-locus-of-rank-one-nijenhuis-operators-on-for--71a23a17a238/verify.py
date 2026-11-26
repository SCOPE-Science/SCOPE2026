"""Finite-field test for the rank-one Nijenhuis census on sl2 (all odd q)."""
from itertools import product
from collections import Counter

def field(q):
    if q==9:
        p=3
        # t^2=-1=2 in F3, elements a+bt represented by a+3b.
        add=lambda x,y:(x%3+y%3)%3+3*((x//3+y//3)%3)
        neg=lambda x:(-x%3)+3*((-(x//3))%3)
        mul=lambda x,y:((x%3)*(y%3)+2*(x//3)*(y//3))%3+3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
    else:
        p=q
        add=lambda x,y:(x+y)%p
        neg=lambda x:(-x)%p
        mul=lambda x,y:x*y%p
    return add,neg,mul

def check(q):
    add,neg,mul=field(q)
    sub=lambda x,y:add(x,neg(y))
    vec=list(product(range(q),repeat=3)); zero=(0,0,0)
    two=add(1,1)
    def bracket(a,b):
        return (mul(two,sub(mul(a[1],b[0]),mul(a[0],b[1]))),
                sub(mul(a[0],b[2]),mul(a[2],b[0])),
                mul(two,sub(mul(a[2],b[1]),mul(a[1],b[2]))))
    dot=lambda a,b:add(add(mul(a[0],b[0]),mul(a[1],b[1])),mul(a[2],b[2]))
    e=((1,0,0),(0,1,0),(0,0,1))
    pairs=((e[0],e[1]),(e[0],e[2]),(e[1],e[2]))
    counts=Counter(); nonzero=[v for v in vec if v!=zero]
    for ui,u in enumerate(nonzero):
        good=0
        for f in nonzero:
            trace=dot(f,u)
            # Explicit torsion for rank-one N, compared against direct Nijenhuis torsion.
            okay=True
            for x,y in pairs:
                lhs=sub(sub(mul(dot(f,x),dot(f,bracket(u,y))),mul(dot(f,y),dot(f,bracket(u,x)))),mul(trace,dot(f,bracket(x,y))))
                if q!=9 or (ui%29==0 and f[0] in (0,1)):
                    Nx=tuple(mul(dot(f,x),z) for z in u)
                    Ny=tuple(mul(dot(f,y),z) for z in u)
                    vx=bracket(Nx,y); vy=bracket(x,Ny); Nxy=tuple(mul(dot(f,bracket(x,y)),z) for z in u)
                    inner=tuple(sub(add(vx[i],vy[i]),Nxy[i]) for i in range(3))
                    t=tuple(sub(bracket(Nx,Ny)[i],mul(dot(f,inner),u[i])) for i in range(3))
                    assert t == tuple(neg(mul(lhs,z)) for z in u), (q,u,f,x,y,t,lhs)
                if lhs: okay=False
            if okay:
                good+=1
                counts['all_pairs']+=1
                counts['trace_zero' if trace==0 else 'trace_nonzero']+=1
        assert good==q*q-1,(q,u,good)
    assert counts['all_pairs']==(q**3-1)*(q*q-1),counts
    assert counts['trace_zero']==(q-1)*(q-1)*(q+1)**2,counts
    assert counts['trace_nonzero']==q*q*(q*q-1)*(q-1),counts
    # Each operator u ⊗ f was counted q-1 times.
    op_count=counts['all_pairs']//(q-1)
    expected=(q*q+q+1)*(q*q-1)
    assert op_count==expected
    print(f'q={q}: nonzero_u={q**3-1}, admissible_f_per_u={q*q-1}, rankone_operators={op_count}, rankone_square_zero={counts["trace_zero"]//(q-1)}, rankone_nonzero_trace={counts["trace_nonzero"]//(q-1)} OK')

if __name__=='__main__':
    for q in (3,5,7):
        check(q)
    print('SL2_RANKONE_NIJENHUIS_OK')
