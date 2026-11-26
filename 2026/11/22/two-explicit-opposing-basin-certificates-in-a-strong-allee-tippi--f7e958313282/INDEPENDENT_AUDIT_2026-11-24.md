# Independent mathematical audit

## correctness

PASS

The axes are invariant and the logarithmic equations preserve positivity for positive data. Since f(u) is bounded above by F=(1-a*phi)^2/(4*phi), exponential bounds on u over finite intervals give finite v bounds as well, proving global existence. The Jacobian at extinction has eigenvalues -a/epsilon,-1. At coexistence its trace is f'(1)/epsilon=[1-phi*(2-a)]/epsilon<0 and determinant v_*/epsilon>0. For the coexistence certificate the predator-prey cross terms cancel, giving Hdot=(u-1)[f(u)-f(1)]=-phi*(u-1)^2*(u-u_c). The admissible range gives a<u_c<1. On u<=u_c the prey contribution to H is at least B, and at (u_c,v_*) equality holds. Any larger strict sublevel contains this point (and points on its left), proving sharpness for containment. Before a first approach to u_c the entropy is nonincreasing, so a solution in H<B stays in its compact initial sublevel in the positive quadrant. The only invariant set of Hdot=0 therein is (1,v_*): at u=1 the prey derivative is (v_*-v)/epsilon. Thus LaSalle applies. With u<=a and v>0 the prey enters/stays below a and decreases; a positive limit is ruled out by the uniformly negative f on any interior compact interval below a. Once u->0, v decays exponentially. For u_0>a the bounds v(t)>=v_0 exp(-t) and f<=F yield epsilon log(u/u_0)<=Ft-v_0(1-exp(-t)). Minimizing (Ft+c)/(1-exp(-t)) gives the sole minimum at exp(T)-1-T=c/F, since the left side is strictly increasing from zero; the minimum is F exp(T) and exp(T)>1 selects W_{-1}. This is sharp only for the stated scalar comparison operated as a strict upper bound test, not for the true separatrix. At a=1/2,phi=4/5,epsilon=1/10, u=4/5, the entropy inequality at v_*=1/10 follows from u_c=3/4<u<1, and the fold is 7/8. For v_0=1/4 use t=4/5: the order-six alternating upper bound on exp(-4/5) and the order-seven upper bound on log(1+3/5) make the required strict comparison an exact rational inequality. Independent replay (python3 -B /workspace/branches/independent_replay.py 3) confirms that inequality, the symbolic cancellation, and yields 0.2487838970931023 for the comparison threshold. The frozen checker was read, not executed; no finite integration is used to prove either basin claim.

## originality

PASS

Pass the two explicit quantitative membership tests, including their precise method-limited bounds, for the frozen polynomial flow at all positive epsilon. The flow itself, its bistable geometry, the fast fold, extinction below the Allee threshold, and extinction-above-separatrix criteria are prior, including under exact rescaling. Neither inspected same-flow phase portrait supplies the explicit pair of inequalities for specified initial data. The proof methods are classical and are not credited as new.

## value

PASS

The gap is practical within the mathematical model: local stability and a separatrix defined as an invariant manifold do not tell a reader which outcome is guaranteed at a specified positive initial state without further calculation. The two explicit, complementary sufficient tests answer that question on distinct computable regions uniformly in positive epsilon; they distinguish outcomes at the same prey below the fast fold, where treating the fold as a basin boundary would be misleading. The value is in explicit certified regions and their precise method-limited thresholds, not a full basin partition, ramp-rate threshold or stochastic extinction claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
