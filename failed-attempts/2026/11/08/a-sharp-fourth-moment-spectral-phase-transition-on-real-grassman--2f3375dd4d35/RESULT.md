# A sharp fourth-moment spectral phase transition on real Grassmannians

## Finding

For every even integer \(n\ge 6\), every integer \(1\le k<n\), and every nonzero real symmetric \(n\times n\) matrix \(A\) with \(\operatorname{tr}A=0\), let \(P\) be a Haar-uniform rank-\(k\) orthogonal projector and let \(f_A(P)=\operatorname{tr}(AP)\). Define
\[
t=k(n-k),\quad D=n(n-3)(n-2)(n-1)(n+1)(n+2)(n+4)(n+6),
\]
\[
v=\frac{2t}{n(n-1)(n+2)},\quad
 a=\frac{12t\big((n^2+5n+18)t-8n^2-12n+24\big)}{D},
\]
\[
b=\frac{48t\big(n(n^2+n+2)-(5n+6)t\big)}{D}.
\]
The following identities hold *for every* admissible \(A\):
\[
\mathbb E f_A^2=v\,\operatorname{tr}(A^2),\qquad
\mathbb E f_A^4=a\big(\operatorname{tr}(A^2)\big)^2+b\operatorname{tr}(A^4).
\]
Set \(\tau_n=n(n^2+n+2)/(5n+6)\). The sharp real \(L^2\)-to-\(L^4\) fourth-power amplification on this first Grassmannian harmonic space is
\[
\boxed{\mathcal C_{n,k}^4:=\sup_{A\ne0,\,\operatorname{tr}A=0}
\frac{\|f_A\|_4^4}{\|f_A\|_2^4}
=\frac{a+bR_*}{v^2}},
\quad R_*=\begin{cases}
\frac{n^2-3n+3}{n(n-1)},&t<\tau_n,\\
\frac1n,&t\ge\tau_n.
\end{cases}
\]
When \(t<\tau_n\), equality is attained precisely by the **one-spike spectra** \(c(n-1,-1,\ldots,-1)\). When \(t>\tau_n\), equality is attained precisely by the **balanced spectra** with \(n/2\) eigenvalues \(+c\) and \(n/2\) eigenvalues \(-c\). Here \(c\in\mathbb R\setminus\{0\}\), and all classifications allow orthogonal conjugation. If \(t=\tau_n\), every nonzero trace-free symmetric matrix attains equality. The same description covers the cases \(k=1,n-1\), which provide comparison with the classical spherical setting; the new phase transition is for the interior Grassmannian ranks \(2\le k\le n-2\).

In the dense-rank limit \(k/n\to\alpha\in(0,1)\) with even \(n\to\infty\), the transition occurs at \(\alpha=(1\pm1/\sqrt5)/2\): one-spike maximizers hold when \(\alpha(1-\alpha)<1/5\), and balanced maximizers when \(\alpha(1-\alpha)>1/5\). No assertion is made at a limiting critical ratio without the exact finite-dimensional comparison.

## Assumptions and scope

The Grassmannian is the set of real orthogonal rank-\(k\) projections in \(\mathbb R^n\) with its unique orthogonally invariant probability measure. Real symmetric \(A\), zero trace, and \(A\ne0\) are essential. The \(L^p\)-norms are computed with this probability measure. Even \(n\ge6\) is imposed for the complete balanced-spectrum equality class; odd dimensions and nonreal coefficient fields are outside the sharpness statement. The moment identities themselves also hold for integer \(n\ge4\).

## Proof

**1. Invariant reduction.** The laws of \(P\) and \(UPU^\mathsf T\) coincide. The trace-free degree-two and degree-four conjugation-invariant polynomials in a real symmetric matrix have respectively the bases \(\operatorname{tr}(A^2)\), and \((\operatorname{tr}(A^2))^2,\operatorname{tr}(A^4)\) for \(n\ge4\). Consequently \(\mathbb Ef_A^2=v\operatorname{tr}(A^2)\) and \(\mathbb Ef_A^4=a(\operatorname{tr}(A^2))^2+b\operatorname{tr}(A^4)\), with scalar coefficients to determine.

