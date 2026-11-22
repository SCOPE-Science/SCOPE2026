# Exact density-total-positivity region of the two-mode Legendre copula

## Finding

For real parameters \(\lambda_1,\lambda_2\), consider the polynomial function
\[
C_{\lambda_1,\lambda_2}(u,v)=uv+3\lambda_1u(1-u)v(1-v)+5\lambda_2(2u^3-3u^2+u)(2v^3-3v^2+v),\quad (u,v)\in[0,1]^2.
\]
Its mixed density is totally positive of order two (density-TP2), and \(C_{\lambda_1,\lambda_2}\) is a copula, **if and only if**
\[
\boxed{\quad\frac{3\sqrt5-7}{20}\le\lambda_2\le\frac1{10},\qquad
\frac{15|\lambda_2|}{1+20\lambda_2}\le\lambda_1\le\frac{1+5\lambda_2}{3}.\quad}
\]
Every endpoint is included. Equivalently, for \(x=2u-1\), \(y=2v-1\), \(a=3\lambda_1\), and \(b=5\lambda_2/4\), the density
\[
c(u,v)=1+a xy+b(3x^2-1)(3y^2-1)
\]
is density-TP2 precisely when
\[
\boxed{\quad\frac{-7+3\sqrt5}{16}\le b\le\frac18,\qquad
\frac{36|b|}{1+16b}\le a\le1+4b.\quad}
\]
Within this density-TP2 subfamily, Spearman's rank correlation \(\rho_S\) fills exactly \([0,1/2]\), with the maximum \(\rho_S=1/2\) attained uniquely at \((\lambda_1,\lambda_2)=(1/2,1/10)\). This is a characterization of this specified **two-mode bivariate family**, not all polynomial or Legendre copulas.

## Assumptions and scope

Both coefficients are arbitrary real numbers before the criterion is imposed. A bivariate copula is a grounded, two-increasing function with unit-uniform marginals. For a continuous nonnegative density \(c\), density-TP2 means
\[
c(u_1,v_1)c(u_2,v_2)\ge c(u_1,v_2)c(u_2,v_1)
\quad\text{for every }0\le u_1\le u_2\le1,\quad 0\le v_1\le v_2\le1.
\]
Where \(c>0\), the criterion is equivalent to \(\partial_u\partial_v\log c\ge0\). The polynomial has uniform marginal densities for every parameter value because both nonconstant basis functions integrate to zero. Thus copula validity is exactly pointwise nonnegativity of the continuous density. All inequalities are nonstrict, including zero-density boundary points.

## Proof

**1. Necessary constraints.** Set \(x=2u-1,y=2v-1\). The density becomes
\[
c=1+a xy+b(3x^2-1)(3y^2-1),\quad (x,y)\in[-1,1]^2.
\]
The sign of \(\partial_u\partial_v\log c\) agrees with the sign of its \(x,y\) version. At \((x,y)=(1,1)\) and \((1,-1)\), density nonnegativity gives \(1+4b\pm a\ge0\); at \((1,0)\) it gives \(1-2b\ge0\). Therefore \(-1/4\le b\le1/2\) and \(|a|\le1+4b\).

Write \(D=c\,c_{xy}-c_xc_y\). Direct differentiation and cancellation yield the exact identity
\[
\boxed{D(x,y)=a[1+b(1+3x^2)(1+3y^2)]+36bxy.}\tag{1}
\]
Since \(b\ge-1/4\), the evaluation \(D(0,0)=a(1+b)\) forces \(a\ge0\). If \(b<0\), evaluating at \((1,1)\) gives \(a(1+16b)+36b\ge0\), hence \(b>-1/16\). If \(b>0\), evaluating at \((1,-1)\) gives \(a(1+16b)-36b\ge0\). In either case, a necessary condition is
\[
a\ge \frac{36|b|}{1+16b}.\tag{2}
\]
For \(-1/16<b<0\), combining (2) with \(a\le1+4b\) is possible exactly when \(1+56b+64b^2\ge0\). The only permitted branch in this interval is \(b\ge b_-:=(-7+3\sqrt5)/16\). Thus no more-negative \(b\) is possible.

