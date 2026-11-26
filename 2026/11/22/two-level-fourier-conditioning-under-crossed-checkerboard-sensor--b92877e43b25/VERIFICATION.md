---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reassessed the corrected claim. The original roots-of-unity factorization pairs simultaneous half-period frequency shifts; the single half-shift cases vanish because the corresponding sine is evaluated at zero. An independent row-side check: set j=2p+a, k=2q+b, m=m₀+u M/2, n=n₀+v N/2 with a,b,u,v binary. A DFT in p,q separates base frequencies (m₀,n₀). After removing unimodular row factors each block has entry exp(iπ[u(a+δ(−1)^b)+v(b+ε(−1)^a)])/2. Its row Gram has diagonal one; rows differing in just one parity have inner product zero (a factor 1+exp(iπ) vanishes); rows differing in both have Gram-entry modulus |sin(πδ) sin(πε)|. Consequently each block has two copies of 1−s and two copies of 1+s, which proves the repaired multiplicities even for both grid sizes two. At s=0 the spectrum consists of one distinct value and A is unitary; at s=1 half the eigenvalues vanish. The frequency-side H is a weighted matching with H²=s²I, giving the stated inverse and sharp norm when s<1. Expanding each parity phase into cosine and parity-weighted sine gives four rectangular transforms for the adjoint and the stated complexity. Replay via these block calculations and corrected RESULT.md 23–47. The supplied checker, inspected but not run, compares the full Gram matrix and tests H² for the predicted H, not a numerical proof of exact frame bounds.

## originality

PASS

The exact crossed two-coordinate product-of-sines dependence and frequency pairing survive the correction; two-band spectra and periodic block Fourier reductions in general are not claimed new. None of the inspected distinct records or primary results covers the crossed-grid statement.

## value

PASS

The corrected formula is an all-size sharp nonperturbative conditioning benchmark. One-coordinate stagger alone may have zero loss, whereas two coupled offsets cause a sharp and exactly quantified rank transition. The inverse by four standard FFTs and an explicit frequency pairing gives the result computational relevance for this sampling model, without claims about arbitrary jitter, partial bandwidth or odd dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
