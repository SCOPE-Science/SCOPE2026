# Degree-profile collapse and the sharp six-parameter collision in Henson triangle-avoidance spectra

## Finding
Let \(a,b,c\ge1\). Let \(F\subseteq K_{a,b}\) be a bipartite *deleted-edge pattern* with shores \(A,B\), and let \(G_F\) be the graph obtained from the complete tripartite graph \(K_{a,b,c}\) by deleting exactly the edges of \(F\) between \(A\) and \(B\). Regard the vertices of \(G_F\) as individually named parameters in the countable homogeneous \(K_4\)-free Henson graph. Let \(P_F(z)\) count complete nonalgebraic one-point types by the number of named neighbors of the new point.

Put \(m=|E(F)|\), \(d_F(v)=\deg_F(v)\), and
\[
D_F(z)=(1+z)^a+(1+z)^b-1
 +z\sum_{v\in A\cup B}\bigl((1+z)^{d_F(v)}-1\bigr)-mz^2.
\]
Then the exact identity for every deleted-edge pattern is
\[
\boxed{P_F(z)=(1+z)^{a+b}+((1+z)^c-1)(D_F(z)+R_F(z)),}
\]
where
\[
R_F(z)=\sum_{\substack{\varnothing\ne S\subseteq A,\ \varnothing\ne T\subseteq B\\ |S|\ge2,\ |T|\ge2,\ S\times T\subseteq E(F)}} z^{|S|+|T|}.
\]
In particular, \(R_F=0\) **if and only if** \(F\) contains no four-cycle. If \(F\) contains \(q_4(F)\) four-cycles, the first coefficient in which the exact polynomial differs from its degree-profile part is the coefficient of \(z^5\), and that difference is exactly \(c q_4(F)\). Thus the four-cycle is the precise first obstruction to degree-only counting.

