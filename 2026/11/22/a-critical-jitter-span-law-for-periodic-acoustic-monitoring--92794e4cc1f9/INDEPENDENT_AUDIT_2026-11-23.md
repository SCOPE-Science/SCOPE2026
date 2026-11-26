# Independent mathematical audit

## correctness

PASS

Conditional on the shared phase, the m miss indicators are independent even if their recording intervals physically overlap. The linear convolution of the intervals of lengths W and ell (when their sum is at most P) gives the overlap trapezoid, of minimum plateau length P-W-ell, maximum plateau length |W-ell| and two ramps of length min(W,ell). For sum exceeding P apply the same computation to the complementary arcs and add W+ell-P to their overlap. This proves the pushforward law including both coincident breakpoints and W=P (constant overlap). The survival power integrated against its two atoms and density 2/P gives the exact formula. For a=0 the low endpoint is one; for a>0 the low-end ramp term is smaller than the positive low plateau by order 1/m at fixed W, and all high-end terms have a strictly smaller base unless W=P, covered separately. Setting W=P-ell+c/m gives low mass |c|/(mP), low base to power m converging to exp(-c_+/(P-ell)), and the low ramp contributes 2(P-ell)/mP times the same exponential. The worst phase attains the minimum overlap; at equality this can occur on a null set, so no worst-phase contradiction. Strict Jensen for m>=2 and nonconstant overlap for W<P give the uniqueness claim. An independent Fraction computation split the phase integral at {0,ell,W,(W+ell) mod P,P} and integrated the affine lift-overlap powers exactly in 2,860 cases (integer 2<=P<=12, 1<=ell<P, 1<=W<=P and m=1,2,3,5,10); all matched. The supplied checker was inspected, not executed. The analytic argument, not the finite diagnostic, certifies the parameter continuum.

## originality

PASS

Best of checked evidence: the exact restricted-span finite miss law and matched floor/inverse-effort/geometric crossover for one shared phase are not covered by the identified empirical recording designs or the classical full-circle random coverage theorem. The interval convolution, conditional independence, and Jensen are standard and not original. The formula is elementary, but the comparison is of the complete model-specific phase-reliability law, not the convolution in isolation.

## value

PASS

A natural design parameter has a complete, practically interpretable regime classification in the idealized model: at criticality an almost-every-phase assurance coexists with zero worst-phase assurance, and O(1/m) changes in allowed span alter the leading miss coefficient. The law quantifies the effect that a duty fraction alone misses. The value is this sharp model benchmark and finite-effort control, not Jensen in isolation or a field-data claim. No fixed-energy optimality, phase drift, imperfect recognition, or nonuniform design theorem follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
