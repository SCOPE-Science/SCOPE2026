# Exact first partial-section norm of homogeneous bidisk quadratics, with universal Banach-valued sharpness

## Finding

Let \(E\) be any nonzero complex Banach space. On the space \(\mathcal P_2(E)\) of \(E\)-valued homogeneous quadratic polynomials on the closed bidisk, equipped with the supremum norm, consider the monomial initial-section projection
\[
\Pi\bigl(Aw^2+Bzw+Cz^2\bigr)=Aw^2+Bzw,
\qquad A,B,C\in E.
\]
Its **exact operator norm, uniformly for every such target space**, is
\[
\boxed{\|\Pi:\mathcal P_2(E)\longrightarrow\mathcal P_2(E)\|=\frac2{\sqrt3}.}
\]
For \(E=\mathbb C\), the nonzero polynomials attaining equality are exactly the scalar multiples and coordinate phase rotations of
\[
\boxed{Q_*(z,w)=\tfrac12w^2+zw-\tfrac14z^2.}
\]
Precisely, every scalar extremizer is \(\lambda Q_*(e^{i\vartheta}z,w)\) with \(\lambda\in\mathbb C\setminus\{0\}\) and \(\vartheta\in\mathbb R\). A two-atom, norm-attaining interpolation formula proves the universal upper bound. It also shows that the first nontrivial two-variable quadratic monomial partial sum is noncontractive, with an exact amplification factor independent of the coefficient Banach space.

## Assumptions and scope

The bidisk is \(\overline{\mathbb D}^{\,2}=\{(z,w)\in\mathbb C^2:|z|,|w|\le1\}\). The norm is \(\|Q\|_\infty=\sup_{|z|,|w|\le1}\|Q(z,w)\|_E\). The monomial order is \(w^2,zw,z^2\); the projection retains the first two terms. This is an operator on the **three-monomial homogeneous quadratic block**, not the full analytic function algebra. The same norm holds under reversed monomial order by coordinate interchange. For \(E\ne\{0\}\), an arbitrary unit vector supplies the scalar sharpness example. The scalar equality classification does not assert uniqueness of vector-valued equality cases for arbitrary Banach targets.

## Proof

**1. Reduction to a disk polynomial.** Put \(P(\zeta)=A+B\zeta+C\zeta^2\). On the distinguished boundary \(|z|=|w|=1\), letting \(\zeta=z/w\) gives \(Q(z,w)=w^2P(\zeta)\). The maximum-modulus principle for Banach-valued holomorphic polynomials (or Hahn–Banach followed by the scalar maximum-modulus principle) therefore gives
\[
\|Q\|_\infty=\max_{|\zeta|=1}\|P(\zeta)\|_E,
\qquad
\|\Pi Q\|_\infty=\max_{|\zeta|=1}\|A+B\zeta\|_E.
\tag{1}
\]

**2. Exact two-atom coefficient annihilation.** Set
\[
\xi_\pm=e^{\pm i\pi/3},\qquad
\lambda_\pm=\tfrac12\mp\frac{i}{2\sqrt3}.
\]
Direct multiplication gives three exact moments
\[
\lambda_++\lambda_-=1,\quad
\lambda_+\xi_++\lambda_-\xi_-=1,\quad
\lambda_+\xi_+^2+\lambda_-\xi_-^2=0,
\quad |\lambda_+|+|\lambda_-|=\frac2{\sqrt3}.
\tag{2}
\]
For every \(|\zeta|=1\), (2) gives the **vector-valued identity**
\[
A+B\zeta=\lambda_+P(\zeta\xi_+)+\lambda_-P(\zeta\xi_-).
\tag{3}
\]
The triangle inequality applied in \(E\) gives \(\|A+B\zeta\|_E\le(2/\sqrt3)\|Q\|_\infty\). Maximizing and using (1) proves the upper bound for every complex Banach target without any structural assumption on its norm.

**3. An extremizer and exact norm.** In the scalar case, take \(P_*(\zeta)=\tfrac12+\zeta-\tfrac14\zeta^2\). For \(s=\cos t\) one checks the identity
\[
|P_*(e^{it})|^2=\frac{27}{16}-\frac12\left(s-\frac12\right)^2.
\tag{4}
\]
Because \(s\in[-1,1]\), the exact supremum is \(3\sqrt3/4\), attained at \(t=\pm\pi/3\). On the other hand \(\|\tfrac12+\zeta\|_\infty=3/2\). Their ratio is \(2/\sqrt3\), so the bound from Step 2 is sharp. For a nonzero Banach target \(E\), multiply \(Q_*\) by an arbitrary unit vector of \(E\).

