# Independent mathematical audit

## correctness

PASS

Averaging squared distances from z=t1+w, w orthogonal 1, over each complete Hamming-weight-s orbit gives d t²+s(1-2t)+||w||². The farthest vertex distance is at least its layer average; a symmetric center t1 realizes equality on every vertex of a given layer. Maximizing in s depends only on a=min S, b=max S because q_s(t) is affine in s. The two-piece strongly convex envelope is uniquely minimized at t=h/d, w=0. Radius²=h(d-h)/d, and the strict affine layer difference identifies only b contacts below d/2, only a above d/2, and every vertex in the crossing case. Works for d=1, singleton S and degenerate polytopes; finite enumeration through d<=8 is not used as infinite proof.

## originality

FAIL

The complete published general Boolean-polytope minimum-sphere theorem states for ANY V⊂{0,1}^d that its unique minimum-enclosing-ball center is the Euclidean projection of u=(1/2)1 onto P=conv(V), with radius² d/4-||u-c||² and contact vertices exactly the maximizers of <1-2c,v>. Apply it to an S-hypersimplex: permutation-invariance makes that projection diagonal; the available diagonal coordinates are exactly [min S/d,max S/d], hence c=(h/d)1. Radius and all layer contacts then follow immediately. This directly covers every part of the submitted S-hypersimplex result, not merely its ordinary or uniform subclasses.

## value

FAIL

Although the S-hypersimplex is natural and its endpoint-only radius is exact, the complete value and contact classification are mechanically obtained by specializing an already-published universal Boolean minimum-sphere projection theorem and averaging the permutation symmetry. No mathematically new structural boundary or independent invariant is left after that reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
