# Independent mathematical audit

## correctness

PASS

The edge inequalities reconstruct the whole body: for z=|x| satisfying them, take t uniform in [0,1], select odd i when t<z_i and even i when t>1−z_i, and assign the prescribed signs. Adjacent intervals do not overlap and the signed expectation is x. Each signed edge inequality has a point with just its two signed halves nonzero and all other inequalities strict, so is a facet. Uniqueness and sign flips force both ellipsoids to be centered and diagonal. For the John squared axes b, inscribed feasibility is b_i+b_{i+1}≤1. Disjoint edges give the even optimum by AM–GM; for n=2m+1 the stated positive edge multipliers sum at each endpoint/vertex to 1/b_i with b_odd=(m+1)/n, b_even=m/n. Concavity of log certifies the unique maximum, and all facets are tangent at their signed b_i,b_{i+1} coordinates. For Löwner inverse squared axes c, the inequalities are the independent-set sums ≤1; AM–GM on the two parity classes forces equality only for the reciprocal class-size weights, which are feasible. The even path has m+1 size-m supports and the odd path has a unique size-(m+1) support; any other odd contact must consist only of the m even vertices to have weight one. Thus all contacts and the claimed homothety follow. The opposite facet pair bounds the inradius and opposite maximum-support vertices bound the circumradius, with both radii feasible at zero. The volume products give the displayed limits. Odd n=3 is valid and layered; nonlayered odd cases begin at n=5. Independent bounded enumeration for n=3,4,5,6,8,9 returned contact counts 6,12,12,32,80,48. The original Python checker was inspected, not executed; the all-n conclusion rests on the analytic certificates.

## originality

PASS

The supported distinct result is the explicit pair of path ellipsoids and parity contact census, including sharp attainment in nonlayered odd order and the odd enclosing-volume gap. The general ball radii, John roundness test and feasible odd John candidate have prior coverage; the homothety also has a standard structural explanation from antiblocker optimization and is not credited as a new generic phenomenon. The strongest available comparators do not give the missing explicit odd path optimizer and complete ellipsoid contacts.

## value

PASS

Fences are a natural nonlayered test family for the earlier height–width entropy equality problem. The exact contact supports distinguish the containing ellipsoid from the ball and show a parity change not conveyed by the homothety. The explicit e^(−1/2) enclosing-volume ratio despite axis ratio tending to one quantifies a high-dimensional geometric effect. These statements provide value independently of the known radii and generic product duality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
