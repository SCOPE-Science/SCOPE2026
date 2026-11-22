# A sharp three-site positivity transition and quadratic noise blowup in Fourier quadrature

## Finding

Let \(N=2m+1\ge3\) be odd and \(h=2\pi/N\). Starting with the uniform circle grid, move only the nodes at \(0\) and \(2h\) symmetrically toward the **stationary** node at \(h\):
\[
x_0=uh,\qquad x_1=h,\qquad x_2=(2-u)h,\qquad
x_j=jh\ (3\le j<N),\qquad 0\le u<1.
\]
There is a unique real quadrature \(Q_{N,u}(p)=\sum_{j=0}^{N-1}w_j(u)p(x_j)\) exact for normalized circle integration on every trigonometric polynomial of degree at most \(m\). Define, for \(0<u<1\),
\[
s=\frac\pi N,\quad f(y)=\csc(sy),\quad S_N(u)=f(u)-f(2-u),\quad
R_N(u)=\frac{2f(1-u)}{S_N(u)}.
\]
The function \(R_N\) is strictly increasing from \(0\) to \(+\infty\). Consequently, a unique \(u_N\in(0,1/2)\) solves \(R_N(u_N)=1\), and **all quadrature weights are nonnegative exactly for \(0\le u\le u_N\)**. Every weight other than the stationary middle weight remains strictly positive throughout \(0\le u<1\); the middle weight alone changes sign, from positive to zero to negative.

The exact sharp amplification of arbitrary bounded sample errors is
\[
\boxed{\ \|Q_{N,u}\|_{\ell^\infty\to\mathbb C}
=\sum_{j=0}^{N-1}|w_j(u)|
=1+\frac2N\max\{0,R_N(u)-1\}.\ }
\]
The transition has a nontrivial large-grid limit with a second-order correction:
\[
\boxed{\ u_N=1-\frac1{\sqrt2}-\frac{\pi^2}{24\sqrt2\,N^2}+O(N^{-4})\quad(N\to\infty,\ N\text{ odd}).\ }
\]
As all three local nodes collide, the optimal noise amplification diverges **quadratically**, with an exact finite-grid coefficient:
\[
\boxed{\ \lim_{u\uparrow1}(1-u)^2\sum_j|w_j(u)|
=\frac{2\sin^2(\pi/N)}{N(\pi/N)^2\cos(\pi/N)}.\ }
\]

## Assumptions and scope

The circle is \(\mathbb R/(2\pi\mathbb Z)\). Integration is \(I(p)=(2\pi)^{-1}\int_0^{2\pi}p(x)\,dx\). The polynomial space is \(\mathcal T_m=\operatorname{span}\{e^{ikx}: -m\le k\le m\}\), of dimension \(N\). The grid nodes in the display are distinct for every \(0\le u<1\), so Fourier interpolation and the associated exact quadrature are unique. The boundary \(u=1\), where three sites coincide, is excluded; only its one-sided amplification asymptotic is claimed. At \(u=0\), all weights equal \(1/N\) and the formulas below are interpreted by continuity.

For \(0<u<1\), the **complete exact weights** are
\[
w_0(u)=w_2(u)=\frac1{\sin(\pi u)S_N(u)},\qquad
w_1(u)=\frac{1-R_N(u)}N,
\]
\[
w_j(u)=\frac1N\left[1-\frac{(-1)^j\bigl(f(j-2+u)-f(j-u)\bigr)}{S_N(u)}\right],
\quad 3\le j<N.
\]
Every denominator in these formulas is positive. In particular \(S_N(u)>0\).

## Proof

