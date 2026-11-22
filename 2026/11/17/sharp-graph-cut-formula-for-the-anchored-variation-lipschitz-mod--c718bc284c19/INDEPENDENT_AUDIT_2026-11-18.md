# Independent mathematical audit

## correctness

PASS

Every coordinate secant slope of g is in [a,b] by absolute continuity, so Sg(x)-Sg(y)=diag(s)(x-y). For fixed increment h, convexity in each slope reduces the bound to masks with slopes in {a,b}. On edges of equal slope the contribution is at most m|hu-hv|; on cut edges it is <=m|hu-hv|+(b-a)|h_v|. A rooted path from r to v gives |h_v|<=|h_r|+sum_edges|grad h|=||h||_{G,r}, hence the upper modulus is m+(b-a)|cut|<=m+(b-a)maxcut. For the lower bound choose a maximum cut with coordinate base levels at differentiability points where slopes approach a,b, orient the root toward a derivative near absolute m, then add the same infinitesimal constant epsilon at every vertex. The input anchored norm is epsilon; the quotient approaches |g’(t_root)|+(b-a)maxcut. At a=b, g is affine and formula reduces to |a|; ReLU and absolute value have finite exact witnesses on strict affine regions. Graph family formulas follow from exact maxcut counts. The NP-hard reduction from general MAX-CUT to connected graphs uses bridging components and color-flip freedom. Independent three-vertex path ReLU pair attained exactly ratio 3, consistent with 1+maxcut=3.

## originality

PASS

Best-of-knowledge PASS: established bounded-variation Nemytskii mapping/local regularity theorems and graph-Sobolev ReLU truncation estimates do not state the exact two-input anchored finite-graph l1-variation/maxcut modulus. MAX-CUT hardness is classical and not claimed as new; the precise composition-operator identity is the novel relationship.

## value

PASS

The exact nonlinear Lipschitz modulus and its graph maxcut characterization show that pointwise nonexpansive nonlinearities may have unbounded two-input variation gain. It resolves an exact natural stability question in graph signal processing, supplies sharp family coefficients, and converts complexity of the operator modulus into classical graph combinatorics; this is more than a textbook composition theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
