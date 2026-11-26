---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The cited Theorem 1.1 and Corollary 4.1 establish the displayed floor-rule strategy for each fixed k and sufficiently large n, with at most the odd middle position an alternative for k>=2. The expected score is the sum of marginal hit probabilities, so the stated tie characterization applies to every deterministic optimum and changes the score by at most one. In the forward a-packet shuffle, each output-origin label word has probability a^-n (multinomial cut times uniform interleaving), and the GSR composition law gives a=2^k. Given the word, the card label equals the preceding packets' total plus the within-packet occurrence rank. Both extreme packets have Bin(n,1/a) sizes; the probability either is too short to contain its half's guesses is O_a(exp(-c_a n)), so discarding outside-packet hits costs at most n times this exceptional-event indicator. Each half's extreme-packet score is a function only of that half's labels, using ranks from the end for the bottom half. The jth success occurs at time T_j with iid geometric gaps; its hit condition is exactly T_j-aj in {-a,...,-1}. For j<=floor(half length/a), every hit lies inside that half, and only the next index can contribute beyond these j, so each truncation costs at most one and is measurable in its own label half. The centered gap walk has span 1 and variance a(a-1); Fourier inversion near 0 and exponential decay away from 0 yield the stated local limit and uniform C/sqrt(m) bound. In the factorial-moment sum, Markov factorization at increasing times gives a product over gaps; cutting out any gap <=epsilon J costs O_r(sqrt(epsilon)) after scaling, by summing the inverse square-root bounds. The remaining Riemann integral in gap coordinates is the stated Dirichlet integral. Lower factorial moments give vanishing repeated-time contributions after scaling the rth ordinary moment, and half-normal moment determinacy gives the claimed one-half law. The disjoint halves are independent and floor(half length/a)/n tends to 1/(2a), giving the scale 1/sqrt(2(a-1)) per half. The bounded and exponentially rare score discrepancies vanish in each scaled L^r, so all moments transfer. The orthogonal rotation identity max(|x+y|,|x-y|)=|x|+|y| yields the equivalent maximum, squared-erf CDF and the stated mean and variance. This is for fixed k, not k growing with n. The frozen checker was inspected, not executed; it provides finite marginal and occupation corroboration rather than proof of the limit.

## originality

PASS

The supported distinct claim is the distribution and all positive integer moments of the total optimal no-feedback score for fixed k>=2. The primary optimal-strategy paper poses exactly this distributional question while giving the leading mean; the known identical-shaped half-normal law is for one shuffle. A related exact first-hit result uses the same packet representation but does not determine repeated hits or the total-score law. No inspected source covers the claimed extension.

## value

PASS

This answers the specific fixed-multishuffle distributional question left by the optimal-strategy theorem. It gives the scale and shape of score fluctuations and asymptotic values of all fixed moments, rather than another expectation calculation. The joint packet reduction explains why two independent limiting contributions appear and why the single-shuffle shape persists after rescaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
