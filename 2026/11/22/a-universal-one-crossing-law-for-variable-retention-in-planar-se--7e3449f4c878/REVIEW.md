# Independent mathematical audit

## correctness

PASS

Independence of the nonconstant positive finite-mean retention time and planar Brownian motion gives R^2/(4 kappa) distributed as T times an independent unit exponential. At squared-radius scale s the signed tail difference is E exp(-s/T) minus exp(-s/m). With Y=1/m-1/T, the scaled difference F(s)=E exp(sY)-1 is strictly convex for s>0: exponential damping of the negative tail justifies differentiation on each compact positive interval, and the positive tail of Y is bounded. The right derivative at 0 is E Y, possibly -infinity (one-sided monotone convergence for the negative part of the difference quotient, dominated convergence for the positive part). Strict Jensen makes this derivative negative, and positive mass on a finite interval strictly above m forces F to diverge upward. Strict convexity then gives exactly one positive zero and positive slope there. The scaled derivative has the opposite sign from J(s)=E[T^-1 exp(sY)]-m^-1, itself strictly convex by positive-s differentiability. Its left limit is positive by Jensen (possibly +infinity, with monotone convergence on T<m); at the crossing J=-F'<0; it diverges upward by the same finite-interval argument with T^-1 bounded below there. The two zeros bracket the crossing and exhaust stationary points; the difference vanishes at 0 and at infinity, so they are strict global extrema. The curvature of exp(-s/t) has sign s-2t, proving strict Jensen brackets even at s=2a or 2b. For bounded centered nonconstant perturbations the uniform Taylor expansion through one s-derivative has leading factor e^-x x(x-2), x=s/m. Its simple zero at 2 and simple stationary points at 2+/-sqrt(2) persist by local sign bracketing and cannot be accompanied by other roots by the global theorem. The constant law is explicitly excluded. The frozen standard-library checker was inspected; its finite examples do not establish the infinite-law proof or test a truly infinite inverse moment.

## originality

PASS

Pass is for the exact radial cumulative-tail and two-extrema morphology at a fixed matched mean for arbitrary nonconstant positive finite-mean retention laws, with strict support brackets and the three weak-variation locations. This is not a claim that variable retention or random parameter mixtures were first seen to enhance long-distance dispersal. The closest no-contact-model ambiguity is between endpoint tails and first-passage probabilities; those kernels and time scales differ. Guttal et al.'s separate supplement is a specific unresolved risk, not negative evidence.

## value

PASS

Fixing mean retention also fixes mean squared displacement, yet the signed abundance beyond a radius changes sign exactly once and has a unique largest suppression and enhancement. That gives a useful sharp benchmark for arbitrary retention distributions, including multimodal laws and singular inverse-time moments, not just another parametric simulation of long-range dispersal. The curvature-based support bracket and weak-variation constants provide concrete scales. The result is a homogeneous independent planar diffusion benchmark, not an ecological prediction when motion and release are coupled.

The dated certificate retains the supplied scientific assessment, sources and limitations.
