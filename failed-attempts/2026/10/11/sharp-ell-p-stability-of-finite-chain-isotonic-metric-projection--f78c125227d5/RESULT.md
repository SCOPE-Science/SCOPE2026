# Sharp \(\ell_p\) stability of finite-chain isotonic metric projections

## Finding

Let \(n\ge1\) be an integer and \(1<p<\infty\). The nearest-point map onto the increasing-sequence cone in real \(\ell_p^n\) has exact Lipschitz constant
\[
\boxed{\operatorname{Lip}(P_{p,n})=
\begin{cases}
1,&n\le2\text{ or }p=2,\\
n^{1/p},&n\ge3\text{ and }1<p<2,\\
(n/2)^{1/p},&n\ge3\text{ and }2<p<\infty.
\end{cases}}
\]
In particular, it is nonexpansive if and only if \(n\le2\) or \(p=2\). For every fixed \(n\ge3\), the optimal Lipschitz constant jumps at the Hilbert exponent, because non-Hilbert scalar block means assign exceptional derivative weight to residual coordinates that equal their fitted value.

## Assumptions and scope

Define \(C_n=\{y\in\mathbb R^n:y_1\le\cdots\le y_n\}\). For each \(x\in\mathbb R^n\), define the **unweighted** isotonic metric projection
\[
P_{p,n}(x)=\operatorname*{argmin}_{y\in C_n}\sum_{i=1}^{n}|x_i-y_i|^p.
\]
The minimizer exists and is unique because the feasible set is closed, the objective coercive, and the scalar power loss strictly convex. All norms below are the same real \(\ell_p\)-norm, and \(\operatorname{Lip}\) is the supremum over all distinct input pairs. The data domain has no boundedness or generic-position restrictions.

## Proof

**1. Scalar pooled means.** For a finite nonempty index block \(B\), set
\[
m_p(a_B)=\operatorname*{argmin}_{t\in\mathbb R}\sum_{i\in B}|a_i-t|^p,
\qquad \phi_p(u)=\operatorname{sgn}(u)|u|^{p-1}.
\]
The unique scalar mean satisfies \(\sum_{i\in B}\phi_p(a_i-m_p(a_B))=0\). It is monotone in each input coordinate and satisfies \(m_p(a_B+c\mathbf1)=m_p(a_B)+c\). Hence \(|m_p(a_B)-m_p(b_B)|\le\|a_B-b_B\|_\infty\). The repeated-block map \(a_B\mapsto m_p(a_B)\mathbf1_B\) is therefore \(|B|^{1/p}\)-Lipschitz in \(\ell_p\). For a two-element block its mean is the arithmetic midpoint for every \(p>1\), giving norm one.

**2. Sharper scalar estimate when \(p>2\).** Fix a nonconstant vector \(a_B\), put \(t=m_p(a_B)\), \(r_i=a_i-t\), \(w_i=|r_i|^{p-2}\), \(W=\sum_{i\in B}w_i>0\), and \(q=p/(p-1)\). Implicit differentiation at this point gives
\[
\frac{\partial m_p}{\partial a_i}=\frac{w_i}{W}.
\]
The balancing condition \(\sum_i\phi_p(r_i)=0\) implies \(|r_i|^{p-1}\le\sum_{j\ne i}|r_j|^{p-1}\). The function \(u\mapsto u^{(p-2)/(p-1)}\) is subadditive on nonnegative inputs. Consequently \(w_i\le\sum_{j\ne i}w_j\), so \(0\le w_i/W\le1/2\). Hölder duality gives
\[
\|\nabla m_p(a_B)\|_q^q
=\sum_i(w_i/W)^q
\le(1/2)^{q-1},
\qquad\|\nabla m_p(a_B)\|_q\le2^{-1/p}.
\]
This bound is valid on the complement of the scalar diagonal, where the implicit function theorem applies. On any straight segment, the scalar diagonal is encountered at most once unless the whole segment lies in it. Integrating on the remaining pieces and using continuity proves that \(m_p\) is globally \(2^{-1/p}\)-Lipschitz on every block of size at least two. A segment wholly in the diagonal satisfies the same bound because \(|B|\ge2\). Therefore the repeated-block map is \((|B|/2)^{1/p}\)-Lipschitz; one-element blocks have constant one.

**3. Pasting blocks.** Every maximal constant run of the unique isotonic minimizer is a consecutive block, and its value minimizes the unrestricted scalar pooled loss on that block. Indeed, neighboring fitted levels are strictly separated, so the common value in a maximal block can be varied slightly in either direction without breaking feasibility. Thus \(P_{p,n}\) is, at every input, equal to one of the finitely many maps indexed by consecutive block partitions, each obtained by taking independent scalar pooled means. By direct-sum geometry, a partition map has Lipschitz constant bounded by the largest of its constituent repeated-block constants.

For clarity, a continuous selection among finitely many maps with the same Lipschitz bound \(L\) is again \(L\)-Lipschitz on any segment. To see this, parameterize the segment at unit \(\ell_p\)-speed and compose with any norm-one dual functional. Subtracting \(L\) times this arc-length parameter from every scalar branch makes all branches nonincreasing. A continuous finite selection of nonincreasing scalar functions cannot cross any fixed horizontal level upwards: at a proposed upward crossing, a subsequence of a single selected branch would have to rise past its value at that crossing. Applying this fact also to the negative dual functional proves the norm estimate. Continuity of \(P_{p,n}\) follows directly from uniqueness and coercivity of its strictly convex minimization problem. We conclude that
\[
\operatorname{Lip}(P_{p,n})\le
\begin{cases}
1,&n\le2,\\
n^{1/p},&n\ge3,\ 1<p<2,\\
1,&p=2,\\
(n/2)^{1/p},&n\ge3,\ p>2.
\end{cases}
\]
For \(p=2\), every block mean is the arithmetic average and the standard Hilbert projection principle also yields the bound one.

