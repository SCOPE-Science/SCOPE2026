# A two-thirds-power law for resistance-optimal rung investment in prism networks

## Finding

**Theorem.** Fix an integer \(m\ge3\), a budget \(B>0\), and a rung price \(c>0\). On the prism graph \(C_m\square K_2\), assign arbitrary independent nonnegative edge conductances. A rail edge costs one unit of budget per unit conductance and a rung edge costs \(c\). Minimize the unscaled Kirchhoff index \(\mathcal K=\sum_{u<v}R_{uv}\), declaring disconnected choices to have infinite objective.

There is a **unique global optimizer**, and all \(2m\) rail edges have a common positive conductance \(a_m\), while all \(m\) rungs have a common positive conductance \(b_m\). Write

\[
\lambda_k=4\sin^2\!\left(\frac{\pi k}{m}\right),\quad
S_m=\frac{m^2-1}{12},\quad
T_m(r)=\sum_{k=0}^{m-1}\frac{1}{2r+\lambda_k}.
\]

The positive ratio \(r_m=b_m/a_m\) is the **unique positive root** of

\[
\boxed{\ cS_m+\sum_{k=0}^{m-1}\frac{c\lambda_k-4}{(2r+\lambda_k)^2}=0.\ }
\]

The optimal weights and objective are

\[
\boxed{\ a_m=\frac{B}{m(2+cr_m)},\qquad b_m=r_ma_m,\qquad
\mathcal K_{\min}=\frac{2m^2}{B}(2+cr_m)\bigl(S_m+T_m(r_m)\bigr).\ }
\]

For every fixed \(c>0\), as \(m\to\infty\), the rung-to-rail ratio and minimum satisfy the sharp limits

\[
\boxed{\ m^{2/3}r_m\longrightarrow \left(\frac{3\sqrt2}{c}\right)^{2/3},\qquad
\mathcal K_{\min}=\frac{m^4}{3B}+\frac{(18c)^{1/3}}{2B}m^{10/3}+o(m^{10/3}) .\ }
\]

In particular, although every rung must retain a positive conductance at every finite \(m\), its optimal conductance relative to a rail edge vanishes at the noninteger exponent \(2/3\).

## Assumptions and scope

The vertices are \((\ell,j)\) with \(\ell\in\{0,1\}\) and \(j\in\mathbb Z/m\mathbb Z\). Rail edges join \((\ell,j)\) to \((\ell,j+1)\) in each layer; rungs join \((0,j)\) to \((1,j)\). For \(m\ge3\) these are \(3m\) distinct edges. Each individual conductance is initially free to vary, including being zero; there is no symmetry assumption in the optimization. The budget is an inequality, saturated at the optimum. The Laplacian is the usual unnormalized symmetric conductance Laplacian, and effective resistances use conductances rather than resistances as edge variables. The asymptotic holds for fixed positive \(B\) and \(c\), not for varying rung prices.

## Proof

**1. Existence, strict convexity, and symmetry.** Restrict the graph Laplacian \(L\) to the mean-zero space \(\mathbf1^\perp\). For a connected design this restriction is positive definite, and

\[
\mathcal K=2m\operatorname{tr}_{\mathbf1^\perp}(L^{-1}).
\]

The conductance budget set is compact. Approaching a disconnected design drives a positive eigenvalue of this restriction to zero, hence drives \(\mathcal K\) to infinity; a minimizer therefore exists and is connected. Along a nonzero perturbation \(H\) of the restricted Laplacian, the second derivative of its inverse trace is

\[
2\operatorname{tr}(L^{-1}HL^{-1}HL^{-1})>0.
\]

Indeed, with \(Q=L^{-1/2}HL^{-1/2}\), the trace equals \(2\operatorname{tr}(Q^2L^{-1})\), which is positive for nonzero symmetric \(H\). Distinct edge weight vectors yield distinct Laplacians because the graph is simple and every edge has its own off-diagonal entry. Thus the objective is strictly convex on connected feasible weights, proving uniqueness. Increasing all positive weights decreases every resistance, so the full budget is used. Rotation of the two cycles and layer exchange preserve prices and act transitively on each of the two edge classes. Uniqueness therefore forces common rail weight \(a_m\) and common rung weight \(b_m\). Neither can vanish, since either all-zero edge class disconnects the prism. Hence \(a_m,b_m>0\), and \(m(2a_m+cb_m)=B\).

**2. Exact spectral reduction.** The cycle Laplacian has eigenvalues \(\lambda_k\) given above. Tensor decomposition across the two layers gives the \(2m\) prism eigenvalues

\[
a_m\lambda_k\quad\text{and}\quad a_m\lambda_k+2b_m\qquad(0\le k<m),
\]

with only the first eigenvalue for \(k=0\) omitted from the inverse trace. The classical cycle reciprocal-eigenvalue sum is

\[
\sum_{k=1}^{m-1}\lambda_k^{-1}=\frac{m^2-1}{12}=S_m.
\]

Putting \(r=b_m/a_m\) and eliminating the budget gives the exact objective

\[
\mathcal K(r)=\frac{2m^2}{B}F_m(r),\quad
F_m(r)=(2+cr)(S_m+T_m(r)),\qquad r>0.
\]

Direct differentiation yields

\[
F_m'(r)=cS_m+\sum_{k=0}^{m-1}\frac{c\lambda_k-4}{(2r+\lambda_k)^2}.
\]

