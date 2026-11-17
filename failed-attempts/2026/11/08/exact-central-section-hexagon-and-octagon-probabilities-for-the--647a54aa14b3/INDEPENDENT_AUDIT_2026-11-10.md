# Independent mathematical audit

## correctness

PASS

The standard rhombic dodecahedron has 14 vertices and 24 axial-to-cube edges. Each generic central plane cuts one vertex per edge whose endpoint normal evaluations have opposite signs. Signed coordinate symmetry reduces the count to six crossed edges when ordered normal magnitudes obey the triangle inequalities and eight otherwise. The normal sphere consists of eight equal central spherical triangles with sides pi/3 and angles arccos(1/3), plus 24 corner triangles. Girard excess gives P6=8(3 arccos(1/3)-pi)/(4pi)=6 arccos(1/3)/pi-2 and P8=1-P6. The actual standard-library verifier inspects all facet triples, symmetries and sample normals; independent numerical computation gave P6≈0.35095931218364385. Exceptional great-circle normals are measure zero. Finite symmetry check is backed by the analytic two-chamber case split.

## originality

FAIL

Two earlier published findings prove a strictly stronger all-diagonal-stretch central-section law for the exact same rhombic dodecahedron, including the assigned hexagon/octagon criterion and probabilities as the equal-scale case. The older source was read in complete RESULT.md; this is decisive mathematical prior coverage, not merely a shared title.

## value

FAIL

The fixed-solid two-point Haar section law is a naturally motivated geometric statistic, but here its complete exact distribution and normal criterion are already explicit special cases of an earlier stronger all-anisotropy theorem. This submission contributes no new useful invariant, structural refinement or independent mathematical gap beyond known-table recomputation. Originality and value fail even though correctness passes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
