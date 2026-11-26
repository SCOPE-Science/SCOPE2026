# Independent mathematical audit

## correctness

PASS

Split into constant, mean-zero part-constant, and within-part mean-zero subspaces (dimension zero for a singleton). The original Laplacian is N on the second subspace and N−n_r on the r-th within-part subspace, so its spectral power gives the stated negative of the missing-edge entry and hence w_r. Homogeneous internal conductances change only the within-part eigenvalues, to Ne_r. The Heun polynomial R(z)=1−z+z²/2 is positive for all real z, so the propagator is positive definite with positive diagonal and, by the constant mode and symmetry, preserves row and column sums. With t=Nh, cross-part entries t(1−t/2)/N force t≤2. A within-part sign on 0<t≤2 equals the sign of (e_r−a_r)−t(e_r²−a_r)/2, positive at t=0 and equal to e_r(1−e_r) at t=2. This gives exactly the stated zero for w_r>1 and none below 2 otherwise. Every entry that becomes negative on its blocking interval stays negative beyond its zero until the cross-part entries alone forbid positivity. Nonnegative row-stochasticity is the maximum principle, and a negative entry gives a basis-vector witness. The derivative numerator for c_α is αa^(α−1)+(1−α)a^α−1>0 by strict weighted AM–GM (the weighted geometric mean is one); 0<c_α<1. Thus the smallest nonsingleton part first crosses w=1 at the stated β_*>1. With all e_r≤1, λ_max=N. With e_max>1, the blocking time for a part attaining e_max is strictly below 2/e_max in scaled time, by a_r(e_max−1)>0, giving a genuine spectral/positivity gap. Spectral stability means nonexpansiveness and includes the limiting eigenmode multiplier one at the ceiling. The complete graph has no internal-edge condition. The numerical K₂,₂ example was independently checked (~0.41018862 versus ~0.44590291). Inspected VERIFY.py and VERIFICATION.md; uploaded tests were not executed, and their scope is finite. No internal-stage positivity claim.

## originality

PASS

The key inputs are known: the scaled regularization, unweighted Heun plateau and weighted block spectral projectors. The closest prior does not give the exact amplified Heun threshold or the strict departure from spectral stability at the first conductance crossing. The weighted Gauss work is especially close in proof method, but its theorem concerns a different rational propagator. The additive positive-conductance change is not equivalent to scaling the original Laplacian or exponentiating its unregularized fractional power.

## value

PASS

This gives a complete, practical step criterion for a published nonlocal graph construction and explains exactly why a spectral timestep rule ceases to preserve the maximum principle. It identifies the first amplification at which an explicit pair of vertices witnesses the mismatch for every graph in the family, not just a conservative positivity bound or a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
