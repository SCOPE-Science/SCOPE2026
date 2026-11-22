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
# Arithmetic verification and limits

Run `python3 verify.py` from the directory containing `verify.py`; it uses only Python's standard library.

The exact Fraction-powered truncated Taylor calculation confirms
\[
R(f(t),t)-f(f(t))=-\frac{t^7}{27}+\frac{13t^9}{162}+O(t^{11})
\]
and
\[
(1-v/3+v^2/9)^{-2}-1=\frac23v+\frac19v^2+O(v^3).
\]
Four numerical diagnostics use strictly positive initial pairs \((1,1)\), \((1.5,0.5)\), \((0.01,0.025)\) and \((3,7)\) with \(10^6\) iterations each. The script reports the centered inverse-square residual at two iteration counts, the leading amplitude and the lag-difference amplitude. At \(10^6\) steps, the first initial pair gives a residual approximately \(1.13125944\), leading amplitude \(1.22474172\) and lag-difference amplitude \(-0.61236832\); these are finite diagnostics, not numerical proofs of the limits.

The infinite-orbit proof rests on positivity, a two-step contraction, a normalized fifth-order graph error and a summable inverse-square recurrence. The checked jet identities are only local coefficients. No finite computation certifies all iterations, global non-synchronous basins or novelty.
