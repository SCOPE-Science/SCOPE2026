# Scientific review: sharp four-secant coverage of the Hermitian quartic

## Correctness — PASS

The claim is finite and completely quantified: all \(532171\) rational projective points, all \(532171\) rational lines, and all \(892\) rational points of the smooth Hermitian quartic over \(\mathbb F_{729}\). The proof defines unique coordinate representatives and exact field arithmetic. Two separate C++17 calculations—one enumerating joining lines of all curve-point pairs and the other scanning every line directly—use different quotient polynomials and coordinate charts and reproduce the same 17-level external histogram. Both assert the stated line counts, the minimum \(25\), the maximum \(222\), the \(\mathbb F_9\)-subplane characterization, and the total incidence identity. Their completion messages were observed after full execution. The projective smoothness and the implication from strictly positive external four-secant counts to completeness are separately proved. Limit: no formal proof-assistant or independently conducted audit has been performed; the finite verification code is a necessary reproducibility artifact.

## Originality — PASS, with residual risk

The closest primary source [1] explicitly leaves \(r=3\) open in its Hermitian completeness theorem and supplies formulas for some **on-curve** incidences, not a \(q=3\) external-point four-secant spectrum. The follow-up [2] proves completeness when \(q\) is sufficiently large, and independently handles a restricted class of points (its \(A=0\) case) at smaller \(q\); its remaining asymptotic estimate does not cover the displayed complete small-\(q\) certificate. Their main statements neither imply the sharp 25 lower bound nor the 222 maximum-locus characterization at \(q=3\). Targeted searches for the 892-point Hermitian quartic, \(\operatorname{PG}(2,729)\), four-secants, and the exact values 39879/25/222 did not find a covering table. The first observed exact figures are supplied by the present verifiers. Residual risk: a classical unpublished, unindexed, or differently parameterized table of Singer/unitary orbit incidences could already imply the result. Absence in searched sources is not proof of absolute priority.

## Mathematical value — PASS

The \(r=3\) Hermitian completeness problem was explicitly singled out as unresolved in [1] and only settled asymptotically in \(q\) in [2]. A complete exact determination for the first odd base field \(q=3\) is a motivated missing small-field case, not an arbitrary numerical slice. The tight nonzero lower bound proves more than completeness, the full distribution quantifies incidence redundancy, and the maximum-locus description ties the exceptional multiplicity to the canonical \(\mathbb F_9\)-subplane. No extrapolation is claimed beyond the finite parameter.

## Closest literature, evidence, and risks

[1] Korchmáros–Nagy–Szőnyi, arXiv:2302.10162v1 (2023), introduction, Theorems 7.2 and 8.1, Section 8.1: later-extension completeness and some on-curve counts; \(r=3\) explicitly untreated for external completeness.

[2] Bartoli–Timpanella, *Journal of Algebraic Combinatorics* 62 (2025), article 21, main theorem and Section 3: asymptotic \(r=3\) completeness, no claimed \(q=3\) external histogram or sharp lower bound.

Unindexed historical computational data could affect priority. Human independent verification and expert review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
