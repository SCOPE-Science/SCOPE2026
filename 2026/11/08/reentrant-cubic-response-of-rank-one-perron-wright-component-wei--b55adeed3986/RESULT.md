# Exact cubic critical-radius response for positive rank-one Perron–Wright kernels

## Finding

Let \(S\) be a nonempty finite type set, let \(\mu\) give strictly positive mass to every type, and let \(u:S\to(0,\infty)\) satisfy \(\mathbb E_\mu u=1\). Define
\[
\alpha=\mathbb E_\mu u^2,\qquad \beta=\mathbb E_\mu u^3,\qquad
\gamma=\mathbb E_\mu u^4,\qquad
\kappa(x,y)=\frac{u(x)u(y)}{\alpha}.
\]
The rank-one operator \(Kf(x)=\int\kappa(x,y)f(y)\,\mu(dy)\) has Perron eigenvalue one. For the analytic rooted-tree critical radius \(\rho(t)\) of the Perron–Wright connected-graph model with edge-intensity tilt \(t\) and gauge \(g_t(x)=\log t-(t-1)u(x)/\alpha\), normalized by \(\rho(1)=1\), one has, as \(\varepsilon\to0\),
\[
\boxed{\log\rho(1+\varepsilon)
=\frac{\alpha^2}{2\beta}\varepsilon^2
+\frac{\alpha^2(3\alpha^2\beta+\alpha\gamma-6\beta^2)}{6\beta^3}\varepsilon^3
+O(\varepsilon^4).}
\]
This identifies the first nonquadratic critical-radius coefficient explicitly in three Perron moments. It is **not** a statement about fixed-surplus connected-graph enumerators at a \(k^{-1/3}\) tilt: that separate transfer requires a uniform enumeration estimate on the indicated scale, which is not established here.

The cubic coefficient \(\mathfrak c_3\) has both signs and exhibits two reversals in a strictly positive two-type family. For \(0<a<1\), let the types take values \(1-a\) and \(21\) with respective masses \(20/(20+a)\) and \(a/(20+a)\). Then \(\mathbb Eu=1\) and
\[
\operatorname{sgn}\mathfrak c_3=-\operatorname{sgn}Q(a),\qquad
Q(a)=13000a^4-325210a^3+509550a^2-2860a+1.
\]
The polynomial has exactly two simple roots \(0<a_-<a_+<1\), isolated by
\[
0.00037<a_-<0.00038,\qquad 0.00525<a_+<0.00527.
\]
Consequently \(\mathfrak c_3<0\) for \(0<a<a_-\) and \(a_+<a<1\), \(\mathfrak c_3>0\) for \(a_-<a<a_+\), and it vanishes at the endpoints. At \(a=1/200\), \((\alpha,\beta,\gamma)=(11/10,6599/2000,19835201/400000)\) and \(\mathfrak c_3=5826325450/862096019397>0\); for the single-type kernel \(\mathfrak c_3=-1/3\).

## Assumptions and scope

The type set is fixed and finite, \(u\) and all type masses are strictly positive, and the normalization of the kernel and edge tilt is exactly as stated. The conclusion is a local identity of an analytic critical radius, not a distributional limit, a claim of universality for arbitrary kernels, or a proof of an asymptotic for connected graph weights at a shrinking \(k^{-1/3}\) tilt. The standard analytic existence and local uniqueness of the critical pair are inherited from the finite-type Perron–Wright theory; their rank-one reduction and Taylor coefficients are verified below.

## Proof

