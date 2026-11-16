# Exact Walsh recovery and sharp endpoint projection for the binary order-four de Bruijn codebook

## Finding

Let \(G=(\mathbb F_2)^{16}\), with cyclic indices \(0,\ldots,15\). Let \(\mathcal B_4\subset G\) consist of all **rooted** binary order-four de Bruijn words: each of the sixteen binary four-bit factors occurs exactly once among the sixteen consecutive cyclic windows. Rotations count as different words. For \(u\in G\), define the unnormalized Boolean Fourier coefficient
\[
W(u)=\sum_{b\in\mathcal B_4}(-1)^{\sum_{i=0}^{15}u_i b_i}.
\]
Let \(T\) be counting convolution by \(1_{\mathcal B_4}\) on functions on \(G\), and let \(R=\operatorname{ran} T\).

**Complete finite spectral theorem.** There are exactly \(256\) codewords. Every Walsh coefficient is divisible by \(16\). The exact signed multiplier histogram is:

| Signed multiplier | Number of characters |
| ---: | ---: |
| -96 | 64 |
| -80 | 32 |
| -64 | 96 |
| -48 | 1,088 |
| -32 | 2,640 |
| -16 | 7,872 |
| 0 | **42,022** |
| 16 | 7,744 |
| 32 | 2,576 |
| 48 | 1,184 |
| 64 | 216 |
| 256 | 2 |

In particular,
\[
\operatorname{rank}T=23514,\qquad
\min_{W(u)\ne0}|W(u)|=16,\qquad
\| (T|_R)^{-1}\|_{2\to2}=\frac1{16}.
\]
Here \(T|_R\) is the restriction to its invariant Fourier range, with counting-measure \(\ell^2\) norm; it is invertible on \(R\). The largest multiplier magnitude is \(256\), so the nonzero-spectrum condition number is \(16\).

The sharp endpoint projection norms, minimized over **all** real or complex linear projections onto \(R\), are
\[
\boxed{\Lambda_1(R)=\Lambda_\infty(R)=\frac{157517}{4096}.}
\]

Of the \(42,022\) zero characters, \(32,768\) are forced by bit-complement symmetry (odd Hamming weight). There are \(9,254\) additional even-weight zeros. At Hamming weight two, precisely the \(48\) characters supported on cyclic pairs of separation one, two, or three vanish; the other \(72\) do not. More precisely, for the circular separation \(d=\min(|i-j|,16-|i-j|)\) of two distinct bit positions, the two-coordinate multiplier takes the following values:

| Separation \(d\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(W(e_i+e_j)\) | 0 | 0 | 0 | -96 | 16 | -16 | -48 | 32 |

This is an exact first-nonlocal-lag correlation law for the uniform rooted order-four de Bruijn ensemble; the first three zeros follow from local four-window uniformity, while the later values require the complete ensemble.

## Assumptions and scope

The coordinate group is the **word-space** group \((\mathbb F_2)^{16}\), not the cyclic time-shift group \(\mathbb Z/16\mathbb Z\). The Fourier transform is unnormalized, and convolution is the counting sum \((Tf)(x)=\sum_{b\in\mathcal B_4}f(x-b)\). All binary inner products are interpreted modulo two. The group is finite, and every norm uses counting measure on \(G\). A rooted word is identified with its literal sixteen-coordinate vector; complementary and rotated words are distinct unless identical as vectors.

## Proof

**Complete codebook enumeration.** A direct method checks every one of the \(2^{16}\) binary words and retains it exactly when the sixteen cyclic four-bit windows are all distinct. It retains \(256\) words. An independent state-transition method considers the eight-bit feedback tables \(g:\mathbb F_2^3\to\mathbb F_2\) and the reversible recurrence
\[
b_{i+4}=b_i+g(b_{i+1},b_{i+2},b_{i+3})\pmod2.
\]
Every de Bruijn cycle, rotated to its unique all-zero four-bit state, arises from exactly one such table: for each triple, the two incoming states must have different successor bits, or a four-bit window would repeat. Conversely, a table whose induced permutation of the sixteen four-bit states is one cycle generates a de Bruijn sequence. Exhausting all \(256\) tables produces exactly \(16\) single-cycle tables. Their sixteen rotations produce \(256\) distinct rooted words, and their set agrees exactly with the direct window-based enumeration. This proves the finite domain is complete without assuming a supplied codeword table.

**Exact Fourier calculation.** Initialize the length-\(65536\) integer vector with ones at precisely these \(256\) words, and apply sixteen butterfly stages \((a,b)\mapsto(a+b,a-b)\). The resulting integer vector is exactly \(W\) by the elementary product-character factorization of the Walsh transform. Independently, at every one of the \(65536\) frequencies, directly sum \((-1)^{u\cdot b}\) over the separately generated feedback-table words. The two arrays agree entry-by-entry. Tallying the exact integers proves the twelve-row histogram, rank, divisibility and minimum nonzero modulus. As internal checks, \(W(0)=256\) and Parseval gives \(\sum_u W(u)^2=65536\cdot256\). All loop bounds and expected exact totals are in the standalone checkers.

**Two-bit correlations and forced zeros.** Complementation preserves \(\mathcal B_4\), so changing \(b\) to \(b+\mathbf1\) gives \(W(u)=(-1)^{\operatorname{wt}(u)}W(u)\). Thus all odd-weight frequencies vanish. Every de Bruijn word contains every four-bit block once, forcing zero signed pair sums for cyclic separations at most three. The direct character sums at the remaining distances, independently checked across every position pair, give the displayed five nonzero values and show there are no other weight-two zeros.

**Sharp endpoint projection norm.** Fourier diagonalization makes \(R\) the span of characters with \(W(u)\ne0\). Its canonical translation-invariant projection is the Fourier multiplier \(1_{\{W\ne0\}}\), with kernel
\[
p(x)=\frac1{65536}\sum_{u:W(u)\ne0}(-1)^{u\cdot x}.
\]
A second exact Walsh transform of the Boolean support mask yields \(\sum_{x\in G}65536|p(x)|=2520272\). Hence \(\|p\|_{\ell^1}=2520272/65536=157517/4096\), equal to the \(\ell^1\) and \(\ell^\infty\) operator norms of this convolution projection. For an arbitrary real or complex linear projection onto \(R\), average its conjugates under all translations of \(G\). The average is again a projection onto \(R\), with no larger endpoint norm, and must equal the unique translation-invariant Fourier projection just described. This proves the claimed minimum among unrestricted projections.

## Verification

Both `check_debruijn4.cpp` (C++17) and `verify_debruijn4.py` (Python 3, standard library only) rebuild the complete input and prove the stated finite counts with exact integers. Compile and run the former using `g++ -std=c++17 -O2 check_debruijn4.cpp -o check && ./check`, and run the latter using `python3 verify_debruijn4.py`. The C++ program independently constructs the codebook by all-word testing and feedback-state cycles, then compares an exact fast Walsh transform with direct signed sums at every frequency. The Python program separately rebuilds the indicator and spectra using its own loops and checks the full histogram and projection kernel. The auxiliary `spectrum.csv` records the complete twelve-level histogram, not a substitute for rebuilding it.

The replayed checks returned `DEBRUIJN4_FOURIER_PASS` and `DEBRUIJN4_PY_PASS`. Both programs verify the rank, all 12 signed levels, exact gap, complete two-point law, and projection numerator. No floating-point calculation is required for any stated result.

## Relationship to prior work

Spinsante, Andrenacci and Gambi (2011) investigate individual periodic autocorrelations, cross-correlations, and spreading-code performance of binary de Bruijn sequences, including an exhaustive population of order-five cycles. Their full publicly accessible article covers classical local-lag cancellations and codebook motivation, but does not calculate the Boolean Fourier transform of the indicator of the entire *rooted order-four word-space codebook* or its sharp unrestricted range-projection norm. Sawada, Williams and Wong (2015 preprint, 2016 journal publication) provide an efficient construction of individual de Bruijn sequences and classical cycle counts, not this Fourier spectrum.

A published mathematical record on order-four universal partial words includes a complete list of their \(256\) ordinary linear unfoldings among other partial words. Their count and underlying codeword enumeration are acknowledged as prior knowledge, not claimed here. That record's assertion is a joint word-length/wildcard enumerator, rather than the word-space signed Fourier distribution, multiplier-zero geometry, or minimum projection norm evaluated here. Another published record on order-five de Bruijn cyclic phase retrieval concerns the cyclic time-Fourier magnitudes of **individual** cycles and their autocorrelation fibers. It does not imply this order-four ensemble's Boolean Fourier support.

## Limitations

The numerical classification is complete for order four only. It does not imply analogous ranks or divisibility for higher orders. The known local-window orthogonality and the cardinality \(256\) are not new contributions. The entire proof of the finite signed histogram and projection numerator depends on the transparent exhaustive integer algorithms; there is no claimed compact symbolic evaluation of every Walsh coefficient. Previously unindexed tabulations or unpublished computations of exactly this codebook's Boolean spectrum remain a historical-priority risk. No independent external mathematical validation is asserted.

## References

1. S. Spinsante, S. Andrenacci and E. Gambi, *Binary De Bruijn sequences for DS-CDMA systems: analysis and results*, EURASIP Journal on Wireless Communications and Networking (2011), article 4, first public 2011-06-06, DOI:10.1186/1687-1499-2011-4. https://link.springer.com/article/10.1186/1687-1499-2011-4
2. J. Sawada, A. Williams and D. Wong, *A surprisingly simple de Bruijn sequence construction*, author manuscript dated 2015-08-12; Discrete Mathematics 339 (2016), 127–131, DOI:10.1016/j.disc.2015.08.002. https://www.researchgate.net/publication/281580620_A_surprisingly_simple_de_Bruijn_sequence_construction
3. *Complete binary order-four universal partial-word enumerator* (published mathematical record, 2026): exact classification of linear partial words, including 256 ordinary order-four de Bruijn unfoldings.
4. *Almost-complete cyclic phase retrieval for binary order-five de Bruijn cycles* (published mathematical record, 2026): individual-cycle cyclic autocorrelation classification at order five.
