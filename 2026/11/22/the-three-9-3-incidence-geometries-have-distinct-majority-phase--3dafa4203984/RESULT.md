# Majority basins on the two non-Pappus nine-point incidence configurations

## Finding

Consider synchronous strict binary majority on the eighteen-vertex Levi graphs of the two non-Pappus combinatorial \((9_3)\) configurations. The graphs on points that join noncollinear pairs have cycle patterns \((9)\) and \((3,6)\), respectively. The following table gives their exact recurrent and transient data. The earlier Pappus spectrum [1] is included as a comparison, not claimed as new.

| Point noncollinearity cycles | Recurrent point-side symbols \(S\) | Fixed states | Primitive temporal two-cycle orbits | Sharp maximum first periodic-entry time | Fourth-step point-side fiber histogram \(\{t:m_t\}\) |
|---|---:|---:|---:|---:|---|
| \((9)\) | 98 | 98 | 4753 | 4 | \(\{1:18,2:18,3:36,4:24,127:2\}\) |
| \((3,6)\) | 96 | 96 | 4560 | 4 | \(\{1:16,2:30,3:12,4:36,128:2\}\) |
| \((3,3,3)\), Pappus [1] | 92 | 92 | 4186 | 3 | \(\{2:54,4:36,130:2\}\) |

Here \(m_t\) counts recurrent point-side symbols with exactly \(t\) preimages under the point component of the fourth iterate. The complete basin multiset follows: each such symbol of weight \(t\) gives one fixed-point basin of size \(t^2\), and each unordered pair of distinct symbols of weights \(t,u\) gives a two-cycle basin of size \(2tu\). Thus the two non-Pappus spectra are distinct from one another. Compared with the earlier Pappus result, each has singleton fixed-point basins and neither settles universally in three updates.

The entry-layer counts are for labelled starting states, not for basins or periodic orbits. The Pappus entries are the sums of the two eventual-period columns of the first-entry table in [1].

| Point noncollinearity cycles | Time 0 | Time 1 | Time 2 | Time 3 | Time 4 |
|---|---:|---:|---:|---:|---:|
| \((9)\) | 9604 | 57996 | 81396 | 95040 | 18108 |
| \((3,6)\) | 9216 | 64768 | 70416 | 105600 | 12144 |
| \((3,3,3)\), Pappus [1] | 8464 | 79152 | 47808 | 126720 | 0 |

In each row all temporal periods are one or two; the number of recurrent full configurations is \(S^2\).

## Assumptions and scope

A configuration here has nine points, nine distinct lines, exactly three incidences per point and per line, and at most one common line per point pair. A state assigns a bit independently to every point and line vertex. In one synchronous update every vertex takes the majority of its three neighbors' bits. The first periodic-entry time is the earliest update count at which the state belongs to its eventual orbit; a two-cycle is one orbit of two states. Basins contain all labelled starting states eventually reaching that orbit. The result does not address other incidence sizes, different thresholds, asynchronous updates, or quotients by spatial symmetry.

Representatives on points \(0,\ldots,8\) have line lists in the order shown:

- \((9)\): \((012),(034),(056),(137),(168),(246),(278),(358),(457)\).
- \((3,6)\): \((012),(034),(056),(148),(167),(237),(268),(358),(457)\).
- \((3,3,3)\), Pappus: \((012),(034),(056),(138),(157),(247),(268),(367),(458)\).

For example, \((012)\) is the line joining points \(0,1,2\). The count of three combinatorial isomorphism classes already appears in [2, Table 1]; the finite classification check below identifies exactly which representative has each point noncollinearity pattern.

## Proof and verification

**Representative check.** A point meets six other points on its three lines without repetition, so the noncollinearity graph is 2-regular. After labelling one point zero, permute the remaining labels so that the lines through it are \((012),(034),(056)\). All configurations now appear among completions by six triples from points 1–8, using no pair twice and filling all remaining point degrees (two at 1–6 and three at 7–8). The finite search in `verify_93.py` enumerates all such increasing lists of triples and finds 176 completions, of patterns \((9),(3,6),(3,3,3)\) in counts 96, 72, and 8. It checks that for every completion a permutation of equal-length cycles and a rotation or reflection of each cycle transport the line-triple set to the corresponding displayed representative. These operations enumerate all possible isomorphisms of the fixed-pattern noncollinearity graphs. The distinct patterns preclude incidence isomorphism between representatives. To recognize the last representative as Pappus directly, take the two base triples \((4,5,8)\) and \((6,3,7)\) in the indicated orders; the three usual pairs of cross-lines meet at 0, 2, and 1, respectively, which lie on \((0,1,2)\).

