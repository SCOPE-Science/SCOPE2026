# Independent mathematical audit

## correctness

PASS

With exclusive colours each root is represented by its nonnegative count vector. A full monochromatic star separates different supports, and a monochromatic star at the smaller threshold separates thresholds on one support; both constants differ from every test. There are d(2^q−1)+2 semantic hypotheses. The q singleton colours are statically shattered at every cap. For the upper bound, use real nonnegative-weight affine thresholds. For q+1 affinely dependent examples, take a nonzero dependence with coefficient sum zero and prescribe negative labels on the negative coefficients and positive labels on the positive ones. The strict inequalities for the negatives violate the dependence. For affinely independent examples, represent a coordinate direction by a linear combination of the examples with coefficient sum zero. Reverse that labeling; the weighted sum of the affine scores is then strictly negative, contradicting nonnegative weight in that coordinate. This also proves the static bound for boundary scores equal to zero. A full online depth k uses at least 2^k distinct hypotheses, yielding the cap-one upper bound. At d=2 a depth q+1 requires precisely 2^q positives at the root, but the empty, singleton, twice-monochromatic and distinct-colour queries have respectively 1, 2^(q−1)+1, 2^q+1 and 2^q+1 positives. None equals 2^q for q≥2. At d=3 the queries 2e_q followed by e_q on the positive branch and 3e_q on the negative branch separate four full blocks of witnesses: q in the support at thresholds 1, 2 or 3, or threshold 1 without q (including the empty trace via the false constant). In each block the other membership bits are queried independently with (t−1)e_q+e_i in the threshold-t block, and with e_i in the no-q block. These are legal queries, realizing every path of depth q+1. The size bound excludes q+2. Independently enumerated distinct functions and exact decision-depth feasibility for q=2,3,4 and all three caps; static upper bounds also checked exhaustively at q=2,3. The all-q conclusion uses the proof, not these samples.

## originality

PASS

The distinct content supported by the comparison is the uniform exact online plateau and transition for the one-test count class, coupled with an unchanged static rank. The generic VC and class-size methods, including the nonnegative affine-threshold obstruction, and the ambient bounded fitting setting are not asserted to be new.

## value

PASS

A single graded restriction is a natural minimal class in which static and adaptive complexity can separate while holding the number of colours fixed. The first cap admitting that separation is a useful benchmark: two successors attain exactly the cardinality at which a deeper tree could exist, but no legal split is balanced; three enable a uniform adaptive tree for arbitrarily many colours. This identifies the structural cause of the gap rather than merely counting hypotheses or exhibiting isolated small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
