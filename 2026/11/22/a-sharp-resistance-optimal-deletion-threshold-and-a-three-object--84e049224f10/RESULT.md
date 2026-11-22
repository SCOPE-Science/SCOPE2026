# A sharp resistance-optimal deletion threshold and a three-objective price ladder on complete networks

## Finding

**Theorem.** Fix an integer \(n\ge4\), a resource budget \(B>0\), and a relative conductance price \(r>0\). On the complete graph \(K_n\), every edge conductance \(w_{ij}\ge0\) is adjustable independently. Edge \(\{1,2\}\) costs \(r\) per unit, while every other edge costs one. Subject to
\[
 r w_{12}+\sum_{\{i,j\}\ne\{1,2\}}w_{ij}\le B,
\]
minimize the sum of all pairwise effective resistances (Kirchhoff index)
\[
 \mathcal K(w)=\sum_{i<j}R_{ij}(w)=n\operatorname{tr}L(w)^\dagger,
\]
assigning cost \(+\infty\) to disconnected positive-conductance supports.

For all the stated parameters there is **one and only one global minimizer**. It has the edge classes \(a=w_{12}\), \(b=w_{1j}=w_{2j}\) for \(3\le j\le n\), and \(c=w_{ij}\) for \(3\le i<j\le n\). Put \(k=n-2\), and define the sharp price
\[
\boxed{r_A(n)=\frac{n}{n-2}.}
\]
If \(0<r<r_A(n)\), set
\[
 h=\sqrt{n\left(\frac{2(n-1)}r-(n-2)\right)},\qquad
 T=n-1+\frac{r(h-n+2)+(n-3)\sqrt r\,h}{2}.
\]
Then the unique optimal conductances are strictly positive and equal to
\[
\boxed{a=\frac{B(h-n+2)}{2T},\quad b=\frac BT,\quad
 c=\frac{B(\sqrt r\,h-2)}{(n-2)T}.}
\]
For \(r\ge r_A(n)\), set \(\Delta=\sqrt{n(n-2)}\) and \(T_0=n-1+(n-3)\Delta/2\). The unique optimum instead is
\[
\boxed{a=0,\quad b=\frac B{T_0},\quad c=\frac{B(\Delta-2)}{(n-2)T_0}>0.}
\]
The two formulas agree at the threshold (where the first gives \(a=0\)). The exact optimum is
\[
\boxed{\mathcal K^*=\begin{cases}
\dfrac{2nT^2}{r h^2 B},&0<r<r_A(n),\\[4pt]
\dfrac{2nT_0^2}{n(n-2)B},&r\ge r_A(n).
\end{cases}}
\]

This A-optimal support transition lies strictly between the previously obtained determinant-optimal and spectral-gap-optimal transitions on the *same* priced complete graph:
\[
\boxed{r_D=\frac{n-1}{n-2}<r_A=\frac n{n-2}<r_E=\frac{2(n-1)}{n-2}.}
\]
The A/D support-disagreement price interval has exact width \(r_A-r_D=1/(n-2)\), whereas the A/E interval has **constant width** \(r_E-r_A=1\) for every \(n\ge4\). The two outer thresholds are cited prior results; only the middle A-threshold, its complete optimizer, and the implied cross-criterion comparison are asserted here as new.

## Assumptions and scope

Let \(L(w)\) be the ordinary, unnormalized weighted graph Laplacian, with negative edge conductances off the diagonal and diagonal row sums. \(L(w)^\dagger\) is the Moore–Penrose pseudoinverse. The graph has all \(\binom n2\) candidate edges; zero allocation is allowed, but no connectivity constraint other than the infinite penalty for a disconnected design is needed. Budget prices and conductances are continuous, with no individual upper bounds or integrality restrictions. The budget is exhausted by any minimizer, because increasing one available conductance strictly lowers the objective on a connected support.

The primary research question is the optimal **sum** of effective resistances, not the maximum individual effective resistance, not the determinant of the grounded Laplacian, and not its smallest positive eigenvalue. The latter two criteria supply comparisons using independently established theorems.

## Proof

