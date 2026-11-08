# Fractional circle smoothing detects the antipodal Diophantine exponent

## Finding

On the unit circle \(\mathbb T=\mathbb R/\mathbb Z\), let \(S_{t,s}\) be the fractional diffusion Fourier multiplier
\[
\widehat {S_{t,s}f}(n)=e^{-t|n|^s}\widehat f(n),\qquad t>0,\quad 0<s\le 2,\quad n\in\mathbb Z,
\]
and let \(U_\alpha f(x)=f(x+\alpha)\). Put
\[
M_{\alpha,s}(t)=\|S_{t,s}(I-U_\alpha)\|_{L^2(\mathbb T)\to L^2(\mathbb T)},\qquad
\Delta_{\alpha,s}(t)=2-M_{\alpha,s}(t).
\]
The following classification holds.

**Irrational angles.** If \(\alpha\notin\mathbb Q/\mathbb Z\), define its fixed-target (antipodal) approximation exponent by
\[
\tau_{1/2}(\alpha)=\limsup_{n\to\infty}
\frac{-\log\operatorname{dist}(n\alpha,1/2+\mathbb Z)}{\log n}
\in[1,+\infty].
\]
With the convention that the displayed fraction below equals one when \(\tau_{1/2}(\alpha)=+\infty\), for every \(0<s\le2\),
\[
\boxed{\displaystyle
\limsup_{t\downarrow0}\frac{\log\Delta_{\alpha,s}(t)}{\log t}
=\frac{2\tau_{1/2}(\alpha)}{s+2\tau_{1/2}(\alpha)}.}
\]
In particular, if \(\alpha\) has bounded continued-fraction partial quotients, there exist positive constants \(c_{\alpha,s},C_{\alpha,s},t_0\) such that for all \(0<t<t_0\),
\[
\boxed{\displaystyle c_{\alpha,s}t^{2/(s+2)}\le\Delta_{\alpha,s}(t)
\le C_{\alpha,s}t^{2/(s+2)}.}
\]
Thus the sharp loss has order \(t^{2/3}\) for Poisson smoothing \(s=1\), and order \(t^{1/2}\) for heat smoothing \(s=2\). These statements concern an operator norm, not the norm of the commutator \([S_{t,s},U_\alpha]\), which vanishes.

**Rational angles.** If \(\alpha=p/q\) in lowest terms with \(q\ge2\), then for all sufficiently small \(t>0\): if \(q\) is even,
\[
M_{\alpha,s}(t)=2e^{-t(q/2)^s},\qquad
\Delta_{\alpha,s}(t)\sim2(q/2)^s t;
\]
if \(q\) is odd,
\[
M_{\alpha,s}(t)=2\cos\!\left(\frac\pi{2q}\right)e^{-tn_*^s},
\qquad
\lim_{t\downarrow0}\Delta_{\alpha,s}(t)
=2-2\cos\!\left(\frac\pi{2q}\right)>0,
\]
where \(n_*\) is the least positive integer whose residue \(pn_*\bmod q\) is \((q-1)/2\) or \((q+1)/2\). For integral \(\alpha\), the operator vanishes and \(\Delta_{\alpha,s}\equiv2\).

## Assumptions and scope

All operator norms use normalized Haar measure on \(\mathbb T\) and complex \(L^2\). The fixed angle \(\alpha\) is taken modulo integers, \(s\) is fixed in \((0,2]\), and \(t\downarrow0\). The antipodal exponent involves approximations to \(1/2+\mathbb Z\), **not** ordinary approximation to \(\mathbb Z\). The constants in the bounded-type result can depend on \(\alpha\) and \(s\). For irrational angles the deficiency is positive at every \(t>0\), tends to zero as \(t\downarrow0\), and its logarithm is therefore well defined for sufficiently small \(t\).

## Proof

