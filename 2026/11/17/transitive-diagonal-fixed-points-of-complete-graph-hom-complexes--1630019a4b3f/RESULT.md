# Transitive diagonal fixed points of complete-graph Hom complexes

## Finding
Let \(G\) be a finite group, \(S\) a finite transitive \(G\)-set of cardinality \(m\ge2\), and \(T\) any finite \(G\)-set of cardinality \(n\). Give \(\operatorname{Hom}(K_S,K_T)\) the simultaneous action on source and target. For each target orbit \(O\subseteq T\), choose \(t_O\in O\), let \(K_O=\operatorname{Stab}_G(t_O)\), and put \(a_O=|S^{K_O}|\). Write \(\mathscr O_+\) for the target orbits with \(a_O>0\), and let \(r=|\mathscr O_+|\).

**Theorem.** There is a canonical piecewise-linear homeomorphism
\[
\big|\operatorname{Hom}(K_S,K_T)\big|^G\ \cong_{\mathrm{PL}}\ \mathop{\ast}_{O\in\mathscr O_+}D_{a_O},
\]
where \(D_a\) denotes a discrete space of \(a\) points, and the empty join means the empty space. Equivalently, if \(S\cong G/L\), then \(a_O=|(G/L)^{K_O}|\), the number of equivariant maps from \(G/K_O\) to \(G/L\).

In particular, the fixed space is empty when \(r=0\), contractible whenever some eligible orbit has \(a_O=1\), and otherwise has integral homotopy type
\[
\bigvee^{\prod_{O\in\mathscr O_+}(a_O-1)} S^{r-1}.
\]
The formulas include the case \(r=1\), where the wedge of zero-dimensional spheres is understood as a discrete set of the stated size plus one.

For a noncyclic illustration, let \(G=S_4\) act naturally on four source vertices and act on target colors consisting of two separate copies of the twelve ordered pairs of distinct elements of \(\{1,2,3,4\}\). Each target orbit has exactly two equivariant maps to the source (first and second coordinates). Thus
\[
\big|\operatorname{Hom}(K_4,K_{24})\big|^{S_4}\cong_{\mathrm{PL}}D_2*D_2\cong S^1.
\]

## Assumptions and scope
All groups and sets are finite; the source action is transitive and has at least two points. The complete graphs are loopless. A Hom cell is a tuple of pairwise disjoint nonempty subsets of target colors, realized as a product of standard simplices. The fixed points here are actual geometric fixed points under the simultaneous source/target action, not homotopy fixed points, fixed vertices alone, or an orbit-space quotient. A target set smaller than the source set is allowed; the formula then correctly gives an empty space. No freeness, faithfulness, or transitivity condition is placed on the target action.

