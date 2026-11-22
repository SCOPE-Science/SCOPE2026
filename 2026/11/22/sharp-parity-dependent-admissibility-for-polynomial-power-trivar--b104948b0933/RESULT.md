# Sharp parity-dependent admissibility for polynomial-power trivariate copulas

## Finding

For every integer \(m\geq1\), every real \(\theta\geq0\), and every real \(\lambda\), consider the trivariate function introduced in Chesneau (2024),
\[
C_{m,\theta,\lambda}(x,y,z)=xyz\bigl[1+\lambda(x-y)^m z^\theta(1-z)\bigr],\qquad (x,y,z)\in[0,1]^3.
\]
At \(z=0\) and \(\theta=0\), use the continuous extension of the entire expression. Define
\[
r_0=1,\qquad r_\theta=\left(\frac{\theta}{\theta+2}\right)^\theta\quad(\theta>0).
\]
For even \(m\), define \(M_2=2\). For even \(m\geq4\), let \(s_m\) be the unique root in \((0,1)\) of
\[
(m+1)s^2+(m-1)^2s-(m-1)(m-2)=0,
\]
and put
\[
M_m=s_m^{m-2}\bigl[m(m-1)(1-s_m)-(m+1)s_m^2\bigr].
\]
Then **the exact, necessary-and-sufficient copula parameter range** is
\[
\boxed{\begin{cases}
-\dfrac1{m+1}\leq\lambda\leq\dfrac1{m+1},&m\ \text{odd},\\[5pt]
-\dfrac1{\max\{(m+1)r_\theta,M_m\}}\leq\lambda\leq\dfrac1{m+1},&m\ \text{even}.
\end{cases}}
\]
There are no other admissible real values of \(\lambda\).

For every even \(m\), \(0<M_m<m+1\) and \(M_m/(m+1)>e^{-2}\). Hence there is a unique \(\theta_m>0\) satisfying \(r_{\theta_m}=M_m/(m+1)\). The lower admissible boundary is \(-1/[(m+1)r_\theta]\) for \(0\leq\theta\leq\theta_m\) and is the constant \(-1/M_m\) thereafter. In contrast, for odd \(m\) the sharp interval is independent of \(\theta\).

In the simplest even case \(m=2\), \(\theta=1\), the *full* parameter range is \(-1/2\leq\lambda\leq1/3\), whereas the previously published sufficient range is \(|\lambda|\leq1/6\). In particular \(\lambda=-2/5\) gives a valid trivariate copula beyond the published range. For \(m=2\), the transition satisfies \((\theta_2/(\theta_2+2))^{\theta_2}=2/3\) and is approximately \(0.1535284495278\).

## Assumptions and scope

The integers \(m\) cover the entire positive range, \(\theta\) is any finite nonnegative real, and \(\lambda\) is unrestricted until the copula condition is applied. The proposed function has uniform one-dimensional margins and vanishes when any coordinate is zero, for every choice of \(\lambda\); the only remaining condition for it to be a trivariate distribution with an absolutely continuous density is nonnegativity of the mixed third derivative. The theorem is pointwise in parameters; it requires no discreteness of \(\theta\) and does not cover \(\theta<0\) or noninteger \(m\).

## Proof

**1. Density and margins.** Write
\[
B_\theta(z)=z^\theta[(\theta+2)z-(\theta+1)],
\]
and
\[
D_m(x,y)=\partial_x\partial_y\bigl[xy(x-y)^m\bigr].
\]
For \(m=1\), \(D_1(x,y)=2(x-y)\). For \(m\geq2\),
\[
D_m(x,y)=(m+1)(x-y)^m-m(m-1)xy(x-y)^{m-2}.
\]
Direct differentiation gives the continuous mixed density
\[
c_{m,\theta,\lambda}(x,y,z)=1-\lambda D_m(x,y)B_\theta(z).
\]
All one-dimensional margins are uniform because \(C(x,1,1)=x\), \(C(1,y,1)=y\), \(C(1,1,z)=z\), and the vanishing-face conditions hold. The fundamental theorem of calculus applied to the mixed derivative shows that \(c\geq0\) everywhere is sufficient for three-increasingness. Conversely, if this continuous density is negative at an interior point, a small box has negative probability. A strict violation occurring at a boundary point extends into the interior by continuity. Thus \(c\geq0\) on the closed cube is also necessary.

