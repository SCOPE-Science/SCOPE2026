# Exact six-vertex involution Fourier spectrum and sharp projection amplification

## Finding

Let \(\mathcal I_6\) be the set of all \(76\) permutation matrices of involutions on six labels, embedded in the additive binary matrix group \(G=(\mathbb F_2)^{6\times6}\). Write \(f=\mathbf1_{\mathcal I_6}\), let \(Tg=f*g\) use **unnormalized counting convolution**, and let \(P\) be the \(\ell^2(G)\)-orthogonal projection onto the range of \(T\).

The exact nullity and rank are
\[
\dim\ker T=14\,313\,062\,400=6825\cdot2^{21},\qquad
\operatorname{rank}T=54\,406\,414\,336=25943\cdot2^{21}.
\]
The smallest nonzero absolute Fourier multiplier equals \(4\), giving
\[
\|T^\dagger\|_{2\to2}=\frac14,\qquad \kappa_+(T)=19.
\]
The exact sharp endpoint amplification of the range projection is
\[
\boxed{\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}=\frac{762169}{16384}.}
\]

Equivalently, on the \(15\) edge-sign bits of \(K_6\), the signed matching sum has exactly \(6825\) zero frequencies and \(25943\) nonzero frequencies, with **19 distinct signed values**. The zero frequencies have negative-edge supports of sizes \(5,7,9,11\) only, in respective counts \(480,2880,2280,1185\). Thus the first cancelling signings use exactly **five** negative edges. Those \(480\) signings form **two** vertex-relabeling orbits: orbit sizes \(120\) and \(360\), with negative-edge degree sequences \((4,2,1,1,1,1)\) and \((3,3,2,1,1,0)\). All \(6825\) zero signings form exactly **26** orbits; their canonical labelled representatives and orbit sizes are in `orbit_table.csv`.

The reduced signed multiplier multiplicities, listed by the multiplier value, are:

| Multiplier | Multiplicity | Multiplier | Multiplicity |
|---:|---:|---:|---:|
| \(-24\) | 6 | \(4\) | 5540 |
| \(-20\) | 75 | \(8\) | 3570 |
| \(-16\) | 465 | \(12\) | 1815 |
| \(-12\) | 1740 | \(16\) | 963 |
| \(-8\) | 4105 | \(20\) | 660 |
| \(-4\) | 6348 | \(24\) | 240 |
| \(0\) | 6825 | \(28\) | 100 |
|  |  | \(32\) | 195 |
|  |  | \(36\) | 60 |
|  |  | \(44\) | 45 |
|  |  | \(56\) | 15 |
|  |  | \(76\) | 1 |

The spectrum in this table is the reduced signed matching sum; the full matrix-group Fourier spectrum has its nonzero signs symmetrically paired along each reduction fiber.

## Assumptions and scope

All vector spaces are over \(\mathbb F_2\), all labels are distinct, the Fourier transform is unnormalized, and the counting convolution has no division by the group order. For \(K\in G\), define its Walsh multiplier by
\[
W(K)=\sum_{\sigma^2=\mathrm{id}}(-1)^{\sum_{i=1}^{6}K_{i,\sigma(i)}}.
\]
For each \(i<j\), define
\[
t_{ij}=K_{ij}+K_{ji}+K_{ii}+K_{jj}\pmod2.
\]
Let \(\mathcal M(K_6)\) contain every graph matching, including the empty matching. Define
\[
Z(t)=\sum_{M\in\mathcal M(K_6)}(-1)^{\sum_{ij\in M}t_{ij}}.
\]
The minimal negative-edge support assertion applies to this **effective** edge-sign vector \(t\), not to entrywise support of the ambient matrix frequency \(K\). The result is a complete exact finite calculation at six labels, not a classification for all orders.

## Proof

**Fourier reduction.** Each involution partitions its labels into fixed points and transposed pairs. If \(a_i=K_{ii}\) and \(b_{ij}=K_{ij}+K_{ji}\), its character equals \((-1)^{\sum_i a_i}\prod_{ij\in M}(-1)^{b_{ij}+a_i+a_j}\). Hence
\[
W(K)=(-1)^{\sum_iK_{ii}}Z(t).
\]
The map \(\phi:G\to(\mathbb F_2)^{15}\), \(K\mapsto t\), is surjective: each \(t_{ij}\) can be prescribed using \(K_{ij}\) with all other entries zero. Every fiber therefore contains \(2^{36-15}=2^{21}\) frequencies. Thus the zero counts and ranks follow from the reduced spectrum. The maximum multiplier is \(Z(0)=|\mathcal M(K_6)|=76\); the exact minimum nonzero magnitude is \(4\).

