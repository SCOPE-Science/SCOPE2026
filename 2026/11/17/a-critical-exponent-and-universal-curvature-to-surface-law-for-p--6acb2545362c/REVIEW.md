# Independent mathematical audit

## correctness

PASS

The suffix-vertex matrix is triangular with determinant ∏s_i, so volume=∏s_i/n!. Barycentric facet normals u_1=a_1e_1, u_i=a_i e_i-a_(i-1)e_(i-1), u_(n+1)=-a_ne_n have lengths q_i and only neighboring pair inner products -a_i². Facet area/volume is nq_i, and ridge area/volume equals n(n-1) sqrt(q_i²q_j²-(u_i·u_j)²). The exterior angle is pi/2 for nonneighbors and pi/2+arcsin(r_i) for neighbors, and V_(n-2)=1/(2pi) ∑_ridges ridge_area*exterior_angle; this reconstructs the exact O(n) formula. For p<=1, ∑q_i~sqrt2∑i^-p diverges while ∑q_i² and adjacent corrections are o((∑q_i)²), giving n²(∑q_i)²/8 and 1/8 ratio. For p>1 absolute summability justifies dominated convergence of pair sums and adjacent corrections and positivity. Independent n=3 equal-leg calculation exactly matched known V_1=1+1/sqrt2+1/sqrt3; n=2 normalization is correct. The existing checker rationally verifies 660 ridge determinants but not asymptotic proof.

## originality

PASS

Known Gao–Vitale intrinsic volumes cover equal-leg orthoscheme p=0, a genuine special case explicitly credited. Weighted power lecture-hall Steiner ridge coefficient and p=1 critical regime differ from prior combinatorial Ehrhart and from vertex covariance spectrum. No inspected stronger source gives the weighted O(n) invariant or curvature/surface universal ratio.

## value

PASS

Weighted lecture-hall simplices are a natural Euclidean geometric family whose lattice/combinatorial simplicity hides metric anisotropy. The exact second intrinsic-volume ratio and p=1 transition classify a meaningful curvature observable; the universal 1/8 ratio to squared surface/volume over a broad phase is structural. The known p=0 endpoint is acknowledged and not counted as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
