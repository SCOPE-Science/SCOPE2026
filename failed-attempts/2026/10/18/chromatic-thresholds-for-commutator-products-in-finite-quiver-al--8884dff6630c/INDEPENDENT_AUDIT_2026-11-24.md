# Independent mathematical audit

## correctness

PASS

Since the arrow radical squares to zero, units split as the additive radical and the diagonal torus. For [g,h]=ghg⁻¹h⁻¹ the radical part in split coordinates is (1−s)·x+(t−1)·z. Loops vanish; products of such outputs add their radical parts. Each supported edge must be separated by one of the 2r diagonal labels, and conversely one nonzero coefficient can independently realize each requested arrow coordinate. This gives the exact coloring cutoff, including isolated vertices and the empty support. Individual nonloop directions generate the derived group for q>2; taking full support realizes the width and summing over edge supports gives the distinct-output formula. For q=2 the torus is trivial and the unit group is abelian. Independent exact computations using the original quotient-algebra multiplication, fixed diagonal pairs, and radical basis vectors gave 58025 and 59049 for one and two commutators in the q=3, K5 example (python3 /workspace/review-evidence/check_frozen.py, commutators). The bounded check uses linearity at fixed diagonals; it is not the general proof.

## originality

FAIL

The unrestricted additive chromatic cutoff alone does not imply a unit-group cutoff. But the distinct indexed additive results b7fb936d5d53 and f660f871aa43 explicitly give the stronger fixed-diagonal coordinate fibers, which do imply this unit-group image by restriction and invertible rescaling. For units U,V with diagonals t,s, the exact ring identity [U,V]_group−1=(UV−VU)(VU)⁻¹ rescales every arrow coefficient i→j by (s_j t_j)⁻¹: UV−VU belongs to the radical, so only the diagonal of (VU)⁻¹ acts on it. At fixed allowable t,s this is a support-preserving bijection on the additive image. Thus the fixed-label image and independence in those records transfer with the palette replaced by (k×)²; multiplying r outputs adds their radical parts. This is mechanical statement coverage, not a claim of publication priority or that either indexed record states the multiplicative theorem verbatim.

## value

FAIL

The support-sensitive word image would be useful if it required a new classification. Here the stronger known fixed-label image/fiber computation gives it by invertible rescaling and restriction to nonzero diagonal labels. The length, width, image-size example, and q=2 boundary are then direct consequences, with no independent new invariant or obstruction in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
