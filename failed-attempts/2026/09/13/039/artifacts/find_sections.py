p=7
At=[1,5,3]  # Atilde
Bt=[2,1,1,6,2]
# A(t)=t^2*At, B=t^3*Bt
A=[0]*9
for i,a in enumerate(At): A[i+2]=(A[i+2]+a)%p
B=[0]*13
for i,b in enumerate(Bt): B[i+3]=(B[i+3]+b)%p
print("A",A,"B",B)
# G check factor
import itertools
def poly_mul(f,g):
    h=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):
            h[i+j]=(h[i+j]+a*b)%p
    return h
def poly_add(f,g):
    n=max(len(f),len(g)); h=[0]*n
    for i in range(len(f)): h[i]+=f[i]
    for i in range(len(g)): h[i]+=g[i]
    return [x%p for x in h]
def peval(f,t):
    return sum(c*pow(t,i,p) for i,c in enumerate(f))%p

# discriminant-like F=4A^3+27B^2 ; 27=-1 mod7
def poly_pow(f,n):
    r=[1]
    for _ in range(n): r=poly_mul(r,f)
    return r
A3=poly_pow(A+[0]*(9-len(A)),3) if len(A)<9 else poly_pow(A,3)
B2=poly_pow(B+[0]*(13-len(B)),2) if len(B)<13 else poly_pow(B,2)
F=[0]*max(len(A3),len(B2))
for i in range(len(A3)): F[i]=(F[i]+4*A3[i])%p
for i in range(len(B2)): F[i]=(F[i]+27*B2[i])%p
# trim zeros high
while len(F)>1 and F[-1]==0: F.pop()
print("F deg",len(F)-1,"coeffs",F)
for t in range(7):
    print(t, peval(A,t), peval(B,t), peval(F,t))
# factor check: divide by t^8? v0 should be 8
print("v0:", next((i for i,c in enumerate(F) if c!=0), None))
# shift to t=1: G1(s)=F(1+s)
# compute valuations via derivatives already done; just print F/(t^8 (t-1)^5) root
# polynomial division
def poly_mod_div(F, root):
    # divide by (t-root), assume divisible
    n=len(F)-1
    q=[0]*n
    # synthetic
    carry=0
    # F = (t-root)Q + R; do from top
    # use long division
    F=list(F)
    Q=[0]*n
    # copy
    R=F[:]
    # degree n -> n-1
    QQ=[0]*n
    rem=0
    # synthetic division with root
    # coefficients high to low
    acc=0
    # standard: b_{n-1}=a_n; b_{k-1}=a_k+root*b_k
    hi=len(F)-1
    b=[0]*(hi+1)
    b[hi-1]=F[hi]
    for k in range(hi-1,0,-1):
        b[k-1]=(F[k]+root*b[k])%p
    rem=(F[0]+root*b[0])%p
    return b[:hi], rem
Q=F[:]
for root,cnt in [(0,8),(1,5)]:
    for _ in range(cnt):
        Q,r=poly_mod_div(Q,root)
        assert r==0, (root,r)
print("remaining deg",len(Q)-1,Q)
# roots of remaining linear
print("rem root:", (-Q[0]*pow(Q[1],-1,p))%p if len(Q)==2 else Q)

# search polynomial sections x deg<=4
def is_square_poly(R):
    # R list coeffs; find y deg<=6 with y^2=R
    # necessary: deg even, leading square
    d=len(R)-1
    while d>0 and R[d]==0: d-=1
    R=R[:d+1]
    if d%2==1: return None
    m=d//2
    # brute force y? 7^7 too big. Instead solve via leading coeff + back-substitution (char not 2)
    # y_m^2 = lead
    lead=R[d]
    sq=[y for y in range(p) if (y*y)%p==lead]
    if not sq: return None
    for ylead in sq:
        y=[0]*(m+1); y[m]=ylead
        # equations: for k=2m down to 0: sum_{i+j=k} y_i y_j = R_k
        # solve descending: k=2m known; k=2m-1: 2*y_m*y_{m-1}=R_{2m-1} -> y_{m-1}
        ok=True
        for k in range(2*m-1,-1,-1):
            # contribution of unknowns: 2*y_m*y_{k-m} if k-m in [0,m-1]
            # isolate
            s=R[k] if k < len(R) else 0
            # subtract known products y_i y_j=k with both >? Actually when solving descending, at step k, unknown is y_{k-m} (if in range) multiplied by 2 y_m; other terms involve y_j with j>k-m which are known.
            j_unknown = k - m
            known=0
            for i in range(m+1):
                j=k-i
                if j<0 or j>m: continue
                if i==m and j==j_unknown and j_unknown!=m:
                    continue
                if j==m and i==j_unknown and j_unknown!=m:
                    continue
                # if either index unknown (<=> index < =m-1 and not yet solved?) solved indices are m, m-1, ..., k-m+1
                # unknown indices are < k-m+1 i.e. <=k-m
                # term with both known: i>=k-m+1 and j>=k-m+1
                if i<=(k-m) and j<=(k-m):
                    # both unknown (unless k-m out of range) -> if k-m<0 then no unknowns
                    pass
                    if j_unknown<0 or j_unknown>m-1:
                        # no unknown; all known? but indices small unknown... hmm at low k many unknowns
                        ok=False; break
                    else:
                        # product of two unknowns - can't solve yet -> fail this branch? Actually for small k this method fails; need different approach
                        ok=False; break
                elif i<=(k-m) or j<=(k-m):
                    # one unknown which must be j_unknown (since one index is m? not necessarily)
                    ok=False; break
                else:
                    known=(known+y[i]*y[j])%p
            if not ok: break
            if j_unknown<0:
                if known!=s: ok=False; break
            elif j_unknown>=m:
                if known!=s: ok=False; break
            else:
                # 2*y_m*y_ju + known = s
                rhs=(s-known)%p
                denom=(2*ylead)%p
                y[j_unknown]=(rhs*pow(denom,-1,p))%p
        if ok:
            # verify
            yy=[0]*(2*m+1)
            for i in range(m+1):
                for j in range(m+1):
                    yy[i+j]=(yy[i+j]+y[i]*y[j])%p
            if yy==R+( [0]*(len(yy)-len(R)) ):
                return y
    return None

sols=[]
for coeffs in itertools.product(range(p), repeat=5):
    x=list(coeffs)
    # compute R=x^3+A x+B
    X=x+[0]*8
    X3=poly_pow(X,3)
    AX=poly_mul(A,X)
    n=max(len(X3),len(AX),len(B))
    R=[0]*n
    for i in range(len(X3)): R[i]=(R[i]+X3[i])%p
    for i in range(len(AX)): R[i]=(R[i]+AX[i])%p
    for i in range(len(B)): R[i]=(R[i]+B[i])%p
    while len(R)>1 and R[-1]==0: R.pop()
    y=is_square_poly(R)
    if y is not None:
        sols.append((x,y,R))
        print("SECTION x=",x,"y=",y)
print("n poly sections:",len(sols))
