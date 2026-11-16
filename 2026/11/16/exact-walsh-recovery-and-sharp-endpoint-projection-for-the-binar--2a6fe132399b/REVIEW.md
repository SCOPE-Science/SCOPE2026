# Self-review

## Correctness — PASS

The finite set is defined by the complete cyclic-four-window condition on all \(65{,}536\) binary words. A second exhaustive method uses all \(256\) possible reversible feedback tables; exactly \(16\) yield single cycles, and their \(16\) roots agree with the direct set of \(256\). The C++17 checker compares a fast exact Walsh transform with independently summed integer characters at **every** frequency. The Python checker separately recomputes the exact histogram, two-point law and Fourier-support projection kernel. The full signed histogram, Parseval checksum, minimum nonzero modulus, zero count, Fourier rank and projection numerator were reproduced. Fourier diagonalization and averaging over all translations rigorously establish the operator-norm assertions for arbitrary linear projections.

## Originality — PASS under bounded comparison

Searches for de Bruijn word-space Fourier transforms, Walsh codebook indicator ranks, exact numerical nullities and equivalent convolution norms found no published theorem covering the present exact Boolean spectrum. Spinsante–Andrenacci–Gambi (2011, full HTML article inspected) calculate auto/cross-correlation performance of individual sequences; this is a different transform. Sawada–Williams–Wong (2015 manuscript text inspected) construct individual cycles. A relevant published order-four partial-word census already enumerates all \(256\) ordinary unfoldings, and this cardinality is treated as known; the complete Walsh nullspace and optimal Fourier range-projection norm are not statements of that census. A published order-five homometry classification concerns the time-shift Fourier magnitude of each cycle and not the Boolean Fourier transform across codewords. Possible unindexed computational tables of the exact spectrum remain a residual priority risk. Exhaustive checking of all historical literature is not claimed.

## Mathematical value — PASS

Order-four de Bruijn sequences constitute a small, complete, natural codebook with \(16\) cyclic classes; exact correlation and recoverability are motivated by spread-spectrum sequence selection. The finding gives a complete integer spectral benchmark rather than merely reproducing the known codebook count. Its \(9{,}254\) even-weight spectral cancellations are not explained by the elementary complement symmetry. The sharp norm over **unrestricted** range projections measures the best possible stability of Fourier-band recovery; the precise nonlocal two-point law locates the first lags beyond the forced uniform four-window regime. The fact is finite and does not require a conjectured general theorem.

## Limits

No claim about higher de Bruijn orders, no structural classification of every individual zero frequency beyond the complete executable census, and no external independent audit. The historical comparison does not rule out unavailable or unindexed exact tabulations.

Self-review: passed. Independent audit: not yet performed.
