# Scientific review: Zariski-chamber support profile of a one-nodal cubic surface resolution

## Correctness — PASS

The six-point assumptions, intersection form, and nef anticanonical class are explicit. Adjunction plus Cauchy--Schwarz bounds the degree of every possible nonexceptional negative curve by two, exhausting the twenty-one \((-1)\)-curves and the unique \((-2)\)-curve. For any independent subset of the \((-1)\)-intersection graph, the Schur complement for adding the \((-2)\)-curve is \(-2+r\), so the admissible subsets are exactly those with at most one root contact. Bauer--Funke--Neumann's negative-definite-support theorem converts this geometric statement to a chamber count. Two distinct finite enumeration algorithms give the same support polynomial. The separate smooth cubic check returns \(2764\). Exact reproducible files are `verify.py` and `verification_output.txt`.

## Originality — PASS (provisional historical priority)

The closest exact published method is Bauer--Funke--Neumann, arXiv:0912.0958, Proposition 1.1 and Section 3, which gives \(2764\) chambers for six points in **general** position. Bauer--Schmitz, arXiv:1204.4373, improves an algorithm but applies its main count to the Segre--Schur quartic. Lubbes, arXiv:1302.6678, classifies the rank-six \(A_1\) root configuration but not this support-count polynomial. Their general methods are fully acknowledged, and no new enumerative algorithm is claimed. Searches for the explicit \(1898\) total, the seven coefficients, and equivalent descriptions of the minimal resolution of a nodal cubic produced no matching statement. The result is the exact natural chamber invariant of the first nodal cubic degeneration. Search failure is not proof of novelty; older tables and unindexed computations remain risks.

## Mathematical value — PASS

The complete support polynomial counts geometric regions governing Zariski decompositions and stable-base-locus phenomena, not an arbitrarily chosen slice. The first nodal degeneration of smooth cubic surfaces is a natural boundary object in the degree-three del Pezzo family. The result quantifies its chamber-complexity drop from \(2764\) to \(1898\) while proving that support size six remains possible. It also separates contributions of supports containing or omitting the exceptional \((-2)\)-curve. A bespoke isolated algorithm or paper-sized extension is not necessary for this exact natural invariant to be useful.

## Limits and independent validation

The proof covers the specified complex minimal resolution, not other singularity types or the singular cubic's own Weil-divisor geometry. A general negative-definite-support theorem is used as prior work; the specialization and finite coefficient evaluation are the new content. Publication priority remains provisional. No independent specialist or external scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
