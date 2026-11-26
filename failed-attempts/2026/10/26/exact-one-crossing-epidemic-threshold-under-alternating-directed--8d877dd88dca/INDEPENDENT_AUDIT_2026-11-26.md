# Independent mathematical audit

## correctness

PASS

The unattenuated monodromy is X^T X for X=exp(τ B), B=[[0,p],[q,0]], with determinant one. Using B²=pq I gives trace 2+4κ²sinh²(aτ); dividing the leading log multiplier by the full period 2τ gives the proposed exponent. H(u)=asinh(κ sinh u) has H''(u)=κ(1−κ²)sinh(u)/(1+κ²sinh²(u))^(3/2), so H(u)/u is strictly decreasing for κ>1. Its distinct endpoint limits give the strict finite-duration sign cases, including equalities at the limiting recovery rates; equal rates instead give a constant exponent. The small-u cubic coefficient is −κ(κ²−1)/6, and H(u)=u+log κ+O(exp(−2u)), giving both claimed root asymptotics at fixed unequal rates. An independent direct matrix-product calculation and bisection reproduced the worked example to floating-point rounding; it did not rerun the source script or independently exhaust its test suite.

## originality

FAIL

A distinct Resultary record covers the exact exponent, strict decrease, entire crossing/sign classification and upper-edge law under a simple reparameterization. Its explicit long-period correction immediately gives the lower-edge law as well. This is demonstrated equivalent coverage, not a claim about which of the two same-UTC-date records appeared first.

## value

FAIL

The sharp matched-transpose stability classification would be useful as a new exact result. In this frozen submission it has no substantive increment over the distinct indexed theorem: changing full period to half-period and inverting its already explicit endpoint expansion leaves no new mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
