# Dilogarithmic covariance and sharp finite-window variance bias for expanding maps

## Finding
For every integer \(b\ge2\), let \(T_b(x)=\{bx\}\) on \([0,1)\), equipped with Lebesgue probability, and let \(g(x)=-\log x\) on \((0,1)\). The stationary sums are \(S_N(x)=\sum_{t=0}^{N-1}g(T_b^t x)\). For all integers \(m\ge1\), set
\[
C(m)=1+\frac1m\sum_{j=1}^{m-1}j\operatorname{Li}_2(-1/j),
\]
where an empty sum is zero and \(\operatorname{Li}_2(z)=\sum_{k=1}^{\infty}z^k/k^2\) for \(|z|\le1\) in the real range used here. Then the exact lag-\(k\) stationary covariance is \(\operatorname{Cov}(g,g\circ T_b^k)=C(b^k)\) for \(k\ge0\). The sequence \(C(m)\) is strictly positive and strictly decreasing over positive integers.

There is a universal constant
\[
B=1+\frac{\gamma}{4}+\sum_{q=3}^{\infty}\frac{(-1)^q\zeta(q-1)}{q^2}
 =1.0102793965954957\ldots
\]
with the sharp expansion, as \(m\to\infty\) through positive integers,
\[
C(m)=\frac{\frac14\log m+B}{m}-\frac1{72m^2}+\frac1{288m^3}+O(m^{-4}).
\]
In particular, \(C(b^k)\sim k(\log b)/(4b^k)\) as \(k\to\infty\): covariance has a logarithmically enhanced exponential tail.

For every integer \(N\ge1\), the positive, convergent constants
\[
\sigma_b^2=1+2\sum_{k=1}^{\infty}C(b^k),\qquad
\kappa_b=2\sum_{k=1}^{\infty}kC(b^k)
\]
give the **exact** finite-window identity
\[
\operatorname{Var}(S_N)=N\sigma_b^2-\kappa_b+R_{b,N},\qquad
R_{b,N}=2\sum_{k=N}^{\infty}(k-N)C(b^k)>0.
\]
The correction is sharp:
\[
R_{b,N}=\frac{N\,b^{1-N}\log b}{2(b-1)^2}+O_b(b^{-N}).
\]
The long-run variance \(\sigma_b^2\) is strictly decreasing in integer \(b\ge2\) and tends to \(1\), with
\[
\sigma_b^2=1+\frac{\frac12\log b+2B}{b}+O\bigl((\log b)b^{-2}\bigr).
\]
For doubling, the formula evaluates numerically to \(\sigma_2^2\approx3.705486\), agreeing with the earlier numerical value reported for this singular observable.

## Assumptions and scope
The dynamics are deterministic integer expanding maps \(T_b\) with \(b\) an integer at least two, the initial point is Lebesgue-distributed, and the observable is \(-\log x\) (not \(-\log|x-a|\) with arbitrary \(a\)). The exceptional orbit points at which a logarithm is undefined form a null set. All covariances and variances are ordinary Lebesgue moments; \(g\in L^2\), with mean \(1\) and variance \(1\). The formula is an exact finite-time statement and does not assert a central limit theorem, a large-deviation theorem, or any result for noninteger slopes.

## Proof
**One-step branch integration.** For any integer \(m\ge1\), the transformation \(T_m(x)=\{mx\}\) has \(m\) equally weighted inverse branches \(x=(j+y)/m\), with \(0\le j\le m-1\). Thus
\[
\int_0^1\log x\,\log\{mx\}\,dx
=\log m+\frac1m\sum_{j=0}^{m-1}J(j),\quad
J(j)=\int_0^1\log(j+y)\log y\,dy.
\]
Direct integration gives \(J(0)=2\). Integration by parts and \(\int_0^1\log y/(j+y)\,dy=\operatorname{Li}_2(-1/j)\) give, for positive integer \(j\),
\[
J(j)=2-\log(j+1)+j\operatorname{Li}_2(-1/j)-j\log((j+1)/j).
\]
The logarithmic terms telescope to \(-m\log m\), so the uncentered moment equals \(2+m^{-1}\sum_{j=1}^{m-1}j\operatorname{Li}_2(-1/j)\). Subtracting \((\mathbb E g)^2=1\) proves the asserted exact \(C(m)\). Since \(T_b^k(x)=\{b^kx\}\) and Lebesgue measure is invariant, these are precisely the stationary lag covariances.

