# Exact Kemeny-optimal symmetric walks on complete split graphs

## Finding

**Theorem (complete split-graph stochastic design).** Let \(p,q\ge 2\) be integers. Form the simple complete split graph \(G_{p,q}=K_p\vee\overline{K_q}\): a clique \(C\) of \(p\) vertices, an independent set \(I\) of \(q\) vertices, every cross edge, and no edges within \(I\). Among **all** irreducible symmetric, nonnegative row-stochastic matrices \(P\) whose positive off-diagonal entries are supported on \(G_{p,q}\) (zero edge probabilities and self-loops are allowed), there is a **unique** minimizer of the zero-diagonal first-passage convention for Kemeny's constant

\[
\mathcal K(P)=\sum_{\lambda\in\sigma(P)\setminus\{1\}}\frac{1}{1-\lambda}=\operatorname{tr}\big((I-P)^+\big).
\]

Writing \(b\) for the common transition probability on a cross edge and \(c\) for the common probability on an edge within \(C\), the unique minimizer is

\[
\boxed{b_*=\frac{1}{\max\{p,q\}},\qquad c_*=\frac{(p-q)_+}{p(p-1)}.}
\]

All clique-vertex holding probabilities are zero. Each independent-set vertex holds with probability \((q-p)_+/q\). Thus every clique edge is used if \(p>q\), while **every** clique edge is discarded if \(q\ge p\), including the critical equality case. The minimum equals

\[
\boxed{\mathcal K_*=
\begin{cases}
q-1+\dfrac{p(p-1)^2}{p^2-q}+\dfrac{p}{p+q},&p>q,\\[4pt]
\dfrac{q(q-1)}p+(p-1)+\dfrac{q}{p+q},&q\ge p.
\end{cases}}
\]

There is also a sharp penalty for forbidding every clique edge. Let \(\mathcal K_{\mathrm{cross}}\) be the best Kemeny constant when only cross edges and holding probabilities are permitted. Then

\[
\boxed{\mathcal K_{\mathrm{cross}}-\mathcal K_*=
\begin{cases}
\dfrac{p^2(p-1)(p-q)}{q(p^2-q)},&p>q,\\[4pt]
0,&q\ge p.
\end{cases}}
\]

In particular, for each fixed \(q\ge2\), \(\mathcal K_{\mathrm{cross}}/\mathcal K_*\sim p/q\) as \(p\to\infty\). The support threshold is therefore accompanied by an arbitrarily large multiplicative benefit from retaining clique edges on the other side of the threshold.

## Assumptions and scope

A symmetric stochastic matrix has \(P=P^{\mathsf T}\), \(P\mathbf1=\mathbf1\), and every entry nonnegative. Its off-diagonal entry is zero on every graph nonedge. Entries on graph edges may vanish. Irreducibility is required to make the stationary-target hitting-time criterion finite; it is equivalent here to connectivity of the positive-edge support. For an irreducible symmetric stochastic matrix, the stationary law is uniform. The nonzero eigenvalues of \(L=I-P\) are positive, even if the chain is periodic. We use the convention \(H_{ii}=0\) in Kemeny's definition; adding a return-time convention changes all candidate constants by the same additive one and does not change minimizers.

No external edge-conductance budget, fixed holding probability, or separate positivity lower bound is imposed. The graph has \(p+q\) labeled vertices. The assertion of uniqueness concerns the full feasible matrix, not just designs invariant under graph automorphisms.

## Proof

**1. Strict global convexity and symmetry.** Associate to each permitted edge \(e=\{u,v\}\) the vector \(a_e=e_u-e_v\) and weight \(w_e=P_{uv}\). Then \(L=\sum_e w_e a_ea_e^{\mathsf T}\). On the subspace \(\mathbf1^\perp\), \(L\) is positive definite exactly when the positive-weight graph is connected. The objective is \(\operatorname{tr}(L^{-1}|_{\mathbf1^\perp})\), where the inverse is only on this subspace. Along a nonconstant affine direction \(H\) in Laplacian space its second derivative is

\[
2\operatorname{tr}(L^{-1}HL^{-1}HL^{-1})>0.
\]

Indeed, after conjugation by \(L^{-1/2}\), the integrand is a positive quadratic form in the nonzero symmetric matrix \(L^{-1/2}HL^{-1/2}\). Different edge weights produce different Laplacians because their negative off-diagonal entries recover the weights. Thus the objective is strictly convex on connected designs. It tends to infinity if a feasible sequence approaches disconnection, and a positive-edge feasible design exists; compactness then gives a unique minimizer. Permuting vertices within either class preserves feasibility and the objective. Averaging an optimizer under these permutations cannot change its unique value and therefore the minimizer has common cross probability \(b\) and common clique-edge probability \(c\).

**2. Exact spectrum.** A clique-contrast vector (zero sum on \(C\), zero on \(I\)) is an \(L\)-eigenvector of eigenvalue \(qb+pc\), with multiplicity \(p-1\). An independent-set contrast has eigenvalue \(pb\), with multiplicity \(q-1\). The class-constant nonuniform vector has eigenvalue \((p+q)b\), with multiplicity one; the all-ones vector has eigenvalue zero. Consequently

\[
\mathcal K(b,c)=\frac{q-1}{pb}+\frac{p-1}{qb+pc}+\frac1{(p+q)b},
\]

under the exact constraints \(b>0\), \(c\ge0\), \(pb\le1\), and \(qb+(p-1)c\le1\). Each constraint is precisely a nonnegative holding-probability requirement.

