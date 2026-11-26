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

The cohomology coefficients are counted by the affine Schubert cell decomposition in complex dimensions, and the selection uses the identity Kazhdan–Lusztig polynomial, not ordinary Betti ranks. The reduced-word subword theorem gives the stated interval recurrence; the right-descent KL recurrence uses zero for incomparable lower indices and integral correction exponents only. An original exact replay using permutations of the 48 roots, bitset intervals and integer polynomials covered all 1,152 Weyl elements and 396,809 comparable pairs, checked word lengths by root inversions and matched all three KL profile counts and all eleven triples (maximum, multiplicity, eligibility). It matched the ambient length distribution and [2]_q[6]_q[8]_q[12]_q coefficients; the general coefficient inequality applies in the stated normalization. The selected maximum length is 23, confirming no eligible degree >=12. A supplemental extraction confirms the same four winners of length 14 in degrees 4–5, the same two of length 20 in degrees 6–9, and the same two of length 23 in degrees 10–11. Replay: /workspace/branches/02db693c-f8a8-46fc-8394-7ce127f57885/replay_root_actions.py, output replay_output.txt there. The independent replay uses one direction of the standard recursion; the frozen two-direction checker was inspected rather than run.

## originality

PASS

The ordinary rank calculation and the ambient inequality are credited to prior theory. The inspected results do not give the 217-element KL-conditioned finite spectrum or exact maximizing multiplicities; the closest exact F4 records address different statistics and cohorts.

## value

PASS

The conditioning is intrinsic: evaluate KL at the identity and select the first nontrivial integer value, then measure ordinary duality defect rather than KL itself. The data decide exactly when the known universal inequality is sharp in exceptional type F4 on that stratum, including the first failure and changes in which lengths and KL profiles maximize. An unconditioned table or a single largest defect cannot answer these questions. This is a useful finite exceptional-type benchmark, without implying new general Weyl-group bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
