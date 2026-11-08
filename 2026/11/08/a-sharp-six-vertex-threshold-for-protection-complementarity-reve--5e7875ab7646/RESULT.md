# A sharp six-vertex threshold for protection-complementarity reversal in directed habitat networks

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite simple directed graph with distinct permanently present source and target \(s,t\). Each other vertex survives independently with probability \(p\in(0,1)\); the target is viable if it is reachable from the source by a directed path whose internal vertices survive. For two distinct internal vertices \(u,v\), let \(F_G(S;p)\) denote the source-to-target reachability probability when, in addition, every internal vertex in \(S\) is perfectly protected. Define the joint protection interaction
\[
I_{uv}^G(p)=F_G(\{u,v\};p)-F_G(\{u\};p)-F_G(\{v\};p)+F_G(\varnothing;p).
\]

1. For **every directed graph with at most five vertices**, the sign of \(I_{uv}^G(p)\) cannot take both strictly positive and strictly negative values as \(p\) varies through \((0,1)\).
2. Among **six-vertex directed acyclic graphs**, every instance where this interaction assumes both signs has the exact form
\[
I_{uv}^G(p)=(1-p)^2(1-2p).
\]
There are exactly 24 such topologically labelled ordered-DAG/protected-unordered-pair cases in the complete census below. All switch at \(p=1/2\), from complementary protection at low survival to substitutable protection at high survival. In particular, six is the smallest possible network order for such a reversal, even if directed cycles are allowed for smaller networks.

The quantitative measure is the standard *joint reliability importance* mixed difference. The asserted mathematical contribution is its sharp directed **vertex-reachability realization threshold** and the six-vertex acyclic classification, not invention of the mixed difference itself.

## Assumptions and scope

The source and target are not random. The intervention makes either or both chosen intermediate vertices certainly present, but does not modify edges. All other intermediate vertices are independently present with the same probability \(p\). Edges do not fail; a directed source-to-target path of surviving intermediate vertices is sufficient for viability. Empty direct source-to-target paths are permitted; if the direct edge exists, reliability is already one and interaction zero. Graphs are finite, with no multiple edges and no self-loops. The order-five lower bound allows cycles. The exhaustive upper-bound classification is asserted only for acyclic six-vertex graphs.

Protection complements when \(I>0\) and substitutes when \(I<0\), as measured by the extra gain from protecting both rather than summing separate gains. The strict sign-reversal conclusion excludes endpoint values \(p=0,1\).

## Proof

**Conditioning identity.** Fix all intermediate random vertices except \(u,v\). For their Boolean states let \(g(a,b)\in\{0,1\}\) be source-to-target reachability. The conditional mixed difference is
\[
\delta=g(1,1)-g(1,0)-g(0,1)+g(0,0)\in\{-1,0,1\}.
\]
Multilinearity of independent Bernoulli survival gives
\[
I_{uv}^G(p)=(1-p)^2\,\mathbb E_p\delta,
\]
where the expectation is over all other internal vertices. This is because setting both reliabilities to one instead of their baseline \(p\) multiplies the usual reliability mixed derivative by \((1-p)^2\). Reachability is nondecreasing separately in every vertex state.

**At most five vertices.** Besides the two protected terminals and candidate vertices \(u,v\), there is at most one additional intermediate vertex \(w\). If none, the conditional \(\delta\) is constant. With \(w\) present, put \(\delta_0\), \(\delta_1\) for the mixed differences when \(w\) is respectively absent and present. Then
\[
I_{uv}^G(p)=(1-p)^2((1-p)\delta_0+p\delta_1).
\]
A strict sign reversal would force \(\delta_0=1,\delta_1=-1\) or the reverse. The reverse is impossible by monotonicity in \(w\): \(\delta_0=-1\) forces \(g(u,v,0)=u\lor v\) and \(\delta_1=1\) forces \(g(u,v,1)=u\land v\), contradicting monotonicity at assignments with just one of \(u,v\) present. The remaining possibility forces the *majority-of-three* Boolean viability function
\[
g(u,v,w)=(u\land v)\lor(u\land w)\lor(v\land w).
\]
This Boolean function cannot be represented as directed \(s\)-to-\(t\) vertex reachability using exactly these three intermediate vertices. There is no viable path with only one intermediate vertex. Write \(L\) for intermediate vertices with an edge from \(s\), and \(R\) for those with an edge into \(t\). Then \(L\cap R=\varnothing\). Yet viability with each of the three unordered pairs of intermediates requires that pair to contain at least one vertex of \(L\) and at least one of \(R\); a source-to-target path using exactly a pair has two intermediate vertices. This would properly two-color all three edges of a triangle, impossible. The argument works even when the full directed network has cycles. Thus no order-five sign reversal is possible.

