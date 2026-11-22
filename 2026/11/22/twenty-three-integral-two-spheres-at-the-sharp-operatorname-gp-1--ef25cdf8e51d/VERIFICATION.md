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

# Executable exact checks

Run `python3 verify.py` with standard Python 3 from the directory containing this file. The package also includes an unedited captured stdout file `verification_output.txt`; the live run terminates with `PASS`.

The checker builds the exact 36-vertex \(\operatorname{GP}(18,3)\) adjacency and all-pairs unit-edge distances; enumerates all faces of the inclusive radius-two Rips clique complex; independently lists all simple graph hexagons and verifies that the 42 exceptional alternating triangles are maximal and exhaustive; and replays the 144 centered-neighborhood free-face pair deletions against the current face set. It also tests every outer-spoke hexagon's uniquely assigned inner edge and that each of the three inner cycles traverses the outer 18-cycle once after substitution.

As a second exact homotopy calculation, after 36 free triangle–tetrahedron deletions, the verifier chooses a 35-edge spanning tree of the remaining connected two-complex, derives signed two-cell attaching words and performs 127 legal elementary generator eliminations. The 23 remaining attached two-disks have empty words, corresponding to a wedge of 23 two-spheres. This separate finite cellular presentation check agrees with the structural paired-hexagon CW proof. Finally, exact signed boundary elimination over the fields with two, three and five elements gives boundary ranks \((35,127,36)\) each time.

The modular computations alone cannot prove integral torsion-freeness or a wedge homotopy type; the explicit homotopy reductions do. The script certifies a **single finite graph**, not a classification over arbitrary sizes, and no independent mathematical audit has been performed.
