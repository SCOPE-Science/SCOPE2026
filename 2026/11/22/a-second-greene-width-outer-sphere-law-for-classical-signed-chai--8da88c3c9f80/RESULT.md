# A second-Greene-width outer-sphere law for classical signed-chain polytopes

## Finding

For every nonempty finite poset \(P\), let \(\mathcal C(P)\subseteq\mathbb R^P\) be Stanley's chain polytope, and put
\[
\mathcal S(P)=\left\{x\in\mathbb R^P:\left|\sum_{p\in C}x_p\right|\le1\text{ for every nonempty chain }C\subseteq P\right\}.
\]
This is the specialization to an ordinary (all-positive) poset of the signed-chain inequalities of Beck--Hlavacek. Define the second Greene width
\[
d_2(P)=\max\bigl\{|A\cup B|:A,B\subseteq P\text{ are antichains}\bigr\},
\]
equivalently the largest cardinality of a subset of height at most two. The following exact metric and contact classification holds:
\[
\boxed{\mathcal S(P)=\mathcal C(P)-\mathcal C(P),\qquad
R_{\min}(\mathcal S(P))=\sqrt{d_2(P)},\qquad
\operatorname{diam}(\mathcal S(P))=2\sqrt{d_2(P)}.}
\]
The minimum-radius Euclidean enclosing ball is **uniquely** centered at the origin. Its **entire** spherical contact set is
\[
\boxed{\left\{\mathbf1_A-\mathbf1_B:
A,B\text{ disjoint antichains},\quad |A|+|B|=d_2(P)\right\}.}
\]
Every diametral pair is the antipodal pair of two such contacts. In particular, let \(\mathscr U_2(P)\) denote the subsets of cardinality \(d_2(P)\) and height at most two. If \(c(U)\) counts connected components (including isolated vertices) of the **comparability graph induced on** \(U\), then the exact number of contact points is
\[
\boxed{N_{\rm contact}(P)=\sum_{U\in\mathscr U_2(P)}2^{c(U)},\qquad
N_{\rm diametral\ pairs}(P)=\tfrac12 N_{\rm contact}(P).}
\]
For an ordinal sum \(P=A_{m_1}\oplus\cdots\oplus A_{m_k}\) of \(k\ge2\) nonempty antichains, the squared enclosing radius is the sum of the two largest layer sizes, and the number of contact points is twice the number of unordered layer pairs attaining that largest two-layer sum. For a chain on \(n\ge2\) elements the contact set has \(n(n-1)\) points; for an antichain on \(n\) elements it has \(2^n\) points. Compared with the enriched chain polytope, whose minimum enclosing radius is \(\sqrt{w(P)}\) for ordinary width \(w(P)\), the ratio of the signed-chain radius to the enriched-chain radius lies sharply between \(1\) and \(\sqrt2\). It equals \(1\) precisely for antichains and equals \(\sqrt2\) precisely when the poset has two disjoint maximum antichains.

## Assumptions and scope

The poset is finite and nonempty; no purity, grading, connectedness, or natural-label assumption is imposed. An antichain may be empty and the union in the definition of \(d_2\) need not be disjoint, although it always has a disjoint antichain partition. Height counts elements, not cover relations. The Euclidean metric is the standard one in the indicator-coordinate embedding of \(\mathbb R^P\). A sphere contact means a point of the **whole polytope** at distance exactly \(R_{\min}\) from the unique circumcenter, rather than merely a vertex of some chosen triangulation. The assertion about an ordinary signed-poset specialization only concerns root differences that represent an ordinary poset; it does not assert a metric theorem for arbitrary signed posets.

The comparability graph of \(P\) joins distinct comparable elements. A subset has height at most two exactly when the induced comparability graph is bipartite. Indeed, a three-element chain would produce a triangle, whereas if the subset has height at most two, sorting its elements by maximum chain length ending at each element gives at most two antichain rank classes, hence a proper two-coloring.

## Proof

**1. Exact identification of the polytope.** The ordinary chain polytope is
\[
\mathcal C(P)=\left\{u\in\mathbb R_{\ge0}^P:\sum_{p\in C}u_p\le1\text{ for all chains }C\right\}.
\]
If \(u,v\in\mathcal C(P)\), then each chain sum of \(u-v\) lies in \([-1,1]\). Thus \(\mathcal C(P)-\mathcal C(P)\subseteq\mathcal S(P)\).

