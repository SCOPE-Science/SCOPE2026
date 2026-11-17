# Sine-edge weights uniquely minimize the two-input variation instability of finite sorting

## Finding
Let \(n\ge 2\), and let \(S:\mathbb R^n\to\mathbb R^n\) arrange coordinates in nondecreasing order. For arbitrary strictly positive path-edge weights \(w=(w_1,\ldots,w_{n-1})\), define
\[
 V_w(h)=\sum_{j=1}^{n-1}w_j|h_{j+1}-h_j|,
 \qquad L_n(w)=\sup_{V_w(x-y)>0}\frac{V_w(Sx-Sy)}{V_w(x-y)}.
\]
For each \(1\le k<n\), put
\[
 B_k(w)=\max_{\substack{A\subseteq\{1,\ldots,n\}\\|A|=k}}
 \sum_{j=1}^{n-1}w_j|\mathbf1_A(j+1)-\mathbf1_A(j)|.
\]
The exact, attained two-input sensitivity for every choice of positive weights is
\[
 \boxed{L_n(w)=\max_{1\le k<n}\frac{B_k(w)}{w_k}.}
\]
Its optimum over *all* positive edge weights, without any normalization or reflection constraint, is
\[
 \boxed{\min_{w_j>0}L_n(w)=\Lambda_n=
 \begin{cases}
 \cot\bigl(\pi/(2n)\bigr),&n\text{ even},\\
 \csc\bigl(\pi/(2n)\bigr),&n\text{ odd}.
 \end{cases}}
\]
**Every minimizing weight vector is a positive multiple of**
\[
 \boxed{w_j^*=\sin\bigl(j\pi/n\bigr),\quad 1\le j<n.}
\]
At this optimum, every single-jump input direction is extremal in an appropriate strict sorting chamber: \(B_k(w^*)=\Lambda_n w_k^*\) for all \(k\). In particular, the optimal factors at four and five sites are \(1+\sqrt 2\) and \(1+\sqrt 5\), versus uniform-weight factors \(3\) and \(4\). Moreover \(\Lambda_n\sim 2n/\pi\), whereas the sharp uniform-weight factor is \(n-1\). For every \(n\ge 4\), optimal nonuniform weights strictly improve the stability of sorting under differences.

## Assumptions and scope
Signals are arbitrary real \(n\)-vectors. Sorting assigns their values to vertices in increasing order; ties cause no ambiguity in the sorted vector. The same strictly positive weights measure adjacent variation before and after sorting. Because both sorting and \(V_w\) respect additive constants, the quotient is defined on vectors modulo constants. The Lipschitz factor involves **two independently chosen inputs**, not the variation of a single sorted vector. Only the finite, ordinary path graph is considered. The case \(n=2\) is included.

## Proof
**1. Exact chamber and single-step reduction.** On every chamber in which all input coordinates are strictly ordered, sorting agrees with a permutation matrix \(P\). For a continuous piecewise-linear map with finitely many such chambers, the global seminorm Lipschitz factor equals the maximum induced seminorm of the chamber matrices: segment subdivision gives the upper bound, and a small perturbation inside a strict chamber gives the reverse bound. Degenerate segments follow by continuity. Every coordinate permutation occurs as some strict sorting chamber.

For \(1\le k<n\), let \(H_k\) be zero on coordinates \(1,\ldots,k\) and one on coordinates \(k+1,\ldots,n\). The exact decomposition
\[
 h=h_1\mathbf1+\sum_{k=1}^{n-1}(h_{k+1}-h_k)H_k
\]
and \(P\mathbf1=\mathbf1\) show
\[
 \|P\|_{V_w\to V_w}=\max_{1\le k<n}\frac{V_w(PH_k)}{w_k}.
\]
For a given \(k\), permuting the coordinates of \(H_k\) generates every zero-one word having \(k\) zeros and \(n-k\) ones. Taking complements does not change its weighted boundary. Thus the largest possible \(V_w(PH_k)\), over all \(P\), is exactly \(B_k(w)\). This proves the first formula. Every maximizing permutation and step direction are realized by a sufficiently small nonzero difference of inputs inside that permutation's strict chamber; sharpness does not rely on a limit at a tie.

