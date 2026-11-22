# Sharp rare-obstruction counts for strong resolving hop domination on binary cubes

## Finding
Let \(Q_d\) be the binary Hamming cube on \(\{0,1\}^d\), with \(d\ge2\). A strong resolving hop dominating set is a set that strongly resolves every vertex pair and has a selected vertex at graph distance exactly two from every unselected vertex. Let \(B_d\) be the number of minimum such sets on the fixed, labeled vertex set.

The minimum size is \(2^{d-1}\). Every minimum set is exactly one choice from each complementary (antipodal) vertex pair, subject to a local forbidden-pattern condition: its unselected complement \(T\) contains no complete closed Hamming-distance-two neighborhood
\[
D_2(v)=\{v\}\cup\{w:d_H(v,w)=2\}.
\]

The first values, including the sharp small-dimension exceptions, are
\[
(B_2,B_3,B_4,B_5,B_6)=(4,14,256,64830,4290774016),
\qquad B_6=(2^{16}-32)^2.
\]
In dimension five, the number \(65536-B_5=706\) of excluded antipodal transversals is governed by the open-neighborhood complex of the \(5\)-regular Clebsch graph. This particular face count is already available in prior work and is used here as an auxiliary boundary check, not claimed as an independently new Clebsch census.

Writing \(m=\binom d2\), the genuinely infinite counting statement is the following **sharp two-order asymptotic**:
\[
\frac{B_d}{2^{2^{d-1}}}
=1-2^{d-m-1}+m\,2^{3d-2m-5}
+O\!\left(2^{2d-2m+3}+2^{9d-3m-9}\right)
\quad(d\to\infty).
\]
In particular, the displayed positive correction \(m2^{3d-2m-5}\) is asymptotically larger than the entire stated error, and \(B_d/2^{2^{d-1}}\to1\). Both the first and second correction coefficients are explicit and sharp. More quantitatively, for every \(d\ge8\), the absolute difference between the left side and the first three terms on the right is bounded by the sum of the two powers of two inside the big-\(O\) term.

## Assumptions and scope
The cube has its usual shortest-path distance \(d_H(x,y)\), the Hamming distance. A vertex \(w\) strongly resolves \(x,y\) if \(x\) lies on a shortest \(w\)-to-\(y\) path or \(y\) lies on a shortest \(w\)-to-\(x\) path. The hop condition uses **exactly** distance two, not at most two. All configurations are distinct labeled vertex subsets; antipodal pairs are \(\{x,\overline x\}\), where \(\overline x\) flips every coordinate. The asymptotic is for integer dimensions tending to infinity. The case \(d=1\) is intentionally excluded because no vertices are distance two apart.

## Proof
**1. Minimum size and exact characterization.** For an antipodal pair \(x,\overline x\), a strong resolver must be one of its endpoints: if \(w\) strongly resolves the pair, a shortest-path equality involves their full diameter \(d\), forcing \(w=x\) or \(w=\overline x\). Every strong resolving set therefore meets all \(2^{d-1}\) antipodal pairs.

Conversely, if \(S\) meets each antipodal pair and two vertices \(x,y\) are both outside \(S\), then \(\overline x\in S\). Every vertex \(y\) lies on some shortest path from \(x\) to \(\overline x\), so \(\overline x\) strongly resolves \(x,y\). Pairs with a selected endpoint are trivially resolved. Thus any antipodal transversal is strong resolving. The coordinate half-cube \(S=\{x:x_1=0\}\) is such a transversal, and each excluded vertex has a selected vertex at distance exactly two by flipping coordinate one and any other coordinate. Hence the sharp minimum is \(2^{d-1}\). For a minimum set with complement \(T\), hop domination fails exactly when there exists \(v\in T\) with \(D_2(v)\subseteq T\), proving the forbidden-pattern characterization.

**2. Dimensions two, three and four.** At \(d=2\), the antipode of each excluded vertex supplies its distance-two witness, giving four good transversals. For \(d=3\), the distance-two graph restricted to each four-vertex parity class is complete: only the two transversals that are whole parity classes fail, yielding \(2^4-2=14\). For \(d=4\), antipodes preserve parity and every transversal has exactly four excluded vertices in each parity class, fewer than the six distance-two neighbors of any vertex; all \(2^8=256\) transversals work.

**3. Dimension five and the Clebsch incidence relation.** In odd dimension, antipodes exchange parity. Let \(E\) be the sixteen even-weight five-bit words and identify a transversal \(T\) with \(U=T\cap E\): its odd members are precisely the complements of points in \(E\setminus U\). On \(E\), let \(C\) join words at Hamming distance four; \(C\) is the Clebsch graph, with parameters \((16,5,0,2)\). Its open neighborhood \(N_C(v)\) consists of the five words at distance four from \(v\), so \(D_2(v)\cap E=E\setminus N_C(v)\). The forbidden condition is therefore equivalent to either \(U\) or \(E\setminus U\) being contained in the open neighborhood of some vertex of \(C\).

The numbers of distinct subsets of a Clebsch open neighborhood by size zero through five are \((1,16,80,160,80,16)\). Indeed, there are sixteen neighborhoods of size five; two distinct neighborhoods meet in zero or two points, so subsets of size at least three belong to a unique neighborhood; pairs belong to exactly two neighborhoods precisely when they are nonadjacent, and there are eighty such pairs. There are \(353\) subsets in total, including the empty set. The two excluded types, \(U\) small and \(E\setminus U\) small, are disjoint, proving \(B_5=2^{16}-2(353)=64830\). This \(352\)-nonempty-face incidence census is credited to the existing Clebsch neighborhood-complex calculation.

