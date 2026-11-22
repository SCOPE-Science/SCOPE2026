# Regular equivariant endomorphisms of finite \(G\)-sets: exact rank census and monoid criterion

## Finding

Let \(G\) be a finite group acting on a nonempty finite set \(X\). An equivariant endomorphism \(f:X\to X\) is **regular** (in the von Neumann semigroup sense) if there exists an equivariant endomorphism \(g:X\to X\) with \(f\circ g\circ f=f\). We determine the image-cardinality distribution of all regular endomorphisms and give an exact criterion for when **every** equivariant endomorphism is regular.

Choose pairwise nonconjugate subgroups \(H_1,\ldots,H_r\) representing the stabilizer types occurring in \(X\), and write

\[
X\cong\bigsqcup_{i=1}^r m_i(G/H_i),\qquad m_i\ge1.
\]

Put \(d_i=|G:H_i|\) and \(a_{ij}=|(G/H_j)^{H_i}|\), the corresponding entries of the table of marks, with source type \(i\) indexing rows and target type \(j\) indexing columns. In particular \(a_{ii}=|N_G(H_i):H_i|\ge1\). For each integer vector \(\mathbf s=(s_1,\ldots,s_r)\), \(0\le s_i\le m_i\), set

\[
b_i(\mathbf s)=\sum_{j=1}^{r}s_ja_{ij},\qquad
F_i(\mathbf s)=\sum_{u=0}^{s_i}(-1)^u\binom{s_i}{u}\bigl(b_i(\mathbf s)-u a_{ii}\bigr)^{m_i}.
\]

**Rank-census theorem.** The complete rank polynomial for regular equivariant maps is

\[
\boxed{R_X(T)=\sum_{0\le s_i\le m_i}\left[\prod_{i=1}^r\binom{m_i}{s_i}F_i(\mathbf s)\right]T^{\sum_{i=1}^rs_id_i}.}
\]

**Monoid-regularity theorem.** All elements of \(\operatorname{End}_G(X)\) are regular if and only if, for every type \(i\) for which some other represented type \(h\ne i\) has \(a_{hi}>0\), both of the following hold: \(m_i=1\); and \(a_{ik}=0\) for every \(k\ne i\). Informally, any represented type receiving maps from a strictly smaller stabilizer type must occur once and be maximal among represented types under the orbit-map preorder.

These statements hold for nonabelian groups, mixed stabilizer types, arbitrary orbit multiplicities, and all finite cardinalities. No faithfulness or transitivity of the action is assumed.

## Assumptions and scope

All group actions are left actions; all maps are total and \(G\)-equivariant. Stabilizer types are conjugacy classes, not individual subgroups. An equivariant map \(G/H_i\to G/H_j\) is determined by the image of \(H_i\), and this image may be any point of \((G/H_j)^{H_i}\); thus there are exactly \(a_{ij}\) such maps. Every map from one finite transitive orbit onto another is surjective. A map between two orbits of the same stabilizer type is an isomorphism, as the orbits have equal finite cardinality.

We enumerate image cardinality, not the number of image orbits. Different vectors \(\mathbf s\) may contribute to the same exponent; coefficients must be added. By convention, \(c^m\) is computed with \(m=m_i\ge1\), so a zero target count contributes zero.

## Proof

**Step 1: regularity is equivalent to an equivariant section onto the image.** Suppose \(f\circ g\circ f=f\). For \(y=f(x)\), the equality gives \(f(g(y))=y\). Consequently, \(g|_{f(X)}\) is a \(G\)-equivariant right inverse of the onto map \(f:X\to f(X)\). Conversely, if an equivariant right inverse \(s:f(X)\to X\) exists, extend \(s\) to an equivariant endomorphism \(g:X\to X\) by taking \(g(x)=x\) on orbit components disjoint from \(f(X)\). This is well-defined because \(f(X)\) is a union of entire orbits, and yields \(fgf=f\).

On a target image orbit \(O\), the restriction \(s|_O\) is an injective equivariant map into a source orbit \(Q\), and \(f|_Q:Q\to O\) is onto. Every equivariant map between transitive finite orbits is onto, so \(s|_O\) is also onto and hence an isomorphism. Thus a section exists precisely when each target orbit in \(f(X)\) has a source orbit of the same stabilizer type mapping isomorphically onto it. Distinct image orbits have distinct such source orbits because the original map sends a single source orbit into a single target orbit.

**Step 2: count regular maps with a fixed image-orbit support.** Select exactly \(s_j\) out of the \(m_j\) labelled target orbits of type \(j\); there are \(\prod_j\binom{m_j}{s_j}\) choices. To map a single source orbit of type \(i\) into this selected set there are exactly \(b_i(\mathbf s)=\sum_j s_ja_{ij}\) equivariant maps. As shown above, the resulting map is regular and has precisely the selected image if and only if **every selected orbit of type \(i\)** receives at least one source orbit of type \(i\). This condition simultaneously guarantees that every selected image orbit is hit: when it receives an equal-type map, that map is onto. The other source types are unrestricted except that they map within the selected target set.

