# Nonlocal attainment below the local quartic entropy stability threshold on the five-cycle
## Finding
Let \(G=\mathbb Z/5\mathbb Z\) with uniform average \(\langle f\rangle=5^{-1}\sum_{j=0}^4f(j)\). Put
\[
\mu=2(1-\cos(2\pi/5))=\frac{5-\sqrt5}{2},\quad
\mathcal E_5(u)=\frac{1}{5\mu}\sum_{j=0}^4(u(j+1)-u(j))^2.
\]
For nonnegative real \(u\) with \(\langle u^2\rangle=1\), define \(d(u)=\|u-1\|_2\), \(\operatorname{Ent}(u^2)=\langle u^2\log(u^2)\rangle\), with \(0\log0=0\), and
\[
\mathcal R(u)=\frac{2\mathcal E_5(u)-\operatorname{Ent}(u^2)}{d(u)^4}\qquad(u\ne1).
\]
Let \(C_5=\inf_{u\ge0,\ \langle u^2\rangle=1,\ u\ne1}\mathcal R(u)\). The local constant at \(1\) is exactly
\[
L_5=\lim_{\rho\downarrow0}\inf_{0<d(u)<\rho}\mathcal R(u)
=\frac{7-\sqrt5}{8}=0.5954915028\ldots.
\]
The new strict global comparison is
\[
\boxed{C_5\le \mathcal R(u_*)<\frac{119}{200}<L_5,\quad
u_* =\frac{(1090,1025,925,925,1025)}{\sqrt{1000120}}.}
\]
Consequently, the global infimum \(C_5\) is attained by a nonconstant nonnegative function and every global minimizer has positive distance from \(1\). This is an existence and localization-separation theorem, not a determination of the exact global constant or of all optimizers.

## Assumptions and scope
All Fourier spaces below are real; the circle indices are taken modulo five, and \(\|u\|_2^2=\langle u^2\rangle\). The first nonzero eigenvalue of the displayed energy is one. The admissible set is the closed nonnegative \(L^2\)-unit sphere in \(\mathbb R^5\). Only nearest-neighbor energy on the five-cycle is considered; no claim is made about word-length energy, other cycle sizes, or complex-valued data.

## Proof
**1. Local threshold.** Write any \(u\) sufficiently near \(1\) uniquely as
\[
u=\frac{1+h}{\sqrt{1+s}},\quad \langle h\rangle=0,\quad s=\langle h^2\rangle.
\]
Decompose \(h=v+w\) orthogonally into the two real Fourier eigenspaces with frequencies \(\pm1\) and \(\pm2\). Put \(r^2=\langle v^2\rangle\) and \(b^2=\langle w^2\rangle\). The normalized eigenvalues are \(1\) and \(1+q\), where
\[
q=\frac{1-\cos(4\pi/5)}{1-\cos(2\pi/5)}-1=\frac{1+\sqrt5}{2}.
\]
For every real first harmonic \(v\) on the five-cycle,
\[
\langle v^3\rangle=0,\qquad \langle v^4\rangle=\frac32 r^4,\qquad
P_2(v^2)=v^2-r^2,\quad \|P_2(v^2)\|_2^2=\frac12r^4,
\]
where \(P_2\) is orthogonal projection onto the second-harmonic subspace. These identities follow directly by summing exponentials over five roots of unity (none of frequencies \(1,2,3,4\) aliases to zero).

Using \(2(1+z)^2\log(1+z)=2z+3z^2+\frac23z^3-\frac16z^4+O(z^5)\), the exact normalization \(\langle u^2\rangle=1\), and \(\mathcal E_5(h)=r^2+(1+q)b^2\), we obtain uniformly as \((r,b)\to(0,0)\)
\[
\Delta(u):=2\mathcal E_5(u)-\operatorname{Ent}(u^2)
=2q b^2-2\langle v^2w\rangle+\frac34r^4+o(b^2+r^4).
\]
Indeed the exact entropy formula is
\[
\operatorname{Ent}(u^2)=\frac{\langle2(1+h)^2\log(1+h)\rangle}{1+s}-\log(1+s),
\]
while \(\mathcal E_5(u)=\mathcal E_5(h)/(1+s)\). The omitted terms, including \(\langle vw^2\rangle\) and \(\langle w^3\rangle\), are \(o(b^2+r^4)\) uniformly since \(r,b\to0\).

