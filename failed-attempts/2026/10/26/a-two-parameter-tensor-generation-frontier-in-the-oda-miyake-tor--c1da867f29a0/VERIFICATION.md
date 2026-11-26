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

The fan is the b=2,c=a+2 specialization of Construction 6.1; the canonical orbit-closure criterion applies over any field. The four ±1 first-coordinate rays are strict vertices, and the four remaining ray tests reduce to the balanced x=0 sections with coordinates h=y−z and g=y+z. For |k|≤1 the indicated support lines meet only the edge containing the target, preserving both edge endpoints as vertices. For k≥2 the first convex certificate with t=4/(k+2) places v₃ in the hull of its other neighbors if 2a+k+2≤0; the second places v₇ in that hull at its own ray if 2a+k+4≥0. The alternatives exhaust all a and include t=1. For the negative wing the counterpart certificates use t=4/(2−k) at h=1, or follow by the lattice map (x,y,z)↦(x,x−y,2x−z). The four variable wall degrees are 2a+k+2, 3−k, k+3 and −2a−k−4, by expressing the sum of the opposite rays in the wall basis and subtracting the coefficient sum from 2. The other fourteen are nonzero constants. Thus in the central band the only wall exclusions are (k,a)=(0,−1),(0,−2), and in the stated a=0 wings all wall degrees are nonzero despite a divisor obstruction. The secondary script was inspected but not executed.

## originality

FAIL

The claimed novelty of the negative k=−1 family is disproved by an explicit lattice isomorphism to the published k=1 family. More decisively, Resultary 838005eaafd0 computes the per-ray obstructions and the complete wall table for the four-parameter family. Substitution immediately recovers the entire complementary |k|≥2 obstruction and the wall-invisible examples. That record states algebraically closed characteristic zero; applying its same field-independent fan tests to the any-field criterion of Ito–Zeng–Zeng requires no new characteristic argument. This is a coverage and distinctness decision, not an attribution of priority: the broader entry itself refers to a previous computation on this exact slice.

## value

FAIL

The proposed slice and its divisor-versus-wall distinction are mathematically motivated, but the submitted exact claims reduce to an isomorphism and simple evaluations of already explicit four-parameter ray and wall tests. Neither presenting convex witnesses for those same inequalities nor restating the field-independent outcome supplies a distinct exact invariant or new class of obstructions. No separate valuable remainder was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
