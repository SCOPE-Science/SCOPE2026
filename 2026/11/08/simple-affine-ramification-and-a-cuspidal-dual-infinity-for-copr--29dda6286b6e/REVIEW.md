# Independent mathematical audit

## correctness

PASS

The frozen theorem survives, but its proof at RESULT.md line 28 gives the wrong leading coefficient for P T_b−Q T_a: only one derivative occurs in either term, so the coefficient is (a−b)2^{a+b−2}, not ab(a−b)2^{a+b−2}. For (a,b)=(2,3), direct expansion gives −8t^4+6t^2−3, not leading coefficient −48. The explicit corrected proof and coefficient regression are delivered under repairs/5. The base-point-free original map is birational since its generic degree divides both a and b; pullback degree b and Chebyshev composition identify its image with the asserted equation. P and Q have disjoint simple roots, so the corrected Gauss coordinates have no common zero; characteristic-zero biduality gives dual degree a+b−1. For W=P Q'−Q P', the differentiated ODE gives (1−t^2)W'=3tW−(b^2−a^2)PQ. W is nonzero at ±1 by this identity and at zeros of P,Q by their simplicity and disjointness. Thus every root of the degree-(a+b−3) Wronskian is simple, including complex roots. The vanishing sequence (0,b−a,b) gives the infinity weight. The dual normalization has only the infinite parameter over [1:0:0]; the orders a,b there are coprime and yield precisely the asserted Puiseux pair and delta. At every finite W root the graph second derivative W/P^3 has a simple zero, so the slope/intercept orders are 2,3, giving a cuspidal branch, not necessarily a distinct dual point. Inspected the frozen report and checker without executing them. Replayed the corrected exact checker with SymPy via python /workspace/repairs/5/verify_chebyshev_dual.py; all 73 bounded pairs passed, now including the coefficient that the frozen script never tested. The unbounded conclusion uses the proof, not the regression.

## originality

PASS

The distinguishable contribution in the corrected result is the uniform finite-Wronskian squarefreeness, hence the ordinary nature of every corresponding cuspidal branch. The exact dual degree, infinity weight and branch type are retained as direct geometric computations, not credited as independently novel from the known Chebyshev normalization and standard tangent-map theory. No inspected antecedent establishes the finite simplicity in this coprime complex family; the inaccessible broader source is a remaining access risk, not evidence of absence.

## value

PASS

The Wronskian's degree does not distinguish one higher-order inflection from several ordinary ones. Excluding every repeated finite root uniformly in a natural two-integer family supplies the complete normalized ramification profile and fixes the finite dual branch types. The explicit infinity calculation tells which singularity in the dual has the potentially large delta contribution and makes the finite classification interpretable. The value does not depend on counting distinct singular points or treating a routine class formula as a standalone discovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
