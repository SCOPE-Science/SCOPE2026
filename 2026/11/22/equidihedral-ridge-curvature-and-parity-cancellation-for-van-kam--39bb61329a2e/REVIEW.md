# Independent mathematical audit

## correctness

PASS

Reassessed the complete corrected RESULT.md. In the frozen proof, line 53 says an odd-order polar edge moves the zero while changing the sign of the moved entry. Such a sign change violates the zero-sum constraint. The repair classifies edges directly: at an edge interior n-2 cube coordinates are fixed, and the two free coordinates have prescribed sum S in [-1,1]^2. Even order gives S=0 and endpoints (1,-1),(-1,1); odd order gives S=±1 and endpoints (0,S),(S,0), so the sign is preserved. Direct binomial counting of fixed coordinates/signs gives both published counts without alteration. An independent bounded enumeration of those coordinate segments for n=4–8 gave counts 12,60,90,420,560 and squared endpoint separations 8 (even) or 2 (odd); the original code was inspected, not executed, and already uses shared-coordinate constraints rather than the erroneous prose rule. Squared normal norms n and n-1 give the exact cosines. The dual ridge has N=n-2 signed vertices with balanced or almost balanced signs, one congruence orbit, and positive definite Gram I-ss^T/n. Its determinant is 2/n and 1^TG^(-1)1=N+(sum s)^2/2, giving the displayed Euclidean simplex volume. The sector-angle weight alpha/(2pi) gives V_(d-2), not the unnormalized t² coefficient; n=4 gives V_1=3. Stirling estimates and arccos expansions give the common leading constant sqrt(2/pi)/(4pi). All numeric conclusions survive the correction. The proof applies only to the stated canonical Euclidean realization; the recorded finite checks do not establish the all-n theorem.

## originality

PASS

The repaired claim preserves the exact Euclidean ridge geometry, codimension-two intrinsic volume and parity-canceling leading constant. The body, its polar model and the cube-slice combinatorial premises are credited rather than presented as independently new; the surviving distinct result is the metric synthesis, in particular the exact Steiner invariant and its leading asymptotic.

## value

PASS

The repaired proof resolves the first ridge-based Steiner curvature coefficient of a canonical polytope family previously studied for volume, convex duality and parity. It explains both the rigidity of each ridge geometry despite the different facet structures and why the two parity classes, with distinct angle and census scales, have the same normalized leading curvature. This makes the exact curvature useful for comparing this family across dimensions. The value is not the already-known polar model or routine counting by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
