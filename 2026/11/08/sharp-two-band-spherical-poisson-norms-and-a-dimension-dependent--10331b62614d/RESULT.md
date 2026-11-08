# Sharp two-band spherical Poisson norms and a dimension-dependent contraction threshold

## Finding

For every integer \(d\ge2\), equip \(\mathbb S^{d-1}\subset\mathbb R^d\) with normalized rotation-invariant probability \(\sigma_d\). On the real centered degree-one-plus-degree-two spherical harmonic space
\[
\mathcal V_d=\{f(\omega)=v\cdot\omega+\omega^{\mathsf T}H\omega:\ v\in\mathbb R^d,\ H=H^{\mathsf T},\ \operatorname{tr}H=0\},
\]
let the harmonic Poisson operator act by
\[
\mathcal P_\rho f=\rho\,v\cdot\omega+\rho^2\omega^{\mathsf T}H\omega,
\qquad 0\le\rho\le1.
\]
Here \(\rho^k\) is the multiplier on degree-\(k\) harmonics; this is the classical ball-Poisson operator, not the different fractional-Laplace semigroup with multipliers \(e^{-t\sqrt{k(k+d-2)}}\).

Put \(r=\rho^2\) and set
\[
A_d=\frac{3d}{d+2},\qquad
B_d=\frac{3(10d-8)}{d+4},\qquad
C_d=\frac{3(d+2)(5d^2-13d+12)}{(d-1)(d+4)(d+6)},\qquad
r_{0,d}=\frac{2A_d}{B_d}=\frac{d(d+4)}{(d+2)(5d-4)}.
\]
The exact fourth power of the restricted operator norm is
\[
\boxed{\|\mathcal P_\rho:\mathcal V_d(L^2)\longrightarrow L^4(\sigma_d)\|^4=
\begin{cases}
A_dr^2,&0\le r\le r_{0,d},\\[2mm]
\dfrac{(B_d^2-4A_dC_d)r^4}{4(B_dr-A_d-C_dr^2)},&r_{0,d}<r\le1.
\end{cases}}
\]
For \(0<r\le r_{0,d}\), the nonzero extremizers are precisely the degree-one harmonics. For \(r>r_{0,d}\), define the first-harmonic energy share
\[
s_{d,r}=\frac{B_dr-2C_dr^2}{2(B_dr-A_d-C_dr^2)}\in(0,1).
\]
Every extremizer has precisely this share. When \(d\ge3\), the extremizers are exactly the nonzero aligned zonal mixtures
\[
f(\omega)=a(u\cdot\omega)+b\big((u\cdot\omega)^2-1/d\big),\quad u\in\mathbb S^{d-1},\quad ab\ne0,\quad
\frac{a^2/d}{a^2/d+2b^2(d-1)/(d^2(d+2))}=s_{d,r}.
\]
For \(d=2\), all nonzero pairs \((v,H)\) with both terms present and the stated energy share are extremal, without an alignment restriction. At \(\rho=0\), the operator is zero and all nonzero inputs give ratio zero.

There is a unique contraction threshold \(r_{*,d}\in(r_{0,d},1)\), equivalently \(\rho_{*,d}=\sqrt{r_{*,d}}\), characterized by
\[
(B_d^2-4A_dC_d)r_{*,d}^4=4(B_dr_{*,d}-A_d-C_dr_{*,d}^2).
\]
The restricted operator is an \(L^2\)-to-\(L^4\) contraction exactly for \(0\le\rho\le\rho_{*,d}\). The thresholds \(\rho_{*,d}\) decrease strictly as \(d\) increases. In particular,
\[
\rho_{*,2}=0.867560653933\ldots,\qquad
\rho_{*,3}=0.812584728029\ldots,\qquad
\lim_{d\to\infty}\rho_{*,d}=0.672044717288805\ldots.
\]
The limit is the unique positive \(\sqrt r\), with \(r\in(1/5,1)\), for which
\[
60r^4+5r^2-10r+1=0.
\]
For fixed \(r>0\), the fourth-power norms increase strictly in dimension, and converge to the Gaussian first-two-chaos norm
\[
\begin{cases}
3r^2,&0\le r\le1/5,\\[1mm]
60r^4/(10r-1-5r^2),&1/5<r\le1.
\end{cases}
\]

