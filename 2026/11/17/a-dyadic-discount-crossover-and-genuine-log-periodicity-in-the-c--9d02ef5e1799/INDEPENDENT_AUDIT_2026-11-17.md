# Independent mathematical audit

## correctness

PASS

For A=[[1,1],[1,2]] modulo 2^a, A^3=I+4C with det(C)=-1, and the 2-adic valuation of A^(3q)-I is 2+nu_2(q) with odd residual matrix invertible, while A^m-I is invertible mod 2 when 3 does not divide m. This classifies primitive depth-b vectors with least period 3*2^max(0,b-2), giving exactly 1 fixed vector, 15 period-3 vectors, 3*4^(s+1) vectors of period 3*2^s for 1<=s<=a-2; sums to 4^a. Independently checked finite trace profile numeric at t=.05,.1,.2,1,2, confirming small-t expansion error O(t^3), and verified exact count formulas analytically. The cycle trace contributes 1/(1-alpha^period); after alpha=e^(-t/M_a), M_a=3*2^(a-2), finite trace is a truncated dyadic geometric sum plus O(2^-a) exceptional terms, tending locally uniformly to L. Bernoulli expansion gives 3/(2t)+1/2+t/14+O(t^3). Periodizing f(u)=u^2/(e^u-1) on multiplicative dyadic scales gives t^2(L-1)=H(t)+O(t^2 exp(-2t)), smooth H(2t)=H(t). Mellin unfolding yields Fourier coefficients 3 Gamma(2-i omega) zeta(2-i omega)/(4 log 2), all nonzero by Re(s)=2 Euler product and nonzero Gamma. The finite checker was inspected; infinite limit and nonconstancy use direct estimates and Mellin argument.

## originality

PASS

Arithmetic period counts and cycle trace identity are known inputs and expressly not claimed as discoveries. The newly assessed statement concerns the simultaneous resolution/discount t crossover, quantitative O(2^-a), both asymptotic regimes and explicit nonconstant dyadic phase and gamma-zeta Fourier spectrum. Chandra treats finite arithmetic landscapes; earlier Chen et al. classify prime-power periods; neither inspected accessible statement provides this particular double-scaling and nonzero phase, though older full texts remain priority risks.

## value

PASS

A natural return-resolvent observable on a classical hyperbolic toral map exhibits discrete scale invariance when lattice resolution and discount are coupled. The nontrivial, exactly computed log-periodic oscillation is structurally informative beyond recomputing a known orbit census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
