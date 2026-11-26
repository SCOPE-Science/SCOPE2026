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

Inclusion–exclusion for j!S(n,j) reduces F_n modulo arbitrary 3^K to a finite exponential sum, with nonunit bases disappearing as soon as n>=K. Modulo 81 the even indices have step-two first difference 72 and all higher differences 0; the second difference vanishes on the three even classes modulo 6, and the first is calibrated by F_6-F_4=4608. Odd first differences are 6 mod 9. In expanding a shift 2t, s=v_3(t), the binomial coefficient at order a has valuation at least s-v_3(a), and a unit-base difference has an additional factor 3^a. For even n the a=2,3 terms are handled separately by the mod-81 bound; a>=4 gives valuation at least s+3. For odd n all a>=2 have valuation at least s+2. With n>=max(4,s+3) only the first term determines the claimed exact valuation. The counting argument then gives the parity-wise residue multiplicities, the sharp least period (any eventual period must preserve parity and satisfy the odd-branch condition), densities and closure; F_0 through F_3 add no other residues. I independently reproduced the modulo-81 leading finite data and fibers through 3^8 with the Stirling DP in /workspace/branches/reproduce_4.py. I did not execute the source script; its self-equality assertion is tautological but the proof and the independent check do not use it.

## originality

FAIL

Demonstrable full coverage by the distinct same-day interpolation record 91974cd107ef. Its stronger branch statement recovers the frozen exact translation law at the stated finite-index threshold, not just the eventual image and fibers. The shared date is not evidence for which record came first; this is a failure to establish a distinct mathematical claim, not a claim about historical priority.

## value

FAIL

The actual distribution is a worthwhile invariant when unknown, but no distinct invariant or non-implied improvement survives here. The frozen exact difference law and safe onset follow by one modular comparison with the stronger isometries, and the finite-exponential proof is an alternative route to fully covered conclusions rather than a separately established contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
