# Independent mathematical audit

## correctness

FAIL

The frozen proof asserts an incorrect exact backward equation (RESULT.md lines 56–60), rather than an incorrect threshold. Let u,r be respectively the half-sum and half-difference of the first moments, and m,h those of the second moments. With f=−1/(1+x), the generator equations give f u′+v r′=−1, f m′+v h′=−2u, and v m′+f h′−2γh=−2r. Thus 2γv h=(v²−f²)m′−2fu+2vr. Differentiate and substitute for r′ and h′: (v²−f²)m″+2f(γ−f′)m′=2(f′−2γ)u+4fu′+2, not +4. Independent symbolic elimination confirms this; the frozen checker only asserts the two Lyapunov identities and leading coefficient matching, so it does not detect the error. The incorrect constant does not affect leading-order conclusions. The protected interval is invariant, with uniformly positive absorption probability in fixed time blocks at the turning point. In the exterior, finite moments propagate between signs and launch points by positive-probability deterministic-direction runs and flips; on a compact interior interval, no-flip probabilities from its endpoints bound the moments uniformly, and conditioning at the next flip or downstream endpoint gives the classical backward equations since neither drift vanishes there. The Lyapunov calculations reproduce exactly: H_2=y²+(v/γ)σy has generator −2(1−D)−vσ/(γy), and H_4=y⁴+(2v/γ)σy³ has generator −4(1−3D)y²−6vσy/γ, y=1+x. For D<1/3 a positive combination, shifted to be nonnegative, controls the integral of twice the first moment up to hitting the turning point; the protected-region remainder is uniformly bounded. This gives the O(x⁴) bound needed to remove the homogeneous solution. In the corrected equation, the integrating factor is proportional to x^(−1/D), and the divided forcing still has leading term −2c x²/D, c=1/[2(1−D)]. For 1/3<D<1 integrating gives m′∼−2c x³/(3D−1); at D=1/3 it gives m′∼−6c x³ log x, contradicting a nonnegative m in both regimes. At D≥1 mean divergence suffices. For D<1/3 integration from infinity gives m′∼2c x³/(1−3D); the displayed exact relation for h gives h=O(x³), preserving the coefficient in each sign. Thus the theorem is supported after correcting the false identity, not refuted. The fixed-mesh killed-box experiments at lower level 1.5 (the turning point is 1 for v=0.5) can corroborate cutoff trends only; they do not verify the critical logarithm or identify infinite-domain moments. No replacement was submitted because the corrected scientific claim is independently covered by the catalogue comparisons below.

## originality

FAIL

The distinct indexed record e8413b5016ce gives the same protected region, second-moment threshold with strict inequality, finite-mean/infinite-variance regime, and quartic coefficient for the identical dynamics and equally likely signs. The stronger distinct record b5b06a8ce81b explicitly covers either initial sign and every integer order; n=1,2 recover exactly the exterior theorems and the sign-conditioned quartic coefficient, and so also all independent mixtures. These are statement-level mathematical coverage, not title matches or the frozen record itself. Their catalogue dates do not settle priority, derivation or attribution; the finding is not distinct in the evidence now available. The 2024 primary paper alone does not establish the full theorem.

## value

FAIL

The finite-mean/infinite-variance separation and exact asymptotic are natural and substantively useful in isolation. As a distinct deliverable, however, this record supplies no additional exact invariant, phenomenon or useful scope beyond the verified exact second-order and broader orientation-conditioned comparisons. Fixing the additive constant restores the derivation of the same result, not a surviving new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
