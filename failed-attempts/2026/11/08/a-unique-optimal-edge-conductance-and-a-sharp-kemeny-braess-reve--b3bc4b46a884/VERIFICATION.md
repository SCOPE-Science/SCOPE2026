---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The transition matrix invariant classes E (two selected endpoints), R (remaining a-2 first-part vertices) and B (opposite part) give a three-by-three equitable quotient, antisymmetric mode eigenvalue -w/(b+w), and n-4 zero eigenvalues. The spectral sum yields K_{a,b}(w)-K_{a,b}(0)=w[4(a-2)w-3b]/(2(b+2w)(ab+w)), so sign reverses at w=3b/[4(a-2)]. With x=w/b, independent symbolic differentiation gives the stated polynomial (8a^2-12a-2)x^2+8a(a-2)x-3a, which has one positive root for integer a>=3; the derivative is negative before and positive after. The proof handles b=1 and nonlazy bipartite periodicity. This matches an earlier all-parameter exact derivation; finite matrix checks in the package are supporting, not an all-integer proof.

## originality

FAIL

Decisive full-text prior: published November 2 theorem "Optimal conductance and a sharp Kemeny benefit bound for one link in a biclique" proves the exact identical rational Delta formula, normalized b scaling, unique optimum quadratic, and Braess zero-crossing, on the broader domain a>=2. It further gives the universal improvement bound -1/6 and balanced-biclique asymptotics. The submitted a>=3 claim is directly subsumed, irrespective of whether its wording advertises uniqueness as new.

## value

FAIL

A conductance-dependent improvement/harm threshold is meaningful as network design mathematics, but the exact graph-class result, optimum, and sign cut were already proved with stronger scope (including a=2 and a sharp benefit bound). Merely repeating the covered subfamily offers no distinct original valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
