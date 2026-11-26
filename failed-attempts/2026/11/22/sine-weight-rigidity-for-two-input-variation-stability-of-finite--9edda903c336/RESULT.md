# Sine-weight rigidity for two-input variation stability of finite sorting

## Finding
Fix an integer \(n\ge2\). For \(w_1,\ldots,w_{n-1}>0\), put
\[
 V_w(z)=\sum_{i=1}^{n-1}w_i|z_{i+1}-z_i|,
\]
and let \(S:\mathbb R^n\to\mathbb R^n\) sort coordinates increasingly. Define its *two-input* Lipschitz gain in weighted variation by
\[
 L_n(w)=\sup_{V_w(x-y)>0}\frac{V_w(Sx-Sy)}{V_w(x-y)}.
\]
For any subset \(A\subseteq\{1,\ldots,n\}\), let its weighted path-edge boundary be \(w(\partial A)=\sum_{i=1}^{n-1}w_i|\mathbf1_A(i+1)-\mathbf1_A(i)|\), and let \(C_j(w)=\max_{|A|=j}w(\partial A)\). Then the **exact, attained norm** for arbitrary positive weights is
\[
 \boxed{L_n(w)=\max_{1\le j<n}\frac{C_j(w)}{w_j}.}
\]
Over all strictly positive weight profiles, the minimum is attained **only** by the ray
\[
 \boxed{w_j=c\sin(\pi j/n),\quad 1\le j<n,\quad c>0.}
\]
Its exact optimum is
\[
 \boxed{\inf_{w>0}L_n(w)=K_n=
 \begin{cases}
 \cot\!\bigl(\pi/(2n)\bigr),&n\ \text{even},\\
 \csc\!\bigl(\pi/(2n)\bigr),&n\ \text{odd}.
 \end{cases}}
\]
In particular \(K_n=2n/\pi+O(n^{-1})\), while uniform edge weights give the larger sharp multiplier \(n-1\). This is a minimax theorem for perturbations **between two inputs**, not the one-input variation contraction of rearrangement.

## Assumptions and scope
The underlying domain is a finite real coordinate path of length \(n\ge2\). Every edge weight is strictly positive and fixed for both the input and output variations. Sorting is increasing, and ties are permitted. Since sorting commutes with adding constants and \(V_w\) vanishes exactly on constant vectors, the ratio is well-defined on the quotient by constants. The supremum involves arbitrary distinct input vectors with nonzero variation difference. Neither periodic edges nor arbitrary graph arrangements are included.

## Proof
**1. Reduction to the maximum-cut formula.** In each open region where coordinates are strictly ordered in a fixed permutation, \(S\) is that coordinate permutation matrix \(P\). For a linear map \(P\) preserving constants, the induced variation seminorm equals its weighted column-sum norm after conjugating by the first-difference map on the quotient. The inverse images of the unit coordinate vectors under that difference map are the step sequences \(h^{(j)}\) that are zero at indices \(1,\ldots,j\) and one at indices \(j+1,\ldots,n\). Thus
\[
 \|P\|_{V_w\to V_w}=
 \max_{1\le j<n}\frac{V_w(Ph^{(j)})}{w_j}.
\]
As \(P\) ranges through all permutations, \(Ph^{(j)}\) ranges through every binary sequence with exactly \(j\) zeros, or equivalently the complementary indicators of all \(j\)-element subsets. Its largest variation is precisely \(C_j(w)\). To pass from local linear norms to the global nonlinear map, partition the segment joining any two inputs at its finitely many crossings of coordinate-order walls (or approximate a segment lying in a wall by generic segments), and sum the variation bounds on the pieces. Conversely, for any specified permutation \(P\), choose a vector with strictly ordered coordinates realizing its chamber. An arbitrarily small step perturbation remains in that chamber, and gives the corresponding linear ratio **exactly**. Therefore the global constant is the displayed maximum-cut formula and is attained by an actual pair.

