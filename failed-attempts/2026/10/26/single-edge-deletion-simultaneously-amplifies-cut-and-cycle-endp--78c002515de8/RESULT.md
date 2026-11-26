# Single-edge deletion simultaneously amplifies cut and cycle endpoint norms from dimension four

## Finding

Let \(H_n\) be the unit-edge Boolean hypercube on \(\{0,1\}^n\), and let \(H_n^-\) be obtained by removing any one edge. For a connected graph \(G\), write \(C_G=D_G^{\mathsf T}(D_GD_G^{\mathsf T})^+D_G\) for the canonical Euclidean-orthogonal projection onto the real edge cut space, and \(Z_G=I-C_G\) for its cycle-space complement. The induced \(\ell_1\) and \(\ell_\infty\) norms of each projection agree by symmetry of its matrix.

For every integer \(n\ge4\), **both** projections exhibit strict amplification after deleting one edge:
\[
\|C_{H_n^-}\|_{1\to1}>\|C_{H_n}\|_{1\to1},\qquad
\|Z_{H_n^-}\|_{1\to1}>\|Z_{H_n}\|_{1\to1}.
\]
More precisely, set
\[
 r_n=\frac2n(1-2^{-n}),\quad
 a_n=\frac2{n(n-1)}\bigl(1-(n+1)2^{-n}\bigr),\quad
 d_n=\frac{(n-3)a_n}{2(1-r_n)},\quad
 z_n=d_n-\frac{2a_n^2}{1-r_n}.
\]
The intact cube norms are \(\|C_{H_n}\|=(n+1)/2\) and \(\|Z_{H_n}\|=(n+3)/2-2r_n\). Every edge \(f\) parallel to the removed edge and shifted by exactly one different coordinate has **exact** post-deletion column sums
\[
\sum_{g\in E(H_n^-)}|(C_{H_n^-})_{gf}|=\frac{n+1}{2}+d_n,\qquad
\sum_{g\in E(H_n^-)}|(Z_{H_n^-})_{gf}|=\frac{n+3}{2}-2r_n+z_n.
\]
Both \(d_n\) and \(z_n\) are positive for every \(n\ge4\), and \(d_n=1/n+O(n^{-2})\), \(z_n=1/n+O(n^{-2})\). These are certified **lower bounds on the new operator norms**, not assertions that these columns globally maximize them.

The threshold is sharp in the hypercube family: for \(n=2\), deleting an edge changes the pair of norms from \((3/2,1)\) to \((1,0)\); for \(n=3\) it changes them from \((2,11/6)\) to \((2,71/40)\). Thus the first dimension in which a deletion **strictly increases both norms** is four.

## Assumptions and scope

All graphs are finite, simple, connected, unweighted, and real. Every graph edge is oriented from bit zero to bit one in its changing coordinate, with \(D_G\) the signed vertex-edge incidence matrix. \(H_n^-\) is connected for \(n\ge2\). The full assertion for \(n\ge4\) concerns a single deleted edge and the canonical orthogonal projections, not the smallest possible norm over all projections, nor a claim of monotonicity for arbitrary graphs.

## Proof

**1. Fourier representation of the intact edge-current matrix.** Let \(E_n\) be the oriented edges of \(H_n\). Write an oriented edge as \((x,i)\), with \(x_i=0\) and other endpoint \(x\oplus e_i\). For \(S\subseteq[n]\), let \(\chi_S(x)=(-1)^{\sum_{k\in S}x_k}\). Each nonconstant Walsh character has Laplacian eigenvalue \(2|S|\). Hence, for edges \((x,i),(y,j)\),
\[
 (C_{H_n})_{(x,i),(y,j)}
 =2^{1-n}\sum_{S\supseteq\{i,j\}}\frac{\chi_S(x\oplus y)}{|S|}
 =2^{1-n}\chi_U(x\oplus y)\int_0^1 t^{|U|-1}
 \prod_{k\notin U}(1+(-1)^{x_k+y_k}t)\,dt,
\]
where \(U=\{i,j\}\) as a set. The integrand is strictly positive for \(0<t<1\); the entry sign is therefore exactly \(\chi_U(x\oplus y)\). In the same coordinate direction, all entries are positive. For a fixed source edge, summing the absolute currents on source-parallel edges gives \(1\), and on edges in each other coordinate direction gives \(1/2\). Indeed, after summing over basepoint bits, the products telescope to \(2^{n-1}\) or \(2^{n-2}\), leaving \(\int_0^1dt=1\) or \(\int_0^1t\,dt=1/2\). Consequently every intact column has absolute sum \(1+(n-1)/2=(n+1)/2\).

**2. Two exact kernel coefficients.** By symmetry delete \(e=(0,1)\), where the coordinate \(1\) denotes the first bit. Let \(f=(e_2,1)\) be the parallel edge one square away. The above integrals give
\[
 r_n=(C_{H_n})_{ee}=2^{1-n}\int_0^1(1+t)^{n-1}\,dt
 =\frac2n(1-2^{-n}),
\]
\[
 a_n=(C_{H_n})_{ef}=2^{1-n}\int_0^1(1+t)^{n-2}(1-t)\,dt
 =\frac2{n(n-1)}\bigl(1-(n+1)2^{-n}\bigr).
\]
Both are positive and \(a_n\le1-r_n\). The latter follows directly from
\[
 (1-r_n)-a_n=\frac{(n-3)2^n+4}{(n-1)2^n}\ge0\quad(n\ge2).
\]
Thus \(0<\alpha:=a_n/(1-r_n)\le1\).

