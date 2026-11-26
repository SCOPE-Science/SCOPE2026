---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The positive Fourier spectrum gives strict positive definiteness on these distinct periodic sites. The Bernoulli polynomial gives K(t,0)=k0-a t^2(1-t)^2 on [0,1]; convolving the sine-density coefficients gives the stated absolutely four-times differentiable kernel mean and the constants b0 and b2. I checked the two-site sum and difference limits b0/k0 and -b2/(2a), and the exact reduced determinant for three sites: 8 k0 a h^3-12 k0 a h^4-2 a^2 h^4(1-h)^4. Its cubic term survives quadratic cancellation. The numerator of the averaged outer weight has quadratic coefficient k0 b2/2+a b0. The outer difference is bounded and the middle weight is -2A/h+O(1). Hence A>0 gives the eventual signs, the exact leading l1 operator norm on arbitrary nodal perturbations, and the variance law for independent centered equal-variance errors. An independent evaluation from the determinant and the convergent mean series gave A=0.04457579267013564 and middle weight -11.5313217985 at N=128. Replay: RESULT.md lines 44–93 and the displayed determinant; read VERIFICATION.md and verify.py without running the frozen script. Distinctness for N>=3 is of transformed sites; the advertised physical-node distinctness holds throughout N>=5. Neither added-noise variance nor a single deliberately collapsing subset is a statement about inherent deterministic error or typical random subsamples.

## originality

PASS

The distinct claim is the sharp two-to-three-site contrast for this periodic kernel and sine density, including the explicit linear coefficient. The closest collision work uses the same general Gram reduction but a quartic rather than a cubic determinant under hypotheses excluding this kernel. The inspected full-lattice results do not govern inversion of a fixed-cardinality principal submatrix. This is a bounded originality decision, not a priority certification.

## value

PASS

This is a motivated adverse design for an existing integration method. It separates simple ill-conditioning from actual weight instability: two nearly coincident sites remain bounded, while the next cluster develops a quantitatively sharp signed mode and an evaluation-noise penalty. The finite design and leading coefficient are useful to judge claims of positivity or robustness under deterministic subsampling, without implying typical-case failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
