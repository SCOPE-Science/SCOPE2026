# An exact interval of disagreement between rainwater volume and full-demand reliability

## Finding
Consider a rainwater tank of capacity \(7\), initially empty, with daily demand \(4\) and four daily rainfalls whose multiset is \(\{0,z,6,6\}\), where \(0\le z\le3\). Under the **fill–cap–serve** operating rule specified below, two standard performance criteria may select disjoint sets of rainfall orders. Precisely, **no rainfall order simultaneously maximizes total supplied volume and the number of fully supplied days if and only if \(1\le z<2\)**. In that window, the maximum volume is \(12+z\), attained with only two fully supplied days, whereas the maximum number of fully supplied days is three and the largest volume among its maximizers is \(11+z\). Consequently the time-reliability optimum sacrifices exactly one volume unit. Outside that window a common optimizer exists. The boundary values \(z=1\) and \(z=2\) are included in the disjoint and common regimes, respectively.

## Assumptions and scope
For each day \(t\in\{1,2,3,4\}\), write \(r_t\) for daily rain, \(S_t\) for end-of-day storage, \(Y_t\) for supply, and \(O_t\) for overflow. The tank starts at \(S_0=0\); rain arrives **before** demand is served. The deterministic update is
\[
W_t=\min\{7,S_{t-1}+r_t\},\quad O_t=(S_{t-1}+r_t-7)_+,\quad Y_t=\min\{4,W_t\},\quad S_t=W_t-Y_t.
\]
There are no losses besides overflow and demand; daily demand is fixed and unmet portions do not carry forward. All twelve distinct labeled permutations (or fewer when \(z=0\)) of \(\{0,z,6,6\}\) are admissible. Define supplied volume \(V=\sum_{t=1}^{4}Y_t\) and fully supplied days \(F=\sum_{t=1}^{4}{\bf1}_{\{Y_t=4\}}\). Their respective maximizers are the volume-reliability and time-reliability optimizers. The question compares hypothetical rainfall chronologies, rather than a physical control that can reschedule storms.

## Proof
**Volume maximum.** Conservation gives \(V+S_4+\sum O_t=12+z\), hence \(V\le12+z\). The order \((6,z,6,0)\) has, for \(0\le z<2\), yields \((4,2+z,4,2)\) and for \(2\le z\le3\), yields \((4,4,4,z)\). In both cases there is no overflow or end storage, and \(V=12+z\). It has two fully supplied days for \(z<2\) and three for \(z\ge2\).

**Full-demand maximum.** Four days cannot all be fully supplied because total inflow \(12+z\le15<16\). For \(0\le z<1\), three full days are impossible: with a single zero-rain day, at most two other days can be fully served unless the two consecutive high-rain days create enough carryover to fully serve the low-rain day; the latter needs \(z\ge1\). This statement is confirmed directly by the twelve-order case partition in the next paragraph. The exhibited volume-maximizing order already supplies two days fully, hence \(F_{\max}=2\) for \(z<1\). For \(1\le z\le3\), the order \((0,6,6,z)\) has \((Y_1,Y_2,Y_3,Y_4)=(0,4,4,4)\) because the last day starts with storage \(3\) after the pair of sixes, so \(F_{\max}=3\).

**Sharp incompatibility on \(1\le z<2\).** In this interval, enumerate the possible positions of the zero and the two sixes. The twelve orders and their number of fully supplied days are:

| Order | Fully supplied days | Supplied volume |
| --- | ---: | ---: |
| \((0,6,6,z)\) | 3 | \(12\) |
| \((0,6,z,6)\) | 2 | \(10+z\) |
| \((0,z,6,6)\) | 2 | \(8+z\) |
| \((6,0,6,z)\) | 2 | \(12+z\) |
| \((6,0,z,6)\) | 2 | \(10+z\) |
| \((6,6,0,z)\) | 2 | \(11+z\) |
| \((6,6,z,0)\) | 3 | \(11+z\) |
| \((6,z,0,6)\) | 2 | \(10+z\) |
| \((6,z,6,0)\) | 2 | \(12+z\) |
| \((z,0,6,6)\) | 2 | \(8+z\) |
| \((z,6,0,6)\) | 2 | \(10+z\) |
| \((z,6,6,0)\) | 2 | \(11+z\) |