**1. Existence, strict convexity, and unrestricted symmetry.** The resource simplex is compact. Every feasible connected design has finite Kirchhoff index, while approach to a disconnected design makes its smallest positive Laplacian eigenvalue tend to zero, so a minimum exists and is connected. Set \(\Pi=I-\mathbf1\mathbf1^{\mathsf T}/n\) and \(A(w)=L(w)+\mathbf1\mathbf1^{\mathsf T}/n\). For connected \(w\),
\[
 \mathcal K(w)=n\bigl(\operatorname{tr}A(w)^{-1}-1\bigr).
\]
The second directional derivative along a nonzero edge-weight perturbation \(H=\delta L\) is
\[
 2n\operatorname{tr}\bigl(A^{-1}HA^{-1}HA^{-1}\bigr)>0.
\]
Indeed, the trace equals the positive trace of a nonzero squared symmetric operator conjugated by a positive definite matrix. Different edge allocations give different Laplacians because each off-diagonal entry determines its edge conductance; hence \(H\ne0\) for a nonzero perturbation. The objective is therefore strictly convex on the connected feasible domain. There is exactly one minimizer, and its invariance under exchanging vertices \(1,2\) and permuting vertices \(3,\ldots,n\) forces the three edge classes \(a,b,c\), even among fully asymmetric candidate allocations.

**2. Spectrum and resource constraint.** Write \(k=n-2\). The vector antisymmetric on vertices \(1,2\) has eigenvalue \(x=2a+kb\). The bipartition-constant contrast between the first two and the remaining \(k\) vertices has eigenvalue \(nb\). Every zero-sum vector supported on the remaining \(k\) vertices has eigenvalue \(z=2b+kc\), with multiplicity \(k-1\). Together with the constant zero eigenvalue, these span all \(n\) dimensions, giving exactly
\[
 \frac{\mathcal K}{n}=F(a,b,c)=\frac1{2a+kb}+\frac1{nb}+\frac{k-1}{2b+kc},
\quad ra+2kb+\frac{k(k-1)}2c=B.
\]

**3. Interior Karush–Kuhn–Tucker system.** With multiplier \(\lambda>0\) for the budget, the \(a\)- and \(c\)-stationarity equations are
\[
 \frac2{x^2}=\lambda r,\qquad \frac{k(k-1)}{z^2}=\lambda\frac{k(k-1)}2.
\]
Thus \(\lambda=2/z^2\) and \(z^2=r x^2\). Substitution into \(b\)-stationarity yields
\[
 \frac{x^2}{b^2}=n\left(\frac{2(k+1)}r-k\right)=h^2.
\]
Consequently \(x=h b\), \(z=\sqrt r\,h b\), and therefore \(a=(h-k)b/2\), \(c=(\sqrt r\,h-2)b/k\). The budget gives \(b=B/T\), as stated. The inequality \(h>k\) is equivalent to \(r<n/k\). Moreover
\[
 (\sqrt r\,h)^2=n\bigl(2(k+1)-kr\bigr)\ge nk>4
\]
throughout \(0<r\le n/k\), because \(k\ge2\). Thus \(c>0\) throughout the interior regime and at its endpoint. All nonnegativity and stationarity conditions hold, proving optimality by convexity and uniqueness by strict convexity.

**4. Deleted-edge regime.** At \(a=0\), take \(z=\Delta b\), where \(\Delta=\sqrt{nk}\). The stationarity equations for \(b,c>0\) imply this ratio and give \(b=B/T_0\), \(c=(\Delta-2)b/k\). Direct substitution into the remaining one-sided stationarity inequality gives
\[
 \left.\frac{\partial F}{\partial a}+\lambda r\right|_{a=0}
 =\frac{2}{k^2b^2}\left(\frac{rk}{n}-1\right)\ge0
 \quad\Longleftrightarrow\quad r\ge\frac nk.
\]
All KKT equations are therefore satisfied precisely on the claimed closed upper-price region. The solution is feasible and connected since \(b,c>0\) (indeed \(\Delta>2\)). It is the unique global optimizer. At equality \(r=n/k\), the interior expressions reduce to the same design.

