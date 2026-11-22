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

# Reproduction and scientific boundaries

The construction uses nonzero binary vectors as Fano points and line normals; adjacency means zero binary dot product. All valid moves are occupied adjacent pair to unoccupied adjacent target, consuming one peg. Reaching each target is allowed to use a different sequence.

Run the self-contained files using:

```sh
python3 verify_fano_pegging.py
c++ -O2 -std=c++17 verify_fano_pegging.cpp -o verify_fano_pegging
./verify_fano_pegging
python3 verify_peg_bfs.py
```

The Python recurrence checks 16,384 masks, all 336 explicit automorphisms, four-point incidence types, failure at five pegs, and all inclusion-minimal states. The C++ bottom-up calculation independently checks all masks and the geometric criterion. The third program enumerates forward reachable configurations directly for every four- and five-element initial set, rather than using the recurrence.

Observed outputs for the reviewed sources: all three programs printed `PASS`; universal counts by size from zero through fourteen were `0 0 0 0 336 1862 2989 3430 3003 2002 1001 364 91 14 1`; inclusion-minimal counts were 336 at four and 434 at five, zero otherwise. Exactly 84 point–line orientation triples define legal directed moves.

The results are exhaustive for the 14-vertex graph but give no conclusion for larger graphs. Source-code calculations establish finite cases, not historical priority or independent external certification. Literature comparisons and residual publication risks appear in REVIEW.md and AUDIT.json.
