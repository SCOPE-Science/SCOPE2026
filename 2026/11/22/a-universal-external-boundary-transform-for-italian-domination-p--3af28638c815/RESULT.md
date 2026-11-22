# A universal external-boundary transform for Italian domination polynomials of leaf coronas

## Finding
Let \(G=(V,E)\) be any finite simple graph on \(n\ge1\) vertices, with no connectivity requirement. Let \(W(G)=G\circ K_1\) denote the graph formed by adjoining one private leaf \(v'\) to every \(v\in V\). An *Italian dominating function* is \(f:V(W(G))\to\{0,1,2\}\) for which every vertex labeled zero has an open-neighborhood label sum at least two. Let \(D_I(W(G);z)=\sum_f z^{\sum_x f(x)}\) count every such function by its total weight.

For each \(P\subseteq V\), put \(B_G(P)=\{v\in V\setminus P:N_G(v)\cap P\ne\varnothing\}\), and \(b_G(P)=|B_G(P)|\). Then the complete Italian domination polynomial of **every** one-leaf corona is
\[
\boxed{D_I(G\circ K_1;z)=\sum_{P\subseteq V} z^{2n-b_G(P)}(2+2z+z^2)^{|P|}(1+z)^{b_G(P)}.}\tag{1}
\]
Thus every coefficient is determined by the two-parameter distribution of the size and external neighborhood of vertex subsets of the base graph; the formula counts *all* functions, not merely optimal or pointwise-minimal functions.

Writing \(\gamma(G)\) for the usual domination number of the base graph, the minimum Italian weight satisfies the previously established identity
\[
\gamma_I(G\circ K_1)=n+\gamma(G),\tag{2}
\]
while the **number of minimum-weight Italian functions** has the exact general expression
\[
\boxed{d_I(G\circ K_1,n+\gamma(G))=\sum_{\substack{P\subseteq V\\ b_G(P)=n-\gamma(G)}}2^{|P|}.}\tag{3}
\]
The total number of Italian functions has the evaluation
\[
\boxed{D_I(G\circ K_1;1)=\sum_{P\subseteq V}5^{|P|}2^{b_G(P)}.}\tag{4}
\]

For an edgeless base on \(n\) vertices, (1) reduces to \(z^{2n}(3+2z+z^2)^n\). For the two-vertex edge base, whose corona is the four-vertex path, the complete polynomial is \(4z^3+13z^4+14z^5+10z^6+4z^7+z^8\). For the three-vertex complete-graph base, the first nonzero coefficient is \(6z^4\). These identities illustrate that the full polynomial contains information not supplied by the minimum-weight identity alone.

## Assumptions and scope
All graphs are finite, undirected, loopless and simple; isolated base vertices and disconnected bases are permitted. The corona contains exactly one pendant leaf per base vertex, not a pendant clique or a multiple-leaf attachment. All labelings are on the fixed labeled vertex set and are counted separately; no quotient by automorphisms is taken. The formal variable \(z\) records total label weight. The definition of Italian domination is also called Roman \(\{2\}\)-domination, distinct from ordinary Roman domination (which requires a neighboring label-two vertex for every zero). When \(n=0\), the same formula extends by convention with value one, but the stated theorem uses \(n\ge1\).

## Proof
**Classification by positive core support.** Let \(f\) be an Italian function. Define \(P=\{v\in V:f(v)>0\}\). For each base vertex \(v\), its pendant leaf \(v'\) has no neighbor other than \(v\). We enumerate the possible ordered pairs \((f(v),f(v'))\) conditional on whether \(v\in P\) and whether a root neighbor lies in \(P\).

If \(v\in P\), then \(f(v)=1\) or \(2\). If \(f(v)=1\), its leaf must be positive, giving precisely \((1,1),(1,2)\). If \(f(v)=2\), its leaf can be \(0,1,2\), giving \((2,0),(2,1),(2,2)\). The zero leaf in the first excluded pair \((1,0)\) would have neighborhood sum one; the allowed pairs have no further restriction because a positive root has no Italian requirement. Their contribution is exactly
\[
z^2+z^3+z^2+z^3+z^4=z^2(2+2z+z^2).\tag{5}
\]

If \(v\notin P\), then \(f(v)=0\), so its leaf is positive (a zero leaf would have a zero neighbor). If \(v\in B_G(P)\), at least one base neighbor has label \(1\) or \(2\). Thus either \((0,1)\) or \((0,2)\) is allowed, because in the first case the leaf contributes one and the positive root neighbor contributes at least one. Their contribution is \(z+z^2=z(1+z)\). If \(v\in V\setminus(P\cup B_G(P))\), every neighboring root has label zero, so its private leaf must carry two, and the unique possible pair is \((0,2)\), contributing \(z^2\).

Conversely, choosing any of these permitted local pairs, independently at each vertex after fixing \(P\), yields an Italian dominating function: each zero leaf has a core root labeled two, each zero root with a positive core neighbor gets the remaining necessary unit from its leaf, and each other zero root is defended by its leaf labeled two. No other vertices require a check. The support \(P\) is uniquely determined by a labeling, so the decomposition has no overlaps. Multiplying contributions for its \(|P|\) positive roots, \(b_G(P)\) boundary-zero roots, and \(n-|P|-b_G(P)\) interior-zero roots gives
\[
\left[z^2(2+2z+z^2)\right]^{|P|}\left[z(1+z)\right]^{b_G(P)}\left[z^2\right]^{n-|P|-b_G(P)}
=z^{2n-b_G(P)}(2+2z+z^2)^{|P|}(1+z)^{b_G(P)}.
\]
Summing over \(P\subseteq V\) proves (1). Evaluating at one proves (4).

