---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Under the stipulated fixed panel, condition first on Z. The one- and two-assay within-primary conditional means are f and f^2 in the unoccupied class, and g=f+theta(p-f) and h=f^2+theta(p^2-f^2) in the occupied class. Cross-primary products factor in each class. Thus C-A^2=psi(1-psi)theta^2(p-f)^2 and D-AB=(p+f)(C-A^2); the two ordered roots, positive T=A-f, and those identities recover every parameter. Inclusion-exclusion on the eight cells proves equivalence of the interior feasibility criterion with the stated equal-marginal/exchangeability constraints. An independent exact forward-Jacobian determinant in the stated parameter order is psi^2 theta^4(p-f)^6(psi-1); the four example moments also agree. A single primary reveals only psi theta; one read per primary reveals only psi, f and g, hence exact continuous aliases with theta(p-f) unchanged. These exhaust fixed allocations with at most three binary assays drawn as stated. The uniqueness of the allocation is for a repeated fixed panel, not for recorded heterogeneous panels: for example, three distinct primaries on some sites give psi,f,g by the ordinary three-repeat binary mixture, and a within-primary pair on other sites then determines p from B=f^2+(A-f)(p+f). This is outside the fixed-panel theorem. Inspected the attached checker without executing it; it tests the discriminant against the generating contrast and then uses the known positive contrast in rational replay. This is not a blind inverse from arbitrary laws or a finite-sample performance test.

## originality

FAIL

The central identification and square-root reconstruction are a strict positive-rank instance of the published binary tripod, not merely analogous to it. Collapse the unobserved path from U1 to Y by conditioning on U1 itself. The remaining ecological inversion, fixed-panel exclusions, feasibility bookkeeping, and forward determinant are direct substitutions or differentiation. The frozen comparison misses this antecedent for the very same observable law and its inversion. No claim that the older tripod paper labels this ecological panel or parameterization is needed.

## value

FAIL

The assay allocation is a clear teaching or design example for a well-specified problem, but the scientific increment after removing the covered tripod inversion is routine exclusion of the other fixed partitions plus differentiation and cell bookkeeping. The determinant displays possible singularity, not a new optimality, sampling-precision or robust calibration guarantee. No independently valuable, nonroutine remainder was established to repair as a finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
