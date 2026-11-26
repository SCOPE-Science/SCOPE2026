# Independent mathematical audit

## correctness

PASS

Under either stated regime nλ→∞, so the Poisson sample mean is relatively consistent by Var(λhat/λ)=1/(nλ), and its all-zero event has probability exp(−nλ)→0. For each fixed k with n p_λ(k)→∞, binomial concentration and p_λhat(k)/p_λ(k)→1 give W_n(k)→1. In the critical regime this handles k<r; at r the binomial count converges to one Z~Poisson(c/r!), while n p_λhat(r)→c/r!, giving the asserted rare-cell ratio. The union bound n P_λ(X≥r+1)=O(nλ^(r+1))→0 makes every later ratio zero simultaneously with high probability. Thus the fixed-weight tail is exactly the sum or weighted supremum in the formulas on that event; no unjustified exchange of an infinite sum and limit is needed. Finite collections share the one rare coordinate by continuous mapping. For either adaptive mass weight the critical cell has O_P(1/n) weight times a tight discrepancy, the empirical tail is identically zero on the same event, and the fitted tail has total weight tending to zero (which also bounds its supremum). At a plateau k=r is concentrated too, including the r=1 plateau. The fixed positive tail bounds the limiting distances away from zero. The e^(−k) example at r=2,c=2 leaves e^(−3)/(1−e^(−1))+e^(−2)|Z−1| for Poisson(1) Z, with minimum about .07876198246 attained when Z=1 (mass e^(−1)). Inspected VERIFICATION.md and verify.py without executing uploaded code: finite histogram and rare-cell checks corroborate but do not establish these limits. The result is for the exact distances defined in RESULT.md, in particular g inside the weighted supremum.

## originality

PASS

The empirical-weight testing construction is credited as prior. The supported distinct claim is the joint shrinking-mean asymptotic law for the explicitly defined infinite-support distances: an exact unseen-tail contribution plus a shared Poisson coordinate at each critical cell, deterministic plateaus between them, and separation of fixed from adaptive weights. Neither the rare-event limit in isolation nor a new version of the test statistic is credited.

## value

PASS

The analysis distinguishes two kinds of behavior for existing goodness-of-fit distances even under a true null: a positive floor and a discrete law from weighting unseen cells versus vanishing distances when mass weights adapt. It explains why changing an apparently secondary weight changes the sparse null limit, and identifies exactly when the floor drops to the next plateau across sample-size scales. This is not a claim of bootstrap size distortion or a result for growing r.

The dated certificate retains the supplied scientific assessment, sources and limitations.
