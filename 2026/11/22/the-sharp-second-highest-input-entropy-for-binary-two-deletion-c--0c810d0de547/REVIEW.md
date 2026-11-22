# Scientific review

## Correctness — PASS

The statement fixes the alphabet, transmission prior, two-position deletion law, and embedding multiplicities. The normalizing count \(4\binom{n+2}{2}\) follows from counting all embeddings into all length-\(n+2\) inputs. The proof derives the exact second-level value and equality cases using the source's checked run identity, a strict cost for each nonsingleton run, convex minimization of the two endpoint weights, and a strict derivative bound separating every case with at least two nonsingleton runs. The cases \(n=2,3\) are included explicitly. Both shipped independent finite checkers report PASS. Neither checker is used to infer the all-length theorem.

Risks: the all-length argument depends on the published run identity and its adjacent-increment inequality, which have been read in the primary manuscript and reproduced in the proof with explicit hypotheses. The new inequalities (5)--(7) require \(n\ge4\), as ensured by at least two nonsingleton runs. No unproved extension to other channels is claimed.

## Originality — PASS against inspected material

Ma and Zhang, arXiv:2611.01064v1, already establish the unique alternating maximizers, and their ancillary `results.json` contains finite strict runner-up examples. This finding does **not** claim those facts as new. The new all-length statement specifies the entire second-highest entropy level and its precise equality class, including a positive exact gap and limiting constant. The publication's global-minimizer inequality is weaker than that exact stability classification. The manuscript's Section 3 proof, Section 6 finite comparisons and ancillary entries were compared to the claimed result; related prior conditional-entropy results were also inspected. Search for second-largest entropy, balanced single-double-run aliases and sharp posterior stability produced no all-length covering theorem.

Residual priority risk: earlier or unindexed work might already contain an equivalent second-level classification. The source's finite runner-up table means the novelty is the **all-length proof and formula**, not the initial finite examples.

## Value — PASS

The established alternating optimum is qualitative: it does not quantify the best competing received words or the entropy lost by the nearest nonalternating observation. This result identifies a rigid, centrally balanced single-defect structure, gives an exact all-length quantitative stability gap, and proves a nonzero limit for the gap multiplied by blocklength. The precise second-extremal layer is a natural robustness invariant for conditional uncertainty under synchronization errors. It is not a rescaling of the known maximal-entropy formula and does not rely on arbitrary finite cutoffs.

## Literature and limits

- H. Ma and W. Zhang, *Maximal input entropy for binary two-deletion and two-insertion channels*, arXiv:2611.01064v1 (2026-10-31), Sections 2, 3, 6, and ancillary `results.json`: https://arxiv.org/pdf/2611.01064
- S. Singhvi, O. Sabary, D. Bar-Lev, E. Yaakobi, *Conditional Entropies of k-Deletion/Insertion Channels*, arXiv:2407.10026 (first public 2024-07-13), Sections IV, VI, VII: https://arxiv.org/abs/2407.10026

The conclusion is binary, two-deletion, uniform-prior only; other channel laws, alphabets, and error radii remain outside its scope. No independent scholarly audit has been performed.

Self-review: passed. Independent audit: not yet performed.
