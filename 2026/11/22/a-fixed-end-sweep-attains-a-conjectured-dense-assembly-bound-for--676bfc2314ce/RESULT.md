# A fixed-end sweep attains a conjectured dense assembly bound for persistent up-Laplacians

## Finding

For a finite filtration of simplicial complexes and each fixed dimension \(q\geq0\), let \(m\geq1\) and \(n\geq1\) be the respective numbers of \((q+1)\)- and \(q\)-simplices in its final complex. A **fixed-end sweep** of reduced persistence columns constructs exactly the matrix of every persistent up-Laplacian at every pair at which its persistent chain space acquires a generator. It performs, including reduction and complete dense matrix assembly but excluding eigendecompositions, at most

\[
O\!\left(m\sum_{t\in\mathcal T}k_t^2+(nm+n^2)\sum_{t\in\mathcal T}k_t\right)
\]

arithmetic operations, where \(\mathcal T\) is the set of birth times of \((q+1)\)-simplices and \(k_t\) is the number of such simplices born by time \(t\). Consequently the cost is

\[
O\!\left(m^4+nm^3+n^2m^2\right).
\]

This is an *existentially specified evaluation order and algorithmic bound* for a fixed-end, row-by-row sweep. It does **not** prove a worst-case bound for every evaluation order, scheduling heuristic, or numerical implementation of the algorithm discussed in [1], and it does not improve on every Schur-complement method.

## Assumptions and scope

Work in exact real arithmetic with a finite filtration \(K_0\subseteq K_1\subseteq\cdots\subseteq K_T\), possibly with several simplices added at the same time. Orient simplices consistently, and order the \(q\)- and \((q+1)\)-simplices nondecreasingly by first appearance. Endow chain spaces with their standard Euclidean simplex-basis inner products. Let \(B\) be the final \(n\times m\) boundary matrix and use zero-based filtration indices, with \(0\le s\le t\le T\). For this result, a relevant pair means a pair \((s_j,t_j)\) defined below; multiple columns may share a pair.

The persistent chain space and persistent up-Laplacian are

\[
C_{q+1}^{s,t}=\{c\in C_{q+1}(K_t):Bc\in C_q(K_s)\},\qquad
\Delta_{q,+}^{s,t}=B_{s,t}\,B_{s,t}^{*},
\]

where \(B_{s,t}\) is the restriction of \(B\) to the domain \(C_{q+1}^{s,t}\), mapped into \(C_q(K_s)\) with its induced inner product. The full \(q\)-Laplacian also has a down term, which is not included in the displayed cost.

Apply ordinary left-to-right persistence column reduction, retaining its basis-change matrix \(V\), to obtain \(R=BV\), where \(V\) is invertible upper triangular and nonzero columns of \(R\) have distinct lowest nonzero rows. For each column \(j\), set \(t_j\) equal to the birth time of the corresponding \((q+1)\)-simplex and set \(s_j\) equal to the birth time of the lowest nonzero \(q\)-simplex row of \(R_j\), or \(0\) if \(R_j=0\). By filtration compatibility, \(s_j\le t_j\).

## Proof

**1. The reduced columns give a two-parameter basis.** At \(t\), retain only columns born by \(t\). The leading block \(V^t\) is invertible, and its columns have zero coordinates on later simplices. To impose the boundary condition at \(s\), delete the rows of \(B\) corresponding to \(q\)-simplices born no later than \(s\). Under column reduction the remaining matrix is the corresponding row deletion of \(R\). A nonzero reduced column has its lowest nonzero row strictly after \(s\) exactly when \(s_j>s\). Such remaining nonzero columns are independent, because their lowest rows are distinct. Thus the columns of \(V\) with \(t_j\le t\) and \(s_j\le s\) are a basis of the kernel of the truncated boundary, namely \(C_{q+1}^{s,t}\). This is the persistence-reduction basis property of [1, Section 4.1].

**2. Fixed-end sweep and exact matrix update.** For each distinct \(t\in\mathcal T\), start a fresh empty orthogonal list \(Q_t\) in \(\mathbb R^m\) and a zero \(n\times n\) matrix \(L_t\). Visit the distinct \(s_j\) of all columns with \(t_j\le t\), in nondecreasing order. At event \(s\), orthogonalize every as-yet-uninserted \(V_j\) with \(s_j=s\), \(t_j\le t\), against all earlier orthogonal vectors in this same row using their squared norms. For each nonzero remainder \(w\), retain it without normalization and update

\[
L_t\ \longleftarrow\ L_t+\frac{(Bw)(Bw)^T}{w^Tw}.
\]

The remainder is nonzero because the eligible \(V_j\) are independent. Its boundary lies in \(C_q(K_s)\): both the new original vector and every previous orthogonal vector in this \(t\)-row lie in \(C_{q+1}^{s,t}\), and that space is linear. By Step 1, the list after an event is an orthogonal basis of \(C_{q+1}^{s,t}\). Hence \(L_t=BQ_t(Q_t^TQ_t)^{-1}Q_t^TB^T\); after restricting to the \(q\)-simplices in \(K_s\), it is exactly the matrix of \(\Delta_{q,+}^{s,t}\). Its other rows and columns are zero because \(B Q_t\subseteq C_q(K_s)\).

