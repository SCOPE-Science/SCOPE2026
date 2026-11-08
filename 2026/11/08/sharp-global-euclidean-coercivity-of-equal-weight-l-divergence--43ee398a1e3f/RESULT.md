# Sharp global Euclidean coercivity of equal-weight L-divergence

## Finding
For every integer \(n\ge2\) the equal-weight geometric-mean L-divergence has the **sharp, dimension-dependent, globally state-space-independent** Euclidean coercivity constant:
\[
\boxed{T_n(q\mid p)\ge\frac{2}{n}\|q-p\|_2^2}\qquad(p,q\in\Delta_n^\circ).
\]
The inequality is strict unless \(p=q\). Its coefficient is optimal over all pairs in the *open* simplex: a two-coordinate perturbation near a boundary face approaches it. This finite-step inequality sharpens the compact-set-dependent coercivity in the recent restricted-market-weight setting and gives a uniform lower bound on worst-case long-run relative growth.

## Assumptions and scope
Let \(n\ge2\) be an integer and
\[
\Delta_n^\circ=\{p\in(0,1)^n:\sum_{i=1}^{n}p_i=1\}.
\]
For \(p,q\in\Delta_n^\circ\) put \(r_i=q_i/p_i\) and define
\[
T_n(q\mid p)=\log\left(\frac1n\sum_{i=1}^n r_i\right)-\frac1n\sum_{i=1}^n\log r_i.
\]
This is precisely the one-step L-divergence of \(\Phi(p)=(\prod_{i=1}^np_i)^{1/n}\), which generates a portfolio holding weight \(1/n\) in each asset at each rebalancing time. The Euclidean norm is the standard norm on \(\mathbb R^n\), with no rescaling of the simplex metric. The asserted coefficient does not depend on how close \(p,q\) are to the boundary, and the conclusion is valid for arbitrarily large one-step displacements within the open simplex.

For the dynamical consequence, take a nonempty compact set \(K\subset\Delta_n^\circ\), and a nonempty compact, forward-left-shift-invariant path space \(\Omega\subset K^{\mathbb N_0}\). Suppose \(\rho>0\), \(C\ge0\), and every \(\omega\in\Omega\) satisfies
\[
\sum_{k=s}^{s+t-1}\|\omega_{k+1}-\omega_k\|_2^2\ge\rho t-C
\quad\text{for all integers }s\ge0,\ t\ge1.
\]
The associated global worst-case rate is
\[
\gamma(\Phi,\Omega)=\lim_{t\to\infty}\min_{\omega\in\Omega}\frac1t\log V_{\pi}(t,\omega),
\]
with \(V_{\pi}\) the relative wealth from rebalancing to equal portfolio weights every step. We establish \(\gamma(\Phi,\Omega)\ge (2/n)\rho\). Neither convexity of \(K\) nor a small-jump restriction is needed for this improved bound.

## Proof
**1. An exact range estimate for the logarithmic arithmetic/geometric gap.** For any positive real numbers \(r_1,\dots,r_n\), let \(m=\min_i r_i\) and \(M=\max_i r_i\). We prove
\[
\log\left(\frac1n\sum_i r_i\right)-\frac1n\sum_i\log r_i
\ge\frac2n\log\frac{m+M}{2\sqrt{mM}}.\tag{1}
\]
If \(m=M\), both sides vanish. Otherwise, hold fixed one occurrence each of the minimum and maximum, and minimize the left side over all remaining coordinates in the box \([m,M]^{n-2}\). The minimum is attained by compactness. Writing \(A=(\sum_i r_i)/n\), the partial derivative with respect to any free coordinate \(z\) is
\[
\frac{\partial}{\partial z}\left(\log A-\frac1n\sum_i\log r_i\right)=\frac{z-A}{n z A}.
\]
Since \(m<A<M\), an additional free coordinate at either endpoint cannot minimize (its inward derivative lowers the objective). Thus each free coordinate lies in the interior and equals \(A\). Therefore \(nA=m+M+(n-2)A\), so \(A=(m+M)/2\), and all free coordinates equal this midpoint. Substitution gives (1), with equality at this midpoint configuration. The argument for \(n=2\) is immediate because no coordinates are free.

