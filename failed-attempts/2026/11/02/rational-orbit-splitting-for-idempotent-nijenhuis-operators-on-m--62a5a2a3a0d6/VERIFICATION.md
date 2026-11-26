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

FAIL

The orbit count, representatives, sizes and reduced incidence-bundle geometry check out, but the explicit split/nonsplit identification in the Assumptions and scope (line 39) is false. For the frozen u=a²+b, X=f+ah+be satisfies X²=u I and has characteristic polynomial T²−u. Its semisimple line is split exactly when u is a square, not when −u is a square. Over F_3, X=f+e has u=1 and two rational eigenlines, whereas −u=2 is nonsquare. This reverses the two arithmetic labels whenever −1 is nonsquare. The projector torsion separates into the two bracket-closure tests; the orthogonal line to a subalgebra plane is a nonzero nilpotent line, making the plane its kernel-line stabilizer. Borel conjugation sends (a,u) to (s+ta,t²u), giving the three fibre orbits and the global sizes stated. Complements form a locally trivial splitting torsor; the zero-discriminant locus is fibrewise a smooth affine line. The frozen finite output was read, not rerun, and does not validate the incorrect split label.

## originality

FAIL

The rational orbit spectrum and its geometric organization are already stated as a distinct exact result in Resultary 4c68434b0025: same identity, rank strata, sizes, square classes and affine-plane bundles. Its proof computes the same normalized stabilizer action. This is established equivalent catalogue coverage, not a claim that the other record was first or that the assigned record was derived from it. Complex splitting orbits also have genuine older equivalent coverage via weight-one Rota–Baxter operators. The assigned record does not isolate a useful distinct remainder beyond the identical census/geometry, and the incorrect split label is not a new result.

## value

PASS

As mathematics, a complete rational orbit stratification on a natural operator locus is a useful classification: knowing only the total or the geometric orbit does not tell how rational conjugacy splits or give its stabilizer sizes. This recognizes mathematical interest of the valid census, not an independent contribution over the exact overlapping record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
