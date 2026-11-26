# Independent mathematical audit

## correctness

PASS

Conditioning on the hub gives the stated degree-(m+1) polynomial. The equality |1+2z|=|1+z| on the stated circle and the strict bound |z|≤2/3 give exactly m interior zeros by Rouché, with none on the boundary. On the negative real axis write z=−x. For 0<x<1/2 the positive ratio (1−2x)/(1−x) decreases from 1 to 0; its m-th power thus crosses x once. For 1/2<x<1 both terms have the same negative sign when m is odd, whereas for even m the log derivative of ((2x−1)/(1−x))^m/x is 2m/(2x−1)+m/(1−x)−1/x>0, and the ratio already exceeds 1 at 2/3. For x>1 the ratio equation becomes x=(2+1/(x−1))^m with a strictly decreasing right-hand side bounded below by 2^m. This proves uniqueness of the exterior zero and the real census, including m=1,2. Differentiation at any multiple zero gives mz=(1+2z)(1+z); for m≥3 its candidates have nonnegative real part, excluded by the root locations, and for m=1,2 all roots are already distinct by the count. Writing Q=2^m, the exterior equation first gives X_m−Q=O(m) by exponentiation and then gives X_m−Q=mQ/[2(X_m−1)]+O(m²/Q)=m/2+O(m²/Q). Under w=(1+2z)/(1+z), an interior zero satisfies |w|^m=|w−1|/|2−w|. On |w|≤1−ε the left side tends uniformly to zero and the right side is at least ε/3; the inverse Möbius map transfers the uniform boundary approach. This is not a claim of angular equidistribution. The accompanying graph/Sturm checks were inspected, not run, and do not certify the complex all-m assertions.

## originality

PASS

The exact partition polynomial, left-half-plane stability and the qualitative circle of accumulation have preexisting coverage. The supported distinct finding is the joint finite-size disk count with simplicity and exact parity census, and the single outlier with its escape expansion. The strongest inspected sources do not give those refinements by direct specialization.

## value

PASS

The once-subdivided star is a natural parameter family separating a shared hub from independent two-vertex arms. The fixed sharp region for the bulk, complete finite-size parity and simplicity, and the location of the one negative outlier give an exact complex-fugacity classification beyond stability and a limiting locus. No angular density or physical phase transition is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