For \(b>1/8\), density nonnegativity at \((x,y)=(1,-t)\), \(0<t\le1\), implies
\[
a\le\inf_{0<t\le1}\left\{\frac{1-2b}{t}+6bt\right\}=2\sqrt{6b(1-2b)}
\quad(1/8<b<1/2).
\]
At \(b=1/2\), the same inequality implies \(a=0\), contradicting (2). For \(1/8<b<1/2\), the bound contradicts (2), because
\[
(36b)^2-24b(1-2b)(1+16b)^2=24b(8b-1)^3>0.
\]
Therefore \(b\le1/8\). The necessary region is exactly the displayed candidate region.

**2. Copula validity throughout the candidate region.** Let \(r=|x|,s=|y|\). Since \(a\ge0\), the smallest density at given \(r,s\) has \(xy=-rs\); it is nonnegative if
\[
a\le Q_b(r,s):=\frac{1+b(3r^2-1)(3s^2-1)}{rs},\qquad r,s>0.
\]
Fix \(t=rs\in(0,1]\). The identity
\[
Q_b(r,s)=\frac{1+b}{t}+9bt-3b\frac{r^2+s^2}{t}
\]
and \(2t\le r^2+s^2\le1+t^2\) show the following. For \(b\le0\), the minimum over \(r,s\) at fixed \(t\) occurs at \(r=s=\sqrt t\), and equals \((1+b)/t+9bt-6b\); this decreases in \(t\) for \(-1/4\le b\le0\). For \(0\le b\le1/8\), the minimum occurs at \(\{r,s\}=\{1,t\}\), and equals \((1-2b)/t+6bt\), also decreasing for \(t\le1\). Consequently \(\inf Q_b=1+4b\), attained at \(t=1\). At \(r=0\) or \(s=0\), the density equals \(1+b(3r^2-1)(3s^2-1)\ge0\) for \(b\in[b_-,1/8]\). Hence \(a\le1+4b\) ensures \(c\ge0\) everywhere. The function therefore is a genuine copula.

**3. Density-TP2 throughout the candidate region.** In equation (1), the minimum over signs of \(x,y\) with fixed \(r,s\) is
\[
D_{\min}(r,s)=a[1+b(1+3r^2)(1+3s^2)]-36|b|rs.
\]
For \(b<0\), the bracket is positive and decreases as either \(r\) or \(s\) increases, while the subtracted term increases. Hence the smallest \(D_{\min}\) is at \(r=s=1\), where it equals \(a(1+16b)-36|b|\ge0\) by (2). For \(b=0\), \(D\equiv a\ge0\).

For \(0<b\le1/8\), set \(t=rs\). AM–GM gives \((1+3r^2)(1+3s^2)\ge(1+3t)^2\). Therefore
\[
D_{\min}(r,s)\ge a[1+b(1+3t)^2]-36bt.
\]
The function \(t/[1+b(1+3t)^2]\) is nondecreasing on \([0,1]\) because the numerator of its derivative, after multiplication by the squared denominator, is \(1+b-9bt^2\ge1-8b\ge0\). Its maximum is \(1/(1+16b)\). Condition (2) thus guarantees \(D\ge0\) everywhere.

The density is strictly positive in the interior of the square: the preceding copula-validity minimization has \(Q_b(r,s)>1+4b\) whenever \(r,s<1\), including the limiting cases \(b=1/8\) and \(b=b_-\). Thus \(\log c\) is well defined in the open square. The relation \(\partial_x\partial_y\log c=D/c^2\ge0\) integrates over each interior rectangle to prove density-TP2 there, and continuity extends it to rectangles touching the boundary. Necessity was already shown in Step 1. This proves the exact, closed region.

**4. Sharp rank-correlation envelope.** Direct integration of the copula polynomial (or its already published rank identity) gives \(\rho_S=\lambda_1=a/3\). In the density-TP2 region, \(0\le a\le1+4b\le3/2\), with equality \(a=3/2\) only when \(b=1/8\); at that point the lower bound (2) also equals \(3/2\). Therefore the sharp range is \([0,1/2]\), and the maximizer is unique. Every intermediate value is realized by the \(b=0\) section for \(0\le\rho_S\le1/3\) and by a continuous path in the closed admissible region from \((a,b)=(1,0)\) to \((3/2,1/8)\) for the remaining values.

