# Independent mathematical audit

## correctness

PASS

The normalized conditional OU variance has the stationary representation Uτ=∫_{−∞}^τ exp[−(τ−h)] q^{N(h,τ]} dh (0⁰=1), where N counts common jumps in dimensionless time. This gives the flow, contraction and boundedness; past initialization errors vanish at least exponentially. For q=0, U=0 at jump instants, but U>0 almost surely at any fixed observation time. Independent Wiener noises make the conditional mixed moments at three distinct labels products of U at the respective times. The generator gives m₁=1/A, m₂=2/(AB), m₃=6/(ABC). With Z=U−m₁, P_s Z=e^(−As)Z, and L(Z²−V₂)=−B(Z²−V₂)+2(1−m₁Δ)Z. Solving this triangular system gives P_s(Z²−V₂)=e^(−Bs)(Z²−V₂)+H(e^(−As)−e^(−Bs))Z. Conditioning on the last gap thus gives C(s,t)=e^(−At)[H V₂ e^(−As)+(K₃−H V₂)e^(−Bs)], where K₃=m₃−3m₁m₂+2m₁³. Substitution factors H V₂−K₃ as T>0 exactly as in RESULT.md. The difference between lag orders has the strict sign of exp(−Δt)−exp(−Δs); the sign-controlling bracket in C increases strictly in the first gap toward H V₂. Its initial sign is that of θ(1−q²)−1, giving the stated unique positive zero below threshold, zero only at first gap zero on threshold, and no zero above. The physical first-gap time is s*/(2κ). Replay the generator and moment steps at RESULT.md lines 42–85 or via the centered hierarchy above. The two frozen scripts were inspected, not executed. Monte Carlo is not support for strictness; the simulated initialization uses a finite jump history.

## originality

PASS

The matched static third-cumulant threshold and known pair-energy covariance are not counted as new. The supported distinction is the exact ordered three-time law, its strict orientation for unequal gaps and the unique first-gap zero in the subcritical regime for arbitrary nontrivial common contractions. The complete-reset catalogue result is a distinct same-day overlap at a static slice, not an inference about date priority.

## value

PASS

Distinct-label pair energy correlations in this identical-trap model are time symmetric, so they cannot serve as this directional diagnostic. The three-label connected observable resolves the orientation for every positive rate and every nontrivial contraction; it also separates a short-first-gap negative regime from a positive regime by an exact, measurable lag boundary. The result needs only three trajectories and treats the exact shot clock, not a many-particle or weak-reset limit. It neither measures entropy production nor establishes finite-sample detection power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
