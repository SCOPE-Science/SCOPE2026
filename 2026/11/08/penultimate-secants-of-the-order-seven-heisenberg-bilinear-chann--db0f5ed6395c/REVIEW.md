# Independent mathematical audit

## correctness

PASS

The two independent rescalings of any nonzero parameter triple give a two-dimensional fiber, so the affine r-channel dimension is at most 145r. Independently rebuilt the derivative over F_29 by scattering the derivatives of d_k a_u b_v times the phase to row (k+u,k+v), directly from the stated coefficient map. Used the frozen 2352 integers, verified the primitive order of 7 modulo 29, and performed exact integer blocked modular elimination, with no floats, on the four selected-column matrices. All four attained 2320 pivots of 2320 for (0,0),(0,1),(1,1),(1,2). Replay: python3 replay/review_q7_rank.py <frozen-package>/parameters_q7.txt 16 0 1 2 3. In the lift to Z[zeta_7], the reduced nonzero full minor cannot come from a zero determinant in the coefficient ring; selecting only the columns of r channels likewise gives 145r independent columns in the complex r-channel Jacobian. The dimension equals the upper bound in characteristic zero. Scaling the first coordinate of every index and transposing (i,j) give the corresponding type scaling and input swap. The remaining triality can also be checked on the coefficient map: with B(x,y)=x_x y_y and q(x)=B(x,x), swap k and u=i-k, replace v by -v, and set i'=i,j'=i-j. The exponent differs from the (-s-t,t) exponent by s q(k')+(s+t)q(u')-(s+t)q(i')+t B(i',j'), a sum of separate input and output phase gauges, yielding a linear equivalence of the image cones. Enumerating the scaling/permutation orbits of (s,t,-s-t) gives sizes 1,18,18,12 covering all 49 pairs. The polynomial map is conical and summing a dense parametrized subset of each cone gives the affine cone over the projective secant on closure. Thus the projective dimension is 145r-1 and the order-16 codimension is 81. Neither this computation nor the original proof tests order 17.

## originality

PASS

The motivating paper supplies the map, symmetries, one-channel dimension and second secants, not the q=7 nondefectivity through r=16. Inspected same-day work has a different invariant. A later result fills at 17 but gives only the 16-channel upper bound, not the exact subgeneric ranks. The pass is for the exact q=7 subgeneric dimensions beyond the known low orders, not for the parameterization, symmetry reductions, orders 1–2, or the generic width.

## value

PASS

q=7 is the first prime case beyond the motivating paper's complete small-q profiles, and r=16 is the largest predicted subambient order. The full exact rank there certifies every lower order for all twists, including their dimension rather than only a generic-width cutoff. It gives a clear answer about dimension 2319 and codimension 81 at the meaningful boundary, complementary to, and not superseded by, filling at 17.

The dated certificate retains the supplied scientific assessment, sources and limitations.
