# Independent mathematical audit

## correctness

PASS

Exponential-time Brownian displacement has MGF M(s)=1/((1-as)(1+bs)). The two-sided Poisson construction at a deterministic observation time gives Y=xi+C Y' in law with independent terms; the backward expansion converges in L² by the triangle inequality and E[C²]<1. Synchronously coupled starting values contract almost surely, because for some rho<1 marks C<=rho occur infinitely often. For necessity, the MGF of C Y' equals (1-as)^(1-p)(1+bs)^(1-r) on (-1/b,1/a); if either shape is below one, this would tend to zero at the corresponding finite endpoint, impossible by Fatou's lemma applied to the positive exponentials. Deconvolution gives gamma shapes (p-1,r-1) for C Y', interpreting zero shape as a point mass. If just one shape is one, the deconvolved law is nonzero but one-sided, inconsistent with nonnegative C and the two-sided Y'; if both are one it forces C=0. With both shapes greater than one there is no atom at zero, so C preserves sign. Gamma-ratio sign probabilities reduce to the beta CDFs at x=b/(a+b); differentiating the displayed difference in (3) and checking its zero endpoint verifies the identity for all real p,r>1. Its only interior zero forces b(p-1)=a(r-1). For sufficiency use H(s)=theta*integral_0^1 t^(theta-1)V(ts) dt for both signs of s (equivalently the printed s^(-theta) expression for positive s). Then sH'=theta(V-H); the proposed deconvolved MGF satisfies this with H(0)=1 by direct differentiation, and power series determine each coefficient since theta+k>0. The transforms therefore solve the fixed point. Finally the even moment ratios determine the law of C² on [0,1], hence C. This is an analytic audit for all real shapes in scope, not an inference from the frozen finite moment checker, which was inspected but not run.

## originality

PASS

The supported distinct claim is inverse rigidity for arbitrary nonnegative contraction laws at the asymmetric excursion scales, including the two-sided shape obstruction and uniqueness. General Poisson-reset perpetuities, the exponential-excursion law and beta-gamma calculus are prior tools. A Poisson shot-noise construction also explains existence on the balanced ray when beta marks are imposed; existence alone is not credited as a new standalone result. No available prior statement establishes necessity over arbitrary C at these asymmetric scales.

## value

PASS

This closes a natural inverse classification: at the two scales intrinsic to the drift-diffusion excursion it determines exactly which targets can occur and diagnoses the unique reset distribution, including a boundary obstruction that is invisible in symmetric special cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
