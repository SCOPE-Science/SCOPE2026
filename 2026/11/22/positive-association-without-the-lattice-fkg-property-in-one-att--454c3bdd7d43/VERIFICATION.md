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

Reconstructed from RESULT.md §§1–4. The minimum of the independent rate-p and rate-(1-p) clocks is rate one and independent of its winning label. In the coupling that advances A clocks and delays B clocks, a first lost A acceptance would have had an A proposal no later in the favored system. Its rejecting B neighbor there would also have been B earlier in the original, a contradiction. The dual earliest-event argument rules out a gained B. The permanent one-attempt rule is respected, since the relevant winning labels cannot flip against the comparison. Harris applies to the independent signed clocks, with the two species ordered oppositely. On a clique condition instead on the attempted set: for a fixed nonempty A-set of size k and l outside B-proposals, the A-set is realized iff the earliest of these k+l proposals lies in it, probability k/(k+l). Summing over the outside proposals gives the claimed triangle and edge laws, their minors (negative on the triangle because 3-(p+2)t >= 1-p; positive on the edge), and the saturation formula. The edgeless case factors, and one or zero vertices have no incomparable sets. Independent exact enumeration on 2–4 vertex cliques at nine rational bias/time combinations reproduces these minors and saturation probabilities; replay `python3 /workspace/audit_checks/frozen_reconstruction.py`. These checks do not establish graph-universality; the order argument does. Ties have probability zero and strictness excludes p=0,1 and t=0.

## originality

PASS

Supported distinctive content is full-field same-color association with the mixed sign for finite one-attempt graphs, separated from output log-supermodularity by an explicit, minimal all-parameter obstruction. The original one-dimensional model, classical product-measure inequality and earlier distance-two sign are credited; the identical indexed record is not a distinct antecedent. No inspected distinct claim gives the obstruction or dominates the combined finding.

## value

PASS

The distinction changes what can be inferred about the physical output law: monotone events of one color are associated on arbitrary graphs, but arguments needing lattice log-supermodularity or monotone conditioning cannot assume it. A triangle gives the sharp graph-size threshold throughout the interior bias range and all positive times, not an isolated numerical counterexample. The complete-graph specialization shows the mechanism persists with size. This says nothing about total uncolored occupancy or repeated proposals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
