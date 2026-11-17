# Three critical extinction phases and a variance-driven logarithmic clock in mixed Beverton–Holt competition

## Finding
Let \(0<\eta<1\), \(a,b>0\), and \(\tau>0\), and define
\[
 f(u)=\frac{\eta}{1+au}+\frac{1-\eta}{1+bu},\quad
 c=\eta a+(1-\eta)b,\quad v=\eta(1-\eta)(a-b)^2.
\]
For every initial point \((x_0,y_0)\in(0,\infty)^2\), consider the symmetric, double-critical, two-species competition system
\[
 x_{n+1}=x_n f(x_n+\tau y_n),\qquad
 y_{n+1}=y_n f(\tau x_n+y_n).
\tag{1}
\]
Every trajectory remains positive and tends to the origin. Its **sharp extinction laws**, including arbitrary unequal positive initial conditions, form the following three phases.

**Cross-competition weaker than self-competition, \(0<\tau<1\).** The two populations synchronize at the sharp algebraic leading scale
\[
 \lim_{n\to\infty}n x_n=\lim_{n\to\infty}n y_n=\frac1{c(1+\tau)}.
\]
For unequal initial populations there is a finite nonzero real \(D\), with the sign of \(x_0-y_0\), such that
\[
 \boxed{\lim_{n\to\infty} n^{2/(1+\tau)}(x_n-y_n)=D.}
\tag{2}
\]
For equal initial populations the difference is identically zero.

**Exactly matched self- and cross-competition, \(\tau=1\).** The composition \(q=x_0/(x_0+y_0)\) is conserved: \((x_n,y_n)=(q z_n,(1-q)z_n)\), with \(z_n=x_n+y_n\). There is a finite real orbit-dependent constant \(H\) such that
\[
 \boxed{\frac1{z_n}=c n-\frac{v}{c}\log n+H+o(1).}
\tag{3}
\]
In particular \(n z_n\to1/c\), and the logarithmic coefficient vanishes precisely when the two channel-specific crowding coefficients coincide, \(a=b\). For genuine heterogeneity \(a\ne b\), the logarithmic delay coefficient is strictly negative and exactly proportional to the variance \(v\).

**Cross-competition stronger than self-competition, \(\tau>1\).** If \(x_0>y_0\), the initially larger species is the asymptotic majority, and for some finite \(L>0\),
\[
 \boxed{\lim_{n\to\infty}n x_n=\frac1c,\qquad
 \lim_{n\to\infty}n^\tau y_n=L.}
\tag{4}
\]
For \(y_0>x_0\), exchange the coordinates. On the exceptional invariant diagonal \(x_0=y_0\), both instead obey \(n x_n=n y_n\to1/[c(1+\tau)]\).

The exponents \(2/(1+\tau)\) and \(\tau\) need not be integers. All limits concern the original discrete generation index \(n\).

## Assumptions and scope
The parameters are fixed, independent of \(n\). Both populations start strictly positive; no upper population bound is required. The response \(f\) is the convex mixture of two Beverton–Holt saturating factors with unit total low-density reproductive multiplier. It arises as an exchange-symmetric double-critical parameter subfamily of the reduced two-host, two-infection-status competition model of Bravo de la Parra and Sanz: choose equal unit reproduction coefficients for susceptible and infected hosts, respective mixture fractions \(\eta\) and \(1-\eta\), and the two reciprocal denominator channels to have own/cross crowding ratios \(1:\tau\). The claim concerns this **two-dimensional reduced** map, not the unreduced four-compartment model at a finite fast-process count. The origin has both linearized multipliers equal to one and is nonhyperbolic. Both parameters \(a,b\) are positive even when equal, and \(\tau\) may be arbitrarily close to its transition value one.

## Proof
**Step 1: exact order retention, extinction and the \(1/n\) envelope.** Each term in \(f(u)\) lies strictly between zero and one for \(u>0\). Thus positive iterates strictly decrease in both coordinates, remain positive, and converge to nonnegative limits. Neither limit can be positive, because then the corresponding coordinate would be multiplied indefinitely by a number uniformly below one. Hence both tend to zero.

The following *exact factorization* is useful. For either channel parameter \(s>0\),
\[
 \frac{x}{1+s(x+\tau y)}-\frac{y}{1+s(\tau x+y)}
 =(x-y)\frac{1+s\tau(x+y)}{[1+s(x+\tau y)][1+s(\tau x+y)]}.
\tag{5}
\]
Taking its positive weighted mixture shows that \(x_n-y_n\) never changes sign and is zero at one time if and only if it was zero initially. Put \(z_n=x_n+y_n\), \(d_n=x_n-y_n\), and \(c=\eta a+(1-\eta)b>0\). Uniform Taylor expansion on the positive cone gives
\[
 z_{n+1}=z_n-c\{x_n^2+y_n^2+2\tau x_n y_n\}+O(z_n^3).
\tag{6}
\]
Since \((x^2+y^2+2\tau xy)/(x+y)^2\) lies between \(\min(1,(1+\tau)/2)\) and \(\max(1,(1+\tau)/2)\), the reciprocal increments \(1/z_{n+1}-1/z_n\) are eventually bounded between two positive constants. Consequently \(z_n=\Theta(1/n)\), \(\sum_n z_n=\infty\), and \(\sum_n z_n^2<\infty\).

