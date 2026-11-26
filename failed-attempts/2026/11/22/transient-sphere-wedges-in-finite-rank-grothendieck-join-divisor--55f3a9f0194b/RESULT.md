# Transient sphere wedges in finite-rank Grothendieck join-divisor filtrations

## Finding
For every integer \(r\ge1\) and every integer \(k\ge1\), consider the nonidentity elements with prime-exponent length at most \(k\) in the subgroup on \(r\) distinct join-primes of the Grothendieck group of finite simplicial complexes. Endow them with the signed-divisor order of Chocano and Prieto-Martínez [1]. Write \(X_{r,k}\) for this finite partially ordered set and \(\Delta X_{r,k}\) for its order complex. Then, equivariantly for signed permutations of the prime coordinates,
\[
 |\Delta X_{r,k}|\simeq \operatorname{sk}_{\min(k,r)-1}(\partial\mathcal O_r),
\]
where \(\partial\mathcal O_r\) is the boundary of the \(r\)-dimensional cross-polytope. In particular,
\[
 |\Delta X_{r,k}|\simeq
 \begin{cases}
 \displaystyle\bigvee^{b_{r,k}} S^{k-1},&1\le k<r,\\
 S^{r-1},&k\ge r,
 \end{cases}
 \qquad b_{r,k}=\sum_{j=0}^{k}(-1)^{k-j}2^j\binom rj.
\]
The \(k=1\) statement uses the standard convention that a wedge of \(m\) zero-spheres is a disjoint set of \(m+1\) points. There is no torsion. All reduced integral persistence intervals under increasing \(k\) are \(b_{r,k}\) copies of \([k,k+1)\) in degree \(k-1\) for \(1\le k<r\), plus one infinite interval \([r,\infty)\) in degree \(r-1\). Every full signed-permutation quotient \(|\Delta X_{r,k}|/(C_2^r\rtimes S_r)\) is contractible.

## Assumptions and scope
Let \(\mathcal S\) be the cancellative commutative monoid of isomorphism classes of finite simplicial complexes under simplicial join, and \(K(\mathcal S)\) its Grothendieck group. Unique join-prime factorization and the minimal-representation signed-divisor order are supplied by [1, Theorems 3.18 and 4.1]. Choose \(r\) distinct prime classes. Their formal exponent subgroup is \(\mathbb Z^r\). Its order is
\[
 x\preceq y\quad\Longleftrightarrow\quad
 \forall i,\ [x_i=0\ \text{or}\ (x_i y_i>0\ \text{and}\ |x_i|\le|y_i|)].
\]
Define \(X_{r,k}=\{x\in\mathbb Z^r:1\le\|x\|_1\le k\}\) with induced order. The norm is the word length in the chosen positive and negative prime generators. All topological claims concern the geometric realization of order complexes, rather than a homeomorphism between non-Hausdorff Alexandrov spaces and spheres. The coordinate signed-permutation group preserves the order and word length. Zero is excluded throughout.

## Proof
**1. A filtration-compatible order retraction.** Set \(\sigma(x)_i=\operatorname{sgn}(x_i)\in\{-1,0,1\}\). On each \(X_{r,k}\), the map \(\sigma\) is an order-preserving retraction onto the subposet
\[
 Q_{r,k}=\{\varepsilon\in\{-1,0,1\}^r:1\le|\operatorname{supp}(\varepsilon)|\le\min(k,r)\}.
\]
Indeed \(\sigma(x)\preceq x\), and if \(x\preceq y\), each nonzero coordinate of \(x\) and \(y\) has the same sign, so \(\sigma(x)\preceq\sigma(y)\). The comparable maps \(\sigma\) and the identity are homotopic as maps of finite posets, and hence induce a homotopy on order complexes. This construction is natural in \(k\) and commutes with all signed coordinate permutations.

**2. Identifying the finite core.** The subposet \(Q_{r,k}\) is the poset of nonempty signed faces of support size at most \(\min(k,r)\) in the simplicial boundary of the cross-polytope. Its order complex is the barycentric subdivision of the asserted skeleton. A signed face is a subset of \(\{1^+,1^-,\ldots,r^+,r^-\}\) containing at most one sign per coordinate. A face of size \(j\) can be chosen in \(2^j\binom rj\) ways.

