# Independent mathematical audit

## correctness

PASS

Exact coordinate minimization in energy coordinates z=H^(1/2)(x−x*) removes the projection along a unit direction u_i, so the sharp worst-direction expectation per expected work is λ_min(U diag(q) Uᵀ), with U=[u₁,u₂] invertible and cᵀq=1. Flip the second column if needed so UᵀU has positive off-diagonal ρ. For a lower bound g on that eigenvalue, congruence gives diag(q)−g(UᵀU)^(−1) positive semidefinite. Writing a_i=q_i−g/(1−ρ²), the two-dimensional condition is a_i≥0 and a₁a₂≥[gρ/(1−ρ²)]². Weighted AM–GM gives 1≥g(c₁+c₂+2ρ√(c₁c₂))/(1−ρ²). Equality is feasible and unique, including ρ=0 where both a_i vanish; for ρ>0 both the determinant bound and c₁a₁=c₂a₂ bind. Mapping back via p=q₁/(q₁+q₂) gives the claimed probabilities, allocation limits and interior support. The fair value is (1−ρ)/(c₁+c₂); the ratio is ≤1+ρ<2, with sharp supremum two by taking ρ→1 and c₁/c₂→∞. The proof's strict intermediate bound by 1+ρ is non-strict at ρ=0, but the finding's strict bound by two and all equality cases are correct. The stated example gives 3/10, 4/85, and 20/17. The verification package was inspected without executing the uploaded program. No claim about asymptotic, wall-clock, or stochastic work-normalized progress follows.

## originality

FAIL

After cost rescaling and inversion of the two-direction Gram matrix, this is exactly the symmetric full-diagonal case of published fixed-trace dominant-eigenvalue minimization (Abad Torres and Roy, Automatica 89, 2018, Thm. 1 and Lemma 1). The known optimum inserted into the inverse reparameterization gives the whole allocation law and sharp value. The fair-sampling comparison and limiting cases are elementary consequences. No independent coverage was needed from the inaccessible statistics papers to decide this issue.

## value

FAIL

The work-aware comparison is a sensible benchmark and may be useful as an application of known spectral allocation. As a standalone new finding, the main optimizer and value are the full-diagonal substitution into an existing stronger solution, and the equality cases, square-root limit and twofold gap follow by elementary algebra of that same substitution. No separately unresolved performance theorem or structural statement survives, and no substantive bounded repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
