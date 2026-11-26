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

Strict concavity makes consecutive sample chords the upper boundary; each chord omits gap³/6 in one quadrant. The polar constraints indexed by a,b meet at w(a,b), where the slack for t is (t−a)(t−b)/(1+ab), so exactly the adjacent intersections give the quadrant boundary chain. The cut-off triangle at insertion has determinant magnitude (a−b)(a−c)(c−b)/D, reproduced independently (python /workspace/audit_checks/reconstruct.py 4); four triangles with the 1/2 area factor give q/D. The new primal is contained in the full parabolic lens and the old polar contains the disk: hence the claimed positive exchange lower bound. The full lens polar is found by maximizing tu+(1−t²)v on [0,1]; u_max is 1 up to v=1/2 and 2√(v(1−v)) thereafter. Thus the full polar area is 2+π/2. All bodies contain the fixed diamond, which justifies polar continuity for finite refinements and infinite prefixes with 0 adjoined. Strictness at the upper endpoint follows by one additional insertion in a positive gap before passing to the full lens; at the lower endpoint compare to the diamond or a finite three-knot subset. For a_n=r^n the interior knots are confined to [0,r] as r→0 and the maximum gap is 1−r as r→1, proving sharpness within the infinite class. Uploaded clipping code inspected, not executed; finite rational checks are not the proof.

## originality

PASS

Pass for the exact coupled area exchange and strict refinement envelope for this parabolic mesh. The underlying bodies, classical lower value and full sample limit's numerical product are prior, not claims to new credit. The strongest overlapping indexed statements do not give every-insertion strict growth or the exact local polar loss.

## value

PASS

A coupled exact exchange for primal and dual areas turns a natural refinement of an established convex-body family into a strict law for a functional not generally monotone under inclusion. The local quantitative sign, the sharp global envelope and the infinite-family endpoint tests are useful structural information independently of the already known endpoint values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
