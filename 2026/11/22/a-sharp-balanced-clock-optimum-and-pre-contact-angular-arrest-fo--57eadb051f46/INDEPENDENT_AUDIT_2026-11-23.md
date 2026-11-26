# Independent mathematical audit

## correctness

PASS

The normalized degree-at-most-four family is the Cao–Llibre normal form. An independent check of completeness is to complexify each circle using U=Z-Z_i and W-W_i=r²/U. Tangency bounds the Laurent exponents of its angular velocity by [-3,3]. The vector field vanishes at the two transverse complex intersections with each of the other two circles (there are no triple intersections for r<1/2). Dividing by the other two circle factors leaves exponents [-1,1], hence an affine A_i. Subtracting the resulting sum of three tangent fields leaves a constant vector times the product of the three circle factors. Comparing the leading homogeneous terms and projecting radially forces this vector to vanish and the sum of the A_i gradients to be zero. At the next degree, M=Σ C_i(grad A_i)^T must send every direction to itself, hence is a scalar matrix; the sum of the intercepts is minus that scalar. Solving with the three given centers recovers exactly the displayed form. On the circles the angle speed is (ω_i−2r cos(t)/√3) times the two strictly positive power factors; their angular shifts are ±π/6 because the negative A_i gradient points along the inward bisector at each vertex. The positive means must each exceed 2r/√3 and sum to 1, giving the strict cutoff, with a zero speed at equality for the balanced field. The period is strictly decreasing in its own mean, so maximizing the minimum mean uniquely yields the balanced parameters. With ε=2√3(r_c−r), the optimal integrand is asymptotic after rescaling t=√(2ε)z to 12/[ε(1+z²)]; the complementary angular interval is bounded and the rescaled integrand has an integrable Cauchy bound. This gives the stated coefficient, with no factor lost from the normalization. For a direct Floquet sign check on circle 1, integrate the cofactor of f_1 against physical time. Reflection t↦−t interchanges the two dependencies on the other circles and cancels the nonconstant parts of A_2 and A_3, leaving (ω_3−ω_2)∫(log f_2)'/A_1 dt. Integrating by parts and pairing t and −t gives a strictly positive integral factor because A_1'=κr sin(t) and f_2(t)>f_2(−t) on (0,π). Cyclic symmetry gives the other signs. Balance is neutral and the stated perturbation separates all means while remaining feasible, proving the strict, unattained hyperbolic infimum. This analytic replay uses frozen RESULT.md, §§1–4; VERIFICATION.md and verify.py were inspected as diagnostics, not executed or used to establish the global claim.

## originality

PASS

No inspected independent source covers the normalized physical-period minimax and its singular asymptotic or the resulting hyperbolic infimum. The degree-four normal form, orientation criterion, neutral condition and the feasibility cutoff as an immediate specialization are covered inputs, not standalone original contributions.

## value

PASS

With the time-scale fixed, the worst-period optimum is a natural global question about the complete degree-four family. The exact optimum separates loss of angular motion from geometric contact and determines its physical-time scale. The hyperbolicity constraint materially changes attainment but not the sharp bound. This is useful beyond the simple radius-cutoff deduction from the existing inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