## Verification

The standalone file `verify.py` checks identity (1), the quadratic and cubic boundary factorizations, the derivative needed for the infinite-domain bound, and an exact-rational finite grid of valid parameters and locations. It also verifies explicit witnesses outside the admitted region and the exact algebraic threshold. Run `python3 verify.py` with SymPy installed in the same directory. The observed output begins `VERIFICATION_OK rational_checks 12141`. The rational-grid checks support the calculations; they do not replace the complete continuous argument in Steps 1–4.

## Relationship to prior work

Longla [1,2] studied the specified freely parameterized two-mode Legendre copula and determined several mixing and rank-correlation properties, originally under sufficient parameter restrictions. The older one-parameter Sarmanov Legendre construction described by Drouet Mari and Kotz [6] is an important antecedent; it does not supply the two-independent-coefficient density-TP2 region calculated here. Longla and Mous-Abou Hamadou [3] subsequently gave broader sufficient restrictions and estimation results. An earlier published mathematical analysis [4] determined the full copula-admissibility region, as well as the unrestricted sharp Spearman and Kendall ranges. Those are established prior findings; the present work does **not** claim their rediscovery. In contrast, density-total-positivity and its exact strong-positive-dependence region are different requirements, not entailed by copula nonnegativity or rank-correlation bounds. In fact, many valid copulas in [4]'s full region have \(D<0\), including \((a,b)=(0,1/16)\). The new condition (1), its sharp simultaneous solution, and the strong-dependence rank envelope are the additions.

Fuchs and Tschimpke [5] study the hierarchy of positive dependence concepts, explaining that density-TP2 is stronger than ordinary copula TP2, stochastic increasingness, and Markov-kernel TP2. Their analyzed Archimedean and extreme-value families are not this two-mode polynomial family. Searches of the accessible prior primary literature and mathematical records found no complete covering density-TP2 classification for the specified density; unindexed or differently parameterized treatments remain a priority risk.

## Limitations

The classification concerns the specified bivariate two-term diagonal Legendre density, not other higher-mode, cross-mode, Archimedean or multivariate copula families. Its positivity statements are exact analytical theorems, while the checker is only finite corroboration. Nothing here proves optimal statistical estimation, empirical fit, or original invention of the copula family, its broad admissibility domain or its unrestricted rank formulas. The older Sarmanov literature has not been exhaustively examined for an equivalent two-independent-coefficient TP2 theorem. Historical priority remains subject to independent literature verification, and independent mathematical validation has not been performed.

## References

[1] M. Longla, *New copula families and mixing properties*, arXiv:2308.11074v1, publicly posted 21 August 2023, section 2.2.2, https://arxiv.org/abs/2308.11074.

[2] M. Longla, *New copula families and mixing properties*, *Statistical Papers* **65** (2024), 4331–4363, open-access full text, https://doi.org/10.1007/s00362-024-01559-9.

[3] M. Longla and Mous-Abou Hamadou, *Estimation problems for some perturbations of the independence copula*, *Statistical Papers* **66** (2025), article 156, open-access full text, https://doi.org/10.1007/s00362-025-01778-8.

[4] *Exact admissibility and sharp rank-correlation ranges for the two-mode Legendre copula* (2026), published proof and files, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-admissibility-and-sharp-rank-correlation-ranges-for-the-tw--4829e3cb0e98.

[5] S. Fuchs and M. Tschimpke, *Total positivity of copulas from a Markov kernel perspective*, arXiv:2205.01914, first posted 4 May 2022, https://arxiv.org/abs/2205.01914.

[6] D. Drouet Mari and S. Kotz, *Correlation and Dependence*, Imperial College Press (2001), section 5.7.2 on Sarmanov’s first two Legendre polynomials; publicly indexed book excerpt at https://www.scribd.com/document/752744010/Kotz-Correlation-and-dependence.
