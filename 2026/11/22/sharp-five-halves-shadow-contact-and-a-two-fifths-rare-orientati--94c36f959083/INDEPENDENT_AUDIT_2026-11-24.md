# Independent mathematical audit

## correctness

PASS

Orient u=(s,0,c) with c>=0. Projection area equals the integral of the positive normal flux; the flat base has outward normal -e3 and contributes zero. The spherical normal region clips the forward hemisphere at n3=h. For s<=|h| either the full cap patch is visible (h>0, integral pi*r^2*c), or the forward hemisphere is contained in the cap (h<0, integral pi). In the mixed case the positively oriented great-circle arc gives 2 arccos(h/s) to the u component of the vector-area line integral; the latitude arc runs from -beta to beta and contributes the integral of r^2*c-h*r*s*cos(phi). The factor 1/2 produces precisely the stated area. The moving-endpoint derivatives cancel because r^2*c-h*r*s*cos(beta)=c and sin(beta)=sqrt(s^2-h^2)/(rs). Hence dB/dalpha=-r^2*s*beta-h*r*c*sin(beta), strictly negative in the mixed region since for h<0 the bracket after division by r^2*s is beta-sin(beta)cos(beta)>0. The endpoint values and axial plateau follow, and |U3| is uniform, so inversion gives the CDF on its strictly monotone interval and the atom of size 1-r only for negative h. The equatorial derivative in c is pi*r^2/2; the exact terminal upper tails for positive h and the hemisphere follow from the affine branches. At contact, the absolute small-lobe correction on a latitude a distance v from tangent is the integral of the positive part of v/c-(sc/2)psi^2 plus terms O(v^2+v psi^2+psi^4). Both positive supports are O(sqrt(v)); the positive-part map is Lipschitz, so the slice error is O(v^(5/2)), and the leading slice integral is 4 sqrt(2)*v^(3/2)/(3 c^2 sqrt(s)). Integrating to delta gives the stated 5/2 coefficient and O(delta^(7/2)), with positive sign for the correction to the all-visible baseline and negative sign for the excluded part of the full disk. For regularity, scaling psi=sqrt(v)*y gives an analytic rescaled integrand in v and s near fixed nonzero contact, and its two leading roots are simple, hence analytic in those parameters. Integrating yields delta^(5/2) times a smooth factor, proving C^2 but not C^3, not merely a formal expansion. For h=-a, s-a=(r/a)(r-c)+O((r-c)^2), giving deterministic coefficient 8 sqrt(2)*sqrt(r)/(15 a^3) in c and its inverse power 2/5 in the continuous upper tail. The order estimate is only for fixed h, not at the hemispherical crossover. The frozen numerical verifier was inspected, not executed. A separate 50-digit flux quadrature on both sides of the clipping-height sign (python3 /workspace/review_checks.py 4) agrees with the mixed profile and confirms the contact coefficient and change of variable at the sampled heights.

## originality

PASS

Credit existing exact spherical-cap projection geometry as a substantive antecedent; the review does not validate a priority claim for the bare brightness formula, the silhouettes, or transition directions. The supported distinct result is the quantified fixed-height contact expansion, and its inversion as a sharp continuous probability correction next to the atom under isotropic viewing. The available related results do not supply that normalized asymptotic for this body. The closest projection paper is access-limited here, so formula-level priority uncertainty remains explicit.

## value

PASS

The fixed-height transition is a natural silhouette tangency for a standard convex body. Resolving its 5/2-order contact explains the failure of C^3 regularity and quantifies how unusually bright continuous orientations accumulate at an actual point mass with a 2/5 power. This is a useful local law beyond evaluating a single directional projected area; it does not purport to resolve the joint h-to-zero crossover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
