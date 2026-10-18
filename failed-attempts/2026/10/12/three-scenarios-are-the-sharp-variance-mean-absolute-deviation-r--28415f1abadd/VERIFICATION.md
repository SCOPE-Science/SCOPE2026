---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For any two equally weighted values deviations are +/- (x-y)/2, hence population V=MAD^2. Direct exact rational evaluation of A=(10,20,30) yields (MAD,V)=(20/3,200/3), B=(14,15,31) yields (22/3,182/3); common mean 20 and strict reversed ranking. For centered triple (-a,-b,a+b), algebra yields MAD=2(a+b)/3 and V=(a+b)^2/2+(a-b)^2/6, and mean-padding preserves numerator sums. Claims are mathematically correct although prior-covered.

## originality

FAIL

Full text of a published earlier Resultary theorem (2026-10-04) on the exact MAD/standard-deviation interval for arbitrary fixed positive atom-mass profiles mathematically dominates the claimed three-scenario ranking boundary. For two equal-mass atoms D/sigma=1 identically; for three equal-mass atoms the achievable ratio is nonconstant [sqrt(2/3),sqrt(8/9)), so choosing two support shapes and positively scaling them reverses MAD versus variance rankings. Equal means follow by translation. The exact particular vectors are routine witnesses, not a genuinely uncovered theorem.

## value

FAIL

The two-versus-three threshold and exact tuple comparison are a short elementary application of the previously published stronger exact fixed-atom standardized MAD interval; no independent unknown natural invariant or substantial new obstruction survives the coverage. Numerical correctness and a portfolio interpretation alone do not establish independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
