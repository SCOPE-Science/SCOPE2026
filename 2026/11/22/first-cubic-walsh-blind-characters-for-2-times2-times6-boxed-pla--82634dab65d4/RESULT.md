# First cubic Walsh blind characters for \(2\times2\times6\) boxed plane partitions

## Finding
Let \(P=[2]\times[2]\times[6]\) be the Cartesian product of chains, and identify an order ideal \(I\subseteq P\) with its 24-bit membership vector in \(G=\mathbb F_2^{24}\). The 336 ideals define an indicator kernel \(f=\mathbf1_{J(P)}\). Its unnormalized Fourier multiplier at a selected cube set \(S\subseteq P\) is
\[
W(S)=\sum_{I\in J(P)}(-1)^{|I\cap S|}.
\]
**The first Walsh cancellations have degree three:** \(W(S)\ne0\) for every \(|S|\le2\), whereas exactly 32 of the \(\binom{24}{3}=2024\) triples have \(W(S)=0\). The 32 are exactly eight orbits, each of size four, under the two commuting involutions that swap the first two coordinates and reverse all three coordinates of \(P\).

For the whole 24-dimensional group, exactly \(1{,}414{,}094\) Fourier multipliers vanish. Hence the convolution \((Tg)(x)=\sum_{y\in G}f(y)g(x-y)\) has
\[
\operatorname{rank}T=16{,}777{,}216-1{,}414{,}094=15{,}363{,}122.
\]
The least nonzero absolute multiplier is \(2\), the largest is \(336\), and the positive-spectrum Hilbert-space condition number is \(168\). The minimum endpoint operator norms among **all** real- or complex-linear projections onto the recoverable Fourier range are
\[
\min_{Q^2=Q,\ \operatorname{ran}Q=\operatorname{ran}T}\|Q\|_{\ell^1\to\ell^1}
=\min_{Q^2=Q,\ \operatorname{ran}Q=\operatorname{ran}T}\|Q\|_{\ell^\infty\to\ell^\infty}
=\frac{2{,}295{,}674{,}241}{4{,}194{,}304}.
\]

In the natural sequence of boxes \([2]\times[2]\times[n]\) for \(1\le n\le6\), the minimum vanishing character weights are respectively \(1,2,1,\text{none},1,3\). Thus width six is the first in this sequence with cancellation but no degree-one or degree-two cancellation.

## Assumptions and scope
The chains are ordered coordinatewise and indexed starting from \(1\). A plane partition is a four-entry array of heights \((a,b,c,d)\) with \(0\le d\le\min(b,c)\), \(0\le b,c\le a\le6\), in the shape
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
It represents exactly the cubes \((i,j,k)\) with \(1\le k\le h_{ij}\). For the binary embedding use \(\operatorname{bit}(i,j,k)=12(i-1)+6(j-1)+(k-1)\). Characters are the real Walsh functions \(\chi_S(x)=(-1)^{\langle \mathbf1_S,x\rangle}\). All transforms and convolution are unnormalized with counting measure; \(\ell^p\) norms use either counting measure or consistently normalized measure (the induced operator norms agree). The projection minimum ranges over all linear projections, without a symmetry hypothesis.

Eight representatives of the 32 vanishing triples (written as triples of cube coordinates) are:

| Orbit | First cube | Second cube | Third cube |
|---:|---|---|---|
| 1 | \((1,1,3)\) | \((1,1,6)\) | \((1,2,2)\) |
| 2 | \((1,1,3)\) | \((1,2,2)\) | \((2,1,4)\) |
| 3 | \((1,1,3)\) | \((1,2,5)\) | \((2,2,1)\) |
| 4 | \((1,1,5)\) | \((1,2,1)\) | \((2,2,2)\) |
| 5 | \((1,1,5)\) | \((1,2,2)\) | \((2,2,2)\) |
| 6 | \((1,1,5)\) | \((1,2,3)\) | \((2,2,2)\) |
| 7 | \((1,1,6)\) | \((1,2,1)\) | \((2,2,1)\) |
| 8 | \((1,2,1)\) | \((1,2,5)\) | \((2,1,3)\) |

Each orbit consists of a representative and its images under coordinate exchange, simultaneous reversal \((i,j,k)\mapsto(3-i,3-j,7-k)\), and their composition. Coordinate exchange is a poset automorphism. Reversal is an order anti-automorphism, and ideal complementation following reversal bijects the ideal family to itself, sending a multiplier to \((-1)^{|S|}\) times its reversal. Therefore both operations preserve the zero set.

## Proof
**1. Exact parametrization and two enumerators.** An ideal is uniquely determined by the four heights above. Exhaustively iterating \(a,b,c,d\) over the stated ranges gives 336 distinct bit masks; the boxed product formula gives the same total \((6+1)(6+2)^2(6+3)/12=336\). Independently, beginning with the empty ideal, add a cube only if its immediate predecessors in all three directions have been added. Breadth-first closure produces exactly the same set of 336 masks. Both methods are implemented in the accompanying standalone checker, with set equality asserted.

**2. Finite low-degree classification.** For any frequency mask \(s\), compute \(W(s)\) by summing \(+1\) or \(-1\) over the 336 ideal masks according to the parity of their binary intersection with \(s\). Evaluating this defining expression for every \(\binom{24}{1}+\binom{24}{2}+\binom{24}{3}=2324\) frequency mask of weight 1, 2, or 3 shows no zero in weights 1 and 2 and exactly 32 zeros in weight 3. Separately form the four symmetry images of each of the eight triples in the table. They are 32 distinct masks, each appears among the calculated zeros, and no other weight-three zero exists. This is a finite exhaustive exact-integer proof, not a statistical sample.

