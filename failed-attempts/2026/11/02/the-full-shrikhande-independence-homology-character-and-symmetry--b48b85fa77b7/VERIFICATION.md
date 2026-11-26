---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An independent exact reproduction (python3 -B /workspace/reproductions/shrikhande.py) enumerates faces by the edge exclusion rule, obtaining (16,72,96,16), with no 5-vertex face. Boundary ranks modulo 101 are (15,57,16); these give rational lower bounds, and the augmentation, the domain dimension of the third boundary, and boundary composition zero give the matching rational upper bounds. Thus reduced rational homology is concentrated in dimension two with rank 23. Direct vertex-permutation search preserving adjacency gives exactly the same 192 permutations as the affine list, independent of the neighborhood-stabilizer argument. Reduced Hopf trace gives the stated signed-face sum: an invariant independent face with j permutation cycles contributes (-1)^(j+1), with empty face contributing -1. Enumeration by independent unions of vertex cycles gave frequencies {-7:12,-3:4,-1:69,0:32,1:24,2:32,3:18,23:1} and the asserted translation grid; integer Fourier inversion reproduced the displayed multiplicities. The character sums are 32 over T and 0 over G. For these finite simplicial actions, barycentric subdivision removes simplex inversions; rational chains of the orbit space identify with coinvariants. Exactness over Q proves the asserted rational orbit-space homology. This gives no integral assertion and the separate nonequivariant wedge claim was already established in the cited prior calculation.

## originality

FAIL

Substantive prior coverage is verified, not merely suggested by a search. Resultary 25a0863c3d60 (2026-10-18) computes the full character of the same 192-element group on the same 23-dimensional H2, in fact including a full element table and irreducible decomposition. It gives both invariant dimensions. Resultary 8980caaada4f explicitly gives the same translation matrices, and 76bf36fe874b gives stronger translation orbit-space topology. The full-group rational acyclicity is a direct consequence of the earlier full-group invariant calculation and the standard rational quotient argument. A general Hopf trace formula with these faces does not provide a distinct new result once the character itself is known.

## value

FAIL

The natural equivariant invariant is scientifically meaningful, but the frozen work supplies no distinct unknown exact fact after prior coverage. Re-enumeration of a known character adds corroboration, and the rational orbit-space consequences are weaker than prior topology for translations and mechanically implied for the full group. No original substantive remainder of the frozen claim was found to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
