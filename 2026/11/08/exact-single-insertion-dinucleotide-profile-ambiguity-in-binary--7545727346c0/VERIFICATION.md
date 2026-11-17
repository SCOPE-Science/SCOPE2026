---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS. Exact all-length invariant is number of distinct linear binary dinucleotide-count profiles after exactly one insertion. From actual RESULT.md six distinct delta vectors arise: e00,e11,e01,e10,e01+e10-e00,e01+e10-e11, with endpoint, present-symbol and equal-pair conditions yielding I(w)=1+[w1=wn]+[0]+[1]+[00]+[11]. Fibonacci no-00 and Lucas trace(M^(n-1)) endpoint counts plus inclusion-exclusion establish C3..C6, with n=1 checked separately. Direct independently constructed output strings/profiles through n=12 match, including n5=(0,16,12,4), n6=(2,18,34,10), n9=(0,88,260,164). Deletion six requires opposite cross-pair boundary changes and both equal-pair internal changes; this forces the insertion-six conditions. Finite checks corroborate but algebraic enumeration proves all n.

## originality

PASS

Best-of-knowledge PASS: exact local single-insertion dinucleotide-frequency neighborhood and four-class Fibonacci/Lucas distribution are not given by the inspected global Markov-profile census or the different one-deletion local profile distribution. Structural deletion-six implication also survives the comparison. Targeted Resultary searches did not locate a covering insertion counterpart; absence is not proof of priority.

## value

PASS

PASS. Single-insertion local profile ambiguity is a natural source-dependent invariant for dinucleotide-frequency DNA sequencing channels. The pointwise six-vector classification, all-length population law and deletion/insertion saturation implication are not mere spelling changes of global code size; they give exact error-ball behavior and realistic finite-width observability limits. The bound and distribution remain independently useful without a new code capacity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
