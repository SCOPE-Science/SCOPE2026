# Independent mathematical audit

## correctness

PASS

For the closed nondegenerate circular cone the polar half-angle is β=π/2−α. On S³ the polar-angle density is (2/π)sin²θ, so the two cap integrals give v₀ and v₄ in the record. The published circular-cone interior formula gives v₁=cos²α/2, v₂=2sinαcosα/π, v₃=sin²α/2. These are positive and sum with the caps to 1. Substitution yields R(β),16/π²,R(α) for the three quotients. For R, x−sin x cos x is strictly positive by its derivative 2sin²x. The numerator of its log derivative with the stated positive denominator is x(1+2cos²x)−3sin x cos x. It vanishes at zero and its derivative is 4sin x(sin x−x cos x)>0 since sin x−x cos x=∫₀ˣu sin u du. Thus R strictly increases from 3π²/16 to infinity; 4/3<3π²/16<2 and 3/2<16/π²<9/4. Since β decreases with α, only k=1 crosses, with equality just at the unique interior threshold, and k=2 obstructs binomial ULC throughout. The excluded endpoints have changing support. The exact threshold and numerical values agree with independent 75-digit bisection on the cross-multiplied equation (/workspace/cone_replay.py): β≈0.5861771479686967924, α≈0.9846191788261998268 radians ≈56.41452337437811814°. This decimal check is not a root-uniqueness proof. The frozen checker was inspected, not run. Bibliographic clarification: ALMT arXiv v2 locates the interior formula in App. D.1, Eq. (D.2); the difference from the frozen locator is not a mathematical error.

## originality

PASS

Pass for the complete sharp Poisson-ULC aperture classification, not the known intrinsic-volume formulas, specific π/3 violation, or the immediate all-aperture central binomial obstruction. The closest earlier limitation gives one counterexample and not the threshold. The known formulas reduce the problem to a scalar inequality but a global monotonicity and endpoint proof are needed to establish the unique transition and the index classification.

## value

PASS

In the very family used to disprove general Poisson ULC, a sharp classification answers which apertures still satisfy it, identifies the only failing index, and distinguishes the two normalizations. The exact boundary and equality case are meaningful benchmarks for questions about conic intrinsic volumes; value is not assigned merely to the numerical cutoff or to the easy central quotient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