**Positivity and monotonicity.** Put \(r_0=1\) and \(r_j=1+j\operatorname{Li}_2(-1/j)\) for positive \(j\). The integral form
\[
r_j=\int_0^1\left(1-\frac{\log(1+s/j)}{s/j}\right)\,ds
\]
shows \(0<r_j<1/(4j)\), because \(0<1-\log(1+u)/u<u/2\) for \(u>0\). Moreover this integrand is strictly increasing in \(u\), so \(r_j\) strictly decreases with \(j\), and \(r_0>r_1\). Since \(C(m)=m^{-1}\sum_{j=0}^{m-1}r_j\), its strict positivity and decrease follow by averaging a strictly decreasing positive sequence.

**Asymptotic covariance.** The convergent dilogarithm series yields
\[
r_j=\sum_{q=2}^{\infty}\frac{(-1)^q}{q^2 j^{q-1}}
=\frac1{4j}-\frac1{9j^2}+\frac1{16j^3}+O(j^{-4}).
\]
Writing \(H_{m-1}^{(s)}=\sum_{j=1}^{m-1}j^{-s}\), sum by powers to obtain
\[
mC(m)=1+\tfrac14 H_{m-1}^{(1)}
 +\sum_{q=3}^{\infty}\frac{(-1)^q}{q^2}H_{m-1}^{(q-1)}.
\]
The \(q\ge3\) infinite sum can be interchanged with the finite \(j\)-sum and its limiting zeta-series is absolutely convergent. Euler--Maclaurin expansions
\[
H_{m-1}^{(1)}=\log m+\gamma-\frac1{2m}-\frac1{12m^2}+O(m^{-4}),
\]
\[
H_{m-1}^{(2)}=\zeta(2)-m^{-1}-\tfrac12m^{-2}+O(m^{-3}),\qquad
H_{m-1}^{(3)}=\zeta(3)-\tfrac12m^{-2}+O(m^{-3})
\]
and the bounds \(\zeta(s)-H_{m-1}^{(s)}=O(m^{1-s})\) for \(s\ge4\) yield \(mC(m)=\frac14\log m+B-1/(72m)+1/(288m^2)+O(m^{-3})\). (For the stated order, terms with \(q\ge5\) contribute only \(O(m^{-3})\).) Divide by \(m\).

**Finite-time variance and bias.** Stationarity and pair counting give, exactly,
\[
\operatorname{Var}(S_N)=N+2\sum_{k=1}^{N-1}(N-k)C(b^k).
\]
Because \(C(b^k)=O_b(kb^{-k})\), the definitions of \(\sigma_b^2\) and \(\kappa_b\) converge absolutely. Add and subtract their tails to obtain the asserted exact remainder \(R_{b,N}\). Substituting the leading lag expansion into the remainder and writing \(k=N+j\), the identity \(\sum_{j\ge0}j b^{-j}=b/(b-1)^2\) gives the explicit leading coefficient, with remainder \(O_b(b^{-N})\). Finally, strict decrease of \(C(m)\) gives \(\sigma_{b+1}^2<\sigma_b^2\). The large-\(b\) asymptotic follows by keeping the \(k=1\) term in the convergent covariance series and bounding the remaining terms by \(O((\log b)b^{-2})\).

## Verification
A standalone checker (`check.py`) independently evaluates the original branch integral by numerical quadrature for \(m=1,2,3,4,5,8\), compares it with the dilogarithmic formula, checks strict monotonicity for 80 consecutive values, checks the three-term large-\(m\) expansion, and verifies the exact finite-window identity for several integer slopes and lengths. It reports `PASS`. These are finite numerical tests, not substitutes for the preceding analytical proof. The original source reports the doubling asymptotic-variance numerical value, which agrees with the series calculation.

## Relationship to prior work
Defaveri and Smith study the same singular Birkhoff sum for doubling, tent, and logistic maps, deriving its dynamical fluctuation regimes and reporting a numerical Green--Kubo variance for doubling. The present result supplies the exact integer-slope lag covariance in dilogarithms, sharp large-lag expansion, and an exact signed finite-window variance bias with a leading coefficient. Nicol and Schindler address large deviations for logarithm-singular observables at periodic and preperiodic points, not the exact covariance or finite-window variance identity established here. Standard branch calculus and Green--Kubo pair counting are used rather than claimed as new tools.

## Limitations
No independence or external review has been performed. The result concerns only a fixed logarithmic singularity at the origin and integer expanding maps. It supplies variance identities but not a central limit theorem or rates in distribution. Although relevant primary papers and targeted literature searches were inspected, undetected equivalent formulas or a stronger historical result remain possible; priority is therefore provisional.

## References
1. L. Defaveri and N. R. Smith, *Dynamical phase transition for a logarithm observable in chaotic systems*, arXiv:2610.21288v1 (first public 2026-10-15), https://arxiv.org/html/2610.21288v1.
2. M. Nicol and T. I. Schindler, *Large deviations for observables with logarithmic singularity and differentiability of the pressure function*, arXiv:2610.35221v1 (first public 2026-10-26), https://arxiv.org/html/2610.35221v1.
