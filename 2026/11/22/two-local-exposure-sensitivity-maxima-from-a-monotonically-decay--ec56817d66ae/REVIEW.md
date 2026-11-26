# Independent mathematical audit

## correctness

PASS

For the precise background-limited objective, S'=N/(2T^(3/2)) with N=2TI−E. This N satisfies N(0)=0, is positive near zero, and tends to −a/λ−b/μ. Differentiation gives N'=a(1−2λT)e^(−λT)+b(1−2μT)e^(−μT). Multiplying by e^(λT) and differentiating twice leaves b d e^(−dT)(d+4μ−2μdT) with d=μ−λ>0, so Rolle bounds the distinct positive zeros of N' by three. The zero of N at zero then bounds its distinct positive zeros by three as well. Three strict maxima would force at least five critical points including the two interior minima, even when some critical points are degenerate. This is the decisive bound; four alternating sampled signs, as opposed to four sign changes, require only three intervening extrema, so the informal sentence at line 36 is unnecessary. An independent exact Fraction enclosure, using degrees 12 and 13 at x/32 before powering, bounds 10⁶ N at 1/20,1/8,1/3,1 in (28439,28440), (−30229,−30228), (27711,27712), (−63029,−63028). Three disjoint sign crossings exhaust the allowed zeros, giving strict max/min/max. Widths for the reported degree-16/17 method check separately. For one mode, N' changes from positive to negative exactly once while N starts at 0 and has a negative limit, proving the unique strict maximum. Replay: RESULT.md 17–48 and python3 /workspace/reproductions/exposure.py. The frozen checker was inspected, not run. No astrophysical fit is used in the proof.

## originality

PASS

Passes for the sharp maximum count with a strictly positive two-mode witness for this specific noise-normalized integral; neither decay templates, the one-mode optimum, nor the standard analytic zero-count method is claimed new. The bounded searches and inspected statements found no independent matching two-maximum result.

## value

PASS

The score for a monotone source can nevertheless offer multiple locally optimal durations, and two positive decay components are minimal for that behavior. A sharp bound and rigorous witness are useful when interpreting or testing a local exposure-time optimizer under the model. This is not a claim about typical observed flares, instrument-specific noise or overhead, or the number of global optima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