**3. Integral homotopy, including the endpoints.** For \(k<r\), these signed faces of size at most \(k\) form a rank-\(k\) truncation of a partition matroid with \(r\) two-element parallel classes. The basis-exchange axiom follows by choosing a coordinate occupied by the larger face and unoccupied by the smaller. Matroid independence complexes are pure shellable [2, Section 5]. Consequently this complex is a wedge of spheres of dimension \(k-1\), with no integral torsion. Its reduced Euler characteristic is computed from the face numbers above:
\[
 (-1)^{k-1}\widetilde\chi
 =\sum_{j=0}^{k}(-1)^{k-j}2^j\binom rj=b_{r,k}.
\]
For \(k=r\), the full signed-face complex is the boundary of the \(r\)-cross-polytope, a single sphere \(S^{r-1}\); for larger \(k\) the retract is unchanged. In particular, for \(r=1\) every stage has the two-point homotopy type \(S^0\).

**4. All persistence maps.** The retractions commute with the inclusions \(X_{r,k}\hookrightarrow X_{r,k+1}\), reducing their persistent homology to the successive cross-polytope skeleton inclusions. For every \(k<r\), the only nonzero reduced integral homology at stage \(k\) lies in degree \(k-1\). Its map to stage \(k+1\) vanishes because the next stage has no homology in that degree. At and after \(k=r\), all maps become isomorphisms on the single top integral class, since the signed-face retract remains the full cross-polytope boundary. This proves the claimed complete interval decomposition and its torsion-free nature, for all integers and with the stated special case \(r=1\).

**5. Actual symmetry quotients.** The group \(B_r=C_2^r\rtimes S_r\) acts on the signed faces and on their chains. Each chain of nonempty signed faces is characterized up to \(B_r\) by its strictly increasing sequence of face sizes: any two such chains are carried to one another by a signed coordinate permutation. The action on the barycentric subdivision has no inversions. Therefore its orbit complex has one simplex for every nonempty subset of \(\{1,\ldots,\min(k,r)\}\), namely the full \((\min(k,r)-1)\)-simplex, which is contractible. Because the order retraction in step 1 is equivariant, it induces a homotopy equivalence on geometric quotients. This proves the final assertion.

## Verification
The standalone `checker.py` independently generates signed faces and their oriented simplicial boundaries for all \(1\le r\le5\), \(1\le k\le r\), and verifies the predicted reduced homology dimensions over each of \(\mathbb F_2,\mathbb F_3,\mathbb F_5\). It additionally verifies that \(\sigma\) is a below-identity monotone retraction on the full finite signed exponent posets for \(r\le5\), \(k\le\min(r,3)\), including every order-comparable pair. The script reports 132 passing arithmetic checks. Illustrative interior multiplicities for \(r=6\) are \(11,49,111,129,63\), followed by one permanent top class. These finite calculations are checks, not substitutes for the proofs in steps 1–5.

## Relationship to prior work
Chocano and Prieto-Martínez [1] establish join-prime factorization, define the signed-divisor Alexandrov order, prove its global contractibility, and show that its order complex is universal for finite order complexes. Their results do not give the homotopy types or inclusion-induced homology maps of the positive-length finite-rank sublevel filtration defined here. A previously established full-punctured-rank sphere description corresponds only to the final stabilized homotopy stage, not the intermediate filtration or its ephemeral classes. On the other hand, the abstract shellability and wedge-of-spheres topology of truncated partition-matroid complexes are already standard [2]; they are inputs, not claimed as new. The new statement is the filtration-compatible identification of the signed-divisor Grothendieck sublevels, its complete integral barcode and their full-symmetry quotient behavior.

## Limitations
These conclusions require a finite chosen set of distinct join-primes and the word-length filtration defined here, not an arbitrary subspace or metric on the complete infinite-rank Grothendieck group. They concern geometric order complexes and their finite-group quotients; they do not determine homeomorphism types of the original Alexandrov finite spaces. No independent verification has been performed. Existing unindexed treatments of the same filtration could affect publication priority.

## References
[1] P. J. Chocano and L. F. Prieto-Martínez, *Negative-Dimensional Simplicial Complexes via the Grothendieck Group of the Join Monoid*, arXiv:2611.14300v1 (first public 10 November 2026), especially Theorems 3.18, 4.1, 4.2, 4.8. https://arxiv.org/abs/2611.14300

[2] *Pseudospheres: combinatorics, topology and distributed systems*, Section 5 on partition matroids, shellability and the wedge-of-spheres theorem, DOI:10.1007/s41468-023-00162-5. https://doi.org/10.1007/s41468-023-00162-5
