---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Farhi–Kane gives omission of the full p-power p^a in L_k exactly when v_p(k+1)≥a=floor(log_p k), with at most one omitted prime. For N=k+1 this gives N=mp^a with 2≤m≤p: k≥p^a excludes m=1, and k<p^(a+1) gives m≤p. Conversely these inequalities ensure the exact defect exponent. For a=1 the prime p≥m is the unique largest prime factor at least sqrt(N), including equality for squares. For each a≥2, split the higher-power count at B=Y^(1/(a+1)); summing p below B and Y/p^a above B over all integers gives O(B²) with a uniform constant for a≥2 by the integral tail. Summing exponents gives O(Y^(2/3) log Y), negligible against Y/log²Y. The reindexing Y=X+1 changes the centered count by O(1); p dividing fixed q contributes only finitely many exponent-one pairs. The cofactor weight w_q has O(q) partial sums, so the lower endpoint subtraction π(m-1) costs O_q(sqrt(X)). The effective prime number theorem works uniformly for X/m≥sqrt(X); summing individual errors costs at most a logarithmic factor before the exponential saving. Li(t)-t/log t has derivative 1/log²t, and Abel summation bounds its weighted contribution by O_q(X/log²X). For the last Taylor remainder, write u=log m and L=log X: the logarithmic derivative of u exp(-u)/(L-u) is 1/u-1+1/(L-u), nonincreasing for u≤L/2. Thus this factor has supremum and variation O(1/L), giving the required second Abel bound. The centered harmonic tail converges by bounded partial sums. Möbius inclusion–exclusion gives the local logarithmic divisor sum; subtracting w_q(1) is essential because primes are not defects. This yields C_2=(log 2-1)/2<0 and C_3=(log 3-1)/3>0. The unweighted leading integral between m=2 and sqrt(X) is log 2+O(1/log X), and the total effect of the π(m-1) terms there is O(X/log X). Independently, cyclically comparing quotient samples modulo L_k gave the predicted least periods for k=1 through 8; a separate smallest-prime-factor sieve applying the pointwise formula to k≤300000 gave 195365 defects, split 193988 and 1377, and normalized centered counts -0.175111 and +0.035803 for q=2,3 at that bound. Replay by direct quotient evaluation over a full period for the small cases and factorization of k+1 for the larger diagnostic. The frozen verify.py was inspected, not executed. Neither finite check proves the asymptotic. The theorem fixes q in advance.

## originality

PASS

The fixed-window period criterion and the leading largest-prime-factor density are prior. Moreover the classical uniform smooth-number expansion gives the fixed-cutoff coprimality coefficient by inclusion–exclusion; that analytic coefficient in isolation is not a new smooth-number phenomenon. What remains is the arithmetic reduction linking the actual least-period defect at its moving cutoff to that coefficient at the stated error scale, excluding the prime layer and controlling higher omitted powers. This produces an explicit sign-changing second-order law for the original period statistic. The bounded comparison did not establish earlier coverage of this reduction or frequency law. It is not publication-priority clearance.

## value

PASS

A fixed-k exact period formula does not quantify how frequently its full period fails over k, or how coprimality affects that frequency. The leading share hides a signed correction which changes direction even for the two smallest prime moduli. The prime exclusion and suppression of higher omitted powers explain that phenomenon and give a usable second-order benchmark for this natural period statistic. The significance is the centered period law, not a new general smooth-number asymptotic or the finite sieve data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
