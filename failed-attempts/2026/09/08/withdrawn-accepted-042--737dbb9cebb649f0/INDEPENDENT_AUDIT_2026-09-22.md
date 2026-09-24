# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/042`  
**Audit date (UTC):** 2026-09-24  
**Audited public head:** `d5a8e9fe353577f49b7ac6a899dfe5f1563518a2`  
**Audited source-tree SHA:** `c0b4f7601b872bf3feb257e1fc1eb8f587deb890`  
**RESULT.md blob:** `131cb772214d2579f2198386ed5de7d74a4c3c5a`  
**Reviewer:** separate AI independent audit for the SCOPE three-axis campaign.

## Scope and claim extracted

The record enumerates simultaneous `(4,5,7)`-core partitions and `(5,6,7)`-core partitions. It claims 10 and 21 objects respectively, gives complete size distributions, all partitions and beta-sets, Durfee sizes, maximum-size witnesses, and hook multisets. It correctly acknowledges that for the consecutive triple `(5,6,7)` the bare count/maximum facts are already consequences of known general results; the claimed new content is the explicit finite census and per-object metadata, plus the non-consecutive `(4,5,7)` table.

## Correctness — PASS

I independently reconstructed both finite censuses by direct hook-length testing, without relying on the record's abacus search or historical audit judgments.

Every simultaneous `(4,5,7)`-core is in particular a `(4,5)`-core. Olsson–Stanton's classical maximum-size theorem for coprime `(s,t)`-cores gives `(s^2-1)(t^2-1)/24`, hence a size bound of 15 for `(4,5)`-cores. Similarly every `(5,6,7)`-core is a `(5,6)`-core, with pair-core maximum 35. These bounds make exhaustive ordinary-partition scans through sizes 15 and 35 complete.

For every partition in those finite windows I constructed the Young diagram and computed every hook length directly. A partition was accepted only when no hook length was divisible by any member of the relevant triple. The clean-room scans found exactly:

- `(4,5,7)`: 10 partitions, with size distribution `0:1, 1:1, 2:2, 3:3, 4:1, 6:2`; maximum 6 attained exactly by `(4,1,1)` and `(3,1,1,1)`.
- `(5,6,7)`: 21 partitions, with size distribution `0:1, 1:1, 2:2, 3:3, 4:5, 5:2, 6:2, 8:2, 9:1, 12:2`; maximum 12 attained exactly by `(6,2,2,2)` and `(4,4,1,1,1,1)`.

For every surviving object I independently recomputed the beta-set `B={lambda_i + ell - i}` and Durfee size. These agree with the complete tables in `RESULT.md`. The two maximum-size objects in each family also reproduce the stated hook multisets.

As an external bound cross-check, later literature summarizing Olsson–Stanton explicitly states the pair-core maximum formula `(s^2-1)(t^2-1)/24`; therefore the finite scan windows above are not heuristic cutoffs.

## Originality — PASS only for the explicit finite tables

I actively searched for prior coverage using exact and equivalent phrases, including `"4,5,7"-core partitions`, `"5,6,7"-core partitions size distribution`, `simultaneous (4,5,7)-core`, and `simultaneous (5,6,7)-core`, in addition to searches around the cited general formulas. No located source tabulated the exact 10-object `(4,5,7)` list or the full 21-object `(5,6,7)` list with beta-sets/Durfee data.

However, substantial headline content for `(5,6,7)` is already covered by stronger general results. Yang, Zhong and Zhou, **“On the Enumeration of (s,s+1,s+2)-Core Partitions”**, arXiv:1406.2583 (2014), explicitly develops general formulas for the number and maximum size of `(s,s+1,s+2)`-core partitions. Substituting `s=5` covers the aggregate count/maximum portion of the `(5,6,7)` claim. This agrees with the record's own limitation statement. Later work on `(t,t+d,t+2d)`-cores likewise describes Yang–Zhong–Zhou as the established consecutive-triple maximum-size result.

Thus originality is credited only narrowly to the explicit finite tables and metadata not found in the searched sources; no originality is credited for the classical beta-set criterion, pair bounds, or the known `(5,6,7)` aggregate formulas.

## Scientific value — FAIL

After subtracting the known general results, the surviving mathematical contribution is a hand-sized data table: 10 objects in one family and 21 in the other, with per-object beta-sets, Durfee sizes, hooks, and size frequencies derived by routine finite enumeration.

The `(5,6,7)` headline count and maximum are already specializations of a general theorem, so the residual content there is mainly listing the 21 objects. The `(4,5,7)` family is non-consecutive but still consists of only 10 objects, obtained with the classical core criterion and a small finite search. The record does not derive a new formula for a family of triples, a structural bijection, a new asymptotic regime, or an algorithmic improvement of independent mathematical interest.

The tables are useful as examples or regression fixtures, but this campaign explicitly requires more than an arbitrary small computation, routine specialization, or finite reformatting to establish scientific value. On that standard, the residual contribution is insufficient.

## Bounded repair attempt

A bounded rewrite could accurately present these tables as illustrative datasets or verification fixtures, but it would not produce a new theorem or reusable structural insight. Rescuing scientific value would require a genuine generalization—for example a parameterized enumeration/size-distribution theorem for a nontrivial family containing `(4,5,7)`, or another structural result explaining the observed tables. That is new research rather than a bounded correction preserving this record's identity.

## Final disposition

- **Correctness:** passed.
- **Originality:** passed narrowly for the explicit finite tables only; aggregate `(5,6,7)` facts are known.
- **Scientific value:** failed.
- **Disposition:** **failed / withdraw from accepted findings**.

This is a scientific-value rejection, not an allegation that the enumerated partitions are incorrect. Historical source and audit files should remain preserved in the failed-attempt archive.
