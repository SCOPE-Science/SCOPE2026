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

# Finite verification

Three standalone programs implement complete deterministic finite computations with standard C++17. Compile and execute `verify_orbits.cpp` and `verify_canonical.cpp` with `g++ -std=c++17 -O3 -o check source.cpp`, substituting each filename for `source.cpp`, and similarly compile `verify_burnside.cpp`.

`verify_orbits.cpp` visits the complete integer interval representing all \(2^{25}\) binary matrices, rejects singular matrices using exact binary elimination, and traverses invertible-matrix orbits under two explicitly given generators of \(S_5\). It checks stabilizer orders directly against the full 120-element permutation group, records element orders to distinguish possible group types, and reports all thirteen type counts.

`verify_canonical.cpp` independently enumerates the complete binary matrix interval, constructs all 120 permutations lexicographically, and counts only orbit-minimal invertible matrices. It separately computes their full stabilizers and group-type breakdown. It confirms the same 13 entries, 85,411 classes, and 9,999,360 labeled matrices.

`verify_burnside.cpp` independently enumerates the binary orbital matrices fixed by each nonidentity cycle type. It obtains invariant-invertible counts 21,504; 1,536; 504; 24; 32; 15 for cycle types \((2,1,1,1)\), \((2,2,1)\), \((3,1,1)\), \((3,2)\), \((4,1)\), and \((5)\), respectively; the identity count uses the exact product for \(\operatorname{GL}_5(2)\). Burnside's weighted sum is 85,411. All programs executed successfully and printed `VERIFY_OK`.

These verifiers prove a finite exhaustive census for the stated dimension and field only. They do not justify claims for higher dimensions, extension fields, or all possible parameter families.
