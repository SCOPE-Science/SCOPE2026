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

PASS: Independently constructed all 65,536 states for strict simultaneous five-neighbor majority on F₂⁴ Cayley graph generators {1,2,4,8,15}, rather than trusting saved output. Exhaustive direct six-iterate check found F^6=F^4, 142 fixed orbits, 1165 primitive 2-cycles, exact first-entry table {(0,1):142,(0,2):2330,(1,1):2616,(1,2):14720,(2,1):11264,(2,2):23680,(3,1):8864,(4,1):1920}, all maximal depth 4, and 140 singleton nonconstant fixed-point basins. Source verify_finite_dynamics.py and verify_independent_symmetry.py at actual Git blobs 6bf0fba6df172a8ec9b6d93faff44d76f4294f70 and 2ecd9ffff89471505d5bcd20b199c2f0d99dfda0 were read. The Cayley spectrum 5¹,1¹⁰,(-3)⁵ yields cut bound |∂U|≥k(16-k)/4; fixed-state cut |∂U|≤2k excludes minority k<8, forcing all 140 nonconstant fixed sign vectors into eigenvalue one As=s. The full automorphism group (F₂)⁴ ⋊ S5 has 1920 maps; the packaged independent generator action verifies 4 fixed and 10 two-cycle geometric classes. This is a genuinely exhaustive finite theorem, not extrapolation to other graphs.

## originality

PASS

PASS, best of knowledge: the classic Goles–Olivos period-at-most-two theorem does not enumerate fixed points, basins, or symmetries. The fully read four-cube Q4 prior census concerns degree-four tie-retaining majority (702 fixed, 885 two-cycles, 30 geometry classes), whereas the Clebsch graph has an added antipodal matching, degree five and strict tie-free update. An exact Clebsch majority census was not found in the relevant published-record comparisons.

## value

PASS

PASS: The Clebsch graph is a natural exceptional 16-vertex strongly regular graph (16,5,0,2). Exact recurrence, fourteen geometric orbit classes, four-update sharp cutoff and balanced isolated equilibria reveal structural behavior that differs sharply from the closely related four-cube. A natural finite classification with complete proof certificate has independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
