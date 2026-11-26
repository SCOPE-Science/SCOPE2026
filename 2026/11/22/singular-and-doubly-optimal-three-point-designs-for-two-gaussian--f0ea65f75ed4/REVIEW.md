# Independent mathematical audit

## correctness

PASS

In the stated source-column and sampling-row order the rows are (a,b,1), (c,c,1), (b,a,1), so the signed determinant is -Delta_d. Proof step 1 displays the outer rows in reverse; this is an orientation-only typo and does not affect the stated absolute determinant or Fisher square. Since a-b>0, the rank defect is exactly the positive return of f=exp(-x^2/2)cosh(dx) to 1. For d<=1, log cosh(dx)<d^2 x^2/2; for d>1, d tanh(dx)/x decreases from d^2 to 0, giving a single crest and a single positive return. At the return the source columns are independent (their common positive middle entry would force a proportionality factor of 1, incompatible with the outer entries); (1,1,-2c) is a null vector. Dividing log f by x^2, the constant and next terms are (d^2-1)/2 and -d^4 x^2/12. The implicit-function argument in x^2 gives the stated onset and error. Each nonzero lobe attains its squared maximum in the interior, strictly locally by analyticity. The positive and negative lobe heights are continuous, for example by maximizing the positive and negative parts on a compact interval and using the uniform Gaussian tail on each compact d-range. As d approaches 1 the positive height tends to 0 while the negative height at x=2 stays bounded below. As d grows the positive value at x=d tends to 1 while the whole negative lobe is bounded by 2 exp(-d^2/2). Continuity gives equality of the two attained heights for at least one d, hence distinct global optima. This does not depend on the numerical illustration.

## originality

PASS

The supported distinct result is the rank-defect threshold, two-lobe geometry, and existence of a global tie for this exact symmetric saturated regression family. The available neighboring statements concern different objectives, noise, parameters or design domains. Primary full-text access was incomplete; no novelty inference is made from failed access or a search miss.

## value

PASS

For a saturated three-sample design, distinct known source locations do not prevent a positive-radius loss of one parameter direction. The sharp separation threshold and onset quantify that blind spot. Comparing the two optimum branches establishes a genuine global design ambiguity at some separation, not merely multiple local optima or a numerical observed tie. These are meaningful distinctions for choosing radii within the motivated family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
