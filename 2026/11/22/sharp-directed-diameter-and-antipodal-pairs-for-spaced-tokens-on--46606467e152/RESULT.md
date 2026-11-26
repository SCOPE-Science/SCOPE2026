# Directed diameter and ordered antipodes for spaced tokens on a cycle

## Finding

Fix integers \(r,k\ge2\) and \(n>rk\). A state is a \(k\)-subset of \(\mathbb Z/n\mathbb Z\) with every clockwise gap between consecutive occupied vertices at least \(r\). A directed move advances one token by one clockwise site and must preserve the gap constraint. In this strongly connected digraph, the directed diameter is
\[
 D=k\bigl(n-1-r(k-1)\bigr).
\]
The ordered pairs at distance \(D\) are exactly the \(n\) simultaneous rotations of
\[
 X_0=\{0,r,\ldots,(k-1)r\},\qquad
 Y_0=\{n-1-r(k-1),\ldots,n-1-r,n-1\}.
\]
Thus exactly \(n\) sources attain the maximum outgoing eccentricity, each with a unique farthest target. The extremal statement uses a clockwise transport distance that follows from the earlier bounded-gap sliding lemma and conservation, as explained below.

## Assumptions and scope

The sites have fixed labels \(0,\ldots,n-1\), and only the arcs \(v\to v+1\pmod n\) may be used, not arbitrary arcs in a power of the cycle. Tokens are indistinguishable; a configuration is a set. All cyclic gaps, including the wraparound gap, must be at least \(r\). Distance counts slides, not waiting or rates. In the separate boundary case \(n=rk\), every gap equals \(r\) and all \(r\) possible cyclic phases are isolated; no finite all-pairs distance or diameter formula is asserted there.

## Proof

**Transport formula used in the proof.** For states \(X,Y\) on a cycle with \(n>rk\), define
\[
 p_j=\sum_{v=0}^j (\mathbf 1_X(v)-\mathbf 1_Y(v)),\qquad 0\le j<n.
\]
The counts \(f_j\) of slide uses of arc \(j\to j+1\) along any route satisfy \(f_j-f_{j-1}=\mathbf 1_X(j)-\mathbf 1_Y(j)\) by conservation. Hence \(f_j=p_j+c\) and \(c\ge-\min p\) by nonnegativity. This bounds the route length below by \(\sum_j(p_j-\min p)\).

Cut the cycle after a minimizing site. The prefixes in the new order are nonnegative, so the sorted positions \(x_i\) of \(X\) and \(y_i\) of \(Y\) satisfy \(x_i\le y_i\) for each \(1\le i\le k\). Indeed, the prefix ending at \(y_i\) contains at least \(i\) source sites. The feasible gap family is exactly the bounded-gap family of [1] with lower bound \(a=r\) and upper bound \(b=n-r(k-1)\): the upper bound follows by summing the other \(k-1\) lower bounds. With \(s=n-rk>0\), we have \(ak<n<bk\), since \(bk-n=(k-1)s>0\). The one-unit descent lemma in [1, proof Step 3], applied from the periodic lift \(y\) down to \(x\), gives a feasible coordinatewise decrement path. Reversing it yields a clockwise route from \(x\) to \(y\). The positions stay in the cut interval because each coordinate is between its two endpoints. No slide crosses the cut, so the route has the normalized flow \(f_j=p_j-\min p\) and proves both connectivity and
\[
 d_{\to}(X,Y)=\sum_j(p_j-\min p)=\sum_{i=1}^k(y_i-x_i).
\]
Equivalently, the clockwise path can be seen directly in this case: in an intermediate state, a token still below its target can be blocked only by the next token at gap exactly \(r\). Feasibility of the targets then forces that next token also to be below its target (using the periodic lift at the wrap). If all unfinished tokens were blocked, all gaps would be exactly \(r\), contrary to positive slack. Successive unblocked advances therefore reach the target without crossing the cut.

