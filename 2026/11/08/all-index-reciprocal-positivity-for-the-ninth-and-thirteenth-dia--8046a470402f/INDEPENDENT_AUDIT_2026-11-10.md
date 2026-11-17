# Independent mathematical audit

## correctness

PASS

The source positivity_certificate.py was inspected down to exact rational arithmetic: for m=9,13 the normalized q_m recurrence is rational, and all m roots are isolated in pairwise-disjoint radius 1/1000 disks by strict Rouché inequalities. Their real positive roots have strictly negative derivatives and smaller moduli than any other root; exact residue bounds show the real pole contribution dominates at n=44 and n=105, respectively, and monotone ratios keep it dominant for all n beyond those. Rational recurrence proves each of the finitely many earlier coefficients positive. An independently written exact rational Rouché/residue implementation reproduced cutoffs 44 and 105 with tail ratios 0.99937837096 and 0.99425975441, and checked coefficients. Thus the finite certificate plus analytic residue inequality covers all nonnegative n; floating-point diagnostics are not used as proof.

## originality

PASS

Fasi–Higham 2019 proposed reciprocal positivity; Scardino 2026 demonstrates conditional eventual positivity under dominant pole but does not prove all-index positive Taylor coefficients for diagonal orders m=9,13. The current exact rational all-root certificates validate hypothesis for both concrete degrees and verify every earlier index, so the conditional prior theorem alone does not imply full statement. Other Resultary degree 3,5,7 and off-diagonal claims concern distinct denominators; no direct m=9 or 13 source found. Scardino full primary inaccessible via lawful routes and institutional VPN disconnected; best-of-knowledge conditional and the risk of an unindexed general diagonal result remain.

## value

PASS

Diagonal Padé degrees nine and thirteen are actually used in scaling-and-squaring matrix exponentials; resolving every scalar reciprocal coefficient for both exactly closes meaningful finite cases of a named open sign conjecture and gives usable positivity premises for error-bound analyses. It does not purport to prove rounding or efficiency bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
