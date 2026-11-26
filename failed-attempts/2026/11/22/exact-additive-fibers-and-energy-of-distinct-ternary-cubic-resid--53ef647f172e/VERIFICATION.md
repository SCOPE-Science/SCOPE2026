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

For k>=3 the cyclic unit group has a cubing kernel of size 3, and the unit image is exactly the two full mod-9 cosets of +1 and -1. The nonunit image is injectively embedded as 27C_{k-3}. The disjoint ordered-summand cases give h_k or 2h_k from the same- or opposite-sign unit cosets, 2s_{k-3} from the mixed pairs, and the quotient fiber exactly on 27-multiples. This includes diagonal value pairs and uses the correct bases k=0,1,2. Squaring the fibers gives 2h_k^3+4h_k^3, the mixed contribution 8h_ks_{k-3}^2, the zero-class cross term 4h_ks_{k-3}^2, and the smaller energy. The normalized recurrence has multiplier 27^(-3) and constant 38/4563 up to errors tending to zero in all three subsequences. Its limit and the ratio after division by (3/13)^4 are both correct. Independent ordered-pair enumeration through k=6 matched all 1080 target fibers at k=3..6 and the cardinalities and energies (for example, E_6=3236473); it is not the all-depth proof. Frozen verify.py was inspected, not run: its mismatch diagnostic has an undefined name at line 47, but this does not affect the proved result or the separate enumeration.

## originality

PASS

The precise distinct-value formulas and constants are different from the inspected input-weighted results, and no inspected exact covering theorem states them. The decomposition, counts, support and convolution case split are established material, not credited as new. Whether evaluating the same convolution with different weights clears the scientific-value bar is a separate issue, assessed below.

## value

FAIL

The cube set and collision energy are natural, but here the exact remainder is a mechanical reweighting of an existing convolution calculation. Let h=h_k, s=s_{k-3} and let T embed the smaller fiber vector by 27. The known decomposition and the published coset-convolution cases give h times the indicators of the two +/-2 classes, 2h on the zero class, and 2s on the two +/-1 classes; the both-nonunit term is exactly T r_{k-3}. These coefficients follow by substituting the known component sizes for the earlier input-sampling weights; there is no new counting step for any target. The squared norm of the fixed terms is 6h^3+8hs^2. Their inner product with the embedded term is 2h times its known mass s^2, and T preserves the smaller squared norm. Hence the asserted energy recurrence is forced, and normalizing it evaluates a geometric series and then divides by the known limiting density to the fourth power. The different constants are correct and are not claimed to have been tabulated before, but their precision here does not supply a structural fact independent of the established decomposition and convolution. No nonmechanical surviving claim was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
