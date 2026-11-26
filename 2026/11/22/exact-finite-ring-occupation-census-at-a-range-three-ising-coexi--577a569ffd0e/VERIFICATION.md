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

Re-audited the replacement for every labeled binary ring n≥7 at h=10J/3 and J>0. The local defect is 3∑1{b_s=b}−10b+3+p_a−p_j. All 16 entries are nonnegative and their cyclic sum is 3(E+nJ)/J. State 0 has no zero-defect predecessor; 2 has no zero-defect successor. The remaining graph forces all closed walks through triple 110 and allows only returns appending 1110 and 01110. Across a return boundary these are exactly runs of three ones with one or two zeros between; conversely after the first zero following each 111 run the next return is determined by the number of remaining zeros. This proves the unique cyclic run decomposition and both directions of the iff classification. Marking block starts gives n/(a+b) times the ordered multinomial count even for rotationally periodic words. The determinant follows from the two intersecting simple cycles; primitivity and the spectral gap verify the stated corollary CLT, with µ=3/L and v=9 Var(length)/L³=9p₄p₅/L³. Independent `python /workspace/independent_replay.py 3` exhausts 7≤n≤16 for energy/occupation counts and checks the symbolic characteristic polynomial; `python /workspace/independent_replay.py 3-language` separately checks 32,640 individual labeled words for the energy/run equivalence. No numerical or formal verification is used to infer the infinite quantifier.

## originality

PASS

For the repaired theorem only: the same-model prior trace and characteristic equation cover the aggregate counts and cumulants, and the prior phase diagram identifies the two pure periods, but neither result characterizes individual labeled periodic words by a necessary and sufficient run constraint with arbitrary mixing. The repaired claim isolates this structural part and credits the trace corollaries.

## value

PASS

The constructive iff rule gives a minimal description of every labeled configuration attaining the coexistence energy: arbitrary mixtures are allowed but no other patterns are. This resolves what the phase and entropy data leave unspecified, gives direct membership and construction without transfer traces, and supplies an exact local defect certificate. It applies uniformly to every admissible ring length, not to an arbitrary small instance. The counts and asymptotics remain reproducible illustrations, not the basis for the value verdict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
