# Self-review

## Correctness — PASS

The exact model is explicitly defined for all \(0<a<b\), \(A,B,T>0\) and \(0\le t\le T\). The two tissue-specific linear-quadratic cross-repair sums each contain three pairwise interactions; only those involving the middle fraction vary with its time. After subtracting the time-independent terms, the objective is precisely the claimed two-exponential contrast. Reflection about \(T/2\) reduces the global problem to a compact half-interval. Its derivative factors as a strictly positive factor times \(r-R(x)\). The crucial claim that \(R\) is strictly increasing follows from \(\sinh z\cosh z>z\) for \(z>0\), checked directly by differentiating both sides. Its endpoint limits are exactly the displayed \(r_0,r_1\). All equality cases and global comparisons therefore follow without numerical extrapolation. The square-root law is a Taylor consequence; the minimum-separation corollary changes only the domain endpoint. The packaged standard-library checker reproduced 195,602 finite assertions as a supplement and not a substitute for proof.

## Originality — PASS, provisional historical priority

The foundational linear-quadratic incomplete-repair exponential model is prior work, not the claim. The closest prior optimization problems are materially different: Yang and Xing's general tumor BED optimization subject to fixed normal BED; Wein, Cohen and Wu's numerical variable-dose-size dynamic program with repopulation and prescribed fractionation patterns; Altman et al.'s single-fraction rearrangement of distinct dose segments for single-tissue cell kill; Bertuzzi et al.'s weekly optimization of fraction **sizes**, subject to normal-tissue damage limits; and Putora et al.'s full-text compensatory-treatment calculation. These formulations do not by their inspected statements provide the exact global three-phase classification for **equal three doses with two fixed event times and a weighted difference of distinct exponential repair responses**. A 2025 open full-text comparison optimizes the number of daily fractions and beamlet intensities, not free subdaily event gaps. The only structurally proximate published database entries concern different objective functions (two-exponential D-optimal sampling or periodic drug-level fluctuation). The new result is not inferred from the absence of matching titles; statements, free variables, and objective function implications were compared.

Remaining risks: Yang–Xing's and Bertuzzi's full texts, the earlier Wein working paper, and Altman's full paper were not fully accessible. Broader literature on optimal arrangement for differences of two exponentials could subsume the result by a nonmedical equivalence. Neither risk is represented as settled; independent historical and mathematical verification are outstanding.

## Value — PASS

The constrained three-event experiment is the smallest nontrivial equal-dose timing design with reflection symmetry. It isolates a genuine tradeoff: preserving tumor-side unrepaired quadratic interaction versus limiting normal-tissue cross-damage with a distinct repair clock. The complete sharp division into uniform, two symmetry-broken interior, and clustered schedules is a structural classification that neither a numerical optimum nor the known one-tissue models supply. The exact two ratio boundaries, the square-root onset and the minimum-separation cutoff expose sensitivity to parameters and delivery feasibility in a reproducible benchmark. The claim does not need a calibrated clinical survival model to be a useful mathematical boundary; however, it cannot support any clinical recommendation by itself.

## Closest literature and access limits

- Yang and Xing (2005): publisher abstract and exact first-publication date inspected; full text not available via attempted lawful routes.
- Wein, Cohen and Wu (1999 working paper; 2000 journal): institutional working-paper metadata and journal abstract inspected; full working-paper text unavailable in this run.
- Altman, Chmura, Deasy and Roeske (2006): institutional author-record abstract and detailed summary inspected; full text unavailable.
- Bertuzzi, Bruni, Papa and Sinisgalli (2012 online): publisher abstract inspected; subscription full text inaccessible.
- Putora et al. (2012): open-access full HTML text, including assumptions, formulas, Methods and Discussion, inspected; its decision problem does not contain the stated continuous three-event repair contrast.
- Bertuzzi et al. (2020): accessible review abstract inspected; PDF not obtainable through available interface; this is a priority limitation.
- Shinde et al. (2025): open full-text methods and decision variables inspected; no continuous within-course timing decision.

Self-review: passed. Independent audit: not yet performed.
