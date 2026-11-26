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

The frozen proof counts distinct classes, including zero once. An odd-prime square has even valuation and square leading unit, and these conditions suffice by lifting. For nonzero shift of valuation t, classes below t keep their leading unit, classes above t obtain the shift's leading unit, and at t the only cancellation is at the unique leading residue −u. Away from 0 and −u the two nonzero unit tests reduce exactly to the finite-field character count; the quadratic character sum is −1 by counting factorizations of u². When t is even the two tail counts coincide by scaling by p^t. Odd t leaves only the lower layers; h=0 returns the cardinality. CRT acts on both membership tests. For p≡1 mod 4 the difference is 2S_{p,m}(1)−p^{m−1}, equal to 1 at m=1 and strictly negative by the geometric bound for p≥5, m≥2. Independent direct sets checked 1,555 prime-power shifts and all 780 shifts over six stated composites, and recovered the prime-five pairs (2,1),(2,5),(6,25),(22,125). Replay: /workspace/branches/f9f84e3c-a818-4441-a4b7-ffbfe2b053a6/independent_check.py. This is finite corroboration; the valuation proof establishes the universal result.

## originality

FAIL

An earlier exact transform on the identical complete square set yields the elementary no-residue-scan correlation formula and the sign reversal. This is demonstrated by a valuation-stratum inversion, not merely the observation that an abstract Fourier transform exists. The exact spatial form need not be printed in the prior record for the implication to hold.

## value

FAIL

The complete local spectrum and sign reversal are meaningful arithmetic features, and the direct argument is a useful alternate derivation. But the frozen claim offers no independent exact invariant beyond elementary inversion of already evaluated valuation strata and CRT. A wording or certificate repair would not leave an uncovered contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
