# Nontrivial affine action on the \(33\)-torsion of a directed tournament Hom complex

## Finding
For the Paley tournament \(T\) on \(\mathbb Z/11\mathbb Z\), define its directed Hom complex \(X=\operatorname{Hom}(\overrightarrow C_3,T)\). The first integral homology torsion is cyclic of order \(33\). The target automorphism \(\mu(v)=3v\pmod{11}\) induces the **nonidentity** action
\[
\mu_*|_{\operatorname{Tor}H_1(X;\mathbb Z)}=\times 25\pmod{33}.
\]
Under the natural affine subgroup \(\{v\mapsto av+b\mid a\in Q,\ b\in\mathbb Z/11\mathbb Z}\), with \(Q=\{1,3,4,5,9\}\), the torsion action is the unique unit \(u\pmod{33}\) such that \(u\equiv1\pmod3\) and \(u\equiv a\pmod{11}\). Thus the multiplier subgroup acts faithfully on \(\mathbb Z/11\mathbb Z\) and fixes the \(\mathbb Z/3\mathbb Z\) summand. Its fixed subgroup in the full torsion is exactly \(\mathbb Z/3\mathbb Z\). Cyclic source-triangle rotation has trivial torsion action.

## Assumptions and scope
The tournament has vertex set \(\mathbb Z/11\mathbb Z\), and \(u\to v\) exactly when \(v-u\in Q\). The oriented source triangle has arcs \(0\to1\), \(1\to2\), \(2\to0\). A closed regular cell of \(X\) is a product \(\Delta(A)\times\Delta(B)\times\Delta(C)\) of three nonempty vertex simplices, where every arrow \(A\to B\), \(B\to C\), and \(C\to A\) occurs. The cell dimension is \(\lvert A\rvert+\lvert B\rvert+\lvert C\rvert-3\). Each factor is oriented by increasing vertex labels and the product uses the coordinate order \(A,B,C\). The homology has ordinary integral coefficients. Only the stated natural affine subgroup and cyclic rotation are assessed; no claim about all automorphisms is required.

## Proof
**Finite cell model and torsion.** Exhaustive bit-mask enumeration gives precisely \(165\) vertices, \(495\) edges and \(330\) two-cells, hence \(990\) nonempty regular cells and \(2145\) codimension-one incidences. The finite matching defined in `verify_paley_torsion_action.py`, by greedily adjoining allowed labels in ordered factor/vertex passes, contains \(477\) pairs. Orient matched incidences upward and all others downward; the provided program performs a complete topological-sort acyclicity check across all \(990\) cells. The resulting integral Morse CW complex has one vertex, \(18\) one-cells and \(17\) two-cells. Its signed second differential is an \(18\times17\) integer matrix \(B\) reproduced from cellular products by recursive gradient-path cancellation. An explicit \(16\times16\) minor formed from its first sixteen columns and all rows except zero-indexed rows \(0,3\) equals \(-1\). The determinants of all eighteen maximal \(17\times17\) minors, indexed by the deleted row, are

`[33,-33,-33,-33,0,-33,0,33,33,33,0,33,-33,33,33,33,-33,33]`.

The unit minor forces the first sixteen Smith invariants to be \(1\); the gcd \(33\) of maximal minors forces the last to be \(33\). With one zero-cell, the Morse first differential is zero. Therefore
\[
H_1(X;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/33\mathbb Z,\qquad H_2(X;\mathbb Z)=0.
\]

**Multiplier action.** A spanning tree supplied by the \(164\) matched zero-to-one pairs converts each critical one-cell into a closed integral cellular cycle. Signed product orientations transport these cycles under \(\mu(v)=3v\). The algorithm builds the mod-eleven cochain kernel of \(B^{\mathsf T}\), lifts the two basis cochains to the original cell complex, and independently verifies that both vanish on all \(330\) signed two-cell boundaries. In the specified basis obtained from free coordinates \(16,17\), their pullback action is
\[
M=\begin{pmatrix}2&10\\10&2\end{pmatrix}\in\operatorname{GL}_2(\mathbb F_{11}),
\qquad \det M=3\pmod{11},\qquad M^5=I.
\]
As an order-five action on the rank-one free integral quotient \(H_1/\operatorname{Tor}\cong\mathbb Z\), \(\mu\) acts trivially. In characteristic eleven, the order-five action is semisimple, so the other eigenvalue of \(M\), namely \(3\), is the multiplier on the order-eleven torsion line. Because \(\mu\) has order five while \(\operatorname{Aut}(\mathbb Z/3\mathbb Z)\) has order two, its action on the order-three summand is trivial. Chinese remaindering gives the unique scalar \(25\pmod{33}\) (since \(25\equiv1\pmod3\) and \(25\equiv3\pmod{11}\)). Every \(a\in Q\) is a power of three, and translations have order eleven, which is coprime to \(\lvert\operatorname{Aut}(\mathbb Z/33\mathbb Z)\rvert=20\). This proves the full stated affine-subgroup formula. The source rotation has order three and therefore acts trivially on the same torsion group. Finally \(\gcd(25-1,33)=3\), giving exactly three fixed torsion classes.

## Verification
Run `python3 verify_paley_torsion_action.py` with Python 3 (standard library only). The independently generated direct signed cellular boundaries have mod-prime ranks \((164,330)\) for primes \(2,13\), and \((164,329)\) for primes \(3,11\), confirming the location of the two prime torsion contributions. The code verifies every incidence, matching acyclicity, exact integer determinants and cohomological evaluations, including the target multiplication and translation, and source rotation. `VERIFIER_OUTPUT.txt` contains the exact reproducible output. The zero-indexed matrix coordinate convention is fixed in the code; no other package data are required.

## Relationship to prior work
Dochtermann and Singh's directed Hom complex construction and natural cyclic-source group action are used as the setting [1], not claimed as new. A pre-existing computation of the nonequivariant integral homology of this exact complex fixes the underlying cyclic torsion order \(33\); that order is **not** claimed as a new result here and is reconstructed only to make the action calculation independently verifiable. The new assertion is the nontrivial integral torsion representation: the order-five target multiplier acts as \(25\), a distinction invisible to rational homology and to the abstract group structure. Govc's directed *flag* complexes concern a different topological construction [2]. No inspected statement gives this specific torsion action.

## Limitations
This does not determine the fundamental group, integral automorphism matrices on the free-plus-torsion extension, the full equivariant homotopy type, or other Paley tournament orders. Source comparisons cannot rule out unindexed equivalent calculations. The proof is exact finite computation over a concrete regular CW model, not an automated proof of a broader family theorem. External independent validation has not been performed.

## References
[1] A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948 (first posted 2021-08-24), §§2.4, 5, 7; https://arxiv.org/abs/2108.10948.

[2] D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333 (2020); https://arxiv.org/abs/2006.05333 (distinct construction).
