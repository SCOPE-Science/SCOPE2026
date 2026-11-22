# Isomorphism rigidity of four-vertex multiarrow path Lie algebras

## Finding

For a field \(k\) and positive integers \(r,s,t\), take the quiver with four vertices in a directed line and \(r,s,t\) parallel arrows on the successive edges. Let \(L_k(r,s,t)\) be the Lie algebra spanned by its positive-length paths, with bracket the commutator of path concatenation. For any two positive parameter triples and **over every field**,

\[
L_k(r,s,t)\cong L_k(r',s',t')
\quad\Longleftrightarrow\quad
s=s'\ \text{and}\ \{r,t\}=\{r',t'\}.
\]

The middle multiplicity is determined intrinsically by a centralizer:

\[
s=\dim_k\bigl(C_{L_k(r,s,t)}([L,L])/[L,L]\bigr).
\]

This is stronger than classification by lower-central graded dimensions. For every integer \(h\ge1\), the two nonisomorphic Lie algebras \(L_k(2h,6h,6h)\) and \(L_k(3h,8h,3h)\) have identical dimensions \((14h,48h^2,72h^3)\) in the three lower-central graded layers but distinct intrinsic centralizer quotient dimensions \(6h\) and \(8h\).

## Assumptions and scope

All fields are permitted, including characteristic two. The quiver has precisely four vertices, with arrows only from the first to second, second to third, and third to fourth vertices, with strictly positive multiplicities. The Lie algebra is the positive-path (Jacobson radical) subspace of the associative path algebra, with its commutator Lie bracket. Paths are multiplied by concatenation if endpoints agree, and by zero otherwise. No assertion is made for quivers with additional arrows, cycles, or relations.

Put \(U=k^r\), \(V=k^s\), \(W=k^t\), corresponding to the three arrow spaces. The path basis identifies the underlying vector space with

\[
L=U\oplus V\oplus W\oplus (U\otimes V)
\oplus(V\otimes W)\oplus(U\otimes V\otimes W).
\]

A lower-central series is \(L_1=L\), \(L_2=[L,L]\), \(L_3=[L,L_2]\), \(L_4=0\).

## Proof

**Path multiplication and lower central series.** The only nonzero brackets between homogeneous positive-length path subspaces, up to antisymmetry and bilinearity, are

\[
[u,v]=u\otimes v,\quad [v,w]=v\otimes w,\quad
[u,v\otimes w]=u\otimes v\otimes w,\quad
[u\otimes v,w]=u\otimes v\otimes w.
\]

Associativity of path concatenation proves the Jacobi identity over every field. The preceding bracket table and positivity of all three multiplicities show

\[
L_2=(U\otimes V)\oplus(V\otimes W)\oplus(U\otimes V\otimes W),
\qquad L_3=U\otimes V\otimes W.
\]

Consequently, the successive quotient dimensions are

\[
\dim(L/L_2)=r+s+t,\qquad
\dim(L_2/L_3)=s(r+t),\qquad
\dim L_3=rst.
\]

**Centralizer lemma.** Since the sum of the lengths of two paths of length at least two exceeds three, \([L_2,L_2]=0\). Every vector in \(V\) also commutes with \(L_2\), so \(V+L_2\subseteq C_L(L_2)\). Write any \(x\in L\) uniquely as \(x=u+v+w+z\), where \(u\in U\), \(v\in V\), \(w\in W\), and \(z\in L_2\). For every \(a\in U,b\in V\),

\[
[x,a\otimes b]=-a\otimes b\otimes w.
\]

Since \(U,V\) are nonzero and the natural map \(w\mapsto a\otimes b\otimes w\) is injective for chosen nonzero \(a,b\), centralizing \(L_2\) forces \(w=0\). Likewise, for any \(b\in V,c\in W\),

\[
[x,b\otimes c]=u\otimes b\otimes c,
\]

and the injectivity of \(u\mapsto u\otimes b\otimes c\) forces \(u=0\). Thus, including characteristic two,

\[
C_L(L_2)=V\oplus L_2,
\qquad \dim(C_L(L_2)/L_2)=s.
\]

**Necessity of the parameter criterion.** A Lie algebra isomorphism preserves \(L_2,L_3\), their quotient dimensions, and the centralizer of \(L_2\). Hence it preserves \(s\). The first and third dimensions determine, respectively, \(r+t\) and \(rt\) once \(s\) is known. The unordered positive pair \(\{r,t\}\) is the unordered set of roots (with multiplicity) of \(T^2-(r+t)T+rt\). This inference concerns integer multiplicities, not roots in the ground field, so it remains valid in positive characteristic.

**Sufficiency.** When the ordered triples coincide, bijections of the individual arrow bases induce path-algebra and hence Lie-algebra isomorphisms. When only the outer multiplicities are interchanged, reverse every arrow and then identify the reversed four-vertex line with the original orientation read backward. The map taking each positive-length path \(p\) to minus its reversed path is a Lie-algebra isomorphism: path reversal exchanges the two products in each commutator, and the global minus sign compensates. The argument also works in characteristic two. This proves the classification.

**A lower-central collision in arbitrarily large dimensions.** For parameters \((2h,6h,6h)\) and \((3h,8h,3h)\), the above quotient formulas give \((14h,48h^2,72h^3)\) in both cases; the centralizer quotient dimensions are \(6h\) and \(8h\). Since \(h\ge1\), these Lie algebras are nonisomorphic despite the identical lower-central dimension sequences. Their common total dimension is \(14h+48h^2+72h^3\).

## Verification

The included standalone `check_line_quiver.py` constructs all positive-length paths independently and evaluates commutators, derived-space ranks, and the linear centralizer constraints over prime fields. It checks all \(27\) triples \(1\le r,s,t\le3\) in each characteristic \(2,3,5\): \(81\) exact finite tests. Each reproduces the four claimed intrinsic dimensions and is invariant under reversing the outer multiplicities. The program additionally checks the displayed family of lower-central collisions for \(h=1\). Run `python3 check_line_quiver.py`; the expected success marker is `FOUR_VERTEX_QUIVER_LIE_CLASSIFICATION_OK 81 finite tests`. The written tensor proof, not these bounded tests, establishes the all-parameter and all-field assertions.

## Relationship to prior work

Mizoguchi's 2026 three-step quiver study, arXiv:2610.25903v1, Section 4, classifies examples of total dimension at most ten and explicitly proves reversal symmetry (Lemma 4.8). The present criterion is an all-multiplicity isomorphism classification for one natural four-vertex multiarrow subfamily; it does not claim reversal symmetry itself as new. Mizoguchi and Tamaru introduced the broader positive-path Lie construction in arXiv:2405.11184, emphasizing nilpotent and geometric properties rather than the present exact isomorphism criterion.

The previously published *Commuting-pair polynomial for the three-step multiarrow line quiver* treats **the identical** \((r,s,t)\) family and derives a finite-field commuting-pair polynomial. Its proof and final claims concern commuting-pair counts, not an all-field isomorphism classification or the derived-ideal centralizer. Comparing statements, the count is a possible invariant of the same object, but its existence alone does not imply the equivalence criterion or the exhibited collision of lower-central dimensions. This close precedent is credited explicitly.

## Limitations

This classification is restricted to a strictly positive three-edge multiarrow line; no general quiver reconstruction theorem is claimed. The centralizer formula does not claim that all lower-central graded Lie algebras with the same dimensions are distinguished by that single invariant outside this family. The computation checks only small prime fields; the general assertions rest on the full proof. An older, unindexed equivalent structural criterion may exist; publication priority has not been independently established. Independent audit has not been performed.

## References

1. F. Mizoguchi, *On nilpotent Lie algebras arising from parabolic subalgebras and quivers — three-step cases*, arXiv:2610.25903v1 (first posted 2026-10-19), Section 4, especially Lemma 4.8 and Theorem 4.9. https://arxiv.org/abs/2610.25903
2. F. Mizoguchi and H. Tamaru, *Nilpotent Lie algebras obtained by quivers and Ricci solitons*, arXiv:2405.11184 (first posted 2024-05-18), Sections 1 and 3. https://arxiv.org/abs/2405.11184
3. *Commuting-pair polynomial for the three-step multiarrow line quiver*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-commuting-pair-polynomial-for-the-three-step-multiarrow-line-qui--0edf4af1aaa4, `RESULT.md`, especially Finding, Proof, and Limitations.