**Exact certificate for the spectrum.** Order the fifteen edges lexicographically. To each matching \(M\) associate its 15-bit incidence mask \(m(M)\), and let \(c_m\) be \(1\) if \(m\) represents a matching and \(0\) otherwise. There are exactly \(76\) such masks. The unnormalized 15-fold Walsh-Hadamard transform of \(c\) is exactly \(Z(t)\). `check_spectrum.cpp` enumerates the masks by the recurrence that either leaves the least remaining vertex fixed or pairs it to another remaining vertex, computes **all \(32768\) coefficients**, and asserts the nineteen-level table. `check_spectrum.py` independently evaluates the same \(32768\) coefficients by a memoized recurrence on remaining vertex subsets **for each signing**, without using that precomputed matching-mask transform. Both agree entry by entry, with the common complete binary-spectrum digest reported in `VERIFICATION.md`.

For every zero mask, the C++ certificate relabels its six vertices through all \(720\) permutations. Taking the minimum 15-bit encoding proves that the zeros split into precisely the 26 orbits listed in `orbit_table.csv`. The associated orbit-size histogram is \(\{30:1,45:1,60:2,90:1,120:2,180:7,360:10,720:2\}\), summing to \(6825\). The smallest zero-support size is five, whose two orbits have the stated degree sequences. Exhaustiveness follows because every 15-bit signing is included; no sampled classification or extrapolation is used.

**Exact sharp operator norms.** On the orthonormal Walsh basis, \(T\) acts diagonally by \(W(K)\). Its Moore-Penrose inverse on the nonzero Fourier modes therefore has norm reciprocal to the smallest nonzero multiplier; the positive-spectrum condition number is the quotient of the largest and smallest absolute nonzero multipliers. Let \(s(t)=\mathbf1_{Z(t)\ne0}\). Since the range-projection multiplier on \(G\) is \(s\circ\phi\), its convolution kernel is supported on the annihilator of \(\ker\phi\); on that subgroup it is the normalized inverse Walsh transform of \(s\) over fifteen bits. Accordingly
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}
=2^{-15}\sum_{u\in(\mathbb F_2)^{15}}\left|\sum_{t\in(\mathbb F_2)^{15}}s(t)(-1)^{u\cdot t}\right|.
\]
The exact integer sum is \(1\,524\,338\), producing \(762169/16384\). For convolution on a finite group, the \(\ell^1\) and \(\ell^\infty\) norms equal the \(\ell^1\)-mass of its kernel, attained by a point mass and by a matching-sign input respectively. This establishes sharpness, not merely an upper bound.

## Verification

The scripts `check_spectrum.cpp` and `check_spectrum.py` use only C++17 and Python 3 standard libraries. They independently produce the full ordered reduced multiplier array; both check the zero-support counts, minimum nonzero magnitude, Parseval identity and range-projection mass. Reproduce by compiling `check_spectrum.cpp` using `g++ -O2 -std=c++17` and running its executable with optional paths for a 32-bit little-endian spectrum and the orbit table, then running `python3 check_spectrum.py`. The code's expected success markers and complete-spectrum digest are recorded in `VERIFICATION.md`.

## Relationship to prior work

Involutions as fixed points and disjoint transpositions and their enumerators are classical; Dukes (2004) studies involution statistics, while Li–Shi–Trinks (2014) treat matching-polynomial reconstruction. Previously available complete-graph matching Fourier results already supply a general signed-matching evaluation in terms of matching counts, a dyadic gcd and examples of singular dimensions. **The reduction to signed matchings, the general formula, and the existence of six-vertex zeros are not claimed as new.** The present finding evaluates the full order-six 19-level spectrum, all zero orbits, the five-edge cancellation threshold with both extremal graph types, and the sharp endpoint range-projection norm. These are not tabulated in the previously inspected results.

Sehrawat–Bhattacharjya (2018) classify signed \(K_6\) under **vertex switching and relabeling**, rather than signed matching-polynomial zeros under **relabeling alone**. Vertex switching changes the unweighted monomer terms in \(Z(t)\), so their sixteen switching-isomorphism classes do not determine the present 26 zero-signing automorphism orbits. Other exact Fourier spectra for perfect matchings and all permutations concern different support sets. The generic matching identity makes the finite problem computable but does not itself evaluate the displayed 19-level distribution or the projection's absolute Fourier-sum norm.

## Limitations

The full exact census and operator endpoint constant concern **six labels only**; no formula for arbitrary-order nullities, orbit counts or range projection norms is asserted. The numerical tables are certified by exhaustive integer computations and an independent recurrence, not by a hand classification of all signed graphs. The complete matching-spectrum array is regenerated by the source code rather than embedded as a 131072-byte binary table. Historical priority is bounded by the inspected sources and accessible search coverage; independent external validation has not been performed.

## References

1. W. M. B. Dukes, *Permutation statistics on involutions*, arXiv:math/0412222v1 (public 2004-12-11). https://arxiv.org/abs/math/0412222
2. X. Li, Y. Shi, M. Trinks, *Polynomial reconstruction of the matching polynomial*, arXiv:1404.3469v1 (public 2014-04-14). https://arxiv.org/abs/1404.3469
3. D. Sehrawat, B. Bhattacharjya, *Signed Complete Graphs on Six Vertices*, arXiv:1812.08383v1 (public 2018-12-20). https://arxiv.org/abs/1812.08383