For fixed \((a,b,c)\), among four-cycle-free patterns, \(P_F=P_{F'}\) holds **if and only if** \(F,F'\) have the same *combined (uncoloured) multiset of vertex degrees*, including degree zero. This is a complete numerical-fibre classification in that natural family.

The first failure of reconstruction for fixed shore sizes occurs with \(a+b=5\) deleted-edge-pattern vertices, and is unique (up to within-shore relabelling) for \((a,b)=(2,3)\): take \(F_A\) to be the two-edge star centered in the two-vertex shore, and \(F_B\) the two-edge star centered in the three-vertex shore. Both have degree multiset \(\{2,1,1,0,0\}\); the resulting connected nonisomorphic old parameter graphs have exactly the same type polynomial for every \(c\ge1\), namely
\[
\boxed{P_{F_A}(z)=P_{F_B}(z)
=(1+z)^5+((1+z)^c-1)(1+5z+6z^2+2z^3).}
\]
For \(c=1\), this is \(1+6z+15z^2+16z^3+7z^4+z^5\), with 46 nonalgebraic singleton types. For arbitrary \(c\), the common total is \(18+14\cdot2^c\), giving collisions among connected parameter graphs at every order \(5+c\ge6\). Their degree sequences differ, and even the sum of cubes of their graph degrees differs by exactly six.

## Assumptions and scope
All graphs are simple, finite, undirected, and loopless. The three vertex shores \(A,B,C\) are independent, of respective sizes \(a,b,c\ge1\), and every cross edge is present except those in \(F\subseteq A\times B\). The degree sequence of \(F\) means the combined multiset across both shores, not the ordered pair of side-specific degree lists. Four-cycle-free is in the ordinary not-necessarily-induced sense; a four-cycle in a bipartite graph is a copy of \(K_{2,2}\). Every \(G_F\) is \(K_4\)-free, so it is a valid parameter graph. The reconstruction threshold is relative to fixed shore sizes \((a,b,c)\); it does not assert a global first collision across unrelated decompositions.

## Proof
**1. Convert extension types into subsets.** In the homogeneous \(K_4\)-free graph, a nonalgebraic one-point neighborhood over a finite named parameter graph is possible precisely if its induced graph contains no triangle. Necessity follows because a triangle with the new point creates a \(K_4\). Sufficiency follows by freely adjoining the new point with precisely those neighbors and using the Henson extension property. Homogeneity identifies exactly one complete type with each possible neighborhood. This criterion is standard, not an originality claim here.

**2. Separate the third shore.** Any subset avoiding \(C\) is triangle-free because \(G_F[A\cup B]\) is bipartite; it contributes \((1+z)^{a+b}\). If the subset meets \(C\), then every selected cross pair \((u,v)\in A\times B\) must be a deleted edge: an undeleted pair makes a triangle with each selected vertex in \(C\). Conversely, if all selected \(A\)-to-\(B\) pairs are deleted, no triangle can occur. There are \((1+z)^c-1\) weighted ways to choose a nonempty portion of \(C\). Thus the second factor is the bipartite rectangle enumerator
\[
Q_F(z)=\sum_{\substack{S\subseteq A,\ T\subseteq B\\ S\times T\subseteq E(F)}} z^{|S|+|T|}.
\]

**3. Exact star-versus-rectangle decomposition.** The cases \(S=\varnothing\) or \(T=\varnothing\) contribute \((1+z)^a+(1+z)^b-1\). Among nonempty pairs, count those with \(|S|=1\) by choosing the unique vertex in \(A\), and those with \(|T|=1\) symmetrically. The two counts overlap on each deleted edge, exactly once, giving \(-mz^2\). The remaining terms are exactly \(R_F\). This proves the boxed formula. If a term occurs in \(R_F\), choosing two vertices from each of \(S,T\) exhibits a four-cycle. Conversely every four-cycle contributes the positive monomial \(z^4\). Hence \(R_F=0\) exactly when \(F\) is four-cycle-free, and \([z^4]R_F=q_4(F)\). The multiplier \((1+z)^c-1\) begins with \(cz\), proving the sharp \(z^5\) correction.

**4. Prove the complete degree-fibre equivalence.** Suppose \(F\) is four-cycle-free. Given \((a,b,c)\) and \(P_F\), polynomial division by the known nonzero factor \((1+z)^c-1\) recovers \(D_F\). Its \(z^2\) coefficient is \(\binom a2+\binom b2+m\), so it recovers \(m\). Consequently it recovers
\[
\sum_{v\in A\cup B}(1+z)^{d_F(v)}
=a+b+\frac{D_F(z)-((1+z)^a+(1+z)^b-1)+mz^2}{z}.
\]
After substituting \(y=1+z\), the right side is \(\sum_v y^{d_F(v)}\), whose coefficients uniquely recover the complete degree multiset. The converse is immediate from the displayed expression for \(D_F\).

**5. Establish sharpness and nonisomorphism.** For \(a+b\le4\), the four-cycle-free bipartite patterns are classified by their degree multiset up to relabelling within each shore (and exchange of shores when equally sized). This is a finite assertion; the standalone checker exhausts every labelled pattern for all such shore sizes, compares the canonical permutations, and confirms it without an assumed classification table. At \((a,b)=(2,3)\), let \(A=\{a_0,a_1\}\), \(B=\{b_0,b_1,b_2\}\), and set \(E(F_A)=\{a_0b_0,a_0b_1\}\), \(E(F_B)=\{a_0b_0,a_1b_0\}\). Both patterns are four-cycle-free and have combined degree multiset \(\{2,1,1,0,0\}\), hence the same displayed polynomial. For fixed \(c\), the degrees in \(G_{F_A}\) are \(c+1\) three times, \(c+2\) once, \(c+3\) once, and \(5\) a total of \(c\) times; those in \(G_{F_B}\) are \(c\) once, \(c+2\) four times, and \(5\) a total of \(c\) times. The difference of sums of cubed degrees is
\[
3(c+1)^3+(c+3)^3-3(c+2)^3-c^3=6.
\]
Thus the parameter graphs are nonisomorphic for *every* \(c\ge1\). They are connected because the nonempty shore \(C\) is adjacent to all of \(A\cup B\). Enumerating all the five-vertex deleted patterns gives this unique new fibre at \((a,b)=(2,3)\); this last uniqueness statement is a complete finite enumeration, not extrapolation to larger patterns.

## Verification
Run the standalone Python-standard-library script `verify_degree_collapse.py`. It constructs each parameter graph from its actual edges and directly enumerates all possible new-point neighborhoods, rejecting triangles by testing every selected triple. Independently it computes the formula from missing-edge degrees; it checks all labelled patterns on shores of total size at most five (220 instances after taking \(c=1,2\)), including 22 instances with four-cycle corrections. It canonically tests the small bipartite patterns under all shore permutations and verifies absence of earlier nontrivial fibres. It also directly enumerates both witnesses for \(1\le c\le7\), verifies their full polynomials and totals, and checks the initial four-cycle boundary. The expected output in `verification_output.txt` ends with `VERIFY_OK` on its one line. These finite checks verify the implementation and finite threshold; the all-size polynomial statements follow from the proof, not extrapolation.

## Relationship to prior work
Conant's 2014 exposition of generic \(K_n\)-free Henson graphs, and the published *Exact finite-parameter 1-type counting in Henson graphs is #P-complete*, provide the general homogeneous-graph extension criterion and its clique-free-subset polynomial interpretation; both are credited. They do not assert the sharp four-cycle boundary or the degree-fibre classification for missing-edge tripartite bases. The published *Forest defects in multipartite clique-avoidance* establishes a homotopy classification of clique-free complexes under forest deletions; its proof was inspected in full and concerns homotopy type and persistence, not the graded face-enumeration and inverse degree-fibre theorem here. Its suspension reduction is compatible with, but does not imply, this cardinality-polynomial reconstruction statement: homotopy equivalent complexes can have different face counts. The established observation that a bipartite four-cycle-free graph has only star bicliques is used explicitly, not claimed as a new lemma. Work on biclique covers such as Otsuki and Hirata (2015) addresses biclique-cover optimisation rather than these one-type polynomials. No mathematical priority claim is made for the elementary star-biclique observation alone.

## Limitations
The inverse theorem requires the three shore sizes as part of its scope and the missing-edge graph to be four-cycle-free. For patterns with four-cycles, additional complete bipartite subgraphs contribute \(R_F\) and degree multisets no longer suffice for the displayed degree-only formula. The first-collision threshold is relative to fixed shore sizes; the family may have other coincidences under different parameter decompositions. Equality of a graded polynomial does not mean equality of labelled types, and the finding does not cover arbitrary parameter graphs or tuple types. Historical originality is provisional because obscure equivalent treatments of biclique enumeration or independent-set polynomial collisions may exist; independent mathematical audit has not been performed.

## References
1. G. Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570, first public 2014-01-08, https://arxiv.org/abs/1401.1570 .
2. *Exact finite-parameter 1-type counting in Henson graphs is #P-complete*, published finding, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650 .
3. *Forest defects in multipartite clique-avoidance: a shape-invariant sphere-wedge law and an integral persistence transition*, published finding, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-forest-defects-in-multipartite-clique-avoidance-a-shape-invarian--636cc79caa35 .
4. H. Otsuki and T. Hirata, *The biclique cover problem and the modified Galois lattice*, IEICE Transactions on Information and Systems E98-D (2015), 497–502, https://doi.org/10.1587/transinf.2014FCP0019 .