**2. Canonical central cuts.** Put \(\theta=\pi/n\), \(s_i=\sin(i\theta)>0\), and \(r=\min(j,n-j)\). A binary sequence with exactly \(j\) ones can cross at most \(2r\) edges, as each of its ones and zeros contributes at most two neighboring boundaries. For the symmetric strictly unimodal sequence of weights \(s_i\), the sum of any at most \(2r\) distinct edge weights is bounded by the sum of the \(2r\) greatest weights (all \(n-1\) when \(2r\ge n-1\)). The latter consist of central consecutive indices and can be realized by an alternating binary pattern with the requested cardinality:

- If \(n=2m+1\), take boundary indices \(m-r+1,\ldots,m+r\).
- If \(n=2m\) and \(j<m\), take indices \(m-j,\ldots,m+j-1\); if \(j>m\), take \(m-r+1,\ldots,m+r\); and if \(j=m\), take all indices \(1,\ldots,n-1\).

The strings are obtained by alternating labels across those edges and holding them constant outside. For each case a direct count gives \(j\) ones, or its complement gives \(j\) ones without changing the boundary. The finite trigonometric progression identity
\[
 \sum_{i=a}^{b}\sin(i\theta)
 =\frac{\sin((b-a+1)\theta/2)\sin((a+b)\theta/2)}{\sin(\theta/2)}
\]
shows that the maximal boundary weight for \(s\) is exactly
\[
 C_j(s)=K_n\sin(j\theta)=K_ns_j
\]
with \(K_n\) as above. Indeed, for odd \(n\), the central sum has \(2r\) terms with midpoint \(n/2\), giving \(\sin(r\theta)/\sin(\theta/2)\); for even \(n\), the chosen central sum has midpoint \((n-1)/2\) or \((n+1)/2\), giving \(\sin(r\theta)\cot(\theta/2)\). The central case \(j=m\) follows from the same identity with all edges. Hence \(L_n(s)=K_n\).

**3. Global lower bound and rigidity.** Define a nonnegative square matrix \(A\), indexed by \(1\le j,i<n\), whose \(j\)-th row is the indicator of the canonical central boundary set in step 2. That set arises from a permitted binary cut of cardinality \(j\); consequently, for *every* \(w>0\),
\[
 L_n(w)\ge\max_j\frac{(Aw)_j}{w_j}.
\]
The trigonometric identity gives \(As=K_ns\). For arbitrary \(w>0\), let \(q=\min_i w_i/s_i>0\), and choose an index \(j\) attaining that minimum. Componentwise \(w\ge qs\), so positivity of \(A\) yields
\[
 (Aw)_j\ge q(As)_j=qK_ns_j=K_nw_j.
\]
Thus \(L_n(w)\ge K_n\). If equality holds, equality must also hold in this coordinate. Every column \(i\) with \(A_{ji}=1\) then satisfies \(w_i=qs_i\). In particular the central column \(i=m\), where \(m=\lfloor n/2\rfloor\), belongs to *every* canonical row, so \(w_m=qs_m\). For the central row \(j=m\), the canonical boundary contains **every edge** (for both even and odd \(n\)), and equality \(L_n(w)=K_n\) forces \((Aw)_m=K_nw_m\). Since all terms of \(w-qs\) are nonnegative and every entry in row \(m\) equals one, they must all vanish. Thus \(w=qs\), establishing unique optimality up to positive scale.

**4. Uniform comparison and asymptotics.** With unit weights, the maximum cut of a binary sequence on a path is \(n-1\), and a fully alternating sequence crosses all edges. For \(j=\lfloor n/2\rfloor\), the denominator is one; hence \(L_n(1)=n-1\). Finally \(\cot t=t^{-1}+O(t)\) and \(\csc t=t^{-1}+O(t)\), with \(t=\pi/(2n)\), prove the asymptotic comparison.

