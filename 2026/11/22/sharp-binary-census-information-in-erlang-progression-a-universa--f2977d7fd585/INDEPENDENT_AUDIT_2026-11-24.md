# Independent mathematical audit

## correctness

PASS

For the stated synchronous Poisson cohort, thinning produces independent means theta P and theta Q, with opposite rate derivatives theta x f and -theta x f. The two log-parameter scores are orthogonal; the information is diagonal with entries theta and theta J. The exact completion-time rate score is k-X, of variance k. For fixed-design binary labels, conditioning this score identifies the rate information with Var(E[X|label]) per individual. Thus its maximization minimizes squared distortion, and any positive-information partition that is not a nearest-centroid threshold a.e. is strictly improvable because the density has no atoms. For a threshold, integration by parts gives conditional centroids k-x f/P and k+x f/Q. Differentiating the between-cell variance gives f(b-a)(R-L) with L=x-a and R=b-x. Concavity of log f implies decreasing reverse hazard f/P and increasing hazard f/Q, via the integrals of f(x-u)/f(x) and f(x+u)/f(x). The integrated ratios for L and R then give strictly increasing L and nonincreasing R, including k=1 with R=1. At zero L tends to 0 and R to k; at infinity L diverges and R tends to 1 by the Erlang survival polynomial. This yields one crossing and the displayed equation. L-R is increasing, not decreasing as stated once in §4; the root trap uses the correct direction. For the center expansion, the Stirling log-density expansion is uniform on |z|<=sqrt(12 log k) with integrable remainder O(phi(z)(1+|z|^6)/k) after subtracting the first skew term, and a left-tail Chernoff bound beyond that window is at most exp(-z^2/2) at its boundary. Integrating (z^3-3z)phi(z)/3 to zero yields phi(0)/3. Consequently for bounded c the CDF shift is (c+1/3)/sqrt(2 pi k)+O(k^-1). This gives L-R=2c-(4/pi)(c+1/3)+o(1), so testing any two fixed c around its zero rigorously localizes the root. Stirling at k+c gives the information correction H(c)=(2/pi)(c+1/3)^2-c^2-1/6; evaluation at the limiting offset yields the claimed positive coefficient. Independently ran python3 /workspace/review_evidence/recompute1.py using regularized Gamma integrals and the log derivative: at k=3 it gave x=3.5880844503693362570577 and J/k=0.641578310051128967688686; at k=5000 the offset and scaled correction were 0.583982273114358 and 0.02798996435343915, consistent with limits 0.5839794646280362 and 0.0279931548760121. These checks are diagnostic; the argument covers all integer stages under local design with a nominal rate.

## originality

PASS

Best of current knowledge the distinct contribution is the sharp large-shape absolute offset and the first information-retention correction for the one-threshold Erlang scale experiment. Nearest-centroid optimality, its threshold equation after evaluating Gamma centroids, and uniqueness from general log-concave quantization are covered by the older framework and are not credited as distinct. The leading 2/pi factor is the normal limiting two-level factor, not by itself the novelty.

## value

PASS

The exact one-bit information loss for incomplete measurement of progression is naturally motivated, and the sharp offset answers a practical and mathematical question not resolved by the normal limit: follow-up is shifted by a constant fraction of one mean stage past the cohort mean. The explicit positive 1/k correction quantifies the approach to the Gaussian retention factor at the optimum. These joint expansions add nontrivial information beyond the covered general optimal-partition result, without claiming field robustness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
