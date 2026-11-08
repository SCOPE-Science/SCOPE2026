# Review of the random-threshold two-alternative lottery law

## Correctness (PASS)
The cutpoint-order reduction gives the exact identity \(V_n=U_n-M_n\), and a first-hitting reflection bijection proves the finite binomial-count formula. For biased directions the overshoot is a tight maximum of a negative-drift walk, while at balance Donsker's principle gives the Brownian maximum; a triangular-array drift argument gives the \(n^{-1/2}\) window. The included independent enumeration over all 131070 sign words through length 16 matched 932 reflection counts and 140 exact rational upper-tail checks. The analytic proof supplies the infinite conclusions; the verifier alone does not.

## Originality (PASS, qualified)
The closest source, Teh and Goldberg (arXiv:2610.37828v1, Appendix E.1), proves a profilewise interval-sweep algorithm, not the random-threshold optimal-rejection distribution or its Brownian transition. Choo–Goldberg–Teh (arXiv:2604.17505v1) develops unanimity query algorithms without a corresponding distribution law. A related earlier threshold-lottery analysis of worst-case unqueried-agent regret uses an adversarial threshold grid rather than this i.i.d. stochastic model. Classical random-walk reflection/hitting/functional limit principles are acknowledged, not claimed as new. An unindexed application of those classical principles to random interval-overlap optimization remains possible.

## Value (PASS)
The motivating optimization model explicitly reports empirical behavior on random data, while this natural two-alternative instance supplies an exact distribution-free benchmark for optimal stakeholder rejection, including when unanimity is exponentially unlikely. The fixed-bias Gaussian and critical Brownian regimes distinguish quantitatively between polarized and balanced populations; the full finite law supports benchmark calibration for every number of stakeholders, not an arbitrarily selected numeric sample.

## Scope and risks
Requires independent stakeholder directions, one common atomless distribution of effective cutpoints, and two alternatives. No assurance of independent scientific validation or generalization beyond these hypotheses.

Self-review: passed. Independent audit: not yet performed.
