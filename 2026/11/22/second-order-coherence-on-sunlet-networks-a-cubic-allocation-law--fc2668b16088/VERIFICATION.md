---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof derives the full Fourier-mode spectrum and exact first and second spectral inverse moments, establishes strict convexity and unrestricted uniqueness, then derives the optimizing cubic and proves one positive root. A positive-coefficient polynomial in \(n-3\) establishes strict separation of the two optimal allocations for every integer \(n\ge3\). Root scaling and substitution into the exact objective give the sharp asymptotic regret. These are analytical steps, not numerical extrapolations.

Run `python3 check_sunlet.py` with NumPy and SciPy. It independently constructs weighted sunlet Laplacians, computes their nonzero eigenvalues, checks trace identities and minimizers against numerical optimization and heterogeneous designs, and tests finite-size asymptotic convergence. It returned:

`PASS: 1009 finite analytical/numerical assertions`

`c=0.153242321348; m=3: (t2,t1)=0.7653298918,0.7302967433; m=4: 0.8992407105,0.8451542547`

Finite diagnostics alone do not prove claims over all integer sizes or all allocations. No independent mathematical validation or formal proof-system certification has been performed.
