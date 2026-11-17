# Independent mathematical audit

## correctness

PASS

Reflecting k black coordinates maps Ferroni minimal-matroid bases isometrically to conv(0,{e_i+f_j}) in H:sum y=sum z=s; an explicit product decomposition with weights y_i z_j/s proves the full halfspace system y_i,z_j>=0 and s<=1. The intrinsic projected normal norms are h=sqrt((n-1)/n) for coordinates and b=sqrt(kr/n) for the base facet. Clearance constraints y_i,z_j>=h rho and s+b rho<=1 give rho<=1/(max(k,r)h+b), attained by feasible centers. At equality the max-size group coordinates are fixed to h rho while the other group surplus is an arbitrary nonnegative vector of sum |k-r| h rho; hence full center locus a regular simplex dimension min(k,r)-1 except rank=corank gives unique point. Tangency and fixed-n maximum floor((n-3)/2) follow. An independent scipy linear-program check for all 2<=k,r<=7 matched the analytic radius, but algebra proves the unrestricted statement.

## originality

PASS

Ferroni 2020/2022 derives the defining minimal-matroid base polytope but studies Ehrhart and lattice counts, not intrinsic inballs. An earlier Resultary formula for all connected rank-two matroids already covers k=2 and by duality corank r=2, which are acknowledged boundary cases. That theorem does not imply the genuinely higher rank-and-corank regular-simplex family. The earlier minimal-matroid minimum enclosing ball is an outer metric optimization. No precise higher-rank all-incenters theorem was found under equivalent pyramid-of-product-of-simplices terminology, but unindexed work remains a risk.

## value

PASS

Largest inscribed ball and complete incenter locus are motivated intrinsic Euclidean invariants of a canonical connected matroid base polytope. The nonuniqueness transition with an exact min(rank,corank)-1 regular simplex, tangency structure and sharp fixed-n dimension provide structural information beyond known Ehrhart and outer-sphere facts; no external large theorem is required for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