**2. The sharp range control on total variation.** In the simplex setting, \(\sum_i p_i r_i=1\). Put \(v=\tfrac12\sum_i|q_i-p_i|=\tfrac12\sum_i p_i|r_i-1|\). For every \(x\in[m,M]\), convexity of \(x\mapsto|x-1|\) gives its chord estimate; averaging with weights \(p_i\) yields
\[
2v\le\frac{2(1-m)(M-1)}{M-m},\quad\text{hence}\quad
v\le\frac{(1-m)(M-1)}{M-m}.
\]
Here \(m\le1\le M\) because the \(p\)-weighted mean of the ratios is one. In general, for a mean \(c\in[m,M]\), maximizing the normalized bound \((c-m)(M-c)/(c(M-m))\) over \(c\) gives the maximizing point \(c=\sqrt{mM}\). Accordingly,
\[
v\le\frac{\sqrt M-\sqrt m}{\sqrt M+\sqrt m}=\tanh x,
\qquad x=\tfrac14\log(M/m).\tag{2}
\]
There is no equality issue when \(m=M\), in which case \(p=q\).

**3. Total variation controls Euclidean displacement.** The coordinate increments \(d_i=q_i-p_i\) sum to zero. Their positive parts and negative parts each have total mass \(v\). For a collection of nonnegative numbers with sum \(v\), the sum of squares is at most \(v^2\). Hence
\[
\|q-p\|_2^2=\sum_i d_i^2\le2v^2\le2\tanh^2x.\tag{3}
\]

**4. Hyperbolic comparison.** A direct identity gives
\[
\frac{m+M}{2\sqrt{mM}}=\cosh(2x).
\]
If \(u=\tanh^2x\in[0,1)\), then
\[
\log\cosh(2x)=\log\frac{1+u}{1-u}=2\operatorname{artanh}u\ge2u,
\]
strictly when \(u>0\), since \(\operatorname{artanh}u-u=\int_0^u\frac{t^2}{1-t^2}\,dt\). Combining this with (1)–(3) gives
\[
T_n(q\mid p)\ge\frac4n\tanh^2x\ge\frac2n\|q-p\|_2^2.
\]
If \(p\ne q\), then \(m<M\), \(u>0\), and the first comparison is strict.

**5. Optimality over strictly positive probability vectors.** Let \(n\ge2\). If \(n=2\), take \(p=(1/2,1/2)\). If \(n>2\), choose \(\varepsilon>0\) with \((n-2)\varepsilon<1\), put \(a=(1-(n-2)\varepsilon)/2\), and set
\[
p=(a,a,\varepsilon,\ldots,\varepsilon),\qquad
q=(a+t,a-t,\varepsilon,\ldots,\varepsilon),\quad0<t<a.
\]
For \(n=2\) the same expression applies with \(a=1/2\) and no final coordinates. The mean of the ratios is exactly one and
\[
T_n(q\mid p)=-\frac1n\log\left(1-\frac{t^2}{a^2}\right),
\quad\|q-p\|_2^2=2t^2.
\]
Consequently \(\lim_{t\downarrow0}T_n(q\mid p)/\|q-p\|_2^2=1/(2na^2)\). For \(n>2\), then letting \(\varepsilon\downarrow0\) gives \(2/n\). For \(n=2\), the limit is already \(2/n=1\). All *approximating* vectors have strictly positive coordinates, so no extension to boundary points is being assumed. The coefficient cannot be increased.

