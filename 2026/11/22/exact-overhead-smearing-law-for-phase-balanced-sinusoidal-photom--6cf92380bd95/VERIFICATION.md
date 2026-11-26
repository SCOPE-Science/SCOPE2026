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

A centered boxcar multiplies each harmonic design column by sinc(x). The phase grid kills the first and second nontrivial harmonic sums for N>=3, so the Gaussian Fisher diagonal is (Nt/nu)(1,sinc(x)^2/2,sinc(x)^2/2), even with unknown baseline and both quadratures. Dividing by N(t+h) and by the limiting rate 1/(2 nu) gives sin²(x)/(x(x+a)). On (0,pi/2), its log derivative g=2 cot(x)-1/x-1/(x+a) strictly decreases since sin(x)<x; it starts positive and ends negative. It stays negative from pi/2 to pi. All x>=pi have objective at most 1/[pi(pi+a)], strictly below the value at pi/2, so later lobes cannot tie. Increasing a raises g pointwise; the roots increase and tend to the root of 2 cot(x)-1/x=0 in (0,pi/2). For a going to zero the root must tend to zero since at any fixed positive x below pi/2, the limiting g is 2(cot(x)-1/x)<0. At the root, a/(x+a)=2(1-x cot(x))~2x²/3; this implies a/x goes to zero and x³~3a/2. Substitution gives loss ~a/x+x²/3~x² and the dimensional constant (6h/omega²)^(1/3). At large a, a j_a tends to sin²(x_infty)/x_infty at the optimizer. At h=0, strict sinc²<1 at all positive times proves the claimed nonattainment. Phase waiting is excluded as stated; the proof is not an optimization over actual observing calendars.

## originality

PASS

The sinc response, independent Gaussian information calculation and duty-cycle accounting are prior or elementary ingredients. Best of the inspected evidence, the supported distinct result is the exact global one-harmonic overhead optimizer with its sharp ceiling and small/large overhead laws. The identical indexed record is not independent evidence; the two same-day spectral-smearing records share the tradeoff and even a cube-root scaling, but not the profile, rate, or ceiling.

## value

PASS

Exposure smearing competes directly with fixed per-exposure charges in phase-balanced scheduling. The result gives a usable exact optimizer at every overhead, rules out longer-exposure lobes rather than just giving a local optimum, and quantifies both a sharp upper ceiling and the leading efficiency loss. That is a reproducible design benchmark for a natural single-harmonic experiment, not a claim about arbitrary photometry or finite-calendar observing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
