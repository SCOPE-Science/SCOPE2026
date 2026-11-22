# Complete Walsh spectrum of Desargues matroid bases and two zero-frequency graph motifs

## Finding

The unnormalized binary convolution supported on the 110 bases of the ordinary rank-three Desargues configuration matroid on ten points has **Fourier rank 952, nullity 72, positive inertia 476 and negative inertia 476**. Its least nonzero Walsh multiplier has absolute value \(2\) and its largest has absolute value \(110\); hence the Euclidean condition number on its recoverable subspace is exactly \(55\), and the Moore–Penrose inverse has Euclidean operator norm \(1/2\).

The 72 zero-frequency characters are **exactly** the ten-coordinate sign vectors corresponding to a five-edge graph on five labelled vertices of one of two isomorphism types: a five-cycle (12 labelled supports) or a *bull graph* (60 labelled supports, comprising a triangle with two pendant edges at distinct triangle vertices). No other frequency vanishes.

The complete signed spectrum, with multiplicities for each positive value and its negative, is:

| Absolute eigenvalue | Positive multiplicity | Negative multiplicity |
|---:|---:|---:|
| 110 | 1 | 1 |
| 44 | 10 | 10 |
| 18 | 5 | 5 |
| 12 | 20 | 20 |
| 10 | 90 | 90 |
| 8 | 60 | 60 |
| 6 | 150 | 150 |
| 4 | 130 | 130 |
| 2 | 10 | 10 |
| 0 | 72 | — |

All frequencies and multiplicities are integers; the underlying vector space has \(2^{10}=1024\) elements. The two labels for signs in the final zero row do not denote two different zero eigenvalues.

## Assumptions and scope

Let \(F=\{0,1,2,3,4\}\), and let the ten points of the Desargues configuration be \(E=\binom F2\), ordered lexicographically. Its ten distinguished collinear triples are the lines \(L_A=\binom A2\) for \(A\in\binom F3\). The ordinary rank-three linear matroid has the base set
\[
\mathcal B=\{B\in\binom E3 : B\neq L_A\text{ for every } A\in\binom F3\},\quad |\mathcal B|=\binom{10}3-10=110.
\]
This is not the distinct *trilateral matroid* on the same configuration, which has 100 bases.

Identify a subset of \(E\) with its binary incidence vector in \(G=(\mathbb Z/2\mathbb Z)^{10}\). Define \(k:G\to\{0,1\}\) by \(k(B)=1\) exactly on \(\mathcal B\), and \(T:\mathbb C^G\to\mathbb C^G\) by \((Tf)(x)=\sum_{y\in G}k(y)f(x-y)\). The Walsh character indexed by \(S\subseteq E\) is \(\chi_S(B)=(-1)^{|S\cap B|}\), and its multiplier is \(\lambda(S)=\sum_{B\in\mathcal B}\chi_S(B)\). This is **counting** rather than probability-normalized convolution. Spectral rank and nullity are invariant under a nonzero common normalization, but the numerical operator norms given above are not.

## Proof

**Exact character formula.** For \(s=|S|\), let
\[
K_3(s;10)=\sum_{j=0}^3(-1)^j\binom sj\binom{10-s}{3-j},
\]
where an out-of-range binomial coefficient is zero. Subtracting the ten forbidden collinear triples from all three-element subsets gives the identity
\[
\boxed{\lambda(S)=K_3(|S|;10)-\sum_{A\in\binom F3}(-1)^{|S\cap L_A|}.}
\]
This proves, in particular, that the ten points and ten lines uniquely determine the entire spectrum, with no geometric coordinates or unstated choices.

**Symmetry and complement.** The natural action of \(\mathfrak S_5\) on the pairs in \(E\) preserves the line family, hence \(\lambda(S)\) is constant on its orbits. Since every base has size three,
\[
\lambda(E\setminus S)=-\lambda(S).
\]
Consequently it suffices to evaluate character supports having at most five of the ten coordinates; supports with more than five follow by complementation.

