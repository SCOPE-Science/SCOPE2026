---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At the integer critical lattice the Zak images of the atoms in each channel are one Zak window times the Fourier characters of the unit square. Parseval gives a multiplication symbol equal to the sum of squared absolute Zak windows, with duplicates counted separately. For u=(x−s_j) mod 1 the hat has Zak modulus squared 1−4u(1−u)sin²(πν), so all channels simultaneously attain B=r at ν=0 and the pointwise minimum over ν occurs at ν=1/2. Continuity makes these essential extrema; the latter symbol is the stated F and its terms vanish jointly exactly for one residue. On each lifted support gap F has second derivative 8r; integrating at the midpoint gives h_iF(z_i)+(r/3)h_i³. The integral over the circle is r/3, and Σh_i=1 gives Σh_i³−k^(−2)=Σ(h_i−1/k)²(h_i+2/k). Equality in the stated defect requires equal gaps and every midpoint globally minimizing. Then F=A+4r(x−z_i)² on each gap, so the jump at a site is −8r/k, whereas the kinks of the individual summands give −8m_i at multiplicity m_i. Conversely equal gaps and multiplicities give equal site values by rotation, so the equal-curvature arcs have their common minimum at the midpoints. This also checks k=1, A=0, and the sharp distinct-site bound.

## originality

FAIL

A prior Resultary result gives the exact same gap quadrature and the exact same cubic factorization for the same circle potential after a change of signs and scale. In --ed3ad9071b26, let R(t)={t}(1−{t}) and V=R*ν. For ν=r^(−1)Σ_j δ_{s_j}, the submitted Zak potential is F=r(1−4V), so A=r(1−4 max V). Multiplying the prior §2 identity max V−1/6=(Σh_i³)/12+Σh_i(max V−V(z_i)) by 4r and subtracting r/(3k²) gives the frozen result, using the same factorization printed in prior §4. The prior statement uses distinct equal masses, but its proof uses only total probability mass for the mean and for V''=−2 off support; both facts are unchanged with arbitrary empirical repetitions and with one or two sites. The equality refinement uses the atomic jumps already read off from the prior distributional V''=2ν−2 dt. Thus the full claimed defect is a direct prior implication after standard Zak diagonalization, not merely an analogy between Sobolev and Gabor problems.

## value

FAIL

The sharp lower frame bound and sensitivity to clustering are motivated quantities, and the formula can be convenient in that notation. But the gap and midpoint structure is already exactly present in the earlier potential result. The Zak change of variables, retaining multiplicity in a probability measure, and reading its atomic derivative jumps are routine; the submission does not solve an independent weighted placement problem, for example the sharp attainable optimum when k does not divide r. The claimed exact invariant therefore adds no distinct nonmechanical value at the submitted scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
