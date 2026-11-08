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
# Verification

Run `python verify_split.py` from this file's directory (Python 3, standard library only). The checker constructs raw ordered disjoint partitions of each team and tests the two functional dependencies without using graph-orientation logic. A second independent routine evaluates the connected-component formula. It compares both for all team masks in every rectangle with \(1\le p,q\le3\) (682 teams), and checks the inclusion-exclusion total in all nine sizes. In addition it calculates the component formula over the complete sets of 2, 16, 512, and 65,536 teams on square alphabets of sizes one through four, independently verifying sharp maximum and aggregate counts. It additionally evaluates 200 seeded four-by-four teams against direct partition enumeration. The expected final line is `PASS`.

Key expected outputs include square-alphabet maxima \(2,4,9,18\), total witness counts \(3,47,2074,183249\), and total satisfying teams \(2,16,460,33959\) (the last set follows by checking nonzero component counts). The last set of satisfying-team numbers is reported as a finite verification table only; no new closed formula for those numbers is needed to prove the main claim.

Scientific scope: finite *sets* of assignments, disjoint ordered splitting explanations, usual functional dependencies. The checker performs exhaustive searches only over the specified finite domains. The all-size component multiplicity, sharp extremum, inclusion-exclusion formula and generating identity require and receive the symbolic proofs in RESULT.md; no finite table establishes them. No external or independent verification is claimed.
