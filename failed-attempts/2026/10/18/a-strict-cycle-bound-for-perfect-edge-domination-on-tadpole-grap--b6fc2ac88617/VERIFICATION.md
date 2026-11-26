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

The three-color rules are bijective: the selected edges are exactly those with two nonwhite ends, and each omitted edge has a white end and a yellow end incident to exactly one selected edge. This allows adjacent selected edges and includes the full edge set. Degree-two transitions give the stated matrix M; a closed walk counts the cycle and tr(M^(c-1) H_t) inserts exactly one degree-three rule and the tail. I reproduced M^5=M^4+M^2 in exact integer arithmetic and independently enumerated the nine seeds: for each edge subset mask S and each unselected edge e, test whether the bit count of S AND the line-graph neighbor mask of e is one. Subtract the tadpole count from the count for C_(c+t) for c=3,4,5 and t=1,2,3 to obtain ((2,3,4),(2,5,7),(4,6,9)). For the tail, partition by the final leaf and its two neighbors: (W,Y) reduces to the shorter extension with a yellow leaf; (Y,Y,W) and (Y,B,Y) reduce to the original leaf colored yellow and white, respectively; (Y,B,B) reduces to the shorter extension with white leaf by replacing the last two remaining colors with (W,Y) from the leaf inward. The inverse in each case follows from the same local rules. These bijections give the tail recurrence from t=4; the matrix gives the cycle-length recurrence from c=6. Subtraction and two strong inductions from the seeds establish the infinite strict bound. The frozen verify.py is finite corroboration, not the induction; it was inspected, not rerun.

## originality

FAIL

The distinct indexed lollipop result 381ff49f7243 covers exactly the same graph family, counting convention, strict inequality at equal order, both recurrence ranges, and identical nine deficit values; it additionally gives a generating function. The frozen finding therefore does not establish a distinct contribution relative to the current indexed record. This is demonstrated statement-level coverage, not a finding that the indexed record was first or that the frozen proof is incorrect. The original research paper's general conjecture and previously proved recurrence tools alone would not justify this verdict.

## value

PASS

Judged as mathematics separately from duplication, a strict equal-order extremal comparison for all cycle lengths and all pendant lengths settles a natural unicyclic test family of the connected-graph conjecture. The exact positive deficit law in two parameters goes beyond a few counts or running an available counting algorithm. It does not settle arbitrary unicyclic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
