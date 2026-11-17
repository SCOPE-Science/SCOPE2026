---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For K_1 join mK_k (k,m>=2), partition dominating sets by hub selection to derive D(z)=z(1+z)^(km)+((1+z)^k-1)^m. D(0)=0 is simple; D(-1)=(-1)^m nonzero. For -1<z<0, put t=1+z: m odd produces no root; m even yields (t^-k-1)^m=1-t, with a strictly decreasing left side and increasing right side after proper endpoint normalization, hence one simple root. For z=-1-s, odd k yields (1+s^-k)^m=1+s, a unique solution s>1 for either m parity; even k yields no root for s>=1 and exactly one s in (0,1) when m even. These exhaust all negative roots, while coefficient positivity excludes positive roots. Bracketed solutions tend to +/-2^(-1/k) when bounded. The odd-k escaping root solves m log(1+s^-k)=log(1+s), giving s^k~km/log m at fixed k. Nonzero integer root would require (1+s^k)^m divisible by s, contrary to congruence 1 mod s. Independently computed exact Sturm root intervals for (k,m)=(2,2),(2,3),(3,2),(3,3),(5,4),(5,5), confirming parity counts; the proof is analytic for all parameters.

## originality

PASS

The known D-polynomial is not claimed novel. The full April–May 2026 Rather preprint in its accessible HTML shows Theorem 3.1 and Corollary 3.2 classify only even friendship graphs, i.e. blade size k=2; they already give the two bounded roots and limits for that subfamily. The submitted classification extends to every k>=3, including odd-k unbounded left root with an explicit km/log m scaling, which cannot follow by a k=2 specialization. The 2025 generalized-friendship formula and root annulus also do not count all real roots for k>=3.

## value

PASS

Domination polynomial zeros encode the combinatorial domination family and their exact real distribution is a motivated invariant. The even-versus-odd blade parity controls whether a negative branch remains bounded or escapes, a genuine structural asymptotic transition not encoded in the known finite polynomial alone. The complete two-parameter zero count, simplicity and locations across an infinite family make a useful self-contained result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
