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

The angular-frequency convention gives kernel sin(Wx)/(πx). Restricting the unitary Fourier transform between the finite windows gives a Hilbert–Schmidt factor, so the square trace is the integral of the squared kernel. Its two off-diagonal rectangles give exactly 2J; they have positive integral because the sine zeros occupy a null subset. Writing s=v−u gives an even, compactly supported difference measure with Fourier transform F(t)=4 sin(at/2)sin(bt/2)/t². Taylor expansion of (D+s)^−2 yields the stated leading J, and fixed-phase sequences realize the entire stated cluster interval. In the exact derivative, expanding (D+s)^−2 and (D+s)^−3 uniformly gives the quadratic term WB sin(2WD) and the cubic term −ab+(B+2WB′)cos(2WD), after factoring π^−2; the sign comes from ∫s sin(2Ws)=−F′(2W). A second derivative of the exact compact integral gives leading curvature 2W²B cos(2WD)/(π²D²) with O(D^−3) error. For B≠0 the derivative signs at the ends of fixed small phase neighborhoods of kπ are opposite, curvature there has fixed nonzero sign, and outside those neighborhoods the leading sine is bounded away from zero. This gives exactly one late stationary point per neighborhood, displacement O(1/k), and alternating strict extrema. For B=0, if sin(Wa)=0 then |2WB′|=a|sin(Wb)|/W<ab, symmetrically if the other factor vanishes, and if both vanish B′=0. The uniform negative D^−3 margin makes J′ strictly negative eventually and the defect strictly increasing to the isolated-window sum. Swapping the Hilbert–Schmidt factor and its adjoint transfers the nonzero spectrum to the dual time–frequency setup with the specified convention.

## originality

PASS

Supported distinct content is the unequal-width large-separation classification, specifically the strict derivative margin under a single resonant width. The trace identity, its dual, and the equal-width classification are covered and not credited here. The strongest matched catalogue analogue uses equal widths and does not address the mixed asymmetry.

## value

PASS

In a canonical two-window concentration problem the summed transition defect does not in general approach independent-window behavior monotonically. The sharp criterion tells when infinitely many separated extrema persist, and proves that tuning only one of two independently variable unequal lengths suffices to remove them eventually, even though a smaller oscillatory derivative term remains. The cluster interval adds quantitative information about the residual coupling independently of any individual eigenvalue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