## Assumptions and scope

All functions, coefficients, norms and extremizers are real; the measure is normalized to mass one; \(d\) is an integer at least two; \(0\le\rho\le1\); the input subspace excludes constants and all harmonics of degree at least three. The operator acts through the ordinary Poisson multipliers \(\rho^k\). A norm-zero operator at \(\rho=0\) is included in the formula. Sharp means attained by a nonzero input in the stated finite-dimensional space.

## Proof

**1. Exact spherical moments.** Let \(G\sim N(0,I_d)\), write \(G=R\omega\) with \(R\) independent of uniform \(\omega\), and put \(T=\operatorname{tr}H^2\), \(U=\operatorname{tr}H^4\). The Gaussian Wick identities, divided by radial moments, give
\[
\begin{aligned}
\mathbb E(v\cdot\omega)^2&=\frac{|v|^2}{d},&
\mathbb E(\omega^{\mathsf T}H\omega)^2&=\frac{2T}{d(d+2)},\\
\mathbb E(v\cdot\omega)^4&=\frac{3|v|^4}{d(d+2)},&
\mathbb E(v\cdot\omega)^2(\omega^{\mathsf T}H\omega)^2&=\frac{2|v|^2T+8v^{\mathsf T}H^2v}{d(d+2)(d+4)},\\
\mathbb E(\omega^{\mathsf T}H\omega)^4&=\frac{12T^2+48U}{d(d+2)(d+4)(d+6)}.
\end{aligned}
\]
The odd cross terms in the fourth power vanish under \(\omega\mapsto-\omega\).

**2. Simultaneously sharp matrix inequalities.** Since the eigenvalues of \(H\) sum to zero, Cauchy--Schwarz applied to the other \(d-1\) eigenvalues yields
\[
v^{\mathsf T}H^2v\le\frac{d-1}{d}|v|^2T.
\]
The sharp traceless fourth-power inequality is
\[
U\le\frac{d^2-3d+3}{d(d-1)}T^2.
\]
For completeness, in dimensions two and three the ratio \(U/T^2\) is identically \(1/2\). In higher dimensions, a maximum on the compact zero-sum, unit-quadratic-mass eigenvalue sphere has at most three distinct coordinates by the Lagrange equation \(4x^3=\alpha+2\beta x\). At a three-root local maximum, an extreme root cannot have multiplicity at least two: opposite perturbations of equal coordinates violate the second-variation condition \(12x^2-2\beta\le0\). Thus both extreme roots have multiplicity one and, by the missing quadratic coefficient and the zero-sum constraint, the middle root is zero, leaving fourth-power ratio \(1/2\). At two-root stationary configurations with multiplicities \(k,d-k\), the ratio is \(d/[k(d-k)]-3/d\), largest for \(k=1\) or \(d-1\). This proves the displayed bound. This known pure-quadratic lemma is also documented in the cited sharp degree-two spherical-harmonic result.

For \(d\ge3\), simultaneous equality with nonzero linear and quadratic energies occurs precisely for \(H=b(uu^{\mathsf T}-I/d)\) and \(v=au\) with \(a,b\ne0\); in dimension two, every traceless symmetric \(H\) satisfies \(H^2=(T/2)I\), so the direction of \(v\) is unrestricted.

**3. Energy reduction.** For any nonzero \(f\), let
\[
s=\frac{|v|^2/d}{|v|^2/d+2T/[d(d+2)]}\in[0,1].
\]
Using the moment identities and both sharp inequalities,
\[
\frac{\|\mathcal P_\rho f\|_4^4}{\|f\|_2^4}
\le r^2\big[A_ds^2+B_dr\,s(1-s)+C_dr^2(1-s)^2\big].
\]
Every value of \(s\) attains equality by a suitable aligned zonal pair, so this scalar maximization is exact. The identities
\[
C_d-A_d=\frac{6(d-2)(d+1)(2d^2+d-12)}{(d-1)(d+2)(d+4)(d+6)}\ge0,
\quad
B_d-2C_d=\frac{72d(2d-3)}{(d-1)(d+4)(d+6)}>0
\]
ensure that the derivative at \(s=0\) is positive for all \(0<r\le1\). At \(s=1\), the derivative has the sign of \(2A_d-B_dr\), changing once at \(r_{0,d}\). The quadratic is therefore maximized at \(s=1\) up to this threshold, and at the unique interior \(s=s_{d,r}\) afterward. Substitution gives exactly the stated piecewise norm and equality classification.

