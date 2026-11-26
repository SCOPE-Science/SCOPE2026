# Independent mathematical audit

## correctness

PASS

The 4k facets of the join arise from one edge in one factor; a vertex misses only two, both in its own factor. Its excess is k-1 in dimension 3k-1. Baumbach–Winter's bound on vanishing order at a face applies in the join's affine hull under the paper's interior nonvanishing convention. At degree k-1 the Taylor polynomial around every vertex would have only its common top homogeneous part; comparing vertices gives periods spanning the ambient space. A polynomial constant on the integer multiples of each period is constant along the corresponding line, so that homogeneous part would be constant, a contradiction. The lower bound also follows directly under the frozen record's potentially weaker convention on zeros of q: let T=sum_i t_i and homogenize q and the p_v relative to T=1 to degrees h and h+1 with h at least deg(q) and max_v deg(p_v)-1. The resulting polynomials satisfy sum_{v in i} P_v=t_i Q by layer precision. On a facet the extended coordinates of nonincident vertices vanish by nonnegativity and affine precision; hence their numerators vanish there, using continuity from the dense set q!=0. Each homogeneous P_v for layer i is thus divisible by both of its nonincident homogeneous facet forms (vanishing on a relatively open patch of each facet hyperplane suffices). Both forms use only that layer's three homogeneous variables. Therefore t_i Q has block degree at least two in each monomial, so Q has block degree at least one in that layer. For k>=2 the ideal of those three variables is prime and does not contain T; removing the extra powers of T used to homogenize q leaves its genuine degree-d homogenization in every block ideal. Its monomials meet all k disjoint blocks, forcing d>=k. For sharpness, the homogeneous factor construction gives alpha_{i,a}=t_i beta_{i,a}(z_i/t_i), with a polynomial common denominator of degree at most k; normalization and the two kinds of affine precision follow separately block by block. At t_i=0 its coordinates extend by 0<=alpha_{i,a}<=t_i; for surviving layers continuity follows from the factor coordinates on the closed quadrilateral. For instance after affine normalization to (0,0),(1,0),(a,b),(0,1), with a,b>0 and a+b>1, let ell=b(1-x)+(a-1)y and m=a(1-y)+(b-1)x. The four nonnegative weights ell*m, b*x*m, (a+b-1)*x*y, a*y*ell reproduce (x,y) after division by their affine sum ab+b(b-1)x+a(a-1)y, positive even on the closed boundary. This confirms the construction for arbitrary shapes. Products of parallelograms have polynomial tensor-product coordinates. Independent replay: python3 /workspace/independent_checks.py 4 verifies factor identities and closed-boundary positivity in 336 model evaluations, not the universal lower bound.

## originality

PASS

Credit Baumbach–Winter for the general local lower bound and the join upper-bound construction. The distinct assertion supported here is the exact minimum among arbitrary rational GBC systems on these joins: the simultaneous constraints across all vertices close the remaining one-degree gap. The parallelogram product comparison is a consequence, not a new product formula. The verdict is provisional with respect to historical priority.

## value

PASS

This settles a sharp natural invariant for all shapes in an unbounded-dimensional family and shows that even factors with polynomial coordinates can require a denominator of growing degree when joined. The all-vertex obstruction is useful beyond verifying a particular Wachspress formula: it separates optimality over all rational systems from the degree of one construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
