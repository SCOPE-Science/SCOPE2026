# Sharp fourth-moment face localization on two-layer graphs with overlapping squares

## Finding
Let \(G\) be a finite simple graph with at least one edge, maximum degree at most two, and no triangles or four-cycles. (Thus every nontrivial connected component is a path or a cycle of length at least five.) Form the two-layer prism \(H=K_2\mathbin\square G\). Give every vertex of \(H\) an independent uniform sign \(\varepsilon_x\). For arbitrary real edge coefficients \(a=(a_e)\), put
\[
F_a=\sum_{\{x,y\}\in E(H)}a_{xy}\varepsilon_x\varepsilon_y,
\qquad S=\sum_{e\in E(H)}a_e^2=\mathbb E F_a^2.
\]
Then for every coefficient vector,
\[
\boxed{\mathbb EF_a^4\le4S^2,\qquad
\sup_{a\ne0}\frac{\|F_a\|_4}{\|F_a\|_2}=\sqrt2.}
\]
Every nonzero equality case has support exactly the four edges of **one vertical square** \(K_2\mathbin\square\{u,v\}\) for an edge \(\{u,v\}\) of \(G\), equal magnitudes on the four edges, and positive product of the four signed coefficients. Conversely every such coefficient vector is an equality case. In particular this classification applies simultaneously to all ordinary ladders \(K_2\mathbin\square P_n\) for \(n\ge2\) and closed ladders \(K_2\mathbin\square C_n\) for \(n\ge5\), where adjacent vertical squares share a rung.

The proof provides an exact fourth-moment deficit decomposition into nonnegative pieces, including a sharp positive-part energy inequality on the base graph.

## Assumptions and scope
All graph vertices are distinct and all edges are simple and undirected. The maximum-degree and girth restrictions are on the base graph \(G\), not the prism \(H\); the prism has many overlapping four-cycles. Isolated vertices of \(G\) are permitted. The probability measure is uniform on all independent signs and \(a\) is any real vector, including vectors with zero coordinates. For \(a\ne0\), \(S>0\); every norm is probability-normalized. The result concerns only the upper fourth-moment constant, not the sharp minimum of the fourth-to-second moment ratio.

Index vertices of \(G\) by \(v\in V\). Write \(r_v\) for the rung coefficient joining the two copies of \(v\); for an edge \(e=\{u,v\}\) of \(G\), write \(p_e,q_e\) for its two horizontal coefficients. Define
\[
R=\sum_v r_v^2,\quad s_e=p_e^2+q_e^2,\quad T=\sum_e s_e,\quad
h_e=|r_ur_v|,\quad f_e=(3h_e-R)_+,\quad g_e=(R-3h_e)_+.
\]
Here \(x_+=\max\{x,0\}\), and \(S=R+T\).

## Proof
**Fourth-moment identity and the relevant squares.** Distinct degree-two Walsh characters are orthogonal, so \(\mathbb E F_a^2=S\). In the fourth-power expansion, the only nonzero products involving four distinct edge characters correspond to simple four-cycles, each with multiplicity \(24\). Since \(G\) has no three- or four-cycles, every four-cycle of \(K_2\mathbin\square G\) is the vertical square associated with exactly one base edge. Therefore
\[
\mathbb EF_a^4
=3S^2-2\left(\sum_v r_v^4+\sum_e(p_e^4+q_e^4)\right)
+24\sum_{e=\{u,v\}}r_ur_vp_eq_e.\tag{1}
\]

**Positive-part graph lemma.** Suppose \(z_v\ge0\) for all vertices of a graph with maximum degree at most two and no triangles. Put \(Z=\sum_vz_v\) and \(w_{\{u,v\}}=[\tfrac32(z_u+z_v)-Z]_+\). Then
\[
\boxed{2\sum_{e\in E(G)}w_e^2\le\sum_vz_v^2.}\tag{2}
\]
For nonzero \(z\), equality holds precisely when its positive entries occur at the two endpoints of a single edge and are equal. To prove (2), any edge with \(w_e>0\) has endpoint mass greater than \(2Z/3\); consequently two such edges cannot be disjoint. Since the graph is triangle-free and has maximum degree two, there are at most two active edges, and if two, they are adjacent. With only one active edge \(e=\{u,v\}\),
\[
2w_e^2\le\frac12(z_u+z_v)^2\le z_u^2+z_v^2\le\sum_vz_v^2,
\]
with equality only in the stated case. With two active edges \(\{a,b\}\) and \(\{b,c\}\), denote their endpoint masses by \(A,B,C\) and all remaining mass by \(D\ge0\). Their positive \(w\)'s are \((A+B)/2-C-D\) and \((B+C)/2-A-D\); hence it suffices to show
\[
(A+B-2C)^2+(B+C-2A)^2\le2(A^2+B^2+C^2).\tag{3}
\]
Both active conditions imply \(B+C>2A\) and \(A+B>2C\). Without loss assume \(A\ge C\), so \(B>2A-C\). The right side minus left side of (3) equals
\[
-3A^2+2AB+8AC+2BC-3C^2
> A^2+10AC-5C^2\ge A^2+5C^2>0.
\]
Thus the two-edge case is strict. If no edge is active and \(z\ne0\), strictness is immediate. This proves the lemma and equality description.