**4. Sharpness below two.** Fix \(n\ge3\) and \(1<p<2\). Choose strictly decreasing observations with a unique zero in an interior coordinate and with scalar pooled mean zero. One explicit choice is
\[
a=(1,0,-c,-2c,\ldots,-(n-2)c),\qquad
c=\left(\sum_{j=1}^{n-2}j^{p-1}\right)^{-1/(p-1)}.
\]
The signed residual powers sum to zero; for every proper prefix their sum is strictly positive. The Karush--Kuhn--Tucker multipliers for the constraints \(y_i-y_{i+1}\le0\) are therefore strictly positive at the all-zero fit. By continuity of the multipliers, in a neighborhood of \(a\), every coordinate of \(P_{p,n}\) equals the common scalar mean.

Perturb only the second observation from zero to \(h>0\), and write \(t_h=m_p(a+h e_2)\). Monotonicity and translation equivariance give \(0\le t_h\le h\). Taylor expansion of the other, nonzero residual contributions gives
\[
(h-t_h)^{p-1}=A t_h+o(t_h),\qquad
A=(p-1)\sum_{i\ne2}|a_i|^{p-2}>0.
\]
Thus \(h-t_h=O(h^{1/(p-1)})=o(h)\), since \(p-1<1\). Consequently \(t_h/h\to1\), and
\[
\lim_{h\downarrow0}\frac{\|P_{p,n}(a+h e_2)-P_{p,n}(a)\|_p}{\|h e_2\|_p}
=n^{1/p}.
\]
This proves the sharp lower bound even though the supremum need not be attained by distinct inputs.

**5. Sharpness above two.** For \(n\ge3\) and \(p>2\), let \(a=(1,0,\ldots,0,-1)\). Again \(m_p(a)=0\); every proper prefix of \(\phi_p(a)\) sums to one, so all KKT multipliers for the full-pooling solution are positive. Full pooling remains optimal locally. The derivative of the scalar mean at \(a\) assigns weights \(1/2\) to the first and final coordinates and zero to the others. The local Jacobian of \(P_{p,n}\) is therefore
\[
v\longmapsto\tfrac12(v_1+v_n)\mathbf1_n,
\]
whose exact \(\ell_p\)-operator norm is \((n/2)^{1/p}\) by Hölder duality. This establishes the sharp upper bound. Finally, for \(n\le2\) or \(p=2\), every feasible input is fixed by its metric projection, forcing the global Lipschitz constant to be at least one. All cases follow.

## Verification

The complete argument uses exact scalar stationarity, strict complementary KKT multipliers, Hölder duality, and a finite-selection Lipschitz lemma. A standalone standard-library Python verifier, `verify_isotonic.py`, independently evaluates the scalar minimizers by bisection and an adjacent-pooling implementation. Executing `python verify_isotonic.py` reports `ISOTONIC_LP_SHARP_NORM_FINITE_CHECK_OK 615`; it checks representative exponents, dimensions, random input pairs, and near-sharp perturbations. These finite tests do **not** establish the theorem for arbitrary parameters or all input pairs; those are covered by the proof above.

## Relationship to prior work

Luss and Rosset (arXiv:1104.1779, originally public April 2011) develop generalized isotonic regression for separable convex differentiable objectives and the requisite block/KKT principles. Németh and Németh (arXiv:1503.08458) discuss order-preserving **Euclidean** projections onto isotonic cones. Kyng, Rao, and Sachdeva (arXiv:1507.00710) develop fast algorithms for \(\ell_p\)-isotonic regression on directed acyclic graphs. Their statements about computing an optimizer or preserving order do not provide the exact worst-case **input-to-output \(\ell_p\)-Lipschitz constant** here, including the two non-Hilbert sharp branches and the discontinuous Hilbert transition. The classical literature on best monotone \(L^p\) approximation remains a possible source of historical overlap, as noted below.

## Limitations

The theorem concerns finite **unweighted real chains**, strictly convex exponents \(1<p<\infty\), and the input/output \(\ell_p\)-metric. It makes no claim about weighted data, arbitrary partial orders, continuum function spaces, or the nonunique endpoint projections \(p=1,\infty\). Historical equivalences in some older monotone \(L^p\) approximation literature cannot be ruled out from accessible primary texts; in particular, the complete text of the 1990 Swetits--Weinstein article was unavailable for an implication-level comparison. No independent review has been performed.

## References

1. R. Luss and S. Rosset, *Generalized Isotonic Regression*, arXiv:1104.1779 (first posted 10 April 2011), https://arxiv.org/abs/1104.1779 .
2. A. B. Németh and S. Z. Németh, *Isotonic Regression and Isotonic Projection*, arXiv:1503.08458 (first posted 29 March 2015), https://arxiv.org/abs/1503.08458 .
3. R. Kyng, A. Rao, S. Sachdeva, *Fast, Provable Algorithms for Isotonic Regression in all* \(\ell_p\)*-norms*, arXiv:1507.00710 (first posted 2 July 2015), https://arxiv.org/abs/1507.00710 .
4. J. J. Swetits and S. E. Weinstein, *Construction of the Best Monotone Approximation on* \(L^p[0,1]\), Journal of Approximation Theory (1990), doi:10.1016/0021-9045(90)90028-O (full text not inspected).
