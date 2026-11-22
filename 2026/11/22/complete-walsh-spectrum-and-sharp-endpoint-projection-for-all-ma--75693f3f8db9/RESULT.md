# Complete Walsh spectrum and sharp endpoint projection for all matchings of the five-by-five bipartite board

## Finding

For the additive Boolean group \(G=\mathbb F_2^{25}\), identify coordinates with the edges of the complete bipartite graph \(K_{5,5}\). Let \(\mathcal M\subset G\) consist of the incidence vectors of all partial matchings, including the empty matching, and let \(T f=1_{\mathcal M}*f\) be counting convolution. There are exactly \(1546\) such matchings. The unnormalized Fourier multiplier \(W(s)=\sum_{m\in\mathcal M}(-1)^{s\cdot m}\) takes exactly \(187\) distinct integer values, with its complete *signed* multiplicity distribution specified by the self-contained spectrum.csv table. Precisely \(1,183,200\) of \(2^{25}\) multipliers vanish, so \(\operatorname{rank}T=32,371,232\). The minimum nonzero absolute multiplier is \(2\), the maximum absolute multiplier is \(1546\), and the sharp spectral condition ratio on the recoverable range is \(773\). If \(\mathcal R=\operatorname{im} T\), the minimum operator norm of any projection \(L^1(G)\to\mathcal R\) and separately of any projection \(L^\infty(G)\to\mathcal R\), with counting or normalized Haar measure, is exactly \(404723613/524288\). The same translation-invariant Fourier-support projection attains both minima.

The 187-row signed histogram in `spectrum.csv` is part of this statement and gives exact multiplicities at every integer multiplier; absent integers have multiplicity zero. It includes a zero frequency multiplicity of 1,183,200 and a single multiplier equal to 1,546.

## Assumptions and scope

Let \(G=(\mathbb F_2)^{25}\) with positions indexed by the edges \((r,c)\) for \(r,c\in\{0,1,2,3,4\}\). A matching is a collection of edges with no shared endpoints. The empty matching is included. We use the unnormalized Walsh transform \(\widehat f(s)=\sum_{x\in G}f(x)(-1)^{s\cdot x}\) and counting convolution \((f*g)(x)=\sum_y f(y)g(x-y)\). The number of matchings is
\[
\sum_{k=0}^5\binom 5k^2 k!=1546.
\]
All ranks and condition ratios refer to linear operators on complex-valued functions on the full group. The condition ratio uses nonzero Fourier multipliers, with no normalization ambiguity. The endpoint projection norm is the induced operator norm for both \(\ell^1\) and \(\ell^\infty\).

## Proof

**Walsh decomposition.** Every group character \(\chi_s(x)=(-1)^{s\cdot x}\) diagonalizes counting convolution, with eigenvalue \(W(s)=\sum_{m\in\mathcal M}\chi_s(m)\). Thus its rank is exactly the number of nonzero \(W(s)\), and its nonzero singular values are the corresponding absolute values. The finite count in `spectrum.csv` gives 1,183,200 zeros and 32,371,232 nonzeros, with minimum positive absolute value 2 and maximum 1,546 (the latter also follows from the triangle inequality and \(W(0)=1546\)). Therefore the sharp condition ratio is 773.

**Exhaustive exact integer certificate, method I.** `verify_fwht.cpp` recursively enumerates all legal partial matchings via the choice of skipping or assigning a fresh column in each row, a disjoint recursion yielding every matching once. Place their indicators at the matching masks in a length-\(2^{25}\) integer array and execute the in-place Walsh butterfly \((u,v)\mapsto(u+v,u-v)\) on each of the 25 bit coordinates. This yields exactly every \(W(s)\), in integer arithmetic, hence every entry of `spectrum.csv`.

