"""Independent twisted-transfer and symbolic determinant certificate."""
from collections import defaultdict
from sympy import symbols, Matrix, eye, factor, diff, expand, series, I, simplify

y,z,w,t = symbols('y z w t')
def flip(c): return ((c & 1)<<1) | ((c & 2)>>1)
def admissible(a,b,c):
    for r in (0,1):
        if ((b>>r)&1)==0:
            n=((a>>r)&1)+((b>>(1-r))&1)+((c>>r)&1)
            if n not in (1,2): return False
    return True

M=Matrix.zeros(16)
J=Matrix.zeros(16)
for a in range(4):
    for b in range(4):
        u=4*a+b
        J[u,4*flip(a)+flip(b)]=1
        for c in range(4):
            if admissible(a,b,c):
                M[u,4*b+c]=z**b.bit_count()
assert M*J==J*M

def restricted_basis():
    pos=[]; neg=[]; seen=set()
    for u in range(16):
        if u in seen:continue
        v=4*flip(u//4)+flip(u%4)
        seen|={u,v}
        if u==v:pos.append({u:1})
        else:pos.append({u:1,v:1});neg.append({u:1,v:-1})
    def transform(basis):
        K=Matrix.zeros(len(basis))
        for j,b in enumerate(basis):
            image=[sum(M[v,u]*c for u,c in b.items()) for v in range(16)]
            for i,g in enumerate(basis):
                v=next(iter(g));K[i,j]=image[v]/g[v]
            assert all(sum(K[i,j]*g.get(v,0) for i,g in enumerate(basis))==image[v] for v in range(16))
        return K
    return transform(pos),transform(neg)

P,Q=restricted_basis()
plus=1-y*z-y*z**2-y**2*z-2*y**2*z**2+y**2*z**3-2*y**3*z**2-2*y**3*z**3-y**3*z**4+y**5*z**3+y**6*z**4
minus=1-y*z+y**2*z+y**2*z**2-y**3*z**2
assert factor((eye(10)-y*P).det(method='domain-ge')-plus)==0
assert factor((eye(6)-y*Q).det(method='domain-ge')-minus)==0

def profile(n):
    answer=defaultdict(int)
    for st in range(16):
        current={(st,0):1}
        for step in range(n):
            following=defaultdict(int)
            for (u,k),ways in current.items():
                a,b=divmod(u,4)
                for c in range(4):
                    if admissible(a,b,c):
                        following[(4*b+c,k+b.bit_count())]+=ways
            current=following
        a,b=divmod(st,4)
        goal=4*flip(a)+flip(b)
        for (u,k),ways in current.items():
            if u==goal: answer[k]+=ways
    return dict(answer)

def expected(n):
    if n%4==2:return n//2,4
    if n%4==0:return n//2+1,n*n
    if n==3:return 2,9
    return (n+1)//2,2*n

def main():
    for n in range(3,41):
        ans=profile(n); low=min(ans)
        assert (low,ans[low])==expected(n),(n,low,ans[low])
        if n<=12 or n%4==0:
            print(f'n={n} min={low} optima={ans[low]} total={sum(ans.values())}')
    # Leading terms in the bivariate logarithm after y=w/t,z=t^2.
    Ap,Bp,Cp=1-w*w,-w-2*w**3+w**5,-2*w**2+w**6
    Am,Bm,Cm=1+w*w,-w-w**3,w**2
    L1=factor(Bm/Am-Bp/Ap)
    L2=factor(Cm/Am-Cp/Ap-(Bm/Am)**2/2+(Bp/Ap)**2/2)
    assert simplify(L1-w**3*(3-w**2)/(1-w**2))==0
    assert simplify((L2+L2.subs(w,I*w))/2-4*w**4/(1-w**4)**2)==0
    print('transfer matrix / determinant / leading coefficient verification PASSED')

if __name__=='__main__':main()
