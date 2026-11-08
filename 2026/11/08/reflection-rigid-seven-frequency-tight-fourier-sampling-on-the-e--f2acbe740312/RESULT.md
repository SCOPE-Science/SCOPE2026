# Reflection-rigid seven-frequency tight Fourier sampling on the eleven-cycle

## Finding

Let \(E=\{0,1,2,3\}\subset\mathbb Z_{11}\), let \(\zeta=e^{2\pi i/11}\), and let a character indexed by \(s\in\mathbb Z_{11}\) be the vector \(v_s=(1,\zeta^s,\zeta^{2s},\zeta^{3s})\in\mathbb C^4\). For a frequency subset \(F\subseteq\mathbb Z_{11}\), consider the exact positive-weight tight-frame equation

\[
\sum_{s\in F}w_s v_s v_s^*=I_4,\qquad w_s>0.
\]

**Theorem.** At least seven distinct frequencies are necessary. Exactly **33** of the \(\binom{11}{7}=330\) seven-frequency subsets admit such weights. For each admissible subset, the normalized weights are **unique**. The admissible subsets are exactly those whose seven cyclic gaps (between successive elements in cyclic order) all belong to \(\{1,2\}\) **and** which are invariant under a reflection \(s\mapsto a-s\pmod{11}\) for some \(a\in\mathbb Z_{11}\). They comprise precisely three dihedral orbits, each with eleven members. Representatives and their canonical gap words are:

| Representative \(F\) | Canonical cyclic gap word | Orbit size |
|---|---|---:|
| \(\{0,1,2,3,5,7,9\}\) | 1112222 | 11 |
| \(\{0,1,2,4,6,7,9\}\) | 1122122 | 11 |
| \(\{0,1,3,4,6,7,9\}\) | 1212122 | 11 |

Every other seven-frequency subset fails to admit nonnegative weights satisfying the tight-frame equation, even if zero weights are allowed (in that case the effective support would have fewer than seven nodes, which is impossible).

Equivalently, precisely these 33 supports carry strictly positive quadrature rules on the eleventh roots of unity that integrate every trigonometric polynomial of degree at most three exactly against normalized Haar measure on the circle.

## Assumptions and scope

All statements are for the exact cyclic group \(\mathbb Z_{11}\), four consecutive signal coordinates, arbitrary **strictly positive real** sampling weights, and exact tightness for all vectors in \(\mathbb C^4\). Frequencies are distinct, and the right side is the identity; a general positive tight-frame constant reduces to this normalization. This is a finite classification and makes no assertion for other moduli or other coordinate sets.

For a seven-subset \(F=\{s_1<\cdots<s_7\}\), write the cyclic gaps as \(d_j=s_{j+1}-s_j\) for \(1\le j<7\), and \(d_7=11+s_1-s_7\). A *canonical gap word* is the lexicographically least word obtained from \((d_1,\ldots,d_7)\) by cyclic rotations and reversal. Translation and reflection of \(F\) preserve this canonical word; conversely, equal canonical words imply that the subsets are dihedrally equivalent.

## Proof

**1. Reduction to six Fourier moments.** The \((i,j)\)-entry of the weighted Gram matrix, for \(i,j\in E\), equals \(\sum_{s\in F}w_s\zeta^{(i-j)s}\). Thus tightness is equivalent to

\[
\sum_{s\in F}w_s=1,\qquad
\sum_{s\in F}w_s\zeta^{ks}=0\quad(k=1,2,3),
\]

with the negative moments vanishing by complex conjugation. A seven-node real solution therefore solves a seven-by-seven real linear system \(Aw=e_1\), with rows \(1,\cos(2\pi s/11),\sin(2\pi s/11),\ldots,\cos(6\pi s/11),\sin(6\pi s/11)\).

**2. A self-contained six-node obstruction.** Let \(s_1,\ldots,s_6\) be six distinct residues and \(z_j=\zeta^{s_j}\). Consider the six-by-six Fourier minor whose row exponents are \(-3,-2,-1,1,2,3\). Multiplying column \(j\) by \(z_j^3\) changes its row exponents to \(0,1,2,4,5,6\). The generalized Vandermonde identity gives

\[
\det(z_j^{r})_{r\in\{0,1,2,4,5,6\},\ 1\le j\le6}
=\left(\prod_{i<j}(z_j-z_i)\right)e_3(z_1,\ldots,z_6),
\]

where \(e_3=\sum_{i<j<k}z_iz_jz_k\). The Vandermonde factor is nonzero. The second factor is a sum of exactly \(\binom63=20\) eleventh roots of unity, counted with multiplicity, and cannot vanish: any vanishing \(\sum_{r=0}^{10}c_r\zeta^r=0\) with nonnegative integer coefficients \(c_r\) forces all \(c_r\) to be equal, because the minimal polynomial of \(\zeta\) is \(1+X+\cdots+X^{10}\). That would make \(\sum c_r\) divisible by 11, contrary to \(20\). Therefore every such six-column matrix is nonsingular. Fewer than six columns are also independent by extension to six. No nonzero weight vector supported on at most six frequencies can make all six nonconstant moments vanish. Seven nodes are necessary.

