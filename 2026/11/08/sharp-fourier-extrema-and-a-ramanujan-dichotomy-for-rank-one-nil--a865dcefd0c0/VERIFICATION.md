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
# Reproducibility and verification

The standalone file `check_nilpotent_graph.py` requires only Python 3 standard-library modules. Running `python check_nilpotent_graph.py` enumerates the connection set via all nonzero pairs \((u,v)\) with \(v^Tu=0\), eliminates duplicate rank-one matrices, enumerates all characters modulo scalar frequency shifts, and compares their complex Fourier sums with the integer eigenline formula. The tested pairs are \((n,q)=(2,2),(2,3),(2,5),(3,2)\).

The verified output includes the complete spectra:

- \((2,2)\): \(3^1,1^3,(-1)^3,(-3)^1\).
- \((2,3)\): \(8^1,2^{12},(-1)^8,(-4)^6\).
- \((2,5)\): \(24^1,4^{60},(-1)^{24},(-6)^{40}\).
- \((3,2)\): \(21^1,9^{28},5^{21},1^{84},(-3)^{98},(-7)^{24}\).

The program terminates with `NILPOTENT_CAYLEY_FOURIER_CHECKS_OK`. These checks test all finite Fourier coefficients for the specified cases, but do not exhaust all dimensions or nonprime fields. The general theorem is established in RESULT.md by exact character orthogonality, projective-eigenline inequalities, conjugacy counts, and a uniform Ramanujan comparison. Independent mathematical audit has not been performed.
