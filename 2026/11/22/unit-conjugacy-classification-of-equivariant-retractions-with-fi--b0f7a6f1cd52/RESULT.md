# Unit-conjugacy classification of equivariant retractions with fixed and free orbits

## Finding
Let \(G\) be a nontrivial finite group of order \(q\ge2\), and consider the finite left \(G\)-set
\[
X=(\{1,\ldots,a\}\text{ with trivial action})\;\sqcup\;(G\times\{1,\ldots,b\}),
\qquad a,b\in\mathbb Z_{\ge0},\quad a+b>0.
\]
Let \(E_G(X)=\{e\in\operatorname{End}_G(X):e^2=e\}\), with the unit group \(U=\operatorname{Aut}_G(X)\) acting by conjugation. Every \(U\)-orbit in \(E_G(X)\) corresponds bijectively to a pair of finite multisets
\[
\mathcal A=\{(s_1,t_1),\ldots,(s_k,t_k)\},\quad s_i\ge1,\ t_i\ge0;
\qquad \mathcal B=\{c_1,\ldots,c_\ell\},\quad c_j\ge1,
\]
satisfying \(\sum_i s_i=a\) and \(\sum_i t_i+\sum_j c_j=b\). An \((s,t)\) entry represents one fixed image point, whose inverse image comprises \(s\) fixed points (including that image point) and \(t\) free \(G\)-orbits. A \(c\) entry represents one free image orbit whose inverse image comprises \(c\) free \(G\)-orbits (including itself). Its image cardinality is \(k+q\ell\).

If \(\mu_{s,t}\) is the multiplicity of \((s,t)\) in \(\mathcal A\), and \(\nu_c\) is the multiplicity of \(c\) in \(\mathcal B\), the size of this **individual conjugacy orbit** is
\[
\boxed{\frac{a!\,b!\,q^{\sum_c(c-1)\nu_c}}
{\displaystyle\prod_{s\ge1,t\ge0}\mu_{s,t}!\big((s-1)!\,t!\big)^{\mu_{s,t}}
\prod_{c\ge1}\nu_c!\,\big((c-1)!\big)^{\nu_c}}.}\tag{1}
\]
The complete rank-refined number \(K_{a,b}^{(q)}(z)\) of **conjugacy orbits**, rather than labeled elements, is therefore determined by
\[
\boxed{\sum_{a,b\ge0}K_{a,b}^{(q)}(z)\,x^a y^b
=\prod_{s\ge1,t\ge0}(1-zx^s y^t)^{-1}
\prod_{c\ge1}(1-z^qy^c)^{-1}.}\tag{2}
\]
All infinite products are formal power series: each coefficient in \(x,y\) is a finite sum. In particular, the **unrefined number of conjugacy classes is independent of the isomorphism type and even the order of every nontrivial finite group**:
\[
\boxed{K_{a,b}^{(q)}(1)=[x^a y^b]
\prod_{s\ge1,t\ge0}(1-x^s y^t)^{-1}\prod_{c\ge1}(1-y^c)^{-1}.}\tag{3}
\]
The labeled count, in contrast, does depend on \(q\):
\[
\boxed{|E_G(X)|=\sum_{k=0}^a\sum_{\ell=0}^b
\binom ak\binom b\ell k^{a-k}(k+q\ell)^{b-\ell}.}\tag{4}
\]
The convention \(0^0=1\) applies. Formula (4) is included as a reconciliation check against known single-idempotent enumerations, not as an independent novelty claim.

## Assumptions and scope
The action on the \(a\) distinguished singleton orbits is trivial. Each of the other \(b\) orbits is free and regular, so \(G\) is required to be nontrivial to keep the two isotropy types distinct. Maps are total \(G\)-equivariant self-maps, with function composition. A unit is a bijective equivariant map; conjugacy is \(e\mapsto ueu^{-1}\) with \(u\in U\), **not** conjugacy by arbitrary set permutations. The coefficient exponent of \(z\) is the number of **points** in the image, \(k+q\ell\), not the number of transitive image orbits. The empty \(G\)-set may be added to (2) as its unique empty idempotent, accounting for the constant coefficient \(1\); it is excluded from the stated nonempty classification simply for clarity. Arbitrary finite groups, including nonabelian groups, are covered.

