# Independent mathematical audit

## correctness

PASS

Dependencies follow strictly decreasing clock paths; retaining just the ordinary clocks on a length-k path bounds the probability of the required order by 1/k!, even if the path meets the marked vertex. Summing against the exponential number of paths gives finite dependence almost surely. In the uniform-label coordinate x=1-e^{-t}, independent detached branches give h'=-h^{q-1}; integrating h^q at an ordinary full vertex yields the frozen p_*. Along the marked-to-target path there are q-2 unchanged child branches at each internal site and q-1 unchanged branches at the target. Subtracting the homogeneous cavity recursion and using du=h^{q-2}dx therefore gives δ_j=-Tδ_{j-1} and the target weight e^{-u}du, with δ_0=g_a. For a>1 the coupled marked label is strictly earlier; the function 1_{s≤x}h(s)^{q-1} is nonincreasing and strictly decreasing in (0,x), giving a strict sign even at x=1. The reverse holds for 0<a<1. Positive integration preserves strictness, so the sign alternates. The uniform bound |g_a|≤1 gives L^r/r!. Expansion at zero yields g_a=-(a-1)u+O_{q,a}(u²), with a global quadratic remainder by continuity even for a<1. The iterated remainder has one extra power and factorial factor. Integration against e^{-u} evaluates the leading term at the upper endpoint with relative O_q(1/r) error, yielding the stated signed coefficient for fixed q and a≠1. For a=1 the response is identically zero.

## originality

PASS

The homogeneous cavity law and the occurrence of alternating factorial screening in a one-dimensional adsorption defect are prior. The distinct contribution is an exact finite-rate response at all distances on a branching regular tree, including the q-dependent clock transformation and sharp coefficient. The checked close sources do not give this response as a special case.

## value

PASS

A finite change of the site attempt rate is a natural perturbation of greedy blocking on a branching graph. The sign at every distance, nonvanishing for every a≠1, and the exact leading factorial constant distinguish the response from a dependency-path upper bound or a linearized homogeneous covariance. The closed formula can predict local changes without simulating a growing neighborhood; quantitative screening persists despite exponential shell growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
