# Independent mathematical audit

## correctness

PASS

Verified by an integral open-cover calculation. At a point with three nonzero homogeneous coordinates, invert those three; xyzw then kills the fourth coordinate in the ring, not just on points. With x=0,y=1 the two independent relations impose (z^3,w^3)=(1,-1); with y=0,x=1 they impose (z^3,w^3)=(-1,-1); with z=0,x=1 they impose (y^3,w^3)=(1,1); with w=0,x=1 they impose (y^3,z^3)=(-1,1). In each case the remaining cubic relation is the sum or difference of the two imposed relations. Changing signs as in the four displayed embeddings yields Z[u,v]/(u^3-1,v^3-1) in each chart. At each coordinate point set its nonzero coordinate to 1 and invert the three cubic coefficients of the equations whose prefactors are the three other coordinates; the coefficients evaluate to units ±1 at the section, and these equations kill all three coordinates on that open. These four opens are copies of Spec Z. No residue-field point has precisely two nonzero homogeneous coordinates: for either surviving coordinate used as a quartic prefactor, the other contributes just its cube with coefficient ±1. Therefore the eight pairwise disjoint opens cover the entire scheme, ruling out additional vertical or infinitesimal pieces. Each rank-nine chart is free on u^i v^j, 0<=i,j<3. Away from 3 the cubic is separable; at 3 it is (u-1)^3, giving one geometric point per factor with completed local ring k[[s,t]]/(s^3,t^3), graded monomial dimensions (1,2,3,2,1) and maximal-ideal nilpotency index 5. The sign-normalized points and eight support points agree with RESULT.md. The frozen check.py inspects rational point counts for eight primes and the local monomial basis; these are finite checks only, not the proof or evidence of geometric reduction in arbitrary fibers.

## originality

PASS

Pass for the specific arithmetic model and its scheme structure, not for the quartics, the forty complex points, or the signed cube-root parametrization. Proposition 5.17 of Chiantini et al. already treats exactly these signs over C as the d=3 case of a power family. Its proof computes the support via coordinate-plane strata and records the relevant cube relations for one plane; the new conclusion must be restricted to the integral gluing-free decomposition, flatness and nonreduced special fiber of the displayed integral ideal. The related same-day Penrose Lefschetz result concerns an Artinian quotient over Q, not this arithmetic conclusion. No ordering is inferred within the day.

## value

PASS

The exact integral algebra and non-curvilinear characteristic-three collision are useful for specializing this standard model of a named configuration: specializing its coordinate table shows merging support, but not the multiplicity, flatness or the two independent nilpotent directions, nor absence of vertical pieces. The decomposition distinguishes a length-nine thickening of embedding dimension two from nine transverse points or one curvilinear component, and exactly identifies when the point scheme can be treated as reduced. The value is specific to this model, not a claim about the entire reflection arrangement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
