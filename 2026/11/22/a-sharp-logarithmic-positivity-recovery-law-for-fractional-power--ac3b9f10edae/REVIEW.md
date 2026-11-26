# Independent mathematical audit

## correctness

PASS

With N=2M and M even the circulant spectrum is the discrete cosine sum with only one antipodal term. Comparing with the periodization F_t of the symmetric p-stable density gives the exact wrap identity: if z=exp(iθ_k)≠1 and d_l=f_t(M+l)−f_t(M+l+1), the error is 2(−1)^k Re[z/(1−z) sum_l d_l z^l]. For A=tM^p large, f_t is convex on [M,∞); d_l decrease to zero and d_0<=ptM^(p−1)e^−A. Dirichlet summation and a direct geometric tail give, respectively, bounds O(tM^(p−1)e^−A/θ_k²) and O(e^−A(1+M/A)). The stable lower bound yields uniform relative o(1) for θ>=t^(1/p) because M^(p−1)e^−A→0 above the proposed threshold, and for θ<t^(1/p) because e^−A(t^(1/p)+A^((1−p)/p))→0 for t<=2. The zero mode is positive and t>=2 is uniformly covered by strict diagonal dominance. At Nyquist, k=M even, the wrap equals minus the alternating sum of d_l; the alternating second differences bound its difference from −d_0/2 by O(d_0−d_1). When A is of order log M, direct differentiation gives (d_0−d_1)/d_0=O(A/M) and d_0~ptM^(p−1)e^−A. The exact stable coefficient can be replayed by integrating the cosine transform of exp(−u^p) twice: its second derivative is −p(p−1)u^(p−2)e^−u plus a remainder with integrable derivative, whose cosine transform is O(1/|x|). The gamma integral then gives q_1(x)~Γ(1+p)sin(πp/2)|x|^(-1−p)/π. Scaling and dominated convergence over the odd translates (2m+1)π give F_t(π)/t→4Γ(1+p)sin(πp/2)π^(−1−p)(1−2^(−1−p))ζ(1+p)=2η(−p). The subcritical ratio M^(p−1)e^−A diverges, yielding a negative mode, and equals e^−h in the fixed-h window, giving the stated limit. This verifies last-failure asymptotics without assuming one finite-N crossing or that Nyquist controls full-matrix recovery at the finer order. Read VERIFICATION.md and verify.py without executing them; the high-precision crossover block only asserts finiteness and prints comparison values, not a numerical error bound.

## originality

PASS

The checked prior statements address fixed or weak angular damping, the Gaussian endpoint p=2, continuum nonpositivity, or stable reference kernels. None supplies the fractional joint-limit last-failure constant or the fixed-order Nyquist window. This is a conclusion from the inspected evidence, not exhaustive priority certification.

## value

PASS

The last loss of positive semidefiniteness is a useful bandwidth boundary for a natural finite covariance model; the result identifies its exact scale for fractional powers and proves uniform positivity over the whole surviving half-line, not just sampled values. The explicit Nyquist window locates a genuine sign crossover and explains the role of the stable algebraic spectrum, without overstating its control of the full-matrix window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
