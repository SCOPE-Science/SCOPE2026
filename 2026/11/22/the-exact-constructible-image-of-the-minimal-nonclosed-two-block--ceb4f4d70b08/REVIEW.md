# Independent mathematical audit

## correctness

PASS

Two singular outputs are attained with C=0; otherwise exchange the outputs if necessary and normalize the invertible one to I. For T=X^(-1)Y, the determinant identity for a rank-one subtraction gives v^T u=1 and v^T Tu=tr(T)-det(T). If T is nonscalar, some u makes (u,Tu) a basis: invariance of the two basis lines and their sum line would force the same scalar on both basis vectors. Prescribe the two evaluations of the linear form on that basis. If T=lambda I, the first equation forces tr(C')=1 and the other determinant is lambda(lambda-1); for either allowed lambda=0,1 an elementary rank-one projector works. No field-size or characteristic assumption is needed. The exceptional set is the open subset of the rank-one 4-by-2 cone given by invertible X and Y neither zero nor X. Its scalar parameter is recovered regularly wherever X is invertible. The irreducible cone has 5-dimensional smooth pivot charts off the origin, full 8-dimensional tangent space at the vertex, and Segre degree binom(4,1)=4. Off the cone the image contains a dense open; rational density follows over infinite fields and geometric density follows on base change. Counting independent columns gives the stated finite-field count. An independent full-complement enumeration over F2, F3 and F4 gave (attained, missing)=(256,0),(6513,48),(65176,360). This is finite corroboration only. Replay: python3 /workspace/branches/9bd7fb60-5b6f-4f54-8ac3-c16fcf4803ea/independent_image_check.py. The supplied finite_field_check.py was inspected rather than executed.

## originality

PASS

The supported distinct claim is the exact all-field shared rank-one-summand image, not the known dense closure, the cited single obstruction over C, or the classical Segre geometry in isolation. The comparison is provisional with respect to unresolved primary-text access.

## value

PASS

The motivating example is a minimal formal model where closure equations give no membership test and a known obstructed pair gives no sufficiency criterion. The exact omitted locus answers realizability for every pair, also explaining the characteristic-two phenomenon that F2 has no rational omissions although the geometric map is not closed. These distinctions matter when using pattern varieties to infer actual compatibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
