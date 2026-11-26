# Independent mathematical audit

## correctness

PASS

In the basis (v,w), write the first column of B as (b,0). The Gram equations are |b|²=β, conjugate(b) B₁₂=c, and |B₂₂|²=t−|c|²/β. The Schur complement is nonnegative, and these conditions give exactly the displayed family, including the redundant second phase when h=0. Each Kraus term multiplies the ww entry by the squared modulus of its lower diagonal entry, so the exact rate is η=|d_L|²+|d_R|²+h². Kraus completeness gives the asserted alternative formula; at least one of u_L and u_R is nonzero, so η<1. Stationarity forces the ww entry and then the off-diagonal entries to vanish. For a qubit density with ww entry p and off-diagonal entry z, the trace distance is 2√(p²+|z|²)≤2√p by positivity. The case n=0 is the identity, also when η=0. The direct recurrence reference is Loebens Theorem 5.2(1): the three Kraus operators share exactly one eigenray, the unique invariant density is P_v, and the balance test gives |ℓ|²=|r|² for divergent return occupation for all initial densities. Theorem 3.8 phrases the hypothesis as ergodicity; citing 5.2(1) avoids any ambiguity.

## originality

PASS

Limited to the explicit fixed-(L,R) parameterization written together with its phase-independent population law. The drift classification itself is covered; the original source motivates the completion problem and gives an example but does not give this formula for the full ray-preserving family. No equivalent explicit result was identified in the inspected scope. This does not claim priority for triangular Gram factorization, the population identity for triangular channels, or the recurrence theorem.

## value

FAIL

The cited fixed-jump design question is meaningful, but the frozen restriction assumes the very shared ray on which the prior recurrence test already reduces to balance, regardless of which admissible stay is used. The remaining parametrization is the standard two-column triangular Gram factor with its diagonal phases, including the zero Schur-complement case. Its rate is forced by a single matrix entry of the Kraus action, and the distance estimate is the generic pure-state bound. Thus the record gives a useful worked specialization, but no substantive additional mathematical step on the design question: in particular it does not decide recurrence of stays that mix the ray. This is a routine deduction rather than a new classification of recurrent stays or an independently nontrivial exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
