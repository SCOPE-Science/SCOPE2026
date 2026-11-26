---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The repaired local theorem has a complete proof. With z=u/K-1, positivity is preserved and the predator obeys v_m<=q^m v_0. The two-step boundary map preserves sign, decreases magnitude by at least a constant times |z|^3, and differs from the exact two-step prey update by O(q^(2m)v_0) at even indices. Taking the total forcing smaller than the trapping margin and summing the inequality proves small-data convergence. The repaired weighted inverse equation d_m=f^(-1)(z_{m+1}+d_{m+1})-z_m has contraction constant Lq<1 and invariant ball radius L C_2 v_0/(1-Lq) in sup_m q^(-m)|d_m|; one chooses a strict inverse-domain margin. Its solution supplies the exact boundary orbit with O(q^m v_0) discrepancy. The locally analytic full map has determinant -q at the equilibrium; the strong-stable theorem for the strict spectral gap supplies a C^3 graph tangent to the contracting eigenline with nonzero v component. Zero boundary phase gives fast convergence, and nonzero phase cannot converge exponentially. Independently expanding f=-z+(2/3)z^3-(2/3)z^4+(2/5)z^5-(8/45)z^6+O(z^7) and composing gives the return coefficients -4/3, zero, 8/15, 4/9 at degrees three through six. Thus w=z_even^(-2) has increment 8/3+64/(15w)+O(w^(-3/2)); first w~8m/3, then w=8m/3+O(log m), so subtracting the harmonic term leaves an absolutely summable remainder and yields (8/5)log m and a finite constant. The exponential discrepancy changes the inverse-square values by O(q^(2m)m^(3/2)), which tends to zero and preserves the eventual sign. Expanding the full exponent and imposing graph invariance yields (1+q)h_1=-p and (1+q^2)h_2=p^2/2+h_1[2k+p(1+theta)+q eta]; the k-derivative is strictly negative. This checks fixed q in (0,1), including k=0, not q=1 or a global basin. Read, but did not execute, the supplied symbolic and finite trajectory diagnostics. The complete corrected RESULT.md and SLOGAN.txt are under repairs/5.

## originality

PASS

Pass for the narrowed statement, not for priority of the scalar clock. The earlier symmetric Ricker record's scalar map is exactly conjugate by s=2z, and its 2/3 and 2/5 clock constants become precisely 8/3 and 8/5; the proof's exponential shadowing scheme is also prior. The repaired claim explicitly treats these as inputs or background. The map-specific contribution is the all-nearby-data positive-predator extension and the explicit, fear-dependent fast-recovery curve in the original coordinates, not a new scalar critical invariant or general stable-foliation theorem.

## value

PASS

The neutral prey multiplier does not distinguish exceptional fast recovery from decay on the two neighboring slow sides. In the stated fear map, the exact quadratic locus is a useful quantitative local invariant: it reveals a change with fear strength invisible both to the linearization and to the universal scalar coefficients. The proof shows that those coefficients actually govern the original prey density under nonzero predator forcing off that locus. The novel value is the distinction and explicit geometry for this model, not a relabelled scalar logarithm or a global ecological forecast.

The dated certificate retains the supplied scientific assessment, sources and limitations.