**1. Scalar critical-pair parameterization.** Write \(F_j(z)=\mathbb E_\mu[u^je^{zu}]\) for \(j\ge1\). In the cited rooted-tree gauge, the critical pair solves
\[
\tau(x)=\rho t\exp\!\left(-\frac{t}{\alpha}u(x)+(K\tau)(x)\right),
\]
and the Perron eigenvalue of its derivative \(M_\tau K\) equals one. Rank one gives \((K\tau)(x)=u(x)m\), with \(m=\alpha^{-1}\mathbb E[u\tau]\). Set \(z=m-t/\alpha\). Thus \(\tau(x)=\rho t e^{zu(x)}\), \(m=\rho tF_1(z)/\alpha\), and \(1=\rho tF_2(z)/\alpha\). Eliminating \(m\) and \(\rho\) yields the exact local parameterization
\[
\boxed{t=\alpha\left(\frac{F_1(z)}{F_2(z)}-z\right),\qquad
\rho=\frac{\alpha}{tF_2(z)}.}
\]
At \(z=0\), one has \(F_1(0)=1\), \(F_2(0)=\alpha\), and \((t,\rho)=(1,1)\). Differentiation gives \(t'(0)=-\beta/\alpha\ne0\), so the analytic inverse \(z=z(t)\) exists in a neighborhood of \(t=1\).

**2. Third-order radius coefficient.** The finite type set makes \(F_j\) entire. With \(\delta=\mathbb Eu^5\),
\[
F_1(z)=1+\alpha z+\frac{\beta}{2}z^2+\frac{\gamma}{6}z^3+O(z^4),\quad
F_2(z)=\alpha+\beta z+\frac{\gamma}{2}z^2+\frac{\delta}{6}z^3+O(z^4).
\]
Analytic series inversion gives
\[
z=-\frac{\alpha}{\beta}\varepsilon
-\frac{\alpha(\alpha^2\beta+\alpha\gamma-2\beta^2)}{2\beta^3}\varepsilon^2
+O(\varepsilon^3),\qquad \varepsilon=t-1.
\]
For the cubic coefficient one also inverts the third-order term, then substitutes into
\(\log\rho=\log\alpha-\log(1+\varepsilon)-\log F_2(z)\).
The fifth-moment terms cancel identically, leaving zero linear term and the displayed quadratic and cubic coefficients. This is a formal-power-series calculation in a genuine analytic inverse, so the remainder is \(O(\varepsilon^4)\), not a finite-difference extrapolation.

**3. Two-type sign classification.** For the displayed masses, direct expansion verifies their sum and mean both equal one, and
\[
3\alpha^2\beta+\alpha\gamma-6\beta^2=-2Q(a).
\]
As \(\alpha,\beta>0\), this determines the cubic sign. The derivative \(Q''(a)=156000a^2-1951260a+1019100\) is positive on \([0,1/2]\); it decreases there and is \(82470\) at \(1/2\). Also, for \(1/2\le a\le1\),
\[
Q'(a)=a(52000a^2-975630a+1019100)-2860>0,
\]
because the parenthesis is at least \(95470\). Since \(Q'(0)=-2860\), \(Q(0)=1\), \(Q(1/1000)<0\), and \(Q(1/100)>0\), strict convexity on the first half and strict increase on the second show exactly two simple roots in \((0,1)\). Rational evaluation gives the announced brackets. Substitution at \(a=1/200\) gives the stated exact positive coefficient; the homogeneous model has \(\rho(t)=e^{t-1}/t\), hence cubic coefficient \(-1/3\).

## Verification and precise limits

The existing `verify.py` checks the analytic series reversion, fifth-moment cancellation, two-type polynomial identity, rational root barriers, and finite weighted-tree identities. An independent exact symbolic derivation reproduced the cubic coefficient and sign factorization. These checks do not prove a connected-enumerator limit at \(k^{-1/3}\), and that limit is **not included in this finding**. The fact that the source's uniform fixed-surplus formula is publicly advertised for \(|t-1|\le Lk^{-1/2}\) does not by itself justify applying it on the larger \(k^{-1/3}\) scale. No conclusion is asserted about that transfer without an additional proved uniformity argument.

## Relationship to prior work

Hu and Sun, *Perron–Wright asymptotics and critical component processes for regular inhomogeneous random graphs*, arXiv:2610.23003v1 (October 16, 2026), establish the analytic critical radius and identify its quadratic response in \(\alpha,\beta\); their stated expansion leaves the cubic coefficient in an \(O(|t-1|^3)\) term. The finding here is its exact rank-one third-order derivative and nonuniversal, twice-reversing sign pattern. Their connected-graph enumeration theorem is not reasserted or extended. Bhamidi, Sen and Wang (arXiv:1404.4118) and Bollobás, Janson and Riordan (doi:10.1002/rsa.20168) provide underlying inhomogeneous-random-graph theory without an identified identical coefficient in inspected materials. An equivalent third derivative in unpublished or differently normalized saddlepoint work is a residual priority risk. No external verification is claimed.

## References

1. W. Hu and W. Sun, *Perron–Wright asymptotics and critical component processes for regular inhomogeneous random graphs*, arXiv:2610.23003v1, https://arxiv.org/abs/2610.23003v1.
2. S. Bhamidi, S. Sen and X. Wang, *Continuum limit of critical inhomogeneous random graphs*, arXiv:1404.4118, https://arxiv.org/abs/1404.4118.
3. B. Bollobás, S. Janson and O. Riordan, *The phase transition in inhomogeneous random graphs*, Random Structures & Algorithms 31 (2007), 3–122, https://doi.org/10.1002/rsa.20168.
