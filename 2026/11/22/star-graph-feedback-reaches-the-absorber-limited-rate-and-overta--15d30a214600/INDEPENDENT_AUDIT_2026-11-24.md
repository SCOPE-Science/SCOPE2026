# Independent mathematical audit

## correctness

PASS

This is a PASS for the repaired package, not for the original wording. The original and side files described the full Liouvillian gap as known only within a factor of two. The cited primary paper's arXiv v2 Eq. (78) gives equality for the connected SWAP measurement-feedback model with active feedback. The repair explicitly uses that model, attributes the equality, and does not identify all Liouvillian modes or claim a preparation time. It also replaces a potentially graph-universal reading of 2λ/n by the exact scope: the all-ones Rayleigh bound is λ|F|/binom(n,2), equal to 2λ/n when |F|=n−1. In particular, uniform active feedback on every edge of the complete graph would give rate λ, so 2λ/n cannot be graph-universal. The star rate is strictly below its bound at finite n≥3 since the all-ones vector is not an eigenvector, and approaches it at fixed λ. The corrected scientific files are under repairs/1; frozen evidence was preserved. Independently, dephasing on a measured edge conjugates by its swap with weight one-half; local feedback changes only the same-edge singlet contribution by −λ times its projector. Compression of a traceless one-site Pauli to the measured singlet vanishes, so overlapping pair projectors have no extra feedback term. This gives the claimed half-rate moves and killing. On the star the two classes have unweighted degrees m−1 and 2. CCᵀ=(m−2)I+11ᵀ gives the two singular values with their multiplicities; the nullspace on the pair side has dimension m(m−3)/2 at m≥3. For m=2 the mean-zero hub-pair combination decouples; at n=2 only killing remains. The positive unique lowest eigenvector is permutation-symmetric and the constant block has determinant λ and trace λ+n/2. Rationalizing its smaller root gives nΛ→2λ. For the ring the symmetric separation mode sin(πs/n) obeys the discrete second difference with zero boundary values, since the allowed moves at separation one total rate one and maximal feedback adds one. Positivity makes this the smallest mode. At λ=1 the star quadratic evaluated at the ring rate equals −1/2, 1−√2, (√5−3)/4 and 0 for n=3,4,5,6. For n≥7 use (n+2)π²/(2n²)<1 to prove strict positivity. The ring rate is below the large star root, giving the required ordering and exact ratio asymptotics. Uniform clock rescaling gives the distinct bounded-hub-rate comparison. The supplied checker and finite test scope were inspected, not rerun; no all-size claim depends on a simulation.

## originality

PASS

The surviving claim is the explicit star spectrum and its exact size comparison and asymptotic saturation at fixed unit edge clocks, not the general SWAP closure, general absorber bound, ring formula, or full-gap identity. The repaired attributions distinguish these. Neither the general pair-matrix formula nor the closest indexed size-crossover statement gives the star theorem at this normalization.

## value

PASS

For two natural sparse architectures the complete star solution quantifies exactly how graph topology changes the prepared-state witness decay rate under equal edge clocks. The tree bound is asymptotically sharp on an edge-minimal connected graph, and the strict crossover begins at a specified size rather than merely following from eventual exponents. The explicit contrary conclusion under bounded incident rates makes the comparison meaningful without implying a hardware or state-independent preparation speedup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
