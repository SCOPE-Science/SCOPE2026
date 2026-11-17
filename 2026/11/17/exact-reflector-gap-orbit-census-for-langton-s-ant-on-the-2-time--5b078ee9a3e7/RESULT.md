# Exact reflector-gap orbit census for Langton's ant on the \(2\times n\) torus

## Finding

For every integer \(n\ge2\), take the ordinary binary Langton ant on a labelled \(2\times n\) square-cell torus. A full state records all \(2n\) binary cell colors, the ant's cell and one of its four compass directions. Count temporal cycles as distinct *orbits of labelled full states*, without identifying spatial rotations or direction reversal.

For each \(1\le j<n\), the number of primitive temporal orbits of length \(8j\) contributed by reflector gaps of size \(j\) is exactly
\[
 C_{8j}^{\mathrm{gap}}(n)=n\,2^{2n-j-1}.
\]
There are, separately, precisely
\[
 C_{4n}^{\mathrm{exception}}(n)=(n+1)2^{n+1}
\]
primitive temporal orbits of period \(4n\), arising from conserved column patterns with at most one reflector. **These two contributions must be added when \(n\) is even and \(j=n/2\)**. No other primitive periods occur. The map is bijective, so no trajectory has a transient. The largest period is \(8(n-1)\) for \(n\ge3\), and eight for \(n=2\).

For a uniformly chosen full state, the (possibly overlapping) contributions to the period law are \(\Pr_{\mathrm{gap}}(8j)=j/2^{j+1}\) and \(\Pr_{\mathrm{exception}}(4n)=(n+1)/2^n\). In particular, for each fixed positive \(j\), the probability of period \(8j\) tends to \(j/2^{j+1}\) as \(n\) grows, and
\[
\mathbb E[\text{least period}]=24-\frac{4(n^2+3n+6)}{2^n}\longrightarrow 24.
\]
Thus worst-case periods grow linearly with circumference, whereas the typical period has an exact size-biased geometric limit of finite mean.

## Assumptions and scope

A color is zero (white) or one (black). At every original step the ant turns right on white, left on black, flips the cell's color, and moves one unit forward. Coordinates are \(x\in\mathbb Z/n\mathbb Z\) and \(y\in\mathbb Z/2\mathbb Z\). Distinct compass directions are retained as directed moves even when opposite directions reach the same neighboring cell (this matters at \(n=2\)). Use the encoding north \(0\), east \(1\), south \(2\), west \(3\). Total full state count is \(8n\,2^{2n}\). Statements apply to arbitrary binary starting colorings and all ant positions and headings, not only the customary all-white seed.

## Proof

**1. Two-step return map and invariants.** The heading alternates vertical/horizontal each original update. At a vertical-heading instant, denote the ant's column by \(x\), row by \(y\), and first outgoing horizontal sign by \(h\in\{-1,+1\}\). Let \(c_{y,x}\) be the current cell colors and \(a_x=c_{0,x}\oplus c_{1,x}\) be their column parity. Define a binary invariant by
\[
 b_z=a_z\oplus\mathbf1_{\{z=x\}},\qquad z\in\mathbb Z/n\mathbb Z.
\]
A two-step macro-update flips the cells \((y,x)\) and \((y,x+h)\), moves the ant to the opposite row in column \(x'=x+h\), and restores a vertical heading. Hence column parity toggles precisely at the departure and arrival columns, and the marker also moves between them: every \(b_z\) stays unchanged. Writing the horizontal sign on the *next* macro-update as \(h'\), the two quarter-turns give
\[
 h'=h(-1)^{a'_{x'}}=-h(-1)^{b_{x'}},\qquad x'=x+h\pmod n.
\]
Thus columns with \(b_z=0\) act as fixed reflectors; those with \(b_z=1\) transmit the projected direction. This conservation-law framework is already present in the 2019 torus discussion cited below; the exact gap decomposition and full orbit count are what is established here.

**2. Periods for two or more reflectors.** Suppose that \(b\) has at least two zeros. For any chosen gap between successive zeros with exactly \(j\) cyclic edges, where \(1\le j<n\), the projected \((x,h)\) state runs back and forth between its two zero endpoints. There are exactly \(2j\) projected position-heading states in this component and its projected least macroperiod is \(2j\). On the outward and inward traversal of each gap edge, macrostep indices have opposite parity; because the active row switches each macrostep, the edge is used once in each row over a projected round trip. Consequently the two endpoint cells on *each* row are flipped once; each interior cell is flipped twice. After \(2j\) macrosteps the projected ant returns but the full binary coloring does not. After \(4j\) macrosteps both the coloring and row return, so the full macroperiod is exactly \(4j\), hence original-step period \(8j\). There is no smaller full period because the projected period is already \(2j\).

**3. At most one reflector.** If \(b\) has exactly one zero, every projected trajectory traverses the full ring in one direction, reflects at that zero, then traverses it backwards. The projected least macroperiod is \(2n\). Over these \(2n\) steps, every horizontal edge is traversed once on each row, so each cell flips twice and the whole full state returns. If \(b\) has no zeros, the projected heading is constant, with projected least macroperiod \(n\); when \(n\) is odd the ant's row differs after \(n\) macrosteps, and when \(n\) is even each row has each of its colors complemented after \(n\) macrosteps. In either case \(2n\) macrosteps restore the full state and the least original-step period is \(4n\). This also proves the absence of nonperiodic states by a direct return argument, independently of general reversibility.

