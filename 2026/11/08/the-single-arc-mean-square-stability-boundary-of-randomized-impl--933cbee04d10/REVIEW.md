# Scientific review — single-arc stability geometry for randomized implicit RK2

## Correctness — PASS

The claim is about the scalar multiplier \(1+z/(1-Uz)\) under fresh uniform sampling. The exact squared-modulus fraction is derived directly from that multiplier, not inferred from a plot. Its derivative in the squared imaginary frequency factors as \((1-2t+2xt(1-t))/((1+xt)^2+qt^2)^2\). Pairing \(t\) with \(1-t\) gives a strictly positive integral for negative real part. The one-positive-root assertion on the real axis follows from an explicit derivative, while the two boundary contact orders follow from exact local expansions. The source's zero-right-half-plane fact is also reproved by pairing reciprocal squared ratios. `check_stability.py` passed 19,832 algebraic, exact-rational and high-precision checks; these supplement, rather than replace, the infinite-domain proof.

## Originality — PASS with residual precedence risk

The strongest direct comparator is Bochacik and Przybyłowicz, arXiv:2404.19059, Section 3.2. It **already states** the moment formula and an exact pointwise test, together with the real-axis cutoff, boundedness, openness and half-plane containment. The present claim explicitly excludes those as contributions. Facts 2–6 do not assert that every fixed-real-part slice is a single interval, that the boundary has only two joining endpoints, or the fourth-/second-order contact laws. The monotone-frequency proof is an additional global inequality; these geometric facts are not merely a reparameterization of a named prior theorem. The explicit comparison uses a different multiplier polynomial from arXiv:2006.12131. The randomized Taylor family of arXiv:2205.10908 and the later randomized SDIRK method of arXiv:2607.18928 do not dominate this exact stability-domain shape result. Similar deductions from the existing implicit moment formula might exist outside indexed sources; this remains the principal residual risk.

## Value — PASS

A numerical solver must know whether a decay rate admits a connected interval of oscillation frequencies, and what happens when damping approaches either critical extreme. The global one-arc theorem replaces an implicitly plotted set with a complete structural classification; the fourth-root contact quantitatively measures near-imaginary-axis fragility and enables a sharp comparison with explicit randomization. No general numerical-ODE convergence or novel algorithm is asserted. The result is a natural complete classification of this particular established stability region, not an arbitrary parameter slice.

## Literature and limits

Compared full primary relevant portions of arXiv:2404.19059 (scheme definition and Section 3.2), arXiv:2006.12131 (Section 5.1), the introduction and representative stability discussion of arXiv:2205.10908, and the abstract/introduction of arXiv:2607.18928. The exact pointwise formula in the first source creates a real risk that a specialist will regard the shape analysis as an immediate corollary; it is therefore central to the precedence assessment and not hidden. The theorem assumes iid uniform stages and a scalar complex linear test equation only. The code is finite supporting evidence, not independent validation.

Self-review: passed. Independent audit: not yet performed.
