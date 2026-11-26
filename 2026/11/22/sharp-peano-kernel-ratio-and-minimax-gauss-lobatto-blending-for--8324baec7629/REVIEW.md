# Independent mathematical audit

## correctness

PASS

On [0,1] I reconstructed the two Peano kernels using left hinges (t−x)_+^5/120, equivalent to the right hinges by degree-five exactness, and independently checked both rules’ twelve moment equalities. With a=(5−√15)/10 and b=(5−√5)/10, the first piece has A=t^6/720, D=t^5/1440. Write R=25−6√15, U=R+√5 and H=RD−UA. For H on the first piece the sign factor R−2Ua has a rational lower bound 860899/10^6. For the scaled kernels 720A,720D,720H on [a,b] the respective Bernstein-coefficient minima have positive rational lower bounds 2,9,7 divided by 10^6; on [b,1/2] the bounds are 249,610,76 divided by 10^6, with the last bound for 720H/(1−z)^2 where z=(t−b)/(1/2−b). Divisibility is exact. The independent reconstruction (python /workspace/branches/independent_peano.py, with SymPy) used rational radical enclosures; no uploaded script was executed. Reflection supplies the other half. At 1/2 the scaled kernels are R/1600 and U/1600; at the outer boundary A/D tends to zero. D is positive off the endpoints, so the gap vanishes only for f^(6) identically zero under the sign assumption. Continuous nonnegative sixth derivatives supported in shrinking interior neighborhoods approach both ratio extremes; negation preserves the ratio for the other sign. Hence the blend’s worst-case normalized error is max(|q|,|c*−q|), uniquely minimized at c*/2. With a fixed finite partition the signed gaps cannot cancel, and placing the bump inside one cell also proves composite sharpness. The signed brackets, not the normalized ratio, reverse for the nonpositive case.

## originality

PASS

The rule pair, comparison, gap certificate, and equal-panel use are established precedents. The new content supported by the comparison is the exact sharp kernel domination constant, with its nonpolynomial limiting extremizers and uniquely optimized coefficient for the same nodes; optimizing an already known ratio interval would by itself be routine.

## value

PASS

This sharp coefficient improves an existing a posteriori certificate for a standard, already implemented rule pair. The old q=1/4 weight genuinely has worst-case coefficient 1/4, approached at the small-ratio end. The minimax weight reduces it to about 0.22036, an 11.85% reduction with the same seven evaluations per panel, and identifies the precise limit of what that gap and the sign assumption can ensure among linear blends. No wall-clock speedup or floating-point guarantee follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