**2. Exact rank-one probe.** Put \(A_1=e_1e_1^\mathsf T-I/n\). Then \(Z=P_{11}\) has the beta law \(\operatorname{Beta}(k/2,(n-k)/2)\), and \(f_{A_1}=Z-k/n\). With rising factorial \((x)_r=x(x+1)\cdots(x+r-1)\),
\[
\mathbb EZ^r=\frac{(k/2)_r}{(n/2)_r}\quad(r=0,1,2,3,4).
\]
The variance of \(Z\) is \(2k(n-k)/[n^2(n+2)]\), whereas \(\operatorname{tr}(A_1^2)=(n-1)/n\); this gives \(v\). Moreover,
\[
\operatorname{tr}(A_1^4)=\frac{(n-1)(n^2-3n+3)}{n^3}.
\]
The fourth centered beta moment equals the explicit sum
\[
M_1=\sum_{j=0}^4\binom4j(-k/n)^{4-j}\frac{(k/2)_j}{(n/2)_j}.
\]

**3. Exact two-coordinate probe.** Put \(A_2=\operatorname{diag}(1,-1,0,\ldots,0)\), \(Z=P_{11}\), and \(W=P_{22}\). Conditional on the first Haar-orthogonal row \(u\), the second row is Haar-uniform on \(u^\perp\). The compression to \(u^\perp\) of the projector onto the first \(k\) coordinate directions has eigenvalues \(1\) (multiplicity \(k-1\)), \(1-Z\) (multiplicity one), and \(0\) (multiplicity \(n-k-1\)). The squares of components of a Haar-uniform unit vector have Dirichlet parameters one half each. Therefore, for every \(0\le r\le4\),
\[
\mathbb E(W^r\mid Z=z)=\frac1{((n-1)/2)_r}
\sum_{j=0}^r\binom rj ((k-1)/2)_{r-j}(1/2)_j(1-z)^j.
\]
Here \(\mathbb E[Z^p(1-Z)^q]=(k/2)_p((n-k)/2)_q/(n/2)_{p+q}\). Substitution into the binomial expansion of \((Z-W)^4\) gives
\[
M_2=\mathbb E(Z-W)^4
=\frac{48k(k+2)(n-k)(n-k+2)}{n(n-1)(n+1)(n+2)(n+4)(n+6)}.
\]
Since \(\operatorname{tr}(A_2^2)=\operatorname{tr}(A_2^4)=2\), the two independent probe identities are
\[
a\frac{(n-1)^2}{n^2}+b\frac{(n-1)(n^2-3n+3)}{n^3}=M_1,
\qquad 4a+2b=M_2.
\]
Solving this nonsingular linear system and simplifying yields exactly the displayed \(a,b\). Each step uses finite identities in beta and Dirichlet moments, not a numerical fitting argument.

**4. Sharp trace-free spectral interval.** Let \(\lambda_1,\ldots,\lambda_n\) be the real eigenvalues of \(A\), with \(\sum\lambda_i=0\) and \(\sum\lambda_i^2>0\). Define \(R(A)=\sum\lambda_i^4/(\sum\lambda_i^2)^2\). Cauchy--Schwarz gives \(R(A)\ge 1/n\), with equality exactly when all \(|\lambda_i|\) coincide. Since \(n\) is even and the trace is zero, these equality spectra are precisely the balanced ones.

