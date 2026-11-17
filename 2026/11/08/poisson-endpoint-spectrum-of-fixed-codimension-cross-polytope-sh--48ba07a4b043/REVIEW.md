# Independent mathematical audit

## correctness

PASS

For a Haar (n-q)-plane E, normal-subspace frame Q=G(G^T G)^-1/2 yields leverage scores ell_i=||Q^T e_i||²=(1/n)g_i^T S_n^-1 g_i, with S_n=G^T G/n ->I for fixed q. Hence projected antipodal radius is sqrt(1-ell_i), and the nearest-sphere deficit scaled by n^{1+2/q} is asymptotically n^{2/q}||g_i||²/2. Since iid chi²_q have small-ball probability x^{q/2}/[2^{q/2}Γ(1+q/2)](1+O(x)), the original n marked-pair deficits form a PPP with cumulative intensity t^{q/2}/Γ(1+q/2). Wishart spectral concentration plus min-chi-square tail uniform integrability gives all positive moments of Y=min deficits: Γ(1+q/2)^{2p/q} Γ(1+2p/q), while Poisson counts give kth order survival law. In n=3,q=1, a unit sphere normal gives max radius sqrt(1-min|u_i|²); inclusion-exclusion on |u_i|<s gives the displayed exact arcsin/arctan CDF. Four independent quadrature checks reproduced the formula. Distinguish generating antipodal pairs from actual vertices of a projected polytope.

## originality

PASS

Best-of-knowledge PASS. Predecessor projected-face/volume results do not determine Euclidean circumsphere deficits of generating vertices when projected dimension is n-q. Random central sections use different geometry and are not interchangeable with projections. The independent minimum-chi-square extreme process is classical, but the explicitly normalized geometric full point process, all moments, and exact three-dimensional octahedron benchmark were not found as a stronger theorem in the inspected primary literature.

## value

PASS

Random shadows of a canonical regular polytope are a natural high-dimensional convex-geometry object. The sharp fixed-codimension endpoint scaling n^{-1-2/q}, complete Poisson multiplicity process, positive-moment law and exact low-dimensional boundary benchmark are meaningful geometric invariants that could be used in studying random projection extremal radii; this is not a small arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