**2. A universal cut-count bound and its sine-weight equality case.** Any zero-one word containing \(q=\min(k,n-k)\) entries in the minority color has at most \(2q\) color changes and at most \(n-1\) changes. Hence its weighted boundary cannot exceed the sum of the \(\min(2q,n-1)\) largest edge weights.

Put \(\theta=\pi/n\) and \(v_j=\sin(j\theta)\). The positive sequence \(v_1,\ldots,v_{n-1}\) is reflection symmetric and grows toward its center. For \(n=2m+1\) odd and \(q\le m\), the \(2q\) largest entries are the central block with edge indices \(m-q+1,\ldots,m+q\). Label the vertices inside its \(2q+1\)-vertex block alternately and label all outside vertices in the majority color. Exactly \(q\) minority vertices and exactly those \(2q\) boundary edges result. Therefore
\[
 B_k(v)=\sum_{j=m-q+1}^{m+q}\sin(j\theta)
 =\frac{\sin(q\theta)}{\sin(\theta/2)}
 =\csc(\theta/2)\sin(k\theta).
\]
The finite sine sum follows from pairing \(j\) with \(n-j\), or summing a geometric progression. For \(n=2m\) even and \(q<m\), either central block of \(2q\) edges, with indices \(m-q,\ldots,m+q-1\) or \(m-q+1,\ldots,m+q\), is a set of the \(2q\) largest weights. The same alternating-block construction attains either, and a finite sine sum gives
\[
 B_k(v)=\sin(q\theta)\cot(\theta/2)
 =\cot(\theta/2)\sin(k\theta).
\]
When \(q=m\) in the even case, the full alternating word changes on all \(n-1\) edges and
\[
 B_m(v)=\sum_{j=1}^{n-1}\sin(j\theta)=\cot(\theta/2)
 =\cot(\theta/2)\,v_m.
\]
Consequently \(B_k(v)=\Lambda_n v_k\) in *every* coordinate, and \(L_n(v)=\Lambda_n\).

**3. Perron lower bound for arbitrary weights.** Define a fixed \((n-1)\times(n-1)\) nonnegative matrix \(A\), with row \(k\) depending on \(q=\min(k,n-k)\). If \(n=2m+1\), the row equals the indicator of the central edge set \(\{m-q+1,\ldots,m+q\}\). If \(n=2m\) and \(q<m\), the row is the average of the indicators of the two central edge sets \(\{m-q,\ldots,m+q-1\}\) and \(\{m-q+1,\ldots,m+q\}\); if \(q=m\), the row is all ones. Each constituent indicator is the boundary of an actual zero-one word having exactly \(k\) entries of one color, so
\[
 (Aw)_k\le B_k(w)\le L_n(w)w_k
 \qquad (1\le k<n)
\]
for *every* positive weight vector \(w\).

Every row of \(A\) has a positive entry in the central column (choose column \(m\)); a central row has all entries positive. Hence \(A\) is irreducible. By the central-block sine identities proved in Step 2,
\[
 Av=\Lambda_n v,\qquad v>0.
\]
The Perron–Frobenius theorem thus identifies \(\Lambda_n\) as the simple spectral radius of \(A\). Let \(u>0\) be the corresponding left eigenvector. Multiplying \(Aw\le L_n(w)w\) by \(u^T\) yields \(\Lambda_n u^Tw\le L_n(w)u^Tw\); therefore \(L_n(w)\ge\Lambda_n\). In case of equality, \(Aw\le\Lambda_n w\) and strict positivity of \(u\) force componentwise equality \(Aw=\Lambda_n w\). Simplicity of the Perron eigenvalue then forces \(w\) to be a positive multiple of \(v\). This proves both global optimality and uniqueness, including \(n=2\).

