# Independent mathematical audit

## correctness

PASS

For stationary binary Markov labels with switch probability h/2, I_n=∑_{i<j}1(S_i=+,S_j=-) gives exact n²/8 +(∑(n+1-2i)S_i)/4 -(∑S_i)²/8. Correlation E S_iS_j=p^{|i-j|} gives mean; zero inversions means no switch or unique ascending switch, giving exact atom. Gaussian regime uses martingale differences D_k=S_k-pS_{k-1} with deterministic variance 1-p², triangular Lindeberg when nh→∞, and M_n² term negligible, with variance scale n³(1+p)/(48h). For nh→λ, independent Bernoulli switch positions converge to rate λ/2 Poisson process giving telegraph inversion-area and atom. For nh→0, one descending switch dominates I>0 and yields U(1-U). Independently enumerated all 2^n label words for n=2..8 with exact rational probabilities at p=0,1/2,3/4; identities verified. This finite test supplements analytical limit arguments.

## originality

PASS

Best-of-knowledge: exact one-shuffle mean/zero atom and all three triangular-array regimes (Gaussian, Poisson-switch telegraph area, rare positive inversions) are absent from inspected same-model mixing and classical iid riffle inversion theorems.

## value

PASS

Identifies three genuinely distinct fluctuation universality classes for a natural single-step shuffle model, with an unusual non-Gaussian conditioned rare-event limit, sharp exponents and exact finite-n zero atom. Distinct from mixing time results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
