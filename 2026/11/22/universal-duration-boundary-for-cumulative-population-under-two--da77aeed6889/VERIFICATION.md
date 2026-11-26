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

For z=rt, the reciprocal obeys Y′=−Y+1/K. Subtracting the two affine evolutions gives (b−a) times 1−e^(−z) in the first stage and (b−a) times [(2−e^(−h))e^(−(z−h))−1] in the second, with a=1/K_H<b=1/K_L. The latter starts positive and ends at −(b−a)(1−e^(−h))², giving the stated unique positive-time crossing and the terminal ranking. For the time integral, the weight is W_y=e^(2z)/[(y+H_HL)(y+H_LH)] with y=1/N_0 and both H increasing. If y₂>y₁, W_y₂/W_y₁ strictly increases with time across both stages (and is continuous at the switch). Hence the ratio of the negative late contribution to the positive early contribution strictly increases with y. At y↓0 the early contribution diverges logarithmically since the signed factor is asymptotic to z and both H_i are linear to leading order; the late contribution stays finite. At y→∞, y²W_y→e^(2z) uniformly. Integrating the two pieces gives −(E−1)²(E²−2E−1)/2 with E=e^h. This proves the claimed regime split and strictness even at the critical duration, where the ratio reaches one only in the y→∞ limit. The population tie, when it exists, is unique; reciprocating y gives the stated orientation. Exact rational stage products for the example are both 16/7 before taking logarithms.

## originality

PASS

The supported distinction is a sharp duration boundary for finite population-time, including strict one-tie classification and its contrast with the terminal order. Existing logistic solutions supply the reciprocal dynamics; the inspected related results do not give the sign classification for these two fixed schedules.

## value

PASS

Even in the simplest exact setting, terminal stock gives misleading guidance if the objective is cumulative abundance. With exposure durations and capacity levels controlled, the theorem isolates when that disagreement is universal and when initial density matters, gives the unique possible tie, and distinguishes this threshold from the within-trajectory crossing. This is a structural comparison, not a field prescription or an arbitrary numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
