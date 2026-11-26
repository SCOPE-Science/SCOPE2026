# Independent mathematical audit

## correctness

PASS

Branch averaging gives the stated three-moment lift and determinant cubic. The positive-map argument is needed because the moment matrix in entry coordinates has negative entries: for a rank-one input with both coordinates nonzero the two images are independent, whereas an input on either axis first reaches a spanning case within three steps. Positive definiteness then persists because the delivered matrix is invertible. Primitivity gives a simple dominant eigenvalue and strictly positive left and right eigenmatrices; a deterministic nonzero initialization has positive projection and the first square moment observes it. For h small the simple leading root is 1−2ph+O(h²). For h>h_c, F_p(1,h)<0 guarantees a real root greater than one, and there is no other positive h below h_c where the rate could equal one. Continuity forces Λ=1 at h_c, where the square moment tends to a positive constant for each nonzero initialization; the phrase instability at the boundary means failure of asymptotic decay, not divergence. F_p(1/4,h)<0 similarly forces Λ>1/4. At h≤1/4, F_h/p at r=Λ exceeds 3(1−p)/16, so the rate strictly decreases there. The exact stationary resultant is 4h³p²Q_p(h); strict concavity and the signs at 0, 1/4 and h_c isolate one candidate in (1/4,h_c). The rate derivative is positive at h_c because F_h(1,h_c)=p(h_c−4)<0 and F_r>0 at the simple leading root. Thus there is exactly one minimizer and gains outside the stable interval cannot match it. Both Q_h and Q_p (partial in p) are negative on the selected root, giving strict decrease of the optimal gain with p. At p=0 the only limiting Q-root in [1/4,2] is 1, a simple root, and at p=1 Q becomes −16(h−1/4)^2. Substitution yields h_*=1−2p+5p²+O(p³) and Λ_*=1−p+p²+O(p³). Applying the strictly positive left Perron functional to the erasure-only fixed direction (1,1)(1,1)ᵀ and its nonzero delivered image gives Λ>1−p, the exact best fresh-erasure rate. The frozen verify.py and VERIFICATION.md were inspected, not executed; the independent symbolic check confirms the resultant and signs and independently reproduces the p=1/2 rates, while finite spectral minimization is not the quantified proof. The frozen enumeration loops over 135 initialization/gain/probability/path-length combinations and asserts the top moment in each; the printed 405 count should not be interpreted as 405 separate moment assertions.

## originality

PASS

The supported contribution is the global mean-square rate optimizer for the precise erased-or-one-step-stale scalar rule, with its reliability dependence and attainable rate gap. The stability boundary formula, covariance lifting as a method, and optimal no-delay Bernoulli rate are prior or elementary baselines, not novelty claims. Same-boundary, fresh-or-stale and other dropout models do not share the objective as a function of gain.

## value

PASS

A stability ceiling does not answer how aggressively to tune the gain. This exact unique optimum, including its strict movement as delivery improves and its separation from the best fresh-packet rate, gives a concrete scalar benchmark for delay-and-erasure algorithms. The result is a complete natural optimization problem in the stipulated rate metric rather than a finite grid or reuse of the known ceiling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
