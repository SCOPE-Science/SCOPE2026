# Independent mathematical audit

## correctness

PASS

Writing \(x=\cos(2\pi r/N)\) turns the sampled polynomial into \(1+ax+b(2x^2-1)\). The two adjacent cosine samples straddling \(-1/\sqrt2\) have opposite signs for \(2x^2-1\). A positive linear combination of their feasibility inequalities cancels \(b\) and gives \(a\le-2(u+v)/(1+2uv)\); choosing \(b=(1+2uv)^{-1}\) factors the candidate as \(2(x-u)(x-v)/(1+2uv)\), which is nonnegative on the sample grid because no sample lies between adjacent \(u,v\). The \(8\mid N\) contact and the \(\sqrt2\) limit follow exactly. Fresh direct feasibility checks on representative moduli \(5,6,7,8,9,16,31\) reproduced the formula. The universal claim rests on the analytic adjacent-sample argument, not the finite verifier.

## originality

FAIL

A current published finding, 'Exact degree-two discretized Carathéodory–Fejér extremals on every cyclic grid', states the same optimization for every modulus, gives exactly the same closed value for all nonaliased orders, and additionally gives the extremizer, factorization and aliased cases. It therefore strictly contains the assigned \(N\ge5\) constant theorem. The foundational primary paper confirms that this is exactly the discretized Carathéodory–Fejér quantity \(M_m(H)\), so the comparison is between identical object/normalization rather than merely similar titles.

## value

FAIL

The exact all-grid constant is a natural invariant, but it is already fully subsumed by the current stronger all-moduli extremal theorem. As an independent record it is therefore redundant rather than a separate mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
