# Height–diameter separation in direct sums of three-dimensional Heisenberg Lie algebras

## Finding

For each field \(F\) and integer \(t\ge2\), the reduced commuting graph of the direct sum \(L=H_3(F)^{\oplus t}\) has **LSG-height exactly two but graph diameter exactly three**. Moreover, its only LSG-closed subspaces are \(\{0\}\) and the full central quotient. The pairs at maximum distance admit a coordinatewise determinant criterion, giving an exact finite-field count:

\[
\#\{(u,v):\operatorname{dist}(u,v)=3\}
=\big((q^2-1)(q^2-q)\big)^t
\qquad(F=\mathbb F_q).
\]

Thus this natural family gives a uniform, explicit strict case of the height-versus-diameter inequality raised in Open Problem 3 of Le–Duong–Nguyen [1].

## Assumptions and scope

Let \(F\) be an arbitrary field, including characteristic two. The three-dimensional Heisenberg Lie algebra \(H_3(F)\) has basis \(a,b,z\) and only nonzero basic bracket \([a,b]=z\). Fix \(t\ge2\) and take a **direct** sum of \(t\) such algebras: all central basis vectors \(z_i\) are independent. Then

\[
V:=L/Z(L)=\bigoplus_{i=1}^{t} F^2,
\quad [u,v]=\sum_{i=1}^t\det(u_i,v_i)z_i.
\]

The reduced commuting graph \(\Gamma_R\) has the nonzero vectors \(V\setminus\{0\}\) as vertices, and distinct vectors are adjacent exactly when all coordinate determinants vanish. For nonzero \(u\), the closed-neighborhood subspace is

\[
C(u)=\{v\in V:\det(u_i,v_i)=0\text{ for all }i\}.
\]

For a vector subspace \(W\le V\), define \(N(\{0\})=\{0\}\) and
\(N(W)=\sum_{0\ne w\in W}C(w)\). The LSG-height \(h(u)\) is the number of strict enlargements in the chain \(Fu,N(Fu),N^2(Fu),\ldots\), stopped when it becomes constant. This is the convention of [1], Definitions 2.9, 2.12 and 2.14. A subspace \(W\) is LSG-closed when \(N(W)=W\). Distances refer to the simple graph, not to its linear closure operation.

## Proof

**First neighborhood.** For any nonzero \(u=(u_1,\ldots,u_t)\), the independence of the central \(z_i\)'s gives

\[
C(u)=\bigoplus_{i=1}^t C_i(u_i),\qquad
C_i(u_i)=\begin{cases}F^2,&u_i=0,\\ Fu_i,&u_i\ne0.\end{cases}
\]

Every \(C_i(u_i)\) contains a nonzero vector, hence \(C(u)\) contains nonzero vectors \(a\) and \(b\) supported in coordinate planes \(1\) and \(2\), respectively. Since \(u\ne0\), at least one \(C_i(u_i)\) is a proper line, so \(C(u)\) is proper in \(V\). On the other hand \(C(u)\supsetneqq Fu\): its dimension is at least \(t\ge2\). Thus \(N(Fu)=C(u)\) is a proper strict enlargement.

**Second neighborhood and closed subspaces.** The vectors \(a,b\) belong to \(C(u)\). As their supports are disjoint, \(C(a)\) contains every vector supported away from the first coordinate and \(C(b)\) contains every vector supported in the first coordinate. Consequently \(C(a)+C(b)=V\), whence

\[
N^2(Fu)=N(C(u))\supseteq C(a)+C(b)=V.
\]

The height of every nonzero \(u\) is therefore exactly \(2\). If \(W\) is LSG-closed and \(W\ne\{0\}\), choose \(u\in W\setminus\{0\}\). By monotonicity, \(V=N^2(Fu)\subseteq N^2(W)=W\), so \(W=V\). Both \(0\) and \(V\) are plainly closed.

**Distance-three criterion.** Two nonzero vectors \(u,v\) possess a common nonzero commuting neighbor if and only if there is at least one \(i\) for which \(u_i,v_i\) are linearly dependent. Indeed, a common commuting neighbor \(w\) satisfies \(w_i\in u_i^\perp\cap v_i^\perp\) in each coordinate plane; in a nondegenerate two-dimensional alternating plane, this intersection is nonzero precisely when \(u_i,v_i\) are dependent (including a zero member). Such a nonzero \(w\) supported in that plane is a common neighbor, using the closed-neighborhood convention. If \(w\) equals an endpoint, then those endpoints commute and their distance is at most one; otherwise they have distance at most two. Conversely, if every pair \((u_i,v_i)\) is independent, the common perpendicular is zero in all coordinates, so no nonzero common neighbor exists. In this latter case construct a path of length three: choose two different indices \(i\ne j\); let \(a\) be supported in \(i\) with value \(u_i\), and let \(b\) be supported in \(j\) with value \(v_j\). Each coordinate projection of either endpoint is nonzero by independence, so the four vertices \(u,a,b,v\) are distinct where consecutive, and
\(u\sim a\sim b\sim v\). Hence the distance equals three precisely in the coordinatewise independent case. Such pairs exist over every field; therefore the diameter is three. The equality of the original and reduced graph diameters is also Theorem 4 of [1]; alternatively, central lifts do not change commutators, so paths lift without changing maximal distance.