**4. Contractivity and dimension.** All nonzero fixed-input fourth moments strictly increase with \(r>0\), as seen in the nonnegative coefficients of the exact moments; hence the maximum increases continuously from zero to a value exceeding one (already pure degree-one at \(r=1\)). As \(A_dr_{0,d}^2<3/4<1\), the unique unit-norm crossing lies strictly beyond \(r_{0,d}\), and satisfies the stated quartic.

The coefficient sequences are strictly increasing with \(d\). Indeed,
\[
A_{d+1}-A_d=\frac6{(d+2)(d+3)},\qquad
B_{d+1}-B_d=\frac{144}{(d+4)(d+5)},
\]
\[
C_{d+1}-C_d=\frac{72(d+1)(2d^3+9d^2-11d-12)}{d(d-1)(d+4)(d+5)(d+6)(d+7)}>0\quad(d\ge2).
\]
Thus the maximized fourth-power norm grows strictly with dimension at every fixed \(r>0\); the unique contractivity thresholds strictly decrease. Taking \(d\to\infty\) in the explicit coefficients yields \((A_d,B_d,C_d)\to(3,30,15)\), giving the asserted Gaussian limit and its unique threshold. The strict monotonicity and limiting values follow directly.

## Verification

The accompanying standalone script `scripts/check_spherical_two_band.py` uses exact rational spherical-coordinate moments through degree eight. It checks the three coefficients against independent zonal moment expansions in 138 rational dimension/radius pairs, the two branches, rational threshold brackets, and strict finite-range dimension comparisons. It prints `ALL_TWO_BAND_SPHERICAL_POISSON_CHECKS_PASSED`. These finite tests do not replace the preceding all-dimensional proof. All numerical thresholds in this note are approximations to uniquely characterized real roots, not independent axioms.

## Relationship to prior work

Beckner's 1992 sphere-Poisson hypercontractivity theorem gives the unrestricted sufficient contraction region \(\rho\le1/\sqrt3\) for \(L^2\to L^4\). That bound, which allows constants and every harmonic degree, neither gives the restricted sharp norm above that radius nor identifies its dimension dependence and extremizers. Montanaro's 2012 exposition explicitly records the spherical multipliers \(\rho^k\) and reproduces Beckner's bound. A published exact fourth-moment result for the *pure* degree-two spherical harmonics provides the coefficient \(C_d\) and its sharp matrix inequality, but does not handle mixed degrees. Previously established mixed-degree sharpness on \(\mathbb S^2\) at \(\rho=1\) is recovered when \(d=3,r=1\); the Gaussian first-two-chaos operator formula is recovered only in the large-dimension limit. Neither specialization determines the present all-dimensional finite-radius norms or strict dimension-dependent contraction thresholds.

## Limitations

Only mean-zero **real** combinations of degrees one and two, normalized surface measure, the classical ball-Poisson multiplier \(\rho^k\), and the \(L^2\)-to-\(L^4\) norm are treated. The unrestricted spherical Poisson operator has constants and higher degrees, so its full norm and its optimal full-space threshold are not computed here. The fractional-Laplace semigroup on the sphere is a different operator; no claim is made about it. Some older unindexed norm-inequality literature could contain a restatement of the mixed-degree formula; the available comparisons support, but cannot prove, novelty. The proof and verification are not an independent audit.

## References

1. W. Beckner, “Sobolev inequalities, the Poisson semigroup, and analysis on the sphere \(S^n\),” *Proc. Natl. Acad. Sci. USA* **89** (1992), 4816–4819. DOI: https://doi.org/10.1073/pnas.89.11.4816 .
2. A. Montanaro, “Some applications of hypercontractive inequalities in quantum information theory,” preprint, November 9, 2012, §2.1. https://people.maths.bris.ac.uk/~csxam/papers/hyper.pdf .
3. “Sharp \(L^4/L^2\) norm and extremizers for degree-two spherical harmonics,” publicly available mathematical research record, September 20, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f .
