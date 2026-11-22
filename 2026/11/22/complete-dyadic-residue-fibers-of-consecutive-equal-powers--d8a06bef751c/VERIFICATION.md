---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scope

The exact theorem is proved by branchwise \(2\)-adic valuation identities, not by numerical experiments. The critical cases are: \(k=1\), the linear map; odd \(k\ge3\), two parity isometries with slope valuation zero; \(k=2\), two isometries of the triangular polynomial; and even \(k\ge4\), four branches modulo four with valuation shift \(\nu_2(k)\). These identities prove surjectivity of each normalized branch by finite quotient permutations and compatible inverse limits. Counting the branch fibers at precision \(2^n\) gives \(2^{\min(n,h(k))}\) preimages per attained residue.

Run `python3 verify.py` to reproduce 11,256 direct finite checks. It checks all residue fibers for each positive exponent from 1 through 40 and every modulus \(2^n\) with \(1\le n\le11\), followed by raw integer-power valuation differences for selected exponents and congruent input pairs. The script does not use the proved formula to compute the left-hand side. The finite checked ranges are not claimed exhaustive over all moduli or exponents.

The source comparisons are detailed in the scientific review. The inspected published results for unrestricted two-variable power sums do not automatically imply the one-variable constrained law; an uncatalogued equivalent statement remains possible. Independent external validation has not been undertaken.