**6. Uniform worst-case-growth consequence.** Write \(\phi=\log\Phi=n^{-1}\sum_i\log p_i\). The exact one-step relative wealth for the equal-weight portfolio is \(n^{-1}\sum_i\omega_{k+1,i}/\omega_{k,i}\). Taking logarithms and telescoping the \(\phi\) terms gives
\[
\log V_{\pi}(t,\omega)
=\phi(\omega_t)-\phi(\omega_0)+\sum_{k=0}^{t-1}T_n(\omega_{k+1}\mid\omega_k).
\]
The compactness of \(K\subset\Delta_n^\circ\) bounds the endpoint term below by \(-\operatorname{osc}_K\phi\). Therefore for every integer \(t\ge1\) and every allowed path
\[
\log V_{\pi}(t,\omega)
\ge\frac2n(\rho t-C)-\operatorname{osc}_K\phi.
\]
Taking minima and dividing by \(t\) proves the claimed bound on \(\gamma\). For completeness, existence of the limit follows either from the cited path-space theorem or directly: the minimum \(b_t=\min_{\omega\in\Omega}\log V_{\pi}(t,\omega)\) is superadditive because the left shift preserves \(\Omega\), and the one-step relative-wealth factors are uniformly bounded above and below on compact \(K\); thus Fekete's lemma gives \(\lim b_t/t\).

## Verification
The attached standalone Python program `verify.py` uses only the standard library. It directly evaluates both sides of the theorem on strictly positive rational simplex grids, independently samples further simplex pairs, tests the range and total-variation lemmas, checks the sharpness family, and accumulates L-divergence along alternating two-state paths. The program is finite corroboration only. Running `python3 verify.py` produced:

```text
VERIFY_OK exact_grid_pairs=68982 range_enumerations=39000 randomized_simplex_pairs=19800 boundary_sharpness=81 two_cycle_checks=24
```

The proof of the statement for arbitrary real \(n,p,q\) and infinite path families is analytic; the finite tests alone do not establish that universality. In the command above, `python3` denotes an ordinary Python 3 interpreter, with no third-party packages.

## Relationship to prior work
Xu and Cui's recent work [1], Appendix B, treats an equal-weight portfolio in a three-asset compact-state model. Its bound is \(T\ge c_K\|q-p\|_2^2\), for example \(c_K=1/(24M^2)\), where the ratio ceiling \(M\) depends on the state set. The present theorem removes that dependence, identifies the exact global coefficient for every \(n\ge2\), and shows why two active coordinates are asymptotically extremal. The pathwise consequence strengthens their Proposition B.1 under the same cumulative-variation mechanism.

Campbell and Wong [2] develop the logarithmic Jensen gap and derive its local quadratic metric (Remark 3.19), but the inspected text does not furnish this exact global finite-displacement Euclidean constant. Pal and Wong [3] give the L-divergence formula and pathwise wealth decomposition, and [4] develops its information geometry; those formulations and local metrics are used as background, not claimed as new. These comparisons distinguish a global sharp coercivity result from existing definitions, local Hessian expansions, and compact-dependent positivity estimates.

## Limitations
The theorem is for equal investment weights and strictly positive simplex coordinates. It does not assert the same constant for arbitrary nonuniform portfolio allocations, for other divergences or coordinate metrics, or for paths leaving a compact interior state set. The coefficient \(2/n\) is a sharp bound for the divergence, not a proof that the induced worst-case dynamic rate equals \((2/n)\rho\) for every restricted path family; only the stated lower bound is established. Historical priority outside the inspected primary literature remains provisional. Independent scientific validation has not been performed.

## References
[1] J. Xu and X. Cui, *Worst-Case Relative Growth of Functionally Generated Portfolios under Restricted Market-Weight Dynamics*, arXiv:2610.41603v1 (first posted 2026-10-30), especially Appendix B. https://arxiv.org/html/2610.41603v1

[2] S. Campbell and T.-K. L. Wong, *A mathematical study of the excess growth rate*, arXiv:2510.25740 (first posted 2025-10-29), especially Section 3.3 and Remark 3.19. https://arxiv.org/html/2510.25740v2

[3] S. Pal and T.-K. L. Wong, *The Geometry of Relative Arbitrage*, arXiv:1402.3720 (first posted 2014-02-17), especially Sections 2.4 and 2.6. https://arxiv.org/html/1402.3720v5

[4] S. Pal and T.-K. L. Wong, *Exponentially Concave Functions and a New Information Geometry*, *Annals of Probability* 46 (2018), 1070–1113, doi:10.1214/17-AOP1201, especially the Introduction and Section 2. https://projecteuclid.org/journals/annals-of-probability/volume-46/issue-2/Exponentially-concave-functions-and-a-new-information-geometry/10.1214/17-AOP1201.pdf
