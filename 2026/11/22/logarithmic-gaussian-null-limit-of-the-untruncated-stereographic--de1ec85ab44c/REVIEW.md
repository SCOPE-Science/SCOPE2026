# Independent mathematical audit

## correctness

PASS

Reconstructed the Cramér–Wold proof for the centered, untruncated pair sums under iid area-uniform sampling on S². For Z=cot(Θ/2), the pair density 2z/(1+z²)² gives mean π/2 for Z and 1/Z, absolute-tail mass O(M^-2), first-tail moment O(M^-1), and a clipped second moment 2(b²+c²) log M+O(1) for W=bZ+c/Z, with no log from the mixed product. At M=n(log n)^(1/4), clipping changes no pair with probability 1-O((log n)^-1/2) and its deterministic centering shift is O((log n)^-1/4). Rotation invariance gives exact degeneracy and constant row second moment v. The predictable variance's diagonal coefficient is 2(n-1)v/n; its remaining pair terms are orthogonal, and the kernel of H² has L² norm squared at most ||H||op² v=O(log n) by the uniform absolute row-integral bound. The off-diagonal deterministic squared weights sum to O(1), so the predictable variance divided by log n converges in probability to 4(b²+c²). Conditioning on the new spherical point gives the independent summands for the fourth-moment bound; the unconditional sum O((log n)^(1/2)+(log n)²/n)=o((log n)²) implies conditional Lindeberg in probability. Slutsky and Cramér–Wold yield the two independent coordinates and the stated finite-list covariance. For fixed n, isolate one colliding pair (or an antipodal pair if b=0) in separated caps with all other terms bounded. Its square has a divergent radial integral, even for signed channels. No variance convergence or power claim is used. The frozen verification references a finite-constant diagnostic; it was inspected, not run, and is not the infinite-limit proof.

## originality

PASS

The exact same-statistic primary paper leaves the raw q=2 case out of its null theorem. The distinct same-day fixed-n two-ray result overlaps in tails and moment divergence but supplies no triangular-array limit. The supported distinct claim is the centered raw q=2 Gaussian null law, including its variance scale and independent channels, not the statistic, finite moment obstruction, or martingale technique.

## value

PASS

Resolves the untruncated null scaling in the dimension where the original test paper's square-integrable theorem stops. The normalization and joint limit determine how different parameter choices co-vary, even though finite-n raw variances do not exist. This is a mathematically useful null law, not a finite-sample calibration or a claim of power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
