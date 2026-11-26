---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

On the exact lattice ab=1/2 set q=1/b=2a. Modulation Fourier orthogonality gives the Walnut shifts by q with overall factor 1/b. For b<=2 only shifts 0 and +/-q can overlap on positive measure. The translated signed products at shift q are -1 exactly on [q-1/2,1/2), so both off-diagonal coefficients are -M by a-periodicity and the diagonal is 2+M by removing a segment of length 2a. The overlap-count mean length in units of a is 2b-2, so M attains the adjacent integers on positive-measure sectors except at integral endpoints. Fourier series on q-spaced fibers gives multiplier (2+M-2M cos(theta))/b, with sectors {2/b}, [1/b,5/b], [0,8/b] for M=0,1,2 respectively. At b=3/2 only M=1 remains; beyond it the zero set of the M=2 multiplier is null, not a kernel. The nonconstant angular sectors push absolutely continuous densities to absolutely continuous spectral measures by change of variables on the two monotone half-circles, and the positive-measure constant sector gives infinite multiplicity. Independently checked each open overlap cell at six rational b, including b=3/2, b=2 and levels immediately on both sides of 3/2, using python3 /workspace/review_replay.py (section 3); this verifies the finite coefficient calculation only. Inspected the frozen rational checker rather than executing it.

## originality

PASS

Best of available evidence for the exact full-band and spectral-type classification, including the complete nonframe regime, not for the frame-set transition or the standard diagonalization method.

## value

PASS

The density-two curve is natural for scalar periodic fiber analysis and the range is the full first-overlap regime, not an arbitrary example. The exact spectra give optimal stability and Bessel bounds and establish that crossing the known frame threshold destroys stable reconstruction abruptly without destroying completeness. The disappearance of a flat eigensector at the included endpoint also describes a spectral transition not encoded in the binary frame criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