**1. Fourier interpolation and the exact weight identities.** The Dirichlet kernel \(D_m(t)=\sum_{k=-m}^m e^{ikt}=\sin(Nt/2)/\sin(t/2)\), with continuous values at its removable singularities, gives the uniform-grid Lagrange cardinal functions
\[
\ell_j(x)=N^{-1}D_m(x-jh),\qquad
p(x)=\sum_{j=0}^{N-1}\ell_j(x)p(jh),\qquad
I(p)=N^{-1}\sum_{j=0}^{N-1}p(jh).
\]
For the two moving sites let \(a=\ell_0(x_0)=\ell_2(x_2)\) and \(b=\ell_2(x_0)=\ell_0(x_2)\). The Dirichlet sine identity gives
\[
a+b=\frac{\sin(\pi u)}N\left[\csc(su)-\csc(s(2-u))\right]
=\frac{\sin(\pi u)}N S_N(u)>0.
\]
Adding the interpolation identities for \(p(x_0)\) and \(p(x_2)\) and solving for \(p(0)+p(2h)\) produces
\[
p(0)+p(2h)=\frac{p(x_0)+p(x_2)-\sum_{j\ne0,2}\bigl(\ell_j(x_0)+\ell_j(x_2)\bigr)p(jh)}{a+b}.
\]
Substitution into the uniform quadrature formula yields \(w_0=w_2=1/[N(a+b)]\) and \(w_j=N^{-1}[1-(\ell_j(x_0)+\ell_j(x_2))/(a+b)]\) for other sites. Applying \(D_m(\ell h)=\sin(\pi\ell)/\sin(s\ell)\) to the shifted noninteger arguments gives exactly the displayed complete weight formulas. Because the nodes remain distinct, this is the unique exact quadrature. In particular \(\sum_jw_j=1\).

**2. Only the stationary middle weight can be nonpositive.** On \((0,N)\), the function \(f(y)=\csc(sy)\) is symmetric, \(f(N-y)=f(y)\), and strictly convex, since
\[
f''(y)=s^2 f(y)\bigl(1+2\cot^2(sy)\bigr)>0.
\]
It decreases as the distance from the nearest endpoint grows on the first half-period. Because \(0<u<1\), the point \(u\) is closer to an endpoint than \(2-u\), hence \(S_N(u)>0\). The two moving-node weights are therefore positive.

When \(N\ge5\), set \(d=2(1-u)>0\) and \(G(v)=f(v)-f(v+d)\). Strict convexity makes \(G\) strictly decreasing wherever defined. Writing \(\Delta_j=G(j-2+u)\), \(3\le j<N\), gives
\[
\Delta_3=f(1+u)-f(3-u)>0,
\qquad \Delta_{N-1}=f(3-u)-f(1+u)=-\Delta_3.
\]
The first inequality follows from \(1+u<3-u\) and \(1+u<N-3+u\), so \(1+u\) lies closer to an endpoint than \(3-u\). Hence \(|\Delta_j|\le\Delta_3=G(1+u)<G(u)=S_N(u)\). The formula for \(w_j\) now yields \(w_j>0\) for every \(3\le j<N\). For \(N=3\) there are no such indices. Thus only \(w_1=(1-R_N)/N\) can fail positivity.

