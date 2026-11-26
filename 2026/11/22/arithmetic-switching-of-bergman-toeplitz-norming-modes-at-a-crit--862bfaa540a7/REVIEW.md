# Independent mathematical audit

## correctness

PASS

Bergman projection in the stated orthonormal monomials gives the squared weight (k+1)(k+d+1)/(k+m+1)^2; the self-commutator subtracts the displaced weight. The first branch increases strictly (factor the weight into two increasing positive ratios); the second is nonnegative, agrees at d-1 and tends to zero, so the norm is attained. Independently set r=m/n and s=(k-d+1)/n. The exact extended tail is F(r,s)=(r-1)(r-1+s)(2r^2+(r+1)s)/[(2r-1+s)^2(r+s)^2]. With P(r)=6r^3-13r^2+6r-1, its s-derivative has sign equal to that of -rP(r)-(r-1)(13r^2-1)s-3(3r^2-1)s^2-2(r+1)s^3. For r=rho+O_B(1/n) this is negative beyond s=C_B/n because the constant is O_B(1/n) and the linear coefficient stays strictly negative. This gives all-index localization, independently of finite sampling. At (rho,0), F_s=0, F_ss/2=G and F_rs=L; Taylor expansion at r=rho+b/n and s=ell/n gives the stated uniform second-order correction. The candidate set can be enlarged to contain both the exact and the quadratic maximizers, since G<0 and |b| is bounded. On the floor sequence 0<|G|<|L|<2|G|, checked by rational bounds on 1.60<rho<1.62, gives a uniform negative gap for ell>=2, even at theta=1. P has no rational root, so density of the irrational rotation gives infinitely many unique wins on either side of the strictly interior threshold. The winner within the O(1/n) boundary layer is not decided. Read RESULT.md, VERIFICATION.md and verify.py; the supplied script was not executed and its truncated finite search is not used to prove global localization.

## originality

PASS

Pass is confined to the bounded integer critical-window quadratic law, the order-n^(-2) norm correction, and repeated fractional-part switching between the two adjacent degrees in the floor sequence. The exact shift/eigenvalue formula, critical upper ratio and macroscopic transition are established antecedents. The materially closest primary work explicitly separates the continuous maximum from the discrete index problem.

## value

PASS

The critical ratio is intrinsic to the natural self-commutator and linked to an explicit open norming-index question. At the cancellation of the leading slope the arithmetic of integer degrees genuinely changes the winning mode infinitely often. The uniform bounded-offset lattice correction and exact eventual two-mode restriction supply meaningful information unavailable from the continuous transition, exact finite-eigenvalue formula alone or a finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
