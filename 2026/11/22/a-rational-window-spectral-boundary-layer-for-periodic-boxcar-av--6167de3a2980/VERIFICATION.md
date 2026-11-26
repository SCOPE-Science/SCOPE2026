---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Fourier integration gives the sinc multiplier and a factor of two for ±n; the strict threshold counts no zero modes. At fixed width the empirical phases are uniform on the irrational orbit or uniform on the rational residues. Applying this on macroscopic frequency blocks in u=pi*alpha*n*t and integrating the threshold gives the mean absolute sine, namely 2/pi or cot(pi/(2b))/b. At fixed detuning lambda and on a rational residue class, u=pi*alpha0*n*t has mesh b*pi*alpha0*t, the phase has the asserted affine dependence on u, and the threshold is (1+lambda*t/alpha0)*u. The changed indicator can differ only near an equality point or cutoff. The squared equality is real analytic and nonidentically zero (the squared sine is bounded on the whole real axis while u squared is not). Its zero set on the compact interval is finite; small interval covers justify this moving Riemann sum and continuity. Reflecting residues gives evenness. For large absolute lambda, partition u into small blocks and sandwich the indicator between the two endpoint thresholds on each block; whole phase periods on each fixed block give the circle average, then mesh refinement gives the integral. At half width the sine contribution is empty for |lambda|<=1/2 and cosine crosses the diagonal once, with root 1-2*lambda^2+O(lambda^4). The positive counting constant gives the inverse ordered-tail law and, by harmonic comparison, the Schatten and Abelian conclusions. Independently tested three non-half resonances against direct counts, including negative detuning.

## originality

PASS

The defensible original content is the moving-window threshold law and its strict half-circle dip, not Fourier diagonalization, rational kernel zeros, or novelty over general fixed-sequence counting principles. The same-day two-aperture text has a fixed-sequence lemma that does imply the fixed-window coefficient after computing the elementary empirical mean; it does not supply the frequency-dependent detuning law. The principal same-operator paper gives minimax risk results rather than this crossover.

## value

PASS

A spectral threshold probes frequencies of order 1/t, making displacement of order t the natural calibration scale. The result measures the leading rank at this scale and shows the counterintuitive initial loss upon detuning the half-circle window even though larger detuning recovers the irrational density. This is stronger than just counting exact Fourier zeros or testing a few bandwidths and matters for hard spectral truncation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
