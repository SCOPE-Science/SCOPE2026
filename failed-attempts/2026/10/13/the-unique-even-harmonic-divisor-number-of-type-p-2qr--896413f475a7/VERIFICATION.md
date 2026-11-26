---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The two placements of 2 exhaust even p²qr with distinct primes, and τ=12. When 2 is squared, 30/7≤H<48/7, so h=5 or 6. Independently writing B=7h and A=48−B gives (Aq−B)(Ar−B)=48B with both factors positive; exact factor-pair enumeration at both h yields only q=5,r=7,h=5. When 2 is unsquared, H=8p²r/((p²+p+1)(r+1)), so 54/13≤H<8 and h=5,6,7. Set D=8p²−h(p²+p+1). We have Dr=h(p²+p+1), so D>0 and D divides 8p². If p≥11, p does not divide h and thus gcd(D,p)=1; this requires D≤8, whereas D≥p²−7p−7≥37. For p=3,5,7 the positive-D candidates have r=65/7,155/45,186/14,285/107,342/50 respectively, never an integer. Finally σ(140)=336 and H=5. This reconstructs an unbounded proof, not a conclusion from the uploaded prime-300 test (inspected, not run).

## originality

FAIL

The prior literature explicitly reports completed global classifications of all integers with integral harmonic mean bounded by 13 (Cohen) and 300 (Goto–Shibata). Every possible solution in the assigned family has integral harmonic mean 5, 6 or 7 by elementary size bounds. The classification is therefore a mechanical slice of published exhaustive classifications, not an unbounded problem left open by a cutoff on the size of n. No claim is made that the papers state the exponent-pattern slice verbatim. Their table entries were not retrievable in the attempted lawful copies; the fail reason is affirmative coverage by the stated global classifications together with the exact scope reduction, not the access failure.

## value

FAIL

This familiar exponent pattern makes a useful exercise in bounding harmonic means, but the resulting classification is already obtainable by elementary filtering of a completed classification. The frozen finding does not establish a more general structural lemma or a genuinely new range. A shorter direct proof supplies explanation, not a distinct classification result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
