# Review status

Scientific audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: **FAIL**. The local derivative computations are correct: at p=x^3 the discriminant gradient vanishes, the Hessian has only the dd entry -54, and on the transverse slice f=-4c^3-27d^2 the Jacobian quotient is the Jacobian quotient with relations c squared and d of length 2. But that quotient is the critical locus of f, not the defined intersection W=Y x_{T*Y} N^*(D/Y). Calaque's conormal-intersection formula identifies the zero-section/conormal fiber product with the (-1)-shifted cotangent of D (for n=0), so its classical truncation contains D rather than being the isolated length-2 Jacobian scheme. Equivalently, classically the conormal intersection has equations Delta=0 and lambda dDelta=0 and contains the entire lambda=0 discriminant. Thus the claimed W≃Crit(Delta), finite length w=2, and ensuing excess identity are false for the stated W.

Originality: **PASS**. Resultary returned only this record for the exact binary-cubic triple-root computation. Calaque and PTVV provide the general shifted cotangent/conormal and Lagrangian-intersection framework, but no inspected source states the record's exact local numerical package. Originality of the intended local example is therefore plausible, though it cannot rescue the false identification.

Scientific value: **PASS**. A correctly formulated first singular binary-cubic discriminant example with nontrivial stabilizer is a natural test case for shifted conormal intersections and excess geometry. The object, orbit, and A2 cusp are mathematically canonical rather than arbitrary. The scientific rejection is correctness, not lack of motivation.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
