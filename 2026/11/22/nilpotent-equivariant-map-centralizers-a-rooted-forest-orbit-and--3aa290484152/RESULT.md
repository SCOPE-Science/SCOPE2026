# Nilpotent equivariant-map centralizers: a rooted-forest orbit and full commutant spectrum

## Finding

Let \(G\) be any finite group of order \(q\ge1\), let \(b\ge1\), and let \(X=\{0\}\sqcup(G\times[b])\) carry the trivial action at its distinguished basepoint \(0\) and a left-regular action on each of the other \(b\) orbits. Write \(M=\operatorname{End}_{G,*}(X)\) for the monoid of **basepoint-preserving** equivariant self-maps and \(z\) for the constant map to \(0\). The basepoint-preserving requirement matters when \(G\) is trivial.

**Theorem.** For every \(f\in M\) satisfying \(f^k=z\) for some positive integer \(k\), its conjugacy class under the full unit group \(M^\times\) is uniquely represented by a rooted forest \(F\) on \(b\) unlabeled vertices, with the roots joined to a new common vertex \(0\). There are thus exactly as many nilpotent unit-conjugacy classes as unlabeled rooted trees on \(b+1\) vertices, independent of the isomorphism type and order of \(G\).

Write \(r(F)\) for the number of vertices adjoining \(0\), \(a(F)\) for the number of automorphisms of the rooted forest (fixing \(0\)), \(s(F)\) for the number of nonroot vertices which have a child, and \(h(F)\) for the greatest distance of a vertex to \(0\). The class has exactly
\[
L_q(F)=\frac{b!\,q^{b-r(F)}}{a(F)}
\]
labelled equivariant maps, each of image cardinality \(1+q\,s(F)\) and nilpotency index \(h(F)\).

The **full composition-centralizer cardinality** \(c_q(F)=|C_M(f)|\), counting *all* equivariant self-maps commuting with \(f\), including nonnilpotents, has the following finite bottom-up recursion. Let \(C(v)\) denote the children of vertex \(v\) in \(F\cup\{0\}\), and put \(R=C(0)\). For every nonroot vertex \(v\) and every vertex \(w\in\{0\}\cup F\), define
\[
\begin{aligned}
H_v(0)&=\prod_{u\in C(v)}\left(H_u(0)+q\sum_{x\in R}H_u(x)\right),\\
H_v(w)&=\prod_{u\in C(v)}\left(\sum_{x\in C(w)}H_u(x)\right),\qquad w\ne0.
\end{aligned}
\]
Empty products are \(1\), empty sums are \(0\). Then
\[
\boxed{c_q(F)=\prod_{v\in R}\left(H_v(0)+q\sum_{w\in R}H_v(w)\right).}
\]
Every term is an integer polynomial in \(q\). In particular, the complete unit-orbit, image-cardinality, nilpotency-index, and centralizer-cardinality spectrum is the explicit finite polynomial
\[
\boxed{\mathcal C_{b,q}(U,V,W)=\sum_{[F]}L_q(F)\,U^{1+q s(F)}V^{h(F)}W^{c_q(F)},}
\]
where the sum ranges over rooted-forest isomorphism types on \(b\) vertices. The polynomial and every unit-conjugacy-class size depend on \(G\) **only through its order**.

For example, at \(b=4,q=2\), the centralizer marginal is
\[
192W^9+96W^{19}+192W^{25}+96W^{45}+80W^{81}+48W^{165}+24W^{441}+W^{6561}.
\]
There are nine unit-conjugacy classes but only eight distinct centralizer sizes: different rooted-forest shapes can have the same commutant cardinality. The coefficients sum to \(729\).

## Assumptions and scope

The action is on exactly one distinguished fixed basepoint and \(b\) free regular orbits. Maps preserve \(0\) and commute with the **left** action of \(G\). They are not required to be injective, linear, or group homomorphisms. Composition is ordinary function composition. Nilpotence means \(f^k=z\), not the absence of nonzero values. If \(q=1\), the distinguished-point requirement is part of the definition; an unrestricted set map could move \(0\), and is not counted. The formulas hold also for nonabelian \(G\). The nilpotency index is the smallest positive \(k\) with \(f^k=z\).

## Proof

**1. Complete parameterization and acyclicity.** Choose the representatives \((1_G,i)\) on the \(b\) regular orbits. An equivariant, basepoint-preserving self-map is uniquely described by, for every \(i\in[b]\), either sending the whole orbit to \(0\), or choosing a target \(p(i)\in[b]\) and a phase \(a_i\in G\), with \(f(g,i)=(ga_i,p(i))\). Extend \(p\) by \(p(0)=0\). Because every nonzero orbit map is a bijection onto its target orbit, \(f\) is nilpotent exactly when its directed parent arrows \(i\to p(i)\) have no directed cycle away from \(0\). Thus the arrows form a rooted forest attached to \(0\).

**2. Simultaneous phase normalization, including nonabelian groups.** Units act by arbitrary permutations of the \(b\) regular orbits together with independent right multiplications by group elements. For the forest \(p\), choose the unit phases recursively from the roots towards the leaves so that conjugation replaces each nonzero edge phase \(a_i\) by \(1_G\); no cyclic consistency requirement occurs. In detail, for a gauge unit with phases \(d_i\), conjugation replaces an edge label by \(d_i^{-1}a_i d_{p(i)}\), up to the harmless choice of conjugation convention. Set \(d_i=a_i d_{p(i)}\) recursively for each nonroot \(i\). Consequently all phase assignments on one labelled forest are unit-conjugate. Relabeling permits precisely rooted-forest isomorphisms, giving the classification. The stabilizer of the normalized map in the unit group has \(a(F)\) forest-label automorphisms and \(q^{r(F)}\) consistent phase assignments (one arbitrary common choice for each component). Since \(|M^\times|=b!q^b\), orbit-stabilizer gives \(L_q(F)\).

