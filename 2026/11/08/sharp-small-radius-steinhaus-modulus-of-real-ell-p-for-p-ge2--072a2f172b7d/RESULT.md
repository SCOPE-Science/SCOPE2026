# Sharp small-radius Steinhaus modulus of real \(\ell_p\) for \(p\ge2\)

## Finding
For a real normed space \(X\), define the two-point Steinhaus modulus and its uniform version by
\[
U_X(x,y;a)=\sup_{\|z\|\le a}\big|\|x+z\|-\|y+z\|\big|,\qquad
U_X(d;a)=\inf_{\substack{x,y\in S_X\\\|x-y\|\ge d}}U_X(x,y;a).
\]
**Theorem.** Let \(2\le p<\infty\), let \(I\) be any index set containing at least two elements, and let \(X=\ell_p(I;\mathbb R)\). For every \(0<d\le2\) and \(0<a\le1/2\),
\[
\boxed{\left|U_X(d;a)-2^{2-p}a d^{p-1}\right|\le(p-1)a^2.}
\]
In particular, for each fixed \(p,d\),
\[
\boxed{\lim_{a\downarrow0}\frac{U_X(d;a)}a=2^{2-p}d^{p-1}.}
\]
The coefficient is exact for every \(p,d\), simultaneously in every allowed dimension. It is already realized by pairs supported on two coordinates.

## Assumptions and scope
Only **real** \(\ell_p\) spaces are asserted. The index set may be finite, countably infinite, or arbitrary; vectors have at most countable nonzero support. The radius restriction \(a\le1/2\) is used for the explicit uniform remainder, not for the existence of the modulus. The distance parameter includes the endpoint \(d=2\). The little-o limit holds with \(p,d\) fixed; it is not a uniform *relative* error when \(d\) simultaneously tends to zero.

## Proof
Write \(q=p/(p-1)\). For \(x\in S_X\) define the norming functional \(J(x)\in\ell_q(I)\) by
\[
J(x)_i=|x_i|^{p-2}x_i,\qquad \langle J(x),x\rangle=\|J(x)\|_q=1.
\]
First compute the exact minimum \(K_p(d)=\inf\{\|J(x)-J(y)\|_q:\ x,y\in S_X,\ \|x-y\|_p\ge d\}\). For real scalars \(u,v\), the function \(F(t)=|t|^{p-2}t\) is increasing and
\[
(F(u)-F(v))(u-v)\ge2^{2-p}|u-v|^p.\tag{1}
\]
Indeed, for \(u>v\), the integral of \((p-1)|t|^{p-2}\) over any interval of length \(u-v\) is minimized by the interval centered at zero, on which it equals \(2^{2-p}(u-v)^{p-1}\). The cases \(u<v\) and \(u=v\) follow by symmetry. Summing (1) over coordinates and applying Hölder gives
\[
\|J(x)-J(y)\|_q\,\|x-y\|_p\ge
\langle J(x)-J(y),x-y\rangle\ge2^{2-p}\|x-y\|_p^p.
\]
Hence \(K_p(d)\ge2^{2-p}d^{p-1}\). For \(s=d/2\) and \(c=(1-s^p)^{1/p}\), choose two distinct coordinates and put
\[
x=(c,s),\qquad y=(c,-s).
\]
Both are unit vectors, \(\|x-y\|_p=d\), and \(J(x)-J(y)=(0,2s^{p-1})\). Therefore
\[
K_p(d)=2s^{p-1}=2^{2-p}d^{p-1}.\tag{2}
\]

Next show that linearization of the *norm* is uniformly quadratic on the sphere. For \(x\in S_X\), \(z\in X\), and \(\|z\|_p\le a\le1/2\), let \(f(t)=\|x+tz\|_p\) on \([0,1]\). Because \(\|x+tz\|_p\ge1-a\ge1/2\), the norm is twice differentiable along this segment. Differentiating the \(p\)-power and applying Hölder yields
\[
0\le f''(t)\le(p-1)\frac{\|z\|_p^2}{\|x+tz\|_p}\le2(p-1)\|z\|_p^2.\tag{3}
\]
For completeness, with \(v=x+tz\), \(A=\sum_i|v_i|^{p-2}v_i z_i\) and \(B=\sum_i|v_i|^{p-2}z_i^2\), the derivative identity is
\[
f''(t)=(p-1)\|v\|_p^{1-p}B-(p-1)\|v\|_p^{1-2p}A^2.
\]
The latter expression is nonnegative by Hölder, and its upper bound in (3) follows from \(B\le\|v\|_p^{p-2}\|z\|_p^2\). This reasoning also applies for \(p=2\), and passage through zero coordinates is harmless for \(p>2\). Integrating (3) with Taylor's remainder yields
\[
0\le\|x+z\|_p-1-\langle J(x),z\rangle\le(p-1)\|z\|_p^2.\tag{4}
\]
For any two unit vectors, subtracting their two nonnegative remainders in (4) shows
\[
\big|\,[\|x+z\|_p-\|y+z\|_p]-\langle J(x)-J(y),z\rangle\,\big|
\le(p-1)a^2.
\]
The supremum of the absolute value of the linear functional over \(\|z\|_p\le a\) is \(a\|J(x)-J(y)\|_q\). Taking the supremum, then the infimum over admissible pairs, proves
\[
aK_p(d)-(p-1)a^2\le U_X(d;a)\le aK_p(d)+(p-1)a^2.
\]
Inserting (2) gives the theorem.

## Verification
The proof is analytic for every real exponent, dimension and admissible radius. Four independent boundary checks are: \(d=2\) has the antipodal extremizer; \(p=2\) gives slope \(d\); the sharp scalar inequality (1) has equality for \(u=-v\); and (4) is dimension-independent. A standalone rational checker, `verify_rational.py`, tests (1) on a grid for even exponents and the exact two-coordinate sharp-coefficient identity. Such finite checks are corroboration, not substitutes for (1)–(4).

## Relationship to prior work
Johnson and Kania [1], first publicly posted February 9, 2026, introduced the exact modulus used here, computed the atomless \(L_1\) value, and established only **order** \(a d^{p-1}\) for \(\ell_p\) when \(p>2\) (Corollary 1.11). They also determined the *squared-norm* Hilbert modulus (Proposition 1.4); that is a different functional. The present theorem determines the leading coefficient for the original unsquared \(\ell_p\) modulus at every fixed distance and adds a uniform finite-radius estimate. The scalar monotonicity estimate used in the proof is classical and is not claimed as a new inequality. Kania and Kochanek [2] developed the qualitative Steinhaus property, without this quantitative coefficient.

## Limitations
No formula for the full finite-radius modulus is asserted beyond the stated quadratic enclosure, nor is any claim made for \(1\le p<2\) or for complex \(\ell_p\). The coefficient may follow from older duality-map literature not indexed under Steinhaus terminology; publication priority requires external verification. The remainder estimate is dimension-free but not claimed to have optimal second-order coefficient. Numerical verification covers only a finite rational grid.

## References
[1] W. B. Johnson and T. Kania, *Uniform Property (S)*, arXiv:2602.09106v2 (first posted 2026-02-09), especially definitions (1)–(4) and Corollary 1.11. https://arxiv.org/html/2602.09106v2

[2] T. Kania and T. Kochanek, *Steinhaus' lattice-point problem for Banach spaces*, arXiv:1302.6443v5 (first posted 2013-02-26). https://arxiv.org/abs/1302.6443
