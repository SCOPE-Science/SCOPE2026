"""Exact coefficient recurrence for the bounded circular five-window count.
No external dependencies.  Each t^n u^d coefficient is an integer.
"""
from math import floor

N = {(1,3):1,(2,1):2,(4,2):4,(5,0):10,(7,1):-7,(10,0):-10}
TERMS = ((1,3,1),(2,1,1),(4,2,1),(5,0,2),(7,1,-1),(10,0,-1))

def coefficients(max_n):
    c=[{} for _ in range(max_n+1)]
    for n in range(1,max_n+1):
        row={}
        for d in range(3*n+1):
            z=N.get((n,d),0)
            for lag,shift,mult in TERMS:
                if n>=lag and d>=shift: z+=mult*c[n-lag].get(d-shift,0)
            if z:row[d]=z
        c[n]=row
    return c

def optimal(n):
    q,r=divmod(n,5)
    if r==0:return 10
    if r==1:return n*(q+1)*(2*q+3)//3
    if r==2:return n
    if r==3:return n*(q+1)*(q+2)*(7*q+12)//24
    return 3*n*(q+1)//2

if __name__=='__main__':
    cc=coefficients(80)
    for n in range(5,81):
        assert all((d>=0 and (3*n-d)%5==0 and x>=0) for d,x in cc[n].items()),(n,cc[n])
        mx=max((3*n-d)//5 for d in cc[n])
        assert mx==3*n//5,(n,mx)
        assert cc[n][3*n-5*mx]==optimal(n),(n,cc[n][3*n-5*mx],optimal(n))
    print('recurrence=PASS n=5..80; exact integer coefficients, sharp floor(3n/5), and all five optimal-multiplicity laws')
    for n in range(5,19):
        print('n='+str(n)+' '+' '.join(str(cc[n].get(3*n-5*k,0)) for k in range(n+1)))