**4. Exhaustive classification of scalar equality.** Let \(P(\zeta)=a+b\zeta+c\zeta^2\) be any nonzero scalar equality case. Multiplication by a scalar and rotation of \(\zeta\) allow \(a,b\ge0\). If either is zero, the ratio is at most \(1\), strictly less than \(2/\sqrt3\); hence \(a,b>0\). Let \(M=\|P\|_\infty\). Equality in the two-atom triangle inequality at \(\zeta=1\), together with \(|\lambda_\pm|=1/\sqrt3\), forces
\[
P(\xi_+)=M e^{i\pi/6},\qquad P(\xi_-)=M e^{-i\pi/6}.
\tag{5}
\]
Subtracting and adding these two equations yields, respectively,
\[
\sqrt3(b+c)=M,\qquad 2a+b-c=\sqrt3M.
\]
In particular \(c\) is real, and solving gives \(c=(a-b)/2\). Since \(|P(e^{it})|\) is maximal at the interior angle \(t=\pi/3\), its derivative there vanishes. For real \(a,b,c\), writing \(s=\cos t\) gives
\[
|P(e^{it})|^2=a^2+b^2+c^2-2ac+2b(a+c)s+4ac s^2.
\]
The derivative at \(s=1/2\) yields \(b(a+c)+2ac=0\). Substitution of \(c=(a-b)/2\) gives \((a+b)(2a-b)=0\), hence \(b=2a\) and \(c=-a/2\). This is exactly the claimed scalar orbit. Conversely, every such phase rotation and scalar multiple attains the bound by Step 3.

## Verification

The universal proof depends only on the exact three-moment identity (2), the boundary reduction (1), and the explicit scalar maximizer (4). A standalone standard-library program `check_quadratic_section.py` verifies the interpolation moments over the rational quadratic field \(\mathbb Q(i\sqrt3)\), the rational squared-norm profile and ratio, the equality-stationarity identity, and 384 supplementary finite numerical trials. It prints `QUADRATIC_BIDISK_SECTION_EXACT_CERTIFICATE_OK 384`. The finite trials are supplementary; the identity proves the inequality for all Banach spaces, not merely sampled polynomials.

## Relationship to prior work

Grando's 2026 study of monomial Schauder bases in spaces of holomorphic functions on Banach spaces develops degree-dependent monomial initial-section bounds, including a general \(n+1\) bound for degree \(n\); the three-term block studied here is the first nontrivial finite two-coordinate test of that framework. The exact \(2/\sqrt3\) norm and its scalar rigidity are narrower and sharper than the published general upper estimate. Geddes and Mason's 1975 work concerns Taylor truncation on the **full disk algebra** and its asymptotic norm growth; a full-algebra projection norm does not determine the norm of a restriction to quadratic inputs. Related exact published-finding corpus results on diagonal Hardy-to-Bergman restriction of quadratics, Euclidean-ball coefficient norms, and low-exponent Hardy Taylor evaluations use different source/target norms and different operators. None of the inspected statements implies the present bidisk supremum-norm projection identity. The full Grando manuscript and the full 1975 paper were not available for line-by-line comparison; they remain bibliographic risks rather than being declared non-covering in their entirety.

## Limitations

The result concerns only the first nontrivial homogeneous quadratic block on the **complex bidisk**, with the specified two-term coordinate cutoff. It does not give sharp projection bounds for higher degrees, arbitrary compact solid sets, real coefficient spaces, other monomial orders, or complete equality classifications in non-strictly-convex Banach targets. The sharp constant may be known implicitly in older approximation-theory sources under another name; an indexed search and the inspected material cannot prove publication priority. There has been no independent mathematical audit.

## References

1. T. Grando, *Monomial bases for holomorphic functions on Banach spaces with an unconditional basis*, arXiv:2608.14926v1, first public arXiv submission 14 August 2026, https://arxiv.org/abs/2608.14926.
2. S. Dineen and J. Mujica, *A monomial basis for the holomorphic functions on \(c_0\)*, Proc. Amer. Math. Soc. 141 (2013), 1663–1672, https://doi.org/10.1090/S0002-9939-2012-11436-4.
3. K. O. Geddes and J. C. Mason, *Polynomial approximation by projections on the unit circle*, SIAM J. Numer. Anal. 12 (1975), 111–120, https://doi.org/10.1137/0712011.
4. *The exact quadratic norm of diagonal Hardy-to-Bergman restriction*, published research record, 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-exact-quadratic-norm-of-diagonal-hardy-to-bergman-restrictio--e1e60f29d3de.
5. *Exact real and complex quadratic Hilbert coefficient constants, with an odd-dimensional gap*, published research record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-and-complex-quadratic-hilbert-coefficient-constants-w--c36cc14a214a.
6. *Sharp second Taylor-section evaluation on sublinear Hardy spaces*, published research record, 16 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-second-taylor-section-evaluation-on-sublinear-hardy-spaces--56944f6874fb.