**Exhaustive orbit certificate.** For each mask from zero through 1023, represent a set of K5 edges using the lexicographic bit order \(01,02,03,04,12,13,14,23,24,34\). The attached executable certificate constructs all 120 permutations of the five underlying vertices, enumerates each orbit as a set of exact integer masks, and checks that these disjoint orbits partition all 1024 masks. There are **34** orbits in all and **20** with at most five selected edges. The following table lists every one of those 20 representatives, its orbit size, its exact value from the boxed formula, its graph degree sequence and its number of K5 triangles. The representatives are machine-readable decimal bit masks, not mathematical variables.

| Support size | Representative mask | Orbit size | Multiplier | Degree sequence | Triangles |
|---:|---:|---:|---:|---|---:|
| 0 | `0` | 1 | 110 | `(0, 0, 0, 0, 0)` | 0 |
| 1 | `1` | 10 | 44 | `(1, 1, 0, 0, 0)` | 0 |
| 2 | `3` | 30 | 6 | `(2, 1, 1, 0, 0)` | 0 |
| 2 | `20` | 15 | 10 | `(1, 1, 1, 1, 0)` | 0 |
| 3 | `7` | 20 | -12 | `(3, 1, 1, 1, 0)` | 0 |
| 3 | `21` | 60 | -8 | `(2, 2, 1, 1, 0)` | 0 |
| 3 | `28` | 30 | -4 | `(2, 1, 1, 1, 1)` | 0 |
| 3 | `19` | 10 | -4 | `(2, 2, 2, 0, 0)` | 1 |
| 4 | `15` | 5 | -18 | `(4, 1, 1, 1, 1)` | 0 |
| 4 | `54` | 15 | -10 | `(2, 2, 2, 2, 0)` | 0 |
| 4 | `29` | 60 | -10 | `(3, 2, 1, 1, 1)` | 0 |
| 4 | `58` | 60 | -6 | `(2, 2, 2, 1, 1)` | 0 |
| 4 | `23` | 60 | -6 | `(3, 2, 2, 1, 0)` | 1 |
| 4 | `184` | 10 | 2 | `(2, 2, 2, 1, 1)` | 1 |
| 5 | `62` | 60 | -4 | `(3, 2, 2, 2, 1)` | 0 |
| 5 | `31` | 30 | -4 | `(4, 2, 2, 1, 1)` | 1 |
| 5 | `220` | 12 | 0 | `(2, 2, 2, 2, 2)` | 0 |
| 5 | `59` | 60 | 0 | `(3, 3, 2, 1, 1)` | 1 |
| 5 | `185` | 60 | 4 | `(3, 2, 2, 2, 1)` | 1 |
| 5 | `55` | 30 | 4 | `(3, 3, 2, 2, 0)` | 2 |

Every row follows by direct substitution into the boxed expression. The orbit program computes the maps \(e=\{u,v\}\mapsto\{\sigma(u),\sigma(v)\}\), checks the row invariance, and verifies the orbit sizes total the complete frequency set. Thus the finite classification is exhaustive, not a truncated experimental search.

**Exact zero locus.** Only the two five-edge rows with multiplier zero survive. Their degree sequences and K5 triangle counts distinguish them from every other row, giving respectively the cycle \(C_5\) (orbit size 12) and the bull graph (orbit size 60). Alternatively, for \(|S|=5\), the Krawtchouk term is zero, and if \(o(S)\) is the number of lines meeting \(S\) in an odd number of points, then \(\lambda(S)=2o(S)-10\). The six five-edge orbit representatives have \(o(S)\in\{3,5,7\}\), with \(o(S)=5\) precisely for the two stated motifs. No frequency of another size can vanish, by the complete table and complement symmetry.