**Independent coefficient count, method II.** Write each frequency as a signed \(5\times5\) matrix with row signs \(\varepsilon_{i,c}\in\{-1,+1\}\). For a given set \(C\) of used columns, let \(d_i(C)\) be the signed weight sum of matchings among the first \(i\) rows using exactly \(C\). Set \(d_0(\varnothing)=1\). Then
\[
d_{i+1}(C)=d_i(C)+\sum_{c\in C}\varepsilon_{i,c}d_i(C\setminus\{c\}).
\]
Summing \(d_5(C)\) gives \(W\). Permuting rows preserves \(W\), so `verify_dp.cpp` enumerates all \(\binom{32+5-1}5=376992\) multisets of five signed row patterns, giving each the exact weight \(5!/\prod m_j!\). These weights total \(2^{25}\); the resulting signed histogram agrees entry-for-entry with method I. Integer recurrence, known loop bounds, and the two complete programs constitute a finite exhaustive proof rather than a numerical experiment.

**Optimal projection.** Write \(S=\{s:W(s)\ne0\}\). The translation-invariant projection onto the convolution range has Fourier symbol \(1_S\) and kernel
\[
p(x)=2^{-25}\sum_{s\in S}(-1)^{s\cdot x}.
\]
The final Walsh butterfly of `verify_fwht.cpp` applies the same exact integer transform to \(1_S\), certifying
\[
\sum_{x\in G}\left|\sum_{s\in S}(-1)^{s\cdot x}\right|=25,902,311,232.
\]
The convolution projection's \(\ell^1\) and \(\ell^\infty\) norms are both \(2^{-25}\) times this integer, reducing to \(404723613/524288\). For any (not necessarily translation-invariant) projection \(Q\) onto the translation-invariant range, average \(\tau_gQ\tau_{-g}\) over all \(g\in G\). This average remains a projection onto the same range and has norm at most \(\|Q\|\), since translations are isometries on both endpoint spaces. A translation-invariant projection onto exactly this range must have Fourier symbol \(1_S\), so it is the one just computed. Hence the displayed number is the minimum over all projections, not merely an upper bound.

## Verification

Compile `verify_fwht.cpp` and `verify_dp.cpp` separately with a C++17 compiler. Execute the first with any argument to additionally compute the exact projection numerator. The first program lists all 33,554,432 frequency values through an exact fast Walsh transform. The second independently enumerates the 376,992 unordered row-sign profiles with integer weights summing to 33,554,432. Compare the signed `value:count` lines from both executables with the two columns of `spectrum.csv`. The exact integer projection numerator is 25,902,311,232. Both programs were executed and their spectra were compared term-for-term; the full projection computation also ran.

## Relationship to prior work

Mitchell's 2004 rook-polynomial algorithm studies unsigned rook-number recurrences and provides the natural matching model and ordinary count. Huo, Liang, Liu, and Bai's 2007 monomer–dimer work develops matchings/permanent counting methods. Their inspected full texts do not give the signed Walsh distribution for the complete \(5\times5\) board nor the minimum Fourier-range endpoint projection norm. Existing exact Fourier results for full permutation matrices or perfect matchings address different support sets; inclusion of those sets inside the full matching family does not determine the Fourier cancellations or the support projection of the larger set.

## Limitations

This is an exact finite-board theorem; it does not establish a formula for arbitrary board sizes or rectangular families. The rank describes noiseless counting-convolution identifiability, while the large endpoint norm describes stability of range projection, not an optimal noisy inversion procedure. The self-review cannot exclude an equivalent unindexed calculation; independent audit has not been performed.

## References

- A. G. Mitchell, *A Block Decomposition Algorithm for Computing Rook Polynomials*, arXiv:math/0407004 (initial public posting 2004-06-30), https://arxiv.org/abs/math/0407004.
- Y. Huo, H. Liang, S.-Q. Liu, and F. Bai, *Computing the Monomer-Dimer Systems through Matrix Permanent*, arXiv:0708.1641, https://arxiv.org/abs/0708.1641.