**Step 2: exact ratio selection.** For positive coordinates write \(R_n=x_n/y_n\). Then
\[
 \log\frac{R_{n+1}}{R_n}
 =\log f(x_n+\tau y_n)-\log f(\tau x_n+y_n)
 =c(\tau-1)d_n+O(z_n^2).
\tag{7}
\]
When \(x_n>y_n\), strict decrease of \(f\) means that \(R_n\) decreases if \(\tau<1\) and increases if \(\tau>1\). It remains greater than one by (5). For \(\tau<1\), were \(R_n\) to approach a limit larger than one, then \(d_n\ge\delta z_n\) eventually; (7) together with \(\sum_nz_n=\infty\) would force \(\log R_n\to-\infty\), a contradiction. Thus \(R_n\to1\). For \(\tau>1\), a finite limit larger than one similarly contradicts (7), now with positive divergence, so \(R_n\to\infty\). The complementary initial ordering is symmetric. At \(\tau=1\), the two denominators are identical and \(R_n\) is exactly constant.

**Step 3: synchronizing phase and its noninteger exponent.** Suppose \(0<\tau<1\). Since \(d_n/z_n\to0\), (6) becomes \(z_{n+1}=z_n-Az_n^2+o(z_n^2)\) with \(A=c(1+\tau)/2\). Therefore \(n z_n\to1/A\). The exact factorization (5) also implies, uniformly as \(z_n\to0\),
\[
 \log\frac{|d_{n+1}|}{|d_n|}=-c z_n+O(z_n^2).
\tag{8}
\]
For \(d_0\ne0\), this initially yields \(|d_n|=n^{-c/A+o(1)}\), and hence \(|d_n|/z_n=n^{-\alpha+o(1)}\), with \(\alpha=c/A-1=(1-\tau)/(1+\tau)>0\). Choose a fixed \(0<\delta<\min(\alpha,1/2)\); then \((d_n/z_n)^2=O(n^{-2\delta})\). Rewriting (6) via \(x^2+y^2+2\tau xy=(1+\tau)z^2/2+(1-\tau)d^2/2\), one gets
\[
 \frac1{z_{n+1}}-\frac1{z_n}
 =A+\frac{c(1-\tau)}2\left(\frac{d_n}{z_n}\right)^2+O(z_n).
\tag{9}
\]
Since \(z_n=O(1/n)\), summation gives \(1/z_n=A n+O(n^{1-2\delta}+\log n)\), where a bound of \(O(\log n)\) replaces the first remainder if \(2\delta=1\). Thus
\[
 z_n=\frac1{A n}+O(n^{-1-2\delta}+\log n/n^2),
\tag{10}
\]
and the series \(\sum_{n\ge1}(z_n-1/(An))\) converges absolutely. Equation (8) now has summable error in the compensated logarithmic product
\[
 \log|d_n|+\frac cA\log n.
\]
Its limit is finite, so \(n^{c/A}d_n\) tends to a finite *nonzero* signed limit because no factor in (5) is zero. As \(c/A=2/(1+\tau)\), (2) follows; dividing \(z_n\) equally gives the two leading population limits.

**Step 4: selecting phase.** Suppose \(\tau>1\) and \(x_0>y_0\). Step 2 gives \(y_n/x_n\to0\). Equation (6) then shows \(n z_n\to1/c\), hence \(n x_n\to1/c\). Equation (7) and \(\sum_{j<n}x_j\sim (1/c)\log n\) give
\[
 \log R_n=(\tau-1)\log n+o(\log n).
\tag{11}
\]
Therefore \(y_n/x_n=O(n^{-\delta})\) for some \(0<\delta<\min(\tau-1,1)\). Expanding the reciprocal of the first equation in (1) gives
\[
 \frac1{x_{n+1}}-\frac1{x_n}
 =c\left(1+\tau\frac{y_n}{x_n}\right)+O(z_n).
\tag{12}
\]
Summation shows \(1/x_n=cn+O(n^{1-\delta}+\log n)\), hence \(x_n=1/(cn)+O(n^{-1-\delta}+\log n/n^2)\) and \(\sum_{n\ge1}(x_n-1/(cn))\) converges. Meanwhile \(y_n=O(n^{-1-\delta})\) and
\[
 \log\frac{y_{n+1}}{y_n}=-c(\tau x_n+y_n)+O(z_n^2).
\tag{13}
\]
The summable errors in (13) show that \(\log(y_n n^\tau)\) converges to a finite real number; exponentiation yields the strictly positive limit \(L\). The other ordering follows by symmetry. If \(x_0=y_0\), both coordinates remain equal by (5), and (6) with \(x_n=y_n\) gives their stated common leading law.

