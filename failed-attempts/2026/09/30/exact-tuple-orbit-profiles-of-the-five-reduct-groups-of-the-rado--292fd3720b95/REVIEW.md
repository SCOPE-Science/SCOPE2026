# Review status

Mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: PASS. Homogeneity of the Rado graph identifies injective ordered \(k\)-tuple orbits for the base automorphism group with labeled graphs on \(k\) vertices. Global complementation acts by translation by the all-ones edge vector. Vertex switching acts by the cut space, whose dimension is \(k-1\); adjoining complementation adds one independent translation for \(k\ge3\). Therefore the injective orbit counts are the stated powers of two, and the full ordered-tuple counts follow by partitioning coordinates by equality pattern, giving the Stirling transform. The package verifier exhaustively reproduces these translation-orbit counts through its finite range.

Originality: FAIL. Bodirsky--Pinsker's complete primary text restates Thomas's classification of the five closed supergroups exactly as the automorphism group, complement extension, switch extension, complement-plus-switch extension, and full symmetric group. Classical Seidel switching theory identifies switching classes with two-graphs, and the cut translations on a fixed labeled \(k\)-set form a \(k-1\)-dimensional binary space. Once those established ingredients are combined with Rado homogeneity, each claimed injective orbit count is an immediate quotient-cardinality calculation; the Stirling transform for repeated tuple coordinates is standard equality-pattern bookkeeping. Exact wording of the profile is not required under the implication standard.

Scientific value: FAIL. The profile is a convenient summary, but after the five reduct groups and switching-class structure are known, all five injective counts are one-line dimensions of elementary binary translation spaces and the noninjective counts are a routine Stirling transform. This is a textbook-level specialization rather than a motivated mathematical gap.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
