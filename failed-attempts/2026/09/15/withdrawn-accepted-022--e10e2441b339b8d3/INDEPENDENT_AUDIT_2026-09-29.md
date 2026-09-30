# Independent Audit — 2026/09/15/022

Audit date: 2026-09-29 (UTC)
Audited tree: `41bfab52a41c7c058f2369b097ccd12c298f5d18`

## Disposition

**FAILED** — The orbifold conclusion is wrong and the z^2±i paired-realization headline is already covered by stronger prior work.

## Correctness

**FAIL**. The explicit orbit identities, the repelling 2-cycle multiplier 4+4i, and the fixed-point multiplier-product distinction between z^2+i and z^2-i all check. However, the orbifold assertion is false. Infinity is a fixed critical point of z^2+i, so the Thurston ramification weight at infinity is infinite, not 2. The signature is (2,2,2,infinity), giving chi=2-3(1-1/2)-(1-0)=-1/2, hence a hyperbolic rather than Euclidean orbifold. Therefore item 4 and the claimed Euclidean explanation of non-uniqueness are incorrect. Hyperbolic rigidity is not contradicted because the two maps merely share an abstract portrait; they are not asserted or shown to be Thurston equivalent.

## Originality

**FAIL**. The central paired-realization phenomenon is already in the literature in a stronger Hurwitz-class form. Floyd–Kelsey–Koch–Lodge–Parry–Pilgrim–Saenz state that among twists of z^2+i there are precisely two rational combinatorial classes, represented by z^2+i and z^2-i, tracing this result to Bartholdi–Nekrashevych. Thus the submitted observation that these two non-conjugate rational maps realize the same coarse abstract portrait is not a new research result; it is a weaker consequence of established classification information.

## Scientific value

**FAIL**. After correcting the orbifold, the record no longer supplies its proposed mechanism for uniqueness failure, and the remaining paired z^2±i realization is already covered by stronger prior work. The exact multiplier calculations are useful checks but are elementary invariants of a classical postcritically finite quadratic pair and do not by themselves constitute a standalone research contribution.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://link.springer.com/article/10.1007/s40598-020-00156-6 — Bonk–Meyer, Section 2.5: the ramification weight is infinite exactly on a critical cycle; gives the orbifold Euler-characteristic definition.
- https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/17-71/index.html — Floyd et al., Theorem 1: twists of z^2+i have precisely two rational classes, z^2±i; attributes the result to Bartholdi–Nekrashevych.
- https://arxiv.org/abs/2608.13850 — Saenz–Samji bicritical-portrait classification supplying the record’s immediate target context.

Independent checks:
- Recomputed 0→i→-1+i→-i→-1+i and the 2-cycle multiplier (2p)(2q)=4+4i.
- Recomputed the product of finite fixed-point multipliers for z^2+c as 4c, hence 4i versus -4i for the two maps.
- Applied the standard ramification definition to the fixed critical point infinity: alpha(infinity)=infinity and chi=-1/2.

Limitations:
- No inaccessible source is represented as read.
- The rejection does not dispute that the two maps share the stated abstract weighted portrait or that they are not Möbius conjugate; it rejects the orbifold claim and the originality/value of the headline.
