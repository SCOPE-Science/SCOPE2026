# Independent mathematical audit

## correctness

PASS

A backward exponential age mixed with the voter semigroup started at fair product measure defines a stationary probability law, with the no-reset probability exp(-rt) bounding the difference between any two coupled histories. The finite-cylinder claim on Z follows from the usual finite backward random-walk ancestry of the rate-one voter process; spin flip, reflection and translation remain exact. For a pair, each coordinate makes two rate-1/2 proposals, giving (r+2)C_j=C_{j-1}+C_{j+1}, with coincident spins yielding C_0=1 (also C_N=1 on a ring). The roots q,1/q give the stated solutions with the two endpoint data or boundedness on Z. Conditioning independent mean-q Ising bonds on product +1 on a ring gives (q^k+q^(N-k))/(1+q^N) for any product of k selected bonds, including the bond sets representing U and V with k=2 and 3. Unconditioned independent bonds give the line formula. The finite spin Fourier basis then proves full agreement of marginals up to order three. For U, the rate-1/2 copy choices give four nearest-neighbour pair terms, two distance-three pair terms and two outward four-spin terms, related by i->3-i and valid also at N=5; all eight choices have the matching negative U terms. Fresh fair resetting subtracts rU. This gives (r+4)U=V+2C_1+C_3, and C_1+C_3=(r+2)C_2 yields the signed defect rC_2 and the stated bound. A distinct four-spin moment implies a distinct marginal. Independent exact full-state solves at N=5 and q=1/3,1/2,2/3 and N=6,q=1/2 checked the generator and witness; at N=5,q=1/2 they give C_2=C_3=4/11, U=V=32/77 and defect 2/11. Replay: python /workspace/branches/a1998109-b582-4937-88d3-2d934255904a/independent_generator_check.py (SymPy). These finite solves are checks only, not the all-rate or infinite-chain proof.

## originality

PASS

The single-time annealed stationary ensemble was already available through ordinary resetting of an iid-sampled fixed configuration. Neither that equivalence nor lack of detailed balance establishes a static distinction from nearest-neighbour equilibrium, still less its minimum correlation order. The inspected work supplies the resetting framework and pair/transient tools, not the specific exact Gibbs matching and positive local stationary defect. Best-of-knowledge comparison.

## value

PASS

This provides an exact all-rate separation between agreement of all low-order static marginals and actual equilibrium, with a signed combination of measurements from at most five adjacent sites. It identifies the first possible correlation order and a nonzero quantitative bound on the same ring or line without a full steady-state solution. This is stronger than nonreversibility and does not purport to distinguish Gibbs laws with arbitrary interactions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