**3. Rank-one deletion formula.** On the mean-zero vertex subspace, deleting \(e\) changes the Laplacian to \(L'=L-b_eb_e^{\mathsf T}\). Since \(r_n<1\), the Sherman–Morrison formula applies. For any remaining oriented edges \(g,h\),
\[
 (C_{H_n^-})_{gh}=(C_{H_n})_{gh}
 +\frac{(C_{H_n})_{ge}(C_{H_n})_{eh}}{1-r_n}.
\]
In particular the new \(f\)-column equals the original \(f\)-column plus \(\alpha\) times the original \(e\)-column, with the row \(e\) omitted. Also
\[
 (C_{H_n^-})_{ff}=r_n+\frac{a_n^2}{1-r_n}.
\]

**4. Exact absolute column sums and strict amplification.** By the explicit Walsh-integral sign formula, the two intact columns for \(f\) and \(e\) have **matching signs** on every coordinate direction except direction \(2\). In direction \(2\), they are negatives with the same absolute value: changing the source basepoint by \(e_2\) flips the forced Walsh sign, while the remaining integral is unchanged. Because \(0<\alpha\le1\), adding \(\alpha\) times column \(e\) increases the absolute sums in matching-sign directions by the corresponding source-column magnitude, and decreases the direction-\(2\) sum by the same factor. With intact total \(C=(n+1)/2\), source diagonal \(r_n\), and direction-\(2\) absolute sum \(1/2\), omission of row \(e\) yields
\[
 \begin{aligned}
 \sum_{g\ne e}|(C_{H_n^-})_{gf}|
 &=C-a_n+\alpha\bigl(C-r_n-2(1/2)\bigr)\\
 &=C+\frac{(n-3)a_n}{2(1-r_n)}=C+d_n.
 \end{aligned}
\]
Since the diagonal of the complementary projection is \(1-(C_{H_n^-})_{ff}\), its corresponding column sum is
\[
 \sum_{g\ne e}|(Z_{H_n^-})_{gf}|
 =C+d_n+1-2\bigl(r_n+a_n^2/(1-r_n)\bigr)
 =\frac{n+3}{2}-2r_n+z_n.
\]
For \(n\ge4\), \(d_n>0\). Moreover
\[
 z_n=\frac{a_n}{1-r_n}\left(\frac{n-3}{2}-2a_n\right)>0,
\]
since \(2a_n<4/[n(n-1)]\le1/3<(n-3)/2\). The positive column increments give the asserted strict **operator-norm lower bounds**. The explicit formulas also yield the stated \(1/n+O(n^{-2})\) asymptotics.

**5. Exact low-dimensional boundary.** At \(n=2\) the damaged graph is a tree, so its cut projection is the identity and its cycle projection vanishes. At \(n=3\), the remaining eleven edges fall into four symmetry classes relative to \(e\). Their cut/cycle absolute column sums, respectively, are
\[
 (15/8,3/2),\quad (2,17/10),\quad
 (39/20,71/40),\quad(9/5,8/5).
\]
The classes have sizes \(4,2,4,1\), exhausting all eleven edges. These entries follow from the same finite Walsh formula and rank-one update; the included exact-rational checker independently reconstructs every column from the grounded inverse of the damaged graph. Hence the maxima are \(2\) and \(71/40\). For intact \(n=3\), the formulas above give \(2\) and \(11/6\). This proves that neither projection strictly increases in dimension three.

## Verification

Execute `python3 verify.py` with Python 3 standard library. The checker recomputes the intact Walsh-current entries and the deleted rank-one formula in dimensions \(2\) through \(5\), independently inverts each damaged graph's grounded Laplacian over exact rational numbers, and compares **all 124 remaining-edge columns**. It verifies the kernel coefficients, direction-wise absolute-current totals, the adjacent-edge formulas, and the complete \(n=3\) boundary census. The universal \(n\ge4\) conclusion follows from the analytical sign-and-inequality proof above, not finite testing.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii [1, Theorem 45 and Corollary 60] determine the exact canonical projection norms **on intact Boolean hypercubes**. The result here addresses the fundamentally different symmetry-broken graph after removing one edge, via a rank-one update and sign analysis. Schild, Rao and Srivastava [2], and Gurel-Gurevich, Nachmias and Sachdeva [3], establish general electrical-flow localization estimates but not this exact perturbation threshold. General rank-one graph-Laplacian updates are standard; the new content is the exact signed-column calculation and simultaneous dimension-four amplification. In contrast, complete-graph and complete-bipartite one-edge deletions have different norm-response phase behavior. The proof makes no claim about optimal nonorthogonal projections.

## Limitations

The exact displayed post-deletion column values are **witnesses**, not an asserted global formula for the entire damaged graph's endpoint norms in dimensions \(n\ge4\). The low-dimensional norms are exact by exhaustive rational computation. The theorem concerns only single-edge deletion, real unweighted cubes, and canonical orthogonal cut/cycle projections; intermediate \(\ell_p\) norms, arbitrary graph modifications, and minimum norms over nonorthogonal projections are not determined. Bibliographic novelty has residual risk from unindexed electrical-network identities.

## References

[1] S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (first public 2023-05-21), Section 2.7, Theorem 45 and Corollary 60. https://arxiv.org/abs/2305.12582

[2] A. Schild, S. Rao and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632v1 (2017-08-04), Sections 1–2. https://arxiv.org/abs/1708.01632

[3] O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130v1 (2026-05-22), Theorems 1.1–1.3. https://arxiv.org/abs/2605.24130
