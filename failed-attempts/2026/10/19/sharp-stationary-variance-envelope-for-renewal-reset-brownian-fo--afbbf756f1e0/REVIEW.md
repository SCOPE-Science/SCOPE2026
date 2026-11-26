# Independent mathematical audit

## correctness

PASS

At stationary time the current renewal interval is length-biased, with uniform age inside it. Conditional on the renewal process the different Brownian excursions are independent and centered; it is this conditional independence, not necessarily independence of marginal random-age samples, that is used for the cross-interval covariance. A lag h in the same interval shares Brownian covariance 2D times the earlier age. Integration of the admissible ages gives C_Y(h)=D E[(T−h)_+²]/m for h≥0 and C_Y(0)=Ds/m. The stationary convolution exists in L² by this finite force variance. Splitting the convolution square into the two lag half-planes yields the prefactor 1/μ in its covariance integral. Integrating the kernel gives F_μ(t)=t²/μ−2t/μ²+2(1−exp(−μt))/μ³. Strict Jensen for exp(−μT) and for the size-biased test (1−exp(−μt))/t proves exactly the open endpoint inequalities when s>m², since strict positivity of T makes the size-biased law nonconstant whenever the original law is nonconstant. For each a in (0,m), the proposed two-atom law preserves the moments because (m−a)(b−m)=s−m². At the two boundaries it respectively tends to the law with mass at zero, and loses its second moment in the weak limit as the rare upper atom diverges. Taking limits of the bounded Laplace transform at fixed moments gives exactly the two variance endpoints. Continuity supplies every intermediate variance. At s=m² only T=m is possible. The lag tests are convex and F_μ is strictly convex for positive arguments, giving the claimed fixed-mean order and unique deterministic minimizer. The independent replay used D=μ=m=1, s=2: Exp(1) gives V=1; for a=1/2, b=3, q=1/5, the variance is 1.009636117113, between 0.864664716763 and 1.264241117657; a=10⁻⁶ and 0.999 approximate the two endpoints from inside. Replay script and output: branches/ed9631dd-5a8d-4da8-ad09-0e51ed6734ee/independent_check.py and independent_check.txt. These are bounded checks. Frozen VERIFICATION.md and verify.py were inspected; the frozen script was not executed.

## originality

FAIL

The same-model mirrored Pareto-tail record explicitly gives the equilibrium stationary force covariance, the all-renewal variance identity, and the fixed-mean convex comparison and minimizer. At fixed m and s the whole envelope is an affine transform of the classical two-moment Laplace transform extremum, whose nontrivial sharp side and unique zero-atom law are explicitly in Guljaš–Pearce–Pečarić Theorem B. The opposite side is strict Jensen, and positive two-point laws joining the limits follow by solving the elementary two-point moment constraints. Thus the envelope is covered by combining checked results and routine consequences, even though neither source uses the exact displayed variance interval as its headline. This is a statement-and-implication comparison, not an inference about priority from dates.

## value

FAIL

Holding force intensity and renewal cadence fixed is a sensible physical comparison. In the frozen formulation, however, the only part beyond the covered model identities and comparisons is the affine re-expression of a classical sharp Laplace extremum, supplemented by elementary two-point interpolation. It does not provide a separate or nonroutine scientific result beyond those ingredients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
