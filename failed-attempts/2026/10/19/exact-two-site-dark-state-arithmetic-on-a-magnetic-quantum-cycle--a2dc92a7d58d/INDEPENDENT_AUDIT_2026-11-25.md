# Independent mathematical audit

## correctness

PASS

For K=H−iγΠ, the imaginary part of any eigenvalue is −γ||Πu||²/||u||². The dark space is the direct sum over E of ker(H−E) intersected with ker Π (not merely the sum of full eigenspaces contained in ker Π). It reduces H and Π. The complement has strictly negative imaginary spectrum, so it decays even with Jordan blocks. The survival limit is the squared dark-projection norm; trace over untrapped sites gives ν/(N−2). Independent derivation of the count: gauge all bonds real except the seam at 0. A dark eigenvector has to solve the Dirichlet problem on both arcs of edge lengths d and N−d. A nonzero wave on only one arc cannot cancel at the first sink because its first neighbor's sine amplitude is nonzero. A common phase is q=πa/h, 1≤a<h, h=gcd(N,d). With m=ad/h and n=a(N−d)/h, matching at d fixes the ratio of arc amplitudes to (−1)^m and matching at 0 requires exp(iφ)=(−1)^(m+n)=(−1)^(aN/h). There is one dimension per allowed a, and none if either arc has length 1. This yields all three cases of the quoted count and trichotomy, including odd N and adjacent traps. For fixed total flux, redistributing bond phases is itself unitarily gauge-equivalent and cannot change the count or sitewise survival; the caution about such redistribution in the frozen Limitations is misleading, but not a flaw in the Finding under its stated assumptions.

## originality

FAIL

A distinct earlier indexed result, 84c3bc481be5, actually states and proves the entire mathematical Finding: zero, half and nonresonant flux dimensions, plus survival. It moreover covers unequal positive losses and gives survival for individual start vertices. Restrict to equal losses and use α=φ/(2π); the original's trichotomy and adjacent-trap case are immediate from the very same dimensions. This is demonstrated indexed coverage, independent of any claim about ultimate external literature priority.

## value

FAIL

The precise flux-switch classification is mathematically useful in isolation, but the frozen contribution adds no invariant, geometry, or survival quantity to the earlier indexed result. Its trichotomy and adjacency observations are immediate arithmetic consequences of existing exact formulas, and the checker reproduces that existing fact. No separate valuable new remainder is claimed or established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
