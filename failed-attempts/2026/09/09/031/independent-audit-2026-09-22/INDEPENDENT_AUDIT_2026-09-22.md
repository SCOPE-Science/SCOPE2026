# Independent audit — 2026/09/09/031

Date: 2026-09-26. Disposition: failed; complete original package archived.

## Correctness — PASS

I independently implemented Murnaghan–Nakayama by enumerating all contained partitions after deleting each cycle-length skew shape, testing connectedness and absence of 2-by-2 squares directly on cells, and taking the sign from its row span. This separate border-strip enumeration matched every one of the 30,976 entries in the committed (S_{15}) character table. Using exact integer class sizes, I recomputed all 176 inner products (sum_mu |C_mu|chi^ho(mu)^2chi^
u(mu)/15!): every one is the stored positive integer. The minimum is 1, the maximum 18,269 at (ho), and the degree-weighted sum is (85,769,322,496=292,864^2). Thus the finite calculation is valid.

## Originality — FAIL

The candidate says no prior source certifies the full containment row for (n=15). Luo and Sellke, *The Saxl Conjecture for Fourth Powers via the Semigroup Property* (2015), section 7, explicitly state that they used a computer and the semigroup property with dominance to verify the Saxl conjecture **up to (ho_9)**. In particular (ho_5) of size 15 was already covered. Li's later triple-hook paper repeats this prior verification through (ho_9). The 176 exact multiplicities may be a separately reproduced data table, but the claimed new finite case settlement is preempted.

## Scientific value — FAIL for the stated conclusion

A correct machine-checkable coefficient row is useful as test data, but the record's proposed scientific conclusion is containment at (k=5), a case already established in a substantially larger prior range. It supplies no new structural proof, unresolved boundary, or analysis of the multiplicities beyond this small row. This assessment does not call the stored computation false.

## Primary source and replay

- Luo and Sellke, *The Saxl Conjecture for Fourth Powers via the Semigroup Property*, arXiv:1511.02387, section 7 concluding remarks p. 35: https://arxiv.org/pdf/1511.02387
- Li, *Saxl Conjecture for triple hooks*, arXiv:1811.10967: https://arxiv.org/abs/1811.10967
- Candidate `artifacts/chartable15.json` and `artifacts/staircase_row.json`; independent cell-based border-strip recursion and exact inner products described above.
