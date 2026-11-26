# Independent mathematical audit

## correctness

PASS

Put s=√h, d_i=1+isw_i. Taking the real part of (I+isL)⁻¹ gives R(h). The Schur complement at the hub is S=1+Σ isw_k/d_k, which lies in the open first quadrant. Inverting gives the hub–leaf entry isw_i/(d_i S) and the leaf–leaf entry −hw_iw_j/(d_i d_j S) before taking real parts. The argument in the first expression lies strictly between −π/2 and π/2. In the second, putting θ_i=atan(sw_i), the real part is nonnegative iff θ_i+θ_j+arg S≥π/2, since this sum is strictly below 3π/2. The minimum is the sum for leaves 1 and 2, allowing ties. For a term with z=w_k, its contribution to Re(d_i d_j S)/h is −w_iw_j+(z−w_i)(z−w_j)/(1+hz²); together with the initial term this gives exactly F_w. The remaining numerators for pair (1,2) are nonnegative, giving strict decrease, opposite limiting signs, and only one positive root. Bounding each summand from below by zero and strictly above by 1/h gives the bounds; equality at the lower end requires every remaining weight to equal w₂, and convergence of the summands to 1/h on compact positive intervals gives sharpness of the upper endpoint at high contrast. The empty sum gives the exact m=2 value. Positive definiteness gives positive diagonals; R(h)1=1 gives the norm criterion by the absolute row sum, and R(0)=I. An independent exact solve of the rational linear system (independent_resolvent_biclique_check.py) gives weak-leaf zero at h=1/6 for (1,2) and h=1/8 for (1,2,2), and entries −1/5726 and 38/8627 at h=1/6 and 1/5 for (1,2,3,7). Frozen verify.py was inspected, not executed. The proof concerns unit masses and positive conductances, not arbitrary trees, normalization or semigroup timing.

## originality

PASS

Credit is for the pair selector, explicit monotone resolvent equation and sharp weight-dependent endpoints. Qualitative eventual positivity is generic and a close same-day heat theorem has qualitative implications, but neither it nor the same-resolvent reentrant example derives those quantitative star statements.

## value

PASS

The theorem makes a sign constraint on a whole matrix an exact scalar test for all positive weights on a natural graph family. It locates both the recoverable step and the competing worst-case weights; with the two weakest conductances fixed the cutoff may grow by the sharp factor m−1. This distinguishes geometry-dependent contractivity from the mere fact of eventual positivity or the uniform-weight example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
