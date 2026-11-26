# Independent mathematical audit

## correctness

PASS

Under the stated C² coefficient, uniform positive diffusivity and absorbing–reflecting assumptions, renewal gives m_r=(1−φ_r)/(rφ_r(x⋆)), with φ_r the unreset hitting-time Laplace profile. The normalization is invertible: φ_r(x)=1−r m_r(x)/(1+r m_r(x⋆)). Integrating (pφ_r′)′=r(p/D)φ_r from x to L using reflection shows φ_r′<0 on x<L, hence m_r′>0. For y>x the ratio φ_r(y)/φ_r(x) is the Laplace transform of the strictly positive time to reach x from y, by path continuity and the strong Markov property. The positive integral expression for 1/H_r, where H_r=rφ_r/(−φ_r′), therefore strictly decreases with r. Subtracting the logarithmic slope equations gives W=m_1′m_2′(H_{r2}−H_{r1})/D>0 in the interior. Cramer's rule yields the stated signs and formulas; the endpoints are determined by continuity, not division at the reflector. The one-rate compactly supported perturbation of D and b is admissible in C² and keeps the same equation for m. For uniqueness of that nonlocal equation, a homogeneous difference a satisfies (r−L)a=r a(x⋆) with zero absorbing and reflecting derivative data, hence a(x)=a(x⋆)(1−φ_r(x)); evaluation at x⋆ forces a=0. Frozen CHECK.py was inspected but not executed; it uses the forward ODE to construct exact-form derivatives, not derivatives of noisy measurements. The proof, replayable from RESULT.md lines 29–95 with the uniqueness calculation above, does not depend on a numerical grid or any external certificate. W vanishes at the reflecting endpoint and no stability to discretization or noise is asserted.

## originality

PASS

Credit is limited to two known-rate resetting mean profiles (equivalently, two full spatial one-target Laplace profiles at those rates) with the specified mixed boundary conditions, pointwise strict determinant, and one-rate insufficiency. Prior two-rate identification from two absorbing-exit splitting profiles is a close but distinct observation scheme; the other source comparisons change the moment, boundary orientation, measurement geometry or unknown. No distinct source inspected establishes the assigned same-data result.

## value

PASS

Rate variation gives a sharp experimental identifiability result with one fixed geometry and reset point: any two distinct positive controls suffice in the exact spatial regime, while one admits a local family of indistinguishable diffusions. The strictly positive determinant is substantive because a formal two-equation inverse would otherwise require a separate nondegeneracy test at every location. The result does not imply a stable numerical inverse from noisy samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
