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

The decisive cylinder identity can be recovered without relying on inaccessible literature. The first pass emits one digit for each input one, marking its original position parity (odd maps to 0, even to 1). The second pass therefore emits one digit for each even-position input one, and that digit is determined by the parity of the rank of the one among all original ones. Condition on any fixed even-length prefix w and then on all even-position bits of the independent fair suffix. Between successive even-position ones of the suffix, and before the first, there is at least one independent fair odd-position bit, with disjoint odd-bit blocks. The odd-bit parities are independent and fair, so the successive rank parities, which are their cumulative parities plus known offsets, are themselves independent and fair. Thus the output has prefix rho^2(w) followed by a fair suffix almost surely, verifying the exact pushforward weight 2^(|rho^2(w)|-|w|), including the empty word and Lebesgue invariance. No exceptional dyadic representation affects this proof. Since |rho^2(w)| counts even-position ones, dyadic resolution falls to ceil(m/2); odd input depth is handled by embedding in the next even depth. Evaluating the four two-bit inputs gives P1=1 and Pr=r/2. On V_m for m>=1 the quotient by V_1 is nilpotent, giving the two simple nonzero modes and no other nonzero eigenvalue. For L-Lipschitz phi, E_(2^n) has L1 error at most L*2^(-2^n), and its nth transfer is the mean plus a_n*r. Contraction of P and Pr=r/2 give |2^(n+1)a_(n+1)-2^n a_n|<=L*2^(n+2-2^n). Summing from n (successive ratios at most 1/2, with strict inequality later) and adding the dyadic error gives 9L*2^(-2^n); stationarity and transfer duality give the covariance statement. Independent exact word-image enumeration recomputed c1=1/4, c2=9/32, c3=1181/4096, c4=38745189/134217728: initialize cell values (2j+1)/2^(2^n+1), push with the cylinder weight on each output prefix, and take 2^n times half the last two cells' difference. At n=4 the tail bound is strictly less than 1/512, yielding the two stated rational endpoints, not an exact value for Lambda(x). The amplitude is positive and integral r*x=1/4. RESULT.md lines 32–82 and the independent word-image procedure allow replay. The supplied VERIFICATION.md and verify.py were inspected, not executed.

## originality

PASS

The binary map, cylinder pushforward and first-bit contraction are not credited as original. The supported refinement is a common linear leading residue for every Lipschitz observable with an explicit L1 remainder on a doubly exponential scale, and a rigorous nonzero witness using the smooth coordinate. The indexed comparisons concern other maps and observable classes; the primary strong-mixing paper is closely relevant, but its full quantitative details were not independently accessible. The pass is bounded to the refinement and is not a priority certificate.

## value

PASS

For a previously qualitatively mixing map, this separates the persistent half-bit mode from all other contributions to smooth/bounded correlations, and provides a uniform estimate at a very different scale for the latter. The coordinate certificate shows that removing the 2^(-n) mode is genuinely necessary even for a natural smooth observable, rather than just detecting an eigenmode among discontinuous cylinder functions. The scale separation and sharp leading rate are useful beyond qualitative mixing and beyond the individual finite rational numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
