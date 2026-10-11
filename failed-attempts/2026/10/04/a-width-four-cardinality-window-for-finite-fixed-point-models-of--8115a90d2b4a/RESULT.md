# A width-four cardinality window for finite fixed-point models of the circle
## Finding
Let \(m_{\mathrm{FPP}}(S^1)\) be the least cardinality of a finite \(T_0\)-space with the fixed point property and weak homotopy type \(S^1\). Then \(10 \le m_{\mathrm{FPP}}(S^1) \le 14\).

Equivalently, the unresolved minimum is confined to the five cardinalities \(10,11,12,13,14\).

## Assumptions and scope
A finite \(T_0\)-space is identified with its specialization poset. The fixed point property means that every continuous self-map has a fixed point. Weak homotopy type is meant in the ordinary sense; by McCord's finite-space theorem, the order complex of a finite \(T_0\)-space has the same weak homotopy type.

The claim concerns only the minimum cardinality for weak circle type. It does not classify the fixed-point spaces of sizes \(10\) through \(14\), nor does it assert that the known \(14\)-point example is minimal.

## Proof
For the lower bound, let \(X\) be a finite \(T_0\)-space with the fixed point property and suppose \(|X|\le 9\). Under the finite-space/poset correspondence, write \(P\) for its specialization poset. Rutkowski's small-set analysis, in the explicit formulation recorded in Schröder's *Ordered Sets*, Exercise 4-34, says that every ordered set with the fixed point property and at most nine elements is connectedly collapsible.

Baclawski proves that connected collapsibility is equivalent to link collapsibility for finite posets, and that a link-collapsible poset is a pseudo cone. A pseudo cone has an acyclic complete matching on its order complex; consequently its geometric realization is contractible, and in particular its reduced integral homology vanishes. Thus
\[
H_1(\Delta P;\mathbb Z)=0.
\]
McCord's weak equivalence between a finite \(T_0\)-space and its order complex then gives \(H_1(X;\mathbb Z)=0\). This is incompatible with \(X\simeq_w S^1\), since \(H_1(S^1;\mathbb Z)\cong\mathbb Z\). Hence any fixed-point finite model of the circle has at least \(10\) points.

For the upper bound, Barmak's Lemma 10 constructs an explicit finite \(T_0\)-space \(K\) with \(14\) points, the fixed point property, and weak homotopy type \(S^1\). Therefore \(m_{\mathrm{FPP}}(S^1)\le 14\).

Combining the two inequalities proves the claim.

## Verification
The lower-bound implication was checked at the level of statements rather than titles: (i) the small-set fixed-point theorem supplies connected collapsibility for every fixed-point poset of cardinality at most \(9\); (ii) Baclawski's Proposition 6.5 and Corollary 6.9 convert connected collapsibility to the pseudo-cone condition; and (iii) the pseudo-cone construction gives a contractible order complex. The contradiction with circle type is then the homology obstruction \(0=H_1(\Delta P;\mathbb Z)\not\cong H_1(S^1;\mathbb Z)=\mathbb Z\).

The upper-bound witness was checked in Barmak's preprint arXiv:1307.1722, Lemma 10, where the displayed space has \(14\) points and is proved both weakly homotopy equivalent to \(S^1\) and to have the fixed point property.

## Relationship to prior work
Rutkowski's 1989 paper determines the fixed-point behavior of small finite posets; Baclawski's 2012 paper supplies the relevant collapse-to-contractibility mechanism; and Barmak's 2013 preprint gives the explicit \(14\)-point fixed-point model of the circle. The stated interval is a synthesis of these results: the lower and upper bounds come from different strands of the finite-poset fixed-point literature.

Targeted searches for the exact minimum-cardinality formulation, its equivalent finite-poset/order-complex formulation, and the numerical interval \(10\) to \(14\) did not locate a source that states this combined bound. This search result is evidence of noncoverage, not a proof of novelty.

## Limitations
The exact value of \(m_{\mathrm{FPP}}(S^1)\) is not determined here. The remaining candidate sizes are \(10,11,12,13,14\). The direct full text of Rutkowski's 1989 article was not accessible during verification; the needed at-most-nine connected-collapse statement was checked through Schröder's explicit later restatement, while the bibliographic identity and scope of Rutkowski's paper were independently checked. This leaves a residual source-inspection risk but does not affect the logical implication once the stated small-set theorem is accepted.

## References
1. A. Rutkowski, *The fixed point property for small sets*, Order 6 (1989), DOI 10.1007/BF00341631.
2. K. Baclawski, *A combinatorial proof of a fixed point property*, Journal of Combinatorial Theory, Series A 119 (2012), 994–1013, DOI 10.1016/j.jcta.2012.01.004.
3. J. A. Barmak, *The fixed point property in every weak homotopy type*, arXiv:1307.1722 (2013); later American Journal of Mathematics, DOI 10.1353/AJM.2016.0042.
4. M. C. McCord, *Singular homology groups and homotopy groups of finite topological spaces*, Duke Mathematical Journal 33 (1966), 465–474.
5. B. S. W. Schröder, *Ordered Sets: An Introduction with Connections from Combinatorics to Topology*, 2nd ed., Exercise 4-34.
