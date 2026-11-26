# Independent mathematical audit

## correctness

PASS

The all-length Morse proof is sound. Toggling the first path vertex leaves exactly the forced edge {2,3}, with vertices 1 and 4 absent and a free path four vertices shorter; m=0,1,2,3 give respectively the empty critical face, none, none, and a critical edge. Toggling the triangle vertex a leaves exactly the three incomparable families with forced edge {0,b}, {0,1}, or {0,n-1}; for n>=4 their free lengths are n-3,n-4,n-4, and for n=3 they are all zero. Subsequent endpoint toggles are realized by the global pivot order a,0,1,...,n-1,b. To verify acyclicity, in a directed cycle of the modified Hasse diagram upward steps along matching edges cannot be consecutive, while cardinality forces equally many up and down steps; hence the cycle alternates and all faces there are matched along it. Choose the earliest pivot among the coordinates changed on that cycle. It must also be removed at a down step. Both endpoints of that down edge were still unmatched when the pivot was processed, so would have been paired together, contradicting that the edge points down. Removing the empty-face pair gives one critical zero-cell plus the stated same-dimensional positive cells; this yields the integral wedge, including C3 and C4, not just homology. Independent cross-check: the simplicial-vertex support formula and exact path homotopy theorem yield the same result, including the empty path convention described in the originality findings. The archive's finite checks are corroborative, not the all-length proof.

## originality

FAIL

The whole claimed four-case theorem is already a direct specialization of Deshpande–Shukla–Singh, arXiv:2001.06775, Theorem 13 and Remark 1, together with the published path types in Deshpande–Singh, arXiv:2001.05448v2, Theorem 4.2. The former is a general connected-graph theorem despite its position in a chordal-graphs section. The triangle's free vertex a is simplicial, with neighbours 0,b, so it meets the hypothesis. Its two-supports are exactly {0,b}, {0,1}, {0,n-1}. Deleting their closed neighbourhoods gives respectively P_{n-3}, P_{n-4}, P_{n-4} for n>=4, and three empty graphs for n=3. The theorem prescribes two suspensions of each summand. With d=4 in the path theorem, P_m gives S^{2j-1} at m=4j or 4j-1, and a point at other positive m. Thus n=4k+3 contributes three S^{2k+1}, n=4k contributes two S^{2k-1}, n=4k+1 contributes none, and n=4k+2 contributes one S^{2k+1}. The empty paths contribute S^1 (as in the suspension convention of Corollary 14, or by collapsing the endpoints of an interval in the star-gluing proof). This gives the exact n=3 and n=4 cases too. It is coverage by direct application even though the exact bouquet table is not printed in those papers. A separate finite replay and an alternative matching do not restore originality of the claimed homotopy classification.

## value

FAIL

The bouquet is natural and the resulting table is useful as a worked example, but all four cases are obtained by listing three supports in the existing decomposition and using the exact path table. No independently useful new homotopy claim or substantive matching invariant beyond that routine specialization is established. The proof and finite diagnostics do not create a surviving scientific claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
