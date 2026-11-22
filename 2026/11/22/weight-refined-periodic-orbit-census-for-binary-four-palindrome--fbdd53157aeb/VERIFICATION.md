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

The complete argument is in `RESULT.md`. `check_cycles.py` reconstructs the eight-state, two-bit weighted binary de Bruijn graph from first principles. It enumerates exactly six simple directed cycles and exactly two vertex-disjoint cycle pairs and reconstructs \(\det(I-zA(u))=1-uz^2-(u+u^3)z^4-u^3z^6\) as a formal integer coefficient dictionary. It does not assume the proposed determinant.

`check_direct.py` enumerates all binary words at each circumference \(1\le n\le16\), explicitly checking all circular length-four windows with periodic indices, and independently compares every one-count to coefficients extracted by a symbolic formal-log recurrence. It also checks primitive-word existence for all tested even circumferences and absence for odd circumferences. Both scripts return normally with assertions active using the Python standard library. Commands from the extracted directory:

```
python3 check_cycles.py
python3 check_direct.py
```

The infinite claim is proved by graph-cycle enumeration, the determinant-trace identity, and constructive overlapping cycles; the finite tests are a cross-check, not an infinite proof. The source comparison is bounded by the accessible full texts and published-record summaries, and independent audit has not been performed.
