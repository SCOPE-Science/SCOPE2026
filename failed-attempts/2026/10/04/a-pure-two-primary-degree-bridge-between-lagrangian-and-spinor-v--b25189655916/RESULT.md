# A pure two-primary degree bridge between Lagrangian and spinor varieties
## Finding
For every integer \(n\ge1\), let
\[
L_n=\operatorname{LG}(n,2n)
\]
be the complex Lagrangian Grassmannian in its Pluecker embedding, and let
\[
S_n=\operatorname{OG}(n+1,2n+2)
\]
be either spinor component in its minimal half-spin embedding. Both have dimension
\[
M=\frac{n(n+1)}2.
\]

Their projective degrees satisfy the exact identity
\[
\deg L_n
=
2^{\binom n2}\deg S_n.
\]
Thus all odd-primary arithmetic agrees:
\[
\nu_p(\deg L_n)=\nu_p(\deg S_n)
\]
for every odd prime \(p\), while
\[
\nu_2(\deg L_n)-\nu_2(\deg S_n)=\binom n2.
\]

Equivalently, the two degrees have the same odd part. Moreover,
\[
\nu_2(\deg L_n)
=
M-s_2(M),
\]
where \(s_2(M)\) denotes the number of \(1\)'s in the binary expansion of \(M\).

The first values illustrate that the discrepancy is purely dyadic:
\[
\begin{array}{c|ccccc}
n&1&2&3&4&5\\
\hline
\deg S_n&1&1&2&12&286\\
\deg L_n&1&2&16&768&292864
\end{array}
\]
and the ratios are
\[
1,\ 2,\ 8,\ 64,\ 1024.
\]

## Assumptions and scope
All varieties are over \(\mathbb C\). The Lagrangian Grassmannian uses its standard Pluecker line bundle. The spinor variety uses the minimal half-spin line bundle; this embedding convention is essential because the orthogonal Pluecker line bundle is the square of the spinor generator.

The comparison is between two minuscule or cominuscule homogeneous varieties of the same triangular dimension. It is a statement about their projective degrees, not an isomorphism over \(\mathbb C\).

A later characteristic-two result identifies the principal-minor image of the Lagrangian Grassmannian with a spinor variety. That geometric phenomenon motivates comparing the two degree sequences, but it is not used in the proof below.

## Proof
A degree formula for the Pluecker-embedded Lagrangian Grassmannian is
\[
\deg L_n
=
\frac{M!}{\prod_{i=1}^{n}(2i-1)!}
\prod_{1\le i<j\le n}(2j-2i).
\]
Factor
\[
2j-2i=2(j-i).
\]
There are \(\binom n2\) pairs, and the Vandermonde product at \(1,2,\ldots,n\) is
\[
\prod_{1\le i<j\le n}(j-i)
=
\prod_{j=1}^{n-1}j!.
\]
Hence
\[
\deg L_n
=
2^{\binom n2}
\frac{M!\prod_{j=1}^{n-1}j!}
{\prod_{i=1}^{n}(2i-1)!}.
\]

For the minimally embedded spinor variety, the Schubert basis is indexed by strict partitions contained in the staircase
\[
(n,n-1,\ldots,1).
\]
Repeated multiplication by the hyperplane class counts saturated chains from the empty partition to this staircase. The shifted hook-length formula therefore gives
\[
\deg S_n
=
\frac{M!\prod_{a=2}^{n-1}a!}
{\prod_{a=2}^{n}(2a-1)!}.
\]
Because \(1!=1\), the non-power-of-two factor in the preceding expression for \(\deg L_n\) is exactly this number. Therefore
\[
\deg L_n
=
2^{\binom n2}\deg S_n.
\]

The odd-prime valuation statement follows immediately from the exact ratio.

For the final two-adic formula, apply Legendre's identity
\[
\nu_2(m!)=m-s_2(m)
\]
to the displayed spinor degree product. The resulting cancellation gives
\[
\nu_2(\deg S_n)
=
n-s_2(M).
\]
Adding
\[
\binom n2
\]
from the degree ratio yields
\[
\nu_2(\deg L_n)
=
\binom n2+n-s_2(M)
=
M-s_2(M).
\]
This equals
\[
\nu_2(M!),
\]
so the two-adic content of the Lagrangian degree is exactly that of \(M!\).

## Verification
The bundled exact-integer checker evaluates both factorial product formulas for
\[
1\le n\le100,
\]
verifies the degree ratio, verifies equality of odd parts, and independently recomputes the two-adic valuations from the resulting integers.

It also computes the shifted-staircase tableau count from the general shifted hook product for
\[
1\le n\le20
\]
and checks that this agrees with the spinor factorial formula. These finite computations are regression evidence only; the infinite identity follows from the two symbolic product formulas and the Vandermonde factorization.

## Relationship to prior work
Kresch and Tamvakis develop the Schubert calculus of both maximal orthogonal and Lagrangian Grassmannians. Their orthogonal paper identifies the spinor variety, its strict-partition Schubert basis, and the relevant Pieri structure, while the companion Lagrangian paper supplies the corresponding symplectic Schubert calculus.

Hiep and Tu later state the explicit Pluecker degree formula for the Lagrangian Grassmannian used above. Fischer gives a bijective proof of the shifted hook-length formula used to evaluate the spinor top intersection.

Van Geemen and Marrani prove a striking characteristic-two relationship: the principal-minor image of the Lagrangian Grassmannian becomes the spinor variety. Their statement concerns a different projective map and characteristic two; it does not state the complex projective-degree ratio above.

Purbhoo's work relates Lagrangian Grassmannians to shifted and unshifted staircase tableaux through a Wronski map. Its available abstract gives related tableau enumerations, but not the comparison of the natural projective degrees of \(L_n\) and \(S_n\). Because the current identity is a short consequence of classical product formulas, an unindexed source could contain it explicitly; this remains the principal originality risk.

## Limitations
The statement depends on the embedding conventions. Replacing the spinor half-spin embedding by the orthogonal Pluecker embedding changes the hyperplane class and hence the degree.

The result compares numerical projective degrees only. It does not construct a complex morphism
\[
L_n\longrightarrow S_n
\]
of degree \(2^{\binom n2}\), and the characteristic-two principal-minor map should not be interpreted as such a construction over \(\mathbb C\).

The identity itself is exact, but the literature search cannot exclude an older source in which this particular comparison of two known product formulas was already written down.

## References
Andrew Kresch and Harry Tamvakis, *Quantum cohomology of orthogonal Grassmannians*, arXiv:math/0306338, first submitted 24 June 2003; Compositio Mathematica 140 (2004), 482--500.

Andrew Kresch and Harry Tamvakis, *Quantum cohomology of the Lagrangian Grassmannian*, arXiv:math/0306337, first submitted 24 June 2003.

Dang Tuan Hiep and Nguyen Chanh Tu, *An identity involving symmetric polynomials and the geometry of Lagrangian Grassmannians*, arXiv:1612.09177; Journal of Algebra 565 (2021), 564--581.

Ilse Fischer, *A bijective proof of the hook-length formula for shifted standard tableaux*, arXiv:math/0112261.

Bert van Geemen and Alessio Marrani, *Lagrangian Grassmannians and Spinor Varieties in Characteristic Two*, SIGMA 15 (2019), 064.

Kevin Purbhoo, *A marvellous embedding of the Lagrangian Grassmannian*, arXiv:1403.0984; Journal of Combinatorial Theory, Series A 155 (2018), 1--26.
