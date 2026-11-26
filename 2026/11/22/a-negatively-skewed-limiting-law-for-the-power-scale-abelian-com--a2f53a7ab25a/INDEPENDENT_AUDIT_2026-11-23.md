# Independent mathematical audit

## correctness

PASS

The exact word is the zero coding of the substitution a -> aaa(a+1 mod 3), since adjoining a base-four digit 3 advances the state and the other digits preserve it. Allouche et al. Proposition 8 gives A_0=2 and the difference 3g_m; Lemma 11 computes the block counts, hence the difference is exactly 2 rho^m Phi(m theta). Shifting the uniformly convergent geometric series gives rho H(t+theta)-H(t)=2Phi(t), with A_m-rho^m H(m theta)=2-H(0). Irrationality follows also because 2cos(2theta)=11/7 cannot be a rational algebraic integer, as it would be if exp(2i theta) were a root of unity. Irrational rotation equidistributes modulo pi/3, and the vanishing error gives the empirical law for uniform sampling of exponents. The support is the full connected image of H, since every neighborhood of an attained value has preimage of positive phase measure; the functional equation precludes a constant H. On [0,pi/3] the cosine range is sqrt(3)cos(t-pi/6); its Fourier coefficient is 3sqrt(3)/(pi(1-36l^2)). Summing the geometric shift gives the stated H coefficients, whose absolute summability follows from rho>1; taking the constant and applying Parseval gives the mean and variance with the stated normalization. The third moment is independently certified without using the frozen Decimal checker. For c_l equal to the nonzero Fourier coefficients of H, it is 6 Re sum_{a,b>=1} c_a c_b conjugate(c_{a+b}). An independent rational-interval computation uses exp(6i theta)=(-143+180i sqrt(3))/343 and a+b<=32, with omitted tail bounded by 1/1372000; the final outward interval [-0.000047314972706,-0.000045857246758] is strictly inside the frozen interval. Replay: /workspace/branches/dfaa9be7-5bda-4eca-ad65-b29dd69ba2ac/power_scale_third_moment.py (exact rational interval computation; its .out file records the enclosure). The replay verifies the integral from the analytic Fourier identity, not the recurrence or equidistribution on its own. The frozen checker and captured output were read, not executed.

## originality

PASS

The exact binary example, nonregularity, recurrence, phase irrationality and block-count formula are prior. Further, the phase waveform and interval already follow from the known recurrence, and equidistribution is a standard consequence once the waveform is available; neither the phase change of variables nor the existence of a pushforward alone is credited as an independent advance. The surviving refinement is the explicit moment law and, especially, the exact nonzero signed third centered moment for this natural non-Pisot example. The earlier recurrence and range statements do not determine skewness by a direct parameter substitution or general symmetry principle: one must analyze the periodic correlations, for example by a bounded, error-controlled Fourier triple calculation. The closest primary and indexed results inspected do not give the sign or signed interval; this is bounded originality evidence, not a priority certification.

## value

PASS

Power lengths are the natural substitution scales of the original nonregularity example, not a numerical slice chosen after observing skewness. The earlier interval describes which values accumulate but not their relative frequency. Exact dispersion and a proved strictly negative third centered moment distinguish the natural phase-averaged law from a symmetric fluctuation model even on the same support. The shape fact is an independently useful small invariant; no claim is made about sampling all integer lengths, a closed-form support endpoint, absolute continuity, or a general skewness law for other words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