**A six-vertex witness.** Take vertices \(0,1,2,3,4,5\), protected terminals \(s=0,t=5\), and directed edges
\[
0\to1,\ 0\to3,\ 1\to2,\ 1\to4,\ 2\to5,\ 3\to4,\ 4\to5.
\]
Protect \(u=1,v=4\). The reliability Boolean function of the four intermediate states is exactly
\[
g=x_1x_2\lor x_1x_4\lor x_3x_4.
\]
Conditioning on \((x_2,x_3)=(0,0),(1,0),(0,1),(1,1)\), the mixed differences in \(x_1,x_4\) are respectively \(1,0,0,-1\). Thus
\[
I_{1,4}(p)=(1-p)^2[(1-p)^2-p^2]=(1-p)^2(1-2p).
\]
For heterogeneous baseline reliabilities \(q_1,q_4,a,b\) at the four internal vertices, the same witness has
\[
I_{1,4}=(1-q_1)(1-q_4)(1-a-b).
\]
Hence the threshold persists on the exact hyperplane \(a+b=1\), independently of the two candidate vertices' baseline reliabilities, provided those reliabilities are below one.

**Complete six-vertex acyclic classification.** Any directed acyclic source-to-target network has the same reachability function after deleting irrelevant edges entering \(s\) or leaving \(t\); the remaining intermediates admit a topological order. So it suffices to enumerate all subgraphs of the 15 possible forward edges in the fixed order \(0<1<2<3<4<5\), with \(s=0,t=5\), and the six unordered pairs of four internal vertices. This is \(2^{15}\cdot6=196608\) exhaustive graph-and-pair cases. For each, fix the two candidate vertices in the four possible on/off states and compute the conditional mixed difference \(d_{ab}\) for the two remaining internal vertices. The interaction polynomial is
\[
I_{uv}^G(p)=(1-p)^2\{d_{00}(1-p)^2+(d_{10}+d_{01})p(1-p)+d_{11}p^2\}.
\]
The accompanying independent-Python-standard-library verifier enumerates all cases, computes exact integer coefficients, tests the quadratic's extrema exactly using rational arithmetic, and obtains 18 distinct coefficient triples. Exactly 24 cases exhibit strict sign reversal, **all** with triple \((d_{00},d_{10}+d_{01},d_{11})=(1,0,-1)\). This proves the universal six-vertex acyclic formula and completes the theorem.

## Verification

Run the standalone `verify.py` with Python 3. It exhausts 32768 topologically labelled DAGs and six candidate pairs per DAG, builds Boolean reachability functions by forward propagation, derives all exact Bernstein coefficient triples, and checks the strict reversal condition using rational extrema. Its assertions establish the counts \(18\) and \(24\) stated above, and the unique switching triple \((1,0,-1)\). A separate breadth-first search verifies all 64 Boolean configurations of the witness against the independent monomial formula. It also checks 24 heterogeneous rational reliability settings against the closed form. The theoretical order-five lower bound does not depend on a finite experiment.

The verifier does not enumerate cyclic six-vertex graphs and therefore establishes no corresponding cyclic six-vertex classification. It also does not claim that a catalogue search proves priority.

## Relationship to prior work

Evans, Pocock and Memmott (2013) motivate robustness to loss of habitat and study multilevel ecological networks; their model uses sequential habitat-loss scenarios rather than this exact conditional two-site intervention interaction. Wu (2005), building on Armstrong and Hong–Lie, defines joint reliability importance via precisely the underlying mixed difference for general coherent systems. Therefore **sign-switching mixed differences are not new in general coherent-system reliability**: the narrower novelty being tested here is the sharp directed *vertex-reachability* minimum and its exhaustive six-vertex DAG profile. Hong and Lie (1993) concern joint reliability importance for *edges in undirected networks*, not automatically the present node-reachability cutoff. The 2002 k-out-of-n work supplies additional reason to avoid claiming novelty for majority-function switching in the abstract. A systematic priority review should still inspect previously unavailable complete network-reliability and graph-realization literature.

## Limitations

The theorem assumes independent survival for unprotected habitats, flawless edges and perfect protection. Acyclicity is required only for the six-vertex universal profile classification, not the five-vertex impossibility. The result is a structural reliability benchmark rather than a verified ecological intervention recommendation. Joint reliability importance itself is established prior art; originality of the exact graph-theoretic cutoff remains provisional pending wider specialized historical literature inspection. No independent audit has been conducted.

## References

- Evans, D. M., Pocock, M. J. O., and Memmott, J. (2013). *The robustness of a network of ecological networks to habitat loss*, Ecology Letters 16, 844–852. First online publication 2013-05-21. DOI: https://doi.org/10.1111/ele.12117. Author manuscript: https://nora.nerc.ac.uk/id/eprint/504615/1/N504615PP.pdf.
- Wu, S. (2005). *Joint importance of multistate systems*, Computers & Industrial Engineering 49, 63–75. DOI: https://doi.org/10.1016/j.cie.2005.02.001. Open repository manuscript: https://kar.kent.ac.uk/31025/1/JointImportance.pdf.
- Hong, J. S., and Lie, C. H. (1993). *Joint reliability-importance of two edges in an undirected network*, IEEE Transactions on Reliability 42, 17–23. DOI: https://doi.org/10.1109/24.210266.
- Hong, J. S., Koo, S. R., and Lie, C. H. (2002). *Joint reliability importance of k-out-of-n systems*, European Journal of Operational Research 142, 539–547. DOI: https://doi.org/10.1016/S0377-2217(01)00306-X.