**3. Unique candidate weights at seven nodes.** For any seven distinct eleventh roots, the real moment matrix \(A\) is invertible. Indeed, setting the exponents to \(-3,-2,-1,0,1,2,3\) and multiplying each column by its \(z_j^3\) gives an ordinary seven-by-seven Vandermonde matrix with exponents \(0,1,\ldots,6\). Hence for every seven-node subset there is a unique real vector \(w=A^{-1}e_1\). By Cramer's rule its \(j\)-th sign is the sign of \(\det(A_j)/\det(A)\), where \(A_j\) is \(A\) with its \(j\)-th column replaced by \(e_1\).

**4. Exhaustive exact-sign classification.** The accompanying standard-library `CHECK.py` performs a finite certificate, not a floating-point guess. It enumerates all \(330\) seven-subsets, partitions them by canonical gap word into exactly \(20\) dihedral classes, and chooses one representative of each class. It forms integer approximations to the real moment matrix at scale \(10^{12}\), obtains every determinant by exact integer fraction-free elimination, and certifies all Cramer signs. Here is the full orbit-level result, writing `+` for seven strictly positive weights and `-` otherwise:

| Canonical gaps | Orbit size | Admissible? |
|---|---:|:---:|
| 1111115 | 11 | - |
| 1111124 | 22 | - |
| 1111133 | 11 | - |
| 1111214 | 22 | - |
| 1111223 | 22 | - |
| 1111232 | 11 | - |
| 1111313 | 11 | - |
| 1112114 | 22 | - |
| 1112123 | 22 | - |
| 1112132 | 22 | - |
| 1112213 | 22 | - |
| 1112222 | 11 | + |
| 1113113 | 11 | - |
| 1121123 | 22 | - |
| 1121213 | 22 | - |
| 1121222 | 22 | - |
| 1121312 | 11 | - |
| 1122113 | 11 | - |
| 1122122 | 11 | + |
| 1212122 | 11 | + |

The sign certificate is rigorous: Machin's arctangent series bounds the error in its rational approximation to \(\pi\) by less than \(10^{-20}\); terminating sine/cosine Taylor series and the rational scale floor give each matrix entry an error smaller than \(2\cdot10^{-12}\). The Leibniz formula consequently bounds the absolute error of every normalized seven-by-seven determinant by \(7!\cdot7\cdot(2\cdot10^{-12})(1+2\cdot10^{-12})^6<10^{-7}\). Every determinant used for a sign has absolute value greater than \(10^{-3}\), as checked in exact integer arithmetic. Thus each reported sign is the sign of the **true** trigonometric determinant. A reflection or translation carries a positive rule to another positive rule by permuting weights, so one representative per class suffices. The three positive classes each contain eleven sets, yielding \(33\) in total. A direct finite comparison of the 20 gap classes shows that these are precisely the classes with all gaps at most two and reflection symmetry.

This proves the claimed classification and uniqueness.

## Verification

Run `python3 CHECK.py` from the directory containing this result. It requires only the Python standard library, enumerates all relevant gap orbits, certifies all 160 determinant signs by integer operations, and terminates with `CERTIFIED_11TH_ROOT_SEVEN_NODE_CLASSIFICATION_PASSED`. There are \(20\) representatives; one determinant and seven Cramer determinants are certified for each. No probabilistic numerical test or external software is part of the proof.

## Relationship to prior work

Finite Gabor-frame block structures motivate sparse acquisition designs (Asipchuk, De Carli, and Rodriguez, 2026), but their subgroup block-equivalence results do not state this seven-frequency optimizer census. Rational-spectrum rigidity for finite unweighted Hadamard pairs (Fu and Song, 2026) concerns a different, unweighted exact-orthogonality setting. Classical positive trigonometric quadrature theory (Peherstorfer, 2010/2011; Luo, Yu, and Meng, 2014) gives general existence/characterization methods; the present claim is the explicit **eleventh-root restricted, four-site** exact minimum, unique positive weights, and the complete 33-subset/three-orbit reflection classification. A related finite prime-cyclic three-site positive-weight theorem has smaller spatial dimension and does not imply the displayed four-site orbit census. Prior general interpolation formulas are not claimed to be new.

## Limitations

The classification concerns exactly \(\mathbb Z_{11}\), not all prime cyclic groups. It gives tightness and uniqueness of sampling weights, not robustness to measurement noise or missing measurements. The finite determinant table is necessary for the full support classification and is included with an exact, reproducible sign certificate; the six-node impossibility and uniqueness arguments are independent of that certificate. An uninspected earlier specialization of general unit-circle quadrature theory might state an equivalent orbit census; this residual publication-priority risk is acknowledged.

## References

1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, first posted May 15, 2026; 2020 MSC 42C15 (primary), 15B05 (primary).
2. X.-Y. Fu, Z.-J. Song, *Rational Spectra for Finite Hadamard Pairs and Bounded Spectral Sets on the Real Line*, arXiv:2607.19858, first posted July 22, 2026.
3. F. Peherstorfer, *Positive Trigonometric Quadrature Formulas and Quadrature on the Unit Circle*, arXiv:1001.2451 (2010); *Mathematics of Computation* 80 (2011), 1685–1701.
4. Z. Luo, R. Yu, Z. Meng, *The Maximum Trigonometric Degrees of Quadrature Formulae with Prescribed Nodes*, *Communications in Mathematical Research* 30 (2014), 334–344, DOI 10.13447/j.1674-5647.2014.04.07.
