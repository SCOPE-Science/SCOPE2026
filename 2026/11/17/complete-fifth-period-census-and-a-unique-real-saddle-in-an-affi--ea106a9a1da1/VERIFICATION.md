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
# Mathematical verification

The proof's exact finite algebra has been checked with the included `CHECK.py` using SymPy over the rational field. It recomputes five iterations of the recurrence, forms the lexicographic Gröbner basis of the two fixed-return equations, and asserts that the second basis element is precisely \(bQ_{15}(b)/1215\). The other basis element solves uniquely for the first coordinate as a rational polynomial in the second. It verifies square-freeness of the sixteenth-degree eliminant and exactly five real nonzero roots using Sturm root counts. Five rational intervals isolate them individually.

The checker then takes the real fifth-periodic point whose second coordinate lies between \(0.675684\) and \(0.675685\), refines its root interval to width below \(10^{-18}\), and evaluates the full fifth-return derivative using rational interval arithmetic. Its trace is strictly between \(-230\) and \(-220\), its determinant between \(-170\) and \(-150\), and the characteristic polynomial changes sign on both \((0,1)\) and \((-\infty,-1)\). Hence the orbit is hyperbolic with one contracting and one expanding tangent multiplier. The extra zero multiplier follows from exact one-step collapse onto the invariant surface.

To replay: install the dependencies in `requirements.txt`, then run `python3 CHECK.py`. The script prints `FIFTH_PERIOD_UNIQUE_REAL_SADDLE_EXACT_OK` only after all exact tests succeed. This is a reproducible mathematical computation, not a substitute for independent review of the proof or a general classification of higher-period points.