**Sharp nonnegative deficit.** Put \(Q=\sum_vr_v^4\) and \(d_e=r_ur_vp_eq_e\). Straight expansion of (1) yields the *exact identity*
\[
\begin{aligned}
4S^2-\mathbb EF_a^4={}&(R-T)^2
+\sum_e(s_e-2f_e)^2+4\sum_eg_es_e\\
&+\left(2Q-4\sum_ef_e^2\right)
+\sum_e(p_e^2-q_e^2)^2\\
&+12\sum_eh_e(|p_e|-|q_e|)^2
+48\sum_e(-d_e)_+ .\tag{4}
\end{aligned}
\]
The first, second, third, fifth, sixth, and seventh terms are manifestly nonnegative. For the fourth, take \(z_v=r_v^2\); since \(h_e=\sqrt{z_uz_v}\le(z_u+z_v)/2\),
\[
f_e=(3h_e-R)_+\le[\tfrac32(z_u+z_v)-R]_+=w_e.
\]
Lemma (2) gives \(4\sum_ef_e^2\le4\sum_ew_e^2\le2Q\). Hence every term of (4) is nonnegative, proving the upper bound.

**All equality cases.** If \(a\ne0\) and the deficit vanishes, the fourth term of (4) and the equality conditions of (2) force \(r_v^2=z>0\) at exactly two adjacent base vertices and zero elsewhere, for some \(z\). In particular \(R=2z\), and \(f_e=z\) for their one connecting base edge \(e\) and \(f=0\) on other edges. The squared terms \((s_e-2f_e)^2\) force \(s_e=2z\) and all other horizontal coefficients to vanish. The remaining terms force \(|p_e|=|q_e|=\sqrt z\), and \((-d_e)_+=0\) forces \(r_ur_vp_eq_e>0\). These conditions are sufficient by (4). Finally a single square with four equal positive coefficients makes \(\mathbb EF_a^4=4S^2\), proving sharpness.

## Verification
The accompanying standalone Python 3 standard-library program `verify.py` derives the exact fourth-moment polynomial independently by complete sign enumeration on small prisms, checks (4) with exact rational arithmetic for \(200\) coefficient families, checks the graph lemma for \(87,369\) nonzero finite integer path profiles, and verifies equality and sign obstructions on every vertical square of the tested prisms. Run `python3 verify.py`; the success marker is `ALL_OVERLAPPING_SQUARE_PRISM_CHECKS_PASSED`. The universal all-graph theorem follows from (1)--(4) and the graph lemma, not from the finite checks.

## Relationship to prior work
Barak and collaborators (2012) motivate the computation of exact \(2\)-to-\(4\) norms of Boolean function subspaces and prove broad computational and hypercontractive assertions, not the sharp prism-family bound here. Blais and Tan (2013) establish general Boolean-cube hypercontractivity by entropy methods, without a sharp graph-specific prism equality classification. The published result *Sharp fourth moments and square localization for graph-supported Walsh spaces* covers base graphs whose four-cycles do **not** share edges. This hypothesis excludes the overlapping vertical-square chains here. The published *Sharp fourth moment and Euclidean distortion of the real \(Q_3\) edge Walsh chaos* proves localization in one particular eight-vertex cube; its proof and statement do not cover arbitrarily long open or closed ladders. The shared moment identity is standard background and is not claimed as novel. The new contribution is the graph-family sharp inequality and rigidity from the positive-part certificate (2)--(4).

## Limitations
All coefficients are real, all signs unbiased and independent, and the exponent is exactly four. Girth and maximum-degree hypotheses on \(G\) are essential to this proof: extra horizontal four-cycles or larger overlapping-star systems require other analyses. No optimal stability modulus for approximate extremizers is asserted. The equality classification is for exactly attaining the upper constant. Independent mathematical audit has not been performed. An unindexed reformulation could still overlap the present statement.

## References
1. B. Barak, F. G. S. L. Brandão, A. W. Harrow, J. A. Kelner, D. Steurer, and Y. Zhou, *Hypercontractivity, Sum-of-Squares Proofs, and their Applications*, arXiv:1205.4484v1, first posted 2012-05-21, https://arxiv.org/abs/1205.4484.
2. E. Blais and L.-Y. Tan, *Hypercontractivity Via the Entropy Method*, *Theory of Computing* 9 (2013), 889–896, published 2013-12-07, DOI 10.4086/toc.2013.v009a029.
3. *Sharp fourth moments and square localization for graph-supported Walsh spaces*, publicly indexed mathematical finding, identifier `0c3ab0087865` (2026).
4. *Sharp fourth moment and Euclidean distortion of the real \(Q_3\) edge Walsh chaos*, publicly indexed mathematical finding, identifier `45ae4e57bc26` (2026).