## Proof
**1. Equivariant maps and idempotence.** Equivariant maps from singleton orbits must take singleton values. A free orbit \(G\times\{j\}\) may map to any singleton (in exactly one way per target singleton), or to another free orbit by a map \(g\mapsto gh\), determined by a single group element \(h\in G\); hence there are \(q\) ways for any specified free target orbit. Equivariant maps cannot take a singleton into a free orbit because free orbits have no \(G\)-fixed points. Every equivariant idempotent fixes its image **pointwise**. Thus each singleton image is a rooted star collecting some singleton sources and free-orbit sources, whereas each free image orbit is a rooted star collecting only free-orbit sources. The relevant disjoint fiber sizes are precisely the \((s,t)\) and \(c\) above, with the stated sum constraints. Conversely any such choice of rooted stars, together with group phases on arrows between free orbits, specifies a unique idempotent.

**2. Classification modulo units.** The unit group is \(S_a\times (G\wr S_b)\): the first factor permutes singleton orbits, and the second permutes free orbits and independently translates their coordinates. The factors cannot interchange orbit types because \(q>1\). Permuting the source and root orbits of a fixed rooted-star forest carries precisely those forests with matching unordered \((s,t)\)- and \(c\)-multiplicity data to each other. For each non-root free orbit pointing to a free root, independently translating its source coordinate changes the arrow's right-multiplication phase by an arbitrary element of \(G\), while no other arrow originates in that orbit. Choose the translation that makes that arrow phase the identity. This works simultaneously for all free-to-free edges, without using commutativity of \(G\) and without changing the underlying rooted stars. Edges into singleton roots have no phase, and identity maps on free roots are forced by idempotence. Therefore all phase assignments on the same rooted forest are unit-conjugate. Distinct multisets cannot be conjugate because units preserve orbit types, image roots and their preimage cardinalities. This gives the claimed complete invariant.

**3. Individual orbit size.** First label the \(a\) fixed points and \(b\) free orbits. For each distinct fixed-root type \((s,t)\), there are \(\mu_{s,t}\) indistinguishable rooted stars with \(s\) singleton members and \(t\) free-orbit members. Exactly one of the \(s\) singleton members is designated its root; exchanging identical stars changes nothing. Likewise each free-root star of size \(c\) has a distinguished free root and \(c-1\) free satellites; stars of identical \(c\) are indistinguishable. The resulting number of rooted-star forests is
\[
\frac{a!\,b!}{\displaystyle\prod_{s,t}\mu_{s,t}!\big((s-1)!\,t!\big)^{\mu_{s,t}}\prod_c\nu_c!\big((c-1)!\big)^{\nu_c}}.
\]
For every free satellite of a free root there are independently \(q\) right-translation labels, and there are exactly \(\sum_c(c-1)\nu_c\) such satellites. Multiplying by this power of \(q\) proves (1). All labeled idempotents of the given profile form one unit orbit by step 2, so this labeled count is exactly its orbit cardinality.

**4. Euler products and independence.** The possible fixed-root block types \((s,t)\), each contributing \(x^s y^t z\), may occur with any multiplicity; the free-root block types \(c\), each contributing \(y^c z^q\), may also occur with any multiplicity. Choosing these multiplicities subject only to the two sum constraints gives (2), with one monomial per unit orbit. Setting \(z=1\) gives (3), which has no group parameter. This independence is specific to the conjugacy **class number**, not to their sizes or rank exponents.

**5. Labeled-count cross-check.** If exactly \(k\) singleton points and \(\ell\) free orbits are chosen as image roots, their choices contribute \(\binom ak\binom b\ell\). Each of the \(a-k\) remaining singleton points chooses one of the \(k\) singleton roots. Each of the \(b-\ell\) remaining free orbits chooses one of \(k\) singleton roots (with unique equivariant map) or one of \(\ell\) free roots with \(q\) phase choices. This gives \(k^{a-k}(k+q\ell)^{b-\ell}\), hence (4), which equals the sum of (1) over all profiles.