Conversely suppose \(x\in\mathcal S(P)\), and set \(x_p^+=\max(x_p,0)\), \(x_p^-=\max(-x_p,0)\). For each chain \(C\), its positive-support subset \(C^+=\{p\in C:x_p>0\}\) is itself a chain. Hence
\[
\sum_{p\in C}x_p^+=\sum_{p\in C^+}x_p\le1.
\]
The negative-support subchain similarly gives \(\sum_{p\in C}x_p^-\le1\). Both positive and negative parts belong to \(\mathcal C(P)\), and \(x=x^+-x^-\). This proves the identity exactly, with no integrality or vertex assumption.

**2. A finite signed-antichain generating set.** Stanley's antichain-vertex theorem gives
\[
\mathcal C(P)=\operatorname{conv}\{\mathbf1_A:A\text{ an antichain of }P\}.
\]
Minkowski linearity of convex hulls therefore gives
\[
\mathcal S(P)=\operatorname{conv}\{\mathbf1_A-\mathbf1_B:A,B\text{ antichains}\}.
\]
If \(A\cap B\ne\varnothing\), deleting their intersection does not change the difference vector. Consequently all generators can be written with disjoint antichains \(A,B\), and for each of them
\[
\|\mathbf1_A-\mathbf1_B\|_2^2=|A|+|B|\le d_2(P).
\]
Every union of two antichains can be made disjoint by deleting its overlap from one member. Thus a disjoint maximizing pair exists, giving a generator of squared norm exactly \(d_2(P)\). The convexity of squared Euclidean norm now proves that the entire body is contained in the ball \(B(0,\sqrt{d_2(P)})\), and this ball has boundary points from the displayed generating set.

**3. Global optimality and uniqueness of the center.** The difference body is centrally symmetric. If \(z\) is any one of the norm-maximizing generators, then \(-z\) is also in the body and the distance between them is \(2\sqrt{d_2(P)}\). Every enclosing ball has radius at least half this distance. The centered ball from Step 2 attains this lower bound, proving the radius and diameter. If a radius-\(\sqrt{d_2(P)}\) ball centered at \(c\) contained both \(\pm z\), then averaging the two squared inequalities yields
\[
\|z\|^2+\|c\|^2\le d_2(P).
\]
Since \(\|z\|^2=d_2(P)\), one has \(c=0\). This also proves uniqueness without any symmetry assumption on candidate centers.

**4. All contacts, not just an upper bound.** Every point \(x\in\mathcal S(P)\) is a convex combination of the finite generators in Step 2. Strict convexity gives
\[
\|x\|^2=\sum_j\lambda_j\|z_j\|^2-\sum_{i<j}\lambda_i\lambda_j\|z_i-z_j\|^2\le d_2(P).
\]
Equality is possible only if every generator of positive weight is the *same vector* and its squared norm is \(d_2(P)\). These vectors are precisely the differences of disjoint maximum-total-size antichains stated in the theorem. The same calculation excludes nonvertex points from the sphere. Since every contact has its negative contact and the diameter equals twice the radius, every diametral pair is antipodal, and conversely every antipodal contact pair is diametral.

**5. Exact contact enumeration.** A contact vector \(z\) determines its support \(U=\{p:z_p\ne0\}\), its positive antichain \(A\), and its negative antichain \(B\) *uniquely*. For each \(U\in\mathscr U_2(P)\), the possible \(\pm1\) assignments on \(U\) are exactly proper two-colorings of its induced comparability graph. Each connected bipartite component has exactly two such assignments. Thus \(U\) supplies exactly \(2^{c(U)}\) distinct contacts. Distinct supports give disjoint contact classes. Summing proves the enumeration; division by two counts antipodal unordered pairs. For an ordinal sum of \(k\ge2\) layers, every maximum two-family is the union of two full layers of maximum total size, giving exactly two signs per maximizing pair because the associated complete bipartite graph is connected. The chain and antichain formulas follow from the same count. Finally \(w(P)\le d_2(P)\le 2w(P)\): one antichain is a two-family, whereas each of two antichains has size at most \(w(P)\). If the poset is not an antichain, a maximum antichain omits some element; adjoining that element as the second antichain shows \(d_2(P)\ge w(P)+1\). Thus equality at the lower end occurs only for antichains. Equality at the upper end occurs precisely if a maximizing union is made of two disjoint maximum antichains. Taking square roots and the known enriched-chain radius gives the sharp ratio statement.

