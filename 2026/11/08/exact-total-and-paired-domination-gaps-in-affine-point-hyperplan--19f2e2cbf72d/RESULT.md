# Exact total and paired domination gaps in affine point–hyperplane incidence graphs

## Finding
Let \(q\) be any prime power and \(d\ge2\). Let \(G_{d,q}\) be the bipartite incidence graph whose vertices are the points and affine hyperplanes of \(\operatorname{AG}(d,q)=\mathbb F_q^d\), with incidence as adjacency. Then
\[
\gamma_t(G_{d,q})=d(q-1)+q+1,\qquad
\gamma_{\mathrm{pr}}(G_{d,q})=2d(q-1)+2.
\]
Consequently the exact paired-over-total domination premium is
\[
\gamma_{\mathrm{pr}}(G_{d,q})-\gamma_t(G_{d,q})=(d-1)(q-1).
\]
Both minima are attained by explicit coordinate configurations. The gap grows without bound either with the dimension or with the field size. This is an exact determination, not a claim that the affine blocking-number bound used in the proof is new.

## Assumptions and scope
A *total dominating set* \(S\) of a simple graph is one in which every vertex, including every member of \(S\), has a neighbor in \(S\). A *paired dominating set* is a dominating set \(S\) whose induced graph has a perfect matching. Every paired dominating set is total dominating. The quantities \(\gamma_t\) and \(\gamma_{\mathrm{pr}}\) are their minimum cardinalities.

A hyperplane is the solution set of \(a_1x_1+\cdots+a_dx_d=b\), with nonzero normal \(a\in\mathbb F_q^d\) and \(b\in\mathbb F_q\); proportional nonzero affine equations define the same vertex, counted only once. The ambient graph is the full point–hyperplane *incidence* graph, not a point graph, complement/nonincidence graph, or an incidence graph with a parallel class omitted. The theorem is asserted for every prime power \(q\), including extension fields, and integer \(d\ge2\). It is not asserted for arbitrary non-Desarguesian affine planes.

## Proof
Write \(P\subseteq\mathbb F_q^d\) for the point vertices of a total dominating set and \(\mathcal H\) for its hyperplane vertices. Every hyperplane, whether selected or not, must be incident with a selected point: a selected hyperplane itself needs a selected point-neighbor, and an unselected hyperplane also needs one. Hence \(P\) intersects every affine hyperplane. Likewise every point lies in some selected hyperplane. Conversely these two conditions give total domination. Thus the total domination problem separates into a point-blocking minimum and a hyperplane-cover minimum.

The Brouwer–Schrijver affine blocking theorem (1978, Theorem, in dimension \(d\)) states that any point set meeting every affine hyperplane in \(\operatorname{AG}(d,q)\) has at least \(d(q-1)+1\) points. This is the required non-elementary input, and its polynomial proof applies to prime-power fields. For the second minimum, each affine hyperplane has exactly \(q^{d-1}\) points, so covering all \(q^d\) points needs at least \(q\) hyperplanes. This is attained by the \(q\) parallel hyperplanes \(x_1=c\), \(c\in\mathbb F_q\).

Write \(0\) for the origin and \(e_i\) for coordinate unit vectors, and put
\[
B=\{0\}\cup\{ce_i:1\le i\le d,\ c\in\mathbb F_q^*\}.
\]
This set has \(d(q-1)+1\) points. For any affine hyperplane \(a\cdot x=b\), choose \(i\) with \(a_i\ne0\); then \((b/a_i)e_i\in B\) lies in that hyperplane. Thus \(B\) meets every hyperplane. Taking \(B\) together with the \(q\) hyperplanes \(x_1=c\) supplies a total dominating set with \(d(q-1)+q+1\) vertices, matching the lower bound.

Now let \(S\) be paired dominating, and write \(P\) and \(\mathcal H\) for its two selected parts. The perfect matching of the bipartite induced graph pairs each point with one hyperplane, hence \(|P|=|\mathcal H|\). Since paired domination implies total domination, the blocking bound gives \(|P|\ge d(q-1)+1\). Thus \(|S|\ge2d(q-1)+2\).

