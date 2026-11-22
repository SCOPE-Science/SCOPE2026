# Self-review

## Correctness (C): PASS

The definition is the original balanced empirical OVL-\(q\) minimum over ordered cuts. A concavity argument moves all cuts to the between-run boundaries without increasing cost; any cell containing \(s\) complete alternating runs has at least \(\lfloor s/2\rfloor\) minority observations. For \(d=(R-1-q)_+\), this yields the universal bound \(n\rho_q\ge\lceil d/2\rceil\). Every disjoint literal block `1001001` provides a two-cut removal at cost one, and sufficiently many such blocks attain the lower bound exactly for all critical-window \(d=O_P(\sqrt n)\). The block count is linear in \(n\) with variance \(O(n)\), while the classical balanced-runs distribution has a standard-normal fluctuation on scale \(\sqrt{n/2}\). The main positive-part limit and zero atom follow. Exact finite binary-word minimizations and independent combinatorial checks pass; finite checks are not used as an infinite proof.

## Originality (O): PASS, with stated historical risks

The primary OVL paper (Komaba, Johno, Nakamoto, arXiv:2206.03166, first public 2022-06-07), the related one-sample paper (arXiv:2408.10612), a 2026 public exact-DP and q=3,4 finite-table study, and classical runs formulas were compared against the precise claim. The primary defines the statistic and gives finite enumeration and q=2 theory; the later work gives exact finite computation, and the classical runs law supplies the already-known count fluctuations. None of the inspected results covers the **strictly positive near-saturation cost**, the disjoint-pattern exact-attainment mechanism, or the complete positive-part Gaussian scaling law. Actual mathematical-record searches and the accessible prior scientific claims revealed no direct match. An older more general segmentation result and the uninspected separate PDF of the later finite-DP study remain residual priority risks; absence of a search hit is not treated as proof of worldwide novelty.

## Value (V): PASS

The natural parameter \(q\) controls a published overlap test's partition complexity. The proved \(q=n+O(\sqrt n)\) phase transition quantifies exact-fit overfitting under the continuous two-sample null, including half of samples having exactly zero empirical overlap at critical tuning. The sharp non-Gaussian null calibration and cheap local edit mechanism are substantive mathematical structure rather than an arbitrary small table. No recommendation of high-q test power or adaptive tuning is inferred.

## Primary comparisons and limitations

The exact runs distribution and Gaussian limit are old mathematical inputs. The new statement is restricted to equal sample sizes, continuous common-null sampling and deterministic cut sequences. A general finite dynamic program does not itself establish the joint limit. The secondary 2026 public abstract and claim ledger were read; its separate PDF was not. Historic high-complexity segmentation coverage may exist. Verification is same-model only, not an independent audit.

Self-review: passed. Independent audit: not yet performed.
