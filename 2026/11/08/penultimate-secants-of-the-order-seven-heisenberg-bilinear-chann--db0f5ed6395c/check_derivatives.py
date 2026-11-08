"""Independent exact checks of the channel Jacobian entries over F_29.
Run: python3 check_derivatives.py parameters_q7.txt
Only the Python standard library is required.
"""
import sys
P=29
Q=7
N=49

def delta(u,v):
    return ((u//Q-v//Q)%Q)*Q+(u%Q-v%Q)%Q

def zpow(e):
    return pow(7,e%Q,P)

def matrix_entry(a,b,d,s,t,i,j):
    out=0
    for k in range(N):
        u=delta(i,k);v=delta(j,k)
        out=(out+d[k]*a[u]*b[v]*zpow(-(k//Q)*(s*(u%Q)+t*(v%Q))))%P
    return out

def derivative(a,b,d,s,t,i,j,typ,h):
    if typ==0:
        k=delta(i,h);v=delta(j,k)
        return d[k]*b[v]*zpow(-s*(k//Q)*(h%Q)-t*(k//Q)*(v%Q))%P
    if typ==1:
        k=delta(j,h);u=delta(i,k)
        return d[k]*a[u]*zpow(-s*(k//Q)*(u%Q)-t*(k//Q)*(h%Q))%P
    u=delta(i,h);v=delta(j,h)
    return a[u]*b[v]*zpow(-s*(h//Q)*(u%Q)-t*(h//Q)*(v%Q))%P

def main():
    with open(sys.argv[1]) as f:
        vals=list(map(int,f.read().split()))
    assert len(vals)==16*3*N
    assert all(1<=x<P for x in vals)
    a,b,d=[vals[i*N:(i+1)*N] for i in range(3)]
    cnt=0
    for s,t in [(0,0),(0,1),(1,1),(1,2)]:
        for i,j in [(0,0),(8,30),(17,34),(42,12),(48,48)]:
            before=matrix_entry(a,b,d,s,t,i,j)
            for typ in range(3):
                for h in [0,5,27,48]:
                    arr=[a,b,d][typ]
                    arr[h]=(arr[h]+1)%P
                    after=matrix_entry(a,b,d,s,t,i,j)
                    arr[h]=(arr[h]-1)%P
                    assert (after-before)%P==derivative(a,b,d,s,t,i,j,typ,h),(s,t,i,j,typ,h)
                    cnt+=1
    print('INDEPENDENT_DERIVATIVE_FORMULAS_OK',cnt)
if __name__=='__main__': main()
