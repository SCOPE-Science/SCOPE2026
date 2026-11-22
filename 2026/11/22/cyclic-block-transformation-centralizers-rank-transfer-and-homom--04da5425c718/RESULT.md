# Cyclic-block transformation centralizers, rank transfer, and homometric fibers

## Finding
For every integer \(m\ge1\), let \(X_m=\mathbb Z/m\mathbb Z\times\{0,1\}\), and let \(M_m\) consist of all transformations
\[
  f(i,b)=(i+k,h_i(b)),\qquad k\in\mathbb Z/m\mathbb Z,\quad h_i:\{0,1\}\to\{0,1\}.
\]
Thus \(M_m\) is the cyclic-character submonoid of the transformations preserving the partition into two-element blocks, with \(|M_m|=m4^m\). Write \(E_m=\{e\in M_m:e^2=e\}\). Every \(e\in E_m\) has block character zero; its local maps are either identity or constant. Write \(w_i=1\) at identity blocks, \(w_i=0\) at constant blocks, \(a=\sum_i w_i\), and
\[
 d_k(w)=\#\{i\in\mathbb Z/m\mathbb Z:w_i=1,\ w_{i+k}=0\}.
\]
For every \(k\), the **composition-centralizer rank polynomial** with block character \(k\) is
\[
 \boxed{C_{e,k}(z)=\sum_{\substack{g\in M_m:ge=eg\\\chi(g)=k}}z^{|\operatorname{im}g|}=2^a z^m(1+z)^{m-2d_k(w)}.}
\]
Consequently \(C_e(z)=2^a z^m\sum_{k=0}^{m-1}(1+z)^{m-2d_k(w)}\). The polynomial \(C_e(z)\) determines \(a\) and the multiset of mismatch counts \(\{d_k(w):0\le k<m\}\), while the indexed family \((C_{e,k}(z))_k\) determines the full ordered mismatch vector. Both are unchanged by any choice of the constant values in \(e\). Idempotents are unit-conjugate precisely when their binary words differ by a cyclic rotation; the unit-conjugacy orbit of a type word \(w\) has \(2^{m-a}\) times as many elements as the rotational orbit of \(w\).

The all-idempotent commuting-pair rank polynomial is
\[
 \boxed{F_m(z)=\sum_{e\in E_m}\ \sum_{g\in M_m:\,eg=ge} z^{|\operatorname{im}g|}
 =2^m z^m\sum_{L\mid m}\varphi(L)\big((2+z)^L+z^L\big)^{m/L}.}
\]
In particular, for independent uniform \(e\in E_m\) and \(g\in M_m\),
\[
 \Pr(eg=ge)=\frac{(2/3)^m}{m}(1+R_m),\quad
 0\le R_m\le (m-1)\left(\frac{\sqrt{10}}4\right)^m.
\]
Conditioned on \(eg=ge\), the total-variation distance between \(|\operatorname{im}g|-m\) and \(\operatorname{Bin}(m,1/2)\) is at most \(R_m/(1+R_m)\).

The unindexed rank-centralizer fingerprint first fails to distinguish unit-conjugacy classes at \(m=5\), already beyond dihedral equivalence: identity-block sets \(\{0,1\}\) and \(\{0,2\}\) have the common polynomial \(4z^5((1+z)^5+2(1+z)^3+2(1+z))\), but are not related by rotations or reflections. The **shift-indexed** fingerprint first fails to distinguish unit-conjugacy at \(m=6\): identity-block sets \(\{0,1,3\}\) and \(\{0,3,5\}\) are not rotations, yet have the same entire indexed spectra. Even after allowing block reflections, an indexed collision first occurs at \(m=8\): identity-block sets
\[
 A=\{0,1,3,4\},\qquad B=\{0,1,2,5\}
\]
are not dihedrally equivalent, but both have mismatch vector \((0,2,3,2,2,2,3,2)\). Their common full centralizer polynomial is
\[
 \boxed{16z^8\big((1+z)^8+5(1+z)^4+2(1+z)^2\big),}
\]
whose value at \(z=1\) is \(5504\). The underlying strict homometry of \(A,B\) is previously known; the assertion here concerns the cyclic-character transformation centralizers and their exact rank polynomials.