**3. Complete Fourier census.** Initialize a signed-integer array \(A\) indexed by \(G\), with \(A(x)=1\) on the 336 ideal masks and zero otherwise. The elementary Walsh butterfly \((u,v)\mapsto(u+v,u-v)\), applied in each of the 24 bit directions, transforms it to the complete array of \(W(s)\), by induction on dimension. The exact count of zero entries is \(1{,}414{,}094\), their weight histogram is reproduced by the checker, and the least nonzero magnitude is \(2\). The maximal magnitude is 336 at the trivial frequency. Character orthogonality gives convolution diagonalization and the stated rank and positive-spectrum condition number. Parseval and Fourier inversion are independently checked via \(\sum_s W(s)^2=336\cdot2^{24}\) and \(\sum_s W(s)=2^{24}\). The checker additionally compares 8192 individual transformed coefficients with signed sums calculated directly from the enumerated ideals.

**4. Sharp endpoint projection.** Let \(E=\{s:W(s)\ne0\}\), with \(|E|=15{,}363{,}122\). The canonical range projection is convolution by \(K(x)=2^{-24}\sum_{s\in E}\chi_s(x)\). An exact second Walsh transform of the indicator of \(E\) yields
\[
\sum_{x\in G}\left|\sum_{s\in E}\chi_s(x)\right|=9{,}182{,}696{,}964.
\]
Thus both endpoint operator norms equal \(9{,}182{,}696{,}964/2^{24}\), reducing to the displayed rational constant. For any other projection \(R\) onto \(\operatorname{ran}T\), average its conjugates by the group translations. The average still has range \(\operatorname{ran}T\), acts identically there, and has operator norm no larger than \(R\), because translations are isometries on both endpoints. It commutes with every translation, so is a Fourier multiplier taking value one exactly on \(E\) and zero off \(E\). Hence it must equal the canonical projection. This proves optimality without assuming symmetry of competitors.

**5. First occurrence in the small-box sequence.** The same exact height enumeration and complete Walsh butterflies for widths \(1,2,3,4,5,6\) yield respectively 6, 61, 680, 0, 107510, 1414094 vanishing characters; their least vanishing weights are respectively 1, 2, 1, none, 1, 3. Since these are all the widths at most six, the first-occurrence assertion is exhaustive within the declared family.

## Verification
Compile the standalone `check.cpp` with a C++17 compiler (GCC or Clang provides the population-count intrinsic) and run it in a writable directory:

```sh
c++ -std=c++17 -O3 check.cpp -o check
./check
```

The expected output begins with `BOX_226_WALSH_PASS`. This program reproduces the direct low-degree signed census, the eight four-element symmetry orbits, independent legal-ideal enumerations, all \(2^{24}\) Walsh multipliers and zero-weight counts, 8192 separate direct character sums, the rank and spectral gap, the sharp projection-kernel \(\ell^1\) sum, both Parseval identities, and the full transforms for the smaller boxes. The proof of the projection optimum is analytic and is given above; the computation supplies its exact rational value.

## Relationship to prior work
MacMahon's product formula and its modern treatment by Ciucu describe the unsigned number of boxed plane partitions and their relation to hexagon tilings. Hersh, Shareshian and Stanton analyze the volume-weighted \(q=-1\) specialization, a single particular all-cubes sign character. Cook and Nagel examine determinant-induced signs for lozenge tilings and nonintersecting path families, not independent signs for every cube coordinate. Borodin, Gorin and Rains give a structured elliptic weight product, whose parameter-constrained weights do not supply the 24 freely chosen binary cube signs or this zero locus.

The closest available published Boolean-Fourier classification treats the **different** \(2\times3\times4\) box (490 ideals), determining its full 24-bit spectrum and sharp projection norm. It demonstrates the applicable transform and translation-averaging method, neither of which is new here. A 336-ideal \(2\times2\times6\) zero-weight-three classification, its 32 triple orbits, and its numerical rank and endpoint constant do not follow from the distinct 490-ideal numeric table. Searches and targeted full-text comparisons found no prior occurrence of the exact new claim, but no claim of exhaustive historical priority is made.

## Limitations
The complete spectral census is finite, valid for this box only. The first-occurrence statement is restricted to the widths one through six; no classification for all larger widths or other three-dimensional boxes is proved. The checker requires sufficient memory for two sequential 24-bit Walsh arrays and uses exact signed integers. There is no independently conducted mathematical audit, and an unindexed equivalent signed-tiling calculation cannot be categorically ruled out.

## References
1. M. Ciucu, *Plane Partitions I: A Generalization of MacMahon's Formula*, arXiv:math/9808017, initially public 1998-08-04; introduction and boxed product formula, https://arxiv.org/abs/math/9808017.
2. A. Borodin, V. Gorin, E. M. Rains, *q-Distributions on Boxed Plane Partitions*, arXiv:0905.0679, initially public 2009-05-05; Section 2 and Theorem 10.5, https://arxiv.org/abs/0905.0679.
3. D. Cook II, U. Nagel, *Enumerations of Lozenge Tilings, Lattice Paths, and Perfect Matchings and the Weak Lefschetz Property*, arXiv:1305.1314, initially public 2013-05-06; Section 5, https://arxiv.org/abs/1305.1314.
4. P. Hersh, J. Shareshian, D. Stanton, *The \(q=-1\) Phenomenon via Homology Concentration*, arXiv:1310.7066, initially public 2013-10-26; Section 5, https://arxiv.org/abs/1310.7066.
5. *Exact Walsh Spectrum and Optimal Endpoint Projection for \(2\times3\times4\) Boxed Plane Partitions* (2026), publicly available: https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-walsh-spectrum-and-optimal-endpoint-projection-for-2-times--009897c7d9c4.
