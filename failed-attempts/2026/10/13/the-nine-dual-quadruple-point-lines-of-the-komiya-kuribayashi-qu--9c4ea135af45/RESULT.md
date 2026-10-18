# The nine dual quadruple-point lines of the Komiya–Kuribayashi quartic form the projective \(B_3\) reflection arrangement
## Finding
Let
\\[
K:\\quad x^4+y^4+z^4+3(x^2y^2+x^2z^2+y^2z^2)=0
\\]
be the Komiya–Kuribayashi quartic over \\(\\mathbb C\\). Janasz–Pokora–Zieliński list the nine quadruple intersection points of its 28 bitangents as
\\[
(1:0:-1),(1:0:0),(1:0:1),(0:1:-1),(0:1:0),(0:1:1),(-1:1:0),(1:1:0),(0:0:1).
\\]
Under the standard projective duality \\((a:b:c)\\mapsto\\{aX+bY+cZ=0\\}\\), these points dualize to the nine lines
\\[
X=0,\\ Y=0,\\ Z=0,\\ X-Y=0,\\ X+Y=0,\\ X-Z=0,\\ X+Z=0,\\ Y-Z=0,\\ Y+Z=0.
\\]
Thus their union is
\\[
XYZ(X-Y)(X+Y)(X-Z)(X+Z)(Y-Z)(Y+Z)=0,
\\]
which is the projectivization of the Coxeter reflection arrangement of type \\(B_3\\).

The intersection multiplicities of this arrangement are
\\[
t_2=6,\\qquad t_3=4,\\qquad t_4=3.
\\]
The three quadruple points are the coordinate vertices. The four triple points are the projective classes of \\((1:\\pm1:\\pm1)\\), and the remaining six singular points are double.

The full projective stabilizer of the nine-line arrangement is
\\[
(C_2)^2\\rtimes S_3\\cong S_4.
\\]
Moreover, the known projective automorphism group \\(\\operatorname{{Aut}}(K)\\cong S_4\\) acts as this full stabilizer. Under the source's correspondence between bitangent quadruple points and involutions, the orbit of three coordinate lines corresponds to the three double transpositions of \\(S_4\\), while the orbit of six diagonal lines corresponds to the six transpositions.

## Assumptions and scope
The base field is \\(\\mathbb C\\), and projective duality is fixed by \\((a:b:c)\\leftrightarrow aX+bY+cZ=0\\). The claim concerns the nine points in Table 9 of the cited source and their dual line arrangement. The group statement is about ordinary projective transformations of \\(\\mathbb P^2\\), not a group scheme in positive characteristic.

## Proof
Dualizing the nine listed points gives, in their displayed order,
\\[
X-Z,\\ X,\\ X+Z,\\ Y-Z,\\ Y,\\ Y+Z,\\ -X+Y,\\ X+Y,\\ Z.
\\]
Up to nonzero scalar multiples, these are exactly the nine reflecting hyperplanes of the signed-permutation root system \\(B_3\\). This proves the arrangement identification.

For the stabilizer, intersection multiplicity is projectively invariant. Hence every projective stabilizer must permute the three points where four arrangement lines meet. Those are exactly the coordinate vertices \\([1:0:0],[0:1:0],[0:0:1]\\), so after composing with a coordinate permutation a stabilizer element is represented by a diagonal matrix \\(\\operatorname{{diag}}(a,b,c)\\). Preservation of the pairs \\(X\\pm Y\\), \\(X\\pm Z\\), and \\(Y\\pm Z\\) forces
\\[
b/a,\\ c/a,\\ c/b\\in\\{1,-1\\}.
\\]
Modulo a common scalar, there are exactly four diagonal sign classes. Together with the six coordinate permutations, this gives exactly \\(4\\cdot6=24\\) projective stabilizers. Signed permutation matrices visibly preserve the nine lines, so no elements are missing. Their projective group is \\(W(B_3)/\\{\\pm I\\}\\cong(C_2)^2\\rtimes S_3\\cong S_4\\).

The source states that \\(K\\) has 24 projective collineations, with automorphism group isomorphic to \\(S_4\\), and that the nine quadruple bitangent points correspond to the nine nontrivial involutions. Every automorphism of \\(K\\) preserves bitangency, hence preserves the nine-point set and its dual arrangement. The resulting action is faithful: a projectivity fixing all nine listed points fixes the three coordinate vertices and also points such as \\((1:0:1)\\) and \\((1:1:0)\\), forcing its diagonal ratios to be equal. Therefore the image has order 24 and equals the full projective stabilizer just computed.

Finally, the correspondence between a quadruple point and its bielliptic involution is equivariant under conjugation: applying an automorphism to the four concurrent bitangents sends the associated projective involution to its conjugate. The nine arrangement lines have stabilizer orbits of sizes \\(3\\) and \\(6\\): the coordinate lines and the six diagonal lines. The nontrivial involutions of \\(S_4\\) have exactly two conjugacy classes, of the same sizes: three double transpositions and six transpositions. Equivariance therefore matches the two orbit types as stated.

## Verification
The accompanying checker constructs the nine dual lines from the source coordinates, compares them with the \\(B_3\\) normals, enumerates all projective intersections, and independently verifies the signed-permutation action. It returns
`VERIFY_OK`, together with \\(t_2=6,t_3=4,t_4=3\\), stabilizer order \\(24\\), and the \\(3+6\\) line-orbit split. The proof of maximality of the stabilizer is the multiplicity-and-monomial argument above and does not depend on finite sampling.

## Relationship to prior work
Janasz–Pokora–Zieliński prove that the Komiya–Kuribayashi quartic has automorphism group \\(S_4\\), that its bitangent arrangement has nine quadruple points, and they give the nine point coordinates explicitly. Their Remark 3.9 records that the nine dual lines form a simplicial arrangement, but it does not identify the arrangement as the \\(B_3\\) Coxeter arrangement, compute its full projective stabilizer, or relate its \\(3+6\\) line orbits to the two involution conjugacy classes. A later study by Merta–Zieliński treats maximal tangency lines and sextactic geometry of the same quartic; it does not supply this bitangent-dual identification.

## Limitations
The result is an exact identification for this one distinguished quartic; it does not classify dual quadruple-point arrangements for all Ciani quartics. The originality comparison cannot exclude an older classical description written in substantially different terminology or coordinates. No claim is made that the \\(B_3\\) name is needed to prove simpliciality; rather, the new content is the exact Coxeter identification together with its stabilizer and involution-orbit interpretation.

## References
1. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514v1 (first public 2023-08-31); Fundamenta Mathematicae 268 (2025), 151–170, DOI 10.4064/fm240105-13-12.
2. Ł. Merta, M. Zieliński, *On quartics with the maximal number of maximal tangency lines*, arXiv:2410.13997v1; Periodica Mathematica Hungarica 91 (2025), 309–319, DOI 10.1007/s10998-025-00648-y.
