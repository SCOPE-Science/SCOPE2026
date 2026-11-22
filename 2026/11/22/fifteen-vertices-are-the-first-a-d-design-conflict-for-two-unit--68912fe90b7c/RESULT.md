# Fifteen vertices are the first A–D design conflict for two unit chords on a path

## Finding
For every integer \(4\le n\le14\), adding exactly two distinct unit-conductance nonedges to the unit-conductance path \(P_n\) gives the *same entire set* of maximizing designs for the spanning-tree count and minimizing designs for the Kirchhoff index. The first conflict occurs at \(n=15\), where these two sets are disjoint. With zero-based vertices \(0,1,\dots,14\), the **only** A-optimal pairs of new edges are
\[
\{(0,9),(4,13)\},\quad \{(1,10),(5,14)\},
\]
and the **only** D-optimal pairs are
\[
\{(0,9),(4,14)\},\quad \{(0,10),(4,14)\},\quad \{(0,10),(5,14)\}.
\]
Every A-optimal design has \(75\) spanning trees and Kirchhoff index \(1004/5\). Every D-optimal design has \(85\) spanning trees and Kirchhoff index \(3420/17\). Thus using a D-optimal design instead of an A-optimal design incurs the exact positive resistance loss
\[
\frac{3420}{17}-\frac{1004}{5}=\frac{32}{85}.
\]

## Assumptions and scope
All graphs are simple, undirected, connected, with unit edge conductances and no parallel edges. The underlying graph \(P_n\) has vertices \(\{0,\ldots,n-1\}\) and edges \(\{(i,i+1):0\le i<n-1\}\). Choose precisely two distinct nonedges \(e=(a,b)\), \(f=(c,d)\), where \(a+2\le b\) and \(c+2\le d\). D-optimal means maximizing the *number* \(\tau(G)\) of spanning trees; A-optimal means minimizing \(\mathrm{Kf}(G)=\sum_{i<j}R_G(i,j)\), total effective resistance. The assertion is only for \(4\le n\le15\), not an all-orders phase law. No continuously variable conductance budgets or candidate-edge prices are considered.

## Proof
Let \(L\) be the path Laplacian, \(b_e=\mathbf e_a-\mathbf e_b\), and \(b_f=\mathbf e_c-\mathbf e_d\). Define
\[
\ell_e=b-a,\quad \ell_f=d-c,\quad h=\max(0,\min(b,d)-\max(a,c)).
\]
The path Green operator satisfies \(b_e^\top L^+b_e=\ell_e\), \(b_f^\top L^+b_f=\ell_f\), and \(b_e^\top L^+b_f=h\). Applying the determinant lemma on \(\mathbf1^\perp\), and using \(\tau(P_n)=1\), yields the *integer* spanning-tree count
\[
D_{ef}:=\tau(P_n+e+f)=(1+\ell_e)(1+\ell_f)-h^2. \tag{1}
\]
For a chord \(e=(a,b)\), set \(s_e(t)=\min(\max(t-a,0),b-a)\), \(\bar s_e=\sum_{t=0}^{n-1}s_e(t)\) and \(v_e(t)=n s_e(t)-\bar s_e\). Solving the unit-current path equation gives \(L^+b_e=-v_e/n\). Write \(R_{ef}=\sum_{t=0}^{n-1}v_e(t)v_f(t)\) and similarly \(R_{ee},R_{ff}\). Woodbury's identity on \(\mathbf1^\perp\), together with \(\mathrm{Kf}(G)=n\operatorname{tr}(L_G^+)\), yields the exact formula
\[
\mathrm{Kf}(P_n+e+f)=\frac{n^3-n}{6}-\frac{(1+\ell_f)R_{ee}+(1+\ell_e)R_{ff}-2h R_{ef}}{nD_{ef}}. \tag{2}
\]
The numerator, denominator, and every auxiliary vector here are integers. Equations (1)–(2) therefore permit *exact finite exhaustive comparison* with integer cross-multiplication or rational fractions and no floating-point ambiguity.

There are precisely \((n-1)(n-2)/2\) eligible nonedges and \(\binom{(n-1)(n-2)/2}{2}\) unordered two-edge augmentations. The accompanying standalone `VERIFY.py` traverses **every** such pair for every \(n=4,\ldots,15\), in total \(13{,}104\) graphs, computes (1)–(2) as exact rational numbers, retains *all ties*, and asserts the following exhaustive summary:

| \(n\) | Maximum \(\tau\) | Number of D-optima | Number of A-optima | Same complete optimizer set? |
|---:|---:|---:|---:|---|
|4|8|3|3|Yes|
|5|12|1|1|Yes|
|6|16|3|3|Yes|
|7|21|3|3|Yes|
|8|27|1|1|Yes|
|9|33|3|3|Yes|
|10|40|3|3|Yes|
|11|48|1|1|Yes|
|12|56|3|3|Yes|
|13|65|3|3|Yes|
|14|75|1|1|Yes|
|15|85|3|2|No|

At \(n=15\), the exhaustive computed argmin/argmax sets are exactly those stated in the Finding section. The independent grounded-Laplacian determinant and inverse calculations in the checker verify their \(\tau\) and \(\mathrm{Kf}\) values. This is a finite, exhaustive computational proof based on explicit identities (1)–(2), not an inference from sampling or an infinite extrapolation.

## Verification
Run `python3 VERIFY.py` with the standard Python 3 library. It independently builds the finite candidate universes, computes the exact-rational analytic scores, checks every listed optimum and tie, and tests representative results against direct matrix-tree determinants (integer Bareiss elimination) and Kirchhoff indices from grounded Laplacian inverses (fractional Gauss–Jordan elimination). The independent comparison identity used is \(\mathrm{Kf}(G)=n\operatorname{tr}(L_g^{-1})-\mathbf1^\top L_g^{-1}\mathbf1\). The reported outcome is an exhaustive pass for \(13{,}104\) candidates. This proof is conditional only on ordinary exact integer/rational arithmetic and the explicitly inspectable source code, not on a proprietary solver.

## Relationship to prior work
Ghosh, Boyd and Saberi (2006) develop total-resistance minimization through continuously optimized edge conductances; this differs from choosing exactly two additional fixed unit edges. Khosoussi and collaborators (2016) develop spanning-tree-maximizing edge augmentation and greedy guarantees, but the present finite A-versus-D optimizer coincidence and first-conflict classification is not asserted there. Earlier extremal bicyclic spanning-tree results address one objective only; no novelty is claimed for the separate maximum-tree-count sequence. Existing one-shortcut path resistance placement and two-rung parallel-path results concern different feasible families. The result is specifically the *sharp finite first separation of both exact optimizer sets on the same two-chord path design space*.

## Limitations
The theorem establishes the first disagreement, not an all-size classification for \(n>15\); no asymptotic conflict theorem is claimed. This exact finite result has a modest Kirchhoff penalty \(32/85\) at the first witness; it is primarily a structural benchmark for objective-dependent graph augmentation. Exhaustive source searches cannot prove publication priority, and equivalently phrased specialized results may remain unindexed. Independent mathematical review has not been performed.

## References
- A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings MTNS, 2006. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
- K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116, first public April 5, 2016. https://arxiv.org/abs/1604.01116
- Y. Tseng and S. Wang, *Maximizing number of spanning trees based on cycle basis representation*, International Journal of Computer Mathematics, 1989. https://doi.org/10.1080/00207168908803727
