# Independent mathematical audit

## correctness

PASS

The stiffly accurate last stage of the two-stage Radau IIA tableau gives r(z)=(1-z/3)/(1+2z/3+z²/6) for the negative-real scalar equation. For the star, use conservation of the total, decay of the hub-minus-leaf-mean contrast by r((m+1)h), and decay of the leaf differences by r(h). This gives the four entry orbits independently of multiplying the displayed projectors. With N=m+1 and g(z)=(1-r(z))/z=(z+6)/(z²+4z+6), the off-diagonals are h g(Nh) and h[g(h)-g(Nh)]/m, both positive since g is positive and strictly decreasing. Subtracting m hub-to-leaf entries from one gives Q_m/D_b; adding r(h) to the distinct-leaf entry gives P_m/(D_a D_b) with the stated coefficients. For h≤3 the leaf diagonal is positive from r(h)≥0 and r(Nh)>-1. For h>3 the quartic is concave in m, so only m=2,10 require checking in the small range. The m=2 coefficients are positive; independently, P_10=h²(11h-82)(h-8)+252h+36, and the quadratic factor is negative only within (82/11,8), where it is bounded below by -9/11. This proves strict positivity there too. For m≥11 the discriminant of Q_m is positive, its roots are positive with sum <2, and P_m(8)=-4(160m²-1392m-2593)<0. Descartes' rule and the positive signs at 3 and infinity give exactly two simple positive leaf roots, in (3,8) and (8,infinity). The sign windows and boundary identities follow including T(0)=I. The small hub root follows from the root product and the large hub limit; testing P_m at fixed h>3 and at h=tm with t bracketing 2 proves the two leaf limits.

## originality

FAIL

A distinct indexed Resultary record states the same all-size, all-step classification for the same generator and same completed method, with identical threshold polynomials and stronger asymptotics. The frozen finding is substantively covered; this does not require assigning priority from catalogue dates or claiming anything about provenance.

## value

FAIL

The phenomenon itself is well motivated: entrywise positivity can fail and return as a stable implicit diffusion step increases, and the two negative diagonal types are informative. But the submitted classification adds no scientific content to the existing exact classification of that same phenomenon, which also gives stronger limits. Neither an illustrative example already in the comparison nor weaker restatement of its asymptotics is an independently useful new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
