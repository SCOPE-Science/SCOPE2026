# Independent mathematical audit

## correctness

PASS

The zonotope intrinsic volume identities are A_n=2 sum_{i<j}|U_i cross U_j| and V_n=sum_{i<j<k}|det(U_i,U_j,U_k)|. For s=|U_i cross U_j|, E s=pi/4, E s^2=2/3, and E(|det| conditional on first two directions)=s/2. Centered pair kernel b=s/2-pi/8 has Var(b)=nu/16; the degenerate triple kernel g=d-(s_ij+s_ik+s_jk)/2+pi/4 has Var(g)=kappa, is pair-orthogonal and has uncorrelated distinct triple indices. Exact Hoeffding decomposition implies the stated covariance, variance and correlation, including strict monotonicity from the positive constants. Independent direct simulation of 20,000 n=4 zonotopes computed area and volume geometrically and measured covariance 0.59167 versus theoretical 0.59780 (1.03% relative deviation); exact algebraic correlation identity checked at n=3,4,5,8,30,120. Simulation is only corroboration.

## originality

FAIL

FAIL: The November 1 2026 publication on isotropic 3D random-zonotope volume proves the identical exact Hoeffding decomposition V-EV=(n-2)sum_{i<j}b(U_i,U_j)+sum h3, where b=|Ui cross Uj|/2-pi/8 and h3 is the same fully degenerate triple kernel. Substituting the standard, already known surface-area formula A-EA=4sum b gives exactly this submission's proposed surface-volume orthogonal relation and covariance. The prior volume-variance computation already supplies the second-order variance; the remainder variance and monotone explicit correlation are immediate algebraic corollaries. The added presentation does not establish a new independent theorem.

## value

FAIL

FAIL: Although surface-volume correlation is a natural geometric question, its complete asserted answer is a short mechanical repackaging of the previously published exact canonical volume kernel and standard surface intrinsic-volume identity. No separate higher-dimensional classification, new boundary phenomenon, distinct conditional law or independently motivated unknown fact survives the stronger prior theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
