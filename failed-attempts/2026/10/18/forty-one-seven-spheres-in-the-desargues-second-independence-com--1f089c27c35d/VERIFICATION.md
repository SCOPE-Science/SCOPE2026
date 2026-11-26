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

For a subset of the defined 20-vertex GP(10,3), components of size at most two are equivalent to induced degree at most one. An independent run generated the faces recursively and cross-checked all 2^20 masks, obtaining 62,049 faces including the empty face and the stated facet and dimension counts. On the nonempty faces the greedy vertex matching leaves the advertised (1,3,44) cells in dimensions (0,6,7) after 31,000 pairings. A complete topological order checks all 400,760 directed incidences, sufficient for Forman's theorem. The independent integral calculation matches the signed three-column witness for masks 0x18e94, 0x55292 and 0x61664 in the claimed 6-cell basis. In the Morse projection a matched upper generator dies and the matched lower face is solved out using the ±1 incidence in its partner's boundary; subsequent lower-face terms occur farther along directed paths, so the recursion terminates. The determinant −1 makes the differential onto over Z, with kernel free of rank 41. The resulting CW model is 5-connected from its cell dimensions; Hurewicz with H₆=0 then makes it 6-connected. Hurewicz representatives for a basis of H₇ give a map from the wedge of 41 seven-spheres that is an integral homology equivalence between simply connected CW complexes and hence a homotopy equivalence. The finite computational certificate supports that nonequivariant conclusion; it is not formal or equivariant verification. The frozen script was not executed.

## originality

FAIL

Distinct public catalogue records already supply exact equivalent coverage of the frozen nonequivariant claim, including its integral rather than merely mod-two conclusion. In particular e931147dfbfd states the same GP(10,3), face rule, wedge, critical cells and primitive witness. Two additional distinct records state the same conclusion and add results not proved in this frozen package. This is a failure of distinct content against the inspected catalogue, not a finding about which record came first historically. The later catalogue labels do not by themselves establish public priority, dependence or authorship.

## value

FAIL

The Desargues graph and integral higher-independence homotopy are well motivated, and the calculation is more informative than a mod-two rank check. As submitted, however, this narrow exact result reproduces a covered classification and primitive certificate. There is no distinct new invariant, broader theorem or symmetry calculation in the package. The independent replay is valuable as corroboration, not an additional research result that rescues the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
