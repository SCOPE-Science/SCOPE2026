# Independent mathematical audit

## correctness

PASS

For n>=3 and positive t=h/r, the vertex coordinates and two facet-normal orbits reconstruct every one of 4n interior dihedral angles. Exterior angles alpha=acos(q/sqrt(t^2+q^2)) strictly increase, beta=acos((ct^2-q^2)/(t^2+q^2)) strictly decrease, and their single crossing yields t_E=q*sqrt(1+2c)/c and Phi_min=acos(-c/(1+c)). Equating base and slant edges independently yields t_U=sqrt(2q(1+2c)), while maximizing h(R^2-h^2/4) yields t_V=sqrt(2). Exact algebra compares these at n=3 and n>=4; cosine Taylor expansions establish the n->infinity scales and pi/3 penalty. This is an analytic all-n proof; 261044 reported finite float assertions are corroboration only.

## originality

PASS

The exact equidihedral minimax and three-selector height separation across every polygon order is not implied by references for equilateral/uniform antiprisms or by unrestricted convex-polytope dihedral constructions. Exact full-parameter optimization is elementary after identifying the two normal orbits, but a nontrivial complete extremal classification remains distinguishable from known fixed-shape formulas. Best-of-knowledge, subject to historical equivalent-minimax formulations.

## value

PASS

Identifies the globally best dihedral balancing shape in a classical natural infinite family and gives exact separation between three intrinsically motivated shape selectors. The robust pi/3 limiting angular penalty for uniform and maximum-volume designs is a mathematically interpretable nonvanishing distinction, not merely a small numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
