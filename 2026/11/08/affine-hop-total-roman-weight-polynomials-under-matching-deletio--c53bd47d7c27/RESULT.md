# Affine hop-total-Roman weight polynomials under matching deletion from complete bipartite graphs

## Finding
For any integers \(a,b\ge3\) and \(0\le t\le\min\{a,b\}\), let \(G_{a,b,t}=K_{a,b}\setminus tK_2\) be a labelled complete bipartite graph after deletion of any matching of size \(t\). Define the hop-total-Roman weight enumerator
\[
P_{a,b,t}(z)=\sum_{f\text{ admissible}} z^{\sum_{v\in V(G_{a,b,t})}f(v)}.
\]
Set, for each integer \(s\ge3\),
\[
F_s(z)=(1+z+z^2)^s-(1+z)^s+z^s,
\qquad
H_s(z)=(z+z^2)(1+z+z^2)^{s-1}-z(1+z)^{s-1}+z^s.
\]
Then the **full weight polynomial**, not just the least weight, obeys the affine deletion law
\[
\boxed{P_{a,b,t}(z)=F_a(z)F_b(z)-tz^2\bigl(H_a(z)+H_b(z)\bigr)+tz^4.}
\]
In particular, \(\gamma_{htR}(G_{a,b,t})=4\), and the number of optimal functions is exactly \(ab-t\). The total number of admissible functions is
\[
\boxed{P_{a,b,t}(1)=(3^a-2^a+1)(3^b-2^b+1)-t\bigl(2\cdot3^{a-1}-2^{a-1}+2\cdot3^{b-1}-2^{b-1}+1\bigr).}
\]
Furthermore, for each integer \(k>2\max\{a,b\}+2\), the coefficient \([z^k]P_{a,b,t}(z)\) does not depend on \(t\). Thus an arbitrary disjoint-edge deletion changes the full spectrum only in an explicitly bounded range, with a universal correction for each deleted edge.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The two vertex classes have sizes \(a\) and \(b\), each at least three. The matching edges removed have distinct endpoints. A function \(f:V(G)\to\{0,1,2\}\) is **hop-total-Roman** if (i) for every vertex \(x\) with \(f(x)=0\), some vertex \(y\) with \(f(y)=2\) has graph distance \(d_G(x,y)=2\); and (ii) the subgraph induced on the positive-labelled vertices has minimum degree at least one. Each labelled function is counted once and contributes its weight as an exponent. The graph is connected in the stated range. The symbol \(z\) is formal; no analytic convergence is involved.

## Proof
**Distance-two reduction.** Every pair of distinct vertices within the first class has a common neighbor in the second class: together they exclude at most two of its \(b\ge3\) vertices. The reverse statement holds using \(a\ge3\). Thus any distinct two vertices in the same class are at distance two. Vertices in opposite classes can never be at distance exactly two, by bipartiteness. Hence condition (i) decouples between the two classes: within each class either all labels are positive, or at least one vertex has label \(2\). This condition also ensures that each class has nonempty positive support.

**One-class polynomials.** For a class of size \(s\), all ternary labelings contribute \((1+z+z^2)^s\). Invalid labelings for condition (i) are those using only labels \(0,1\) with at least one zero, of weight polynomial \((1+z)^s-z^s\). Their removal gives \(F_s\). For a specified vertex \(x\) required to be positive, begin with \((z+z^2)(1+z+z^2)^{s-1}\), subtract the labelings having no \(2\) and at least one zero, with polynomial \(z(1+z)^{s-1}-z^s\), to obtain \(H_s\).

**Exactly which supports fail totality.** Let \(U,W\) denote the positive supports in the two classes; both are nonempty. The graph induced on \(U\cup W\) is the complete bipartite graph between \(U,W\), apart from those edges in the deleted matching whose endpoints are both positive. A positive vertex can have no positive neighbor only if the opposite support consists of its unique missing matched neighbor. Therefore, for each deleted pair \((x,y)\), the bad functions arising from that pair are precisely the union of two events: \(U=\{x\}\) and \(y\in W\), or \(W=\{y\}\) and \(x\in U\). Because the class sizes are at least three, if a class has singleton positive support, its unique positive vertex must carry label \(2\) to protect all zeros in that class. Thus the two events have respective weight polynomials \(z^2H_b(z)\) and \(z^2H_a(z)\). Their intersection consists of the unique labelling with only \(x\) and \(y\) positive, both labelled \(2\), and contributes \(z^4\). Since distinct deleted pairs share no endpoints, none of these bad-event unions intersects another: the singleton support or its required positive partner would have to be different. Inclusion-exclusion for the \(t\) disjoint bad-event unions gives the displayed full polynomial.

