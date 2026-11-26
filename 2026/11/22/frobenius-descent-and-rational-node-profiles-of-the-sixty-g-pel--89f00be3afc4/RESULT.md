# Rational-node profiles of Frobenius-invariant Göpel tetrads

## Finding

Let \(C\) be a smooth genus-two curve over an odd finite field \(k=\mathbb F_q\). A Göpel tetrad on its singular Jacobian Kummer quartic is an unordered set of four geometric nodes with no triple on a trope. For each Göpel tetrad \(A\) invariant under Frobenius \(F\), let \(j(A)\) be the number of its nodes individually rational over \(k\). The polynomial
\[
P_\lambda(u)=\sum_{F(A)=A}u^{j(A)}
\]
depends only on the partition \(\lambda\) for Frobenius on the six geometric Weierstrass points. It is given by

| Weierstrass Frobenius type | \(P_\lambda(u)\) |
|---|---|
| \(1^6\) | \(60u^4\) |
| \(2,1^4\) | \(6+6u^4\) |
| \(3,1^3\) | \(0\) |
| \(2^2,1^2\) | \(3+4u^2+u^4\) |
| \(4,1^2\) | \(1+u^2\) |
| \(3,2,1\) | \(0\) |
| \(5,1\) | \(0\) |
| \(2^3\) | \(3+12u^2+u^4\) |
| \(4,2\) | \(1+u^2\) |
| \(3^2\) | \(3u\) |
| \(6\) | \(u\) |

In particular a setwise rational tetrad can have no rational node. Over \(\mathbb F_{q^m}\), the same table applies to the cycle type of \(F^m\), so it gives the analogous distribution over every extension.

## Assumptions and scope

No ordinarity or genericity is required. Rationality of a tetrad means invariance of the set, not of each node or any associated Cremona map. The table is conditional on the branch permutation and makes no claim that all types occur over each fixed finite field. It refines, but does not redetermine as a novelty claim, the unweighted Göpel orbit spectrum and tetrad zeta functions.

## Proof

Write \(B\) for the six Weierstrass points. The two-torsion node space is \(V=\{A\subseteq B: |A|\text{ even}\}/(A\sim B\setminus A)\). Its group law is symmetric difference modulo complement, and the Weil pairing is \(\langle A,D\rangle=|A\cap D|\bmod 2\). This classical description is Galois-equivariant. Every class is represented uniquely by the empty set or a two-element set. Together with the classical Kummer incidence description, the Göpel tetrads are the affine translates of the totally isotropic two-dimensional subspaces. These geometric identifications are prior work.

Two distinct nonzero classes represented by two-element sets are orthogonal exactly when their pairs are disjoint, and their sum is represented by the complementary pair. Thus a maximal isotropic subspace consists of zero and the three edges of a perfect matching of \(B\). Its own tetrad has \(j=1+\#\{\text{matching edges fixed by }F\}\) when the matching is stable. The three other cosets have a simple form: for any two matching edges \(B_1,B_2\), the four crossing pairs \(\{x,y\}\) with \(x\in B_1,y\in B_2\) make one coset. Adding a node of the direction matching exchanges an endpoint, or both endpoints, giving exactly these four nodes. Equivalently each such coset marks the remaining edge \(M\). The coset is stable exactly if \(M\) is fixed and the partition \(B_1|B_2\) of its complement is invariant.

There are two cases for a fixed marked tetrad. If Frobenius fixes both two-element blocks individually, then a crossing pair is fixed only when both endpoints are fixed individually. Thus \(j=4\) if the action on the complement is the identity and \(j=0\) otherwise. If Frobenius exchanges the blocks, a crossing pair is fixed exactly when its two endpoints are exchanged; the count is \(j=2\) if \(F^2\) is the identity on the blocks and \(j=0\) otherwise.

For clarity, the following finite enumeration using these rules gives every coefficient shown. On six labels use a permutation with consecutive cycles of lengths \(\lambda\). List the 15 perfect matchings by pairing the first unused label with any other unused label and iterating. For each matching, skip it if its three edges are not preserved as a set. Otherwise add \(u^{1+b}\), where \(b\) is the number of individually preserved edges. For each of these \(b\) edges as the mark, apply the preceding crossing-pair rule to the remaining two edges and add one monomial. This processes every stable affine coset exactly once. For instance, for a transposition the moved pair occurs in each of the three stable matchings. The origin-containing coset and the coset marking that pair both have four fixed nodes; the two other choices of mark give zero. For a product of two three-cycles none of the three stable matchings has an individually fixed edge, so their three origin-containing tetrads have one rational node each. All other rows follow by the same finite rule. Conjugation does not change the result, and applying the rule to powers proves the extension assertion.

## Verification

Run `python3 gopel_verify.py` with Python 3.10 or newer. The standard-library program computes the rational-node profiles for all 720 permutations; compare the `fixed-node-profile` fields with the coefficient table above. It also compares the symplectic-model sets with the 60 tetrads obtained independently from the no-three-on-a-trope test. The auxiliary unweighted cycle spectra printed by the script are consistency checks, not assertions of originality for those spectra.

## Relationship to prior work

Dolgachev–Keum give the geometric affine-isotropic description and Kumar treats the no-three-on-a-trope configuration. The catalogue result *Göpel and Rosenhain tetrad counts determine their joint zeta functions over finite fields* lists all eleven unweighted Göpel orbit rows for the same object and hypotheses. Specializing the present polynomial at \(u=1\) recovers its count of rational Göpel tetrads. The additional invariant is the incidence refinement *inside* invariant tetrads, separating zero, one, two and four individually fixed nodes, not the unweighted zeta function or the joint determination theorem. Historical priority for the refinement is provisional.

## References

1. I. Dolgachev and J. Keum, *Birational automorphisms of quartic Hessian surfaces*, §4, [arXiv:math/0103186](https://arxiv.org/abs/math/0103186).
2. A. Kumar, *Elliptic fibrations on a generic Jacobian Kummer surface*, §§2–3, [arXiv:1105.1715](https://arxiv.org/abs/1105.1715).
3. *Göpel and Rosenhain tetrad counts determine their joint zeta functions over finite fields*, [catalogue record 6d840aff1b1c](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-g-pel-and-rosenhain-tetrad-counts-determine-their-joint-zeta-fun--6d840aff1b1c).
