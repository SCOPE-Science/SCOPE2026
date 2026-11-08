# Scientific assessment

## Correctness — PASS

The orientation lemma follows directly from the forbidden length-one prefix/suffix match. The maximum second-one and third-one indices satisfy \(I+J\le n-1\), because otherwise a one-one prefix equals a one-one suffix at length \(n-J\). Conversely this inequality rules out suffix starts at the second or third marker by giving a mismatch of the count of ones, proving complete equivalence rather than only a necessary bound. Each codebook lies in a maximal integer-rectangle \(B_{n,t}\), whose exact size is \(t(2n-3-3t)/2\). Optimizing yields the closed capacity and every maximizing rectangle. Direct executable checks confirm compatibility and small exact global optima, but no finite cutoff is taken as an infinite proof.

## Originality — PASS with historical qualification

Full scientific texts checked: Chee–Kiah–Purkayastha–Wang (arXiv:1209.0236), Blackburn (arXiv:1303.1026), Blackburn–Esfahani–Kreher–Stinson (arXiv:2211.10309), Stanovnik–Moškon–Mraz (2024, DOI:10.1007/s10623-023-01344-z), and Stanovnik–Moškon–Mraz (arXiv:2410.18458). These address unrestricted codes, prohibited overlap-length sets, general maximum-code optimization, or approximately balanced / restricted-run words, rather than this exact sparse fixed-weight-three capacity plus complete extremizer classification. In particular, a generic unrestricted upper bound is not a sharp bound in this weight layer, and results for roughly half-positive words do not imply the sparse \(n\)-variable classification. There is an unresolved possibility of an implicit specialization or unindexed prior theorem; no mathematical priority beyond inspected evidence is asserted.

## Value — PASS

Fixed marker count is a natural constrained-synchronization model. Weight three is the first case with two independent interior marker positions. Here their prefix/suffix compatibility collapses to a sharp global rectangle condition. The result gives exact capacity for all lengths, asymptotic growth, and a full classification of codebook extremizers including the residue-three multiplicity transition, not simply a finite table or a substitution into an unrestricted result.

## Boundaries and reproducibility

See `RESULT.md` for definitions and proof and `verify.py` for executable independent finite checks. Only the same mathematical assessment is recorded; independent external validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