**Extrema and affine defect.** The one-class polynomial has no terms below degree two, and for \(s\ge3\) its coefficient of degree two is exactly \(s\): the only such labelings select one \(2\) and label all other vertices zero. The coefficient of degree two in \(H_s\) is \(1\). Consequently the least possible total weight is \(4\), with coefficient \(ab-t\), which is positive since \(a,b\ge3\) and \(t\le\min\{a,b\}\). Evaluating \(F_s(1)=3^s-2^s+1\) and \(H_s(1)=2\cdot3^{s-1}-2^{s-1}+1\) proves the count of all functions. Finally \(\deg H_s=2s\), so the deletion correction has degree \(2\max\{a,b\}+2\), proving the claimed high-weight stability. The proof is uniform for all stated parameters. \(\square\)

## Verification
The provided standalone file `verify_hop_tr.py` uses only the Python standard library. For each of 28 parameter profiles \(3\le a\le b\le5\) and \(0\le t\le a\), it constructs the graph, independently computes all graph distances with breadth-first search, enumerates every ternary vertex labelling, tests both original conditions, and compares the resulting entire polynomial coefficient-by-coefficient with a separate integer-polynomial implementation of the closed formula. In total it inspects 523,422 labelings. The executable finishes with `VERIFY_OK profiles=28 labels=523422 valid=376483 independent_shortest_paths=PASS full_integer_polynomials=PASS linear_matching_defect=PASS minimum_placements=PASS`. These finite tests corroborate the theorem but do not replace the all-parameter proof.

For example, \(P_{3,3,0}(z)=9z^4+42z^5+85z^6+102z^7+84z^8+50z^9+21z^{10}+6z^{11}+z^{12}\); deleting a perfect matching yields \(P_{3,3,3}(z)=6z^4+12z^5+55z^6+84z^7+78z^8+50z^9+21z^{10}+6z^{11}+z^{12}\). The latter graph is a six-cycle, consistent with the previously published scalar minimum.

## Relationship to prior work
Abdollahzadeh Ahangar, Chellali, Sheikholeslami and Soroudi introduced hop-total-Roman domination and established bounds, a complexity result for bipartite graphs, exact minimum values on paths and cycles, and structural criteria for small minimum values [1]. Their Proposition 6 gives strong prior coverage of the minimum-weight-four phenomenon; **the fact that the minimum is four is not claimed new**. The present claim instead classifies **all labelled functions by every weight**, and establishes an exact linear response to deletion of an arbitrary matching, including all coefficient changes and their high-weight cutoff. Jafari Rad and Shabani studied hop-Roman domination without the positive-support totality condition [2], which does not determine these weight polynomials. Roman-domination enumerators requiring adjacent rather than distance-two defenders likewise do not imply the stated formula. Research-record and literature searches found no equivalent complete enumerator for this parameter family, though absence of a match is not a proof of priority.

## Limitations
This theorem assumes each shore has at least three vertices and the deleted edges form a matching. The distance-two reduction can fail for smaller shores, and the independent bad-event argument fails for deletions sharing endpoints. No formula for arbitrary deleted-edge subgraphs is asserted. Only two-distance defenders and the *positive-induced-subgraph* totality convention are used; other Roman or hop-domination conventions are different. Publication priority remains provisional because a semantically equivalent formulation could exist outside the inspected corpus. All original mathematical arguments and code require independent review before claiming independent verification.

## References
[1] H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami and M. Soroudi, “Hop total Roman domination in graphs,” *AKCE International Journal of Graphs and Combinatorics* **20** (2023), 73–78. DOI: 10.1080/09728600.2023.2184288. First publicly available online 2023-03-30. See especially §§2–5 and Proposition 6.

[2] N. Jafari Rad and E. Shabani, “On the complexity of some hop domination parameters,” *Electronic Journal of Graph Theory and Applications* **7** (2019), 74–86. DOI: 10.5614/ejgta.2019.7.1.6. This concerns the hop-Roman rather than hop-total-Roman predicate.
