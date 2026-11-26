# Independent mathematical audit

## correctness

PASS

For a fixed drive trajectory, each odd binomial coefficient contributes a factor (1−2p_{m,k}) to the row mean. Over F_2, (1+x)^s is a product of (1+x^{2^j}) over the one-bits of s, giving 2^{pop(s)} distinct monomials. The squared mean is thus bounded by rho^{2^{pop(s)+1}}, with rho=1−2epsilon, and is identically zero when rho=0. For s=S_m, the probability of pop(s)<r is bounded by O(m^−1/2) times the number of such binary strings, a fixed-degree polynomial in log m for fixed r. First taking m to infinity, then r to infinity, gives convergence of the bias in L^2 of the drive. Viewed as random elements over the environment in this Hilbert space, the independent rows minus their means have norm at most two, so the martingale of their 1/m-weighted sums is L^2 bounded and converges almost surely. Hilbert-space Kronecker and Cesàro averaging remove the centered fluctuation and bias. On the resulting common environment event, fixed t is obtained by using floor(Nt) terms; a finite mesh and |zeta_m|=1 give the uniform-on-compacts probability conclusion. The conditional martingale increment has unit diagonal covariance and off-diagonal zeta_{j−1}; bounded rescaled jumps satisfy the martingale FCLT and covariance tI gives independence. The recorded parity, finite-mean and binomial bound checks were inspected, not re-executed; they do not establish the almost-sure environment assertion.

## originality

FAIL

The frozen conclusion is fully covered by a distinct indexed stronger result on the identical array and walk: Resultary 00b4222393d7 proves a quenched sharp two-sided law of the iterated logarithm for the same cross-bracket. That gives all held-out bracket and Brownian claims, including conditional L^2, by bounded convergence and the bracket FCLT. This is demonstrated existing coverage, not a finding about who first proved the quenched limit. The covering record carries a later catalog date, and Hamza–Tournier v1 itself gives only the annealed result for this model. The frozen proof is valid and differs in method, but no distinct mathematical conclusion survives the comparison.

## value

PASS

The quenched upgrade for tied-cardinality rows is a substantive probability question in its own right: it controls covariance after conditioning on almost every environment, which annealed weak convergence does not provide. The short Hilbert-space proof exposes useful separation of row independence and binary-popcount bias. This intrinsic interest does not remove the decisive overlap with the stronger catalog result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
