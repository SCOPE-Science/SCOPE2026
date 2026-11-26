# Independent mathematical audit

## correctness

PASS

The strategy payoff difference is r(1-2n), the noise-payoff difference is -2r, and its square gives the 4r^2 factor in the correction. The normalization and time scales match Chen–Wu–Guan v2 Eqs. (4), (9) and (14); equation numbering should be tied to that version rather than to the first-public date or current numbering. The vector field preserves the closed square and its faces; uniqueness keeps initially interior trajectories interior at finite times. Solving the strategy nullcline at x=x_* or on n=0,1 gives the stated X,N and sharp k_c, including theta=1 with no boundary threshold. The weighted Bernoulli divergence has derivative -4s^2r^2k^2(x-X)^2+2sr(n-N)(X-x_*). The face term is nonpositive in both strict boundary regimes. Sublevels bound x away from both frequency boundaries and exclude the unselected environmental endpoint(s); for a selected face the entropy extends to that face. The largest invariant set of zero derivative is the target because x=X forces n=N to persist. At zero noise the entropy is proper and strictly convex, with a single minimum; each positive regular level is a closed curve without equilibria, hence periodic. For an independent check of the critical asymptotics, use oriented u=x-x_* on the upper branch and u=x_*-x on the lower branch, and let v>0 be distance to the selected environmental face. At k=k_c the exact equations are u'=-lambda(t)(u-kappa*v), v'=-H*v(1-v)*u, where lambda=4s^2r^2k_c^2*x(1-x), H=epsilon(1+theta), kappa=1/(2sr*k_c^2)=|theta-1|/(1+theta). The global result gives u,v->0 and lambda->lambda_*>0. Then q=u/v solves q'=-[lambda-H(1-v)u]q+lambda*kappa. The bracket is eventually uniformly positive and the forcing in the equation for q-kappa tends to zero; variation of constants gives q->kappa. Thus (1/v)'=H(1-v)q->H*kappa, which gives both displayed inverse-time coefficients for every interior start. `python /workspace/review_replay.py 3` independently checks the exact entropy identity and the two signed critical slopes, not the infinite-time conclusion by simulation. The result is for the deterministic ODE; weak-selection modeling does not validate arbitrary formal noise or stochastic paths.

## originality

PASS

The same model, donation payoffs, noiseless centers and locally damped coexistence are prior. The supported distinct result is the all-interior positive-noise selection theorem across the two boundary transitions, especially the critical resource and cooperator amplitudes. The usual entropy and linearization tools are not new. No inspected statement implied this complete model-specific result; this is not a priority certificate.

## value

PASS

The phase transition separates globally restored or depleted resource states from interior coexistence in the same deterministic model, a question not answered by a local damping calculation. The critical inverse-time amplitudes give measurable information about both variables and explain slow relaxation at the saturation threshold. These are global basin and rate results, not only an equilibrium root calculation; they do not claim biological validation outside weak selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
