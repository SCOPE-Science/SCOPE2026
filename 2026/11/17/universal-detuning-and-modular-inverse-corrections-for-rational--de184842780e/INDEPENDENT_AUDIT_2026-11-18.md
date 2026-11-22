# Independent mathematical audit

## correctness

PASS

For fixed coprime k<n, n>=4, and bounded detuning σ, the reference half-grid orbit is separated from zero by 1/(2n), so all logistic tails are uniform on a fixed phase window. The two nearest sites give order-q corrections, q=exp(-a/(2n)); the positive first site contributes q exp(-u), and the negative site reached at t*≡-k^{-1} mod n contributes -q exp(u), while distant sites are O(q³). The normalized n-return H_a(u,σ) admits the stated uniform C1 expansion σ−2sinh(u)+q[2sinh(2u)−a(1+(t*σ/n) exp(u))]+O(a²q²). Strict negative ∂uH proves local unique zero and implicit differentiability; separation of sites gives primitive n-period. Solving for u and propagating the recurrence yields the stated cyclic coefficient B_j(σ), with O(q/a+a q²) spatial error; differentiated return gives 1−Λ=2aq cosh(z)+O(a²q²) and slope product n+O(aq). Independent exact modular itinerary reconstruction for n=4 yields k=1: [0,-3,-2,-1], t*=3 and k=3: [0,-1,2,1], t*=1, so the arithmetic distinction is genuine. Reviewed 105-digit mpmath diagnostic code covers 40 bounded cases, not the uniform asymptotic theorem.

## originality

PASS

Fresh best-of-knowledge primary-source and published-mathematics comparison of the exact final theorem, not a claim of exhaustive historical priority. The new coefficient is not implied by the σ=0 function value or n=3 profile; its derivation requires tracking the delayed negative-site tail and detuning along the full cyclic itinerary.

## value

PASS

The first detuning-dependent exponentially small position coefficient identifies an arithmetic memory of the rotation numerator absent from the universal leading arcsinh crossover. It resolves a natural perturbation boundary for a well-studied smooth surrogate of circle rotations, alongside sharp attraction and parameter-susceptibility scaling. The fixed-rational and period-three parts are explicitly credited and are not the novelty claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
