# Universal second-order skew-Schäffer curvature of real \(L_4\)

## Finding
Let \(X=L_4(\Omega,\mu;\mathbb R)\) have dimension at least two. For every \(1\le t\le\infty\), let
\[
\mathcal S_t(h)=\inf_{\|x\|_4=\|y\|_4=1}\mathcal M_t(\|x+h y\|_4,\|h x-y\|_4),
\]
where \(\mathcal M_t(a,b)=((a^t+b^t)/2)^{1/t}\) for finite \(t\), and \(\mathcal M_\infty(a,b)=\max\{a,b\}\). Then the entire family has **one common second-order expansion**, uniformly over its outer exponent:
\[
\boxed{\sup_{1\le t\le\infty}\left|\mathcal S_t(h)^2-\left(1-\frac{h}{\sqrt2}+\frac54h^2\right)\right|\le100h^3\quad(0\le h\le1/8).}
\]
Consequently, uniformly in \(t\),
\[
\boxed{\mathcal S_t(h)=1-\frac{h}{2\sqrt2}+\frac9{16}h^2+O(h^3)\quad(h\downarrow0).}
\]
In particular, every two outer power means produce skew-Schäffer radii that differ by \(O(h^3)\) near zero. The formula is independent of the measure space as long as \(X\) contains two disjoint nonzero elements.

## Assumptions and scope
All functions, norms, and duality pairings are real. The measure space can be atomic or nonatomic, finite- or infinite-dimensional; only two disjointly supported unit functions are needed for the upper bound. The infimum need not be attained for every positive \(h\). At \(h=0\) all radii equal one. The bound is local to \(0\le h\le1/8\); it does not assert equality of the full parameter profiles. The outer-exponent supremum includes the maximum-mean endpoint \(t=\infty\).

## Proof
Write \(\phi(z)=\|z\|_4^2\), \(P=\int x^3y\,d\mu\), \(Q=\int xy^3\,d\mu\), \(E=\int x^2y^2\,d\mu\), and \(A=P-Q\) for unit functions \(x,y\). Put
\[
G_h(x,y)=\tfrac12\bigl(\phi(x+hy)+\phi(hx-y)\bigr).
\]
At any unit \(z\), the first two directional derivatives are
\[
D\phi(z)[v]=2\int z^3v,\qquad D^2\phi(z)[v,v]=6\int z^2v^2-4\left(\int z^3v\right)^2.
\]
For any nonzero \(z\), direct differentiation of \(\phi(z)=(\int z^4)^{1/2}\) gives \(|D^3\phi(z)[v,v,v]|\le72\|v\|_4^3/\|z\|_4\). Every segment from a unit vector in a unit direction of length \(h\le1/8\) stays outside the norm ball of radius \(7/8\). Taylor's theorem therefore gives, with a conservative absolute remainder bound,
\[
\tag{1}\left|G_h-\bigl(1+hA+h^2B\bigr)\right|\le24h^3,
\qquad B=3E-P^2-Q^2.
\]

The central exact stability identity follows by expanding a quartic square:
\[
\tag{2}d:=A+\frac1{\sqrt2}=\frac1{2\sqrt2}\left\|x^2+\sqrt2xy-y^2\right\|_2^2\ge0.
\]
Set \(R=x^2+\sqrt2xy-y^2\) and \(\delta=\|R\|_2=(2\sqrt2d)^{1/2}\). The three errors \(e_1=\int Rx^2\), \(e_2=\int Ry^2\), and \(e_3=\int Rxy\) have absolute values at most \(\delta\) by Hölder. The identities
\[
e_1=1+\sqrt2P-E,\quad e_2=E+\sqrt2Q-1,\quad e_3=P+\sqrt2E-Q
\]
then imply
\[
\tag{3}|E-\tfrac12|\le\tfrac{2+\sqrt2}{4}\delta,\quad |P+\tfrac1{2\sqrt2}|,|Q-\tfrac1{2\sqrt2}|\le\tfrac{1+(2+\sqrt2)/4}{\sqrt2}\delta.
\]
As \(|P|,|Q|\le1\), these bounds yield \(|B-5/4|\le7\delta\le12\sqrt d\). They also give \(|P+Q|\le\sqrt2\delta\).

