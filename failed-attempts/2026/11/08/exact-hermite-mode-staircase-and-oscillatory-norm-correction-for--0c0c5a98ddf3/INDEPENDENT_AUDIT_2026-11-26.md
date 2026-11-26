# Independent mathematical audit

## correctness

PASS

For the stated unit Gaussian the Hermite STFT has squared amplitude e^{-u}u^n/n! and an angular monomial phase up to a common phase, so the radial integral is diagonal; u=π(x²+ξ²) has radial area element du after integrating the angle. The eigenvalues sum to L. The adjacent difference is the lower endpoint minus the upper endpoint of e^{-u}u^{n+1}/(n+1)!; for s>0 it has the sign of L−(n+1)log(1+L/s), and for s=0 it is negative. This gives all maximizers and ties. At a tie, the common endpoint value times (n+1)(1/s−1/(s+L)) gives the claimed slope jump. For m=floor(ρ) and δ=m−s, Stirling gives log of the Poisson density times sqrt(2πs) equal to −[δ/2+(v−δ)^2/2+1/12]/s+O_L(s^{-2}) uniformly on 0≤v≤L because δ is bounded. Averaging this coefficient yields C_L+(δ−(L−1)/2)^2/2. Then δ=L/2−{ρ}+O_L(s^{-1}), also at ties with this choice of mode. The continuous unbounded monotone ρ crosses every phase arbitrarily far out, giving the stated cluster set. The attached verify_annulus.py was inspected, not executed; its finite Simpson checks are corroboration only.

## originality

FAIL

The October 18 indexed Gaussian-annulus theorem already contains all fixed-area mode/tie and derivative-jump formulas and the full second-order asymptotic with an equivalent Bernoulli phase. Its remainder is unchanged by recentering and replacing the phase as in the frozen statement. Neither Knutsen's partial earlier result nor an inaccessible source is the basis of this verdict.

## value

FAIL

The exact mode staircase and nonconstant norm correction address natural quantitative questions beyond Knutsen's leading term, but the frozen record repeats the earlier indexed solution. Changing the phase coordinate within the already established remainder does not establish an independently new invariant, asymptotic order or transition law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
