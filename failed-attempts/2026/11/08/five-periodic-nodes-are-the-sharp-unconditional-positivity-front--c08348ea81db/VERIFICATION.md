---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS — The two-stage 4th-order Gauss-Legendre Padé end-step f(x)=(x²-6x+12)/(x²+6x+12) applied to cycle Laplacian is spectrally positive and mass-preserving. Exact kernels for n=3,4,5 are rational with nonnegative coefficient numerators; independent SymPy rational matrix calculation confirmed their positivity at representative h and their row sums. The all-n Green kernel G_{0,k}=(n²-1)/(12n)-k(n-k)/(2n), with zero row sums and LG=I-J/n, yields T=I-12G/h+O_n(h^-2). The adjacent coefficient is -(n-1)(n-5)/(nh), negative for all sufficiently large h when n>=6. Independent exact n6,h8 computation gives -6584/580537. This is a valid complete all-n proof rather than an extrapolation from examples.

## originality

FAIL

FAIL — Published 2026-10-13 full theorem on the SAME two-stage Gauss-Legendre [2/2] Padé update and unit cycles proves the identical all-size iff n<=5, exact same small-cycle rational kernels and -(n-1)(n-5)/(nh) adjacent asymptotic, plus the stronger exact six-cycle positivity threshold. Published 2026-10-25 independently reiterates this identical conclusion and six-cycle quartic. Exact change of notation Q=-L, R(-hL)=T makes the prior and submission mathematically identical; the h=8 witness is a corollary of the stronger old threshold.

## value

FAIL

FAIL — The mathematical classification is a known theorem, not a distinct valuable exact invariant. The added rational witness at h=8 and reproduced positive kernel identities do not extend earlier results; the October prior provides even the precise onset h_6≈6.36885. Technical correctness/reproducibility does not rescue value in a fully covered claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
