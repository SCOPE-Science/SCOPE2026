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

The bit-mask update is exactly (E,R) -> (T(E) outside E union R, E); the threshold counts the four Hamming-distance-one neighbors. In my separate vectorized enumeration of every ternary state, I found the first t with F^(t+4)(x)=F^t(x), or would have rejected the bound if any state did not have such a t by 7. An equality certifies recurrence and holds from first entry if it holds later. Shorter return tests yielded only periods 1 and 4. All eleven nonzero depth/period cells agree with both frozen outputs; canonical phases give one fixed point and eighteen four-orbits and all 18 individual basin sizes match. The exact depth-seven count is 19200; the explicit trajectory from ternary index 88458 reproduces all nine witness rows through its first fixed phase at 7. The equality F^11=F^7 is certified by enumeration and the witness proves F^10 differs from F^6. The coordinate permutations and translations are the full group: a stabilizer of 0 permutes its four neighbors, determining any vertex from its distance to 0 and to those neighbors. Applying all 384 permutations to every recurrent phase gives class sizes 6 and 12, and XOR closure of the direction sets checks the four disjoint affine two-flats, including the stated equality pattern of their directions. Their basins are 676 (parallel) and 644 (alternating). I also verified the 72 nonconstant recurrent transitions are unchanged by adding antipodal edges; this says nothing about their full basins on the folded cube.

## originality

PASS

The exact threshold-two census on the unmodified four-cube is supported as distinct within the inspected evidence. There is significant overlap with the same-day Clebsch finding: the per-orbit basin sizes and seven-update cutoff coincide, the geometry is related, and every Q4 four-wave persists under folding. The Clebsch claim nevertheless concerns a different map, with 90 orbits, not 18; it does not give the Q4 counts, selection of cycles or entry histogram. I do not infer order or priority within that date.

## value

PASS

The standard four-cube and its smallest square-torus realization with C4 factors make a natural controlled case for changing threshold and adjacency. The full labelled invariant separates the two possible affine phase geometries, quantifies how rare their attraction is, and proves that all oscillatory basins stabilize by depth two while extinction transients reach depth seven. These precise structural and basin facts give a reusable benchmark and a base case for comparisons with the threshold-one and folded-cube models, not just a state count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
