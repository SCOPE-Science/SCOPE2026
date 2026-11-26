---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Square-zero Taylor evaluation and CRT modulo (X−a)² prescribe the residue and scalar derivative independently, and ordinary interpolation prescribes translations. The resulting functional data are unique because V is nonzero. Idempotence forces the residue map onto its fixed residues. There the fiber map is b v+w with b²=b and bw=0, hence identity (b=1,w=0) or constant (b=0). Every image point of an idempotent is fixed, so no unused fiber can add other points to that target. Each unused residue can send to a specified full fiber in q^(d+1) ways, or to a specified singleton in one way. Multiplying independently gives the fixed-image multiplicity and, by choosing k residues, s full fibers, and k−s singleton values, the rank polynomial. The image cardinality is k+s(q^d−1), with unique maximum at k=s=q and unique proper maximum type k=q,s=q−1; its coefficient is q^(d+1). A separate exact check (`python3 review_checks/finite_checks.py 3`) built the span of monomial evaluation tables by direct square-zero ring multiplication and recovered the image counts 15, 35, 99 and idempotent totals 21, 49, 129 for q=2,d=1,2,3, including the fixed-image multiplicities. The finite check is not a substitute for the CRT proof.

## originality

PASS

Within the bounded comparison, no earlier retract-specific theorem or exact enumeration of these subset images and ranks was identified. The polynomial-function normal form itself is established prior work; the new presentation only applies it to composition-idempotents. The routine nature of that deduction is evaluated separately under value.

## value

FAIL

The object and image-rank question are natural, and the exact identities are correct. But here the known independent affine-fiber parametrization already reduces the entire problem to scalar idempotence over a field. Each fixed block is identity or constant by b²=b and bw=0, and the unused blocks impose no further constraint beyond independently choosing one of the already parametrized affine maps or one forced constant. The image count, rank support, enumerator and extremal gap are the same immediate product count and the size of one lost fiber minus a singleton. No additional structural obstruction, distinct mechanism, or application separates the claimed exact invariant from that mechanical calculation. The failure is routine derivation, not a counterexample to any formula or a claim that a prior table lists every coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
