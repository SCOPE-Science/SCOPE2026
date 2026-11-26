# Independent mathematical audit

## correctness

PASS

The drift is stable and symmetric with eigenvalues a,a+b; splitting the stationary Lyapunov equation into the P and I−P blocks gives denominators equal to the corresponding sums of relaxation rates. Positivity of D guarantees an invertible covariance. With the specified index and sign convention A=D−KC=(CK−KC)/2=b(PD−DP)/(2a+b). Writing T=T̄1+v shows A is the wedge of 1 and v with the stated coefficient: for unequal baths the rank is exactly two and Ω=b||v||/[(2a+b)√n], and for equal baths A=0. Since j(x)=AC⁻¹xρ(x), this is also pointwise confinement of the flux vectors. Conversion of bath force-work from Stratonovich gives h_i=(KCK−DK)_ii=(−AK)_ii; uniform off-diagonals of K give the stated row sums and ∑h_i=0. The Gaussian quadratic rate is tr(C⁻¹AᵀD⁻¹A); substitute A=D−KC on the right, use skew symmetry and cyclicity, to obtain −tr(D⁻¹AK), the reservoir rate. For the cold family the other two baths sum to 3−ε, their product is (6−12ε+4ε²)/4>0 on the stated interval, and total sum of squares is 6. Hence the first two moments and integrated-current spectrum are fixed, but only the 1/ε term of ∑1/T_i diverges. The divergence concerns entropy production, not heat flux or the full matrix A, and never assumes zero-temperature dynamics. Fresh bounded reproduction: exact SymPy Lyapunov solves in four cases (equal and unequal baths), heat and entropy trace checks, and symbolic cold-family moments and leading coefficient. Replay cd /workspace && python3 review-evidence/reproduce.py 1; output review-evidence/1.txt. Inspected but did not execute the frozen verifier; its recorded 36 cases are corroboration, not the general proof.

## originality

PASS

The Gaussian commutator is prior work, its rank bound follows from the two-rate drift with a one-dimensional eigenspace, and the two-bath case has a gyrator antecedent. The supported distinct contribution is the closed all-bath thermodynamic classification in this symmetry class coupled with the fixed-temperature-moments, fixed-integrated-current-spectrum divergence witness, not the general Gaussian method or unbounded OU dissipation without those constraints.

## value

PASS

A natural pinned complete-graph model reduces the stationary current to one plane irrespective of the number of unequal baths, giving a useful exactly solvable benchmark. More importantly, the fixed-moment witness distinguishes the purely spectral current diagnostic from reservoir entropy production even at fixed drift. It quantifies a real failure of inference from the measured invariant, not a claim about diverging mechanical heat flux or an arbitrary graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