**3. A unique sharp crossing.** The derivative \(f'\) is strictly increasing. Using the reflection identity for \(f\),
\[
S_N'(u)=f'(u)+f'(2-u)=f'(u)-f'(N-2+u)<0,
\]
because \(N-2+u>u\). At the same time \(f(1-u)\) is strictly increasing as a function of \(u\), since \(f'<0\) on \((0,1)\). Thus the positive quotient \(R_N(u)=2f(1-u)/S_N(u)\) is strictly increasing. The endpoint expansions \(f(u)\sim1/(su)\) as \(u\downarrow0\), and \(S_N(1-\varepsilon)\sim2s\cos(s)\varepsilon/\sin^2(s)\) as \(\varepsilon\downarrow0\), imply \(R_N(0+)=0\), \(R_N(1-)=\infty\). There is exactly one crossing. Since \(R_N(1/2)=2f(1/2)/[f(1/2)-f(3/2)]>2\), it occurs strictly below \(1/2\). Together with step 2, this proves the full positivity phase portrait.

**4. Exact amplification and the large-grid critical point.** Since all weights other than \(w_1\) are positive and their total sum is one,
\[
\sum_j|w_j|=1+2\max(0,-w_1)=1+\frac2N\max\{0,R_N-1\}.
\]
This sum is the exact norm against sample errors bounded by one, because choosing the sign of each error to match the corresponding real weight attains it.

To derive the large-grid expansion, put \(s=\pi/N\) and set
\[
F(u)=\frac2{1-u}-\frac1u+\frac1{2-u}.
\]
The equation \(R_N(u)=1\) is equivalent to \(2f(1-u)-f(u)+f(2-u)=0\). Expanding \(s\csc(sy)=y^{-1}+s^2y/6+O(s^4)\), uniformly near its simple root, gives
\[
0=F(u)+\frac23(1-u)s^2+O(s^4).
\]
The unique root of \(F\) in \((0,1)\) is \(u_*=1-1/\sqrt2\), and \(F'(u_*)=16\). The implicit root expansion therefore gives
\[
u_N=u_*-\frac{(2/3)(1-u_*)}{16}s^2+O(s^4)
=1-\frac1{\sqrt2}-\frac{\pi^2}{24\sqrt2\,N^2}+O(N^{-4}).
\]

**5. Triple-collision divergence.** Set \(\varepsilon=1-u\). Elementary Taylor expansions at \(s\) yield
\[
f(\varepsilon)\sim\frac1{s\varepsilon},\qquad
S_N(1-\varepsilon)=f(1-\varepsilon)-f(1+\varepsilon)
\sim\frac{2s\cos s}{\sin^2 s}\,\varepsilon.
\]
Consequently
\[
R_N(1-\varepsilon)\sim
\frac{\sin^2s}{s^2\cos s}\,\varepsilon^{-2}.
\]
In the negative-weight regime, use the exact amplification formula of step 4 to obtain the claimed coefficient \(2\sin^2s/(Ns^2\cos s)\). The cosine is positive for every odd \(N\ge3\), so the divergence is genuine.

## Verification

The standalone `check.py` requires only the Python standard library. Running `python check.py` prints `PASS 7820 numerical assertions across odd Fourier grids, exactness, positivity, critical point and blowup`. It tests odd lengths through \(101\), many parameters on both sides of the calculated boundary, all Fourier moments through degree \(m\), the positivity pattern and the sharp amplification formula; it also checks second-order threshold asymptotics up to length \(1201\) and the fixed-size collision coefficient. A separate direct numerical inversion of the Fourier-Vandermonde system agreed with the explicit weights on sizes \(3,5,7,9,17,31\). Finite checks are not the proof for all odd lengths; the analytic argument in steps 1–5 establishes that conclusion.

## Relationship to prior work

Austin's dissertation [1], Chapter 3.5.2, and Austin–Trefethen [2] study interpolatory Fourier quadrature on perturbed equispaced nodes, including absolute-weight amplification, but do not derive the localized, sharp three-site transition. Yu–Townsend [3], Theorem 4.1, establishes that *alternating perturbation of many nodes* can make a central quadrature weight negative for arbitrarily small displacement when the grid is sufficiently large; its general estimates do not imply this exact two-node deformation, its isolated negative middle weight or its closed critical limit.

The publicly available result [4] analyzes a different geometry: it moves an **adjacent pair inward toward each other** and finds positive quadrature weights through double collision, with linear vanishing of a Fourier singular value. In contrast, here the **two outer nodes of a consecutive triple approach a stationary middle node**, causing exactly one negative quadrature weight and quadratic sample-noise amplification near *triple* collision. Neither result is a corollary of the other as stated. The distinction between two-point and three-point crowding is the principal structural motivation, not a claim about a universally worst perturbation pattern.

## Limitations

Only the explicitly prescribed two-node symmetric deformation of an odd full-rank periodic Fourier grid is classified. This is a statement about exact quadrature weights and worst-case bounded errors, not a theorem on Fourier-interpolant convergence for an arbitrary function or arbitrary grid perturbations. It does not determine the condition number of the full interpolation matrix or claim any stability at the collision itself. The asymptotic critical expansion is for increasing odd \(N\); the blowup coefficient is for each fixed odd \(N\). A search and direct source comparison support best-knowledge priority but do not amount to an independent historical audit.

## References

[1] A. P. Austin, *Some New Results on and Applications of Interpolation in Numerical Computation*, DPhil thesis, University of Oxford (public repository deposit December 8, 2016), Chapter 3.5.2. https://ora.ox.ac.uk/objects/uuid:11c16937-4a59-494d-a06f-6d27b634e2f3 . Accessible text: https://personal.math.vt.edu/apaustin/pubs/DPhilThesis.pdf .

[2] A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018v1 (first public December 13, 2016), SIAM Journal on Numerical Analysis 55 (2017), 2113–2122. https://arxiv.org/pdf/1612.04018 .

[3] A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722v1 (first public February 9, 2022), Section 4 and Appendix B. https://arxiv.org/pdf/2202.04722 .

[4] *Positive Fourier quadrature survives symmetric pair collision with a sharp singular-value law*, publicly available mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-positive-fourier-quadrature-survives-symmetric-pair-collision-wi--92a65f43a0d4 .
