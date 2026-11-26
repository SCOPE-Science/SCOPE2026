# Independent mathematical audit

## correctness

PASS

For a fixed graph, shifting −L by cI makes it nonnegative, and each pair is reached by a positive shortest walk. This yields Q(t)>0 for t>0 and the first off-diagonal Taylor term (W^d)ᵢⱼ t^d/d!, since diagonal stays cannot reach distance d in d factors. On a nonedge the I and L terms in the integral representation of L^α vanish entrywise. For 1<α<2 the remaining integrand is positive, and after division by ε=α−1 its limit at α=1 is ∫Q(s)ᵢⱼ s⁻² ds: the prefactor 1/[εΓ(−1−ε)] tends to 1, the small-s integrand is dominated for ε bounded strictly below 1 using d≥2, and Q(s)ᵢⱼ≤1 controls the tail. Spectral differentiation gives b=(L log L)ᵢⱼ. Let r=ε^{1/(d−1)}. Joint analyticity after dividing the off-diagonal entry by t gives a t^{d−1}−bε+O(t^d+εt+ε²), with derivative error O(t^{d−1}+ε). Below cr for fixed c below the predicted positive rescaled zero, the error is o(ε) uniformly. Above Cr for C above that zero, ε≤t^{d−1}/C^{d−1} and the error is a uniformly small multiple of t^{d−1} after shrinking the local rectangle. Between cr and Cr the rescaled quotient converges in C¹ to a z^{d−1}−b with strictly positive derivative on [c,C], so there is exactly one simple zero. Compact-time continuity and uniform spectral-gap convergence to the positive constant projector rule out all later zeros. Adjacent entries have positive first Taylor coefficient for small ε, and the diagonal is positive by positive definiteness. A finite simultaneous ε bound and a finite maximum over pairs give the exact nonnegative time set; smaller distances have vanishing ratios at the diameter scale. For P4, cosine eigenvectors give endpoint projector weights 1/4 at 0 and 2, and −1/(4λ) at λ=2±√2, so b=(log 2)/4; the sole shortest path gives a=1/6 and the stated square-root constant. The frozen checker and its 97-pair recorded numerical results were inspected, not executed; the independent spectral coefficient check is not a numerical proof of uniqueness.

## originality

PASS

Unique recovery and linear onset are known on important diameter-two families, some for every α>1. General eventual-positivity theory supplies a late positive tail. The supported distinct result is the simultaneous unique-crossing law on all fixed finite positively weighted connected graphs sufficiently near α=1, with the positive heat-kernel coefficient, all distance-dependent time scales, and the diameter maximum. The strongest inspected matches do not imply this extension; the assessment is bounded, not a priority claim.

## value

PASS

The theorem gives a concrete quantitative boundary that eventual-positivity criteria alone do not resolve: each nonedge changes sign exactly once and its distance determines how long negativity persists. The coefficient uses both weighted shortest walks and the positive integral over all ordinary heat times. It yields an exact diameter law and explains a square-root onset already on P4, rather than merely extrapolating the known linear regime on diameter-two families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
