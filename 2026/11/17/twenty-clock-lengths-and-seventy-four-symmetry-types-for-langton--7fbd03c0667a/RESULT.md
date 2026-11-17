# Twenty clock lengths and seventy-four symmetry types for Langton’s ant on the \(3\times4\) torus

## Finding

The standard Langton ant on the \(3\times4\) discrete torus has exactly **2,480** distinct primitive temporal cycles, whose lengths belong to exactly **twenty** classes. Under its **48** geometric rule symmetries, the primitive cycles split into exactly **74** symmetry types. Every state is periodic from its first update; the shortest period is **16** and the longest is **312**. Every period is divisible by **8**.

The complete counts are:

| Least temporal period | Primitive cycles | Geometric symmetry types |
| ---: | ---: | ---: |
| 16 | 384 | 8 |
| 24 | 152 | 8 |
| 40 | 192 | 5 |
| 48 | 112 | 3 |
| 56 | 144 | 5 |
| 64 | 48 | 1 |
| 72 | 564 | 18 |
| 80 | 144 | 3 |
| 88 | 96 | 2 |
| 96 | 16 | 1 |
| 104 | 24 | 1 |
| 112 | 96 | 2 |
| 120 | 48 | 4 |
| 128 | 48 | 1 |
| 136 | 192 | 4 |
| 144 | 16 | 1 |
| 152 | 84 | 3 |
| 168 | 12 | 1 |
| 184 | 12 | 1 |
| 312 | 96 | 2 |
| **Total** | **2,480** | **74** |

In particular, a temporal period alone does not determine the geometric orbit type: among the **564** period-72 cycles there are **18** inequivalent symmetry types. The **96** longest cycles form exactly two distinct symmetry types, each containing 48 cycles.

## Assumptions and scope

The sites are \(V=\mathbb Z/3\mathbb Z\times\mathbb Z/4\mathbb Z\), with 3 columns and 4 rows. Every site is white (bit 0) or black (bit 1), the ant occupies one site and faces north, east, south or west. At each synchronous step it reads its **current** site: white turns the heading clockwise and black counterclockwise; it flips that site's bit and then moves one cell in its new heading, with both coordinates taken periodically. Exactly one ant is present. Configurations are labelled, with no color, position or orientation restrictions.

A state is \(s=(B,p,d)\), where \(B\in\{0,1}^V\), \(p\in V\), and \(d\) is one of the four headings. Thus the state set has size \(2^{12}\cdot12\cdot4=196608\). A primitive temporal cycle is a distinct orbit under repeated application of one update, not a state count. A geometric symmetry type is an orbit of *temporal cycles* under the group \(G\) described below; time translates along a temporal cycle are already identified.

The symmetry group \(G\) consists of the maps
\[
(x,y)\longmapsto(\epsilon_x x+a,\epsilon_y y+b),\qquad
\epsilon_x,\epsilon_y\in\{-1,1},\ a\in\mathbb Z/3\mathbb Z,\ b\in\mathbb Z/4\mathbb Z.
\]
The spatial heading is transformed by the same two signs. A sign map with \(\epsilon_x\epsilon_y=-1\) additionally complements *all* board bits. Hence \(G\) has \(3\cdot4\cdot2\cdot2=48\) elements and commutes with the ant's update. The color complementation in orientation-reversing maps is essential.

## Proof

