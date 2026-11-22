---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For n>=6, the equivariant simplicial map replacing vertices 3 and n-2 by 1 and n respectively is contiguous to the identity and retracts onto the induced subcomplex deleting 3,n-2; for n=6 the two substitutions agree with distinct endpoints and remain valid. The residual graph is P2 disjoint union P_(n-6) disjoint union P2, so its independence complex is a three-factor join. Reversal interchanges the outer two S0 factors, which is the unit sphere of the swap R_+ plus R_- representation; the central factor carries shorter path reversal. Base cases n=1..5 supply the fixed/antipodal representation directions and contractible cases, giving the six-periodic a_n,b_n table and the equivariant homotopy classification. Passing to ordinary orbit spaces yields S^(a-1)*RP^(b-1), and integral projective homology gives first H3=Z/2 at n14 and arbitrarily many two-torsion degrees. Independent full-face quotient Euler checks for n<=16 agreed with representation prediction; Euler alone would not certify torsion, which follows from the structural equivariant map and projective cellular chains.

## originality

PASS

The 2026 path-reversal orientation theorem computes reversal sign on rank-one top integral homology and hence rational quotient homology, but explicitly not equivariant homotopy or integral quotient torsion; the full relevant RESULT.md was inspected. The 2026 reflection-fixed higher-path theorem computes geometric fixed loci, a different construction from orbit spaces. A projective-suspension cycle/half-turn result has a different underlying complex, with no known equivariant equivalence to these path independence complexes. Ehrenborg–Hetyei describe ordinary path independence homotopy only. Thus the all-n integral orbit quotient classification is new relative to inspected sources.

## value

PASS

The equivariant six-step graph fold determines all ordinary quotient homotopy types and detects unbounded integral two-torsion that is invisible to the known homology orientation character and rational quotients. This is a motivated strong refinement of natural path symmetry, not an arbitrary low-order torsion example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