**4. Dimension six.** Antipodes preserve parity. Each parity class has thirty-two vertices and sixteen antipodal pairs, so choices on the two classes are independent. For any vertex \(v\), \(D_2(v)\) has \(1+\binom62=16\) vertices, exactly one from every antipodal pair in the same parity class: distances to \(v\) in an antipodal pair add to six and are either \((0,6)\) or \((2,4)\). Thus a bad transversal of that parity class must equal \(D_2(v)\). The thirty-two choices of \(v\) give distinct forbidden transversals (their pairwise neighborhood intersections have size at most ten). Each parity class therefore has \(2^{16}-32\) valid choices, proving \(B_6=(2^{16}-32)^2=4290774016\).

**5. Two sharp orders in the all-dimensional count.** Choose \(T\) uniformly among the \(2^{2^{d-1}}\) antipodal transversals and put \(m=\binom d2\), \(L=m+1\). For each cube vertex \(v\), write \(A_v=\{D_2(v)\subseteq T\}\). When \(d\ge5\), the \(L\) elements of \(D_2(v)\) occupy distinct antipodal pairs, hence \(\Pr(A_v)=2^{-L}\). The first inclusion-exclusion sum is
\[
\Sigma_1=2^d2^{-L}=2^{d-m-1}.
\]
For distinct centers at Hamming distance \(r\), elementary two-coordinate-flip counting gives
\[
|D_2(v)\cap D_2(w)|=
\begin{cases}
2d-2,&r=2,\\
6,&r=4,\\
0,&\text{otherwise}.
\end{cases}
\]
For \(d\ge7\), the union of the two sets at center distance two contains no antipodal pair: for odd \(d\) the union has one parity, while for even \(d\ge8\), an antipodal conflict would imply \(d-2\le4\), impossible. Therefore each such pair has joint probability \(2^{-2L+2d-2}=2^{-2m+2d-4}\). There are \(2^{d-1}m\) unordered center pairs at distance two, contributing
\[
\mu_d=m2^{3d-2m-5}.
\]
For all other center pairs, the joint probability is at most \(2^{-2L+6}=2^{-2m+4}\) (and zero if a conflicting antipodal pair occurs). There are fewer than \(2^{2d-1}\) pairs in total, so the remaining second-sum contribution \(R_2\) obeys
\[
0\le R_2\le2^{2d-2m+3}.
\]
For any three distinct centers, the union of their closed distance-two neighborhoods has at least \(3L-3(2d-2)=3m-6d+9\) vertices, since two different neighborhoods intersect in at most \(2d-2\) vertices. A consistent union fixes that many independent antipodal choices, and an inconsistent union has probability zero. With fewer than \(2^{3d}\) unordered triples, the third inclusion-exclusion sum satisfies
\[
0\le\Sigma_3\le 2^{9d-3m-9}.
\]
The first three Bonferroni inequalities yield
\[
\left|\Pr(T\text{ has no forbidden pattern})-
(1-\Sigma_1+\mu_d)\right|
\le R_2+\Sigma_3
\le2^{2d-2m+3}+2^{9d-3m-9}.
\]
Dividing either bound by \(\mu_d\) gives terms bounded respectively by \(2^{8-d}/m\) and \(2^{6d-m-4}/m\), both tending to zero as \(d\to\infty\). This proves the quantitative estimate and the genuinely sharp second correction.

## Verification
The standalone standard-library programs `verify_small.py` and `verify_structure.py` reconstruct antipodal choices and Hamming neighborhoods without relying on stored graph tables. Run `python verify_small.py` and `python verify_structure.py` from the extracted artifact directory. The first directly checks strong resolution for every antipodal basis through dimension four, then enumerates all \(65536\) choices in dimension five and the \(65536\) parity-side choices in dimension six. The second reconstructs the Clebsch strongly regular parameters, neighborhood face counts, all closed-distance-two pair-intersection formulas through dimension ten, and the thirty-two forbidden parity-side transversals in dimension six. Expected outputs are embedded separately in `verification_outputs.txt`.

## Relationship to prior work
Mohamad and Rara (2023) define strong resolving hop domination and study joins, coronas and lexicographic products, not the Cartesian-power cube optimum census or its rare-event expansion. Earlier strong-metric-dimension literature treats antipodal bases without the simultaneous hop condition. The known \(352\) nonempty faces in the Clebsch open-neighborhood complex are mathematically sufficient to recover the auxiliary dimension-five count once the parity reduction above is supplied; that count alone is **not** an original result. The new combined statement is the exact strong-resolving-hop threshold and structural forbidden-pattern reduction, the dimension-six census, and particularly the two-term all-dimension rarity theorem with the explicit next coefficient. No searched covering statement implies that entire claim.

## Limitations
The second-order expansion is an asymptotic result, not a closed formula for \(B_d\) in every dimension. The exact finite counts are limited to dimensions two through six, and no exact count is claimed for dimension seven or higher. The error bound may be numerically weak in early dimensions even though it is asymptotically smaller than the second term. Publication-priority checks cannot exhaust unpublished or poorly indexed equivalences; independent mathematical review has not occurred.

## References
1. J. S. Mohamad and H. M. Rara, “Strong Resolving Hop Domination in Graphs,” *European Journal of Pure and Applied Mathematics* 16 (2023), 131–143, DOI: https://doi.org/10.29020/nybg.ejpam.v16i1.4578, public 2023-01-29.
2. J. A. Rodríguez-Velázquez, I. G. Yero, D. Kuziak and O. R. Oellermann, “On the strong metric dimension of Cartesian and direct products of graphs,” arXiv:1307.4722 (2013), https://arxiv.org/abs/1307.4722.
3. “The \(5\)-regular Clebsch neighborhood complex is a wedge of \(31\) \(2\)-spheres,” openly accessible research record at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a, including its pre-existing \(352\)-nonempty-face census; used solely for the covered dimension-five face count.
