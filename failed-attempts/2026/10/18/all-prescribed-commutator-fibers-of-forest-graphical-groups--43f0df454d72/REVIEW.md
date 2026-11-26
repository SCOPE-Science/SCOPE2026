# Independent mathematical audit

## correctness

PASS

The cocycle gives the alternating edge determinant with the stated commutator convention; basis brackets generate the full edge space. For each allowed nonzero vertex set U, contracting its zero-target edges gives a forest with c(U) components and r surviving edges: projective labels contribute (q+1)^c(U) q^r, and scalar propagation along the nonzero-target forest contributes (q-1)^(|U|-r). The input centers are unconstrained. The empty zero set proves attainment, including in characteristic two; empty and isolated components give the expected factors. Conditional subtree counts really depend only on whether the parent label is zero: the linear determinant equation at a prescribed nonzero parent gives q child labels, with one zero label precisely at target zero. Thus the two states suffice and the arithmetic bound is uniform in q, not a bit complexity claim. Direct enumeration independently agreed with the formula and recurrence on the empty forest, binary and F4 paths, and an F3 disconnected forest. The F2 path gives (76,36,24,24,36,12,24,24) before the central factor.

## originality

FAIL

A distinct earlier Resultary forest Lie-algebra record already states the main all-target formula, with the same all-characteristic scope. The group presentation adds no new fiber information: both maps depend on the same determinants of the vertex coordinates and both input central factors are q^(2m). Width and support invariance then follow from the earlier formula. The explicit two-state recurrence is not stated in the inspected earlier finding, but that does not make the original complete fiber theorem distinct.

## value

FAIL

The all-target invariant is mathematically meaningful, but the frozen contribution centers on an already exact forest result. The group translation and binary path specialization add no invariant; the displayed bottom-up calculation is a useful implementation note obtained directly by conditioning the same local determinant count in the earlier rooted forest argument. The submitted package does not establish a separately substantive new structural or algorithmic claim that warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
