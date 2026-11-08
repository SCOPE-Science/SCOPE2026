# Scientific review

## Correctness — PASS

For the exact stated domain \(n\ge3\), the three-step conservation law makes every vertex fire the same number of times. Only one or two firings per vertex permit primitive period three. For one firing, the proof obtains three exact chip intervals, one for each firing phase; they are nonempty precisely when all three phase groups are nonempty. The product of their enumerators and multinomial phase assignments yields \(P_n(z)\). A coordinatewise chip complement interchanges the one-firing and two-firing families. Each positive phase-size triple has a contiguous mass range with upper endpoint \(n(n-2)\); maximizing \(ab+bc+ca\) provides the exact lower endpoint and proves no internal gaps. The endpoints and orbit counts follow from surjection enumeration and periodicity. Two distinct implementation styles passed from package files: direct state enumeration through six vertices and independent firing-word interval enumeration through nine vertices. Finite tests are supplemental to the full proof.

## Originality — PASS, qualified

Levine, arXiv:0811.2800 (primary full text accessed; relevant §§1 and 4 inspected), establishes complete-graph period/activity and the qualitative middle window, under a self-loop convention conjugate to this loopless convention by a one-chip-per-vertex shift. The current work does not rely on this convention difference for originality. Jiang, arXiv:1003.0943 (primary full text accessed; relevant results and proof sections inspected), provides possible periods and general lemmas rather than an energy-refined period-three census. Jiang–Scully–Zhang, arXiv:1211.6786 (primary full text accessed; relevant results and proof sections inspected), classifies firing patterns but not the chip-height multipliers and sharp mass bands. Ji–Li–Wang, arXiv:2408.10508 (primary full text accessed; relevant results and proof sections inspected), proves that period three is excluded strictly inside the middle-stair interval, not exact counts at its two excluded endpoints. The assessed contribution is the exact polynomial and all-chip-total support with endpoint populations. Checks of nearby indexed results and accessible prior research records found no implication covering this claim. Unindexed earlier work is a residual priority risk; absence from a search is not proof of novelty.

## Mathematical value — PASS

Exact mass-resolved primitive-orbit counts are natural dynamical observables in fixed-energy sandpile systems. Here the complete graph is the canonical mean-field example underlying the devil's staircase. The theorem goes beyond period existence: it identifies two *complete* intervals of attainable chip totals, the exact central forbidden gap, the exact numbers at both sharp exclusion endpoints, and a binomially structured endpoint extremizer. The all-size classification is a meaningful finite-energy benchmark independent of a downstream application. Its value is not based on code or mere correct restatement of the known activity theorem.

## Limitations and residual scientific risk

The theorem covers initially periodic primitive-three configurations only, not transient basins or other periods. The overlap assessment cannot rule out older unindexed enumerations. The new derivation is elementary but the resulting complete all-parameter mass polynomial and endpoint counts are not stated in the primary sources inspected. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
