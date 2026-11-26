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

On the lifted strip, recursively integrate the top edge increments and add the rung increments to obtain a bottom height. The square identities give the bottom-edge increments, so a deck translation adds H_n on either rail. A closed walk of degree w therefore integrates to wH_n and has length at least n|w|, while the rails achieve the stated maximal cycle mean. The exact activity theorem of Gravner, Lyu and Sivakoff then applies per vertex. Checking the color pairs gives δ=3g+df with the stated f, so GHM excitation (0→1) uses one third the CCA circulation. Zero activity on a finite eventual cycle implies a constant CCA state on the connected prism or the all-rest GHM state. The transfer trace counts labelled rung strings once, and H_n is divisible by three. Independent symbolic reconstruction decomposes the transfer into the three simultaneous color-shift sectors and verifies the full unweighted characteristic polynomial, the invariant tilted block and its characteristic polynomial, and the stated variance; replay: python /workspace/audit_evidence/reconstruct.py (prism_blocks). At z=1 each row and column has at least six ones, proving positivity of T(1)². The simple analytic Perron branch and the spectral gap give the CLT from the characteristic-function trace ratio. Peripheral equality requires an edge phase coboundary: self-loops force the constant phase to one, and the diagonal-rung color cycle of length three forces e^{3it}=1. Conversely those three points are gauge-conjugate, with identical positive leading Gaussian contributions. Spectral gap elsewhere and bounded small-neighborhood domination give the local-limit constant, including its factor three.

## originality

FAIL

The October 26 circular-prism extinction record is a verified exact overlap, not a keyword or numerical match. Its flatness mask and tilted 9-state transfer already encode the entire conditioned winding distribution, up to a diagonal gauge and the lattice scaling by three. It gives the same unweighted characteristic polynomial, exact extinction count, analytic dominant-eigenvalue expansion and the same Fourier Gaussian coefficient. The additional conditioned Gaussian statement follows directly from its analytic trace expansion. The rate formulas on the conditioned class are direct applications of the prior general cycle-mean theorem to the one rim circulation already identified in the prior prism proof. The explicit smaller block is a different derivation, not an independently distinct claim of the Finding.

## value

FAIL

The local-flatness versus global-winding distinction is mathematically meaningful, but this Finding mainly repackages an available winding generator and its calculated Perron curvature. Conditioning amounts to dividing by the unweighted trace, and the change in lattice spacing and rates is a normalization. The useful 3×3 block provides a compact derivation but does not by itself deliver a substantively different scientific invariant or phenomenon in this Finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
