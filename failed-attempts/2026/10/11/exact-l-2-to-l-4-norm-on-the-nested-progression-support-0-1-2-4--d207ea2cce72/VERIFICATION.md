---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Parseval on P² yields an exact sum of collision fibers, the only two nontrivial midpoint collisions being b²+2ac and c²+2ad. Triangle alignment shows all positive coefficient magnitudes attain the quartic envelope H=2−Σx_j⁴+4xzy²+4xwz² on Σx_j²=1. Boundary faces obey H≤15/7, while equal magnitudes yield H=9/4, forcing an interior maximizer. The stationary polynomial system is represented in the inspected exact SymPy Gröbner-elimination code. Its resultant forces the ninth-degree delta polynomial; Descartes one sign change and Q(0)<0<Q(1) give one positive root. Independent SymPy root isolation gives delta~0.29941386284032834, C~1.231414565773106. Separately published complete real-parameter dual-quadratic proof for exact same support and constant supplies a second analytic correctness verification; numerical root by itself not proof of elimination.

## originality

FAIL

Decisive separate published prior covers the exact original in full: Sharp fourth moments for linked-midpoint four-character spectra establishes K=2.299413862840329... on every compact abelian G with a character of order >=9 or infinity, for arbitrary four complex coefficients on {0,1,2,4}, and all equality classes. Choosing G=T and chi(z)=z yields exactly this sharp circle L2→L4 norm, not merely similar numerical parameters. Its full proof was read, including two-collision envelope, global negative-definite dual certificate and equalities. Thus this assigned finding is a strictly covered special case.

## value

FAIL

The exact sparse-four-frequency fourth moment is mathematically natural and correct, but the assigned deliverable is an already published strict special case of a theorem proving the SAME sharp value and all extremizers over a broader class of groups. Merely reparameterizing the algebraic constant as a ninth-degree delta root creates no new usable invariant, motivated obstruction or independent fact beyond the stronger covering result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