**Factorization through two shores.** Let \(A\) send the nine point bits to the nine line majorities, and let \(B\) send line bits to point majorities. Then
\[
F(x,y)=(B(y),A(x)),\qquad F^2(x,y)=(H(x),K(y)),\qquad H=B\circ A,\quad K=A\circ B.
\]
The finite calculation on all 512 point-side and all 512 line-side inputs checks \(H^3=H^2\) and \(K^3=K^2\) for each representative. Hence \(F^6=F^4\) on every state. On \(X=\operatorname{im}H^2\) and \(Y=\operatorname{im}K^2\) the maps \(A,B\) are mutually inverse: \(BA=H\) is the identity on \(X\), \(AB=K\) is the identity on \(Y\), and \(K A=A H\) and \(H B=B K\) give the image inclusions. Thus \(F\) acts as the swap on \(X^2\) after coding the second shore by \(B\). This gives exactly \(S=|X|\) fixed states and \(\binom S2\) primitive two-cycle orbits. The computed sizes for the non-Pappus types are 98 and 96.

**Basins.** Let \(\alpha_x=|(H^2)^{-1}(x)|\) and \(\beta_y=|(K^2)^{-1}(y)|\). The same complete tables check the pointwise identity \(\alpha_x=\beta_{A(x)}\) for each \(x\in X\), not just equality of their histograms. As \(F^4=(H^2,K^2)\), its fibers have product sizes. A fixed state at symbol \(x\) consequently has an entire basin of size \(\alpha_x^2\); the two swapped states corresponding to distinct \(x,z\) have disjoint fibers with total size \(2\alpha_x\alpha_z\). The displayed histograms come from enumerating the \(\alpha_x\). Each gives \(\sum_x\alpha_x=512\), so the basin total is \(512^2\).

**First-entry census.** At update \(r\) a state is periodic exactly when its images at \(r\) and \(r+2\) agree, by the proven period bound. In the \((9)\) and \((3,6)\) types, with bit position \(i\) labelling vertex \(i\) on each shore, input masks \((46,0)\) give the time-three states \((0,8)\) and \((0,32)\), respectively, while both time-five states equal \((0,0)\). This proves sharpness at four in both cases. The independently formulated full-state procedure in `check_full_states.cpp` takes all \(2^{18}\) states on each graph, evaluates their successors, peels off vertices of indegree zero, and traverses the surviving cycles. Propagating distances and orbit labels backwards through the peel order gives the full first-entry counts and basin spectrum. This procedure also reproduces the comparison row for Pappus.

To reproduce both procedures, run `python3 verify_93.py` and separately compile `check_full_states.cpp` with `g++ -O2 -std=c++17 check_full_states.cpp -o check_full_states` and run the executable. The Python script checks isomorphism coverage, both shore retractions, sharp witnesses and their fiber data; the C++ checker asserts the orbit counts and maximum depths, and prints the complete first-entry and basin histograms for comparison. No inference for other graphs is made from these finite calculations.

## Relationship to other work

The Pappus orbit counts, sharp transient, fourth-step fiber profile, individual basin multiset and entry census in [1] concern the same cubic bipartite Levi graph. This is not a different dynamical system under dual labelling: either shore assignment gives the same underlying graph and synchronous majority rule. The combinatorial class count is also known [2], and an eventual period bound of two is general for parallel majority in the relevant undirected setting [3]. The contribution here is the exact majority census on the two non-Pappus types and the resulting comparison across the known classes; the class count and the Pappus baseline receive no originality claim. The exact enumerations establish these finite facts but not bibliographic priority.

## References

1. *Pappus majority dynamics: 92 recurrent symbols and a sharp three-update transient*, Resultary, 2026-11-17, Finding and basin computation, [record](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-pappus-majority-dynamics-92-recurrent-symbols-and-a-sharp-three--b7ac6ea9e0f4).
2. J. Bokowski and V. Pilaud, *Enumerating topological \((n_k)\)-configurations*, Table 1, [arXiv:1210.0306](https://arxiv.org/abs/1210.0306).
3. E. M. Adam, M. A. Dahleh, and A. E. Ozdaglar, *On Threshold Models over Finite Networks*, §4.3, [arXiv:1211.0654](https://arxiv.org/abs/1211.0654).