Every relevant pair \((s_j,t_j)\) occurs as an event of the \(t=t_j\) sweep. At any other pair \((s,t)\), the same eligible columns occur as at the most recent event at the largest \(t'\in\mathcal T\) with \(t'\le t\), and with the largest eligible \(s'\le s\) in that row. Thus its up-Laplacian is the corresponding principal block (with newly born zero rows and columns), or zero when no column is eligible. This does not require rebuilding an orthogonal basis for off-grid locations.

**3. Amortized arithmetic bound.** Fix \(t\). Exactly \(k_t\) columns are inserted, each into an orthogonal list of length at most \(k_t-1\). The scalar products, residual updates and squared-norm divisions cost \(O(mk_t^2)\) field operations in this row. The map \(w\mapsto Bw\) costs \(O(nm)\) and the dense rank-one outer-product update costs \(O(n^2)\) per inserted vector. There are therefore \(O(mk_t^2+(nm+n^2)k_t)\) operations per \(t\). Column reduction, including updates to the basis-change matrix \(V\), costs \(O((n+m)m^2)\). Since the final end-time row has \(k_t=m\), this preliminary cost is absorbed by the displayed sum. Sorting or bucketing the event times is likewise absorbed. The working matrices require \(O(m^2+nm+n^2)\) storage, excluding the optionally retained output matrices.

Finally, \(|\mathcal T|\le m\), \(k_t\le m\), so \(\sum_{t\in\mathcal T}k_t^2\le m^3\) and \(\sum_{t\in\mathcal T}k_t\le m^2\). Substitution yields the asserted quartic-dominant dense arithmetic bound. At the opposite extreme, if all \(m\) higher-dimensional simplices arrive at one end level, the same sum gives the strictly smaller bound \(O(m^3+nm^2+n^2m)\). No sparsity, generic-position, distinct-birth, or fixed-dimension-of-the-chain-space assumption is needed. \(\square\)

## Verification

The accompanying standalone `checker.py`, run using `sympy==1.14.0`, generates 120 seeded random genuine face-closed filtrations (at most six vertices), including tied birth levels and both dimensions \(q=0,1\). It verifies 969 fixed-end event matrices **exactly over the rationals** against an independently formed kernel and orthogonal projection. It additionally checks all available filtration index pairs, including pairs not on the event grid, against this direct calculation. The recorded output was:

```
PASS exact rational: seed 718 sampled filtrations 120 checks {0: 731, 1: 238} cases {0: 120, 1: 73}
```

This is finite corroboration only; the all-filtration claim is established by the preceding linear-algebra argument.

## Relationship to prior work

Kirchner and Vittorietti [1, Sections 4.1–4.2] already prove the persistence-reduced-column basis property, identify relevant pairs, and explain Gram–Schmidt and rank-one reuse. Their Section 6 proposes the same worst-case polynomial order without proving it for their whole implementation. The present contribution is the **specified fixed-end sweep schedule and its amortized, instance-sensitive proof**, not those foundational steps and not proof of the bound for unrestricted evaluation orders. The suggested complexity order is therefore not asserted to be new as a conjectural numerical expression.

Mémoli, Wan and Wang [2, Appendix E] earlier provide an all-pairs iterative Schur-complement approach with different parameters and update operations, which may be faster on some inputs; the claim does not subsume it. PETLS [3] is another existing approach to persistent Laplacian calculation. Neither a new general all-pairs method nor a universal speed advantage is claimed.

## Limitations

The bound is an exact-arithmetic operation count, not a bit-complexity or floating-point stability bound. It assumes storage or generation of persistence-reduction columns; it excludes spectral eigendecompositions, the down-Laplacian and the cost of retaining separate matrices for all off-grid filtration pairs. It is for a row-wise schedule explicitly specified above, not every possible reuse schedule. Prior work supplies most of the linear-algebra framework, and equivalently scheduled algorithms or amortization arguments may have appeared in unindexed literature. No independent mathematical audit has been performed.

## References

[1] J. Kirchner and M. Vittorietti, *New persistent chain spaces: identifying and computing the relevant persistent Laplacians of a filtration*, arXiv:2611.09610v1 (first public 2026-11-06), Sections 4 and 6, https://arxiv.org/html/2611.09610v1.

[2] F. Mémoli, Z. Wan and Y. Wang, *Persistent Laplacians: Properties, Algorithms and Implications*, arXiv:2012.02808 (first public 2020-12-04), Appendix E, https://arxiv.org/abs/2012.02808.

[3] B. Jones and G.-W. Wei, *PETLS: PErsistent Topological Laplacian Software*, arXiv:2508.11560 (first public 2025-08-15), https://arxiv.org/abs/2508.11560.
