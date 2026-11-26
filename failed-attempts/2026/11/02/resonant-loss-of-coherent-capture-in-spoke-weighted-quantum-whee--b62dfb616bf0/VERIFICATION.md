---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For J>0 and strictly positive local rates, the dark complement of the detector Krylov space is invariant and annihilated by the loss. An eigenvector of the graph evolution's effective Hamiltonian with a real eigenvalue must have zero amplitude at each detector by its loss expectation, so the bright restriction has strictly negative imaginary spectrum and decays even with Jordan blocks. The remaining trace is exactly the dark projector weight for any density matrix. The radial block eigenvalues are 1±√(1+na²), and the rim Fourier eigenvalues are c_k with pairs of multiplicity two except the even alternating endpoint. Counting multiples of n/gcd(n,2d) strictly below n/2 gives the displayed baseline. The two independent point evaluations on a merged radial/Fourier eigenspace have one row proportional to the other only at phase +1, while the total separated rank is already two at phase −1: the rank drops by one exactly outside the −1 case, including at the one-column endpoint. If there was no generic dark mode at even n=2s, then gcd(s,d)=1; phase −1 would force s|k, ruling it out at an interior collision. Odd n cannot have phase −1, and d=1 at the even endpoint works. The hub detector separates the radial vector at a collision, leaving one rim direction per distinct Fourier frequency plus two radial directions. The independently constructed algebraic Krylov ranks (python3 /workspace/review_evidence/reproduce.py 3) confirm generic, tuned and detuned cases, irrational squared tunings and all distances for the selected sizes. These finite checks are not the all-size proof.

## originality

FAIL

The main two-rim classification is already covered by an exact rank-preserving reduction to Resultary 5b3d49cda4e9, the distinct same-date weighted-wheel Laplacian two-leader theorem, together with the previously indexed adjacency collision spectrum (4f4cd11381f0). This is a coverage conclusion, not a claim that the same-date work appeared first. Adjacency and Laplacian are not the same operator and do not have the same resonance weights. Nonetheless their detector-restricted eigenspace decompositions match for every adjacency parameter after the explicit reparameterization below. The general asymptotic bright-projection relation is known; the hub-plus-rim rank is a direct two-block dimension count, not an independent surviving classification gap.

## value

FAIL

The absorbing-wheel model and design question are natural. However, the exact resonant rim-pair result is mechanically transferred from the matching rank classification, with its adjacency collision parameters separately known. The standard conversion from rank to mixed-state asymptotic capture and the immediate hub/rim count do not supply a substantive independent exact remainder; no new finite-time or parameter-sensitivity result is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
