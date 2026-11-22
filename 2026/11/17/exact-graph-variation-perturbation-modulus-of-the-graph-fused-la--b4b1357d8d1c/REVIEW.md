# Independent mathematical audit

## correctness

PASS

Inspected real graph-TV proximal KKT proof. Positive-weight connected graph makes J_w a seminorm modulo constants, and strict quadratic fidelity yields unique continuous polyhedral prox T_lambda. At each full-dimensional active face its derivative is the orthogonal averaging projection P_pi to connected fused blocks (Tibshirani-Taylor local affine projection). Graph layer-cake/coarea reduces its J_w seminorm exactly to indicators 1_S and weighted cuts. Crucially, every connected-block partition is truly locally attainable: start with distinct block levels u, cross-edge saturated dual signs and interior dual zero, then solve the mean-zero within-block residual h-P_pi h by a spanning-tree dual flow of size O(epsilon) strictly within capacities. This yields exact difference epsilon P_pi 1_S and attains all candidate ratios for any lambda>0. A full line segment crosses finitely many affine pieces, establishing global upper bound. For two q-cliques with one bridge, the single-bridge input cut has J=1; joining t vertices per clique in a single fused connected block gives J(P_pi 1_L)=t(q-t), maximizing to floor(q^2/4). Independent q=4,6,8 cases produced ratios 4,9,16, while global <= |E| <= n(n-1)/2 proves quadratic growth. Infinite graphs, zero weights, nonquadratic penalties excluded. RESULT.md blob 911220bf533a1f54d7e049eea862648f33c3a74d.

## originality

PASS

Foundational generalized-lasso local projection theory and graph ROF contraction of individual signals are correctly credited; the sharp two-input all-graph weighted-TV modulus, exact all-partition/cut attainment and quadratic barbell sensitivity were not previously established in inspected claims.

## value

PASS

Provides an exact, graph-structured sensitivity coefficient for a widely used nonlinear denoiser, identifies every active partition/cut witness rather than a loose Euclidean contraction, and proves quadratic two-input variation amplification on a natural bridge-barbell family. This resolves a genuine stability gap and yields useful worst-case counterexamples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
