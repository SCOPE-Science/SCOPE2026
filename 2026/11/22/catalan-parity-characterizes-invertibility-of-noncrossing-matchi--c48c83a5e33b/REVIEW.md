# Self-review

## Correctness — PASS
The claim fixes all quantifiers \(n\ge1\), the Boolean chord group and unnormalized Walsh convention. The all-size proof uses the Catalan reflection parity recurrence, an odd-sign nonvanishing argument, a zero pairing for even orders, and a central-chord square factorization for odd orders. The recursive witness terminates precisely outside the Mersenne indices. The standalone exact checker tests the constructed frequencies up to order 30 and exhaustively tests the entire small Walsh spectrum through order four; these finite checks supplement, rather than replace, the proof.

## Originality — PASS under bounded comparison
The closest full inspected source, *Integral Fourier identifiability from noncrossing perfect matchings*, concerns a first-degree centered covariance Gram matrix with rank \((n-1)^2\), not full-group convolution. Asinowski provides Catalan enumeration; Lin gives Catalan parity; neither supplies an explicit balanced chord frequency for every even-Catalan order. General finite-group Fourier results and unrestricted perfect-matching spectra have different claims. Searches tested aliases, signed chord matching sums, global invertibility and Mersenne parity. Priority remains provisional because a historical Temperley–Lieb signed link-pattern formula might be equivalent under an unpublished or unindexed transformation.

## Value — PASS
This is a complete all-order invertibility classification for a canonical Catalan family under its natural binary edge-incidence embedding. It distinguishes guaranteed recovery from explicit information loss and proves a nontrivial converse to the parity obstruction; even support size by itself does not generally force a Fourier zero. The constructive frequency witnesses and recursive proof provide reusable tools for related planar matching ensembles.

## Scope and risks
No full rank formula at singular orders, quantitative conditioning or generalization to arbitrary planar point configurations is claimed. The literature comparison is bounded, and independent mathematical auditing remains outstanding.

Self-review: passed. Independent audit: not yet performed.