## Proof
Realize a point of \(\operatorname{Hom}(K_S,K_T)\) as nonnegative numbers \(p_s(t)\) with \(\sum_{t\in T}p_s(t)=1\) for every \(s\in S\), and \(p_s(t)p_{s'}(t)=0\) for all distinct \(s,s'\). The latter condition says that the nonempty probability supports of different source vertices are disjoint. A point is fixed if and only if
\[
p_{gs}(gt)=p_s(t)\qquad(g\in G,\ s\in S,\ t\in T).
\]
For each color \(t\) carrying positive mass, disjointness assigns it to a unique source vertex \(f(t)\). The fixed equation makes the selected-color set a union of target orbits and forces \(f(gt)=g f(t)\). Therefore every selected target orbit \(O\) comes equipped with exactly one equivariant map \(O\to S\). Such maps are determined by the image of \(t_O\), and that image may be any element of \(S^{K_O}\), giving precisely \(a_O\) choices. No orbit having \(a_O=0\) may be selected, and an orbit cannot be selected twice with different assignments.

Within each selected orbit \(O\), equivariance makes every positive matrix entry equal to a single scalar \(c_O>0\). Since the source action is transitive and the equivariant map is surjective, each source vertex receives exactly \(|O|/m\) colors from \(O\). Hence row normalization is equivalent to
\[
\sum_{O\text{ selected}}\frac{|O|}{m}c_O=1.
\]
Set \(\lambda_O=(|O|/m)c_O\). Then the \(\lambda_O\) are precisely barycentric coordinates on the simplex associated with the chosen equivariant map for each selected orbit. They extend continuously to zero, when that orbit disappears. Conversely, from a join point choose at most one map per positive-weight orbit and define \(p_s(t)=(m/|O|)\lambda_O\) if the chosen map sends \(t\) to \(s\), and zero otherwise. The formulas are mutually inverse, linear on each simplex, and compatible on common faces. This is the required global PL homeomorphism.

The reduced integral homology and homotopy type follow by the join identity \(X*Y\simeq\Sigma(X\wedge Y)\): each \(D_a\) with \(a>1\) is a wedge of \(a-1\) copies of \(S^0\); if any factor is a point, the join is a cone. The empty case has no contributing orbits. This finishes the proof in all cases.

## Verification
The standalone `verify_nonabelian_hom.py` performs an independent exhaustive support-assignment check for the natural three-source action of \(S_3\) with a natural three-color orbit and a regular six-color orbit. All \(4^9=262144\) possible color-to-source-or-unused assignments are considered, with each of the six group elements checked. Exactly seven nonempty invariant Hom supports occur, as predicted by \((1+1)(3+1)-1=7\). The same program independently constructs the two twelve-color ordered-pair orbits for \(S_4\), verifies two equivariant maps per orbit and the eight nonempty support cells of a four-cycle. These are finite corroborations, not the proof of the general theorem. Run `python3 verify_nonabelian_hom.py` from the package directory; no nonstandard dependencies are required.

## Relationship to prior work
Babson and Kozlov, *Diagrams of classifying spaces and k-fold Boolean algebras* (arXiv:math/9704227, first publicly posted April 29, 1997), already identify the ordered-disjoint-nonempty-block face poset in Section 6. Their Theorem 6.2(d) treats the ordinary homotopy type and Theorem 6.2(e) the block-permutation quotient, not the fixed loci of arbitrary simultaneous source–target groups. Their later *Complexes of graph homomorphisms* (arXiv:math/0310056, first publicly posted October 5, 2003), defines the Hom polyhedral complex and obtain its ordinary nonequivariant sphere-wedge type for complete graphs (Section 4.3). Their source-swap equivariant theorem for trees (Proposition 5.5) concerns a different action and does not state a simultaneous, arbitrary-transitive-group fixed-point model. Dochtermann, *Hom complexes and homotopy theory in the category of graphs* (arXiv:math/0605275), establishes functorial and categorical Hom-complex results, not this stabilizer-weighted join formula.

A previously developed diagonal cyclic special case has one fixed choice count equal to the source cycle length per eligible target orbit. The present statement strictly extends that case: it includes noncyclic transitive groups, varying stabilizer-dependent choice counts, and contractible-versus-spherical cases within the same target action. Ordinary rational character formulas for the two-sided symmetry of complete-graph Hom complexes are also weaker information: they do not determine all subgroup-fixed homotopy types. Equivalent unindexed general equivariant statements remain a possible originality risk.

## Limitations
The source action must be transitive; for arbitrary intransitive source actions the row-normalization variables for distinct orbits interact, and this join description is not asserted. The theorem is a PL classification of geometric fixed spaces, not a classification of the entire equivariant Hom-complex homotopy type or of arbitrary graph pairs. No independent mathematical audit or definitive publication-priority verification has been performed.

## References
1. E. Babson and D. N. Kozlov, *Diagrams of classifying spaces and k-fold Boolean algebras*, arXiv:math/9704227 (first version April 29, 1997), especially Section 6 and Theorem 6.2. https://arxiv.org/abs/math/9704227
2. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056 (first version October 5, 2003), especially Definition 1.2, Section 4.3, and Proposition 5.5. https://arxiv.org/abs/math/0310056
3. A. Dochtermann, *Hom complexes and homotopy theory in the category of graphs*, arXiv:math/0605275 (first version 2006), especially Sections 3 and 5. https://arxiv.org/abs/math/0605275
