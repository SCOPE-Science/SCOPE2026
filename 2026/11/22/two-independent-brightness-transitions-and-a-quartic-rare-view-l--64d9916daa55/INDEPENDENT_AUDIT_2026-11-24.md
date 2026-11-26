# Independent mathematical audit

## correctness

PASS

The corrected RESULT.md in /workspace/repairs/1/ is complete; its mathematics is verified as follows. The absolute-normal integrals of the two lateral halves agree by central reflection, and the bicone has no equatorial surface face. For radius one, parameterizing the upper surface by radius rho and azimuth gives normal times area element rho*(k cos(phi),k sin(phi),1) d rho d phi. Hence Cauchy's projection formula gives half the integral of |z+c cos(phi)|, with c=k sqrt(1-z^2). For c<=z the sign does not change; otherwise integration between the zeros gives 2[S+z arcsin(z/c)] with S=sqrt(c^2-z^2), equivalent to (1), including the limiting endpoints. Differentiating, F'_k=2t(H(t)-k^2)/(1+t^2) with t=z/S increasing; the derivative numerator of H is t+(t^2-1)arctan(t), positive also when t<1 by arctan(t)<t. H increases from 1 to infinity, so the only possible interior extremum is a strict nondegenerate minimum for k>1; the maxima follow from comparing endpoints 2k and pi. Uniformity of |U3| converts exactly these monotonic sublevel intervals into (3), with no atoms. The near-equator quadratic coefficient is (1-k^2)/k, and at k=1 expansion of the derivative gives F=2+z^4/3+2z^6/5+O(z^8); inversion gives the quartic tail and conditional uniform law. Expanding H=1+2t^2/3+O(t^4) gives z_*^2 asymptotic to 3(k-1), and local analyticity in k and z gives the minimum deficit asymptotic to 3(k-1)^2. At the axial maximum the tail is exactly linear; the equatorial maximum contributes a square-root probability with O(epsilon^(3/2)) error, so their separate contributions at the tie give (5). At tangency the excess is 2[S-z arctan(S/z)] asymptotic to 2S^3/(3z0^2); S^2 is asymptotic to 2(1+k^2)z0(z0-z). This gives (6) with matching first derivatives but unbounded left second derivative. All asymptotics are at fixed aspect except the stated separate bifurcation limit. The frozen numerical checker was inspected, not executed; these symbolic arguments do not depend on finite tests.

## originality

PASS

Applies to the repaired claim, not the frozen broad novelty attribution. The earlier single-cone profile yields the frozen bicone profile exactly by F_bicone=2F_single-pi*z. The repaired RESULT.md credits that implication, retains the contact expansion and inverse construction as supporting consequences, and limits the contribution to the global bicone minimum and maximum transitions and the specific rare-view laws. The available closest sources do not supply those extremal classifications and critical laws for this body. The inaccessible Vickers–Brown comparison is explicitly unresolved rather than treated as evidence of absence.

## value

PASS

The two parameter transitions give a complete global directional classification for a natural convex body. At the minimum threshold the quadratic term disappears and the probability exponent is one quarter. At the maximum threshold two equal brightest latitudes make unequal contributions to near-brightest views. The distinction between equal deterministic extrema and unequal random tails is a substantive, sharp conclusion even after removing standalone novelty claims for the profile and its routine consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
