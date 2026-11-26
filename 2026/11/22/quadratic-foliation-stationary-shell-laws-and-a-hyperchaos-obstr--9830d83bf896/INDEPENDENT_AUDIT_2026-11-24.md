# Independent mathematical audit

## correctness

PASS

The absolutely continuous chain rule gives d[w−(x²+y²)/2]/dt=0 across both regions, almost everywhere, and the inverse coordinate change adds (x²+y²)/2 to J. Direct differentiation gives the two coboundaries in the frozen proof; the derivative of |x| equals σ(x)y almost everywhere in time, including on any positive-measure switching level set where y=0 almost everywhere. Integrating over time and using invariance and compact support annihilates the coboundaries. If the y² moment vanishes, invariance and continuity give y=z=0 on almost every stationary path, and the third equation forces x=±1, so there is no non-equilibrium exception. For c<0 the required positive average of x²−|x| forces mass outside |x|≤1. For c>0, Cauchy–Schwarz and E|x|>E x² imply E x²<1. The upper activity bound is strict because equality in |x|−x²≤1/4 would confine stationary continuous paths to x=±1/2, impossible for equilibria. The z² bound follows from the first balance. In the product coordinates, the J direction is exactly fixed. At each transverse crossing the base saltation is a rank-one shear with unit determinant because the jump is tangential; smooth trace −a therefore gives the base determinant exp(−aT). The flow direction supplies the other unit multiplier on a periodic orbit. Under the stated regular-cocycle hypotheses it likewise has zero Lyapunov exponent: on a non-equilibrium compact ergodic trajectory recurrence to a positive-speed set and bounded speed give limsup of its growth rate zero, which is the exponent if the limit exists. The two remaining exponents sum to −a. A separate symbolic replay reproduced the local algebra; see /workspace/branches/4f722b5b-9c75-4a46-ad29-eee09055dba5/record4_replay.py. The supplied checker was inspected, not run. Neither check establishes global well-posedness or excludes grazing or irregular cocycles.

## originality

PASS

The model and general variational methods are prior. For the exact printed four-dimensional system, the surviving contribution is the explicit global reduction combined with the two stationary shell laws and a proved regular-dynamics restriction, not a general theory of saltation or a claim that first integrals are a new way to find neutral directions.

## value

PASS

The exact reduction gives a testable correction to a published hyperchaos interpretation, with no numerical surrogate needed. The two stationary balances apply beyond individual periodic orbits and add quantitative, sign-dependent restrictions on recurrent states. The work is valuable as a model-specific structural correction even without an existence or global switching theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
