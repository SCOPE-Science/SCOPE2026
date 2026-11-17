---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For N=2p,p>=2 and q-th roots window with time shifts {0,1} and even frequency modulations, the frame operator splits exactly into p two-dimensional Fourier fibers. With c_r=x_r-x_(r+p), the fiber spectrum is 1±|cos(pi k_r/q)| where k_0=c_0+c_(p-1) and k_r=c_r-c_(r-1). This integer transformation has determinant two: mod odd q its image is all (Z/q)^p, mod even q exactly the even-sum parity code, each with kernel size two. Thus for any threshold a, the exact survival count is h(a)^p for q odd or h(a)^p+d(a)^p for q even, divided by q^p, where h counts allowed fiber residues and d is even minus odd allowed counts. The basis probability, optimal lower bound and exact numbers of optimizers follow by optimizing min distance of k_r from {0,q}, with the q mod 4, p parity branches. Independent exhaustive enumeration of all ratio vectors q=2..7,p=2..5 (bounded total <=200000), 16 survival-threshold comparisons and four full complex Gabor matrix eigenvalue checks verify the formulas, without extrapolating finite evidence to arbitrary p,q.

## originality

PASS

Qualified nonredundant finite-phase lower-frame-bound survival law and exact nonorthogonal optimum-count classification. The general fiber decomposition, continuous Steinhaus spectrum, and orthonormal existence/count are already known and specifically not credited as new.

## value

PASS

Two-translation even-modulation cyclic Gabor systems form a natural minimal critical measurement design. Quantizing the phase alphabet makes determinant-two fibers dependent by an explicit parity code; the exact finite-dimensional probability of each lower bound, sharp nonorthogonal attainable optimum and counts have direct meaning for discrete phase design and conditioning. The known orthonormal and continuous-phase pieces are excluded from claimed value, leaving a motivated exact discrete invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
