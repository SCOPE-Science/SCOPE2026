# Petersen acyclic orientations: exact Walsh nullity, correlation shells, and optimal projection norm

## Finding

Let \(P\) be the Petersen graph on vertices \(0,\ldots,9\), with outer cycle \(0,1,2,3,4,0\), spokes \(i\leftrightarrow i+5\) for \(0\le i\le4\), and inner star \(i+5\leftrightarrow5+((i+2)\bmod5)\). Order its fifteen undirected edges lexicographically. Encode an orientation by \(x\in\mathbb F_2^{15}\): edge \((a,b)\), \(a<b\), points from \(a\) to \(b\) if its bit is zero and in the reverse direction if its bit is one. Let \(A\) be the family of acyclic orientations and define
\[
W(u)=\sum_{x\in A}(-1)^{u\cdot x},\qquad u\in\mathbb F_2^{15}.
\]

The exhaustive signed spectrum has 60 levels, including 19,112 zero multipliers; hence convolution by \(1_A\) has
\[
\boxed{\operatorname{rank}T_A=13\,656.}
\]

Of the zero frequencies, 16,384 have odd Hamming weight (forced by reversal of every edge), and another 2,728 have even weight. The absolute two-edge Fourier correlations have three sharply distinguished shells, determined by edge distance in the line graph of \(P\):

| Line-graph distance | Number of unordered pairs | \(\lvert\mathbb E[(-1)^{x_e+x_f}]\rvert\) |
|---:|---:|---:|
| 1 | 30 | \(81/695\) |
| 2 | 60 | \(9/139\) |
| 3 | 15 | \(0\) |

Let \(E=\{u:W(u)\ne0\}\), and let \(R\) be the convolution range. Among **all** real or complex linear projections from \(\ell^1(\mathbb F_2^{15})\) onto \(R\), and likewise from \(\ell^\infty(\mathbb F_2^{15})\) onto \(R\), the respective minimum operator norms agree and are
\[
\boxed{\Lambda_1(R)=\Lambda_\infty(R)=\frac{34809}{1024}.}
\]

## Assumptions and scope

All 32,768 orientation masks are distinguished; no quotient by graph automorphisms is taken. Acyclic means there is no directed cycle of any length. The Fourier transform is unnormalized, and counting convolution is \((T_A f)(y)=\sum_{x\in\mathbb F_2^{15}}1_A(x)f(y+x)\). The \(\ell^1\) and \(\ell^\infty\) norms are unweighted finite-vector norms. The projection minimum allows arbitrary linear projections, without translation or graph-symmetry assumptions. Graph distances in the table are shortest-path distances in the **line graph**, not distances between endpoints of the original edges.

## Proof

**1. Complete orientation enumeration.** The edge array in `verify_petersen.cpp` is

```
(0,1),(0,4),(0,5),(1,2),(1,6),(2,3),(2,7),(3,4),
(3,8),(4,9),(5,7),(5,8),(6,8),(6,9),(7,9).
```

The bit mask \(m\in\{0,\ldots,2^{15}-1\}\) uniquely specifies one orientation. A topological-peeling test accepts an orientation exactly when it has no directed cycle: in any finite nonempty acyclic digraph a source exists, and a nonempty digraph with no source contains a directed cycle. Independently, the verifier enumerates all simple undirected Petersen cycles by starting at their minimum-labeled vertex and retaining one of the two traversal directions. There are exactly 57 such cycles, distributed by length as 12 of length five, 10 of length six, 15 of length eight, and 20 of length nine. An orientation is cyclic exactly when at least one of these 57 cycles is coherently directed in either direction. Both predicates agree for **every** one of the 32,768 masks and yield \(|A|=16\,680\). This agrees with the classical chromatic-polynomial specialization but is not the new result.

**2. Exact Fourier spectrum.** The verifier initializes the complete binary indicator array \(1_A\), then uses a full integer Walsh–Hadamard transform. Independently, it calculates each of the 16,384 even-weight Fourier coefficients by its literal signed sum over all 16,680 accepted masks. Every coefficient agrees. The remaining odd-weight coefficients are zero: if \(x\in A\), reversing all fifteen edges gives \(x+\mathbf 1\in A\), whereas the Walsh character changes by \((-1)^{|u|}\). The signed histogram is `walsh_histogram.csv` and its 60 entries sum to 32,768 frequencies. It has exactly 19,112 zeros. Since characters diagonalize counting convolution, its rank is the number of nonzero multipliers, \(32\,768-19\,112=13\,656\). The squared-multiplier identity \(\sum_u W(u)^2=2^{15}\lvert A\rvert\) checks exact Parseval normalization.

