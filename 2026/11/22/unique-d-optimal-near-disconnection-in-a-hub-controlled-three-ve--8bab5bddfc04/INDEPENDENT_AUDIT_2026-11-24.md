# Independent mathematical audit

## correctness

PASS

The positive damping shifts the weighted star spectrum to μ, μ+S±√(S²−3uv), distinct for the positive spokes. In modal coordinates the Lyapunov Gramian has entries bᵢbⱼ/(αᵢ+αⱼ). The Cauchy determinant cancels the squared Vandermonde in the Kalman determinant, whose modulus is uv|u−v|, leaving the denominator product stated in (1). Independently, solving the nine Lyapunov equations modulo 1009 for (μ,u,v)=(1,1,2),(2,2,2),(3,5,11),(7,3,17),(2,13,7) gave determinant residues 983,0,522,111,371, agreeing with (1); these checks do not replace the identity. The product x=uv/S² parametrizes unordered positive pairs. The objective is positive between its zero boundary values 0 and 1/4. Its log derivative is −Qτ over a positive denominator. The positive quadratic coefficient, negative constant and Qτ(1/6)>0 give a unique positive root in (0,1/6), with a change from increasing to decreasing. The resulting unequal optimum has exactly two labelled allocations. The log derivative increases strictly with τ at every fixed interior x, forcing the zero rightward. Substituting x=τz and dividing Q by τ² gives limiting polynomial 9z²−12z−16 with a simple positive root c. At large τ the log derivative tends to 2/x−4/(1−4x) with derivative −216 at 1/6, and its first damping correction is −9/(2τ²), giving −1/(48τ²) in the root and O(τ⁻³) remainder. The weaker solution of z(S−z)=S²x is Sx+O(Sx²). Substitution in (1) gives the displayed (5√5−11)/(1152μ²S), whereas any fixed unequal positive pair gives a positive constant times μ⁻¹. The undamped integral itself is not finite. The packaged checker was reviewed, not executed.

## originality

PASS

Credit the Gramian-volume objective and the general Cauchy/Krylov reduction. The supported distinction is the exact all-damping optimizer and strict monotonicity for an undirected hub-controlled star under the fixed spoke-sum constraint. A directed-chain record also covers the weak-damping mechanism: after spectral matching it can even be used to recover the leading optimum value. It does not give the finite-damping star optimization, because the matching changes the feasible spectrum and multiplies the determinant by a nonconstant factor. No ordering is inferred from the common publication date.

## value

PASS

For the smallest undirected star allowing a nontrivial split of a fixed conductance, this fully resolves an explicit determinant design for all damping ratios, not a numerical sample or a fixed-damping slice. It separates volume from intuition based on equal mixing weights and shows the unique unordered optimum approaches disconnection while maintaining controllability. The increasing normalized product and sharp asymptotics quantify the transition and the fixed-design penalty without claiming larger-network optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
