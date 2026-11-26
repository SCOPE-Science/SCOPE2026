# Independent mathematical audit

## correctness

PASS

Independent derivation: at a fixed block count t the optimizer takes the best coordinates in each block. If the unrestricted top-k set has count T>r, the gain for a step ending at t≤r is the t-th largest first-block weight minus the (k−t+1)-st largest second-block weight; the former is in the unrestricted set and the latter is not, so the gain is positive. Hence the constrained count is min(T,r). Uniform strict Gaussian orders and transitivity within each block then give the mass 1/M below r and p/N_r at r (including T=r). Square and sum these masses for the collision law. For x=h/n and y=k/n, Stirling in a fixed standardized window gives the hypergeometric prefactor (2πn x(1−x)y(1−y))^(−1/2) and log exponential −(t−hk/n)^2/[2n x(1−x)y(1−y)]+O(n^(−1/2)) uniformly there: linear entropy terms cancel. This variance proxy differs from the stated variance by a factor tending to one. Riemann summation and Chebyshev outside a fixed large standardized window give the distribution limit. Rounding is negligible; interior collision mass times M/σ_n vanishes, and the boundary mass tends after scaling to (1−Φ(a))²/φ(a)>0. Thus localization holds and multiplication by F/M→Φ(a) yields the uniform-baseline comparison. L<r<U holds eventually under the proportional hypotheses and ensures two distinct masses in the finite result.

## originality

PASS

Credit the known one-split polytope, random-order greedy framework and standard hypergeometric limit theorems. The supported distinct claim is the explicit two-orbit angular collision law and its sharp critical-window amplification and localization relative to uniform sampling of the same vertices. No equivalent statement or stronger evaluated law covering this regime was identified in the material compared.

## value

PASS

The exact law explains a useful sampling distinction: an orbit vanishing in relative vertex count dominates repeated Gaussian exposure. The explicit threshold-dependent factor and concentration give a quantitative diagnostic for random linear optimization on a natural family, not just a finite face-count computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
