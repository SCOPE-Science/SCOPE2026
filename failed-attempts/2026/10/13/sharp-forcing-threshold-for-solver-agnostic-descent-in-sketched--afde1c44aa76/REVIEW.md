# Independent mathematical audit

## correctness

FAIL

The residual-only frontier is correct uniformly over nonzero g in range(B), not necessarily sharp for an individually fixed g. For H=B+mu I the worst directional derivative is -g^T H^-1 g + eta ||g|| ||H^-1 g||, attained by aligning rho with H^-1 g. Restricting H^-1 to range(B) and taking its minimum cosine gives 2 sqrt(ab)/(a+b), with endpoint weights a/(a+b), b/(a+b) in the H eigenbasis. This attains the threshold for each spectrum and gives ascent above it; for a=b the threshold is 1, reached by rho=g. Kernel components cannot worsen the directional derivative. In the sketch, range(A A^T)=range(A) for A=MJ^T. However, the frozen record also asserts s^T rho=0 for standard LSMR and uses it to explain the source guarantee. BMM does invoke that identity, but its eq. (2.9) is a primal least-squares minimization on the Krylov subspace (the LSQR property), whereas standard LSMR minimizes the normal-equation residual (MINRES on the normal equation). For H=diag(2,4), g=(1,1), the first LSMR step from zero is s=-(3/10)g by minimizing ||g+Hs|| over span(g). Then rho=(2/5,-1/5) and s^T rho=-3/50, not zero, even with ||rho||/||g||=1/sqrt(10)<1. It does satisfy s^T H rho=0. This example is realizable with mu=1, M=I, J=diag(1,sqrt(3)), F=(1,1/sqrt(3)). The implication from s^T rho=0 to strict descent for nonzero s is correct conditionally, but standard LSMR does not in general supply that premise. The example challenges the asserted orthogonality, not the sign of descent in that example or the source's entire convergence result.

## originality

FAIL

The corrected residual-only result is the classical first antieigenvalue applied to the inverse regularized normal matrix on its positive spectral space. An elementary maximization over a Euclidean ball identifies exactly the classical quotient, and the cited theorem already gives the sharp constant and extremizers. The named application does not supply a distinct exact fact.

## value

FAIL

The advice that a norm test should not be transferred between solvers without checking geometry is useful, but the exact residual-only threshold is a direct application of the named classical formula. The additional LSMR explanation does not supply a valid distinct result. Removing it would leave only the covered deduction; no repaired finding is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
