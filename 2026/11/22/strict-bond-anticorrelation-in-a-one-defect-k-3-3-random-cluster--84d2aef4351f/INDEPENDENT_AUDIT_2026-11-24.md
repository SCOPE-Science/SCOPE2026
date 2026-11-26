# Independent mathematical audit

## correctness

PASS

The graph has six vertices with isolated vertices counted in k(A). For each of the 36 distinct unordered pairs, stripping only the marked activities from the four occupation cells gives Cov=x_e x_f(F00 F11-F10 F01)/Z². The separately written integer replay (branches/2760e33c-5e6f-463f-a09b-d3e7f82e1958/k33_independent_replay.py) enumerated all 512 subsets, multiplied each quotient back by q²(1-q), and matched the frozen certificate coefficient by coefficient for every pair. The automorphisms fixing the defect produce eight actual pair orbits, with sizes 4,4,2,4,8,8,4,2. Their distinct quotients have 26,25,65,58,67,64,65,58 monomials, all with positive coefficients on the support. Thus each quotient is strictly positive for positive q,v,w, and the normalized covariance is strictly negative since additionally 1-q>0 and Z>0. This covers all independent choices of q,v,w in the stated domain, including w=v; it does not cover nine independent edge activities, general K_m,n, or negative association. The accompanying replay JSON and summary are in the same replay directory. Frozen verify.py was inspected, not executed.

## originality

PASS

Best of current knowledge for the whole one-defect positive-activity K3,3 family at 0<q<1, not for negative correlation on this host under every measure. The graph falls outside the rank/corank and series–parallel results, and the known complete-bipartite uniform forest and uniform connected-spanning ensembles are different laws. The comparable one-defect K5 record is a different fixed host, not a stronger graph theorem. No historical priority guarantee.

## value

PASS

K3,3 is a natural small non-series-parallel bipartite test case outside the rank/corank cutoff. A single weighted bond models the smallest nonhomogeneous perturbation while allowing arbitrarily strong disorder, not just perturbation of equal weights. All-pair, full-domain sign with integer certificates gives an exact benchmark for when negative dependence persists despite that disorder. The domain-wide conclusion does not follow from a small rational grid or an endpoint ensemble.

The dated certificate retains the supplied scientific assessment, sources and limitations.