**Inertia and sharp bounds.** The values in the table, their orbit multiplicities, and complement antisymmetry produce the stated signed spectrum: there are \(476\) strictly positive, \(476\) strictly negative, and \(72\) zero Walsh multipliers. The smallest nonzero absolute value is \(2\), attained for example on the ten representatives in the positive two row, and the maximum is \(110\), attained on the empty/full frequency supports. The Walsh transform diagonalizes \(T\) unitarily after normalizing the character basis. Therefore the rank, nullity, positive/negative inertia, positive-spectrum condition number and pseudoinverse norm follow exactly.

## Verification

Run `python3 verify.py` with Python 3.9 or newer and no third-party packages. The verifier computes the base set independently of the orbit list, obtains all 1024 multipliers by direct signed summation, recomputes them by a complete Walsh–Hadamard transform, and checks equality with the Krawtchouk-minus-lines formula. It enumerates all 34 \(\mathfrak S_5\) graph orbits from vertex permutations, verifies the complete signed histogram and the weight-by-weight histogram, checks both zero orbits, and verifies the two extreme magnitudes, two inertia counts and complement antisymmetry. Every arithmetic test is exact over the integers. The proof is a finite exhaustive argument; no numerical approximation or extrapolation to larger configurations is used.

## Relationship to prior work

Saniga's publicly posted 2011 note studies geometric hyperplanes of the Desargues configuration and provides the ten-point, ten-line incidence structure. Stroppel and Stroppel describe the precise two-subset/three-subset incidence realization and the \(\mathfrak S_5\) symmetry in their 2012 preprint. Raney distinguishes the 110 bases of an ordinary linear matroid from the 100 bases of the separate trilateral matroid. These establish the classical geometry and matroid base count; they do not state the signed Walsh spectrum, its exact nullspace or the bull/cycle frequency dichotomy.

A published exact root-line sampling study of the type-\(D_5\) geometry identifies the same two five-vertex graph shapes, the five-cycle and the bull, as **E-optimal doubled-edge supports**. Its object is a fifteen-row evaluation operator on real symmetric matrices and its criterion is a least singular value, not the Walsh transform of the 110 Desargues bases. Thus it provides a nontrivial related graph-motif coincidence but does not supply the 72-dimensional Fourier-nullity statement.

Other Boolean Fourier calculations for a five-vertex triangle-free *graph-property indicator*, or for bases of finite projective geometries, concern different codebooks. Neither contains a statement implying the 72 zero modes for this 110-base Desargues kernel. No unqualified historical uniqueness or independent external validation is asserted.

## Limitations

This is a complete **finite**, ten-coordinate classification, not an infinite-family theorem. A database search is not a proof of historical priority. The result does not classify Fourier spectra of the distinct 100-base trilateral matroid or of general ten-point configurations, and does not give an optimal \(\ell^1\) range-projection norm. The complete integer certificate supplies reproducibility, not independent auditing or formal proof-assistant certification.

## References

- M. Saniga, *Geometric Hyperplanes: Desargues Encodes Doily*, arXiv:1101.0977v1, first posted 2011-01-03. https://arxiv.org/abs/1101.0977
- B. Stroppel and M. Stroppel, *Desargues, Doily, Dualities, and Exceptional Isomorphisms*, Universität Stuttgart Preprint 2012/017, §1.1 and §2. https://www.f08.uni-stuttgart.de/.content/media/downloads/Mathematik/mathematische_berichte/2012/2012-017.pdf
- M. W. Raney, *Trilateral matroids induced by \(n_3\)-configurations*, Ars Mathematica Contemporanea 14 (2018), 267–284, definitions and Section 2. https://dlib.si/stream/URN%3ANBN%3ASI%3ADOC-MEFZYR32/05145667-048b-4665-848a-8535fd489b9a/PDF

- *A sharp E-optimal fifteen-sample quadratic frame on the type-\(D_5\) root lines*, 2026-11-16, published exact sampling and graph-motif result. https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-sharp-e-optimal-fifteen-sample-quadratic-frame-on-the-type-d-5--56771725ce8b
