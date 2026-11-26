# Independent mathematical audit

## correctness

PASS

Direct substitution gives du/dt=omega xw and dw/dt=-omega xu, so E is conserved, the affine Jacobian magnitude for spatial area is omega/A, and theta is increasing on x>0 with derivative omega x. For r=sqrt(E)<=a, minimization of the sinusoidal y expression gives a lower bound C/A-(C-F)/(A(1+sqrt(D/A)))>0, including F=0. Thus for 0<r<a each full turn is physical, and the nonstationary part of r=a is one physical arc. The tangent-half-angle integral gives T=2pi/(omega sqrt(a²-E)). At each interior concentration z, each of the two phase branches contributes 1/(omega z sqrt(E-(z-a)²)) to the physical-time density before normalization by T. The alternative measure x dt=dtheta/omega gives 2pi/omega per turn; an extra factor of x integrates to 2pi a/omega, and the periodic sine term in the mean of y integrates to zero by a log derivative. From the vanishing mean and x>=0, the law of x converges weakly to delta_0. At the double root, the half-angle variable satisfies d(tan(theta/2))/dt=omega a, yielding the exact rational pulse, two-sided tails, and full angle change 2pi, proving the same finite exposure. On r>a the accessible arc has simple clock zeros and infinite time to its endpoints, with dx/(x dt)=-omega r sin(theta) giving the stated asymptotic log-decay rate. Bounded energy and the inward derivative on y=0 exclude forward escape or quadrant exit from positive x,y; the backward half-plane arc need not stay physical. The equilibrium case E=0 and x=0 are excluded from the periodic law as required. Replay: the affine, angular and half-angle formulas displayed in repaired RESULT.md; inspected frozen CHECK.py and VERIFICATION.md, no frozen code executed.

## originality

PASS

The repaired finding claims the exact concentration occupation law versus the matched finite concentration exposure on periodic trajectories and the complete positive critical trajectory of the specified chemical model. It explicitly treats the center reduction and the scalar Adler regimes as background. The retrieved oscillator and chemical-center papers do not give the full observable comparison in the physically admissible domain, and the distinct indexed kinetic sources concern different systems and observables.

## value

PASS

The time weighting matters for a concentration observable at this natural kinetic locus: normalized sampling would indicate extinction and a vanishing mean, even though an entire recurrent excursion has an exact finite concentration–time integral. The exact same integral on the admissible complete critical pulse gives a quantitative benchmark across loss of periodicity, not just a relabeling of scalar phase-locking. The density gives a way to compute threshold residence times or moments for this concentration without assuming uniform phase. Neither the exterior phase-flow corollary nor the period integral is promoted as a separate new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
