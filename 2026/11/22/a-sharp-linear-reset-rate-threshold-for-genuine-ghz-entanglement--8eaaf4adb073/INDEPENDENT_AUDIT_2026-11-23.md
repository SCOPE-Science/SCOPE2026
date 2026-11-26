# Independent mathematical audit

## correctness

PASS

From any initial state the no-reset branch has mass e^(−rt); the remaining branch is the channel average over ages 0 to t. This proves the stationary Laplace integral and trace-norm convergence independently of the initial state. Tensorized depolarization multiplies the sole GHZ coherence by e^(−nγt) and gives equal populations for complementary words. The exact general X-state GM concurrence formula gives max(0,2c+2d_0−1) upon summing unordered non-GHZ complementary pairs. The reference in RESULT.md points to the appendix's Eq. (13), a restricted block lemma; the general theorem used here is Sec. II, Eq. (5), and does apply. The age variable Z has E[Z^j]=ρ/(ρ+j); expanding the endpoint populations produces precisely the even-binomial sum. Its j=0 value is 1; each term is nondecreasing in ρ, and the separate ρ/(ρ+n) term is strictly increasing. Continuity and endpoint values 2^(1−n)−1 and 1 give exactly one positive threshold. Direct combination of the rational terms gives the n=3 and n=4 checks. Independently, express the binomial sum as E[ρ/(ρ+J)] for J~Bin(n,1/2) conditioned even. For n>4 its first four moments equal the unconditioned ones, by vanishing alternating sums of polynomials of degree <n. Taylor expansion about n/2 uses mean-zero centered first and third moments, variance n/4, and fourth moment O(n²); the fourth derivative is O(n⁻⁴) uniformly on J≥0 for ρ=cn+d with c bounded away from 0 and bounded d. This yields 2c/(2c+1)+[2d/(2c+1)²+2c/(2c+1)³]/n+O(n⁻²) for the binomial term. Adding the separate term gives leading zero c=1/sqrt(2) and canceling the 1/n coefficient gives d=−1/2+sqrt(2)/4. The rational derivative on this scale is at least n/(ρ+n)², so an O(n⁻²) residual locates the root to O(n⁻¹), by bracketing a distance O(n⁻¹) around cn+d.

## originality

PASS

The inspected overlaps separately supply the X-state concurrence formula, local-depolarization dynamics results, and renewal resetting, or change the noise, state or entanglement diagnostic. None supplies the conjunction of full GHZ resets and independent local depolarization, evaluated for stationary genuine concurrence with the stated unique rational threshold and two-term linear law.

## value

PASS

This gives an exact full-system reset overhead for maintaining a standard genuinely multipartite resource against independent isotropic local noise. A one-cut entanglement diagnostic would not answer that question. The all-size boundary, extensive coefficient and finite-size correction quantify what is required; the different scaling in the closest amplitude-damping comparator illustrates why the noise model matters. The value is a maintenance law using an entangled reset resource, not a protocol for creating GHZ entanglement from separable resets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