**4. Uniform comparison and asymptotic.** With unit weights, an alternating binary word has \(n-1\) changes, achievable at a central cut; no word can have more. Hence \(L_n(\mathbf1)=n-1\). The exact parity formulas give \(\Lambda_n=2n/\pi+O(1/n)\). For \(n=3\) the optimum is \(2\) and has uniform weights; for \(n\ge4\) the sine weights are nonconstant, so strict uniqueness entails \(\Lambda_n<n-1\).

## Verification
Run `python CHECK.py` with Python 3 and no external packages. The checker enumerates every binary boundary pattern for \(2\le n\le11\), verifies the central-cut Perron eigenrelation through \(n=250\), checks the strict-chamber attaining-pair construction and independently samples other positive edge weights. Its successful output includes `ALL_SORTING_WEIGHTED_VARIATION_TESTS_PASS`. Enumeration only corroborates the finite cases. The all-order theorem and uniqueness follow analytically from the four proof steps above.

## Relationship to prior work
Chernozhukov, Fernández-Val and Galichon (arXiv:0806.4730, first posted 2008-06-29, Section 2.2) show that increasing rearrangement improves estimation against a monotone target in ordinary \(L^p\) discrepancies. Their comparison does not bound adjacent variation of the *difference of two rearranged arbitrary inputs* and has no optimized edge metric. Bankevich and Nazarov (arXiv:1402.3006, first posted 2014-02-12, especially Sections 1–2 and 7–8) give weighted continuous one-input Pólya–Szegő rearrangement inequalities. Steinerberger (arXiv:2209.06765, Theorem 2 and its proof) studies one-input graph-gradient rearrangement via edge-isoperimetry. The previously published finite-path sharp one-input convex-energy sorting result [4] gives the maximum ratio of an output prefix weight to a *minimum* fixed-cardinality input cut; this is a different quantity from the two-input modulus. A more general finite-graph **two-input** sorting cut characterization also yields the fixed-weight path coefficient (in its maximum-cut/minimum-cut form). Therefore the fixed-weight cut expression here is a supporting lemma, **not a claim of priority**. The contribution is the complete optimization of that coefficient over **all** strictly positive path weights, its unique sine optimizer, and the exact parity-dependent optimum. A previously published two-input Sobolev result for sorting on stars [5] uses a different graph and a quadratic norm. A weighted running-median theorem [6] does use a sine-vector Perron argument, but its local three-edge selector matrix and its bounded optimal coefficient do not imply the all-to-all sorting-chamber cut matrix or the unbounded parity formulas here. The material inspected does not provide the present theorem; an unindexed equivalent is not excluded.

## Limitations
The result concerns finite *paths*, increasing sorting of real scalar coordinates, strictly positive common input/output variation weights, and the global two-input seminorm. It does not establish the same optimum on cycles, trees, infinite sequences, or for other powers of the gradient norm. The theorem's sharpness is an exact finite-dimensional mathematical statement; its historical priority is qualified by limited indexing of older weighted-rearrangement and nonlinear Perron–Frobenius literature.

## References
1. V. Chernozhukov, I. Fernández-Val and A. Galichon, *Improving Point and Interval Estimates of Monotone Functions by Rearrangement*, arXiv:0806.4730, v1 2008-06-29, https://arxiv.org/abs/0806.4730.
2. S. V. Bankevich and A. I. Nazarov, *On Monotonicity of Some Functionals under Rearrangements*, arXiv:1402.3006, v1 2014-02-12, https://arxiv.org/abs/1402.3006.
3. S. Steinerberger, *Discrete Rearrangements and the Pólya–Szegő Inequality on Graphs*, arXiv:2209.06765, v1 2022-09-14, https://arxiv.org/abs/2209.06765.
4. *Isoperimetric sharp constants for sorting in convex weighted-path energies*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-isoperimetric-sharp-constants-for-sorting-in-convex-weighted-pat--40c683c1fbd3.
5. *Sharp two-point stability of sorting in finite-star Sobolev norms*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-two-point-stability-of-sorting-in-finite-star-sobolev-norm--6993154cc2b9.
6. *Sharp two-input variation sensitivity of three-point median smoothing on finite paths*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-input-variation-sensitivity-of-three-point-median-smoo--5759b99f2a42.