**3. Two-edge correlation shells.** For a uniformly chosen acyclic mask, \(\mathbb E[(-1)^{x_e+x_f}]=W(\mathbf e_e+\mathbf e_f)/16680\). The verifier independently computes all 105 line-graph distances by breadth-first search, and all corresponding Walsh coefficients by both transform and direct signed enumeration. Its exact assertions give 30 distance-one pairs with absolute coefficient 1,944, 60 distance-two pairs with absolute coefficient 1,080, and 15 distance-three pairs with coefficient zero. Reducing these fractions gives the displayed \(81/695\), \(9/139\), and zero. The signs of the nonzero correlations depend on the fixed reference edge orientations; the reported absolute magnitudes do not.

**4. Unrestricted optimal projection norm.** Write \(H(x)=\sum_{u\in E}(-1)^{u\cdot x}\). The unique translation-invariant projection onto \(R\) is convolution by \(K(x)=2^{-15}H(x)\): in Fourier coordinates, it equals one on \(E\) and zero off \(E\). Its \(\ell^1\) and \(\ell^\infty\) operator norms both equal \(\sum_x|K(x)|\). The verifier applies an independent Walsh–Hadamard transform to the support indicator \(1_E\), and `projection_kernel_histogram.csv` gives every resulting coefficient with multiplicity. Exact summation yields
\[
\sum_x|H(x)|=1\,113\,888,\qquad
\sum_x H(x)^2=2^{15}\lvert E\rvert.
\]
Hence \(\sum_x|K(x)|=1\,113\,888/32\,768=34\,809/1\,024\). For any linear projection \(Q\) onto \(R\), average its conjugates by all translations. The average remains a projection onto \(R\) (translations preserve the subspace and all conjugates fix it) and has norm no greater than \(\lVert Q\rVert\). Translation-invariant projections onto \(R\) are unique by their Fourier multipliers, so this average must be the canonical \(K\)-projection. It follows that no unrestricted projection can improve either endpoint norm.

## Verification

Compile using `g++ -std=c++17 -O3 verify_petersen.cpp -o verify_petersen` and execute `./verify_petersen` from the directory containing the two CSV certificates. The checker has no nonstandard library dependencies. The complete tests are exact-integer: two independent acyclicity predicates; full Walsh transform against direct sums at every even-weight frequency; the forced odd-frequency cancellation; signed and projection-kernel CSV equality; both Parseval identities; all 105 two-edge correlation magnitudes and graph distances. The expected successful output starts with `PETERSEN_ACYCLIC_FOURIER_PASS` and gives 57 cycles, 16,680 acyclic masks, 19,112 zero frequencies, rank 13,656, and kernel absolute sum 1,113,888.

## Relationship to prior work

Stanley's 1973 chromatic reciprocity theorem determines the total number of acyclic orientations from the chromatic polynomial. Gebhard and Sagan's 1999 account develops unique-sink enumeration and related bijections. Cameron's 2015 account records 16,680 Petersen acyclic orientations and 168 automorphism orbits. The published finite census *Nine symmetry types and exact click distances for Petersen acyclic orientations* determines click-reconfiguration components, diameters and symmetry orbits. These results provide enumeration and structural context, but their stated values do not determine a Walsh multiplier distribution, two-edge correlations under the uniform acyclic law, or the sharp projection constant. The present finding is not a re-enumeration of the known 16,680 total or the previously studied click components.

## Limitations

The numerical spectrum is established for the single Petersen graph, not every cubic or vertex-transitive graph. The edge signs of the two-point correlations depend on the chosen orientation convention, while magnitudes and zero status are invariant under changing reference directions. No full spectrum formula for larger Kneser graphs is claimed. The complete finite computation has been checked internally by distinct algorithms but has not undergone independent external mathematical validation. Historical novelty searches cannot exclude unindexed tables or unpublished calculations; potentially relevant PDFs inspected only in part remain a residual source risk.

## References

1. R. P. Stanley, *Acyclic orientations of graphs*, Discrete Mathematics 5 (1973), 171–178, DOI 10.1016/0012-365X(73)90108-8. Accessible 2006 reprint: https://math.mit.edu/~rstan/pubs/pubfiles/18.pdf
2. D. D. Gebhard and B. E. Sagan, *Sinks in Acyclic Orientations of Graphs*, publicly posted 1999-07-12, arXiv:math/9907078. https://arxiv.org/abs/math/9907078
3. P. J. Cameron, *Acyclic orientations* (2015), https://cameroncounts.github.io/web/talks/15/pcc.pdf
4. *Nine symmetry types and exact click distances for Petersen acyclic orientations*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-nine-symmetry-types-and-exact-click-distances-for-petersen-acycl--5191306166b5
