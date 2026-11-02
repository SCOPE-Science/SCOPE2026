---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The all-dimensional statement C_tr(F diag(p) F†)=sum |p_k-1/d| is proved correctly by a cyclic twirl and Fourier diagonalization for every d>=2 and boundary spectrum. However the same final claim asserts a qutrit formula 4r max_k |cos(theta+2pi*k/3)| without imposing r>=0, while positivity permits negative r. Explicit exact counterexample r=-1/12, theta=0 gives eigenvalues 1/6,5/12,5/12, real positive density, trace coherence 1/3, and claimed right side -1/3. Hence one final claim containing that assertion is false as stated.

## originality

FAIL

A January 2026 primary paper establishes precisely the two nontrivial symmetry premises (circulant rho is fixed by the uniform cyclic quantum channel; every incoherent diagonal delta is sent to I/d). Standard CPTP trace-norm contractivity and Fourier diagonalization then give the entire all-dimensional formula as an immediate corollary. Explicit formula not printed verbatim does not confer novelty. The qutrit formula also has a sign defect at permitted negative r. Other special classes and the Resultary qutrit Schatten work are not the decisive source.

## value

FAIL

The full circulant state simplex and trace-coherence measure are natural. Nevertheless, the only valid principal equation follows immediately from Xie-Zhang 2026 Eq.3.2 and Corollaries 3.6/4.2 plus standard CPTP trace-norm contractivity and elementary Fourier diagonalization. The qutrit clause is a direct three-number zero-sum simplification with an omitted sign assumption. It determines no genuinely unknown natural invariant beyond the established universal channel projection, and offers no separately motivated new structural boundary or result; correct reproducible instances alone would not confer independent research value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