**Step 5: the heterogeneity logarithm at exact equality.** With \(\tau=1\), put \(z=x+y\). Then \(z_{n+1}=z_n f(z_n)\) and both coordinate shares are constant. Write \(d_2=\eta a^2+(1-\eta)b^2\). Since \(f(z)=1-cz+d_2z^2+O(z^3)\) and \(d_2-c^2=v\), one obtains
\[
 \frac1{z_{n+1}}-\frac1{z_n}=c-v z_n+O(z_n^2).
\tag{14}
\]
The reciprocal first satisfies \(1/z_n=cn+O(\log n)\), whence \(z_n=1/(cn)+O(\log n/n^2)\). Subtracting \(c-v/(cn)\) from (14) leaves an absolutely summable sequence (because \(\sum_n|z_n-1/(cn)|<\infty\) and \(\sum_nz_n^2<\infty\)). The standard difference between harmonic numbers and \(\log n\) converges. Thus \(1/z_n-cn+(v/c)\log n\to H\in\mathbb R\), proving (3) with a genuine finite limit, not just an \(O(1)\) remainder.

## Verification
The accompanying standalone `verify.py` independently checks the exact algebraic difference factorization and the variance identity for symbolic parameters; it also iterates the rational map at positive examples in all three phases and compares normalized observables at increasing finite horizons. For an unequal-channel example \(\eta=2/5\), \(a=2\), \(b=1/2\), the analytic constants are \(c=11/10\) and \(v=27/50\). In the balanced critical phase it verifies the stabilizing quantity \(1/z_n-cn+(v/c)\log n\), not only the leading \(n z_n\). The code can be run with `python3 verify.py` using Python 3 and SymPy. These finite diagnostics do not prove asymptotic statements; Steps 1–5 provide the unrestricted analytical proofs.

## Relationship to prior work
Bravo de la Parra and Sanz, *A discrete model of competing species sharing a parasite* (first verified public version: September 17, 2019, DOI 10.3934/dcdsb.2019204), establish the four-compartment construction, its two-dimensional rational mixture reduction and convergence to equilibria. Their Theorem 3.2 covers the **qualitative extinction conclusion** when both low-density reproductive multipliers are at most one, including equality. No new qualitative extinction claim is made here. Their accessible full text, including Theorem 3.2, the model definition, the reduction and appendices, does not report the simultaneously critical three-phase population profiles, the exact noninteger synchronization/minority exponents or the channel-variance logarithmic correction.

Sacker (2011), *Global stability in a multi-species periodic Leslie–Gower model*, proves global positive periodic attractors under supercritical growth and weak competition and discusses numerical exclusion under high competition; it does not supply the stated two-neutral-multiplier critical rates. A previously published critical trichotomy for a **species-swapping Ricker–Beverton–Holt map** has a two-step return, alternating dominance and a different saturation mechanism; its formula does not imply this strictly order-preserving mixture map. A published rank-one periodically harvested Lotka–Volterra critical trichotomy assumes proportional interaction rows and has a conserved power relation; it does not imply (1) or its heterogeneity-variance logarithm. These are substantive differences in objects and implications, not an assertion that matching terminology alone proves novelty.

## Limitations
The result concerns an exchange-symmetric, simultaneously critical subfamily, not all parameter choices of the source model. It does not establish convergence rates for the unreduced four-compartment system when the disease dynamics runs for only finitely many fast steps per demographic step, nor does it cover stochastic infection, nonsymmetric mixtures or coefficients varying with time. The limits depend on fixed positive initial states; convergence is not claimed uniform as \(\tau\to1\), and the nonzero asymptotic amplitude \(D\) or \(L\) generally depends on the initial point. The zero-initial-coordinate boundary is excluded. Equivalent statements may exist in unindexed nonlinear difference-equation literature; bibliographic coverage is not a proof of priority. Independent audit has not been performed.

## References
1. R. Bravo de la Parra and L. Sanz, *A discrete model of competing species sharing a parasite*, *Discrete and Continuous Dynamical Systems B* **25** (2020), 2121–2142, DOI 10.3934/dcdsb.2019204, first available online **2019-09-17**: https://www.aimsciences.org/article/doi/10.3934/dcdsb.2019204 . Later arXiv deposit: https://arxiv.org/abs/2402.04041 .
2. R. J. Sacker, *Global stability in a multi-species periodic Leslie–Gower model*, *Journal of Biological Dynamics* **5** (2011), 549–562, DOI 10.1080/17513758.2011.554891, https://www.tandfonline.com/doi/full/10.1080/17513758.2011.554891 .
3. *Critical-extinction trichotomy for a symmetric Ricker–Beverton–Holt map*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-critical-extinction-trichotomy-for-a-symmetric-ricker-beverton-h--c5cfc413632f .
4. *A critical extinction-exponent trichotomy for periodically harvested rank-one competition*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-critical-extinction-exponent-trichotomy-for-periodically-harve--55e6694e28df .