As \(r\downarrow0\), the \(k=0\) summand is \(-1/r^2\), while the others stay bounded, so \(F_m'(r)\to-\infty\). As \(r\to\infty\), the sum vanishes and \(F_m'(r)\to cS_m>0\). The budget parameter \(b\in(0,B/(mc))\) relates to \(r\) by a strictly increasing bijection \(b=Br/[m(2+cr)]\). The original objective is strictly convex as a function of this affine budget parameter \(b\). Therefore its derivative crosses zero precisely once. Since the derivative with respect to \(r\) has the same sign, the displayed equation has exactly one positive root, which determines the unique global optimum.

**3. Explicit finite-size resolvent.** Set

\[
q(r)=1+r-\sqrt{r(r+2)}\in(0,1).
\]

The Fourier expansion of the Poisson kernel, sampled at the \(m\)-th roots of unity, gives the exact identity

\[
\boxed{\ T_m(r)=\frac{m}{2\sqrt{r(r+2)}}\frac{1+q(r)^m}{1-q(r)^m}.\ }
\]

For completeness, \(q+q^{-1}=2(1+r)\) and the Fourier coefficient of \([2(1+r-\cos\theta)]^{-1}\) at frequency \(j\) is \(q^{|j|}/[2\sqrt{r(r+2)}]\). Summing over the equally spaced frequencies retains exactly multiples of \(m\), producing the displayed geometric series. This formula is also an efficient scalar evaluator of the optimizer equation.

**4. Sharp asymptotic.** Fix \(c>0\). For a trial ratio \(r=m^{-2/3}\), the resolvent formula gives

\[
F_m(m^{-2/3})=\frac{m^2}{6}+O(m^{4/3}).
\]

Since \(F_m(r)\ge 2S_m+cS_mr+2T_m(r)\), optimality implies both \(r_m=O(m^{-2/3})\) and \(T_m(r_m)=O(m^{4/3})\). The exact resolvent also gives \(T_m(r)\ge m/[2\sqrt{r(r+2)}]\); hence \(r_m=\Omega(m^{-2/3})\). Consequently \(\xi_m=m^{2/3}r_m\) remains in a fixed compact subset of \((0,\infty)\). Uniformly on such compact sets, \(q(\xi m^{-2/3})^m\to0\) exponentially in \(m^{2/3}\), and the same resolvent identity yields

\[
F_m(\xi m^{-2/3})=\frac{m^2}{6}+m^{4/3}\left(\frac{c\xi}{12}+\frac{1}{\sqrt{2\xi}}\right)+o(m^{4/3}).
\]

The bracketed function is strictly convex and has its unique minimizer at \(\xi_*=(3\sqrt2/c)^{2/3}\). Compactness plus uniform convergence forces \(\xi_m\to\xi_*\). At this minimizer the bracket equals \((18c)^{1/3}/4\). Multiplying by \(2m^2/B\) establishes both asymptotic claims. The proof also shows the rung share of the budget is asymptotic to \((c\xi_*/2)m^{-2/3}\).

## Verification

The standalone `verify.py` uses standard-library exact rational matrix inversion to compare the \(2m\)-vertex Kirchhoff index directly with the spectral formula for several cycle sizes and positive rational weight pairs. It also checks the exact resolvent matrix identity, the closed-form scalar sum, the first-order root signs, and the asymptotic ratio at large finite sizes. Run `python3 verify.py` in a directory containing the extracted files. The expected output is `VERIFY_OK 119`. These finite checks are reproducibility checks, not an exhaustive proof over all \(m,c,B\). The infinite-domain theorem follows from the four analytic steps above.

## Relationship to prior work

Zhang and Yang (2006) derived Kirchhoff-index and resistance formulas for circulant graphs, including cycles; the cycle reciprocal-spectral sum is used here without novelty claim. Ghosh, Boyd and Saberi (2008, with a 2006 conference version) established strict convex resistance-design optimization and general optimality methods and treated several graph families, but the examined graph examples do not supply a priced-prism allocation or the \(m^{-2/3}\) rung law. Carmona, Encinas and Mitjana (2014) derive weighted resistance formulas for linear ladder-like chains, a distinct path-based family, without the present circular-prism budget optimizer. Cinkir (2017) gives the unweighted prism Kirchhoff-index formula; in the special case \(a=b=1\), the spectral expression here reproduces that known value. These established ingredients and special cases are not presented as new results. The new assertion is the **globally unrestricted two-price optimization and sharp fractional-power scaling**.

## Limitations

The asymptotic assumes a fixed positive cost ratio and does not cover double scalings where \(c\) depends on \(m\), arbitrary nonuniform edge prices, or non-prism ladders. The optimizer is specified by a uniquely solvable scalar equation, not by radicals for general \(m\). Literature priority is assessed from located materials and remains subject to possible unindexed equivalent results; a missing match is not a theorem of novelty. The proof has not received independent mathematical validation.

## References

1. H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107 (2007), 330–339; first online September 5, 2006. https://doi.org/10.1002/qua.21068
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66. https://doi.org/10.1137/050645452 ; author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. A. Carmona, A. M. Encinas, and M. Mitjana, *Effective resistances for ladder-like chains*, International Journal of Quantum Chemistry 114 (2014), 1670–1677. https://doi.org/10.1002/qua.24740 ; lawful manuscript: https://upcommons.upc.edu/server/api/core/bitstreams/303b177e-4325-4803-8cf5-491df6737da2/content
4. Z. Cinkir, *Effective Resistances and Kirchhoff Index of Prism Graphs* (2017), arXiv:1704.03429. https://arxiv.org/abs/1704.03429
