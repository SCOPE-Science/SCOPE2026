# Independent mathematical audit

## correctness

PASS

RESULT.md blob ba2787: in sector x=r(p_i+u e_i), n_i.p_i=Delta_i and n_i.e_i=0 give V_i=Delta_i(r-1) and exact ODE dot r=-c_i(r-1), r dot u=omega_i+(B_i^0+c_i u)(r-1), c_i=lambda_i||e_i||^2>0. For r<1 minimum angular numerator at u=1, for r>1 at u=0: strictly positive for all r>0 iff B_i^0>=0 and omega_i>=B_i^1. Violate B0 at large r or omega threshold near origin to prove necessity. Radial r remains in compact positive interval between initial r and 1, angular rate bounded above/below, so no stalled or Zeno switches. Integrating radial ODE yields exponential attraction; all sectors recur, so omega-limit is C; periodicity forces r=1. Floquet multiplier and T from edge times. Independent exact rational diamond confirms each Delta=1,B0=1,B1=3 with lambda=1,mu=-2,omega=4; T=1 and multiplier e^-2. Equality boundaries covered; no origin/Filippov assertions.

## originality

PASS

Kai (2026) primary introduces full three-parameter affine model but explicitly confines attraction result to small invariant annulus and does not claim global uniqueness. Published calibrated shape-conjugacy result has bounded exterior collar and B_i^0<0, cannot satisfy candidate global monotone-angular criterion. Earlier regular-polygon Filippov result takes mu=0 and sliding convention, while candidate proves no zero-shear polygon can have B_i^0>=0 on all sides because sum_i p_i.e_i=-sum||e_i||^2/2<0. No implication from these other results to sheared, all-plane, positive-transversal crossing regime.

## value

PASS

Establishes a sharp, nonempty computable global-positivity regime in a natural previously local-only polygonal oscillator model. Its shear necessity is a structural obstruction; the whole punctured-plane basin, uniqueness, rate and Floquet formula make it a meaningful exact global dynamics classification, not parameter relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
