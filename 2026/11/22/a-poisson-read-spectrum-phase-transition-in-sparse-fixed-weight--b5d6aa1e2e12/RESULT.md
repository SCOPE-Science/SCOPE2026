# A Poisson read-spectrum phase transition in sparse fixed-weight binary strings

## Finding

Let \(k\ge2\) be fixed. Let \(W_n\) be uniform among binary words of length \(n\) containing exactly \(r_n\) ones, where \(r_n/\sqrt n\to c\) for a fixed \(0<c<\infty\). The *complete contiguous read histogram* \(H_{n,k}\) records, for every binary \(k\)-mer \(u\), the number \(H_u(W_n)\) of its overlapping occurrences.

Write the positions of the ones as \(p_1<\cdots<p_{r_n}\), and for \(1\le d<k\) let \(X_d\) count consecutive one-pairs of separation exactly \(d\):
\[
X_d=\#\{i:1\le i<r_n,\ p_{i+1}-p_i=d\}.
\]
Then:

1. The vector \((X_1,\ldots,X_{k-1})\) converges in total variation to a vector of \(k-1\) **independent Poisson variables of mean \(c^2\)**.
2. With probability tending to one, the entire histogram is the following *injective affine function* of this vector. All \(k\)-mers with at least three ones have count zero. For \(1\le d<k\) and \(0\le j<k-d\),
\[
H_{0^j1 0^{d-1}1 0^{k-d-1-j}}=X_d.
\]
For \(0\le j<k\),
\[
H_{0^j1 0^{k-1-j}}
=r_n-\sum_{d=1}^{k-1}\left(\mathbf1_{j\le k-d-1}+\mathbf1_{j\ge d}\right)X_d,
\]
and
\[
H_{0^k}=n-k+1-kr_n+\sum_{d=1}^{k-1}(k-d)X_d.
\]
The two-one coordinates, for instance those with \(j=0\), recover the vector \(X\) exactly.
3. For two independently selected words \(W_n,W'_n\) of the stated length and weight,
\[
\lim_{n\to\infty}\Pr\{H_{n,k}(W_n)=H_{n,k}(W'_n)\}
=\left[e^{-2c^2}I_0(2c^2)\right]^{k-1},
\]
where \(I_0(2z)=\sum_{m\ge0}z^{2m}/(m!)^2\) is the modified Bessel function.
4. Define the *separated reference histogram* by \(H_{0^k}=n-k+1-kr_n\), by \(H_{0^j1 0^{k-1-j}}=r_n\) for every \(j\), and by zero counts for all other \(k\)-mers. Its exact probability, when \(n\ge k\), is
\[
\frac{\binom{n-(r_n+1)(k-1)}{r_n}}{\binom n{r_n}},
\]
using a zero numerator when its upper argument is smaller than \(r_n\). For \(r_n=o(\sqrt n)\) this probability tends to one; in the critical window it tends to \(e^{-(k-1)c^2}\); for \(r_n/\sqrt n\to\infty\) with \(r_n=o(n)\), it tends to zero. Thus the nontrivial read-histogram collision transition occurs at the square-root sparsity scale.

## Assumptions and scope

All words are *indexed, linear, and binary*, and all reads are contiguous overlapping factors. The histogram retains multiplicities, not just the set of distinct factors. No cyclic wrap-around, sequencing errors, or reverse-complement identification is used. The read length \(k\) is fixed as \(n\) grows. The critical-window conclusion requires \(r_n/\sqrt n\to c\in(0,\infty)\); only the separated-reference probability is additionally asserted for subcritical and supercritical sparse weights.

For a short word the formulas for the reference histogram need not define nonnegative entries; the exact numerator convention then gives probability zero. The asymptotic regime guarantees that all relevant counts become valid.

## Proof

**Uniform gap compositions.** Put \(r=r_n\), \(Z=n-r\). The \(r+1\) nonnegative zero gaps (before, between, and after the ones) form a uniformly random weak composition of \(Z\). There are \(\binom nr\) such compositions. Fix \(t\) distinct *internal* gap indices and assign fixed nonnegative lengths \(g_1,\ldots,g_t\). Writing \(s=\sum g_i\), the exact joint probability is
\[
\Pr(G_{i_1}=g_1,\ldots,G_{i_t}=g_t)
=\frac{\binom{n-s-t}{r-t}}{\binom nr}.
\]
For fixed \(t,s\) and \(r/\sqrt n\to c\), this equals \((r/n)^t(1+o(1))\), uniformly over the choices of the indices. Expanding any fixed joint factorial moment of \((X_1,\ldots,X_{k-1})\), the summands involve distinct gap indices and the prescribed values \(G_i=d-1\). If the total factorial order is \(t\), the moment tends to \((r^2/n)^t\to c^{2t}\). These are precisely the joint factorial moments of independent \(\operatorname{Poisson}(c^2)\) variables. Multivariate factorial-moment convergence gives convergence in distribution. On this fixed countable lattice, convergence to a probability measure also implies total-variation convergence by truncation to a sufficiently large finite box.

**No triple clusters and no boundary truncation.** A one within \(k-1\) positions of either endpoint has probability \(O_k(r/n)\). If a \(k\)-window contains three ones, two consecutive internal gaps have total separation at most \(k-1\). For any specified neighboring pair of gaps, the composition formula above makes this probability \(O_k((r/n)^2)\). Summing over \(r-2\) choices gives \(O_k(r^3/n^2)\). Both error probabilities tend to zero in the critical window, establishing a good event of probability \(1-o(1)\).

**Exact histogram on the good event.** Each one belongs to exactly \(k\) windows. Absent close pairs these windows contain it alone, contributing \(r\) to every singleton-pattern coordinate and \(kr\) nonzero windows. An internal consecutive pair at distance \(d<k\) lies jointly in exactly \(k-d\) windows; in the good event no such window has a third one. For every offset \(j\in\{0,\ldots,k-d-1\}\) it contributes one copy of the displayed two-one factor. It replaces one single-one window for the left marker whenever \(j\le k-d-1\), and one for the right marker whenever \(j\ge d\). The offsets can be counted by the two indicators in the singleton formula. Each replaced double-counted window adds one unit to the all-zero coordinate relative to the default count \(n-k+1-kr\), summed as \(k-d\) per close pair. Since no three ones lie in one window, these adjustments are disjoint at window level. This proves every stated coordinate and the injectivity via any fixed offset coordinate of each two-one pair pattern.

**Collision limit.** Two independent random words have independent read histograms. With asymptotic probability one each histogram is the same injective deterministic function of its close-gap vector, with the same \(n,r,k\). Thus equality of histograms and equality of the vectors differ with probability \(o(1)\). By total-variation convergence the limiting equality probability is that of two independent vectors of independent \(\operatorname{Poisson}(c^2)\) coordinates. One coordinate collides with probability
\[
\sum_{m\ge0}\left(e^{-c^2}\frac{c^{2m}}{m!}\right)^2
=e^{-2c^2}I_0(2c^2).
\]
Taking the \((k-1)\)-st power gives the formula.

**Exact separated event and its threshold.** The reference histogram occurs if and only if no window contains two ones and no one loses a boundary window. Indeed the reference histogram has no two-one coordinate, which forbids all pairs at distance below \(k\); its singleton counts are then exactly \(r\) if and only if both outer gaps are at least \(k-1\). Thus all \(r+1\) zero gaps are at least \(k-1\). Removing those compulsory zeros leaves \(n-r-(r+1)(k-1)\) zeros in \(r+1\) gaps, giving \(\binom{n-(r+1)(k-1)}r\) words.

For fixed \(k\) and \(r=o(n)\), the logarithm of this ratio is \(-(k-1)r^2/n+o(1)\) if \(r=O(\sqrt n)\), by the product expansion of binomial coefficients. The limits for subcritical and critical weights follow. In the supercritical sparse case the ratio is at most \(\exp(-\Omega_k(r^2/n))\) when it is nonzero, and otherwise is exactly zero. This proves the sharp transition.

## Verification

The accompanying standard-library program `verify.py` calculates all literal length-\(k\) histograms on 12,365 good-event configurations and compares each with the explicit affine formula. It also compares the exact separated-word binomial coefficient with direct word enumeration in 379 parameter cases. A seeded 15,000-trial finite simulation records near-Poisson means and small off-diagonal covariances at \(n=2500\), \(r=50\), \(k=4\). The exact finite checks supplement the proof; no finite sample is used to establish an asymptotic assertion. Reproduce by running `python3 verify.py` from the folder containing the script.

## Relationship to prior work

Chakraborty, Grossi, Kimura, Punzi, Sadakane, and Zuba (2026) study compact representations preserving the **set** of present \(k\)-mers through graph covers, not the multiplicity vector of random fixed-weight words. En Gad (2026) uses substring-count hashes in deletion-correcting codes but does not present a fixed-read-length sparse profile or its collision distribution. Classical Poisson approximation for occurrences of rare motifs motivates the probabilistic technique, but a marginal occurrence approximation by itself does not identify the full histogram from \(k-1\) gap statistics or yield the stated all-coordinate collision law. Published fixed-small-weight trigram classifications concern a different, noncritical sparsity regime. These comparisons support a distinct claim, not a proof of absolute historical novelty.

## Limitations

The result covers the uniform fixed-weight binary model with \(k\) held constant, and does not establish the same limit for growing read lengths, general alphabets, correlated sources, or noisy reads. Total-variation convergence is proved qualitatively; no explicit finite-\(n\) convergence rate is asserted. The two-sample collision law measures equal *histograms*, not unique recovery of the original word. Search coverage cannot rule out unindexed equivalent results; independent scientific validation remains unperformed.

## References

- S. Chakraborty, R. Grossi, R. Kimura, G. Punzi, K. Sadakane, W. Zuba, *Variations on the Problem of Identifying Spectrum-Preserving String Sets*, arXiv:2602.19408, first posted 2026-02-23, https://arxiv.org/abs/2602.19408.
- E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493, first posted 2026-09-16, https://arxiv.org/abs/2609.19493.
- *Normal and Compound Poisson Approximations for Pattern Occurrences in NGS Reads*, 2012, https://pmc.ncbi.nlm.nih.gov/articles/PMC3375642/ (background on motif-count approximation, not a source for the present theorem).