For equality, retain \(B\) and select the hyperplane family
\[
\mathcal H^*=\{x_1=c:c\in\mathbb F_q\}\ \cup\
\{x_i=c:2\le i\le d,\ c\in\mathbb F_q^*\}.
\]
Its cardinality is \(q+(d-1)(q-1)=d(q-1)+1\). Because it contains every \(x_1=c\), it covers all points; \(B\) meets every hyperplane, so \(B\cup\mathcal H^*\) dominates the graph. Moreover it has the explicit perfect matching: match \(ce_i\) to the hyperplane \(x_i=c\) for every \(c\ne0\) and every \(i\), and match \(0\) to \(x_1=0\). These are all selected vertices and all pairs are incident. The lower bound is therefore tight. Subtraction yields \((d-1)(q-1)\), completing the proof.

## Verification
The construction checker `verify_construct.py` builds the complete point–hyperplane incidence graph for prime-field test cases \((q,d)=(2,2),(3,2),(5,2),(7,2),(2,3),(3,3),(2,4),(3,4)\). It checks that the selected points meet every hyperplane, that selected hyperplanes cover all points, that every prescribed matching pair is incident and each vertex occurs exactly once, and that the displayed size and gap formulas hold. Results are recorded in `construction.out`.

An independent exhaustive program, `verify_exhaustive.py`, generates all point/line subsets and tests open-neighborhood domination and a recursively searched perfect matching for \(\operatorname{AG}(2,2)\) and \(\operatorname{AG}(2,3)\). It finds \((\gamma_t,\gamma_{\mathrm{pr}})=(5,6)\) and \((8,10)\), respectively, as recorded in `exhaustive.out`. These finite checks do not replace the published all-field blocking theorem or the symbolic construction.

Run `python3 verify_construct.py` and `python3 verify_exhaustive.py` using Python 3.8 or later; the latter program assumes ordinary modular arithmetic for its prime-field examples. The all-prime-power theorem is established by the mathematical proof, not by experiments limited to prime fields.

## Relationship to prior work
Brouwer and Schrijver proved the sharp minimum \(d(q-1)+1\) for affine hyperplane-blocking point sets (1978); this numerical blocking theorem is explicitly prior art and is used as a lemma. Haynes and Slater introduced paired domination and its basic relation to total domination (1998). Héger and Nagy studied *ordinary* dominating sets in incidence graphs of projective planes (arXiv:1603.02933, 2016), a different geometry and predicate, and discuss affine blocking sets as background. Adriaensen, Mattheus, and Spiro (2023/2024) study *edge* domination in incidence graphs and minimum maximal matchings, not the present vertex total/paired domination formulas. The assertion here is the sharp simultaneous pair of total and paired parameters on the full affine point–hyperplane incidence graphs, including the explicit matching witness and their exact gap. The statements are not inferred solely from a search failure; priority beyond the inspected sources remains subject to further literature review.

## Limitations
The blocking bound depends on the finite-field affine-space theorem; no corresponding assertion is made for arbitrary non-Desarguesian incidence structures. This result does not enumerate all minimum configurations, classify their exchange graphs, or establish a new general blocking-set bound. The original 1998 paired-domination article was accessible as a publisher abstract but not completely read; an earlier unindexed deduction of these exact incidence-graph formulas remains possible. No independent scholarly audit has been performed.

## References
1. A. E. Brouwer and A. Schrijver, “The Blocking Number of an Affine Space,” *Journal of Combinatorial Theory, Series A* 24 (1978), 251–253. Original open full text: https://ir.cwi.nl/pub/9858/9858D.pdf.
2. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F. Publisher records first online publication as 1998-12-07.
3. T. Héger and Z. L. Nagy, “Dominating sets in projective planes,” arXiv:1603.02933 (first posted 2016-03-09); *Journal of Combinatorial Designs* 25 (2017), 293–309.
4. S. Adriaensen, S. Mattheus, and S. Spiro, “Incidence-free sets and edge domination in incidence graphs,” *Journal of Combinatorial Designs* 32 (2024), 55–87. DOI: 10.1002/jcd.21925 (first posted 2023-11-23).
