# Independent mathematical audit

## correctness

PASS

Summing the four PDEs and integrating with Neumann conditions gives total-biomass conservation. Differentiation at (1,1,1,1) gives the stated J. Independently eliminate the (N,Z,D) block, putting x=s+q: the determinant is x[(x+1/2)(x+1)(s+dq−1/4)+5x/8+7/16]. Thus det(sI−M)=(s+q)(s³+A s²+B s+C), with A=(d+2)q+5/4, B=(1+2d)q²+(1+3d/2)q+3/4, and C=[d(16q³+24q²+8q)−4q²+4q+5]/16. AB−C has coefficients 2(d+1)², 3d²/2+5d+7/2, 17d/8+5/2, 5/8 in descending q powers, all positive. Also b₀=qC, H₂=AB−C+A²q+Aq², and H₃=(AB−C)(q³+Aq²+Bq+C), giving the printed positive Hurwitz factors. Cubic Routh gives zero or one open-right-half-plane eigenvalue according to C>0 or C<0; in the latter case it is a positive real root. At C=0 the zero is simple and the remaining roots stable. AB≠C excludes a nonzero imaginary pair. At q=0 the only neutral direction is removed by the fixed-total constraint since the simple zero has left null vector (1,1,1,1); its cubic is strictly Hurwitz. The derivative numerator in RESULT.md changes sign once: by Descartes and its values −9043/32 at 9/4 and 163 at 4. Hence on the exact Neumann lattice the maximum is at n=4, comparing R(9/4)=25/1287 and R(4)=43/1440; R(25/4)=101/3915 is second. This covers the neutral equality and open single-unstable-mode interval. At the lower endpoint n=5 is neutral in addition to the unstable n=4, not an exception to the stated open interval. At q=4,d=1/100 the check gives b₀=−143/20. Inspected verify.py and VERIFICATION.md without executing the supplied checker; the argument is all-mode, linear, and not a nonlinear pattern claim.

## originality

PASS

On the inspected evidence, the supported distinct result is the exact all-mode necessary-and-sufficient onset, absence of an oscillatory instability, and isolated harmonic window for this one-phytoplankton-contrast specialization. The ecological kinetics, Neumann modal decomposition and determinant-based sufficient test are prior. The directly relevant thesis remains a named access risk.

## value

PASS

Whether a closed conservative ecosystem can destabilize when just one compartment differs in diffusion is a natural question raised by the original multi-scale sufficient condition. This gives a positive-equilibrium witness with an exact range, rules out missed oscillatory modes, and identifies the unique selected harmonic and the gap to the next onset on the actual domain. The fractions are useful because they resolve an all-mode classification of a minimal transport contrast, not as isolated numbers or as evidence of a nonlinear attractor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
