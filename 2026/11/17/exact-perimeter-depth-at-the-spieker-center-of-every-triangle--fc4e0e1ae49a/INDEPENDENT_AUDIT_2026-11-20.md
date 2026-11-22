# Independent mathematical audit

## correctness

PASS

Read full RESULT.md and actual verify.py tree entry. The arclength centroid barycentric coordinates yield adjacent-edge intercepts X=c(a+c)/(2P), Y=b(a+b)/(2P). For each vertex the cut arc u+v is strictly convex under X/u+Y/v=1, with inner W-line minimizer (sqrt X+sqrt Y)^2 or the shorter-side endpoint. The feasibility inequality gives the stated Q switch. At fixed perimeter, monotone adjacent-side pair depth makes the vertex opposite the longest side optimal. The endpoint inequality is b+2c>a; the interior inequality follows by monotonicity in a, t=b/c<=2+sqrt(5) and exact factor -(t+1)^2(t^2-10t+1). Degenerate family (1,1,eps) tends to 1/3; equilateral gives 4/9. Independently evaluated 120 random valid triangles against numerical line-cut optimization with 1600 angular directions; finite tests corroborate the global proof, not replace it.

## originality

PASS

Best-of-knowledge explicit two-branch arclength-depth profile at the Spieker point and its sharp shape-independent 1/3 bound are not stated by the read area-centroid perimeter Winternitz theorem. Older 2022 perimeter-dividing envelope results provide a general geometric method and may implicitly enable derivation, but do not without further optimization establish this specific canonical-center minimax/constant. Classical centerpoint existence for some point does not identify the Spieker point. Priority may be implicit in archived envelope literature.

## value

PASS

The boundary arclength centroid is a natural constructible triangle center; computing its exact minimum halfspace mass for every shape identifies a nontrivial fixed-center sharp 1/3 guarantee. Unlike the generic centerpoint existence result, the theorem names the same canonical point for each triangle and exhibits the depth transition and flattening extremizer. The comparison with area-centroid 3/10 has clear geometric meaning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
