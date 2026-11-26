# Independent mathematical audit

## correctness

PASS

An interior equilibrium has u<U and u>m/(cb), so b>b₀ is necessary. On the predator nullcline v=(cbu−m)/η, the prey per-capita equation strictly decreases in u and has opposite signs at m/(cb) and U, proving sufficiency and uniqueness. Its two-equation Jacobian has positive determinant −ηF_u−cbF_v; implicit differentiation gives u_b′=(−ηv_b+cu_bF_v)/det J<0. The bounds on u squeeze it to U as b↓b₀, and bv_b<r and the predator equation give (u_b,v_b)→(0,0) as b→∞. Eliminating b and multiplying by u gives the stated f. For each 0<u<U, f(u,0)>0 and f decreases to negative infinity in v, so it defines a smooth positive graph v=q(u) with zero endpoint values from the limits of the equilibrium branch. At a stationary point q″=−f_uu/f_v<0 since both partial derivatives are strictly negative. A positive interior maximum exists, and two strict maxima would force an interior minimum, which violates that sign. The sole maximum therefore has the stated derivative signs on both sides; the decreasing u_b reverses their order and transfers strict curvature as q″(u_*)(u_b′)^2. Restricting b to (b₀,β] gives exactly the stated refuge maxima including β=b_*. At the witness, det J=32, u_b′=−1/4 and q″=−11/20, giving −11/320. The logistic estimates bound trajectories for each b, but no convergence or management conclusion is needed here. Frozen checker.py and VERIFICATION.md were inspected, not executed; they are a replay of the witness and finite examples, not of the universal proof.

## originality

PASS

The model, invasion threshold, uniqueness of coexistence, and qualitative possibility of intermediate-attack peaks are not claimed as new. The supported distinct claim is a parameter-uniform theorem of exactly one nondegenerate maximum for the rational fear/crowding and predator-interference equations, together with the feasible refuge classification. Neither the same-model stability papers/records nor the verified local parameter sweeps yield that cross-parameter theorem.

## value

PASS

The proof replaces range-dependent sensitivity plots with a global, nondegenerate classification valid for every admissible positive parameter set. It determines exactly when positive refuge maximizes equilibrium predator abundance and distinguishes that effect from the monotone prey response, with an exact interior witness. That is useful within this model even though the qualitative overexploitation mechanism is familiar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