## Verification

The standalone `verify.py` uses exact integer arithmetic and the standard Python library. It independently generates every naturally labeled partial order with at most five elements (407 transitive closures), all of their antichains, and all of their chains. For each order it computes (i) the complete set of differences of antichain indicators, (ii) the ternary integer points satisfying the signed chain inequalities, (iii) the maximum squared Euclidean norm, (iv) the maximum disjoint two-antichain cardinality, and (v) the complete sets of sphere contacts from both constructions. All comparisons agree. It covers 36,947 counted integer points across these posets and 3,158 counted contact occurrences. Run `python3 verify.py` with Python 3.10 or later. The final output must begin with `POSSET_DIFFERENCE_BODY_PASS`.

These tests are finite corroboration, not an infinite proof or a claim that integer-point comparisons alone exhaust all real points. The exact polytope identity and strict-convexity argument in Steps 1–5 prove the all-poset theorem.

## Relationship to prior work

Stanley's chain-polytope theorem (1986) supplies the antichain indicator vertices, not the Euclidean classification here. Beck and Hlavacek (arXiv:2311.04409, 2023) introduce signed chain inequalities and characterize their integer points; their Section 6 motivates the ordinary-poset specialization. They do not state the identity with the chain-polytope difference body or the complete minimum enclosing sphere, contact counts, and second-Greene-width interpretation. These results are consequences of their definitions combined with the older antichain-vertex theorem, but are not presented as new structure for arbitrary signed posets.

A published geometric result on enriched chain polytopes gives enclosing radius \(\sqrt{w(P)}\) and contacts at signed maximum antichains. That *different* polytope requires a single signed antichain support; the present difference body permits two disjoint antichains and detects \(d_2(P)\). Work on order-polytope difference bodies classifies **inscribed** sphere contacts rather than the **enclosing** sphere here. Results on symmetric twinned chain polytopes use \(\operatorname{conv}(\mathcal C\cup-\mathcal C)\), not the Minkowski difference \(\mathcal C-\mathcal C\). These distinctions are of the objects and statements, not just titles. No claim of independently verified historical priority is made; separately indexed or older equivalent descriptions could remain.

## Limitations

The theorem is specialized to the canonical signed-chain geometry arising from ordinary posets; genuinely signed type-B roots need not enjoy the positive/negative-part decomposition. Euclidean radii depend on coordinates and are not invariant under a general affine realization. The integer invariant \(d_2\) is classical; the claim is its *exact geometric realization and full contact characterization*, not the discovery of the combinatorial invariant or an algorithm beyond standard poset methods. Independent audit and exhaustive historical-priority validation have not occurred.

## References

1. R. P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry **1** (1986), 9–23, DOI 10.1007/BF02187680.
2. Matthias Beck and Max Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409v1, publicly posted 2023-11-08, especially Section 6, Definitions 6.4–6.5 and Proposition 6.10, https://arxiv.org/abs/2311.04409.
3. C. Greene and D. J. Kleitman, *The Structure of Sperner k-Families*, Journal of Combinatorial Theory, Series A **20** (1976), 41–68 (for the classical \(k\)-family width terminology).
4. S. Okada and A. Tsuchiya, *Two Enriched Poset Polytopes*, arXiv:2003.12271, 2020 (for the distinct enriched-chain construction).
5. *Height and width are the exact Euclidean radii of enriched chain polytopes*, mathematical research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-height-and-width-are-the-exact-euclidean-radii-of-enriched-chain--db93f92ff100.
6. *Alternating-chain rigidity and the contact collapse of order-polytope difference bodies*, mathematical research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-alternating-chain-rigidity-and-the-contact-collapse-of-order-pol--9aba23dfb7e5.
7. *Incenter boxes and contact strata of layered twinned chain polytopes*, mathematical research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-incenter-boxes-and-contact-strata-of-layered-twinned-chain-polyt--410962c86761.
