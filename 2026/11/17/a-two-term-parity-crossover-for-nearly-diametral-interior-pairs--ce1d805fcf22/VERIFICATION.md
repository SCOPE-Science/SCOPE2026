---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. For normalized interior-area points and δ=2π/n, the exact polygon polar boundary r(u)=cos(δ/2)/cos[δ({u}−1/2)] gives (1−r)/δ²=h(u)+δ²k(u)+O(δ⁴), confirmed independently from the cosine series. On D>2−δ²t, radial deficits z1,z2≤t and angular offset w is bounded by an O_T(1) constant; thus the distance Taylor remainder is uniform on a compact localization box, not asserted globally. The exact cosine law yields the defect S+w²/4−δ²[Sw²/8+w⁴/192]+O_T(δ⁴); at its leading boundary S=t−w²/4 the correction becomes tw²/8−5w⁴/192. Integrating the radial two-simplex with Jacobian (1−δ²(H+s1+s2)) gives (B²/2)+δ²[BQ−HB²/2−B³/3], and the exact angular normalization 2π²/A_n²=2+(2/3)δ²+O(δ⁴) yields Fσ+δ²Jσ+O_T(δ⁴). Uniformity at B=0 follows from the Lipschitz derivative of (x_+)². The even local diamond and the two odd minimizers of G give the respective 4/3 and 128/27 quartic onset constants, with exact odd threshold 1/16; the simple 0≤h≤1/8 comparison gives the 32/15 disk envelope. Compact measure convergence yields conditional four-dimensional volume uniformity, and barycentric slack gives Dirichlet(1,1,1). Independent SymPy expansion checked h and k and the exact defect coefficient; source script uses 4D deterministic Sobol/quadrature but is only bounded numerical corroboration, not an infinite proof. Scope excludes t growing with n and boundary-arclength sampling.

## originality

PASS

Best-of-knowledge PASS for explicit δ²Jσ and a uniform O_T(δ⁴) remainder and interior-area conditional four-dimensional law, not for polygon parity or the leading radial integral viewed in isolation. Full prior boundary-arclength theorem determines its Hσ, and the exact identity Fσ''(t)=2Hσ(4t), with zero initial conditions, already determines the leading Fσ. Bäsel's exact fixed-n interior distance law determines every finite-n probability and in principle its asymptotic consequences, so a previous explicit uniform expansion could cover the claim; the inspected main theorem does not formulate this scaling or its conditional law. Search cannot establish historical uniqueness.

## value

PASS

PASS. Exact quantitative finite-side corrections at a singular parity-dependent diameter endpoint, together with the conditional geometric distribution and sharp odd/no-threshold dichotomy, answer a natural random-point geometry question beyond the already-covered leading boundary chord law. The uniform O_T(δ⁴) control is needed to distinguish finite-polygon probabilities with the same disk limit; the Dirichlet shares reveal a robust four-dimensional geometry. The finite-n distribution existing in the literature does not by itself make the nontrivial uniform second term an arbitrary table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
