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

Eliminating the last two equations gives y=5x/D, z=x(rho+x)/D; for x≠0, D=0 is incompatible with solvability, and a quartic root cannot have D=0. The scalar first equation is -xF/D². The independent rational check /workspace/review-evidence/2/check.py regenerates the discriminant and subresultant, isolates the two negative zeros, and counts 4,2,0 quartic roots at -3,-3/2,-1. Constant leading coefficient 8 and absence of other discriminant zeros extend those counts on the open intervals. The degree-one gcd at each fold gives one double root and no other multiple root. At -sqrt(5) the quartic's zero root is replaced by the distinct axial equilibrium (0,5,-sqrt(5)); at tau it is a simple root representing only the origin. The new check certifies the fold abscissae and F_rho, F_xx, c2 enclosures: roughly (0.620901,-38.654,-41.766,-31.314) and (0.103167,32.087,17.817,13.778). Smooth elimination, a simple zero eigenvalue and nonzero scalar unfolding/curvature give genuine flow saddle-nodes; trace -8 and c2 supply the transverse signs. Independent nullspace projection reproduces both nonzero center coefficients at tau in the stated normalization. This is a proof of the equilibrium census and local events, not a global attractor classification. The packaged checker was inspected, not executed.

## originality

FAIL

The mathematical classification is sound, but the original claim that the negative range is previously unclassified is materially overstated. A distinct earlier-dated Resultary result proves the same upper negative fold and generic transcritical event, the counts between and above them, and isolates both negative discriminant roots. This is actual coverage, not just a similar title or a coincident polynomial. Completion of the far-negative census and some local coefficients are additions relative to that comparison, not a reason to pass the broad frozen novelty claim. A later-dated record gives equivalent full counts and the same exceptional axial case; this is separate evidence of overlap, not evidence of earlier priority. No replacement is submitted: the remaining coefficient and enclosure differences to the full-census comparison do not provide a separately motivated result.

## value

PASS

A full real-equilibrium census on the missing far-negative portion of a natural one-parameter benchmark is useful: it shows where extra states appear, handles the singular elimination at -sqrt(5), and distinguishes a mixed-transverse fold from one with stable transverse dynamics. This is meaningful independently of numerical trajectories; extra digits alone would not be valuable. This does not remove the originality failure for the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
