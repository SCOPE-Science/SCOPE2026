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

The analytic derivation uses translation-sector simple-energy separation, the exceptional zero-energy sector on even rings, and exact Fourier-edge amplitudes. It verifies the loss-free kernel and deduces eventual jump probability from contractive non-Hermitian evolution.

To replay finite corroboration from the packaged artifacts, run `python verify_rank.py` (Python 3 standard library) and `OPENBLAS_NUM_THREADS=1 python verify_projector.py` (Python 3 with NumPy). Both programs should terminate with `PASS`; the captured original stdout files are `rank.log` and `projector.log`.

The first program checks modular observability ranks for \(3\le n\le16\) over two primes. The second program checks nonuniform-loss spectral projectors, orthogonality and the full distance-resolved capture table for \(3\le n\le14\). These finite verifications do not replace the all-size proof or establish independent scientific validation. The scope excludes coherent interactions, flux, finite-time decay rates and missing loss channels.
