# Independent mathematical audit

## correctness

PASS

With q(t)=p sin²(ωt/2), the first waiting interval has success and failure Laplace weights A and B from q and 1−q against the exponential density. The failed transition resets to the same state, giving A/(1−B); the return starts with the weights interchanged and gives B+A·A/(1−B). For real s>−r, B(s) is strictly decreasing, B(0)<1 and B(−r+)=∞, since the failure probability is periodic with positive average even at p=1. The equation B(−ρ)=1 gives a simple pole with positive residue, since A(−ρ)>0 and −B'(−ρ)>0. Strict triangle inequality for the continuous failure kernel excludes nonreal poles on this line, and monotonicity excludes poles further right. The return multiplier A(−ρ) is positive and A,B are regular there; the rational transforms thus give positive, common leading survival exponents. Setting x=r/ω, y=ρ/ω and u=x−y gives 0=2y(u−p/(4y))²+(2−p)y−p²/(8y). This proves y≤p/√(8(2−p)) globally, with equality only when u=p/(4y), and the resulting x,y satisfy the pole equation with 0<y<x throughout 0<p≤1. This independently verifies the unique optimizer without using the discriminant argument; the printed discriminant was also checked symbolically. The means from the transforms are 2(r²+ω²)/(prω²) and 2/r, and x_*²−1=p²/[8(2−p)] gives the sharp comparison including resonance and the p→0 infimum. The result concerns the late-time rate only, not a finite cutoff; ideal Poisson probing, a coupled qubit and p>0 are essential to this check.

## originality

PASS

Credit Kulkarni–Majumdar for the pole-based objective, the resonant cubic, the resonance tail/mean distinction, and the shared transition/return optimizer in that example. Their exact cubic makes the resonance constant algebraically accessible; do not treat that special case as the distinct contribution. The supported refinement is the explicit globally unique optimizer and sharp comparison over the full detuning range, established through uniform dominant-pole and optimization arguments. The strongest compared results supply the prerequisite renewal formulation, not an optimization theorem whose specialization gives this all-p result. No claim of exhaustive historical priority is made.

## value

PASS

This closes a previously posed rate-selection problem across an experimentally interpretable coupling parameter. The exact optimum and bound tell how one should tune a probe chosen for suppression of long delays rather than the mean, including the return protocol whose mean has no interior optimum. The rate shift is modest; the mathematical value is a sharp uniform separation of objectives and an exact common late-tail design, not a claim that the protocol optimizes finite quantiles or works outside the ideal model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
