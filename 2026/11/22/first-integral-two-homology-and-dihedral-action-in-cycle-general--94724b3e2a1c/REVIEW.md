# Independent mathematical audit

## correctness

PASS

The original arithmetic was correct; the repair removes the already covered onset as a contribution and gives an explicit integral symmetry basis. I independently generated forbidden triples from the interiors of both arcs between every pair, using every tied shortest arc; no four-sets survive. With the star at zero as spanning tree, projecting a 1-cycle onto the coefficients of the non-tree edges is an integral isomorphism, so the signed triangle matrix in those coordinates presents H1. Smith normal form over Z has only unit nonzero entries, with ranks 1,0,5,2,14,8,27,20,44,36 for n=3 through 12. Together with the 2-face counts this gives the complete table with no torsion. At n=9 the exact kernel recovers the original two action matrices. For the repaired geometric basis, the three eight-term octahedral sums have zero boundary; in each a mixed-residue triangle is unique to that sum and has coefficient ±1. The tested coordinate minor is diag(-1,-1,-1), giving an integral basis using the rank-three computation. Rotation permutes the three oriented cycles and reflection transposes two without signs, as checked on the signed chains. The H1 reflection sign follows from chain traces (1,-4,-2) and trace 1 on H2; odd-order rotation cannot negate integral rank one. Independently computed the quotient by explicit dihedral orbits of flag cells in the barycentric subdivision: (8,16,10) cells with boundary ranks 7 and 9, giving unreduced rational Betti numbers (1,0,1). Face dimensions make stabilizers pointwise on flags, so these are ordinary quotient cellular chains. Replay: python3 /workspace/review-evidence/topology.py cycles, output cycles.log. Corrected RESULT.md and SLOGAN.txt are in repairs/5; supporting frozen checkers are unchanged.

## originality

PASS

This PASS applies only to the repaired finding. The original onset assertion is covered by a distinct exact same-model all-orders nonvanishing classification. It is now credited as already covered and not asserted as a contribution. That comparison explicitly supplies one primitive octahedral cycle per positive order rather than a basis, and does not give full Betti numbers, H1, torsion, or symmetry representations. The corrected exact integral table and equivariant basis/quotient are not supplied by or mechanical substitutions into the inspected results. No chronological ordering is inferred from the shared catalogue date.

## value

PASS

The repaired computation measures more than where a class first exists. It gives exact integral ranks including the large first homology in even cases and rules out torsion across the cutoff. The nine-cycle has a geometric, integral basis of cycles permuted by symmetry; it explains why the sum of the two-dimensional generators survives passage to the ordinary quotient but the one-dimensional class does not. The geometric permutation description and the quotient provide precise, reusable invariants of the natural small cycle with several independent two-classes. Neither value nor novelty is based on reasserting the already covered threshold or on a homotopy-type inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
