# Independent mathematical audit

## correctness

PASS

At scale three the twelve vertices are the even-sign signed permutations of (3,1,1), and the tetrahedron-edge subdivisions and four triangular truncation faces give 18 edges, every endpoint dot product 7 and squared norm 11. All generic section vertices are transverse crossings of edges; vertex-incident normals form a null union of great circles. Even-sign symmetry of the solid plus reversal of the central-plane normal reduces the area calculation to x>y>z>0, of area π/12. In (y/x,z/x), the four possible sign changes give exactly the six listed regions. Independent replay `python3 /workspace/review_checks.py 2` builds all rational ray intersections from vertex normals and cone boundaries, tests every vertex sign assignment for interior, and counts crossings at a rational interior ray using the nearest-pair graph. It finds exactly those six regions, two for each count, and sums chamber solid angles to 0.21593608531264044, 0.5202474652389364, 0.26381644944842314. For the two four-section triangles the absolute ray determinants are 2 and 1, and their dot-product and norm denominators are the exact D₁ and D₂ in the finding. The probability an edge with endpoint angle arccos(7/11) is separated by the central plane is that angle divided by π, so the mean is exactly m; on {4,5,6}, the total mass and mean then fix the other two atoms. The finite chamber enumeration checks the whole generic sign arrangement, not a sample of orientations. The frozen verification and checker were inspected, not executed.

## originality

FAIL

The distinct same-day published Haar polygon law has literally the same scaled solid, central sampling and counted statistic, supplies the entire law, and also resolves the finer full great-circle chamber structure. The exact arctan and arccos forms can be identified geometrically, not just by matching decimals. Let Ω₁ and Ω₂ be the frozen four-section triangle areas with ray determinants 2 and 1. Reflect the first triangle across y=z to make an unsplit spherical quadrilateral. The two opposite corners away from the mirror have angle θ₁=arccos(1/11); the mirror corners have angles θ₅ and π−θ₇ from their vertex-normal dot products. Spherical excess gives 2Ω₁=−π+2θ₁+θ₅−θ₇. The second triangle is one eighth of the axial octagon x≥max(3|y|+|z|,|y|+3|z|); its four corners with one of y,z zero have angle π−θ₉ and the four equal-absolute-coordinate corners have angle π−θ₇. Thus 8Ω₂=2π−4θ₇−4θ₉. The overlap source sums these shapes with multiplicities 24 and 6, giving exactly 48(Ω₁+Ω₂)/(4π)=q, and the identical mean fixes the other probabilities. No priority inference follows from the common catalogue day.

## value

FAIL

A Haar central-section complexity law for an Archimedean solid is a natural exact invariant. This submission, however, gives the same invariant already determined by the other exact law and chamber tables. Its compact two-triangle expression is an alternate evaluation of the known total area rather than an additional distributional or structural fact independent of that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
