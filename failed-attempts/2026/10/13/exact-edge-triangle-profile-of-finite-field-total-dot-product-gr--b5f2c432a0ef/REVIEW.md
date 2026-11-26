# Independent mathematical audit

## correctness

PASS

For any adjacent distinct nonzero x,y, the joint orthogonality equations cut out ⟨x,y⟩^⊥ of codimension r because the form is nondegenerate. Exclude zero and exactly those endpoints with self-dot zero. Dependent edges require isotropic scalar multiples and q>2. An AA edge is e_1,e_2. In characteristic two an IA edge is e_1+e_2,e_3; in odd characteristic even the first three coordinates admit an isotropic point: the sets of squares and -1 minus squares each have (q+1)/2 elements, so x^2+y^2=-1 has a solution. Its perpendicular hyperplane cannot be wholly isotropic, since polarization would force it inside its own one-dimensional orthogonal complement. This proves nonconstant multiplicity. For n>=4 all independent edges have at least q^(n-2)-3>=1 common neighbors; dependent edges also have positive counts. In dimension three a totally isotropic 2-space would lie inside its 1-dimensional orthogonal complement, impossible. The ternary isotropic locus has q^2-1 nonzero vectors: in characteristic two the sum of coordinates vanishes; in odd characteristic projectivization is a smooth rational conic with q+1 points (use lines through a rational point, including its single tangent). Counting IA edges from isotropic vertices gives (q^2-1)(q^2-q), and grouping isotropic scalar fibers gives (q+1)binom(q-1,2) dependent edges. The anisotropic degree sum q^2(q-1)(q^2-1) is 2E_AA+E_IA. The resulting three counts multiplied by q-1, q-2 and q^2-3 and divided by three yield the stated triangle product. At (2,3) only the six IA edges have zero multiplicity. `python /workspace/audit_checks_1_5.py 3` independently enumerated graphs using bitset neighborhood intersections for (2,3),(2,4),(3,3),(5,3),(9,3), including F_9 via u^2=-1, obtaining one triangle at (2,3), 56 at (3,3), and 82160 at (9,3). This is regression evidence; the arbitrary-parameter proof is by dimension, not finite extrapolation.

## originality

FAIL

Godsil's exact symmetric-design incidence-matrix square, in the same section as the polarity given by the standard coordinate dot product, already determines every two-point intersection of the looped projective relation. The unprojectivized looped relation is obtained by replacing each projective point by its q−1 nonzero vectors, with the same adjacency for every representative, and deleting endpoint loops gives the frozen formula. Thus the finding is a mechanically implied specialization, not an identified verbatim prior vector-level statement. Rank-three counts and the exceptional coverage boundary are immediate consequences with the standard absolute-point count.

## value

FAIL

The local question is well motivated and the formula is a useful translation of the projective design answer. Under the value standard the exact datum and sharp exception are nevertheless mechanically implied: multiplying the classical projective co-incidence counts by fiber size and removing isotropic endpoint loops yields the entire edge profile. The dimension-three corollaries then use standard absolute-point and degree counts, not a separate mathematical advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
