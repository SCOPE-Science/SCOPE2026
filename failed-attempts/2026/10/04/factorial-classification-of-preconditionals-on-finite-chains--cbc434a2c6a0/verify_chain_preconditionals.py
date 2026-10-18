from itertools import product
from math import factorial

def op_from_tau(n, tau):
    top=n-1
    op=[[None]*n for _ in range(n)]
    for j in range(n):
        op[0][j]=top
        op[top][j]=j
    for i in range(1,top):
        op[i][0]=0
        for j in range(1,n):
            if j>=i:
                op[i][j]=top
            else:
                fixed=[k for k in range(j,i) if tau[k] <= i]
                op[i][j]=fixed[0] if fixed else top
    return tuple(tuple(r) for r in op)

def check_all(n, op):
    top=n-1
    for a in range(n):
        if op[top][a] > a:
            return False
    for a,b in product(range(n), repeat=2):
        if min(a,b) > op[a][b]:
            return False
        if op[a][b] > op[a][min(a,b)]:
            return False
    for a,b,c in product(range(n), repeat=3):
        if b<=a and op[a][op[b][c]] > op[b][c]:
            return False
        if b<=c and op[a][b] > op[a][c]:
            return False
    if any(op[a][a] != top for a in range(n)):
        return False
    if any(min(a,op[a][0]) != 0 for a in range(n)):
        return False
    neg=[op[a][0] for a in range(n)]
    if any(a > neg[neg[a]] for a in range(n)):
        return False
    return True

def activation_ops(n):
    if n==2:
        taus=[()]
    else:
        ranges=[range(j+1,n) for j in range(1,n-1)]
        taus=product(*ranges)
    ans=set()
    for tup in taus:
        tau={j:t for j,t in zip(range(1,n-1),tup)}
        op=op_from_tau(n,tau)
        assert check_all(n,op)
        ans.add(op)
    return ans

def row_candidates(n,a):
    top=n-1
    if a==0:
        return [(top,)*n]
    if a==top:
        return [tuple(range(n))]
    out=[]
    def rec(j, prev, arr):
        if j==a:
            out.append(tuple(arr+[top]*(n-a)))
            return
        lo=max(prev,j)
        for v in range(lo,n):
            rec(j+1,v,arr+[v])
    rec(1,0,[0])
    return out

def exhaustive_T_ops(n):
    rows=[row_candidates(n,a) for a in range(n)]
    ans=set()
    for op in product(*rows):
        ok=True
        for a in range(n):
            for b in range(a+1):
                for c in range(n):
                    d=op[b][c]
                    if op[a][d] > d:
                        ok=False
                        break
                if not ok: break
            if not ok: break
        if ok:
            assert check_all(n,op)
            ans.add(tuple(tuple(r) for r in op))
    return ans

for n in range(2,9):
    A=activation_ops(n)
    assert len(A)==factorial(n-2), (n,len(A))
    if n<=6:
        E=exhaustive_T_ops(n)
        assert A==E, (n,len(A),len(E))
    print(n, len(A))
print("VERIFY_OK")
