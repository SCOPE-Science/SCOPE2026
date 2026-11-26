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

The involution has eight fixed triples and 28 eligible pairs. Projecting a balanced cycle to the vertex classes of negative reversal gives even undirected degrees, counting loops twice. Six odd vertices in the full quotient force at least three omitted pairs. Exactly three omissions must form a perfect matching of those six vertices. The two matchings have nonzero residual divergence differences (-2 at 12 and +2 at 03, respectively). This difference is invariant under replacing a triple by its negative reversal, so neither matching can leave a balanced set. The 24 cyclic windows of the witness meet all exclusions and their distinctness also ensures least period 24. An independent bounded enumeration reproduced the degrees, both matchings, both residuals and all witness checks. Frozen replay path: verify.py, with verification_output.txt alongside the original RESULT.md; the uploaded script was not executed. The proof is only for alphabet four and window length three; no extremizer classification is obtained.

## originality

FAIL

A distinct indexed result states the same exact optimum under the same involution and self-pair convention and proves it by the same parity, two-matching and invariant-divergence obstruction. A different valid 24-symbol witness does not supply a distinct extremal claim or classify the solutions. This is demonstrable equivalent coverage, not a date-based finding of priority, dependence, or authorship.

## value

FAIL

Resolving this specific open table entry would have standalone mathematical value, including the obstruction to even a disconnected balanced choice at length 25. The separate finding adds neither an exact fact beyond the covered optimum nor a different obstruction or classification. A second example of attainment, without a new property of that example, does not justify a standalone extremal finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
