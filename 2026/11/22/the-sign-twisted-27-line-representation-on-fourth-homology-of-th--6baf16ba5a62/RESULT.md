# The sign-twisted 27-line representation on fourth homology of the cubic-surface skew-line complex

## Finding
Let \(S\) be any smooth cubic surface over \(\mathbb C\), let \(\mathcal L\) be its set of \(27\) geometric lines, and let \(K(S)\) be the simplicial complex whose simplices are all pairwise disjoint subsets of \(\mathcal L\). Write \(W=W(E_6)\) for the full group preserving the configuration of lines, and \(\varepsilon:W\longrightarrow\{\pm1}\) for the determinant (reflection-sign) character on the six-dimensional root space.

**Theorem.** The full rational \(W\)-representation on reduced simplicial homology is concentrated in degree four, with
\[
\widetilde H_4(K(S);\mathbb Q)\ \cong\ \varepsilon\otimes\ker\left(\mathbb Q[\mathcal L]\xrightarrow{\text{sum}}\mathbb Q\right).
\]
In particular, this is a \(26\)-dimensional representation, and its exact character on every element \(w\in W\) is
\[
\operatorname{tr}\!\left(w\mid\widetilde H_4(K(S);\mathbb Q)\right)
=\det_{E_6}(w)\bigl(\#\operatorname{Fix}_{\mathcal L}(w)-1\bigr).
\]
Thus a root reflection fixes fifteen lines but has fourth-homology trace \(-14\), whereas an order-three class fixing nine lines has trace \(+8\). This identifies the full rational symmetry module, rather than only the number of homology generators or the un-oriented action on simplices.

## Assumptions and scope
A marking of \(S\) identifies its Picard lattice with that of the blow-up of six points of \(\mathbb P^2\) in general position. Using the hyperplane pullback \(H\) and exceptional divisors \(E_i\) indexed by \(0\le i<6\), the \(27\) line classes are
\[
E_i,\qquad L_{ij}=H-E_i-E_j\ (i<j),\qquad Q_i=2H-\sum_{k\ne i} E_k.
\]
The intersection form is \(H^2=1\), \(E_i^2=-1\), \(H\cdot E_i=0\) and \(E_i\cdot E_j=0\) for \(i\ne j\). Two distinct lines are joined in the Schläfli graph precisely when their intersection is zero. Its flag complex is \(K(S)\). The full combinatorial automorphism group is \(W(E_6)\) of order \(51,840\), which acts on \(K(S)\) independently of whether the individual marked cubic admits such automorphisms.

## Proof
**1. Finite model and homology.** Enumerate the \(27\) divisor classes as above, and construct all cliques of mutually intersection-zero classes by adjoining vertices in increasing order. Every clique has a unique increasing ordering, so this enumerates the entire complex, with \((f_0,f_1,f_2,f_3,f_4,f_5)=(27,216,720,1080,648,72)\). Including the empty face, the augmented simplicial boundary maps \(\partial_i\) for face sizes \(1\le i\le6\) have ranks over \(\mathbb F_2\)
\[
(1,26,190,530,550,72).
\]
These are exact binary row-reduction ranks of complete integer \(0,\pm1\) boundary matrices, not sample estimates. Every rank over \(\mathbb Q\) is at least its rank over \(\mathbb F_2\). Since \(\partial_i\partial_{i+1}=0\) and the sums of the displayed consecutive lower bounds saturate \(27,216,720,1080\), while the last boundary rank saturates the entire \(72\)-dimensional chain group, *all six rational ranks are forced equal* to the displayed numbers. Hence the sole nonzero reduced rational homology is in degree four and has dimension \(648-550-72=26\).

**2. Finite Weyl presentation.** The five adjacent transpositions of the six \(E_i\) and the Cremona reflection in \(\alpha=H-E_0-E_1-E_2\) act on the \(27\) line classes by explicit divisor-lattice formulas. For a root \(\alpha^2=-2\), the reflection is \(D\mapsto D+(D\cdot\alpha)\alpha\). Each of the six generators is an involution preserving the full skew-line graph. Exhaustive closure gives precisely \(51,840\) distinct permutations. Tracking the parity of generator word-length, with a consistency check for every enumerated edge of the Cayley graph, computes the determinant character \(\varepsilon\) on the full group.

**3. Equivariant Lefschetz trace.** Fix a Weyl element \(w\). For each oriented simplex \(\sigma=(v_0<\cdots<v_d)\) invariant as a set, the induced action contributes the sign of the permutation carrying the ordered tuple into \((w(v_0),\ldots,w(v_d))\); non-invariant simplices contribute zero. Let \(c_d(w)\) be the sum of these signs for all \(d\)-simplices. The reduced Lefschetz formula gives
\[
\operatorname{tr}\left(w\mid\widetilde H_4(K(S);\mathbb Q)\right)
=-1+\sum_{d=0}^5(-1)^d c_d(w).
\]
Every value \(c_d\) is computed by exhaustive traversal of the corresponding finite simplices, keeping orientation signs. The verifier constructs all \(25\) distinct conjugacy classes through conjugation by the six generators, and verifies for one representative of **each** class the exact identity
\[
-1+\sum_{d=0}^5(-1)^d c_d(w)=\varepsilon(w)\bigl(\#\operatorname{Fix}_{\mathcal L}(w)-1\bigr).
\]
The verified class cardinalities sum to \(51,840\), so this checks the character on the entire Weyl group, not on a nonexhaustive subset. All operations use exact integer and binary arithmetic. The resulting complete twenty-five-class numerical certificate is:

| Class size | Root determinant | Fixed lines | Line-cycle profile | Fourth-homology trace |
|---:|:---:|---:|:---|---:|
| 6480 | -1 | 1 | `1^1_2^1_8^3` | 0 |
| 5760 | +1 | 0 | `9^3` | -1 |
| 5184 | -1 | 0 | `2^1_5^3_10^1` | 1 |
| 5184 | +1 | 2 | `1^2_5^5` | 1 |
| 4320 | -1 | 1 | `1^1_4^2_6^1_12^1` | 0 |
| 4320 | -1 | 0 | `3^1_6^4` | 1 |
| 4320 | +1 | 0 | `3^1_12^2` | -1 |
| 3240 | +1 | 1 | `1^1_2^3_4^5` | 0 |
| 2160 | +1 | 1 | `1^1_2^4_3^2_6^2` | 0 |
| 1620 | -1 | 5 | `1^5_2^1_4^5` | -4 |
| 1440 | -1 | 3 | `1^3_2^3_3^4_6^1` | -2 |
| 1440 | -1 | 0 | `3^5_6^2` | 1 |
| 1440 | +1 | 3 | `1^3_2^3_6^3` | 2 |
| 1440 | +1 | 0 | `3^1_6^4` | -1 |
| 720 | +1 | 0 | `3^1_6^4` | -1 |
| 540 | -1 | 3 | `1^3_2^12` | -2 |
| 540 | -1 | 1 | `1^1_2^3_4^5` | 0 |
| 540 | +1 | 3 | `1^3_4^6` | 2 |
| 480 | +1 | 0 | `3^9` | -1 |
| 270 | +1 | 7 | `1^7_2^10` | 6 |
| 240 | +1 | 9 | `1^9_3^6` | 8 |
| 80 | +1 | 0 | `3^9` | -1 |
| 45 | +1 | 3 | `1^3_2^12` | 2 |
| 36 | -1 | 15 | `1^15_2^6` | -14 |
| 1 | +1 | 27 | `1^27` | 26 |

**4. Identification of representations.** The augmentation of the natural \(27\)-line permutation module has character \(\#\operatorname{Fix}_{\mathcal L}(w)-1\). Its tensor product with the one-dimensional root determinant has exactly the character computed in Step 3. Over \(\mathbb Q\), finite-group representations are semisimple and character equality implies isomorphism. Therefore the asserted \(W\)-module identification holds.

## Verification
The standalone, standard-library Python program `verify.py` implements every divisor class, complete skew-line complex, the six integer reflection actions, binary boundary rank calculations, all \(51,840\) group elements, all \(25\) conjugacy classes, and every oriented fixed-face character sum. Run `python3 verify.py` and require all assertions and the final marker `SCHLAFLI_WEYL_HOMOLOGY_CHARACTER_VERIFIED_OK`. The exact saved output is `verification_output.txt`. The calculation is an exhaustive finite certificate for this fixed configuration; the preceding classical divisor description provides its geometric interpretation.

## Relationship to prior work
The classical line coordinates and blow-up geometry are described in Dolgachev–Kapranov (first posted April 13, 1993), Section 0.1. The published Schläfli graph reference gives its full \(W(E_6)\) automorphism group and its maximal cliques.

The nearest already-public calculation, *A wedge of twenty-six four-spheres from the 27 lines on a cubic surface* (2026), studies **exactly this** disjoint-line simplicial complex and proves its integral nonequivariant homotopy type \(\bigvee^{26} S^4\); its scope explicitly does not determine the full Weyl action on homology. The present theorem uses the same complex but determines its full \(W(E_6)\)-representation, including orientation signs not supplied by the list of unoriented cliques or the ordinary Betti numbers.

Cioabă–Mim (2026), Proposition 7.7(2b), proves vanishing of first clique homology for the Schläfli graph over arbitrary fields, but does not imply the fourth-degree Weyl character. A separate cubic-surface arithmetic chamber orbit census determines permutation cycles on the unoriented faces, not their orientations and not the induced rational homology representation. The new character formula does not follow from the un-oriented orbit data alone without the orientation-sign calculation.

## Limitations
The result classifies only the **rational**, not the integral \(W(E_6)\)-homology lattice; integral extension and torsion structures of the action are not determined. It concerns the abstract cubic-surface line configuration over \(\mathbb C\), rather than a claim that every cubic surface has all \(51,840\) automorphisms. No direct assertion is made about actual Galois realizability of arbitrary Weyl classes. Historical priority remains provisional: earlier unindexed equivariant calculations cannot be ruled out by database searches. Independent review has not yet been performed.

## References
1. I. Dolgachev and M. Kapranov, *Schur quadrics, cubic surfaces and rank 2 vector bundles over the projective plane*, arXiv:alg-geom/9304005v1 (April 13, 1993), Section 0.1, https://arxiv.org/html/alg-geom/9304005v1.
2. *A wedge of twenty-six four-spheres from the 27 lines on a cubic surface* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-wedge-of-twenty-six-four-spheres-from-the-27-lines-on-a-cubic--4e8fcf03196e.
3. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (2026), Proposition 7.7(2b), https://arxiv.org/abs/2606.27328.
4. A. E. Brouwer and collaborators, *Schläfli graph* (online graph data), https://jaanos.github.io/tables/graphs/Schlaefli.html.
