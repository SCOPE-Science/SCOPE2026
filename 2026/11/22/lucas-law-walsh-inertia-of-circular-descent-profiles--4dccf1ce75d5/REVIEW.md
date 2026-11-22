# Review of the Lucas-law Walsh inertia theorem

## Correctness — PASS
The claimed domain is every integer \(n\ge3\). Disjoint local comparison blocks yield independent relative orderings, with the precise Eulerian normalization. The full comparison circle is handled separately by a rotational cyclic Eulerian identity. The nonzero character set equals vertex sets covered by matchings of \(C_n\), and the two-to-one full-covering case gives the parity correction. The matching-polynomial evaluation at \(-1\) gives the exact positive/negative imbalance. The proof covers all order and sign cases; 2081 exact checks in `verification.py` independently replay the formula for orders 3–9.

## Originality — PASS within bounded literature inspection
Foata–Schützenberger's signed Eulerian identity and Petersen's circular Eulerian polynomial are classical inputs and not claimed new. The closest indexed linear-descent Fourier result has Fibonacci rather than cyclic Lucas support and does not include the closed circular character or duplicated perfect-matching fiber. Chang–Ma–Yeh use descent values, Elizalde uses permutations that are single cycles with ordinary descents, and the checked cyclic peak–valley study is only second-order. The inspected sources do not directly establish the claimed complete cyclic Boolean-convolution inertia. Earlier unindexed equivalent formulas remain possible.

## Value — PASS
This is an exact natural infinite-family spectral classification, not a finite-only coincidence: it identifies all non-recoverable Fourier modes and computes every sign multiplicity. The six-periodic inertia imbalance and the even-cycle perfect-matching correction quantify the boundary effect of circularising the descent statistic. The exponential recoverable fraction is a usable measure of signal loss.

## Closest literature and limitations
Foata–Schützenberger (2005 arXiv edition of 1970 monograph), Petersen (2006 dissertation, Chapter 1 §1.5), Chang–Ma–Yeh (2008 arXiv), and Elizalde (2009 arXiv) were compared with precise distinction of statistics and implications. The proof does not determine the smallest nonzero singular value or endpoint projector norm. Literature priority remains bounded; an independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
