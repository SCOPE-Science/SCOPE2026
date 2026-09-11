# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# North-drift walk S2: infinite group, genus-one kernel, and certified irrational cone exponent

## 1. Model and kernel
S2 = {(-1,0),(0,-1),(0,1),(1,1)} (W,S,N,NE). Step polynomial
S(x,y) = 1/x+1/y+y+xy. Kernel K(x,y) = xy(1-tS) equals
  K = -t x^2 y^2 - t x y^2 - t x - t y + x y.
Group involutions (kernel Vieta maps): for fixed y, the two x-roots satisfy
x*x' = 1/y, so Phi(x,y) = (1/(xy), y); for fixed x, the two y-roots satisfy
y*y' = 1/(x+1), so Psi(x,y) = (x, 1/((x+1)y)).
Put theta = Psi o Phi: theta(x,y) = (1/(xy), x/(1+xy)).

## 2. Discriminants and genus
x-discriminant: Dx(y) = (y-t-t y^2)^2 - 4 t^2 y^3
  = t^2 y^4 + (-4t^2-2t)y^3 + (2t^2+1)y^2 - 2t y + t^2 (degree 4).
y-discriminant: Dy(x) = (x-t)^2 + 4t^2 x^2(x+1)
  = -4t^2 x^3 + (1-4t^2)x^2 - 2t x + t^2 (degree 3).
Symbolic computation (artifacts s1.py, s2.py) gives
  disc_y(Dx) = -256 t^8 P(t), disc_x(Dy) = -16 t^4 P(t),
  Res_y(Dx, N) = -16 t^8 P(t),
where P(t) = 11t^4+36t^3+8t^2-t-1 and N is the numerator of dK/dy after
eliminating x via dK/dx = 0 (so Res tests common zeros of Dx and the
singular-point condition, i.e. affine singular points of K=0).
Lemma: P(t) < 0 on [0,1/4]. Proof: on [0,1/4], 11t^4 <= (11/16)t^2 and
36t^3 <= 9t^2, so P(t) <= f(t) := (283/16)t^2 - t - 1. f is a quadratic with
vertex at t = 8/283 > 0, f(0) = -1, f(1/4) = -37/256 < 0, hence f < 0 on
[0,1/4], so P < 0 there. All bounds are exact rational arithmetic
(artifact t9_verifyall.py).
Corollary: for t in (0,1/4), Dx and Dy are separable (nonzero discriminants),
and Dx,N have no common zero (nonzero resultant), so the affine curve K=0 is
smooth. Compactify to P1xP1: with bihomogeneous F = -tX0^2Y0^2 - tX0X1Y0^2
- tX0X1Y1^2 - tX1^2Y0Y1 + X0X1Y0Y1, direct checks (artifact t10_infty.py):
F(1,0,Y) = -tY0^2 (zero only at ([1:0],[0:1]), gradient (0,-t,0,0) != 0);
F(X,1,0) = -tX0(X0+X1) (zeros ([0:1],[1:0]) gradient (-t,0,0,-t) != 0 and
([1:-1],[1:0]) gradient (-t,-t,0,-t-1) != 0); corner ([1:0],[1:0]) has
F = -t != 0, not on the curve. Hence the projective kernel curve is a smooth
bidegree-(2,2) curve, of genus (2-1)(2-1) = 1, for every t in (0,1/4).

