# Independent mathematical audit

## correctness

PASS

The gradient step is 1/(m+h u), where u=p3-p1; reusing it twice gives the fourth power weights in the record. In coordinates (u,y) with y=p2, the normalizer is S=1-y+(2-6y)u²-3u⁴. The numerators for (u',y') are u(u⁴+6u²+1)-4u(1-y)(u²+1) and y u⁴. At u=±1/√2,y=1/4, these give (−u,y) with S=1/4. Quotient differentiation gives J(u)=[[5,8u],[7u,5]]. Thus J(−u)J(u)=(25−56u²)I=−3I; the change to (p1,p2) is affine and leaves that scalar derivative unchanged. Smoothness near the orbit gives repulsion for the return, not an assertion about the global fate of perturbed trajectories. Radial contraction is over the full period: the gradient norm ratio is h⁴/[4(m²−h²/2)²]<1; the ratio after just one cycle need not be <1. A separate exact symbolic replay in /workspace/branches/152ded78-b129-4846-8e0f-604fe88e8815/independent_csd_return_check.py confirmed both Jacobians and products. The frozen checker and its recorded output were inspected, not executed.

## originality

FAIL

Li–Wang's exact map and orbit already determine the return derivative for their example; affine normalization gives the same projective system throughout the arithmetic family. More decisively, the distinct indexed arithmetic-spectrum record gives that very normalized map and interior reversal orbit for the full family. The asserted signed scalar derivative is a direct evaluation of the published rational formulas followed by a two-by-two product. Neither antecedent spells out the multiplier or calls the orbit a repeller; the finding nevertheless has demonstrable implication coverage, not just title or parameter overlap.

## value

FAIL

Local repulsion of a radially contracting exceptional trajectory is a motivated dynamical question, and the explicit multiplier is a useful explanatory calculation. As a standalone narrow invariant, however, this is mechanically obtained by differentiating the already known exact rational map at the already tabulated reversal weights, with no new regime, obstruction or classification beyond that evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
