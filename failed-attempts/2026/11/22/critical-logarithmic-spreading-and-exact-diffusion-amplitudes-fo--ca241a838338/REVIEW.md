# Independent mathematical audit

## correctness

PASS

The generator gives the moment equations in RESULT.md:35–43 without a boundary-flux argument: A=E[XV] has transport source E[V²]=v²P(active), loss λA, and resting-to-moving source α₀ηB/t, while B=E[X²1_rest] has inflow λ(M−B) and outflow 2ηB/3. The active probability is 1−(λ/γ)(1−e^(−γt)), and the positive source and B≥0 give A>0 and M'=2A>0. Transforming the scalar equation after multiplying by t gives RESULT.md:56–64 with the stated signs and normalizations. For I~s^(1+θ), (IF)'~−Cs^(θ−2); below 1 the divergent integral dominates the integration constant, and at 1 it gives C log(1/s)+O(1). The nonnegative, nondecreasing M meets the monotone-density hypothesis of the Laplace Tauberian step (Γ(2)=1). Thus both physical-time limits and amplitudes are correct; the scale λ in the logarithm has no leading effect at fixed rates. The strict condition λ/η<2/3 is exactly the feasibility of θ=1 in the open reinforcement interval; divergence as θ approaches 1 presupposes that approach is available. VERIFICATION.md and verify.py describe symbolic and finite trajectory checks, inspected but not executed; those checks do not establish the infinite-time limit.

## originality

FAIL

The same-model primary paper gives not merely a related evolution equation or an exponent, but the exact forced MSD transform (16) and its leading small-s inhomogeneous balance (17) with the identical C and θ. Integrating this already identified leading balance, then applying standard monotone Laplace inversion with immediate generator monotonicity, mechanically yields both limits and the amplitudes. It is a correct clarification of the published formula, not an independent original result under this standard. This is implicit derivability, not an assertion that the paper prints the two limits.

## value

FAIL

Distinguishing equality from ordinary diffusion is useful interpretation of the published model, and the logarithm is real. But the frozen contribution is restricted to reading off the leading terms of the published forced balance and routine inversion; positivity follows from the same moment generator. The fixed-rate amplitudes and feasibility inequality are mechanically implied. No separate quantitative uniform crossover, distributional result, or other nonroutine gap is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
