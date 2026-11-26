# Independent mathematical audit

## correctness

PASS

Independence turns negative log all-failure probability into sum L(z_i); this is exactly a volume-weighted sum of z_i^d L(z_i)/b^d. To check the nonstandard step, write h'(z)=z^(d-1)Q(z), Q=d L(z)-z/(exp(z)-1). The series for L is strictly less than the geometric series 1/(exp(z)-1), so Q(z)<0 for z>=d. On (0,d), Q' has the sign of z/(1-exp(-z))-(d+1), which is negative because the first expression before subtraction increases to d/(1-exp(-d))<d+1. At zero Q diverges positively. Hence there is one root and a strict global maximizer, even for noninteger d>0; h tends to zero at both endpoints. A positive-volume weighted average attains the bound exactly when all pieces have that one maximizing size. For equal pieces the real count maps monotonically to z, so the integer optimum lies at one or both clipped bracketing integers; this is not a claim about unequal pieces. Increasing d adds a strictly positive multiple of L to Q, moving the root strictly right. At d=1, z=log 2 solves the equation. My direct recalculation at d=b+1=2 with b=V=1 gives P_3=0.442398109933, P_4=0.441026845693 and bound 0.443195608693. The frozen script was inspected, not executed. Its bisection and enumeration are supplemental for the tested ranges, not proof at all d or all counts.

## originality

PASS

Provisional novelty is the strict global preferred-size law for the specified inverse-length probability at every d>0, with exact attainment and a discrete consequence. The generic per-resource inequality, independence factorization and unimodal integer rounding are not new.

## value

PASS

The material-limited reliability objective is distinct from surviving biomass and is meaningful when one surviving lineage suffices. The strict optimum and equality rule give a sharp performance ceiling for arbitrary cutting, and the exact two-count rule yields a practical equal-size benchmark for the stipulated model. This is model-level value only: genotype, site, dependence and actual size-response data limit any field interpretation; the record does not overpromise a field optimum or a solution for unequal pieces at generic budgets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