## Assumptions and scope
All transformation compositions are ordinary function composition. The block character \(\chi(g)=k\) is the unique shift satisfying \(g(\{i\}\times\{0,1\})\subseteq\{i+k\}\times\{0,1\}\). Ranks are set-theoretic image cardinalities in \(X_m\); since characters are permutations, ranks sum over blocks. There are no assumptions on a field or group beyond the finite cyclic index set. The constants in an idempotent may independently take either value in each nonidentity block. The asymptotic assertion holds as positive integer \(m\to\infty\), without restricting its divisor structure.

## Proof
1. **Idempotents and conjugation.** The character map from \(M_m\) to the cyclic group \(C_m\) respects multiplication. Idempotency forces an idempotent cyclic-group element, hence character zero. The three idempotent maps on a two-element set are identity and the two constants, giving \(|E_m|=3^m\) and \(\operatorname{rank}e=m+a\). The units have independent local permutations and arbitrary cyclic block shift: \(U(M_m)\cong(S_2)^m\rtimes C_m\). On constants, a local permutation exchanges the two fixed values; it does not exchange a constant map with an identity. Hence type words classify unit-conjugacy up to rotation, and the orbit size is \(2^{m-a}|\operatorname{Rot}(w)|\).
2. **Local intertwining.** Fix \(\chi(g)=k\), and write \(h_i\) for the map from source block \(i\) to target block \(i+k\). Commutation is equivalent, independently for every source block, to \(h_i\circ e_i=e_{i+k}\circ h_i\). With source and target types respectively identity/identity, identity/constant, constant/identity, and constant/constant, the rank enumerators of allowable local maps are
\[
 2z+2z^2,\qquad z,\qquad 2z,\qquad z+z^2.
\]
There are \(a-d_k\), \(d_k\), \(d_k\), and \(m-a-d_k\) instances, respectively. Equality of the two mixed counts follows by cyclic translation of the binary word. Multiplication yields
\[
 (2z+2z^2)^{a-d_k}z^{d_k}(2z)^{d_k}(z+z^2)^{m-a-d_k}
 =2^a z^m(1+z)^{m-2d_k}.
\]
This proves the indexed polynomial and its sum. The coefficient of \(z^m\) in \(C_e(z)\) is \(m2^a\), determining \(a\). After division by \(2^a z^m\), the polynomials \((1+z)^{m-2d}\) for distinct feasible \(d\) have distinct degrees and are linearly independent, proving that the unindexed polynomial determines exactly the mismatch histogram. The indexed polynomials recover each \(d_k\).
3. **Global transfer.** For each fixed binary word \(w\), exactly \(2^{m-a}\) idempotents have that type. Multiplying this by the local factor \(2^a\) gives \(2^m\), independent of \(w\). The number of directed disagreeing edges \(w_i\ne w_{i+k}\) equals \(2d_k\). Put \(u=1+z\). Then \(u^{m-2d_k}\) is the edge-weight product on the permutation \(i\mapsto i+k\), with edge weight \(u\) for equal bits and \(1\) for unequal bits. On a cycle of length \(L\), the sum over all binary colorings is the trace of the \(L\)-th power of the matrix
\[
 \begin{pmatrix}u&1\\1&u\end{pmatrix},
\]
namely \((u+1)^L+(u-1)^L=(2+z)^L+z^L\). A shift of order \(L\) has \(m/L\) such cycles, and exactly \(\varphi(L)\) shifts have order \(L\). Summation gives \(F_m(z)\).
4. **Probability and rank law.** Since \(|E_m|=3^m\) and \(|M_m|=m4^m\), dividing \(F_m(1)\) yields the probability. The identity shift contributes \(8^m\) pairs. The relative mass of all other shifts is
\[
 R_m=\sum_{\substack{L\mid m\\L\ge2}}\varphi(L)
 \left(\frac{(3^L+1)^{1/L}}4\right)^m.
\]
The function \(L\mapsto(3^L+1)^{1/L}\) is nonincreasing in positive integers, hence bounded by \(\sqrt{10}\) for \(L\ge2\). The identity \(\sum_{L\mid m}\varphi(L)=m\) gives the stated bound. Conditional on identity character \(\chi(g)=0\), the rank generating polynomial is \(4^m z^m(1+z)^m\); after normalization the rank excess is exactly \(\operatorname{Bin}(m,1/2)\). Mixing in all nonzero shifts has weight \(R_m/(1+R_m)\), proving the total-variation bound.
5. **Homometry and cutoffs.** Writing \(A=\{i:w_i=1\}\), one has \(d_k=|A|-|A\cap(A-k)|\), so identical cyclic autocorrelations give identical indexed centralizer spectra. Direct substitution establishes the three displayed pairs, and checking all rotations (respectively rotations and reflections) establishes inequivalence. For the three first-occurrence cutoffs, the accompanying exhaustive finite checker enumerates all \(2^m\) binary words for each \(m\le7\), computes the mismatch histograms and ordered vectors and canonical cyclic/dihedral forms, and verifies no earlier collision of the specified kind. The eight-block set pair is a classical strictly homometric pair; its homometry is not claimed as new.