**Minimum weight and its full multiplicity.** Let \(M=\max_{P\subseteq V} b_G(P)\). All factors in (1), after extracting their lowest power of \(z\), have nonzero positive constant term. Thus the least exponent is \(2n-M\). For any \(P\), the set \(P\cup\big(V\setminus(P\cup B_G(P))\big)\) dominates \(G\) and has cardinality \(n-b_G(P)\). Hence \(\gamma(G)\le n-b_G(P)\), giving \(M\le n-\gamma(G)\). Conversely, if \(P\) is a minimum dominating set of cardinality \(\gamma(G)\), then \(B_G(P)=V\setminus P\) and \(b_G(P)=n-\gamma(G)\); hence \(M=n-\gamma(G)\). This recovers (2), originally proved in the cited earlier literature. For each support \(P\) attaining \(M\), the coefficient at its lowest power \(z^{2n-M}\) is the constant coefficient of \((2+2z+z^2)^{|P|}(1+z)^M\), namely \(2^{|P|}\). Supports with smaller boundary contribute only at greater weights. Summation proves (3).

## Verification
Two standalone, dependency-free implementations are supplied: `verify.py` (Python 3) and `verify_all_small.cpp` (C++17). They enumerate every labeling of the full leaf corona directly and compare its complete coefficient vector with the subset formula, without using the structural proof for the direct enumeration. The C++ program covers **all 1,099 labeled simple base graphs of orders one through five**, checking 22,719 polynomial coefficient positions, minimum values and minimum multiplicities. The Python program separately checks every base graph through four vertices and four representative five-vertex bases (path, cycle, star, complete graph). Both return `VERIFY_OK`.

To reproduce, run `python3 verify.py`, then compile with `c++ -O3 -std=c++17 verify_all_small.cpp -o verify_all_small` and run `./verify_all_small`. The finite tests are corroboration, not a proof of the all-order formula; the complete classification and boundary-dominating-set argument above provide the proof.

## Relationship to prior work
Shao and Zhao [1], first available September 9, 2026, introduced explicit Italian-domination coefficient counting for trees and cycles and provided dynamic programs for these classes. They did not state the all-base leaf-corona boundary transform (1); their general-tree algorithm could compute coefficients of individual leaf-corona trees, but does not by itself provide formula (1) for arbitrary bases, including cyclic/disconnected graphs.

Alizadeh, Maimani, Parsaei Majd and Rajabi Parsa [2, Theorem 3.2] already proved the *scalar* identity (2) for all base graphs. Hernández-Ortiz, Montejano and Rodríguez-Velázquez [3] developed the analogous scalar Italian-domination theory for rooted products. Neither scalar result implies the coefficientwise enumerator (1) or minimum multiplicity (3), and (2) is **not claimed as original** here.

A recent exact study of **sunlet** graphs [4] gives minimum-function multiplicities for cycle bases; these are already known and form a covered special case of (3). The present claim is the full all-weight enumerator simultaneously for *every* base graph, including weight levels not addressed by [4]. Closely related published mathematical records [5] and [6] enumerate **restrained Italian** and **pointwise-minimal Roman** functions of leaf coronas, respectively; those have additional or different labeling conditions, so their statements do not imply (1). The possible recurrence of the same external-neighborhood statistic is not an identity of the enumerated classes.

## Limitations
The formula is an explicit sum over all base subsets, and does not yield a polynomial-time algorithm for arbitrary input graphs. Complexity of extracting coefficients from this transform is not settled here. The formula applies only to one private leaf per core vertex. Its minimum-weight identity is established prior work, and its sunlet minimum counts also have prior exact treatments. Unindexed papers or uninspected parts of the historical literature may contain equivalent all-weight results; priority is therefore provisional. The verification programs test only finite base orders, and independent mathematical audit has not yet been performed.

## References
1. P. Shao and C. Zhao, *Counting Weight-k Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1 (first public 2026-09-09), https://arxiv.org/abs/2610.00108.
2. F. Alizadeh, H. R. Maimani, L. Parsaei Majd and M. Rajabi Parsa, *Roman \(\{2\}\)-domination in graphs and graph products*, arXiv:1701.01416 (first public 2017-01-05), Theorem 3.2, https://arxiv.org/abs/1701.01416.
3. R. Hernández-Ortiz, L. P. Montejano and J. A. Rodríguez-Velázquez, *Italian domination in rooted product graphs*, arXiv:2006.02124 (first public 2020-06-03), https://arxiv.org/abs/2006.02124.
4. *Exact minimum Italian-domination multiplicities of sunlet graphs*, accessible public mathematical record (2026-10-13), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-minimum-italian-domination-multiplicities-of-sunlet-graphs--9dede768c463.
5. *Restrained Italian domination polynomials of leaf coronas from induced boundary profiles*, accessible public mathematical record (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-restrained-italian-domination-polynomials-of-leaf-coronas-from-i--fa69dce458b7.
6. *A neighborhood enumerator for pointwise-minimal Roman functions on one-leaf coronas*, accessible public mathematical record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-neighborhood-enumerator-for-pointwise-minimal-roman-functions--15936ceec4cf.
