# Independent mathematical audit

## correctness

PASS

The stated maxima and equality classification follow analytically. A rectangle c+[-u,u]+[-v,v] in central-symmetric K can be centered by averaging with its reflected copy without changing side lengths. With p=u+v and q=u-v, p,q have equal norm and perimeter 2(|p+q|+|p-q|). This expression is separately convex on K×K, hence bounded above by vertex pairs; equal vertex radii R make each distinct diameter-pair vertex rectangle feasible, so the bound is attained. Strict convexity in each argument away from collinearity excludes nonvertex centered maximizers; a collinear pair only yields 4R and is suboptimal. For any off-center maximizer with vertex p of norm R, |c+p|²+|c-p|²≤2R² forces c=0. The angular identity gives 4√2 R cos(ε/2); nearest-perpendicular pairs are found by the monotone two-pointer scan on sorted diameter angles. For regular even n the defect is 0 or π/n, and the stated counts follow by cyclic partner enumeration. Inspected verify_rectangle.py tests n=4..602 and 104 additional samples; these finite checks are not the universal proof.

## originality

FAIL

Definitive statement-level coverage: the published full RESULT.md "Vertex rigidity and the exact maximum perimeter of parallelograms in centrally symmetric cyclic polygons" treats the identical class, same perpendicularity-defect invariant, same value, all optimizer rectangles, and O(n) selection, and strengthens optimization to every inscribed parallelogram. Thus every asserted rectangle theorem and its regular n corollary is already implied; a different title and verifier do not establish original contribution. The two published records were deposited in the same October 11 Resultary commit, so no chronological precedence is inferred, only lack of a distinct uncovered finding.

## value

PASS

The vertex-rigidity principle, exact sharp perimeter and all-maximizer description are meaningful structural geometry, and linear selection for a natural restricted polygon class is mathematically motivated. They are not a vacuous normalizing check or arbitrary finite table; intrinsic mathematical value survives, but publication as a separate original finding is defeated by covering work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
