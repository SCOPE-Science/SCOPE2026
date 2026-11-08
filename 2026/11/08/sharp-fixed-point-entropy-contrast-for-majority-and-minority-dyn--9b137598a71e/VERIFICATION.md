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

The exact defining graph is hub \(h\), rim \(C_n\), and one private leaf per rim vertex. Two independently written ordinary Python checkers are included: `verify_direct.py` and `verify_symbolic.py`. Run `python verify_direct.py` and `python verify_symbolic.py` from this directory using Python 3 and SymPy for the symbolic checker. The saved terminal outputs `direct.log` and `symbolic.log` are embedded alongside the scripts.

The direct checker uses an explicit per-vertex neighbor list and exhaustively visits \(699008\) labelled configurations at lengths \(3\le n\le9\) for each update rule. It agrees with a separately encoded cyclic-word test at all seven lengths. The symbolic checker calculates characteristic polynomials of the weighted four-state matrices and exact rational saddle derivatives; it matches trace coefficients to independent run-composition formulas at all lengths \(3\le n\le54\). It also prints finite-length ratios to the asserted asymptotics for \(n\in\{50,51,100,101,200,201\}\). No timeout was interpreted as a mathematical exclusion.

The complete infinite-length correctness depends on the written local-reduction proof and elementary run counts, followed by primitive-matrix spectral theory and a Fourier local central limit argument. Finite tests and numerical ratios alone cannot certify these limits. One older methodological report was available only as an abstract and cover; it is an originality limitation, not evidence of an equivalence. Independent scientific audit has not been performed.
