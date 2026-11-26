# Independent mathematical audit

## correctness

PASS

For the iid product-uniform null and nonzero integer frequencies, write D=n^-1 a^T H b with H the sample-centering projection. E|D|^2=tr(H)/n^2. Haar balance for each coordinate has only the within-mode pairing and, when frequencies agree up to sign, a crossed pairing with the all-equal overlap removed. Indeed, a singleton index cannot balance, so only a 2+2 split or all four indices equal is possible, even for harmonically related frequencies. A single crossing contracts to the off-diagonal square sum of H^2, (n-1)/n, before division by n^4. For the two double crossings let B=sum_ij H_ij^4; inclusion-exclusion gives respectively (n-1)^2-2(n-1)^2/n+B and (n-1)-2(n-1)^2/n+B, using tr(H^4)=n-1. These produce all four displayed covariance cases. There are PQ unordered reverse-sign pairs and 2PQ(P+Q-2) unordered pairs sharing exactly one absolute frequency, which gives the rectangular formula. If (P+Q)/n^2 tends to c, the variance/mean ratio tends to 1+2c. At n=2 the final two cases coincide; the introductory phrase 'four values' should be read as four cases, as explicitly qualified in the scope. Replay: python3 /workspace/independent_checks.py 3 (seventh-root quadrature with numerical complex evaluation for n=2,3,4); the source checker was read, not executed.

## originality

PASS

The factorization discrepancy and weighted circular-independence framework are known. The distinct claim is the finite-null squared-energy covariance law under product Haar, including the opposite-sign split, and its exact growing-rectangle consequence. The nearest univariate Resultary moment formulas and the broader weighted-norm frameworks do not compute those cross-coordinate contractions. No equivalent result was established by the bounded searches; this is not a historical priority claim.

## value

PASS

The complete signed-pair covariance table provides an exact input to the variance of arbitrary finite weighted harmonic sums under a natural null and explains when independence-style fixed-grid variance estimates miss a macroscopic contribution. It identifies a dependence mechanism due to marginal frequency sharing, not merely a larger-grid numerical correction. No null distribution approximation or level guarantee is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