## Verification
`CHECK.py` uses Python 3 standard-library integers and `Fraction` to exhaustively enumerate every fixed-cardinality cut for lengths \(2\) through \(11\), including the realization of each claimed central edge set. It independently checks the trigonometric constant numerically, and for hundreds of positive rational weight profiles compares the cut formula with all permuted step inputs and randomly generated *two-input* sorted differences exactly. It constructs an actual strict-chamber rational pair attaining a nontrivial weighted ratio. Run with `python CHECK.py`. Expected terminal lines include `CENTRAL_CUTS_ALL_CARDINALITIES_AND_SINE_EQUALITIES_PASS`, `EXACT_WEIGHTED_CUT_OPERATOR_NORMS_AND_TWO_INPUT_TESTS_PASS`, `ACTUAL_STRICT_SORTING_CHAMBER_SHARPNESS_WITNESS_PASS`, and `ALL_SORTING_VARIATION_CERTIFICATES_PASS`. These finite tests supplement, but do not replace, the arbitrary-dimension proof above.

## Relationship to prior work
Chong (1975, Theorem 2.1) proves weak submajorization of the *single-input* difference magnitudes after decreasing rearrangement; this yields the classical unweighted one-input variation inequality, but does not estimate the weighted variation of **differences between two rearranged inputs**. Anevski–Fougères (arXiv:0710.4617v1, 2007-10-25, Section 2) develop rearrangement regularity for statistical estimation, mainly uniform and ordinary \(L^p\) estimates, not the weighted edge-variation minimax problem. Bankevich–Nazarov (arXiv:1402.3006v1, Sections 2–3) study weighted Pólya–Szegő inequalities under rearrangement, again for the energy of *one function*.

Related published finite-path results include an exact *one-input* weighted convex-energy rearrangement ratio \(\max_j w_j/h_j(w)\) and a two-input **star-graph quadratic Sobolev** sorting constant. Neither result implies the present *two-input path* maximum-*cut* formula, and the sine minimax profile does not appear in those inspected statements. A sharp sine-weight optimization for three-point median filtering concerns a different nonlinear map and has a different formula. The classical sources provide important rearrangement background; the maximum-cut derivation and global weight-design theorem address a distinct stability question. Historical-priority risk remains for unindexed finite rearrangement and nonlinear metric geometry literature.

## Limitations
This theorem is finite-dimensional and specific to the weighted \(\ell^1\) norm of first differences on an open path. It does not treat continuous BV functions, non-path graphs, periodic boundary conditions, higher-order differences, or the same sorting map in weighted \(\ell^p\) Sobolev metrics. Optimizing weights makes the two-input gain smallest but never below one and does not amount to a probabilistic error bound. Existing unpublished or unindexed equivalent formulations cannot be excluded. Only self-review has occurred; independent audit is not performed.

## References
1. K.-M. Chong, *Variation reducing properties of decreasing rearrangements*, Canadian Journal of Mathematics **27** (1975), 330–336, Theorem 2.1. https://doi.org/10.4153/CJM-1975-040-2
2. D. Anevski and A.-L. Fougères, *Limit properties of the monotone rearrangement for density and regression function estimation*, arXiv:0710.4617v1, first public 2007-10-25. https://arxiv.org/abs/0710.4617
3. S. V. Bankevich and A. I. Nazarov, *On monotonicity of some functionals under rearrangements*, arXiv:1402.3006v1, first public 2014-02-12. https://arxiv.org/abs/1402.3006
4. *Isoperimetric sharp constants for sorting in convex weighted-path energies*, published mathematical record (2026), identifier `2026/10/25/SCOPE-isoperimetric-sharp-constants-for-sorting-in-convex-weighted-pat--40c683c1fbd3`.
5. *Sharp two-point stability of sorting in finite-star Sobolev norms*, published mathematical record (2026), identifier `2026/10/26/SCOPE-sharp-two-point-stability-of-sorting-in-finite-star-sobolev-norm--6993154cc2b9`.
