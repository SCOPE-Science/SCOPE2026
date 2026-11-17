# Eight symmetry types classify every Langton-ant orbit on the \(3\times3\) torus

## Finding
Consider the standard two-colour, one-ant Langton dynamics on the labelled periodic \(3\times3\) square grid: on white, turn right; on black, turn left; flip that cell; then move one step. A state records all nine cell colours, the ant's position, and one of four directions. **Every one of the \(2^9\cdot9\cdot4=18{,}432\) states is periodic. There are exactly \(288\) primitive temporal cycles, with precisely eight possible least periods.** Moreover, all temporal cycles with a given least period are equivalent under grid translations, quarter-turn rotations, and the combination of a spatial reflection with global colour complementation.

| Least temporal period | Number of primitive temporal cycles | States | Representative state code |
| ---: | ---: | ---: | ---: |
| 18 | 24 | 432 | 116 |
| 30 | 24 | 720 | 128 |
| 42 | 24 | 1,008 | 43 |
| 66 | 24 | 1,584 | 0 |
| 70 | 72 | 5,040 | 40 |
| 74 | 72 | 5,328 | 42 |
| 78 | 24 | 1,872 | 120 |
| 102 | 24 | 2,448 | 385 |
| **Total** | **288** | **18,432** | — |

Thus there are exactly **eight temporal-cycle classes under the specified extended spatial symmetry group**, one for each period. The all-white initial board is represented by code 0 and belongs to period 66; it does not determine the other seven possible periods. The maximum least period over all states is 102.

## Assumptions and scope
The grid is \(\mathbb Z/3\mathbb Z\times\mathbb Z/3\mathbb Z\), with directions \(d=0,1,2,3\) denoting north, east, south, west. Encode a state as the integer
\[
 z=4(9b+p)+d,\qquad 0\le b<512,\quad 0\le p<9,\quad 0\le d<4,
\]
where bit \(p=3y+x\) of \(b\) is one exactly when cell \((x,y)\) is black. North decreases \(y\). For a state \((b,p,d)\), put \(c=(b\mathbin{\mathrm{div}}2^p)\bmod2\), define \(d'=d+1\pmod4\) when \(c=0\), and \(d'=d-1\pmod4\) when \(c=1\). Flip bit \(p\) and move in direction \(d'\), both coordinates modulo three. This completely defines the time-one permutation \(F\). The convention is **turn–flip–move**, as in the 2019 finite-torus discussion; the equivalent arrival-cell convention used in some other literature requires recoding the ant's position.

The spatial group \(G\) has order \(72\): nine translations composed with the eight symmetries of the square, where every orientation-reversing symmetry is accompanied by complementation of all nine colours. Each element of \(G\) commutes with \(F\). The claim is solely for the \(3\times3\) torus with one ant; no all-size cycle classification is asserted.

## Proof
**(1) Invertibility.** From the new ant position and new direction, reverse its last spatial move to recover the previously occupied cell. Flip that cell's recorded colour back and use its recovered old colour to undo the final quarter-turn. This uniquely recovers the prior state, so \(F\) is a permutation of the finite state space. Every state is therefore periodic from time zero.

**(2) Symmetry.** Translations and rotations merely relabel the ant's cell, colours, and direction, and therefore commute with \(F\). A spatial reflection exchanges left with right. Complementing the cell colours simultaneously exchanges which of those turns is prescribed, so the composition also commutes with \(F\). These transformations generate \(G\) with \(9\cdot8=72\) distinct elements.

**(3) Exact finite covering certificate.** The standalone checker `cover_certificate.py` implements precisely the state encoding and rule above. For each of the eight representative integer codes in the table, it computes successive iterates until the claimed first return, asserting that no state repeats earlier. It then forms the union of all temporal iterates of all \(72\) group images of that representative. For the eight representatives in increasing period order, the checker establishes union sizes
\[
 432,\ 720,\ 1008,\ 1584,\ 5040,\ 5328,\ 1872,\ 2448.
\]
It checks that the eight unions are pairwise disjoint, that the group transformations commute with \(F\) on **all** \(18{,}432\) states, and that \(F\) maps the entire state set bijectively to itself. Their sizes sum to \(18{,}432\), so no other states, cycles, periods, or symmetry classes exist. Dividing each union's size by its primitive period gives the table's exact cycle multiplicities. Because each union is the image of a single seed under time evolution and \(G\), every union represents one symmetry class of temporal cycles.

**(4) Independent exhaustive decomposition.** The separate C++17 file `exhaustive_cycles.cpp` directly enumerates every state without using the representative list or any symmetry reduction, checks both explicit forward and backward transitions, and counts each primitive cycle by tracing from its smallest unvisited member. Its eight period counts agree with the covering certificate, including the sharp maximum 102.

The two approaches provide a finite exhaustive proof and an independently structured cross-check of the computational certificate. They do not rely on a statistical sample or on extrapolation from smaller configurations.

## Verification
Compile and execute `exhaustive_cycles.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic exhaustive_cycles.cpp -o exhaustive_cycles && ./exhaustive_cycles`; run `python3 cover_certificate.py`. The expected complete outputs are included as `exhaustive_cycles.out` and `cover_certificate.out`. Both programs were executed with successful internal assertions. The second program checks the symmetry action on all states and covers every state from eight seed cycles. The first independently enumerates all cycles and checks an explicit inverse.

## Relationship to prior work
Gale, Propp, Sutherland and Troubetzkoy introduced Truchet-tile and symmetry methods for generalized ant dynamics in the plane, but do not give this finite-torus temporal-cycle census; their proof explicitly notes that a planar argument need not hold on a torus. Tsukiji and Hagiwara studied reversible generalized ant complexity on infinite lattices, not the present small torus's full permutation cycle structure. A 2019 discussion by Connor Harris and others already identifies reversibility, translations, rotations, and reflection coupled with colour inversion, and tabulates the 66-step return from the **all-white** \(3\times3\) state. Those ingredients, including the general symmetry mechanism and the period-66 example, are prior knowledge. A later OEIS entry also records that one special initial-state period. The new contribution is the complete 288-cycle census and its eight full symmetry types, not the existence of the ant, reversibility, or any individual all-white return.

## Limitations
The result concerns one finite torus, not an asymptotic or all-circumference formula. The exhaustive finite checker is part of the proof, so confirmation involves executing and examining ordinary source code. Although the inspected sources do not state or imply this complete census, an unidentified historical enumeration could exist. Independent external mathematical validation has not been performed.

## References
1. D. Gale, J. Propp, S. Sutherland, and S. Troubetzkoy, *Further Travels with My Ant*, arXiv:math/9501233v1 (publicly posted 1995-01-19), https://arxiv.org/html/math/9501233v1 .
2. T. Tsukiji and T. Hagiwara, *Recognizing the Repeatable Configurations of Time-Reversible Generalized Langton's Ant Is PSPACE-Hard*, Algorithms **4** (2011), 1–15, https://doi.org/10.3390/a4010001 (published 2011-01-28).
3. *What is the period of Langton's ant on a torus?*, Mathematics Stack Exchange question 3296855 and answers (initial question 2019-07-18), https://math.stackexchange.com/questions/3296855/what-is-the-period-of-langtons-ant-on-a-torus .
4. OEIS A386970, *Period of Langton's ant on an n X 3 torus* (initial sequence date 2025-08-11), https://oeis.org/A386970 .
