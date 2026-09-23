# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source tree: `f2fb84653525f70d60068b4f11f9353ee7c3ca9a`, verified unchanged before review.

## Correctness

The record's explicit 17-point set is internally consistent: its line-occupancy data and code interpretation give an `(17,3)`-arc / `[17,3,14]` NMDS example, and the committed exhaustive search supplies a plausible certificate that no eighth off-conic point can be added to the fixed conic. The central problem is not a demonstrated false witness.

## Originality

The literature comparison is decisively incomplete. In Dönmez–Akpınar–Pelen, *Near-MDS codes of lengths q+6 and q+7 from conics in PG(2,q)*, arXiv:2608.18192, Problem 6.2 explicitly states that for `q=9` a conic extends to `(n,3)`-arcs of maximal size `n=17=2q-1`, citing the earlier classification work of Marcugini, Milani, and Pambianco. The cited primary references are *Classification of the [n,3,n-3]_q NMDS codes over GF(7), GF(8), and GF(9)*, Ars Combinatoria 61 (2001), 263–269, and *NMDS codes of maximal length over F_q, 8<=q<=11*, IEEE Transactions on Information Theory 48 (2002), 963–966. Thus existence and maximal length 17 over `F_9`, including the conic-extension fact used as the record's headline, were already in the literature decades earlier.

## Scientific value

The record adds one explicit coordinate witness, line/weight statistics, a stabilizer computation, and an independent finite search, but these are ancillary invariants of a parameter set already covered by published classification/maximal-length work. Without a demonstrated inequivalence or invariant absent from those classifications, the residual material is not sufficient to preserve the accepted headline as a standalone novel finding. Repair would require a new comparison to the historical classification rather than a bounded wording change.

## Disposition

**FAILED.** The accepted package overclaims originality of a known maximal conic-extension/NMDS parameter.
