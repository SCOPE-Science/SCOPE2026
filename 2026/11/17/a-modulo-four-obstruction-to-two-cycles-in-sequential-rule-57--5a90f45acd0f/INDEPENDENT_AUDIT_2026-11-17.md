# Independent mathematical audit

## correctness

PASS

For every n>=3 a Rule-57 site update holds the center exactly for neighbors (0,1), otherwise it complements; hence each update is involutive and a complete sweep is bijective. If F(x)=y and F(y)=x, any unchanged bit would require its adjacent bits unchanged in both sweeps; cyclic connectivity would make all bits unchanged, contradicting impossibility of a fixed point. Thus y=1-x. Interior toggles give x_{i+2}=1-x_i for 0<=i<=n-3, while the two scan-seam constraints give x_{n-1}=x_1 and x_{n-2}=x_0. The four-term recurrence and both boundary equations have four solutions precisely for n=2 mod4, none otherwise; these make two 2-orbits under complement. Independently written truth-table exhaustive search reproduced exact second-iterate fixed sets for every n=3..15; finite enumeration is corroboration, the boundary argument proves all n.

## originality

PASS

The fixed-sweep modulo-four two-cycle classification is not an implication of center-permutivity, known absence of Rule-57 fixed points, or permutation-group generation while varying scan orders. Searches of published findings returned the same target record and distinct Rule-150, Rule-60 or unrelated cyclic-rule results, rather than an earlier theorem asserting this exact Rule-57 two-iterate fixed set. Source coverage is best-of-knowledge, especially for possible unindexed all-period classifications.

## value

PASS

Fixed sequential local rules are standard model maps, but the theorem gives a sharp uniform period-two obstruction with an actual length congruence and a complete list of low-period configurations. It exposes a non-obvious scan-seam constraint and determines a natural minimal temporal statistic for every ring size; this is more than a fixed-point existence check or a single toy instance. The bounded low-period sector is intrinsically meaningful even without an all-period classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
