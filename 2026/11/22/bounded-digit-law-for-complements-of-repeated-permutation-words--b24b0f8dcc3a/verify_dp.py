"""Independent delete-or-keep dynamic programming against coefficient counts."""
from functools import lru_cache

def actual(q,m,k):
    P='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:q]
    w=P*(m+k);u=P*k
    @lru_cache(maxsize=None)
    def F(i,j):
        if i==len(w):return frozenset(['']) if j==len(u) else frozenset()
        keep={w[i]+v for v in F(i+1,j)}
        if j<len(u) and w[i]==u[j]:keep.update(F(i+1,j+1))
        return frozenset(keep)
    return F(0,0)

def formula(q,m,k):
    a=[1]
    for _ in range(m):
        b=[0]*(len(a)+q-1)
        for i,v in enumerate(a):
            for d in range(q):b[i+d]+=v
        a=b
    return sum(a[:q*k+1])

def main():
    checks=0
    sample=[]
    for q in (2,3,4,5):
        for m in range(0,7):
            for k in range(0,5):
                if q*(m+k)>25:continue
                result=len(actual(q,m,k));f=formula(q,m,k)
                if result!=f:raise AssertionError((q,m,k,result,f))
                checks+=1
                if (q,m,k) in [(3,4,2),(4,4,2),(5,3,2)]:sample.append((q,m,k,result))
    print('PASS independent deletion-DP versus polynomial coefficients')
    print('parameter_cases',checks)
    print('selected_counts',sample)
if __name__=='__main__':main()