## 3. Infinite walk group via a fixed-point eigenvalue certificate
Exact rational orbit ledger (artifact t1b.py): theta^n(1,1) for n = 0..15 are
16 distinct positive rational points with strictly growing digit lengths
(e.g. step 11 has 25/28-digit coordinates), and pullback total degrees of
theta^n as rational maps (exact Poly-gcd cancellation, artifact t1c.py) are
1,2,4,7,11,15,21 for n = 0..6. These prove order exceeding 16 but a finite
computation cannot exclude a large finite order, so the proof uses eigenvalues.
Fixed point: theta(x,y) = (x,y) iff x^2 y = 1 and x/(1+xy) = y. With y = 1/x^2
the second condition is u^2/(u+1) = 1/u^2, i.e. u^4 - u - 1 = 0. The quartic
u^4-u-1 has f(1.2207) = -2766880299199/10^16 < 0 and f(1.2208) > 0 (exact
fractions), so a real root u* in (1.2207,1.2208) exists; p* = (u*,1/u*^2) is a
theta-fixed point (positive quadrant).
Jacobian (artifact t7 derivation): Dtheta has trace Tr = -x^2/(xy+1)^2 - 1/(x^2 y)
and det = 1/(xy^2(xy+1)). On y = 1/x^2: Tr| = -x^4/(x+1)^2 - 1,
Det| = x^4/(x+1). At x = u* with u*^4 = u*+1: Det = 1 and
Tr =: T* = -1/(u*+1) - 1 in (-1.45031,-1.45028) (exact endpoint fractions).
Resultant elimination of u between u^4-u-1 and (T+1)(u+1)+1 = 0 gives the exact
trace polynomial fT(T) = T^4+9T^3+27T^2+35T+17 (hand-checkable: w = 1/(u+1)
satisfies w^4-5w^3+6w^2-4w+1 = 0 via Res_u(u^4-u-1, w(u+1)-1); then T = -1-w;
fT(-1-w) = w^4-5w^3+6w^2-4w+1 expands to the same; artifact t4_trace.py).
Since Det = 1, the eigenvalues {lam, lam^{-1}} satisfy lam+lam^{-1} = T*.
If theta had finite order n, D(theta^n)(p*) = Dtheta(p*)^n = I, so lam would be
a root of unity, lam = e^{2pi i k/m}, and T* = 2cos(2pi k/m) with [Q(T*):Q] =
phi(m)/2 (for the standard Niven/Lehmer classification; m >= 3 since T* is not
in {2,-2,0,+-1}).
Irreducibility: fT mod 3 = T^4-T-1; Rabin test (artifact t12_lintrace.py):
gcd(T^3-T,fT) = gcd(T^9-T,fT) = 1 mod 3 and fT | T^81-T mod 3, certifying
irreducibility over F3, hence over Q. So [Q(T*):Q] = 4, forcing phi(m) = 8,
m in {15,16,20,24,30}. The five cyclotomic trace polynomials
T^4-T^3-4T^2+4T+1, T^4-4T^2+2, T^4-5T^2+5, T^4-4T^2+1, T^4+T^3-4T^2-4T+1
(computed as sqrt(Res_y(Phi_m(y), y^2-Ty+1))) are each different from fT.
Contradiction. Hence no finite n exists: theta has infinite order and G(S2)
is infinite. The word is theta = Psi o Phi, explicitly
(x,y) -> (1/(xy), x/(1+xy)).

