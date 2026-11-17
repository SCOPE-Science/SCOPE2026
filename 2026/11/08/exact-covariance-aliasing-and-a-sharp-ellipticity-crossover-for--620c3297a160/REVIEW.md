# Independent mathematical audit

## correctness

PASS

Integrating factor W(t)=e^(−At)X(t)e^(−Aᵀt) gives W′(t)=e^(−At)Qe^(−Aᵀt), a rotating rank-one projector. Substituting the actual published two-/three-stage SSPRK Shu–Osher updates yields trapezoidal/Simpson node weights. Complex anisotropy of F(t) is exp(2iωt), and finite geometric sums give T/2(1±ρ_N|cosφ|) versus T/2(1±ρ_N(2+cosφ)/3), ρ_N=|sinNφ/(Nsinφ)| with continuous phase limits. Positive weighted sampled-projector spans prove rank deficiency iff φ∈πZ for trapezoid and 2πZ for Simpson. Comparing the amplitude factors yields sign threshold cosφ=−1/2 and equality at ρ_N=0 or cosφ=1. Taylor expansion gives the fixed-N quadratic near-odd-half-turn coefficients. Independently formed all sampled matrices and checked all eigenvalues in 70 (N,φ,method) cases, including exact resonance; universal sets follow from span/analytic proof.

## originality

PASS

Best-of-knowledge PASS: Zhang–Lan–Jing introduce the exact methods and show SPSD/second-order accuracy, but their accessible full text does not assert strict positivity, exact rank-loss phases, smallest-eigenvalue crossover, or near-resonance coefficients. Generic Lyapunov Gramian and SSP theory provide methods and representation, not this complete phase classification. A trigonometric quadrature aliasing restatement remains possible.

## value

PASS

Positive semidefiniteness can mask a singular numerical covariance despite a full-rank continuous Gramian. The exact mechanism and a counterintuitive phase sector where higher order helps or hurts conditioning provide a motivated structural boundary for a natural positivity-preserving method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
