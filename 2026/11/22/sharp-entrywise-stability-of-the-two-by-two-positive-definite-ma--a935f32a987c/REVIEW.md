# Scientific review

## Correctness

PASS. The positive Lyapunov kernel reduces the symmetric-entrywise derivative norm to a diagonal row-square integral, achieved by a rank-one sign direction. The ordering of semigroup row sums and spectral endpoint monotonicity are explicit. Factoring the scalar objective derivative shows a unique orientation \(\tan\theta=\sqrt2-1\). Convex segment integration proves the two-input upper bound; interior perturbations recover the lower bound. All denominator and boundary restrictions are stated. The standalone checker passed 16,515 supplementary tests, none of which is treated as the proof.

## Originality

PASS under the recorded best-knowledge literature comparison, not a certification of priority. Carlsson (2018) gives the matrix-square-root derivative but not this optimized entrywise spectral-window bound. Higham–Relton (2014), Theorem 5.5, controls *Frobenius*-norm conditioning and cannot imply the lower scalar bound because maximum-entry perturbations can be larger after rotating eigenvectors. Kandolf et al. (2020) and Schweitzer (2022) address general Fréchet approximations and higher-order conditioning. Related published two-by-two semidefinite projection, square-root iteration, and matrix-inversion stability results concern different maps or different perturbation questions. An obscure equivalent explicit inequality remains possible; exact-priority claims should receive an independent systematic literature review.

## Mathematical value

PASS. This is the complete natural two-by-two, two-ended eigenvalue-window sensitivity law for a canonical functional calculus. The universal \(\pi/8\) extremizer and sharp high-contrast factor \((3+2\sqrt2)/4\) quantify a genuine loss invisible in scalar and Frobenius conditioning. This provides a precise small-matrix robustness benchmark and a nontrivial boundary example for broader componentwise perturbation theory. Its dimensional restriction is explicit rather than presented as an arbitrary slice or a higher-dimensional theorem.

## Closest literature and limitations

Carlsson, arXiv:1810.01464 (reviewed relevant sections of full text); Higham–Relton, DOI:10.1137/130945259 (reviewed full-text condition number theorem in PDF); Kandolf et al., arXiv:2008.12926; Schweitzer, arXiv:2203.03930. The result is for real symmetric matrices and the absolute-entry maximum norm. An earlier equivalent derivation in a different conditioning language remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