Fix \(i\). By inclusion–exclusion over the \(s_i\) selected target orbits of type \(i\), the number of assignments of the \(m_i\) labelled type-\(i\) source orbits which hit every selected same-type target orbit is

\[
F_i(\mathbf s)=\sum_{u=0}^{s_i}(-1)^u\binom{s_i}{u}(b_i(\mathbf s)-ua_{ii})^{m_i}.
\]

The subtraction of \(ua_{ii}\) removes exactly the maps landing in a specified collection of \(u\) forbidden equal-type targets. Choices for different source types are independent; multiply the \(F_i\), multiply by the target-support selection factors, and attach the total image cardinality \(\sum_i s_i d_i\). Summing over \(\mathbf s\) proves the polynomial formula without any overcounting.

**Step 3: characterize when all endomorphisms are regular.** Consider the directed graph of represented orbit types, with arrow \(i\to j\) exactly when \(a_{ij}>0\). Between different represented types this relation strictly increases subgroup order (up to conjugacy), hence it cannot contain a directed cycle of strict arrows. Suppose every type \(i\) receiving a strict incoming arrow has multiplicity one and no strict outgoing arrow. Let \(f\) be any equivariant endomorphism and let \(O\subseteq f(X)\) be a target image orbit of type \(i\). If no type-\(i\) source maps onto \(O\), some source of a different type \(h\) must do so, giving a strict incoming arrow \(h\to i\). The unique type-\(i\) source orbit must then map somewhere other than \(O\). It cannot map into another type-\(i\) orbit, since there is only one, and it cannot map into a different type, since there is no strict outgoing arrow. Contradiction. Therefore every image orbit has an equal-type source; by Step 1, every map is regular.

Conversely, suppose \(h\ne i\) and \(a_{hi}>0\). Choose one source orbit \(Q_h\) of type \(h\) and one target orbit \(O_i\) of type \(i\), and map \(Q_h\) onto \(O_i\). If \(m_i\ge2\), map every source orbit of type \(i\) isomorphically into a **different** type-\(i\) target orbit. If \(m_i=1\) and \(a_{ik}>0\) for some \(k\ne i\), map the unique type-\(i\) source orbit into an orbit of type \(k\). In either case, let all as-yet-unassigned source orbits map identically to themselves. This constructs an equivariant map whose image contains \(O_i\), but no source orbit of type \(i\) maps onto \(O_i\). By Step 1 the map is not regular. Hence regularity of the whole monoid forces both stated conditions for every type with strict incoming arrows.

## Verification

The standalone `VERIFY.py` uses only the Python 3 standard library. It independently enumerates group actions and all equivariant point maps, determines regularity by explicitly searching for actual inner inverses \(g\), calculates the table-of-marks formula separately, and compares the two rank polynomials and the whole-monoid criterion. It covers ten finite labelled action configurations for trivial, cyclic and nonabelian symmetric groups, including multiplicity changes and conjugate stabilizer types.

For example, for the order-two group acting on one free orbit and two fixed points, there are \(16\) equivariant endomorphisms, of which exactly \(14\) are regular, with rank polynomial

\[
R_X(T)=2T+4T^2+4T^3+4T^4.
\]

For the nonabelian symmetric group on three symbols, acting on one natural three-point orbit, one two-point orbit and two fixed points, there are \(48\) equivariant maps and \(36\) regular ones. These are finite consistency tests; the proof in Steps 1–3 establishes the universal quantifiers.

## Relationship to prior work

Castillo-Ramirez and Ruiz-Medina's 2022 paper develops the orbit-map structure of finite equivariant transformation monoids and determines their relative rank modulo units. The present formula uses the same basic orbit-map facts but counts **von Neumann regular elements by image cardinality**, and the monoid criterion concerns **all elements being regular**, rather than minimal generating sets. Ruiz-Medina's 2025 cardinality paper counts the whole equivariant endomorphism monoid and its units but does not give the present section-refined regular-element formula. A 2025 Green-relations paper studies semigroup relations rather than deriving this rank census or the stated whole-monoid condition. Classical results on free or projective group acts address more restricted actions. The underlying finite-group table of marks and inclusion–exclusion are standard ingredients, not claimed as new.

## Limitations

The polynomial requires the table of marks restricted to stabilizer types actually occurring in the action, as well as their multiplicities. It does not count nilpotent elements, classify Green classes, or settle infinite actions. The finite computational tests are checks, not an independent proof of the general theorem. The historical priority assessment is limited to literature materially inspected and discoverable indexed results; older or unindexed equivalent formulations may exist. Independent external review has not been performed.

## References

- Alonso Castillo-Ramirez and Ramón H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite \(G\)-set*, first posted 2022-03-23, https://arxiv.org/abs/2203.12158.
- Ramón H. Ruiz-Medina, *Cardinalities in finite monoids of \(G\)-equivariant functions*, 2025, https://arxiv.org/abs/2503.03772.
- Ramón H. Ruiz-Medina and coauthors, *Green relations over finite monoids of \(G\)-equivariant functions*, 2025, https://arxiv.org/abs/2503.14511.
- S. Bulman-Fleming, *Regularity and products of idempotents in endomorphism monoids of projective acts*, 1995, DOI: 10.1112/S0025579300014649.
