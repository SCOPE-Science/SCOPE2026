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

# Exact verification details

The standalone `verify_gauss_multipartite.py` requires Python and SymPy; run `python verify_gauss_multipartite.py` in the directory containing the file. The recorded output is `verification_output.txt`. It asserts coefficientwise nonnegativity of the monotonicity certificate and Padé order matching at stages 1 through 28, compares the analytic graph spectral formula with direct rational matrix functional calculus for seven graph configurations, stages 1 through 6 and three stepsizes, checks stochastic row sums and offdiagonal signs, tests odd-stage large-step diagonal loss, and checks the two-vertex case. The actual run passed 741 exact assertions.

The all-stage universal proof does **not** derive from tests of finitely many stages or graphs. Its critical arguments are the symbolic coefficient-pair inequality for the entire Padé family and a remainder identity obtained from repeated integration by parts, together with a complete symbolic Laplacian spectral resolution. The verification does not assess independent mathematical validation, arbitrary weighted/directed graphs or internal Runge–Kutta stage positivity.
