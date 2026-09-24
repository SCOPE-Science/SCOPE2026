# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/040`  
**Audit date (UTC):** 2026-09-24  
**Audited public head:** `5578c014cee5dc844817cf329cc783e9debef2eb`  
**Audited source-tree SHA:** `fe6a8e3d22f98382eba73bd1a295120c9333029d`  
**RESULT.md blob:** `6de095aee775d7e2c67c2a4ecfe62a4e4c1a73d`  
**Reviewer:** separate AI independent audit for the SCOPE three-axis campaign.

## Scope and claim extracted

The record exhaustively studies the labelled `6 x 6` binary matrices with every row and column sum equal to 3. It claims there are 297200 matrices; their permanents are distributed as
`17:21600, 18:216000, 20:59400, 36:200`; the minimum is 17; all 21600 minimizers form one orbit under independent row and column permutations; and a displayed matrix `M*` is a minimizer. It compares the exact minimum with Schrijver's general lower bound and Bregman–Minc's maximum bound.

## Correctness — PASS

I independently reconstructed the finite census without using the record's verification scripts.

Generation used all 20 six-bit masks of Hamming weight three and row-by-row backtracking with exact column-sum feasibility pruning. This produced **297200** matrices, independently matching OEIS A001501 at `n=6`.

For every generated matrix I evaluated the permanent with an independent Ryser inclusion-exclusion implementation. Popcounts `|row & S|` were precomputed for the 20 possible rows and all 64 column subsets; the 64 signed products were then accumulated for every matrix. The resulting exact distribution was:

- permanent 17: 21600 matrices;
- permanent 18: 216000;
- permanent 20: 59400;
- permanent 36: 200.

The counts sum to 297200, and the minimum/maximum are 17/36 as claimed.

I also encoded the displayed `M*` directly, recomputed `per(M*) = 17`, generated its full `S_6 x S_6` row/column orbit, and obtained exactly 21600 distinct labelled matrices. Every permanent-17 matrix in the independently generated census lies in that orbit, so the single-minimizer-orbit assertion is independently confirmed.

The background comparisons are numerically consistent: Schrijver's cubic bipartite bound gives `(4/3)^6 = 4096/729 < 6`, hence only the integer lower bound 6 at this order, while Bregman–Minc gives the sharp upper value 36 because 3 divides 6.

## Originality — PASS, but only narrowly

Targeted searches were made for the exact minimum, the four-value distribution, and the minimizer orbit, including:
- `"6x6" permanent 17 row sums 3 column sums 3`;
- `"297200" permanent 6x6 3-regular bipartite`;
- `"D(6,3)" permanent 17`;
- `"3-regular bipartite" 6 6 permanent 17`;
- `"permanent distribution" "6x6" (0,1) matrices`.

No prior source located in these searches stated the exact `17/18/20/36` distribution or the one-orbit minimizer classification.

The closest prior material instead supplies surrounding facts:
- OEIS A001501 gives only the cardinality 297200 at `n=6`;
- Schrijver's theorem gives a general lower bound for perfect matchings in regular bipartite graphs;
- Bregman–Minc gives the general upper bound;
- the House of Graphs census records only **five connected cubic bipartite graphs on 12 vertices**.

Thus the precise labelled permanent census appears not to be directly tabulated in the located prior literature. This originality judgment is limited to the exact finite table/orbit statement, not to the underlying inequalities, graph classification, or algorithms.

## Scientific value — FAIL

The residual contribution is too small for this campaign's scientific-value standard.

A `6 x 6` matrix in this class is the biadjacency matrix of a cubic bipartite graph on 12 vertices with a fixed bipartition. The House of Graphs census shows that there are only **five connected** cubic bipartite graph isomorphism types on 12 vertices. If such a graph is disconnected at this order, each cubic bipartite component must have at least six vertices, so the only disconnected type is `K_{3,3} disjoint union K_{3,3}`. Consequently the entire unlabelled structural universe behind the 297200 labelled matrices consists of only six graph types.

The record therefore expands a very small finite isomorphism census into a labelled distribution and evaluates one elementary invariant on it. It does not establish a pattern over `n`, improve Schrijver's or Bregman–Minc's theorem, identify a new asymptotic regime, or derive a structural characterization of minimizers beyond this single tiny order. The exact minimum 17 is computationally correct, but its gap from the general lower bound at `n=6` is not by itself a scientifically consequential sharpness result.

The exhaustive certificate is useful as a reproducibility benchmark or exercise. Under the campaign rule that routine exhaustive searches and small finite tables are not automatically valuable, however, that utility is insufficient for accepted-finding status.

## Bounded repair attempt

A bounded rewrite could honestly present the work as a benchmark table for the six graph types at order 12, but that would make the limited scope even clearer and would not cure the value failure. A genuinely worthwhile repair would require a new structural theorem, a sequence of exact minima across nontrivial orders, or an explanation/generalization of the minimizer type. Those are new research tasks, not bounded repairs to this record.

## Final disposition

- **Correctness:** passed.
- **Originality:** passed narrowly for the exact finite table/orbit.
- **Scientific value:** failed.
- **Disposition:** **failed / withdraw from accepted findings**.

This is a scientific-value rejection, not an allegation that the enumerated numbers are wrong. Historical files should remain preserved in the failed-attempt archive.
