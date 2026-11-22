# Scientific review of the orientation-weighted spectral law

## Correctness (C): PASS
The central identity is an exact rank-three factorization of the branch-weighted adjacency matrix, verified directly with the published canonical Markov formula. The resulting cubic's coefficients were derived independently and exhaustively checked against full characteristic polynomials for all words of 3 through 9 branches. The probabilistic argument only invokes the classical central limit theorem for the independent interior signs, the law of large numbers for bounded one-dependent switch counts, and continuity of the spectral-radius map on roots of fixed-degree monic polynomials. The three endpoint cases and their discriminants give the claimed atom. Finite tests do not certify the infinite limit and are clearly marked supportive.

## Originality (O): PASS, with historical-priority risk
Oliveira's initial paper already defines the signed operator and illustrates two individual weighted-trace calculations; neither this nor its unsigned cubic gives the random-word spectral distribution. Closest full published comparisons include the all-orientation **unsigned** Parry mixing bound and the fixed-map **physical switching** statistics. A related exact unsigned entropy multiset and Gaussian defect does not imply this signed spectrum: multiplying by the branch-orientation matrix changes the leading spectral order from \(n\) to \(\sqrt n\), introduces a complex-conjugate root regime and a positive probability atom. General weighted kneading theory supplies the context, not an evident equivalent asymptotic law. Unindexed signed random transfer-matrix calculations could still dominate or duplicate this result, and human priority review is appropriate.

## Value (V): PASS
The problem is forced by a genuine asymptotic distinction between ordinary orbit growth and orientation-cancelled closed Markov paths. Instead of simply reparameterizing an unsigned result, the theorem identifies a sharp non-Gaussian three-regime law and a positive atom determined by conjugate-root coalescence. The exact atom and \(\sqrt n\) scaling quantify information that the unsigned entropy spectrum does not determine. The scope is explicitly confined to this concrete, naturally motivated canonical family.

## Scope and limitations
The limiting distribution is over independently chosen orientation words, not trajectories of a fixed random dynamical system. Signed symbolic trace counts can cancel for a specific period, and the symbolic determinant does not automatically account for boundary-periodic corrections. Rugh–Tan and general random signed operator literature warrant independent follow-up for historical priority.

Self-review: passed. Independent audit: not yet performed.