**3. Rank and index.** The image contains \(0\), and the only nonzero image orbits are the parent vertices having at least one child. Each is a regular orbit with exactly \(q\) elements. Hence the image cardinality is \(1+q s(F)\). A vertex at depth \(d\) reaches \(0\) after exactly \(d\) applications; all vertices reach it after \(h(F)\) steps and some do not earlier. This proves the index statement.

**4. Recursion for the *whole* centralizer.** Fix the normalized representative \(f\). For a second pointed equivariant map \(g\), write \(y(v)=0\) or \(y(v)=w\in F\) for its target orbit and attach an independently chosen group phase \(\gamma_v\) whenever \(y(v)\ne0\). The equality \(fg=gf\) at the representative of the orbit \(v\) implies the following and is equivalent to it:

- If \(y(p(v))=0\), then either \(y(v)=0\) or \(y(v)\in R\). In the latter case \(\gamma_v\) is arbitrary, giving \(q\) phase choices.
- If \(y(p(v))=w\ne0\), then \(y(v)\in C(w)\), and the corresponding phase is **forced** to equal \(\gamma_{p(v)}\); thus this choice carries no additional factor \(q\).

These statements also hold when \(p(v)=0\), because \(g(0)=0\). Every vertex belongs to a unique parent chain, so constraints on different children are independent after the parent's target and phase have been fixed. Define \(H_v(0)\) to count valid assignments on the descendants of \(v\) conditional on \(g(v)=0\). Define \(H_v(w)\), for nonzero \(w\), to count valid descendant assignments conditional on \(g(v)=(\gamma,w)\) for any one fixed phase \(\gamma\). These counts do not depend on the value of that fixed phase, because all nonzero-edge phases in \(f\) are normalized. Multiplying the allowed choices for each child proves exactly the two displayed recursions, from the leaves upward. Finally, the parents of the roots are \(0\) and their subtrees partition all nonroot vertices, so multiplying the root contributions proves the expression for \(c_q(F)\). This proves the result for an arbitrary finite, not necessarily abelian, group.

**5. Exhaustive synthesis.** Each rooted-forest isomorphism type occurs in exactly one unit orbit by Step 2. Steps 3–4 give its three statistics. Summing with orbit multiplicities proves the polynomial. No finite checking is used to infer the statements for arbitrary \(b\) or \(G\).

## Verification

Run the self-contained Python 3 file `verify.py` from the same directory: `python3 verify.py`. It enumerates all parent functions at \(b\le5\), tests acyclicity, and checks the previously known weighted nilpotent count \((1+bq)^{b-1}\) for \(q=1,2,3,6\). Independent full commutation enumeration checks the recursion for cyclic groups of orders two, three and six, and also the nonabelian group \(S_3\), through \(b=3\); the order-two case is checked through \(b=4\). Direct conjugation enumeration checks the orbit-size formula through \(b=3\) for all these groups. The script prints `NILPOTENT_POINTED_GSET_CENTRALIZERS_PASSED` upon success. These are finite checks of examples; the general proof is above.

## Relationship to prior work

Castillo-Ramírez and Ruiz-Medina (arXiv:2203.12158, initially public on 2022-03-23) study equivariant endomorphism monoids and their units, and establish group-action/wreath-product foundations, but not the nilpotent centralizer distribution proved here. Al-Aadhami's 2017 thesis, publicly deposited 2018-02-26, already gives the **total labelled nilpotent count** for partial equivariant transformations. In the present homogeneous pointed case this known count is \((1+bq)^{b-1}\); it is used only as a cross-check and is **not presented as new**. Earlier work by Araújo and Konieczny (2013) characterizes centralizing maps in the full transformation semigroup by functional-digraph homomorphisms, which covers the unlabelled, unrestricted mapping setting and supports the recursion's general mechanism. It does not directly state the finite-group-equivariant, phase-normalized unit-orbit and cardinality-refined spectrum. Konieczny and Lipscomb (1998) treat partial transformation centralizers more generally; their complete article was not available for statement-level comparison, creating a historical-priority risk for an equivalent reduction.

## Limitations

This is confined to pointed unions of free regular orbits, not arbitrary stabilizer types. The formula counts composition centralizers inside \(M\), not centralizers in the full transformation semigroup on the underlying set. A full conjugacy classification of the **centralizer monoids themselves** is not claimed. Different rooted-forest types can share centralizer cardinalities. The earlier total nilpotent formula and general graph-homomorphism characterizations are prior work. Novelty relative to unindexed older articles is not independently certified, and no independent mathematical audit has been performed.

## References

1. A. Castillo-Ramírez and R. H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite G-set*, arXiv:2203.12158 (2022), https://arxiv.org/abs/2203.12158 (full text inspected, including §§1–3).
2. A. Al-Aadhami, *Combinatorial Questions for S wr T_n for a semigroup*, PhD thesis, University of York (2017), White Rose eTheses 19494, https://etheses.whiterose.ac.uk/id/eprint/19494/ (thesis PDF inspected, particularly Chapter 5, §5.3 and Corollary 5.3.20).
3. J. Araújo and J. Konieczny, *Centralizers in the Full Transformation Semigroup*, Semigroup Forum **86** (2013), 1–31, doi:10.1007/s00233-012-9424-0, https://doi.org/10.1007/s00233-012-9424-0 (accessible full manuscript text inspected).
4. J. Konieczny and S. Lipscomb, *Centralizers in the semigroup of partial transformations*, Math. Japonica **48** (1998), 367–376 (identified through the references of [3]; full text unavailable).
