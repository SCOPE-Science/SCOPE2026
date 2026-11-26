# Conjugacy classes of Klein-four subgroups in the hyperoctahedral groups

## Finding

Let \(B_n=C_2\wr S_n\) for \(n\ge 0\), and let \(c_n\) count the inner conjugacy classes of embedded Klein-four subgroups in \(B_n\). Put
\[
\begin{aligned}
P(z)&=\frac{1}{(1-z)^4(1-z^2)^6(1-z^4)},\\
T(z)&=\frac{1}{(1-z)^2(1-z^2)^3(1-z^4)^3},\\
C(z)&=\frac{1}{(1-z)(1-z^3)(1-z^4)(1-z^6)^2},\\
I(z)&=\frac{1}{(1-z)^2(1-z^2)}.
\end{aligned}
\]
Then
\[
\sum_{n\ge0}c_nz^n=\frac{P(z)+3T(z)+2C(z)}6-I(z).
\]
In particular \(c_n\) is a quasipolynomial of degree ten with period dividing twelve, and
\[
c_n=\frac{n^{10}}{1536\,10!}+O(n^9).
\]
The values for \(0\le n\le 10\) are \(0,0,2,7,23,51,116,223,431,762,1341\).

## Assumptions and scope

We represent \(B_n\) by signed permutation matrices of the coordinate lines, with \(B_0\) the trivial group. We count classes under inner conjugation by \(B_n\), not under arbitrary automorphisms of \(B_n\). A subgroup and its conjugates are counted without any choice of generators. This is an ordinary generating series for subgroup classes, not a labeled enumeration of all embeddings.

## Proof

Put \(K=C_2\times C_2\). A homomorphism \(K\to B_n\) gives a signed action on the coordinate lines. A transitive orbit of the underlying line action is \(K/H\), with \(H\le K\). A chosen coordinate line in this orbit has stabilizer \(H\), which acts on the line by a character \(\chi:H\to C_2\). A basis can be chosen by transporting a unit vector from that line with coset representatives; all signs of the resulting action are then determined by \(\chi\). Choosing other coset representatives changes only the basis signs. Since \(K\) is abelian, changing the starting line does not change \(H\) or \(\chi\). Hence target-conjugacy classes of homomorphisms are multisets of transitive signed types \((H,\chi)\). The types have sizes one, two and four, in numbers four, six and one, respectively.

An injective homomorphism identifies \(K\) with its image. Two such homomorphisms have conjugate images precisely when they differ by conjugation in \(B_n\) and precomposition by a source automorphism. Thus we act on the target-conjugacy classes by \(\operatorname{Aut}(K)\cong S_3\). A cycle of length \(\ell\) of types of size \(d\) contributes \((1-z^{d\ell})^{-1}\) to the series of fixed multisets, since all its types must have the same multiplicity. The identity yields \(P\). A transposition permutes the three nontrivial characters of \(K\) and the three order-two subgroups, fixing one of each. It fixes the trivial character of \(K\); for the size-two types it preserves the trivial/nontrivial character distinction. Thus it has cycle patterns \(1^2 2\) on the size-one types and \(1^2 2^2\) on the size-two types. A three-cycle similarly has patterns \(1\,3\) and \(3^2\). Both fix the size-four type. They give \(T\) and \(C\). Burnside's lemma gives \((P+3T+2C)/6\) for all source-automorphism orbits.

To retain only injective maps, remove all orbits of maps with trivial or cyclic image. The source automorphisms act transitively on the nonzero quotient maps \(K\to C_2\), so this removal amounts to one class per target-conjugacy class of an element of order dividing two, including the identity. A signed permutation is classified up to conjugacy by the lengths of its cycles and the product of signs on each cycle: conjugating by coordinate sign changes normalizes every cycle to have all but one sign positive, and permuting coordinates reorders cycles of each type. An element of order dividing two can have positive and negative signed fixed points and positive signed two-cycles only. These give exactly \(I(z)\). Subtracting proves the series for \(c_n\).

At \(z=1\) only \(P\) has pole order eleven; its leading Laurent term is \((1-z)^{-11}/256\). All other poles have order at most ten and lie at twelfth roots of unity. The signed sum is proper rational, so partial fractions give a quasipolynomial for every \(n\ge 0\), with period dividing twelve. Only the pole of order eleven contributes at degree ten, with leading coefficient \(1/(1536\,10!)\).

## Verification

Run `python verify.py` with Python 3.10 or later and no extra dependencies. It expands the rational series using integer arithmetic and independently constructs the conjugacy classes of actual subgroups through rank five, conjugating by generators of the signed permutation group. This is a finite check; the proof gives the all-rank claim.

## Relationship to prior work

Tamanoi, Theorem C (1-16) and Theorem D (1-17), gives the general equivariant-bundle and wreath-product homomorphism framework. Its point specialization gives \(P(z)\), the series for target-conjugacy classes of homomorphisms, but does not quotient by source-generator changes or impose faithfulness. The further \(S_3\) action on the signed types and the deletion of noninjective maps give the subgroup-class series here. The count of individual embedded subgroups, rather than subgroup classes, follows from Tamanoi's exponential formula by specializing \(M\) to a point and applying kernel inclusion-exclusion; it is not a claimed contribution. Burns and Pfeiffer address maximal-order abelian subgroups of finite Coxeter groups, not all subgroup classes with image isomorphic to \(C_2^2\).

## Limitations

Only Klein-four subgroup classes under inner conjugation are enumerated. The computation does not cover higher elementary abelian ranks or normalizers. The literature comparison does not rule out an unindexed equivalent subgroup-class census.

## References

- H. Tamanoi, *Generalized orbifold Euler characteristics of symmetric orbifolds and covering spaces*, Algebraic & Geometric Topology 3 (2003), 791–856. DOI: 10.2140/agt.2003.3.791. https://arxiv.org/abs/math/0309133
- J. M. Burns and G. Pfeiffer, *Maximal order Abelian subgroups of Coxeter groups*, Glasgow Mathematical Journal 65 (2023), 114–120. DOI: 10.1017/S0017089522000143.
