"""DIRECT verification of the DP weight bug: test the recursion step k=1 by hand.
W_1[(e1),0] should be int_0^1 t dt = 1/2. Recursion: Q=p1=t_1: t-expansion A=1,f=0:
W_1 = C/(A+0+1) W_0[(0,..,0), A+1] = 1/2 * 1 = 1/2. OK so W_1 is right.
W_2[(e1),0] should be int_{Dx_2} (x+y) = 1/6. Recursion from W_1:
subs of e1: (f=0,A=1),(f=e1,A=0). W_2 = 1/2*W_1[(0),2] + 1*W_1[(e1),1].
W_1[(0),2] = int_0^1 u^2 du = 1/3. W_1[(e1),1] = int_0^1 t(1-t) dt = 1/6.
So W_2 = 1/2*1/3 + 1/6 = 1/3. But true answer 1/6! So recursion DOUBLE counts.
Why? t-expansion of Q at level 2: Q(x,y)=x+y. Expand in y (last var): Q = x + y,
i.e., f-parts: Q'_0 = x (f=0? no!). The term x corresponds to f=e1 (Q' restricted),
A=0. Term y corresponds to f=0, A=1. That's what we used. Integral over y then x:
int_{Dx_1} [int_0^u (Q'(x) + y) dy] dx with u=1-x: inner = Q'(x)*u + u^2/2 = x(1-x)+(1-x)^2/2.
Outer int_0^1: 1/6 + 1/6 = 1/3?? But direct int_{x+y<=1}(x+y) = ?
int_0^1 int_0^{1-x} (x+y) dy dx = int_0^1 [x(1-x) + (1-x)^2/2] dx = 1/6+1/6=1/3.
Hmm! So 1/3, and my 'exact' formula d!/(k+d)! = 1/6 was WRONG?
Check: int_{Dx_2(1)} (x+y) dxdy. Substitute s=x+y: int_0^1 s * (measure of {x+y=s}) ds = int_0^1 s^2 ds = 1/3.
Yes! 1/3. The Laplace formula: int_{Dx_k(1)} S^d (S=sum) = ? Laplace: int e^{-tS}... 
int_{Dx_k(1)} S^d = k * B(d+1... : = k*d!/(k+d)!? For k=2,d=1: 2/6=1/3. Yes.
So correct formula is k*d!/(k+d)! — I dropped the factor k (volume of slice scales).
And int p1 over Dx_3 = 3*1/24=1/8? k*d!/(k+d)! = 3/24=1/8. Earlier 'verify_smallk' J1(p1)=1/24 matched —
that used only W on Dx_2 with r>=2 (r>=1 always correct since those are single-variable Betas).
So: the bottom-up DP is CORRECT; my check formula was wrong. Verify: k=50, d=1: 50/51! vs got 8.2198735416e-64.
51! = 1.551...e66. 50/51! = 3.223...e-65?? compute: 51! = 155568095557812363380911522709709038990... let me just numerically compare in script.
Also int p1^2: E[S^2] style: S^2 = sum t_i^2 + 2 sum t_it_j: Dirichlet: int t_i^2 = 2!/(k+2)!, int t_it_j = 1/(k+2)!.
So int S^2 = [2k + k(k-1)]/(k+2)! = k(k+1)/(k+2)!. Check DP.
"""
import pickle, math
d = pickle.load(open("output/artifacts/dp_corr.pkl","rb"))
vecs = d["vecs"]; Eidx={v:i for i,v in enumerate(vecs)}
v50 = d["val50"]
for dd in range(0,7):
    e = tuple(([dd]+[0]*8))
    got = v50[(Eidx[e],0)]
    # exact: int S^d = sum over compositions: d!/(prod mult!) * (multinomial over k vars)... 
    # S^d = sum_{|alpha|=d} d!/alpha! t^alpha; int t^alpha = prod(alpha_i!)/(k+d)!
    # so int = d!/(k+d)! * #{alpha:|alpha|=d} = d!/(k+d)! * C(k+d-1,d) = (k+d-1)!/((k+d)! ) * ... = C(k+d-1,d)*d!/(k+d)! = (k+d-1)!/(k+d)!/ ... compute C(k+d-1,d)*d! = (k+d-1)!/(d!(k-1)!) * d! = (k+d-1)!/(k-1)!. divide by (k+d)!: = 1/[(k-1)! (k+d)].
    want = 1/(math.factorial(49)*(50+dd))
    print("d=%d got=%.10e want=%.10e ratio=%.8f" % (dd, got, want, got/want))
