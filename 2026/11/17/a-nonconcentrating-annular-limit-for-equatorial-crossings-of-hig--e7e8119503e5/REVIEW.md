# Scientific review: equatorial crossings of spherical chords

## Correctness — PASS

The exact segment-intersection expression is obtained by solving the last-coordinate linear interpolation equation. Conditional on opposite endpoint signs, the two positive endpoint heights are independent and have the absolute-coordinate law of surface-uniform sphere points, and their equatorial directions are independent and uniform. Gaussian normalization supplies independent half-normal limits for the two heights after multiplication by \(\sqrt d\); independent directional inner products have mean zero and variance exactly \(1/(d-1)\). The denominator of the resulting continuous map is almost surely positive. The half-normal ratio has the half-Cauchy law; a two-branch change of variables gives \(f_Q(q)=2/(\pi q\sqrt{2q-1})\) on \((1/2,1)\). The density normalizes and its first two moments are explicitly integrated. Boundedness of the intersected segment inside the unit ball justifies convergence of all fixed positive moments. The direction/radius independence follows from stabilizer rotational invariance, independently of the asymptotic argument.

The executable `check.py` was run successfully from the supplied package directory. Its numerical diagnostics reproduce the normalization, moment integrals, ratio transform and two finite-dimensional simulations. Finite simulations do not prove the limiting theorem.

## Originality — PASS, with residual historical uncertainty

The closest literature inspected is Sidiropoulos (arXiv:1411.5639), whose full mathematical development computes the independent-spherical-endpoint *chord length* law rather than the location of its intersection with an equatorial hyperplane. Bilyk and collaborators (arXiv:2307.04314) establish the unusual equality between independent spherical endpoints and the kinematic line measure in ambient dimension three, but not a high-dimensional conditional intersection-radius law. The related public paper *Uniform-disk law and Cauchy disintegration for hemispherical geodesic midpoints* concerns the shorter intrinsic midpoint of two points in one hemisphere; the present observable is the **Euclidean chord's intersection with the equator when the endpoints occupy opposite hemispheres**. Neither object or sampling law reduces to the other via its stated theorem.

Coleman's 1989 *Random sections of a sphere* is a residual historical priority risk: an abstract was accessible, not its full text. The absence of a result in retrieved publications and similarity searches does not establish mathematical uniqueness. No independent historical audit has occurred.

## Mathematical value — PASS

For a fixed equatorial hyperplane, two independently uniform high-dimensional sphere points are on opposite sides with probability \(1/2\), so their connecting chord's crossing location is a natural observable. Its limiting squared radius has a sharp positive inner-radius threshold \(1/2\) while retaining positive variance \(4/(3\pi)-4/\pi^2\). This contrasts sharply with concentration of the **same chords' lengths** at \(\sqrt2\) and prevents an erroneous kinematic-line interpretation of high-dimensional endpoint sampling. The formula gives a full probability law, not just a scalar cutoff, and moments follow exactly. These features make the specific nonconcentration statement useful for geometric sampling and high-dimensional stereological modeling, despite an elementary proof once the right endpoint-height variables are identified.

## Limits

No convergence rate, shared-space angular limit, or invariant random-line conclusion is established. The source-priority risk from older sections literature remains, and all numerical computations are finite.

Self-review: passed. Independent audit: not yet performed.