**5. Minimum and three-criterion comparison.** The inverse-trace objective \(F\) is homogeneous of degree \(-1\) in the conductances. Euler's relation at the optimum, including the boundary solution, gives \(F=\lambda B=2B/z^2\). Substituting \(z=\sqrt r\,hB/T\) or \(z=\Delta B/T_0\) yields the exact minimum in the finding. The already established D- and E-optimal single-priced-edge threshold values are \((n-1)/(n-2)\) and \(2(n-1)/(n-2)\), respectively. Subtraction proves \(r_A-r_D=1/(n-2)\) and \(r_E-r_A=1\) without any asymptotic inference.

## Verification

The standalone `verify.py` is runnable with Python 3, NumPy, and SymPy. It constructs each full weighted Laplacian from all independently specified edge entries, independently checks its positive eigenvalues against the symmetry decomposition, and computes \(\operatorname{tr}(L+\mathbf1\mathbf1^{\mathsf T}/n)^{-1}-1\) directly. It also checks budget equalities, active and one-sided KKT equations, and nearby feasible perturbations over 810 parameter combinations, including prices immediately below and above the exact threshold. Additional tests perform exact rational matrix inversion and polynomial-spectrum comparisons for small complete graphs, and exact rational threshold ordering checks for 96 network orders. **All 908 test cases passed** when run from this package.

Finite verification is corroboration only. The proof of global uniqueness and the all-parameter threshold is the strict-convexity and exact KKT argument above. No numerical inference is used to establish an infinite assertion.

## Relationship to prior work

Ghosh, Boyd, and Saberi establish strict convexity, a general effective-resistance optimization framework, and analytic optima for equal-priced graphs including the complete graph, as well as wheel and barbell families. The full 2006 conference and 2008 journal versions were examined in their relevant methodological and example sections; neither gives the single-exceptional-price complete-graph optimizer, threshold, or three-criterion comparison. Their general first-order optimality conditions are used as foundational machinery, not claimed as new.

A previous complete-graph result titled *A sharp single-price deletion threshold for D-optimal complete-graph conductances* (2026) proves the determinant-optimal threshold \(r_D\) on the identical price class. *A single-pair versus multi-pair price threshold for spectral-gap design of complete graphs* (2026) proves \(r_E\) on that class. Their full results and proofs were inspected and compared by implication: neither theorem determines the sum-of-inverse-eigenvalues minimizer or its middle threshold. A previous resistance-optimization theorem for a *perfect matching* of expensive edges in \(K_{2m}\) is not a one-edge theorem: it has a different edge-price orbit and cannot be specialized to a single marked edge without changing the feasible problem.

A 2026 analysis of general power-law costs and Kirchhoff-index design proves relevant uniqueness and marginal-worth principles, including support deletion at linear price. The accessible full HTML was checked in the relevant theoretical, complete-graph, and examples sections; it does not provide this one-expensive-edge closed classification. The new contribution is not the general convexity or the existence of a support transition, but its exact universal \(n/(n-2)\) location, unique conductor formulas, and the constant-width A/E disagreement.

## Limitations

The theorem requires an otherwise complete graph, only one differently priced link, a linear budget, and a sum-of-all-pairs resistance objective. It does not extend without further analysis to multiple anomalous edges, spatial nonlinear costs, integer allocations, maximum pairwise resistance, or finite-gain consensus design. A targeted literature and results search can never prove absolute novelty; an unlocated, equivalently formulated historic result remains a publication-priority risk. The mathematical checks here are not an independent audit.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24–28, 2006, pp. 1185–1196. Early public version: https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, *SIAM Review* **50** (2008), 37–66; electronically published 2008-02-01, doi:10.1137/050645452. https://stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. *A sharp single-price deletion threshold for D-optimal complete-graph conductances*, published research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-single-price-deletion-threshold-for-d-optimal-complete-g--75c0841ce157
4. *A single-pair versus multi-pair price threshold for spectral-gap design of complete graphs*, published research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-single-pair-versus-multi-pair-price-threshold-for-spectral-gap--c0a7ce2499f8
5. *A sharp matching-price transition in resistance-optimized complete networks*, published research result (2026), on an entire perfect matching rather than one marked edge. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-sharp-matching-price-transition-in-resistance-optimized-comple--cf3b1355b128
6. H. Tovar et al., *Cost convexity controls the architecture of resistance-optimal networks*, arXiv:2610.03627, first posted 2026-10-02. https://arxiv.org/abs/2610.03627
