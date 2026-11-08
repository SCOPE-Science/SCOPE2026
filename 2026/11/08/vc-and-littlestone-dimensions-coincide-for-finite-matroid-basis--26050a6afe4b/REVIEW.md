# Mathematical review

**Correctness — PASS.** All matroids and boundary cases are covered. The characterization of shattered supports is a direct basis-extension argument. The classical matroid-intersection min--max theorem yields the parameter \(d(M)\); a direct substitution of ranks in deletion and contraction gives \(d(M)=1+\min\{d(M\setminus e),d(M/e)\}\) for every nonloop/noncoloop \(e\). The Littlestone recurrence has the same branches, proving the asserted equality by induction. The proof does not extrapolate a finite computation.

**Originality — PASS within examined evidence.** Mofidi's full Theorem 3.3 and accompanying proof already establish the static statement for graphic matroids, so that statement is not presented as new. Guingona et al. establish equal VC and Littlestone ranks for zero-set families, not unrestricted matroid bases. published-finding corpus comparisons did not identify the arbitrary-matroid basis 2-rank identity. This cannot exclude an equivalent formulation in other literature.

**Mathematical value — PASS.** The result determines a worst-case *adaptive* membership-query invariant of every finite matroid base concept class from an exact offline min--max formula and explains why adaptive trees have no dimension advantage. It covers arbitrary matroids, including nonrepresentable examples, and supplies an effective reduction to classical matroid intersection. The proof's pointwise minor recurrence gives additional structure, beyond an unmotivated finite count.

**Closest literature and limitations.** The 2022 spanning-tree hypergraph result gives a graphical VC special case, and the 2021 zero-set theorem is a different general coincidence phenomenon. Classical matroid-intersection theory supplies a central identity, not a new one. The finding does not address independent-set classes, arbitrary constant-weight families or proper subclasses of the bases. Priority remains uncertain, and independent verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