**4. Orbit counting.** Fix a binary invariant word \(b\). The data consisting of the ant's column \(x\), horizontal sign \(h\), active row \(y\), and the complete first-row coloring \((c_{0,z})_z\) determine a unique vertical-heading state: use \(a_z=b_z\oplus\mathbf1_{\{z=x\}}\) to reconstruct the other-row coloring, and choose the unique incoming vertical heading that produces \(h\). Thus each projected \((x,h)\) state has exactly \(2^{n+1}\) lifts. Since every full ant orbit alternates vertical and horizontal-heading states, counting cycles of the vertical macro-map is exactly the same as counting cycles of the original one-step map.

For any fixed reflector gap of \(j\) edges, the associated projected component contains \(2j\) states and hence \(2j\,2^{n+1}\) vertical macro-states. Division by its exact \(4j\) macroperiod yields exactly \(2^n\) full cycles per gap. Choosing an ordered start zero, then \(j-1\) intermediate ones, a terminal zero and \(n-j-1\) free remaining bits gives \(n2^{n-j-1}\) pairs \((b,\text{gap})\). Therefore \(C_{8j}^{\mathrm{gap}}(n)=n2^{2n-j-1}\).

For a word \(b\) with one zero, all \(2n\) projected states belong to a single projected orbit, and the \(2n\,2^{n+1}\) lifted macro-states partition into \(2^{n+1}\) full cycles of macroperiod \(2n\). The all-one word has two projected orbits (the two constant travel directions), each of length \(n\), again giving in total \(2^{n+1}\) full cycles of macroperiod \(2n\). There are \(n\) one-zero patterns and one no-zero pattern, yielding \((n+1)2^{n+1}\) cycles of original period \(4n\).

The state checksum follows identically:
\[
\sum_{j=1}^{n-1}(8j)n2^{2n-j-1}+(4n)(n+1)2^{n+1}=8n2^{2n}.
\]
The probability contributions divide these period-weighted orbit counts by the total state count. Finally, summing their period-weighted probabilities and using the finite series for \(\sum_{j=1}^{n-1}j^2/2^j\) gives the displayed exact mean and limiting law.

## Verification

`verification/direct_census.cpp` implements the original turn-flip-move rule without using the reflector reduction. When compiled under C++17 it enumerates every full labelled state at each \(n=2,\ldots,9\), follows complete permutation cycles, compares their length multiplicities to the theorem and checks that total cycle-weighted population equals \(8n2^{2n}\). Its captured output is `verification/direct_census_output.txt`.

`verification/column_invariant.py` independently implements two one-step moves for each vertical-heading state at \(n=2,\ldots,7\) and checks the conserved column word, the predicted reflector sign at the next macro-update and sampled projected return lengths. Its captured output is `verification/column_invariant_output.txt`. These finite runs test the proof but do not replace its all-\(n\) combinatorial derivation.

## Relationship to prior work

The classical ant and its planar generalizations are discussed by Gale, Propp, Sutherland and Troubetzkoy (1995), whose accessible full text concerns bilateral symmetry and Truchet contours rather than all-state two-row torus cycle counts. The 2019 Mathematics Stack Exchange torus discussion explicitly notes reversibility, lists the recurrence of the **single all-white** \(2\times n\) starting configuration (period 16 for \(n\ge3\)), and states a conserved column-parity-plus-ant-marker quantity. Thus neither the reversibility nor that invariant is asserted as new; the present exact all-configuration reflector-gap partition, cycle multiplicities and limiting period law are the distinct additions. Hagiwara and Tsukiji study a different twisted-torus complexity problem. Gajardo and Goles (2004) investigate a family of one-dimensional ants on the infinite lattice; the accessible abstract does not establish the labelled \(2\times n\) torus census, but its full text could not be inspected and remains a priority risk.

## Limitations

The classification is for exactly two rows, periodic directions and the standard binary right/left turn-flip-move ant. It does not classify taller tori, boundary-reflecting strips, multi-color ants, or geometric orbit classes modulo spatial symmetries. Other formulations of narrow-strip ant dynamics could conceal a prior equivalent classification. The complete text of the related 2004 one-dimensional-ant paper was inaccessible; historical priority is qualified, not independently certified. All computational checks are finite; the proof of every size is the invariant and gap argument above. No independent mathematical audit has been performed.

## References

1. D. Gale, J. Propp, S. Sutherland, S. Troubetzkoy, *Further Travels with My Ant* (1995), arXiv:math/9501233, https://arxiv.org/html/math/9501233v1 (public v1: 1995-01-19).
2. *What is the period of Langton's ant on a torus?*, Mathematics Stack Exchange (2019), including Connor Harris and Derek Ledbetter's contributions, https://math.stackexchange.com/questions/3296855/what-is-the-period-of-langtons-ant-on-a-torus .
3. A. Gajardo, E. Goles, *Dynamics of a class of ants on a one-dimensional lattice*, Theoretical Computer Science 322 (2004), 267–283, https://doi.org/10.1016/j.tcs.2004.03.012 (abstract inspected; full text unavailable).
4. T. Hagiwara, T. Tsukiji, *Hardness of Approximation for Langton's Ant on a Twisted Torus*, Algorithms 13 (2020), 344, https://doi.org/10.3390/a13120344 .
5. A. Gajardo, A. Moreira, E. Goles, *Complexity of Langton's ant*, Discrete Applied Mathematics 117 (2002), 41–50, https://doi.org/10.1016/S0166-218X(00)00334-6 .
