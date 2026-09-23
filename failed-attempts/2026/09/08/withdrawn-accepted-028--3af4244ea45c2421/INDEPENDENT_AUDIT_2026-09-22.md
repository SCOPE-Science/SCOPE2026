# Independent three-axis audit — 2026-09-22 campaign

## Record and source identity

- Source path: `2026/09/08/028`
- Audited repository: `SCOPE-Science/SCOPE2026`
- Audited source tree: `cbbd3a64737a99202516d1d852b248afb2e51814`
- `RESULT.md` blob: `279e5c96f20804dfa6f8709e557e52070fa5dd50`
- `VERIFICATION.md` blob: `83b03a7f246da30fad50fa39962dbb6d7f0519f0`
- Review date (UTC): 2026-09-23
- Review type: separate AI independent audit; not human/expert attestation and not Lean/formal verification.

## Claim audited

The record fixes the 22 isotopy representatives of Latin squares of order 6 in McKay file order and claims a complete per-type table of transversal counts `T_i` and maximum numbers `p_i` of pairwise cell-disjoint transversals. It reports `p_max=4`, attained on eight isotopy types, with packing values only 0, 2, or 4, and states that no prior source publishes the distribution.

## Correctness — PASS

I independently fetched the 22 official order-6 isotopy representatives from Brendan McKay's `latin_is6.txt` data file and reconstructed the finite computation without using the record's verifier.

For each square I enumerated all 720 column permutations and accepted exactly those selecting six distinct symbols, obtaining the transversal-count vector
`[32,0,8,0,0,24,24,8,0,8,0,24,8,8,8,8,0,0,0,0,8,0]`.

I then independently solved maximum cell-disjoint set packing on the enumerated transversal families by depth-first branch-and-bound. This reproduced exactly the packing vector
`[4,0,4,0,0,4,4,2,0,2,0,4,2,4,4,2,0,0,0,0,4,0]`, so `p_max=4` and the record's eight file-order extremal types are correct.

No correctness defect was found in the central finite table.

## Originality — FAIL

The central scientific novelty claim is contradicted by older literature.

Ian M. Wanless, *A Generalisation of Transversals for Latin Squares*, Electronic Journal of Combinatorics 9 (2002), R12, gives an exhaustive order-6 table by **main class** of the maximum number of parallel (pairwise disjoint) transversals. Its table reports, for order 6, six main classes with maximum 0, two with maximum 2, and four with maximum 4; no other values occur. Thus the order-6 packing spectrum `{0,2,4}` and the exact maximum `4` were already published in 2002. The paper also notes an order-6 example with four parallel transversals. Open full text: `https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i1r12/pdf`.

McKay, McLeod and Wanless, *The number of transversals in a Latin square*, Designs, Codes and Cryptography 40 (2006), 269–284, reports exhaustive computation of the number of transversals in one representative of **every isotopy class** through order 9, using independent programs. Its order-6 row records minimum 0 and maximum 32, agreeing with the present 22-type table's range. Open full text: `https://users.cecs.anu.edu.au/~bdm/papers/transversals.pdf`.

The record's 22-row McKay-file-order table is a finer reindexing than Wanless's 12 main-class packing table and supplies explicit witnesses, but it does not make `p_max=4`, the packing spectrum, or exhaustive order-6 transversal enumeration new. The statement that the order-6 packing distribution was unknown/no prior source published it is materially overstated.

The decisive sources were lawfully available in full open access, so no institutional-download fallback was required.

## Scientific value — FAIL

After subtracting the 2002 packing classification and the 2006 all-isotopy transversal enumeration, the surviving contribution is principally a mapping of those finite facts to a particular 22-representative file order plus explicit packing witnesses. That is useful reproducibility/catalogue annotation, but it does not establish a new packing bound, new order, new structural characterization, new algorithmic method, or new asymptotic consequence.

Under the campaign's scientific-value standard, a file-order refinement and witness list for a completely enumerated classical order does not provide enough surviving scientific contribution to validate the record.

## Bounded repair considered

A bounded repair can accurately cite Wanless (2002) for the order-6 parallel-transversal packing spectrum and McKay–McLeod–Wanless (2006) for exhaustive isotopy-class transversal counting, then present the 22-row table as a derived index/witness supplement. That repair removes the false novelty claim but does not create a sufficiently original and substantial result. A legitimate retry would need a genuinely new theorem, new order/regime, or structural consequence not already present in these exhaustive classifications.

## Final disposition

- Correctness: **PASS**
- Originality: **FAIL**
- Scientific value: **FAIL**
- Disposition: **failed / withdraw from validated findings**

The finite table is reproducible and correct, but its main packing spectrum and exhaustive-transversal context were already published in stronger or directly covering form.