**1. Exact Fourier diagonalization.** The character \(e_n(x)=e^{2\pi i n x}\) is an eigenvector of \(S_{t,s}(I-U_\alpha)\) with eigenvalue \(e^{-t|n|^s}(1-e^{2\pi i n\alpha})\). The spectral norm is therefore
\[
M_{\alpha,s}(t)=\sup_{n\ge1}2e^{-tn^s}|\sin(\pi n\alpha)|.
\]
For \(\delta_n=\operatorname{dist}(n\alpha,1/2+\mathbb Z)\in[0,1/2]\), the absolute sine equals \(\cos(\pi\delta_n)\). Therefore, defining
\[
E_n(t)=2\big(1-e^{-tn^s}\cos(\pi\delta_n)\big),
\qquad \Delta_{\alpha,s}(t)=\inf_{n\ge1}E_n(t),
\]
we have the two-sided numerical inequality
\[
 c\min\{1,tn^s+\delta_n^2\}\le E_n(t)
 \le C\min\{1,tn^s+\delta_n^2\},\tag{1}
\]
for universal \(c,C>0\). Indeed for \(x=tn^s\le1\), use \(1-e^{-x}\ge(1-e^{-1})x\), \(e^{-x}\ge e^{-1}\), and \(1-\cos(\pi u)\ge2u^2\) for \(0\le u\le1/2\); when \(x>1\), \(E_n\ge2(1-e^{-1})\). The upper inequality follows from \(1-e^{-x}\le x\), \(1-\cos(\pi u)\le\pi^2u^2/2\), and \(E_n\le2\). Thus whenever
\[
F_{\alpha,s}(t)=\inf_{n\ge1}(tn^s+\delta_n^2)\longrightarrow0,
\]
the deficit satisfies \(\Delta_{\alpha,s}(t)\asymp F_{\alpha,s}(t)\) with absolute comparison constants. For irrational \(\alpha\), density of its positive rotation orbit supplies indices with arbitrarily small \(\delta_n\), and hence \(F_{\alpha,s}(t)\to0\) by first fixing an index and then taking small \(t\).

**2. The exponent identity.** For irrational \(\alpha\), let \(\tau=\tau_{1/2}(\alpha)\). One first has \(\tau\ge1\). To see this, let \(p_k/q_k\) be convergents of \(\alpha\), select an integer \(j_k\) nearest to \(q_k/2\), and solve \(n_k p_k\equiv j_k\pmod {q_k}\) with \(1\le n_k<q_k\) for all sufficiently large \(k\). Then
\[
\delta_{n_k}\le \frac1{2q_k}+\frac{n_k}{q_kq_{k+1}}
\le\frac3{2q_k}\le\frac3{2n_k}.
\]
The indices \(n_k\) are unbounded since no fixed positive multiple of irrational \(\alpha\) is a half-integer. This proves \(\tau\ge1\).

Suppose first \(\tau<\infty\). For any \(\eta>0\), for every sufficiently large integer \(n\), \(\delta_n\ge n^{-(\tau+\eta)}\). For the finitely many remaining indices the \(\delta_n\) have a fixed positive minimum. By (1) and the scaling minimization
\[
\inf_{x>0}\{t x^s+x^{-2a}\}
=C_{a,s}\,t^{2a/(s+2a)},\qquad a>0,
\]
we obtain \(\Delta_{\alpha,s}(t)\ge c_{\eta,\alpha,s}t^{2(\tau+\eta)/(s+2(\tau+\eta))}\) for small \(t\). Since \(\log t<0\), this gives an upper bound \(2(\tau+\eta)/(s+2(\tau+\eta))\) on the logarithmic limsup.

Conversely choose \(n_j\to\infty\) such that
\(a_j=-\log\delta_{n_j}/\log n_j\to\tau\) and put \(t_j=\delta_{n_j}^2/n_j^s\). Then \(t_j\downarrow0\), \(\Delta_{\alpha,s}(t_j)\le C\delta_{n_j}^2\), and division by the negative logarithm yields
\[
\limsup_{t\downarrow0}\frac{\log\Delta_{\alpha,s}(t)}{\log t}
\ge\lim_{j\to\infty}\frac{2a_j}{s+2a_j}
=\frac{2\tau}{s+2\tau}.
\]
Letting \(\eta\downarrow0\) completes the finite-exponent case. When \(\tau=\infty\), the same subsequence argument gives a lower bound of one for the logarithmic limsup; the universal estimate
\(\Delta_{\alpha,s}(t)\ge2(1-e^{-t})\) gives the reverse bound of one.