**2. Exact range of the \(z\) factor.** For \(\theta=0\), \(B_0(z)=2z-1\). For \(\theta>0\),
\[
B_\theta'(z)=(\theta+1)z^{\theta-1}[(\theta+2)z-\theta],
\]
so its minimum is \(-r_\theta\) at \(z=\theta/(\theta+2)\), while its maximum is \(1\) at \(z=1\). Thus its exact image is \([-r_\theta,1]\) for all \(\theta\geq0\). Moreover \(r_\theta\) decreases strictly from \(1\) to \(e^{-2}\), since the derivative of its logarithm is \(-\log(1+2/\theta)+2/(\theta+2)<0\).

**3. Exact range of the \((x,y)\) factor.** For \(m\geq2\) let \(s=|x-y|\in[0,1]\). At a fixed \(s\), the product \(p=xy\) ranges exactly over \([0,1-s]\), by letting one coordinate range from \(s\) to \(1\) and the other equal the first minus \(s\). Consequently, for even \(m\),
\[
D_m=s^{m-2}[(m+1)s^2-m(m-1)p].
\]
Its maximum is \(m+1\), attained at \((x,y)=(1,0)\) or its reversal. Its minimum is the negative of
\[
\max_{0\leq s\leq1}H_m(s),\quad
H_m(s)=s^{m-2}[m(m-1)(1-s)-(m+1)s^2].
\]
When \(m=2\), \(H_2(s)=2(1-s)-3s^2\) decreases strictly and the maximum is \(2\). For \(m\geq4\),
\[
H_m'(s)=m s^{m-3}[(m-1)(m-2)-(m-1)^2s-(m+1)s^2].
\]
The bracket is strictly decreasing on \([0,1]\), positive at zero and negative at one. Its unique root \(s_m\) is the global maximizer, yielding precisely \(M_m\) above. Also \(0<M_m<m+1\): for \(m\geq3\),
\[
H_m(s)\leq m(m-1)s^{m-2}(1-s)\leq m\left(\frac{m-2}{m-1}\right)^{m-2}<m+1;
\]
for \(m=2\), \(M_2=2<3\).

If \(m\) is odd, exchanging \(x\) and \(y\) negates \(D_m\). The preceding bound \(|D_m|\leq m+1\) follows by the same fixed-\(s\) argument: the positive term is at most \((m+1)s^m\), and the magnitude of the negative term is at most \(m(m-1)s^{m-2}(1-s)\leq m\) for \(m\geq3\), with \(m=1\) checked directly. Since \(D_m(1,0)=m+1\) and \(D_m(0,1)=-(m+1)\) for odd \(m\), its exact image is \([-(m+1),m+1]\).

**4. Product extrema and necessity.** Since \((x,y)\) and \(z\) vary independently, the extrema of \(D_m(x,y)B_\theta(z)\) are among products of endpoints of their exact ranges. For odd \(m\) this range has extrema \(-(m+1)\) and \(m+1\); for even \(m\) they are
\[
-\max\{(m+1)r_\theta,M_m\}\quad\text{and}\quad m+1.
\]
The condition \(1-\lambda D_mB_\theta\geq0\) everywhere gives exactly the two displayed parameter intervals, including both endpoints. Outside either interval an extremal factor product makes the density strictly negative, in the interior or at a boundary with negative interior neighbors, so the condition is also necessary.

