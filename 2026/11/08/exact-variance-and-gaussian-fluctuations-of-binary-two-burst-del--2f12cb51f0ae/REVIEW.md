# Independent mathematical audit

## correctness

PASS

For independent uniform source X in {0,1}^n, n>=4, deleting two disjoint length-two bursts and counting DISTINCT length-n-4 outputs, delay-two changes T_i=1_{X_i != X_{i+2}} are independent fair Bernoulli. The proof specializes the published canonical burst-deletion normal form to a pointwise exact quadratic count. Expanding in centered Z_i=T_i-1/2 gives linear coefficients (m-2)/2 at endpoints and (m-3)/2 internally, and quadratic weights -1 at distance two, +1 at >=3. Orthogonality yields E B_n=(n^2-3n+4)/8 and Var B_n=(n-4)(2n^2-15n+31)/32. The quadratic remainder has variance O(n²), while the linear independent-sum term is asymptotically n^{3/2}/4 times a standard normal; CLT and Slutsky prove the Gaussian limit. n=4 yields constant 1. Independent direct enumeration of all 2040 binary source words of length 4 through 10 constructed UNIQUE deletion outputs, matched the pointwise canonical polynomial and exactly matched the mean/variance at each length. The all-n canonical lemma belongs to Wang et al.; finite cases do not prove that lemma.

## originality

PASS

Wang–Kong–Yaakobi–Duman 2026 establish arbitrary-source multiple-burst canonical histories; Lan–Sun–Yu–Ge 2025 establish maximal sphere cardinalities, neither accessible indexed text states a random-center variance or Gaussian limit. Resultary October 2026 exact binary two-DELETION sphere variance is a distinct channel deleting two individual bits, not two disjoint double-bursts. The source normal form is prior work and not claimed new. Wang full primary text was not retrieved, so confidence in exact prior scope and lemma wording remains qualified; still best-of-knowledge neither variance nor Gaussian limit is shown to be prior.

## value

PASS

Distinct-output burst-deletion ball size controls ambiguity of a natural burst channel; worst-case cardinality alone omits dispersion of typical random source words. An exact finite-length second moment plus sharp Gaussian n^{3/2}-scale fluctuations provides an independently useful random-source characterization across every n>=4 and a principled asymptotic normal approximation, beyond merely repeating normal-form combinatorics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