If \(b/r^2\to\infty\) along a sequence (including \(r=0\)), then \(2qb^2\) dominates the other displayed terms and \(\Delta/d^4\to+\infty\). For sequences with \(b=O(r^2)\), complete the square to get
\[
\begin{aligned}
2q\|w\|_2^2-2\langle P_2(v^2),w\rangle+\frac34r^4
&=2q\left\|w-\frac{P_2(v^2)}{2q}\right\|_2^2
 +\left(\frac34-\frac1{4q}\right)r^4.
\end{aligned}
\]
Also \(d(u)^2=r^2+b^2+O((r^2+b^2)^2)\), and so every sequence \(u\to1\) has \(\liminf\mathcal R(u)\ge \frac34-\frac1{4q}=(7-\sqrt5)/8\). Conversely take \(v=\varepsilon\sqrt2\cos(2\pi j/5)\) and \(w=P_2(v^2)/(2q)\); for small positive \(\varepsilon\), the normalized \(u\) is nonnegative and achieves this limit. Thus the stated exact local threshold holds.

**2. Rationally certified nonlocal witness.** Let
\[
(x_0,x_1,x_2,x_3,x_4)=(1090,1025,925,925,1025),\qquad S=1000120,
\]
so \(u_*=x/\sqrt S\), \(\langle x\rangle=998\), and \(\langle x^2\rangle=S\). Directly,
\[
\mathcal E_5(u_*)=\frac{5690}{S}\frac{5+\sqrt5}{10},\qquad
d(u_*)^2=2\left(1-\frac{998}{\sqrt S}\right),
\]
\[
\operatorname{Ent}(u_*^2)=\frac15\sum_{j=0}^4\frac{x_j^2}{S}\log\!\left(\frac{x_j^2}{S}\right).
\]
The standalone `verify_exact.py` uses only rational arithmetic and integer-square-root brackets to bound square roots, and a rational atanh expansion with an explicit tail bound for each logarithm. It establishes strictly
\[
2\mathcal E_5(u_*)-\operatorname{Ent}(u_*^2)
<\frac{119}{200}\,d(u_*)^4
\]
and \(119/200<(7-\sqrt5)/8\). Thus \(C_5\le\mathcal R(u_*)<119/200<L_5\).

**3. Attainment away from the constant.** The admissible nonnegative unit sphere is compact. The quotient \(\mathcal R\) is continuous wherever \(u\ne1\), including at zero coordinates by continuity of \(x\log x\) at zero. A minimizing sequence cannot tend to \(1\), because its quotient values tend to \(C_5<L_5\), whereas every approach to \(1\) has liminf at least \(L_5\). A convergent subsequence therefore has a nonconstant limit, at which \(\mathcal R\) attains \(C_5\). Every minimizing point has strictly positive \(d\).

## Verification
Run `python3 verify_exact.py` using Python's standard library. All decisive comparisons are exact `Fraction` inequalities; decimal outputs are descriptive only. The witness satisfies \(\mathcal R(u_*)\approx0.5949234120988\ldots\), below \(119/200=0.595\), while the exact local constant is \(0.5954915028125\ldots\). The proof of the local lower bound and compactness is analytic, not inferred from numerical checks.

## Relationship to prior work
Chen–Lam–Lu, arXiv:2610.05347 (first submitted 2026-10-04), prove a global quartic entropy lower bound for finite cycles and provide near-constant Fourier families giving upper bounds. They do not establish the strict five-cycle comparison between the global optimal constant and the local value. The published local-threshold analysis linked below determines the local constant exactly but explicitly does not exclude a lower nonlocal competitor. The present witness supplies such a competitor and, together with the local threshold, proves nonconstant attainment. Xie–Zhang supply earlier stability estimates but no corresponding strict global-versus-local comparison for the nearest-neighbor five-cycle. Dovetta–Serra study Gaussian/EUCLIDEAN log-Sobolev optimizer existence for a different stability quotient and domain.

## Limitations
The strict gap is small but mathematically consequential: it proves a nonlocal mechanism controls the global optimization. The exact value of \(C_5\), uniqueness, symmetry and positivity of all minimizers are not resolved. The certificate verifies one explicit point; it is not an exhaustive search. Bibliographic novelty is stated relative to the materially inspected sources, not as a guarantee against all prior equivalent formulations. No independent audit has been performed.

## References
1. L. Chen, N. Lam, G. Lu, *Sharp uniform stability of the logarithmic Sobolev inequality on finite cycles and stability of the cubic Sobolev inequality*, arXiv:2610.05347, first submitted 2026-10-04. https://arxiv.org/abs/2610.05347
2. *Exact local quartic stability constants at the constant extremizer on cycles*, published result and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-local-quartic-stability-constants-at-the-constant-extremiz--3ea04e5fdc28/RESULT.md
3. X. Xie, H. Zhang, *Sharp log-Sobolev inequalities and quartic stability on finite cyclic groups*, arXiv:2606.02847. https://arxiv.org/abs/2606.02847
4. S. Dovetta, E. Serra, *Existence of optimizers for the sharp stability constant in the logarithmic Sobolev inequality*, arXiv:2606.23225. https://arxiv.org/abs/2606.23225
