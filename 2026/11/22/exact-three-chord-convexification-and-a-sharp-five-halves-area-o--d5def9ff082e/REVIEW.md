# Independent mathematical audit

## correctness

PASS

The support-line intersection is e^(it)((1+i)R+eps e^(3it)); shifting by -pi/4 gives the stated z. Since r>4eps, the argument winds once with strictly positive derivative (the numerator is at least (r-eps)(r-4eps)), so the image is a regular positively oriented radial Jordan curve. Its curvature numerator has minimum (r-4eps)(r-16eps), giving convexity at and below r/16. Above, maximizing x as a quartic in c=cos(t) gives its only maxima at +/-s: the negative branch of c*(2c^2-1) never reaches q=r/(16eps)>1/sqrt(2), and its positive increasing branch crosses q exactly once between cos(pi/6) and 1. At these contacts x''<0 and y'>0. Curvature is strictly positive on the entire retained arc from s to 2pi/3-s by the cosine bound, and the two rotations give the same geometry. For the global patch, x(s)>0 and the vertical segment, traversed upward, is a strictly increasing polar graph over the same angular interval as the removed arc. The other two segments have rotated disjoint angular intervals. On those rays the removed arc has smaller radius by x(t)<x(s) for |t|<s. The patched curve is consequently a simple radial graph containing the original; it has a continuous nondecreasing tangent lift of one turn (the retained tangent lift is t+pi/2+arg(r-4eps e^(3it)), joining each chord with the same vertical direction up to rotation). Hence it bounds a convex domain. Conversely every arc and replacement chord belongs to the original hull, proving equality and excluding extra faces. Green's formula yields pi*(r^2+4eps^2) and the pockets give the stated integral since y is strictly increasing on a removed arc. Expanding 16eps cos(s)cos(2s)=r gives s^2=32delta/(5r)+O(delta^2); uniformly at t=s*u the x difference is (5r/8)s^4(1-u^2)^2+O(s^6) and y'=3r/4+O(s^2). Integrating gives (3r^2/2)s^5. Substitution t=s*u and the analytic implicit equation in s^2 show that the full defect above onset is delta^(5/2) times an analytic function with the stated nonzero limit; this justifies C^2 but not C^3, not merely a formal differentiation of an error bound. RESULT.md §§1–5 and the inspected checker give replay paths. Independent quadrature via the cubic for cos(s) gives the R=1 coefficient 130.70243996332004023, and at eps=.1249 an independent 72000-point hull agrees within 1.3e-8 in area. These checks do not prove the continuum claim; the global argument does. No assertion is made at eps=R/8 or for other viewing angles.

## originality

PASS

Pass for the all-amplitude three-chord convexification and exact hull defect, including its onset coefficient, not for the classical parametrization or same-family curvature transition. Neither the inspected same-family curvature/area results nor the close exact integral-epicycloid hull determines this amplitude-dependent hull law. Priority remains bounded by the material inspected.

## value

PASS

Once concavity appears, the exact hull is a natural global invariant: curvature alone cannot say which arcs are lost, how many faces replace them, or the amount of area recovered. The all-amplitude chord characterization answers these questions and fixes the first nonsmooth term in the hull area as the amplitude varies. The value is in the precise new convexification law, not a repeat of the curvature threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