**1. Immediate periodicity.** The local update is bijective on these finite states. Given the resulting state \((B',p',d')\), first subtract the displacement along the final heading \(d'\) from \(p'\) to find the previously visited site \(p\). The bit before flipping was \(b=1-B'(p)\). The previous heading was \(d=d'-(1-2b)\pmod{4}\), indexing north, east, south, west clockwise. The previous board is \(B'\) with the bit at \(p\) toggled again. This is a two-sided inverse. Since the entire state set is finite, all states belong to cycles with no preperiod.

**2. Commuting geometric symmetries.** Every translation commutes with the local rule. A coordinate reflection reverses right and left turns; global bit complementation simultaneously exchanges their triggers, so the combined transformation commutes with the local rule. The allowed coordinate-sign transformations and translations form the 48-element group defined above. Quarter-turn rotations are not symmetries of an unequal-sided \(3\times4\) torus.

**3. Finite covering certificate.** `verify_direct.py` enumerates every integer in \([0,196607]\), decodes it to one board, site and heading, verifies both inverse identities, and follows each not-yet-labelled state until it returns to its start. It marks each visited state exactly once and obtains the 20 cycle counts in the table. For each cycle representative, it applies all 48 geometric transformations, identifies the cycle reached, and unions the resulting cycle labels. This gives exactly the 74 symmetry types in the table. The checker also verifies commutation with the ant map on *every* state for four generators (unit translations in each coordinate and the two complemented reflections), thus covering the entire group. It records every within-type orbit size in `direct_output.txt`.

**4. Independent Burnside certificate.** `verify_independent.cpp` uses a separately implemented, differently encoded ant update; it constructs the complete successor graph and checks that each state has indegree one. It counts every temporal cycle again. For each of the 48 group transformations it counts the temporal cycles mapped to themselves; Burnside's lemma gives the symmetry-type count at each period as the fixed-cycle sum divided by 48. `independent_output.txt` gives these exact sums. Both programs independently return the identical per-period table, the total state volume \(196608\), and the sharp maximum 312; in particular none has a cycle length outside the listed set.

These are exhaustive finite proofs because every one of the \(196608\) input states and every group transformation on the cycle representatives are processed with integer operations. They are not sampling or extrapolations.

## Verification

Run `python3 verify_direct.py` with standard Python 3, or compile and run `verify_independent.cpp` with a C++17 compiler (`c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`). Both scripts print `all_checks_passed` on successful completion. Their exact outputs are supplied as `direct_output.txt` and `independent_output.txt`. The second script uses Burnside counting rather than the union-find symmetry quotient used in the first.

The sum of all primitive cycle counts is \(2480\); the period-weighted sum is \(196608\); the sum of symmetry-type counts is \(74\). For the all-white board at the origin, the ant has period \(72\) when initially facing east (along the 3-site axis) and period \(56\) when initially facing north (along the 4-site axis), agreeing with the two orientation-specific entries of the 2019 rectangular table after exchanging axes. The census extends those particular orbit measurements to **all** initial boards, ant positions and headings.

## Relationship to prior work

Tsukiji and Hagiwara (2011) establish general time-reversibility for the traditional and generalized infinite-grid ant; they do not give a labelled finite \(3\times4\) full orbit count. The 2019 torus discussion supplies a uniform-board return period \(72\) for \(3\times4\), general parity lower bounds and the reflection–color-exchange symmetry. Those facts are credited, but do not imply the counts of other primitive periods or geometric cycle classes. Hagiwara and Tsukiji (2020) study reachability/approximation hardness on twisted tori, not this small ordinary untwisted torus. OEIS A386970 similarly records single-background return times in \(n\times3\), not all board states.

The present classification is particularly natural because \(3\times4\) is the smallest unequal-sided torus having at least three sites in each direction. Its periods do not determine its geometric orbit types: the 20 period labels refine into 74 classes, including 18 inequivalent period-72 classes. This breaks the one-period-one-symmetry-type pattern of the smallest square case, without asserting that the same pattern holds for any wider rectangle.

## Limitations

This theorem is specific to the \(3\times4\) torus and the stated turn-flip-move convention. No formula for larger rectangles, bound for all even circumferences, or behavior on the infinite lattice is claimed. Complete computational enumeration proves this **finite** claim, not any all-size assertion. The literature comparison did not establish absolute historical priority; unindexed computations of this small finite case may exist. Independent external mathematical validation has not been performed.

## References

1. T. Tsukiji and T. Hagiwara, “Recognizing the Repeatable Configurations of Time-Reversible Generalized Langton’s Ant Is PSPACE-Hard,” *Algorithms* **4** (2011), 1–15; https://doi.org/10.3390/a4010001 (open-access full text, published 2011-01-28).
2. C. Harris and D. Ledbetter, answers and discussion, “What is the period of Langton’s ant on a torus?”, Mathematics Stack Exchange (2019); https://math.stackexchange.com/questions/3296855/what-is-the-period-of-langtons-ant-on-a-torus (includes the all-white \(3\times4\) period 72, symmetry discussion, and parity lower bounds).
3. T. Hagiwara and T. Tsukiji, “Hardness of Approximation for Langton’s Ant on a Twisted Torus,” *Algorithms* **13** (2020), 344; https://doi.org/10.3390/a13120344 (open-access full text; different geometry and complexity question).
4. C. Moya Garcia, OEIS A386970, “Period of Langton’s ant on an n X 3 torus” (2025); https://oeis.org/A386970 (one uniform initial configuration per size, not a full state classification).