Each row follows by four substitutions into the displayed recurrence; the table exhausts the \(4!/2!=12\) distinct orders. Hence the only three-full-day orders are \((0,6,6,z)\) and \((6,6,z,0)\). Their volume values are respectively \(12\) and \(11+z\), so the largest volume achievable with three full days is \(11+z<12+z\). There can be no joint optimizer. The table also shows exactly one unit of excess capacity loss in either three-day optimizer; in the first ordering the one lost unit is overflow, while the second has one unit of overflow and zero final storage. For \(0\le z<1\), the same twelve case types show at most two full days (the only candidates for three full days above fail on their last required full day); for \(2\le z\le3\), \((6,z,6,0)\) gives three full days and maximal volume. This completes the iff classification, including both endpoints.

## Verification
The standalone Python 3 checker `check.py` uses exact rational arithmetic (`fractions.Fraction`) and enumerates the complete finite set of storm orders at fourteen rational values, including \(z=0,1,2,3\), and multiple interior values on both sides of both thresholds. It asserts conservation, admissible state bounds, both optimum values, compatibility, the exact optimizer set for three fully served days inside the incompatibility interval, and a representative numerical tradeoff. It prints `PASS exact rational checks: 554`. These finite samples do not establish the continuum theorem; the twelve-order symbolic case partition and conservation argument above do.

At \(z=3/2\), \((6,3/2,6,0)\) supplies \(27/2\) units but fully meets only two days; \((6,6,3/2,0)\) fully meets three days but supplies only \(25/2\) units.

## Relationship to prior work
Rainwater-harvesting research distinguishes time-based reliability (fraction of demand periods completely met) and volumetric reliability (fraction of total demand volume supplied). Hanson and Vogel (2014) analyze generalized storage–reliability–yield relationships with simulated precipitation, and Liaw and Tsai (2004) examine storage sizing for domestic rainwater harvesting. Ndiritu and colleagues (2011) examine yield–reliability simulation for rural water supply; Mitchell (2007) evaluates simulation-rule sensitivity. The exact finite **permutation-level incompatibility interval** for the two criteria under the present specified fill–cap–serve rule does not follow from the inspected storage-sizing or simulation relationships. A method that supplies the day's demand from *preceding* storage is not the fill–cap–serve model here, so the distinctions in update order are material. These comparisons do not establish historical uniqueness among all tank-scheduling literature.

## Limitations
This is a small exact benchmark for an idealized four-day, one-tank model, not a field estimate or a recommendation to schedule rainfall. Capacity, demand, and two major inflows are fixed; the result does not classify arbitrary tanks or longer sequences. A different demand-and-spill ordering, evaporation, leakage, stochastic rain, and demand carryover may change the optimality window. Some historical multiobjective cistern studies could not be inspected in full; mathematical novelty is provisional pending that comparison.

## References
- Hanson, L. S., and Vogel, R. M. (2014), *Generalized storage–reliability–yield relationships for rainwater harvesting systems*, Environmental Research Letters 9, 075007. https://doi.org/10.1088/1748-9326/9/7/075007
- Liaw, C.-H., and Tsai, Y.-L. (2004), *Optimum Storage Volume of Rooftop Rain Water Harvesting Systems for Domestic Use*. https://doi.org/10.1111/j.1752-1688.2004.tb01054.x
- Ndiritu, J., Odiyo, J., Makungo, R., Ntuli, C., and Mwaka, B. (2011), *Yield–reliability analysis for rural domestic water supply from combined rainwater harvesting and run-of-river abstraction*. https://doi.org/10.1080/02626667.2011.555766
- Mitchell, V. G. (2007), *How important is the selection of computational analysis method to the accuracy of rainwater tank behaviour modelling?* https://doi.org/10.1002/hyp.6499