## 4. Cramer saddlepoint, growth constant, correlation, exponent
North drift m = (0,1/4) (mean of the four steps). Cramer function
L(a,b) = (e^{-a}+e^{-b}+e^{b}+e^{a+b})/4. Stationarity: e^{a+b} = e^{-a} and
e^{b}+e^{a+b} = e^{-b}, whence b = -2a and with u = e^a: u^4-u-1 = 0, the same
quartic; v := e^b = 1/u^2. Saddlepoint value Smin = 2/u+u^2+1/u^2 =: rho
(= Z, the twisted normalization). Exponentially twisted weights
w_W = 1/u, w_S = u^2, w_N = 1/u^2, w_NE = 1/u give twisted mean zero and
covariances Exx = (2/u)/Z, Exy = (1/u)/Z, Eyy = (u^2+1/u^2+1/u)/Z.
Correlation r = Exy/sqrt(Exx Eyy) satisfies exact identity
r^2 = u/(2(u^4+u+1)) (symbolic cancellation, artifact t3_minpoly.py).
Numerics at 50 digits (artifact t2_saddle.py): u* = 1.22074408460575...,
rho = 3.79960475359607..., r = 0.37070894172584...,
p := pi/arccos(-r) = 1.61060355244795....
Rigorous enclosures (artifact t11_intervals.py, exact Fractions + proved
monotonicity: g(u) = u/(2(u^4+u+1)) decreasing since g'(u) has sign 1-3u^4 < 0;
S' numerator = 2(u^4-u-1)):
u* in (1.2207,1.2208) (width 1e-4); rho in (3.7993606, 3.7996048);
r in (0.3706981, 0.3707175); p in (1.6105959, 1.6106132) (width ~1.8e-5).
These are the Denisov-Wachtel cone parameters (rho = excursion growth constant,
p = cone exponent combination); their identification as excursion asymptotics
uses cited cone machinery (see Limitations).

## 5. Irrationality of the cone exponent
Put R = r^2. Eliminating u between R = u/(2(u^4+u+1)) and u^4-u-1 = 0 gives
256R^4+64R^3-48R^2+12R-1 = 0 (resultant, artifact t3_minpoly.py). Put
T2 = -2r (so T2 = zeta+zeta^{-1} with zeta = e^{i arccos(-r)}); then
T2^2 = 4R and T2 satisfies hT(T2) = 0 with
hT(T) = T^8+T^6-3T^4+3T^2-1 (substitute R = T^2/4; artifact t6 derivation).
hT is irreducible over Q: mod 3 it is T^8+T^6-1 with
gcd(T^3-T,hT) = gcd(T^9-T,hT) = gcd(T^81-T,hT) = 1 and hT | T^{3^8}-T mod 3
(Rabin test, artifact t8_irred_cert.py), so [Q(T2):Q] = 8.
If arccos(-r)/pi = k/m were rational, T2 = 2cos(pi+... ) = 2cos(theta') for a
rational angle, with [Q(T2):Q] = phi(N)/2 for some N; degree 8 forces
phi(N) = 16, N in {17,32,34,40,48,60}. The six corresponding trace polynomials
(sqrt(Res_y(Phi_N(y),y^2-Ty+1))) are respectively
T^8+T^7-7T^6-6T^5+15T^4+10T^3-10T^2-4T+1 (N=17),
T^8-8T^6+20T^4-16T^2+2 (N=32),
T^8-T^7-7T^6+6T^5+15T^4-10T^3-10T^2+4T+1 (N=34),
T^8-8T^6+19T^4-12T^2+1 (N=40),
T^8-8T^6+20T^4-16T^2+1 (N=48),
T^8-7T^6+14T^4-8T^2+1 (N=60),
none equal to hT (artifact t8_irred_cert.py). Hence arccos(-r)/pi is irrational,
i.e. p = pi/arccos(-r) in (1.6105959,1.6106132) is irrational as a number.

## 6. What is NOT proved (limitations)
Full target additionally needs: excursion prefactor kappa, verification of the
Denisov-Wachtel hypotheses for S2, unique dominant singularity of the excursion
/ y-boundary series, and transfer of the irrational exponent to a BRS-type
non-D-finiteness conclusion for Q(0,1;t). Those analytic steps are not done
here; the irrationality proved is for the explicit algebraic number p above,
whose identification with the y-boundary singular exponent relies on cited cone
machinery. The contribution is therefore reported as an emergent finding, not
the complete target.

## 7. Replay
Run scripts in output/artifacts in order:
s1.py s2.py (discriminants) -> t10_infty.py (boundary smoothness) ->
t1b.py t1c.py (orbit/degrees) -> t2_saddle.py t11_intervals.py (constants) ->
t3_minpoly.py t4_trace.py t12_lintrace.py t8_irred_cert.py (polynomials +
Rabin certificates) -> t9_verifyall.py (master exact replay, VERIFY_OK).
