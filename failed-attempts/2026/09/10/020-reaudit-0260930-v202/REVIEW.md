# Review status

Independent mathematical audit date: 2026-09-30 UTC.

Disposition: **failed**.

Correctness: PASS. Independent symbolic differentiation on the six basis monomials of H_{2,0} plus H_{0,2} reproduced zero for the numerator of the Rossi Paneitz operator. The committed artifacts also verify the cancellation by several routes, including direct vector fields, Takeuchi-normalized formulas, a full degree-2 basis sweep, and an alternate normalization. The theorem and the refutation of the proposed negative degree-2 witness are mathematically correct under the stated fixed-contact-form convention.

Originality: FAIL. Takeuchi's published full text already gives the exact Rossi Kohn-Laplacian and torsion formulas in equations (5.15)–(5.22), the spherical-harmonic eigenvalues in (5.25), and the bidegree-shift rule in (5.26). Applying those published identities to degree 2 is a short direct specialization whose cancellation yields the claimed kernel. Under the audit bar that counts corollaries and mechanically implied special cases as covered even when not stated verbatim, the final theorem is covered by prior work.

Scientific value: PASS. The calculation is a useful clarification because it rules out a natural even-degree negativity witness and cleanly contrasts with the known odd-degree negative directions. It has diagnostic value for choosing trial functions, even though that does not overcome the originality failure.

Evidence: `INDEPENDENT_AUDIT_2026-09-30.md` and `INDEPENDENT_AUDIT_2026-09-30.json`.
