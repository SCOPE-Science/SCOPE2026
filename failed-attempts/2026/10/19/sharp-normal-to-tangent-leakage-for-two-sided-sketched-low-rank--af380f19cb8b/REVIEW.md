# Independent mathematical audit

## correctness

PASS

Both projectors agree on the tangent space. On the normal space write the complementary oblique maps on each side as graphs [-C;I], [-D;I] in orthonormal coordinates. Their tensor product has squared norm (1+γ_L²)(1+γ_R²); its orthogonal normal component is the identity, so Pythagoras subtracts one to give the squared defect. A product of top right singular vectors gives equality, including when one defect vanishes. For a combined trial/normal compression K with ||K−I||≤e, the normal-to-trial coefficient A⁻¹B has norm at most e/√(1−e²). Indeed for unit normal y with w=A⁻¹By≠0 and x=w/||w||, write a=xᵀAx, b=xᵀBy. Then b=a||w|| and (a−1)²+b²≤e², with maximal b²/a² at a=1−e². Applying this to the two residual-specific compressed spaces gives the stated sharp universal coefficient, not an exact coefficient for every realized input. The 2×2 Gram examples have spectrum 1±e, yield equality for all permitted distortions and can be embedded in 2×3 sketches. For e_L=3/5, e_R=4/5 the three nonzero leakage entries are −1, 3/4, 4/3, with squared norm 481/144. N=0 gives zero without additional embedding; zero distortions and the tolerance frontier follow by substitution. The supplied script was inspected, not run.

## originality

FAIL

Equation (1), the central exact norm, is a direct consequence of the previously given two-sided projector and general oblique-projector geometry on its product complement. The reviewed literature did not explicitly print this residual bound; the sharp residual-specific specialization uses the same norm identity after restriction and the elementary sharp subspace angle bound for a near-identity positive operator. The related indexed Gaussian and sensitivity records are not exact duplicates and are not the basis for the failure. This assessment concerns coverage by implication, not chronology or authorship.

## value

FAIL

Leakage control is a natural question, but this particular norm and sharp tolerance are obtained by multiplying two complementary projector norms, subtracting the unit normal component and applying the elementary sharp bound on the angle between a subspace and its near-identity image. Independent two-dimensional equality on each side already realizes the product. No distinct scientific remainder beyond those exact consequences is established; this is not a judgment against sketch-error bounds in general.

The dated certificate retains the supplied scientific assessment, sources and limitations.
