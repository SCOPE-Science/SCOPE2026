# Independent mathematical audit

## correctness

PASS

For vertical phase U in (0,1), the sole integer layer is at height 1; its section is a square of side L=nU. The deterministic horizontal apex-dependent shifts preserve the independent uniform phases modulo one conditional on U. The two interval counts are independently floor(L)+Bernoulli(frac(L)). Write L=j+r; j is uniform on 0,...,n-1 and r independently uniform on [0,1). The probabilities of zero, one and two additional interval points, integrated over r, are each 1/3. Products are j^2, j(j+1), (j+1)^2; the first two coincide at j=0 and consecutive bins share the interior squares, with no further collisions. This includes n=1 and applies to every real apex displacement. Conditional mean is L^2; conditional second moment is [j^2+(2j+1)r]^2. Integrating and summing gives E N=n^2/3 and E N^2=n^4/5+n^2/9+1/45, hence the claimed variance. Each interval count is at distance at most 1 from nU; the product bound |N/n^2-U^2|<=2/n+1/n^2 establishes almost-sure convergence under common phases and the asserted CDF; the variance formula gives the coefficient of variation. Boundary events have translation measure zero, including over countably many n. The inspected rational checker compares finite section counts and finite moment sums only and was not executed.

## originality

PASS

The surviving claim is the complete square/pronic probability law, invariant under real horizontal displacement of the apex, with its exact moments and nonconcentration consequence for this natural thin family. The single-section trick and interval rounding are not original. The closest indexed comparison uses the same height-one reduction for simplex sections, but its distribution and geometry do not cover square sections. The inspected literature and catalogue establish no equivalent or stronger statement covering this law.

## value

PASS

A square pyramid with one lattice unit of height is a canonical convex polytope for isolating anisotropic count fluctuations as volumes diverge. The complete positive mass spectrum, including apex invariance and how interior and endpoint weights differ, gives an exact benchmark that generic mean-as-volume or fluctuation estimates miss. The nonzero limiting coefficient of variation quantifies why fixed-height growth is different from isotropic dilation; it is not itself a new general concentration principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
