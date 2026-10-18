# Higher-order Bell orbit profiles calibrate the finite Morley-rank equivalence tower

## Finding
For each integer \(r\ge 1\), let \(\mathfrak E_r\) be the countable homogeneous structure with nested equivalence relations
\[
E_1\subseteq\cdots\subseteq E_{r-1},
\]
such that every \(E_1\)-class is infinite, every \(E_{i+1}\)-class contains infinitely many \(E_i\)-classes, and there are infinitely many \(E_{r-1}\)-classes. For \(r=1\), \(\mathfrak E_1\) is the pure countably infinite set.

Write \(B_n^{(0)}=1\) and, for \(m\ge0\),
\[
B_n^{(m+1)}=\sum_{k=1}^n {n\brace k}B_k^{(m)}.
\]
Then
\[
o_n^i(\operatorname{Aut}(\mathfrak E_r))=B_n^{(r-1)}
\quad\text{and}\quad
o_n(\operatorname{Aut}(\mathfrak E_r))=B_n^{(r)}.
\]
Moreover \(\mathfrak E_r\) has Morley rank exactly \(r\). Consequently
\[
o_n(\operatorname{Aut}(\mathfrak E_r))
=
o_n^i(\operatorname{Aut}(\mathfrak E_{r+1})).
\]

The exponential generating functions
\[
F_m(z)=\sum_{n\ge0}B_n^{(m)}\frac{z^n}{n!}
\]
satisfy
\[
F_0(z)=e^z,\qquad F_{m+1}(z)=\exp(F_m(z)-1).
\]

## Assumptions and scope
The language of \(\mathfrak E_r\) contains only the equivalence relations \(E_1,\ldots,E_{r-1}\). The structure is the Fraïssé limit of finite structures carrying a chain of nested equivalence relations, equivalently the unique countable homogeneous structure satisfying the stated infinite-branching axioms. The orbit statements concern ordered \(n\)-tuples; \(o_n^i\) counts orbits of injective tuples and \(o_n\) counts all tuple orbits.

The claim is an exact identification for this canonical tower. It does not assert that higher-order Bell numbers characterize every monadically stable structure of Morley rank \(r\), nor that these structures are extremal among all rank-\(r\) examples.

## Proof
Homogeneity implies that two finite tuples lie in the same automorphism orbit exactly when their quantifier-free nested-equivalence patterns agree.

For an injective tuple \((a_1,\ldots,a_n)\), each relation \(E_j\) induces a set partition \(\pi_j\) of \([n]\), and nesting gives
\[
\pi_1\preceq\pi_2\preceq\cdots\preceq\pi_{r-1},
\]
where \(\preceq\) means refinement. Conversely every such chain is realized in \(\mathfrak E_r\), because every finite nested-equivalence pattern belongs to its age. Therefore injective tuple orbits are exactly chains of \(r-1\) nested set partitions.

Let \(A_m(n)\) be the number of chains of \(m\) nested partitions of an \(n\)-set, with \(A_0(n)=1\). Choosing the first partition with \(k\) blocks and then a chain of \(m\) partitions of those blocks gives
\[
A_{m+1}(n)=\sum_{k=1}^n {n\brace k}A_m(k).
\]
Thus \(A_m(n)=B_n^{(m)}\), proving
\[
o_n^i(\operatorname{Aut}(\mathfrak E_r))=B_n^{(r-1)}.
\]

For an arbitrary tuple, equality of coordinates contributes an additional initial set partition before the \(E_1,\ldots,E_{r-1}\) partitions. Hence arbitrary tuple orbits are chains of \(r\) nested partitions, so
\[
o_n(\operatorname{Aut}(\mathfrak E_r))=B_n^{(r)}.
\]
The displayed shift identity follows immediately.

For Morley rank, set \(E_0\) to equality and regard the whole domain as one formal \(E_r\)-class. Quantifier elimination for this homogeneous relational Fraïssé limit reduces every unary formula over finitely many parameters to a Boolean combination of conditions \(E_j(x,a)\). An \(E_1\)-class is a pure infinite set, hence has Morley rank \(1\). Inductively, an \(E_j\)-class is partitioned into infinitely many pairwise disjoint definable \(E_{j-1}\)-classes of rank \(j-1\), so its rank is at least \(j\); quantifier elimination shows that no unary definable refinement can create a further infinite family of subsets of rank \(j\), so its rank is at most \(j\). Thus the whole domain has Morley rank exactly \(r\).

Finally, the exponential generating function recurrence is the standard Stirling-transform identity:
\[
\sum_{n\ge0}\left(\sum_{k=0}^n{n\brace k}B_k^{(m)}\right)\frac{z^n}{n!}
=
\exp(F_m(z)-1).
\]

## Verification
A standalone verifier independently generates all set partitions by restricted-growth strings, enumerates all refinement chains directly, and compares them with the Stirling-transform recurrence. It checks ranks \(1\) through \(4\) for tuple lengths through \(7\), and separately verifies the all-tuple/injective-rank-shift identity through tuple length \(10\). Running `python3 verification.py` prints `VERIFY_OK`.

The finite computation is a consistency check only. The infinite statement follows from homogeneity, realization of every finite nested-equivalence pattern, and the quantifier-elimination induction for Morley rank.

## Relationship to prior work
Bodor's classification of countable \(\omega\)-categorical monadically stable structures explicitly organizes their automorphism groups by Morley rank and uses wreath products with \(\operatorname{Sym}(\omega)\) as the operation corresponding to countably many copies. The paper proves oligomorphic closure and rank classification but does not state these exact orbit sequences.

Higher-order Bell numbers and their interpretation through iterated or nested partitions are classical; Skau and Kristensen give the recurrence and nested-partition interpretation used here. The new point is the exact model-theoretic calibration: the canonical Morley-rank-\(r\) nested-equivalence tower has injective orbit profile \(B_n^{(r-1)}\), while its full tuple profile is the next higher-order Bell row, producing the rank-shift identity above.

## Limitations
The higher-order Bell numbers themselves, their recurrence, and their nested-partition interpretation are prior mathematics. The claim is limited to their exact realization as the two natural ordered-tuple orbit profiles of the canonical nested-equivalence tower and to the resulting alignment with Morley rank.

No extremality or uniqueness statement is made for all monadically stable structures of a fixed Morley rank.

## References
1. Bertalan Bodor, *Classification of \(\omega\)-categorical monadically stable structures*, arXiv:2011.08793, first submitted 17 November 2020; Journal of Symbolic Logic 89 (2024), 460–495.
2. Ivar Henning Skau and Kai Forsberg Kristensen, *Sets of iterated Partitions and the Bell iterated Exponential Integers*, arXiv:1903.08379, 2019.
3. E. T. Bell, *The iterated exponential integers*, Annals of Mathematics 39 (1938), 539–557.
