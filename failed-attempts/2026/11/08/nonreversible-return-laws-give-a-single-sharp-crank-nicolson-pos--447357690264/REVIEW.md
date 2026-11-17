# Independent mathematical audit

## correctness

PASS

For finite row-conservative Markov Q, the M-matrix resolvent R_s=(I−sQ)^{-1} is stochastic and nonnegative; Cayley C_{2s}=2R_s−I makes only diagonals possible sign obstructions. For uniformization P=I+Q/λ with z=λs/(1+λs), first-return generating function F_i(z) gives R_{ii}=(1−z)/(1−F_i(z)) and 1/R_{ii}=a_i/(1−z)+Σ_{n≥1}f_{i,n}Σ_{k=0}^{n−1}z^k. This inverse increases strictly for every nonabsorbing state, including transient defective-return mass a_i>0; absorbing states retain 1. Its limit is zero for transient states and their normalized closed-class stationary probability for recurrent states. Thus every diagonal meets 1/2 on an initial interval, producing one global threshold. H=∞ iff every state recurrent with closed classes of size ≤2 and balanced pair rates. For directed unit-rate 3-cycle, independent exact inversion yields R_{ii}=(1+s)^2/(1+3s+3s²) and cutoff H=1+√5. Fresh SymPy checks confirmed this formula, both reducible examples, and diagonal monotonicity at six rational s values. Finite examples are only confirmation; arbitrary generator proof is renewal monotonicity.

## originality

FAIL

FAIL: the claimed universal nonreversible return-resolvent mechanism, single-interval frontier for all irreducible chains and directed three-cycle constant were already published on Nov2 and in the stronger Oct12 θ-method result. The sole remaining reducible extension is the standard defective-first-return/closed-class corollary of that mechanism, not independent originality of the central claim.

## value

FAIL

Classifying Markov integrator positivity is valuable generally, but the earlier two full results already supply its defining stochastic renewal mechanism, all irreducible nonreversible sharp thresholds and the directed-cycle example. Adding transient/closed-class decomposition to the same monotone return identity is routine Markov-chain bookkeeping, with no mathematically new boundary or needed invariant beyond those prior results. The proposed final claim is therefore a correct but substantially covered recombination rather than an independently worthwhile finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