## Verification
The standalone `verify.py` independently generates every idempotent by composing explicit equivariant orbit maps, canonically assigns each profile, and checks all three ways of counting: (i) exact enumeration versus (4); (ii) the distinct generated profile set versus coefficient extraction in (2), using separate recursive multiset generation; (iii) each profile's labeled population versus (1). It additionally constructs the actual full unit-conjugacy orbit of one representative by breadth-first search under generators of \(S_a\), \(S_b\), and coordinate translations, and compares it to the entire profile bucket. The script covers 33 nonempty test cases for \(G=C_2\), \(C_3\), and the nonabelian \(S_3\), with up to three fixed and three regular orbit positions where computationally feasible. Its output ends with `GSET_RETRACTION_UNIT_ORBITS_VERIFIED cases=33`. For example, \((a,b)=(2,2)\) has \(9\) conjugacy classes for every nontrivial \(G\), whereas the labeled idempotent counts are \(29\) for \(C_2\) and \(53\) for \(S_3\). All finite experiments support but do not replace the arbitrary-group proof above.

## Relationship to prior work
Castillo-Ramirez and Ruiz-Medina [1] establish the general finite-\(G\)-set endomorphism and unit-group framework and calculate relative ranks, not the distribution of unit-conjugacy classes of idempotents for a mixture of fixed and free orbits. Ruiz-Medina's subsequent thesis [2] provides an extended survey and structural results on these monoids; its relevant main results do not supply (1)–(3). The thesis of Al-Aadhami [3], Section 4.3.1, gives the standard labeled single-idempotent count for the homogeneous free-\(G\)-set wreath product, which is recovered when \(a=0\) in (4), but neither addresses mixed stabilizer types nor provides this mixed conjugacy-orbit census. Existing homogeneous simultaneous untwisting results [4] cover arbitrary commuting families on free \(G\)-sets; their homogeneous premise does not imply the mixed rooted-star classification. Previously recorded labeled rank formulas for all permutation centralizers [5] concern the count of **elements**, not their automorphism orbits. The genuine new assertion assessed here is the mixed-isotropy unit-conjugacy classification, orbit cardinality (1), and the group-independent all-rank orbit Euler product (2), not the classical rooted-star construction alone.

## Limitations
The two orbit types must be the trivial singleton \(G/G\) and free regular \(G/1\); arbitrary intermediate stabilizers could require additional incidence constraints and nontrivial phase stabilizers. The unit-conjugacy classes depend only on \(a,b\), but the rank-refined classes depend on \(q\), and labeled orbit sizes depend on \(q\). The result does not classify multiple commuting idempotents, Green's relations, or the automorphism group of the full monoid. Historic priority remains provisional: an earlier general theorem on group-set retraction isomorphism classes or permutation centralizers might subsume the classification after a nontrivial specialization, even though it was not located in the inspected literature. 

## References
[1] A. Castillo-Ramirez and R. H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite \(G\)-set*, arXiv:2203.12158v1 (2022-03-23). https://arxiv.org/abs/2203.12158

[2] R. H. Ruiz-Medina, *El monoide de endomorfismos de \(G\)-conjuntos: estructuras y otras propiedades algebraicas*, arXiv:2408.10209v1 (2024-07-12). https://arxiv.org/abs/2408.10209

[3] A. D. H. Al-Aadhami, *Combinatorial Questions for \(S\wr_n\mathcal T_n\) for a Semigroup*, University of York thesis (public repository deposit 2018-02-26), especially Section 4.3.1. https://etheses.whiterose.ac.uk/id/eprint/19494/

[4] *Simultaneous untwisting of commuting retractions on homogeneous finite group-sets*, published mathematical research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-simultaneous-untwisting-of-commuting-retractions-on-homogeneous--19779e27b698

[5] *Rank enumeration and minimum retraction size in permutation-centralizer monoids*, published mathematical research record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rank-enumeration-and-minimum-retraction-size-in-permutation-cent--46b24971b86b
