# Scientific review

## Correctness

**PASS.** The claimed family is an explicit set identity for every integer \(k\ge2\), not a prediction from a finite scan. Six residue-slice interval classes convert the restricted triple-sum operation into exact affine interval arithmetic. All five tables are recomputed symbolically by `verify_symbolic.py`, which proves the necessary order/adjacency relations over the entire half-line of integers \(k\ge2\); the finite base partition and modular separation are then sufficient for an infinite covering induction. The unique long interblock gap proves the minimal eventual period. The independent direct greedy implementation agrees through \(12h\) for 399 parameters, and longer for eight parameters. These last computations are corroboration, not the infinite proof.

## Originality

**PASS, with priority qualification.** The nearest primary source is van Berkel--Bosma, *On \(t\)-sumfree sequences* (arXiv:2609.16843v1, 15 September 2026): its general three-sumfree theorem requires \(g\ge\max(f+1,d-1)\) for \(S_{f,g,g+d}\), whereas for this family \((f,g,d)=(1,2,6k+3)\) the inequality fails for all \(k\ge2\). Its computations cover numerous individual small triples but do not imply the infinite formula. Shtrezi (arXiv:2606.17447v1, 13 June 2026) covers seeds \((1,g,g+1)\), which meet \((1,2,6k+5)\) only outside the claimed range. published-finding corpus searches found closely related **two**-sumfree families, which do not imply the claimed **three**-sumfree theorem. The source's relevant abstract and introduction were read; later sections were not fully accessible, leaving a documented historical-priority risk, not proof of uniqueness.

## Mathematical value

**PASS.** The source studies the general open problem of eventual periodicity for greedy three-sumfree sequences, proving a broad region but leaving an infinite complement in parameter space. This result settles an entire arithmetic progression of seed triples inside that complement, determines every term instead of only existence of periodicity, and gives a sharp least period plus exact density. The affine interval mechanism is reusable for checking other structured seed subfamilies. It is not merely another finite table row, and it makes no claim about the full open conjecture.

## Limitations and residual risks

The theorem is restricted to \(h\equiv5\pmod6\) with \(h\ge17\). It does not prove the conjecture for all triples. Its main symbolic checker depends on the elementary and explicitly stated exact formulas for distinct sums of integer intervals, and should be independently inspected if used as a publication proof. A fully unindexed earlier derivation or a conclusion buried in incompletely accessible later sections of the motivating source cannot be excluded. There has been no independent audit.

Self-review: passed. Independent audit: not yet performed.
