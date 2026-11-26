# Independent mathematical audit

## correctness

PASS

The identity-started node is mu=(N^3+3N)/(N^3+2); the tangent remainder is (x-mu)^2/(mu^2 x). The only random coordinate pair for sign probes has coefficient 1/(4N) in the inverse and (1-2N^2/mu^2)/(4N) in the remainder. This verifies the centered samplewise identity for shared probes, baseline variance 1/(4sN^2), strict inflation for N>=2, and ratio asymptotic 4N^4. The eigenvalue remainders at 1,N,2N are O(N^-4), asymptotic to N, and asymptotic to 2N, respectively. With multiplicities N^3,1,1 this gives squared remainder norm asymptotic to 5N^2, inverse squared norm asymptotic to N^3, and Gaussian variance ratio asymptotic to 5/N. Direct trace subtraction verifies relative discrepancy asymptotic to 3/N^2. For two eigenvalues a<b the projector decomposition gives exact sign ratio (1-ab/mu^2)^2, bounded by (b/a-1)^2 when the denominator variance is positive. Frozen RESULT.md lines 44–84 is an algebraic replay; supplied verify.py was inspected, not executed. 'Vanishing Frobenius residual' is only relative to the inverse norm; the absolute remainder norm grows. Exact actions are assumed.

## originality

PASS

Credit the existing estimator, variance formulas, the warning for spectral deflation and the two-spectrum formula. The distinct finding is an exact three-spectrum one-node inverse family with quartic sign-variance inflation and a simultaneously vanishing Gaussian ratio and relative deterministic bias. The inspected strongest comparisons do not establish this joint separation.

## value

PASS

The example isolates why relative Frobenius or deterministic trace accuracy is not a sufficient diagnostic for sign-probe improvement, while directly checking that Gaussian variance does improve against its own baseline. The quadratic two-level ceiling makes the quartic three-level effect structurally meaningful. No claim about equal cost, absolute Gaussian versus sign variance, or finite-tolerance actions follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