**3. Saturation of the clique stochasticity constraint.** For any fixed feasible \(b>0\), the objective strictly decreases as \(c\) increases. Hence \(c=(1-qb)/(p-1)\). Setting

\[
A=\frac{q-1}{p}+\frac1{p+q}>0,
\qquad 0<b\le b_{\max}=\frac1{\max\{p,q\}},
\]

gives the strictly convex scalar objective

\[
F(b)=\frac A b+\frac{(p-1)^2}{p-qb},\qquad
F'(b)=-\frac{A}{b^2}+\frac{q(p-1)^2}{(p-qb)^2},
\]

and \(F''(b)=2A/b^3+2q^2(p-1)^2/(p-qb)^3>0\).

**4. The upper endpoint is always optimal.** If \(q\ge p\), then \(b_{\max}=1/q\) and

\[
F'(b_{\max})=q(1-qA)<0,
\]

because \(qA=q(q-1)/p+q/(p+q)>1\). If \(p>q\ge2\), then \(b_{\max}=1/p\) and

\[
F'(b_{\max})=-Ap^2+\frac{qp^2(p-1)^2}{(p^2-q)^2}<0.
\]

For the last inequality, \(p^2-q>p(p-1)\), so the positive term is strictly less than \(q\), while \(Ap^2>p(q-1)\ge q\) for integers \(p>q\ge2\). Since \(F'\) is strictly increasing, its negative value at the upper endpoint forces \(F'(b)<0\) throughout the feasible interval. Therefore \(b=b_{\max}\) is the unique minimizer, and substitution gives the asserted \(c_*\), holding probabilities, and piecewise minimum.

**5. Exact cost of deleting clique links.** Under the additional restriction \(c=0\), \(\mathcal K(b,0)=A_0/b\), with \(A_0=(q-1)/p+(p-1)/q+1/(p+q)>0\). It is strictly decreasing, so its unique minimizer is again \(b_{\max}\). Subtracting the unrestricted minimum gives the displayed nonnegative gap, strictly positive precisely when \(p>q\). At fixed \(q\) and \(p\to\infty\), the restricted cost is \(p^2/q+O_q(p)\), whereas \(\mathcal K_*=p+O_q(1)\), proving the ratio asymptotic. All claimed equality cases have now been exhausted.

## Verification

The standalone Python 3 program `verify_split.py` uses only the standard library and executes 168,156 exact-rational assertions. It compares closed-form optimal values with independently inverted \((I-P+J/(p+q))\) matrices, checks nonoptimal feasible rational designs, tests the precise restricted-support loss formula, and checks the derivative endpoint certificate over thousands of size pairs. The file runs with `python3 verify_split.py` and reports the number of completed checks. These finite checks are independent corroboration; the strict all-size claims follow from the preceding proof, not the checker.

For a concrete noncritical example, \((p,q)=(4,2)\) has \(b_*=1/4\) and \(c_*=1/6\); removing all clique links incurs the exact additive penalty \(24/7\). At \((p,q)=(2,3)\), instead, \(b_*=1/3\) and \(c_*=0\); every clique edge is optimally unused.

## Relationship to prior work

Boyd–Diaconis–Parrilo–Xiao (arXiv:0709.0955; first arXiv public posting 2007-09-06) develop symmetry reduction for the **second-largest eigenvalue modulus** of symmetric stochastic walks, not their Kemeny trace. Ghosh–Boyd–Saberi (SIAM Review, 2008) study total effective resistance under a **single global sum-of-conductances budget**, rather than the vertexwise row-stochastic constraints here. Kirkland (2010) treats minimum Kemeny value on **directed**, not necessarily symmetric, subordinate chains. General reversible-chain Kemeny optimization and stochastic completion formulations are also available. Those methodologies motivate the problem and do not directly supply the present all-size, full-feasible-set optimizer or its edge-deletion penalty. An indexed complete-split fastest-mixing classification has related edge-support thresholds but a different objective.

## Limitations

The theorem concerns symmetric, uniform-stationary chains. It does not extend as stated to nonreversible chains, a prescribed nonuniform stationary measure, edge prices, mandatory positive clique edges, or optimizing SLEM rather than Kemeny's constant. Aperiodicity is not imposed; the balanced case can be periodic, though its Kemeny constant is finite. The closed-form result has not undergone independent mathematical audit. Literature-index coverage cannot establish publication priority, and inaccessible specialized manuscripts may contain equivalent results.

## References

1. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955, first posted 2007-09-06. https://arxiv.org/abs/0709.0955
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing effective resistance of a graph*, SIAM Review **50** (2008), 37–66. https://doi.org/10.1137/050645452 ; author-hosted full text https://stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. S. Kirkland, *Fastest expected time to mixing for a Markov chain on a directed graph*, Linear Algebra and Its Applications **433** (2010), 1988–1996. https://doi.org/10.1016/j.laa.2010.07.016 ; author-hosted text https://www.hamilton.ie/skirkland/min_kemeny_final.pdf
4. *Completion problems and sparsity for Kemeny's constant*, Canadian Mathematical Bulletin **68** (2025), 1–18. https://doi.org/10.4153/S0008439524000419
5. F. Durastante, M. Gnazzo, and B. Meini, *Kemeny's constant minimization for reversible Markov chains via structure-preserving perturbations*, BIT Numerical Mathematics **66** (2026), article 59. https://doi.org/10.1007/s10543-026-01152-6