To maximize, normalize \(\sum\lambda_i^2=1\). Lagrange multipliers imply every coordinate is a real root of \(4x^3-2\mu x-\nu=0\). If there are three distinct roots \(a_0<b_0<c_0\), the second variation of the constrained Lagrangian in the direction exchanging two copies of \(a_0\), or two copies of \(c_0\), is strictly positive (the derivative of this cubic is \(4(a_0-b_0)(a_0-c_0)>0\) and \(4(c_0-a_0)(c_0-b_0)>0\), respectively). Thus each extreme root occurs only once. Then \(a_0+c_0+(n-2)b_0=0\); the vanishing quadratic coefficient in the cubic also gives \(a_0+b_0+c_0=0\), so \((n-3)b_0=0\). Hence \(b_0=0\) and \(a_0=-c_0\), giving \(R=1/2\). This is smaller than the one-spike value below for \(n\ge4\). Therefore a maximizer has just two eigenvalues with multiplicities \(p\) and \(n-p\). The trace constraint gives
\[
R=\frac{n}{p(n-p)}-\frac3n,
\]
which is maximized precisely for \(p=1\) or \(n-1\), yielding
\[
\frac1n\le R(A)\le\frac{n^2-3n+3}{n(n-1)}.
\]
The equality classifications are exactly those in the Finding.

**5. Phase transition.** Dividing the fourth-moment identity by \(v^2(\operatorname{tr}A^2)^2\) reduces sharpness to maximizing \(a+bR\). All factors of \(b\) outside \(n(n^2+n+2)-(5n+6)k(n-k)\) are strictly positive, so its sign is exactly the stated threshold comparison. At \(b=0\), the normalized fourth moment is independent of the spectrum. Finally \(\tau_n/n^2\to1/5\); substituting \(k/n\to\alpha\) yields the limiting phase boundaries and the optimizer regimes away from criticality.

## Verification

The standalone file `CHECK.py` constructs the two probe moments *independently* from exact rational beta--Dirichlet conditional moments, then verifies the derived polynomial identities for 120 pairs \((n,k)\) with even \(4\le n\le22\). It also independently checks the displayed spectral interval on rational sample eigenvalue vectors. Its final output is `ALL_GRASSMANN_FIRST_HARMONIC_CHECKS_PASSED`. These finite tests do not replace the all-dimensional symbolic proof above, and they do not constitute independent audit.

## Relationship to prior work

Matsumoto's 2013 full treatment of class BD I, especially Theorem 4.2, provides Weingarten formulas for all polynomial moments of orthogonal Grassmannian matrix ensembles; such general integration formulas are **prior**, not part of the new assertion. Bodmann--Ehler--Gräf's 2017 full-text Theorem 2.4 gives explicit trace moments through order three and discusses general zonal-polynomial moment recovery. They do not provide the sharp \(L^2\)-to-\(L^4\) operator norm with the one-spike-to-balanced transition and complete equality classes stated here. The rank-one case reduces to familiar sphere quadratic-harmonic moments, and the isolated \(\operatorname{Gr}(2,4)\) special case is already known; neither is claimed as a standalone discovery. The claimed contribution is the complete rank-dependent transition for even \(n\ge6\), including the interior ranks and exact coefficient formulas.

## Limitations

No claim is made for odd-dimensional optimal spectra, complex/quaternionic Grassmannians, higher moments, or equality behavior exactly at a limiting critical proportion without the finite comparison. The moment coefficients are reducible to established Weingarten and zonal integration machinery; originality refers to the optimized fourth-moment theorem and its spectral transition, subject to unindexed equivalent results in the broader literature. Bibliographic priority is not independently certified.

## References

1. S. Matsumoto, *Weingarten calculus for matrix ensembles associated with compact symmetric spaces*, arXiv:1301.5401v1 (public 23 January 2013), especially Section 4.2/Theorem 4.2. https://arxiv.org/abs/1301.5401
2. B. G. Bodmann, M. Ehler and M. Gräf, *From Low- to High-Dimensional Moments Without Magic*, Journal of Theoretical Probability 31 (2018), first online 14 September 2017, especially Theorem 2.4 and Section 3. https://doi.org/10.1007/s10959-017-0785-x