**5. Genuine parity-dependent transition.** For even \(m\), \(M_m/(m+1)<1\). The lower bound is strictly above \(e^{-2}\): for \(m=2\) this is \(2/3>e^{-2}\). For even \(m\geq4\), evaluate \(H_m\) at \(s=1-2/m\) to obtain
\[
\frac{M_m}{m+1}\geq
\left(1-\frac2m\right)^{m-2}\left(1-\frac{4}{m^2(m+1)}\right)>e^{-2}.
\]
For completeness, if \(0<t<1\), the series \(\log(1-t)+t/(1-t)=\sum_{k\ge2}(1-1/k)t^k\ge t^2/2\). With \(t=2/m\), this bounds the first logarithm below by \(-2+2(m-2)/m^2\). For \(u=4/[m^2(m+1)]\), \(\log(1-u)\ge-u/(1-u)\ge-1/m^2\) for \(m\ge4\). Adding establishes the strict claimed bound. Strict decrease and the endpoint limits of \(r_\theta\) now give a unique finite \(\theta_m\) and the two stated branches.

## Verification

Run `python check_admissibility.py` with Python, SymPy and SciPy. It checks exact symbolic mixed-derivative identities for twelve integer exponents, checks globally optimized numerical factor extrema over forty combinations of exponents and shape parameters, checks even-exponent root inequalities, and checks the \(m=2\) transition value. The file produced 118 passing assertions. Numerical global optimization is supplementary evidence; steps 1–5 above prove the global statements for every allowed parameter. The checker is standalone and contains no external data dependencies.

## Relationship to prior work

Chesneau (2024), Proposition 2.1, introduces precisely this first nonexchangeable trivariate copula and proves the **sufficient** condition
\[
|\lambda|\leq\frac1{(\theta+1)\max\{m(m-1),m+1\}}.
\]
The original Table 1 uses that restricted condition in concrete cases. The present theorem does not claim the formula or the basic density differentiation as new. It determines the previously unspecified **necessary-and-sufficient** domain, including its parity-dependent asymmetric negative boundary and transition. This cannot follow from the prior sufficient inequality: at \(m=2,\theta=1,\lambda=-2/5\) the previous inequality fails but the exact density bound proves admissibility. For odd \(m\), the sharp bound is independent of \(\theta\), unlike the earlier sufficient range.

The other polynomial three-dimensional copula in the same paper (Proposition 3.1) uses a distinct perturbation with parameters \(\alpha,\beta\). Classical trivariate FGM copulas likewise have a different density polynomial. Neither formula identifies the exact admissibility region for the present family. General copula criteria characterize admissibility by density positivity, but do not supply the needed global extrema or the parity transition. No claim of comprehensive historical priority or independent review is made.

## Limitations

The classification only concerns the first Chesneau (2024) family and is not a classification of every trivariate polynomial-power or distorted copula. The shape exponent is an integer; the real exponent \(\theta\) must be nonnegative. The density can vanish on boundary or interior points at extremal parameters; no assertion of strict density positivity at the endpoints is made. No distribution-estimation, finite-sample inference, or tail-dependence performance statement follows without further analysis. The literature comparison is limited to accessible primary materials and mathematical search records; unindexed or inaccessible results could alter the priority assessment.

## References

1. C. Chesneau, “On Two Simple, Three-Parameter, Three-Dimensional, Non-Exchangeable Copulas,” *Contemporary Mathematics* **5**(1), 874–887 (2024), first published 29 February 2024, DOI: https://doi.org/10.37256/cm.5120242507. Specifically Proposition 2.1, its proof and Table 1. Public full text: https://ojs.wiserpub.com/index.php/CM/article/download/2507/1971/38771.
2. H. Joe, *Dependence Modeling with Copulas* (2014), general background on copula density nonnegativity and dependence families; no special parameter-extremum result invoked.
3. “Simplified pair copula constructions—Limitations and extensions,” *Journal of Multivariate Analysis* (2013), DOI: https://doi.org/10.1016/j.jmva.2013.04.014 (background on the classical trivariate FGM family, not this polynomial-power family).
