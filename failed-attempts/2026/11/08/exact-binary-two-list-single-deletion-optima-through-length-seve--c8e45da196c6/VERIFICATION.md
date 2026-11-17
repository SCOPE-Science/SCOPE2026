---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Definition is exact capacity-two incidence packing over all 2^n codewords and their distinct one-deletion outputs. Independently fetched actual certificate.json and verified ALL 2≤n≤7 codeword witnesses and every rational dual constraint at each leaf using exact integer arithmetic in separate JS evaluator; n7 has exactly 103 nodes and 52 leaves, while list-one n7 bound uses 25 nodes and 13 leaves. Upper dual costs are strictly less than next integer, internal branches exhaust each binary choice. Hence code sizes and 33>32 follow rigorously for finite n. The certificates prove C, not O/V.

## originality

FAIL

Decisive full coverage: Oct13 published theorem gives complete length-seven list capacity vector including L=2=33 and all n≤6 pairs, explicitly identifies first strict 33>2*16 gap. Nov2 published theorem gives identical seven-length list-two sequence, 33-word witness and nondecomposability proof using exact rational dual branch certificates. The new differing 103-node certificate instead of 101-node certificate does not yield a different theorem.

## value

FAIL

The natural finite exact optimum is valuable as mathematics, but already fully published with exact proof and even an identical witness; the submitted result contributes no distinct scientifically valuable new invariant, structural insight or stronger generality beyond re-certifying the old answer. Thus V FAIL for this submission as an original contribution, not because short-code classification is intrinsically uninteresting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
