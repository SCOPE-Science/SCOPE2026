# Independent mathematical audit

## correctness

PASS

For the stipulated scalar ODE, f=(1-x)P-1 has degree M and f(1)=-1. Local asymptotic stability at an interior zero requires a positive drift just left and a negative drift just right, even when the zero is not hyperbolic, since a nonzero polynomial has isolated zeros. Each pair of consecutive attractors therefore costs an intervening zero; 2k-1<=M gives the claimed bound. In the proposed construction the coefficient sum bound follows from the product of one plus each small positive root of Q. The geometric-series baseline gives exactly -x^M; at each of the M interleaved test points all factor distances are at least delta/(2M), so the perturbation dominates by at least 4(1-delta)>1. The alternating signs and the negative right boundary yield M distinct interior roots of a degree-M polynomial, necessarily simple. Working leftwards from the right boundary gives exactly ceil(M/2) attractors, and the strict signs persist on an open positive-coefficient neighborhood. The sign at x=0 has the stated even/odd orientation. Inspected RESULT.md, VERIFICATION.md and verify.py. The rational sign certificates for M=2 through 12 are supplementary and were not rerun. This verifies the scalar theorem only, not an all-order rigorous stochastic-to-mean-field limit; the cited source treats the latter as conjectural.

## originality

FAIL

A distinct October 25 indexed record already establishes the sharp all-order count and the stronger realization of any prescribed set of M simple interior roots with sum below one. Normalizing recovery gives the same scalar polynomial. As those roots coalesce toward zero, the coefficients of P converge to one because f(1)=-1 fixes the multiplicative factor and P=(1+f)/(1-x). Openness is automatic for the simple interior roots in the strictly positive coefficient region. The same-day exact inverse-design entry is a further mathematical match, not used to infer temporal priority. The strongest earlier index evidence, rather than the equation's appearance by itself in prior papers, decides the failure.

## value

FAIL

The source's all-order question is mathematically motivated, but the frozen answer supplies no distinct structural consequence beyond prior arbitrary simple-root placement. The coefficient-near-one condition is the small-root limit of the already determined factorized polynomial, and openness is routine simple-root continuation. The alternate sign-interleaving construction and finite examples do not add a mathematically useful new regime or remove a restriction of the prior theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
