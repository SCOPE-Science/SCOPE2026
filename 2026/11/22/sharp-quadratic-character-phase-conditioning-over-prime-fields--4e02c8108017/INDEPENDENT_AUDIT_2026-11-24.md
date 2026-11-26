# Independent mathematical audit

## correctness

PASS

On unnormalized complex column space, s=cr reduces all nonzero c to the c=1 matrix or its conjugate, preserving its entire singular spectrum and the real candidate right-singular line. The c=1 kernel expands as C+iSη(1+u)+(1−C)1_{u=−1}; the zero/constant sector and the nontrivial multiplicative-character sector are orthogonal invariant subspaces. On each character χ the map to χ inverse has multiplier iS times the shifted Jacobi sum plus (1−C)χ(−1). For η, reindexing by u/(1+u) makes the shifted sum the sum of η over the field excluding 1, hence −1. This gives modulus m=2sin(π/p). For the other nontrivial χ, χη is nontrivial, so the Gauss-product identity gives Jacobi modulus √p, hence S√p−(1−C)≤|Lχ|≤S√p+(1−C). The lower bound is strictly above m at p=5 and stays so by monotonicity of √p cos(π/p) and 1+sin(π/p). For the zero/constant block B, the normalized constant gives the √(p−1) entries and summation over the kernel gives its lower-right entry 1+(p−1)C−w. Thus det B=w(1−C−ipS); the trace of B*B is 2p−1+(1+(p−2)C)^2+S². Independent symbolic expansion reduces det(B*B−m²I) to (p−1)(p−3)(1−C)^2(1+2C)>0, and the shifted trace is positive. Both block modes therefore exceed m strictly, proving simplicity. For p≥7, |B_22|≥(p−1)C>3(p−1)/5>√p+1/2 bounds all nontrivial characters from above and lies below or at the block's largest singular value. For p=5 the second-column squared norm is (15+√5)/2 and exceeds (S√5+1−C)^2, as verified by the stated strict rational bounds. The top singular value is consequently the larger Gram root's square root. Finally T_p=p²+O(1), D_p=O(1), and m=2π/p+O(p⁻³), which give the claimed condition number including its bounded remainder. CHECK.py was inspected as a finite numerical diagnostic, not run or used in place of the all-prime argument.

## originality

PASS

Credit the classical character transform and Jacobi identities. The supported distinct claim is the two exact complex singular edges, the simple quadratic right-singular line, nonzero-shift equivalence, and resulting exact conditioning of this shifted-product three-phase mask at angle 2π/p. Closest retrieved comparators differ in phase function, normalization, matrix dimensions or spectral question. The exact-source literature lookup is bounded, including explicit access limits for the closest determinant paper.

## value

PASS

A shifted multiplicative mask with a canonical quadratic character and unimodular phases is a natural family for a sharp stability calculation. Exact singular edges determine worst-case Euclidean inverse amplification and identify a unique, explicitly described direction invisible to rank alone. The uniform quadratic growth quantifies increasing ill-conditioning despite constant entry magnitudes; the result need not imply a general claim about finite-field sampling to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
