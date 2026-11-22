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
# Verification of the finite universal-spectrum census

`verify_all.py` and `verify_orbits.py` can be run directly in one directory with Python 3.10 or later and the accompanying `orbit_witnesses.json`. They use only standard-library integer arithmetic, exact set operations, and Gaussian-integer character sums. The expected exact output is embedded as `verify_output.txt`.

The first checker enumerates all \(6{,}907\) subsets containing the identity with sizes dividing \(16\); disjoint-cover recursion generates all normalized tiling complements. It verifies that all \(715\) normalized tiles have a common character basis and exactly \(460\) have no subgroup choice. The second checker uses a different direct complement-enumeration method, validates every proposed witness on \(19\) affine representatives, and independently checks subgroup exclusion and affine orbit coverage. The two checks agree on the universal and obstruction totals of \(2{,}155\) and \(1{,}168\), respectively.

The criterion \(\sum_{t\in T}\chi_\xi(t)=0\) is tested as a pair of exact integer equations. The finite enumeration, rather than a floating-point experiment, supports the complete claim. No extension beyond \(\mathbb Z_4^2\), external formal certification, or independent audit is asserted.
