# Independent mathematical audit

## correctness

PASS

For positive order m, factoring out sin(theta)^m leaves a polynomial in cos(theta) of degree at most L−1−m. With L−m nonpolar resolving rings the cardinal weights give precisely the omitted-ring operator’s maximum absolute row sum, and the pole contributes zero. Resolving sets are prefixes in descending ring order. I independently computed the subset minimax values via D(empty)=0 and D(S)=min_{s in S} max(F_L(S),D(S−s)), with weighted row sums via barycentric products and 192-bit Arb enclosures. The computations compare distinct relevant threshold tags by strict interval separation and handle identical tags by identity. They confirm the greedy choices and equality of the two objectives for L=2 through 11, including the zero at L=2. At L=12 the greedy cost is in the Arb ball centered at 4.4912808131248052018326013351... (radius < 8e−55) and the global cost at 3.7469440041222800437101185915... (radius < 6e−55). The displayed alternative has the global bottleneck, and the reduction exceeds 16 percent. Independently confirmed both bottleneck orders, resolving sets and worst omitted nodes (greedy: m=5, t=8; optimum: m=6, t=2). The frozen reachability proof is a different valid test of the same minimax inequality: deleting all subsets whose costs are at least the candidate threshold leaves no full chain. Its trigonometric, interval and cutoff logic was inspected, not executed.

## originality

PASS

The objective, grid and greedy procedure are explicit prior work, including a displayed L=12 greedy arrangement. The inspected strongest prior source explicitly leaves alternatives to the greedy step as future work; it does not give the global cutoff, certified improving placement, or global value. Other inspected optimizations change the objective or latitude domain. Pass applies to the finite global comparison, not the placement algorithm or interpolation formula.

## value

PASS

The prior placement procedure directly controls each next extrapolation norm but leaves the effect of future prefixes unresolved. A certified first failure and the globally achievable improvement of more than 16 percent distinguish a substantive tradeoff from a small numerical change, and give a benchmark for non-greedy placements. The cutoff is motivated by the first divergence, not an arbitrary finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
