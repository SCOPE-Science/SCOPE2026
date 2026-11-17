# Independent mathematical audit

## correctness

PASS

For the complete mixed finite birth-death SIS chain with b_k=(N-k)(epsilon+sum_{j=1}^d c_j binom(k,j)), q_k=mu*k, epsilon>0, 0<epsilon<mu/N and nonnegative group rates, detailed balance yields pi_(k+1)/pi_k=b_k/[mu(k+1)]. The sign polynomial P(x)=b_x-mu(x+1) has P(0),P(N)<0 and degree at most d+1; each strict nonzero peak requires an internally positive sign component bracketed by two separate roots, hence at most 1+floor((d+1)/2) strict modes. This is an infinite-N root argument, not finite interpolation. For d=3 the explicit positive rational construction uses epsilon=(t+1/N)/2, t=(N-5)/[(N-1)(N-2)], c1=(L+U)/2, c2=(U-L)/2, c3=N+1 and gives edge signs [-,+,-,+,...,+], exactly peaks 0,2,N for every N>=4. The minimum N=4 follows from 5-state requirement. Exact N=4 probabilities independently verified as (8192,4096,4608,4416,5727)/27039. Boundaries with ties cannot create more strict peaks.

## originality

PASS

Best-of-knowledge originality follows from statement-level and implication-level comparisons; no identified complete earlier theorem covers the stated surviving exact result. See structured checks, inspected source material and risks.

## value

PASS

The smallest higher interaction order allowing *three finite stationary probability modes* and the minimum population size are mathematically motivated sharp structural cutoffs. Finite seeded stationary laws differ from deterministic endemic mean-field attractors; the strict-mode ceiling and uniform positive-channel witness identify when higher-order contagion permits a qualitatively new stochastic shape, and are not merely a parameter rename.

The dated certificate retains the supplied scientific assessment, sources and limitations.