**3. Uniform power law for bounded type.** If the partial quotients of irrational \(\alpha\) are bounded, then for some \(b_\alpha>0\), \(\operatorname{dist}(m\alpha,\mathbb Z)\ge b_\alpha/m\) for all \(m\ge1\). Consequently \(\delta_n\ge b_\alpha/(4n)\), using \(\operatorname{dist}(2n\alpha,\mathbb Z)\le2\delta_n\). Formula (1) and minimization give the lower estimate \(c_{\alpha,s}t^{2/(s+2)}\).

For the matching upper estimate let \(Q=\lceil t^{-1/(s+2)}\rceil\), and choose \(k\) with \(q_k\le Q<q_{k+1}\). Bounded partial quotients imply \(q_{k+1}\le B_\alpha q_k\), so \(q_k\ge Q/B_\alpha\). The modular-grid construction of Step 2 yields some \(1\le n<q_k\le Q\) with \(\delta_n\le3/(2q_k)\le3B_\alpha/(2Q)\). Therefore
\[
F_{\alpha,s}(t)\le tQ^s+\frac{9B_\alpha^2}{4Q^2}
\le C_{\alpha,s}t^{2/(s+2)},
\]
and (1) proves the claim for every sufficiently small \(t\).

**4. Rational classification.** Let \(\alpha=p/q\) be reduced. The angular values \(2|\sin(\pi np/q)|\) are periodic modulo \(q\). If \(q\) is even, the maximum value two occurs exactly when \(n\equiv q/2\pmod q\), because \(p\) is odd. The least such positive \(n\) is \(q/2\). All other residue classes have strictly smaller angular factor, hence cannot beat this class when \(t>0\) is sufficiently small, giving the first exact formula. If \(q\ge3\) is odd, the maximal angular factor is \(2\cos(\pi/(2q))\), achieved precisely when \(pn\equiv(q\pm1)/2\pmod q\); among all such \(n\), the least is \(n_*\). The strict gap to other angular values again makes this the maximizer for all sufficiently small \(t\). For \(q=1\), every rotation is the identity. This completes all cases.

## Verification

The accompanying standalone `checker.py` evaluates both the Fourier multiplier norm and independently formed finite Fourier-space operators, verifies the rational parity formulas for sample denominators, and checks the anticipated scaling on several fractional powers. Invoke `python3 checker.py` in a Python environment with NumPy. Its final success marker is `FRACTIONAL_ROTATION_CHECKS_PASS 950`. These are finite, floating-point consistency tests, not substitutes for the analytic arguments establishing all integers and all positive times.

## Relationship to prior work

Fractional Poisson/heat semigroups and rotation Diophantine exponents are standard independently. Frank and Ivanisvili (arXiv:2101.06209, first posted 2021-01-15) study hypercontractive \(L^p\)-to-\(L^q\) estimates for the fractional-Laplacian semigroup on spheres, not the fixed-angle \(L^2\) multiplier deficit. Galatolo and Sorrentino (arXiv:2006.15937, first posted 2020-06-29) study quantitative statistical stability of invariant measures under perturbations of irrational rotations, a different observable and perturbation mechanism. Kleinbock and Wadleigh (arXiv:1709.04082, first posted 2017-09-12) prove a metric inhomogeneous shrinking-target theorem, rather than the exact fixed-rotation spectral exponent transfer above. The result here links these themes by an explicit minimization principle for the natural smoothed translation contrast.

## Limitations

The logarithmic statement uses a limsup; it does **not** claim a full limit of \(\log\Delta/\log t\) for every irrational angle. The bounded-type two-sided order has unspecified, angle-dependent constants, not a universally sharp leading coefficient. The theorem is restricted to \(L^2\) circle Fourier multipliers with \(0<s\le2\); no corresponding \(L^p\) operator-norm exponent for \(p\ne2\) is asserted. For angles of unbounded continued-fraction type, the precise behavior at every scale can differ from the bounded-type power law.

## References

1. D. Kleinbock and N. Wadleigh, *An Inhomogeneous Dirichlet Theorem via Shrinking Targets*, arXiv:1709.04082 (initial version 2017-09-12).
2. S. Galatolo and A. Sorrentino, *Quantitative Statistical Stability and Linear Response for Irrational Rotations and Diffeomorphisms of the Circle*, arXiv:2006.15937 (initial version 2020-06-29).
3. R. L. Frank and P. Ivanisvili, *Hypercontractivity of the Semigroup of the Fractional Laplacian on the n-Sphere*, arXiv:2101.06209 (initial version 2021-01-15).