## Verification
Run `python checks/cyclic_check.py` with Python 3 and no external dependencies. The program enumerates every idempotent and every transformation in \(M_m\) for \(1\le m\le5\), tests commutation by evaluating both composites on every point, counts the image ranks, and compares these counts to both the fixed-idempotent polynomial and the divisor-sum formula. The resulting total commuting-pair counts are \(8,104,960,8320,64000\). A second check enumerates all binary patterns for \(1\le m\le7\), verifying the three minimality statements for unindexed and indexed spectra and cyclic/dihedral equivalence, and checks the explicit homometric pair at \(m=8\). These checks are finite corroboration: the all-\(m\) statements rest on the preceding algebraic and transfer-matrix proofs.

## Relationship to prior work
Sarkar and Singh developed partition-preserving transformation semigroups with prescribed character and characterized their idempotents and regularity; their results are structural premises, not the new centralizer polynomials. Their separate treatment of bijective characters deals with Green's relations and unit-regularity in a larger semigroup than the cyclic-character submonoid. Araújo and Konieczny described centralizers in full transformation semigroups through functional digraphs; restricting that general description to cyclic block characters and deriving the exact rank distribution, divisor transfer formula, and probability law requires additional analysis. Jedrzejewski and Johnson studied cyclic homometric sets and explicitly recorded the eight-point pair; the connection of its Patterson function to the full indexed centralizer spectra of the present monoids is the contribution here. Known general classifications, homometric examples, and finite-subgroup facts are not asserted as original.

## Limitations
The construction is specialized to two-element blocks and cyclic, rather than arbitrary bijective, characters. The rank-centralizer polynomial does not recover the individual shift mismatch sequence, only its histogram; even the indexed sequence cannot separate the exhibited homometric type words. The asymptotic law concerns a uniformly chosen idempotent and independently chosen arbitrary monoid element, not two independently uniform arbitrary monoid elements. The small-\(m\) exhaustive checks cannot establish the all-\(m\) formulas; that role is supplied by the general proof. A complete historical-priority determination across all semigroup centralizer and wreath-product literature is not asserted.

## References
- M. Sarkar and S. N. Singh, *Semigroups of transformations whose characters belong to a given semigroup*, arXiv:2310.19414v1, first submitted 30 October 2023. https://arxiv.org/html/2310.19414v1
- M. Sarkar and S. N. Singh, *On the Semigroup of Partition-Preserving Transformations Whose Characters Are Bijective*, Bulletin of the Korean Mathematical Society 61 (2024), 117–133. https://doi.org/10.4134/BKMS.b230053
- J. Araújo and J. Konieczny, *Centralizers in the Full Transformation Semigroup*, Semigroup Forum 2013, DOI 10.1007/s00233-012-9424-0. https://doi.org/10.1007/s00233-012-9424-0
- F. Jedrzejewski and T. Johnson, *The Structure of Z-Related Sets*, arXiv:1304.6608v1 (23 April 2013). https://arxiv.org/abs/1304.6608
