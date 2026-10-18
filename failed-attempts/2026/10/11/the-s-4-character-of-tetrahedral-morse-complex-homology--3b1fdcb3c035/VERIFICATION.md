---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Read the actual RESULT.md and detailed verifier code. The full simplex has 15 nonempty faces and 28 primitive Hasse pairs. The source enumerates 12,820 acyclic matching simplices with f=(28,300,1544,3932,4632,2128,256), gives an acyclic finite Morse matching with one critical 0-cell, two critical 3-cells, 101 critical 4-cells, and a unit 2x2 minor of the signed Morse boundary; this proves H4=Z^99 and no other reduced homology. Exact signed fixed-simplex traces by cycle type have Lefschetz sums (100,2,0,1,0), subtracting H0 gives (99,1,-1,0,-1). Independently recomputed the five alternating sums and rational S4 character inner products; multiplicities are 4,13,8,12,4. Published independent complete same theorem separately obtains these exact values. This verifies the stated finite rational homology action, not full equivariant homotopy or integral Specht lattices.

## originality

FAIL

Decisive direct duplication: previously published Resultary complete S4-character theorem studies EXACT full nonpure tetrahedral Morse matching complex, the same 28 Hasse edges, the same signed fixed-simplex formula, the identical five class traces, and the identical Specht decomposition. Its proof even offers an independent orbit-block enumeration. Thus the whole candidate is covered, not merely the nonequivariant 99-sphere homotopy statement in Scoville.

## value

FAIL

The S4 action on the 99-dimensional homology is a natural invariant and could be valuable if unknown, but this complete character and irreducible decomposition were already published and are reproduced without a new equivariant classification, algorithmic improvement, integral refinement or higher-dimensional result. No independent mathematical gap remains in the final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