**Finite-field count.** In \(F_q^2\), there are \(q^2-1\) choices of nonzero \(u_i\), followed by \(q^2-q\) choices of \(v_i\) outside its one-dimensional span. Choices are independent across \(i=1,\ldots,t\); multiplying gives the displayed number of **ordered** distance-three pairs. The count is over quotient vectors, not central lifts, projective points or unordered pairs.

**One-summand boundary.** For \(t=1\), \(C(u)=Fu\) for every nonzero vector \(u\in F^2\). Every one-dimensional subspace is closed, every vertex has height zero, and the reduced graph is a disjoint union of complete graphs on nonzero vectors of each one-dimensional subspace, with infinite diameter.

## Verification

The accompanying dependency-free `check_rcg.py` exhaustively constructs the quotient commuting graph, computes graph distances, iterated linear-neighborhood ranks, and counts ordered distance-three pairs for the following cases:

| Factor half-ranks | Field order | Vertices | Height | Diameter | Ordered distance-three pairs |
|---|---:|---:|---:|---:|---:|
| \((1)\) | 2 | 3 | 0 | disconnected | 0 |
| \((1)\) | 3 | 8 | 0 | disconnected | 0 |
| \((1,1)\) | 2 | 15 | 2 | 3 | 36 |
| \((1,1)\) | 3 | 80 | 2 | 3 | 2304 |
| \((1,1,1)\) | 2 | 63 | 2 | 3 | 216 |

Two additional controls, half-ranks \((2)\) and \((2,1)\) over \(F_2\), verify height two and diameter two; they are not new claims of this theorem. The script reports `HEISENBERG_RCG_HEIGHT_DIAMETER_OK` only after all assertions pass. These finite checks corroborate, but do not replace, the all-field proof above.

## Relationship to prior work

Le, Duong and Nguyen [1] define LSG-neighborhood height, show that RCGs preserve connectivity and diameter and respect direct sums (Theorems 4–5), and ask for equality cases of height and diameter in Open Problem 3. Their full text does not compute the present Heisenberg product family, its strict inequality, or its distance-three locus.

Ha and coauthors [2] already prove that commuting graphs of direct sums of two nonabelian Lie algebras have diameter at most three (Proposition 6), and their Proposition 21 shows diameter two if the central quotient dimension exceeds twice the derived-algebra dimension. That latter implication **covers the diameter-two case of Heisenberg products with at least one larger symplectic block**, which is deliberately excluded from this theorem. Their Theorem 24 covers individual higher-dimensional Heisenberg algebras, but does not provide the all-three-dimensional-summand strict-height classification or pair census.

Duong and coauthors [3] describe commuting graph properties of an individual Heisenberg Lie algebra. In particular, the three-dimensional one has projective-line components, consistent with the one-summand boundary here; the direct-sum height and distance-three distribution are different questions.

## Limitations

The theorem concerns direct sums with **independent** central lines, not central products, general two-step nilpotent Lie algebras, or arbitrary products of LSGs. The finite-field formula counts ordered pairs in the reduced graph only. Correctness is established by the written algebraic proof and limited exhaustive checks; independent mathematical review and exhaustive historical priority assessment have not occurred. Search cannot exclude every older unindexed special case.

## References

[1] Vu A. Le, Hoa Q. Duong, Tuan A. Nguyen, *Linear structure graphs associated with commuting graphs of Lie algebras*, arXiv:2611.10788v1 (first public submission 2026-11-07), Sections 2, 4 and Open Problem 3. https://arxiv.org/abs/2611.10788

[2] *Diameter of Commuting Graphs of Lie Algebras*, arXiv:2405.06521 (2024), especially Propositions 6 and 21 and Theorem 24. https://arxiv.org/pdf/2405.06521

[3] H. Q. Duong and collaborators, *On Some Graph Properties of Heisenberg Lie Algebras* (2025), DOI:10.54607/hcmue.js.22.10.4490(2025), especially the discussion of three-dimensional Heisenberg commuting graphs. https://journal.hcmue.edu.vn/index.php/hcmuejos/article/download/4490/3813/20931
