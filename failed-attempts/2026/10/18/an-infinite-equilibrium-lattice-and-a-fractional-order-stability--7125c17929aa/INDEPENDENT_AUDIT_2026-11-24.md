# Independent mathematical audit

## correctness

PASS

The constant-sequence equation is G_c=0. If c>1, y≠0 fixes x=±√(1−1/c); solving the sine equation gives all four branches. With x positive the positive-determinant ordinates are y=(−1)^j(j+τ), and central reflection supplies exactly one more point per level. The trace is −1; negative determinant gives a positive root. At determinant 1/4 the repeated root is −1/2. The scalar generating function has denominator (1−z)^ν−zλ, with its unit-circle boundary obtained by setting z=e^{it}. Each ray in the allowed angular sector has one nonzero boundary radius, with the stable component on the inner side. At a nonzero boundary eigenvalue the uncancelled pole is simple: a double zero would require 1+(ν−1)z=0, impossible there. Decaying coefficients cannot have such a pole, by the radial Abel limit. In the stable interior the only possible closed-disk singularity is at z=1, where the nonzero eigenvalue keeps the denominator invertible. The local generating function is (1−z)^{ν−1} times a bounded analytic-in-powers factor, giving decay O(n^−ν) for ν<1; the same argument applies to the higher resolvent power of a Jordan block. At ν=1 the criterion reduces to ordinary disk stability of 1+λ. On the trace −1 complex pair, the eigenvalue radius increases and the allowable radius decreases, so there is exactly one crossing. The comparison at determinant 1 gives equality at ν=1 and strict stability at ν<1. The strict integer count gives the ceiling, and monotonicity of each level gives unique thresholds. With h=√(c−1), τ=arctan(h)/π=O(h); the level equation gives h=(Dν/(2π))/j+O(j^−3) and hence the stated O(j^−4) remainder for c−1. The origin cases follow directly from eigenvalues −1 and c−1, and at c=1 each stationary point (0,k) has a zero eigenvalue.

## originality

FAIL

There is verified equivalent coverage in a distinct indexed record, 2026/11/22/SCOPE-fractional-memory-stability-staircase-and-inverse-square-accumul--83f0e50e0fe3. Its finding and proof cover the same recurrence, same all-real stationary branches, paired positive determinant levels, sharp strict cutoff, exact ceiling count, and inverse-square threshold accumulation. The stronger-looking remainder follows directly from its exact threshold equation. This is a statement-level coverage decision, not a conclusion that the indexed record predates the frozen work or that one derived from the other.

## value

PASS

As a classification, the all-real equilibrium lattice and exact strict-order staircase answer a natural question left by a principal-branch treatment. The count quantifies how more stable equilibria emerge near c=1 and distinguishes infinitely many equilibria from finitely many stable ones at each fixed parameter. That mathematical usefulness does not add new value relative to the equivalent indexed theorem and does not cure the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
