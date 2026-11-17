"""Independent rung-transfer exact check for an antiferromagnetic Möbius ladder."""

SPINS = [(-1,-1),(-1,1),(1,-1),(1,1)]

def sector_minima(n):
    out={}
    for first in range(4):
        a,b=SPINS[first]
        dyn={(first,a+b):(a*b,1)}
        for j in range(1,n):
            nxt={}
            for (old,mag),(eng,count) in dyn.items():
                p,q=SPINS[old]
                for new,(r,s) in enumerate(SPINS):
                    e=eng+r*s+p*r+q*s
                    key=(new,mag+r+s)
                    if key not in nxt or e<nxt[key][0]:nxt[key]=(e,count)
                    elif e==nxt[key][0]:nxt[key]=(e,nxt[key][1]+count)
            dyn=nxt
        for (last,mag),(eng,count) in dyn.items():
            c,d=SPINS[last]
            e=eng+c*b+d*a # crossing a_last to b_first, b_last to a_first
            if mag not in out or e<out[mag][0]:out[mag]=(e,count)
            elif e==out[mag][0]:out[mag]=(e,out[mag][1]+count)
    return out

def pell_lucas(n):
    u,v=2,2
    for _ in range(2,n+1):u,v=v,2*v+u
    return v

# Independent sets: transfer on the three allowed states of one rung.
def number_independent(n):
    T=((1,1,1),(1,0,1),(1,1,0))
    P=(0,2,1)
    # Matrix multiplication has no floating point and does not use the closed form.
    A=[[int(i==j) for j in range(3)] for i in range(3)]
    for _ in range(n):
        A=[[sum(A[i][k]*T[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    return sum(A[i][P[i]] for i in range(3))

def check(n):
    hull=sector_minima(n)
    assert sum(x[1] for x in hull.values())<=4**n
    assert number_independent(n)==pell_lucas(n)-(-1)**n
    for B in (0,1,2,3,4,5,6,7,8):
        arr=[(2*energy-B*m,deg) for m,(energy,deg) in hull.items()]
        best=min(v for v,_ in arr)
        multiplicity=sum(c for v,c in arr if v==best)
        if n%2:
            expected=min(-6*n,6*n-2*n*B)
            d=2 if B<6 else (number_independent(n) if B==6 else 1)
        else:
            expected=min(-6*n+8,-6*n+12-2*B,6*n-2*n*B)
            d=(2*n if B<2 else 4*n if B==2 else 2*n if B<6
               else number_independent(n) if B==6 else 1)
        assert (best,multiplicity)==(expected,d),(n,B,(best,multiplicity),(expected,d))
    if n%2:
        assert hull[0]==(-3*n,2)
    else:
        assert hull[0]==(-3*n+4,2*n)
        assert hull[2]==(-3*n+6,2*n)

for n in range(3,51):
    check(n)
    if n<=12 or n in (20,30,40,50): print('transfer checked n=',n,'independent sets=',number_independent(n))
print('ALL_TRANSFER_AND_INDEPENDENCE_CHECKS_PASS')
