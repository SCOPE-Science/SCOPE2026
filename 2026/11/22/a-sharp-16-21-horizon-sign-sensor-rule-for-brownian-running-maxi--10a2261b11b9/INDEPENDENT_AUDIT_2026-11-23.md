# Independent mathematical audit

## correctness

PASS

The conditional-mean decoder is the L² projection onto the span of 1 and the fair sign, so the risk is the half-normal variance minus the squared mixed moment. To check that moment, write a=√s, b=√(1−s), and U=1−Φ. The reflection principle gives the surviving density at x≤m up to time s as p_s(x)−p_s(2m−x); survival after s contributes 1−2U((m−x)/b). Integrating the signed exceedance probability over m≥0 and changing variables d=m−x in the x≤m part gives a/√(2π)+4∫₀^∞[U(d/a)−U(2d/a)]U(d/b) dd. In this calculation the x>m contribution is a/√(2π), and the integrated signed reflection term with future survival replaced by 1 is zero. The integral of U(d/A)U(d/B) equals (A+B−√(A²+B²))/(2√(2π)); it is the expectation of the minimum of the positive parts of two independent scaled standard normals, computed in polar coordinates. This recovers the stated mixed moment, with b=0 covered directly or by continuity. The radical numerator is positive for s>0 and its derivative has the sign of 16−21s; the limit at zero is zero, so the minimizer is uniquely interior. Substitution, an independent high-precision arithmetic check, and Brownian scaling agree with the reported risks and percentages.

## originality

PASS

The substantive step is the exact interior-time mixed moment for the free Brownian maximum and the sign at the observation time. The endpoint case is covered. No distinct source inspected supplies the interior curve or a theorem from which it and the optimum follow by substitution; known joint-law ingredients still require a signed integration over both parts of the path.

## value

PASS

With a fixed information budget of one zero-threshold bit, choosing a time before observing a path is a natural design problem. The exact decoder, strict interior optimum and about 8.82% advantage over terminal sensing solve that design problem and give a benchmark for richer sensors. This conclusion depends on the nonterminal mixed moment, not just the known terminal normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
