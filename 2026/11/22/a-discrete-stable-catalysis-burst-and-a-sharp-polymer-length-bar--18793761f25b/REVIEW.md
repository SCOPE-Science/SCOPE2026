# Scientific review

## Correctness — PASS

The count of distinct ordered ligations is \(R_\ell=\sum_{j=2}^\ell(j-1)\kappa^j\). Given one Pareto molecular weight, each of these distinct reactions is catalyzed independently with probability \(1-e^{-\lambda_nW/N_n}\), giving the exact binomial generating function. The change of variables and integrable bound \(\min\{1,v\}v^{-\alpha-1}\), for \(0<\alpha<1\), justify the integral limit without substituting numerical evidence for an infinite proof. Independence between molecules yields both the marked compound Poisson limit and Poisson active-catalyst law. Direct asymptotic expansion of \(N_\ell\) and \(R_\ell\) identifies the linear fraction, logarithmic shift and lattice correction. A short RAF necessarily contains a short catalytic incidence; the cited full-network existence theorem supplies nonvacuity. The standard-library checker confirms the exact finite example and algebraic reductions but is not an infinite certificate.

## Originality — PASS, with residual priority risk

Compared directly with Kim and Sönmez (2026), their Theorem 8 determines full-network RAF existence, Theorem 5 treats the single-molecule degree tail in another normalization, and Proposition 10 establishes a supercatalyst regime. None is equivalent to the short-reaction/short-molecule compound Poisson count, its sharp logarithmically shifted length window, and the resulting lower bound for every RAF's maximum molecular length. Hordijk and Steel (2016) cover different variable-rate allocations and RAF sizes; Steel, Hordijk and Smith (2012) give minimum RAF reaction-count bounds, not this length cutoff; and the 2019 diversity study varies the ambient maximum polymer length under constant catalysis. All are pertinent but do not directly dominate the final statement.

Standard Sibuya laws and Poisson rare-event limits are prior mathematics. Possible unindexed regular-variation and RAF-length equivalences are explicitly acknowledged; no novelty is claimed solely from an unsuccessful database search.

## Value — PASS

The recent weighted-catalysis research poses the problem of whether a small number of catalysts can sustain RAFs. This theorem answers a separate structural question: at what molecular scale catalytic links first exist, how many unusually productive short catalysts appear there, and why a globally supercritical RAF still cannot be entirely made of too-short molecules. The exact logarithmic term and nondegenerate marked critical law differentiate finite-window behavior from a coarse linear bound. It provides a mathematical benchmark for numerical RAF-length sampling, without claiming the necessary condition suffices or predicting real chemical emergence.

## Risks and limits

The statement relies on forward-only ligations, independent weights, a diffuse kernel and \(0<\alpha<1\). Lattice cutoff offsets can prevent convergence to one fixed critical distribution. Other unindexed material could contain the same reduction; independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
