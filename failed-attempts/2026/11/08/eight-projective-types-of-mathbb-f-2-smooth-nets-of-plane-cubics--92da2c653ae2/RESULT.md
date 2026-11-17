# Eight projective types of \(\mathbb F_2\)-smooth nets of plane cubics

## Finding

Let \(V=\mathbb F_2[X,Y,Z]_3\), a ten-dimensional vector space. A **smooth net** means a three-dimensional \(\mathbb F_2\)-linear subspace \(W\subset V\) for which every nonzero \(F\in W\) defines a geometrically smooth cubic in \(\mathbb P^2_{\mathbb F_2}\). Thus the projectivization of \(W\) is a projective plane with seven \(\mathbb F_2\)-rational members, all geometrically smooth; it is *not* asserted that every member over an algebraic closure is smooth.

**Theorem.** There are exactly \(864\) such nets \(W\), comprising exactly **eight** orbits under coordinate changes by \(\operatorname{PGL}_3(\mathbb F_2)\). Three orbits have size \(8\) and projective stabilizer order \(21\); five have size \(168\) and trivial stabilizer. Equivalently, the orbit sizes are
\[
  8,\;8,\;8,\;168,\;168,\;168,\;168,\;168.
\]

The following eight triples of coefficient masks give representatives. Set
\[
(m_0,\ldots,m_9)=(X^3,Y^3,Z^3,X^2Y,X^2Z,XY^2,Y^2Z,XZ^2,YZ^2,XYZ),
\quad F_b=\sum_{j=0}^{9} \bigl(\lfloor b/2^j\rfloor\bmod2\bigr)m_j.
\]
In each table row, \(W\) is the span of the three forms \(F_b\) indexed by the listed masks; \(N_1\)-spectrum lists \(\#C_F(\mathbb F_2)\) for the seven nonzero members, with multiplicity.

| Class | Basis masks | Orbit size | Stabilizer order | \(N_1\)-spectrum |
|:--:|:--|--:|--:|:--|
| 1 | 7, 186, 363 | 8 | 21 | 3, 3, 3, 3, 3, 3, 3 |
| 2 | 7, 201, 368 | 168 | 1 | 1, 1, 3, 3, 3, 5, 5 |
| 3 | 7, 201, 890 | 168 | 1 | 2, 2, 2, 3, 3, 4, 5 |
| 4 | 7, 216, 882 | 168 | 1 | 1, 2, 2, 3, 4, 4, 5 |
| 5 | 15, 211, 310 | 8 | 21 | 3, 3, 3, 3, 3, 3, 3 |
| 6 | 15, 231, 849 | 168 | 1 | 1, 2, 2, 3, 4, 4, 5 |
| 7 | 15, 246, 309 | 8 | 21 | 3, 3, 3, 3, 3, 3, 3 |
| 8 | 31, 172, 837 | 168 | 1 | 1, 1, 2, 4, 4, 4, 5 |

In particular, neither the seven-member rational-point spectrum nor the abstract existence of a smooth net determines its coordinate-equivalence class.

## Assumptions and scope

The base field is precisely \(\mathbb F_2\); all coefficients of a net and all coordinate changes lie in that field. Curves are **geometrically** smooth, i.e. smooth over \(\overline{\mathbb F}_2\). Only the seven \(\mathbb F_2\)-rational nonzero forms in each net must be smooth. Two nets are equivalent exactly when a \(\operatorname{PGL}_3(\mathbb F_2)\) coordinate change carries one entire three-dimensional subspace onto the other. Changing the basis of a net does not change the net and is already quotiented by storing subspaces rather than ordered triples.

## Proof

**Jacobian criterion.** For every nonzero homogeneous cubic \(F\) in characteristic two, Euler's identity gives
\[
 F=X\frac{\partial F}{\partial X}+Y\frac{\partial F}{\partial Y}+Z\frac{\partial F}{\partial Z}.
\]
Consequently the projective cubic \(F=0\) is geometrically smooth if and only if its three homogeneous quadratic partial derivatives have no common nontrivial zero over the algebraic closure. For homogeneous polynomials, this is equivalent to the affine common-zero ideal of the derivatives being zero-dimensional: its only point is the origin. The checker performs exact Gröbner-basis zero-dimensionality tests over \(\mathbb F_2\). This is an exact algebraic test over the closure; no finite-field point count substitutes for it.

**Complete enumeration.** Every nonzero cubic is uniquely represented by an integer mask \(1\le b\le1023\) using the ten ordered monomials above. Exact Jacobian tests leave \(336\) smooth masks. From a subspace \(W\) all of whose nonzero elements are smooth, an extension \(W'=W+\mathbb F_2v\), with \(v\notin W\), is smooth precisely when every element of the coset \(v+W\) is smooth. Enumerating all such cosets, and canonically retaining the sorted set \(W'\setminus\{0\}\), removes all duplicate ordered bases. Every larger admissible space contains an admissible codimension-one subspace, so this recursion omits none. The exact counts by vector-space dimension are
\[
\begin{array}{c|cccc}
\dim_{\mathbb F_2}W&1&2&3&4\\\hline
\#\{W: W\setminus\{0\}\text{ geometrically smooth}\}&336&5544&864&0.
\end{array}
\]
In particular all \(864\) smooth nets are explicitly enumerated. The absence of dimension-four smooth systems is included as a consistency check, **not as a new theorem**: it is covered by the general bound of Asgarli–Ghioca–Reichstein [1].

**Projective equivalence.** Every invertible binary \(3\times3\) matrix is a distinct element of \(\operatorname{PGL}_3(\mathbb F_2)\), because the only nonzero binary scalar is \(1\). Enumerating independent row triples yields exactly \(168\) matrices. For each matrix, substitute its three binary linear forms for \(X,Y,Z\), expand the ten cubic monomials modulo two, and apply the resulting invertible linear transformation to the seven nonzero masks of every net. Taking complete group orbits partitions the \(864\) nets into eight disjoint classes, with sizes as displayed in the theorem. Their sizes sum to \(3\cdot8+5\cdot168=864\). Orbit-stabilizer gives stabilizer orders \(168/8=21\) or \(168/168=1\). The canonical minima yield precisely the eight three-mask bases listed. This gives both exhaustive coverage and pairwise inequivalence of the representatives.

**Rational-point profiles.** Evaluating the seven forms in each representative on the seven points \(\mathbb P^2(\mathbb F_2)\) gives the displayed spectra. This evaluation is supplementary to, not a substitute for, the projective-orbit computation.

## Verification

Execute the included standalone program `verify_smooth_cubic_nets.py` using Python 3.10+ and SymPy 1.12+:

```
python verify_smooth_cubic_nets.py
```

The verifier independently constructs all ten monomials and their exact formal partial derivatives; scans the \(1023\) forms with the homogeneous-ideal criterion; constructs and deduplicates all admissible subspaces through dimension four; enumerates all invertible coordinate matrices and their induced action; determines all orbits and stabilizers; reconstructs every representative and rational-point profile; and asserts all stated totals. It also performs a separate derivative evaluation on every rational projective point over each of \(\mathbb F_2,\mathbb F_4,\mathbb F_8,\mathbb F_{16}\). The independent small-extension scan flags exactly the same \(687\) singular masks, but the full algebraic-closure smoothness conclusion rests on the Gröbner criterion, not on this bounded scan.

The expected final line is:

```
SMOOTH_NET_CLASSIFICATION_PASS 336 5544 864 8
```

## Relationship to prior work

Asgarli, Ghioca, and Reichstein [1, Theorem 2] construct maximal-projective-dimension smooth linear systems for the applicable characteristics and prove that projective dimension greater than the ambient dimension is impossible. In particular, **existence** of a projective plane of smooth ternary cubics over \(\mathbb F_2\), and **nonexistence** of larger smooth systems, are both previously known. Their construction does not supply a census or a projective orbit classification of all the binary smooth nets.

Asgarli and Ghioca [2, Introduction, Theorems 2–3] explicitly distinguish smooth cubic systems from systems whose members are merely geometrically irreducible. Their computational appendix addresses geometric irreducibility of *higher-dimensional* systems and does not determine the eight smooth-net equivalence classes above.

Berg [3] studies enumerative characteristic numbers (curve incidence with general points and tangencies) in characteristic two over an algebraically closed field, a different enumerative problem from the distribution of \(\mathbb F_2\)-rational planes entirely avoiding the smooth-cubic discriminant's rational points. The main new result here is specifically the exact finite-field net count and eight coordinate-orbit types, not the general existence theorem, an individual plane cubic classification, or characteristic numbers.

## Limitations

This is a complete finite-field classification for one field and degree, not a formula for other fields or for smooth members over every algebraic extension. Exhaustive computation uses exact polynomial arithmetic and a particular transparent representation; independent reproduction and historical-priority checking remain appropriate. Prior mathematical tables or unpublished computations could conceivably have the same orbit census under different terminology. No independent audit is claimed.

## References

[1] S. Asgarli, D. Ghioca, Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918 (first public July 2, 2022), https://arxiv.org/abs/2207.00918 ; full text https://arxiv.org/html/2207.00918v2 .

[2] S. Asgarli, D. Ghioca, *Linear system of geometrically irreducible plane cubics over finite fields*, arXiv:2407.18104 (first public July 25, 2024), https://arxiv.org/abs/2407.18104 ; open full text https://webpages.scu.edu/ftp/sasgarli/geom-irred-cubics.pdf .

[3] A. H. Berg, *Enumerative geometry for plane cubic curves in characteristic 2*, Compositio Mathematica 111 (1998), 123–147, https://doi.org/10.1023/A:1000291224146 .