For the quadratic mean, (1)–(3) yield
\[
\tag{4}G_h\ge1-\frac h{\sqrt2}+\frac54h^2+hd-12h^2\sqrt d-24h^3.
\]
For the arithmetic mean, denote \(u=\|x+hy\|_4\) and \(v=\|hx-y\|_4\). The identity \(\mathcal M_1(u,v)^2=G_h-(u-v)^2/4\) is exact. Moreover, for \(\|z\|_4\ge3/4\), the second derivative of \(\|z\|_4\) in a unit direction has absolute value at most \(8\), so the first variations of the two norms give
\[
|u-v-h(P+Q)|\le8h^2.
\]
Using (2)–(3) and \((a+b)^2\le2a^2+2b^2\), we obtain
\[
\tag{5}\frac{(u-v)^2}{4}\le 2\sqrt2h^2d+32h^4.
\]
For \(0\le h\le1/8\), the coefficient of \(hd\) in the combination (4)–(5) is \(1-2\sqrt2h\ge1/2\). Complete the square:
\[
\frac h2d-12h^2\sqrt d=\frac h2(\sqrt d-12h)^2-72h^3.
\]
It follows that, for all unit pairs,
\[
\tag{6}\mathcal M_1(u,v)^2\ge1-\frac h{\sqrt2}+\frac54h^2-100h^3.
\]

To attain the leading coefficients simultaneously for all outer exponents, choose disjoint unit vectors \(f,g\in X\) and positive numbers \(a,b\) determined by
\[
a^2=\frac{\sqrt3-1}{2\sqrt2},\qquad b^2=\frac{\sqrt3+1}{2\sqrt2}.
\]
They satisfy \(a^4+b^4=1\) and \(ab=1/2\). Put \(x=af+bg\), \(y=bf-ag\). Then \(\|x\|_4=\|y\|_4=1\), \(P=-1/(2\sqrt2)\), \(Q=1/(2\sqrt2)\), \(E=1/2\), and the two transformed vectors have exactly the same norm for every \(h\):
\[
\|x+hy\|_4=\|hx-y\|_4.
\]
Therefore their common power mean, for **every** \(t\in[1,\infty]\), equals \(\sqrt{G_h(x,y)}\). Equation (1) gives the common upper estimate
\[
\tag{7}\mathcal S_t(h)^2\le1-\frac h{\sqrt2}+\frac54h^2+24h^3.
\]
Finally, power means increase with the exponent, so (6) gives \(\mathcal S_t(h)^2\ge\mathcal S_1(h)^2\) for all \(t\). Combining (6) and (7) proves the boxed uniform bound. Taylor expansion of the square root, valid uniformly since the radii stay close to one, gives the coefficient \(9/16\).

## Verification
The identity (2), the moment relations (3), and the explicit trial pair are checked independently by the included `verify.py`, using exact polynomial arithmetic and deterministic finite-vector tests. The analytic conclusions depend on the displayed derivative estimates and global inequalities, not on finite experiments. The proof determines the second-order curvature but not the full positive-parameter optimizer set.

## Relationship to prior work
Xu and Liu introduced the skew-Schäffer radii and calculated the exact \(L_p\) profile when the outer mean exponent equals \(p\). Their theorem therefore covers the quartic outer-mean case \(t=4\), but does not imply a lower bound for the arithmetic mean \(t=1\), or uniform curvature across \(1\le t\le\infty\). An earlier general result for uniformly smooth Banach spaces proves the common **first-order** slope for finite outer exponents, not the second-order coefficient or the endpoint-uniform estimate. A published exact calculation of a skew **supremal** mean on real \(\ell_4\) also has a different extremal direction and does not furnish the needed infimal arithmetic-mean lower bound. The new step is the quartic square-defect rigidity (2) plus its uniform second-order optimization and the arithmetic-mean comparison (5).

## Limitations
The result is for real \(L_4\), not complex \(L_4\) or other exponents. Its universal cubic remainder is deliberately conservative and does not give the exact third-order coefficient. The original first-order skewness theorem and the previously known matched-exponent formula are not claimed as new. The best-knowledge literature assessment cannot rule out an unindexed equivalent second-order theorem, and there is no independent mathematical audit.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, first posted 2 October 2026, https://arxiv.org/abs/2610.03050.
2. *Infinitesimal skew radii detect Hilbert geometry in uniformly smooth Banach spaces*, publicly indexed mathematical research result (11 October 2026), identifier 88548343e0a2.
3. *Exact skew geometric mean constant of \(\ell_4\)*, publicly indexed mathematical research result (4 October 2026), identifier 7a18ef79086d.