**Diameter and equality.** In the cut coordinates, feasibility gives \(x_i\ge r(i-1)\) and \(y_i\le n-1-r(k-i)\). Every summand of the transport distance is therefore at most \(n-1-r(k-1)\). If the sum is \(D\), every summand must attain that bound, which forces \(x_i=r(i-1)\) and \(y_i=n-1-r(k-i)\) for every \(i\). Conversely, the displayed \(X_0,Y_0\) are feasible, each with one gap \(n-r(k-1)>r\) and all others equal to \(r\). Across the cut after \(n-1\), their paired positions satisfy \(x_i\le y_i\) and all prefixes are nonnegative (every target in a prefix has its matched source in the prefix). The prefix at \(n-1\) is zero, so this is a minimizing cut. Hence the distance is exactly \(D\). The unique gap larger than \(r\) fixes its endpoints in any rotation that fixes the source, so the \(n\) rotations are distinct with distinct sources. The equality classification gives each such source exactly one farthest target, and all other sources have strictly smaller outgoing eccentricity.

**Auxiliary counts.** For \(s=n-rk>0\), distinguishing a token gives its position and a weak composition of \(s\) into the \(k\) successive excess gaps. There are \(k\) such choices per state, so the number of vertices is \((n/k)\binom{s+k-1}{k-1}\). An outgoing arc is specified instead by the moving token and excess gaps with at least one unit in the gap ahead of it. Removing that unit gives \(n\binom{s+k-2}{k-1}\) directed arcs. These counts are not needed for the equality classification.

## Verification

The algebraic proof gives the diameter and equality conditions for all \(n>rk\). In the companion source files, `verify.py` uses direct feasible-set enumeration, generates legal clockwise moves, and compares BFS distances against the transport formula. It also checks the vertex count, diameter, and number of ordered pairs at the diameter. The supplied `verification_output.txt` records 73 positive-slack cases and 1,896,844 ordered-pair comparisons on the bounded grid implemented in the checker. Run `python3 verify.py` where the companion checker is stored to reproduce those tests. They do not check the frozen boundary or prove the general result.

## Relationship to prior work

The clockwise distance and connectivity are consequences of the comparable-lift descent lemma in [1] plus the minimum-prefix cut and flow calculation above. Although [1] states its transport theorem for **undirected** moves, its descent lemma supplies the needed monotone path for the comparable lifts after the cut. Its frozen lower-bound case also applies here. The extremal result is the exact maximum of the resulting **directed** distance and the classification of its ordered equality pairs; the bounded-gap lemma itself neither computes that maximum nor selects these pairs.

Directed token-sliding work gives reachability algorithms for oriented cycles [2] and shortest sequences on polytrees [3]. The case \(r=2\) is directed independent-set sliding along the clockwise cycle; for larger \(r\), single-step arcs are still those of the base cycle. The same dynamics can also be viewed as one-site hops of nonoverlapping rods of length \(r\) on a periodic lattice. The exclusion diameters in [4] concern symmetric moves or a lifted model with an additional active-particle pointer, not the directed diameter of the unaugmented rod configurations. The accessible abstract of [5] focuses on steady-state currents, densities and phases for extended particles; its full geometric scope was not determined. These comparisons do not settle historical priority outside the inspected material.

## Limitations

This is a finite labelled-cycle result with a uniform minimum gap and a single global direction. It does not imply mixing-time bounds or a diametral classification for bidirectional, lifted, inhomogeneous, or nonperiodic dynamics.

## References

1. *Circular bounded-gap token systems have transport-optimal sliding distances*, 8 November 2026, proof Step 3, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-circular-bounded-gap-token-systems-have-transport-optimal-slidin--edbf2b8cafb9/RESULT.md.
2. N. Banerjee, C. Engels and D. A. Hoang, *Directed Token Sliding*, §4.1, https://arxiv.org/abs/2411.16149.
3. T. Ito, Y. Iwamasa, Y. Kobayashi, Y. Nakahata, Y. Otachi, M. Takahashi and K. Wasa, *Independent set reconfiguration on directed graphs*, https://arxiv.org/abs/2203.13435.
4. X. Zhang and W. Krauth, *Diameters of Symmetric and Lifted Simple Exclusion Models*, https://doi.org/10.1007/s10955-024-03312-w.
5. G. Lakatos and T. Chou, *Totally asymmetric exclusion processes with particles of arbitrary size*, https://doi.org/10.1088/0305-4470/36/8/302; abstract at https://www.osti.gov/etdeweb/biblio/20365177.
