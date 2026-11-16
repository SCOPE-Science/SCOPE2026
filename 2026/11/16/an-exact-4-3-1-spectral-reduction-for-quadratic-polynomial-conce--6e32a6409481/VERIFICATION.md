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

# Reproducibility
The analytic certificate is the complete representation/moment proof in `RESULT.md`. In particular, the \(\binom{d+2}{2}\)-dimensional polynomial space decomposes into a four-dimensional trivial multiplicity space, a three-dimensional standard multiplicity space, and an irreducible edge kernel with the stated multiplicities. All matrix entries are finite combinations of explicit gamma moments; no unknown spectral data are inputs.

Run `python verify.py` after installing NumPy. It implements the full monomial Gram pencil separately from the invariant block pencils, then compares sorted spectra in every integer dimension from four through eight, the exact edge eigenvalue and the trace identity. The run passed in the construction environment for polynomial-space dimensions 15, 21, 28, 36 and 45. For dimension four it gave extremal eigenvalues approximately \(0.0000793986560408\) and \(0.483477188673\). The script has no external file or network dependencies. These finite computations are corroboration, not a proof for all dimensions.

Limits: no independent assessment has been performed, and priority comparisons cannot guarantee that every historical specialist formula is indexed.
