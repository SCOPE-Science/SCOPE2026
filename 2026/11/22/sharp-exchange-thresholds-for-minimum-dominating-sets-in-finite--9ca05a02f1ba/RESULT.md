# Sharp exchange thresholds for minimum dominating sets in finite affine planes

## Finding
For any finite affine plane \(\mathcal A\) of order \(q\ge2\), let \(G(\mathcal A)\) be its point–line incidence graph. For each line \(B\), set
\[
S_B=\{\text{the }q\text{ points of }B\}\cup\{\ell:\ell\parallel B,\ \ell\ne B\}.
\]
The family \(\{S_B:B\text{ a line}\}\) is precisely the family of minimum dominating sets; it has \(q(q+1)\) members, each of size \(2q-1\). The size formula and the super-neatness of affine-plane domination were already established by Tang and Zhou (2016); we give a direct self-contained classification to make the exchange result independent of that publication.

Define \(R_t(G)\) on all minimum dominating sets, joining distinct \(S,T\) when \(|S\setminus T|=|T\setminus S|\le t\). Its exact graph is
\[
R_t(G)\cong\begin{cases}
\overline{K}_{q(q+1)}&t<\min(q+1,2q-2),\\
K_{2,2,2}&q=2,\ t=2,\\
K_6&q=2,\ t\ge3,\\
K_{12}&q=3,\ t\ge4,\\
(q+1)K_q&q\ge4,\ q+1\le t<2q-2,\\
K_{q(q+1)}&q\ge4,\ t\ge2q-2.
\end{cases}
\]
In particular the exact connectivity budget is always \(2q-2\), and for orders at least four there is a nonempty interval of budgets on which movement within parallel classes is possible but movement between different parallel classes is impossible. For order four the intermediate interval has just one integer; its length grows unboundedly with the order.

## Assumptions and scope
A finite affine plane of order \(q\) is an incidence structure with \(q^2\) points, \(q(q+1)\) lines of \(q\) points each, unique joining line for any distinct points, and \(q+1\) parallel classes of \(q\) disjoint lines each. Only existing finite affine planes are quantified over; no assumption of Desarguesian coordinates or prime-power order is used. Graph domination is by closed neighborhoods. The graphs \(R_t\) use *at most* \(t\) simultaneous vertex replacements, with all intermediate states constrained to be minimum dominating sets. The result does not concern addition/deletion reconfiguration or nonminimum dominating sets.

## Proof
Let \(S\) be a dominating set; let \(a\) be its selected point-vertices, \(b\) its selected line-vertices. To dominate all line-vertices, each point can cover at most \(q+1\) lines and each selected line covers itself, so \(a(q+1)+b\ge q(q+1)\). To dominate all point-vertices, \(a+qb\ge q^2\). For any \(|S|\le 2q-1\), substituting \(b\le2q-1-a\) gives \(qa\ge q^2-q+1\), hence \(a\ge q\); the other inequality gives \((q-1)a\le q^2-q\), hence \(a\le q\). Thus \(a=q\) and \(b=q-1\), and no dominating set of smaller cardinality exists.

The \(q\) selected points collectively meet at most \(q^2+1\) distinct lines: the first meets \(q+1\) lines, and each following point meets at most \(q\) previously uncounted lines because it shares a joining line with the first. These points must meet at least \(q(q+1)-(q-1)=q^2+1\) lines, since the \(q-1\) selected line-vertices must comprise the remaining unhit lines. Hence equality holds. For \(q\ge3\), if the selected points were not collinear, some third point would be outside the line through the first two, and then it shares two *distinct* already-counted joining lines with these first two points. This would give at most \(q-1\) new lines from the third point and break equality. Thus all points are collinear. For \(q=2\), any two points are collinear. The selected points are therefore exactly the full point set of some line \(B\). The only lines avoiding all of these points are the \(q-1\) other members of the parallel class of \(B\), so those and only those must be selected. Conversely such a set covers every line-vertex (either by a selected point or itself) and every point-vertex (either it lies on \(B\) or lies on a selected parallel mate). This gives the complete set classification.

If distinct \(B,C\) are parallel, their point subsets are disjoint and their selected line subsets overlap in exactly \(q-2\) members. Hence \(|S_B\cap S_C|=q-2\), yielding exchange cost \((2q-1)-(q-2)=q+1\). If they are nonparallel, their point subsets meet in one point and their line subsets are drawn from distinct parallel classes, so \(|S_B\cap S_C|=1\), yielding cost \(2q-2\). Compare these two numbers for each order: at order two the cross-class cost is two and within-class cost is three; at order three both are four; from order four onward the within-class cost is smaller, and parallel classes give exactly \(q+1\) clique components until the cross-class threshold. These comparisons prove the displayed graph and sharp connectivity budget.

## Verification
Two standalone implementations supplied with this result independently construct affine incidence graphs over fields of orders \(2,3,4\). A Python checker enumerates all candidates of the forced point/line cardinalities and verifies the geometrically predicted family and every pairwise exchange cost. A separate C++17 checker exhaustively enumerates every vertex subset of cardinality at most \(2q-1\), checks dominating status directly from closed-neighborhood bitmasks, and independently checks all optimum sets and pairwise distances. Exact outputs are in CHECKS.txt; commands are `python3 verify_affine.py` and `g++ -O2 -std=c++17 verify_affine.cpp -o verify_affine && ./verify_affine`. These computations corroborate but are not used in place of the all-order proof.

## Relationship to prior work
Goldberg, Rajendraprasad and Mathew (2014) initiated domination in design incidence graphs and established a projective-plane domination value. Tang and Zhou (2016, arXiv:1603.07398, Theorems 4.2–4.3) **already proved** \(\gamma(G)=2q-1\) for affine planes and that all their minimum dominating sets are super-neat; these known statements are not claimed as new. Héger and Nagy (2016) concern small dominating sets in **projective**, not affine, incidence graphs. Tang, Zhou and Chen (2019) also state affine-plane super-neatness, as shown by their abstract. The contribution assessed here is the sharp *minimum-solution batch-exchange graph and connectivity phase transition* over the full affine-plane family. Nearby published results on projective-plane geodetic/connected-domination exchanges and affine-plane total/paired domination concern distinct optimization constraints and do not, as stated, give this minimum ordinary-domination reconfiguration graph.

## Limitations
The result concerns only fixed-size minimum-set batch replacement and uses an elementary consequence of the already-known minimum domination geometry. It does not imply new domination-number bounds. A complete full-text priority comparison with the 2019 Tang–Zhou–Chen paper was unavailable, though its published abstract concerns domination numbers and super-neatness, not reconfiguration; an unindexed earlier treatment of the same exchange graph remains possible. No independent mathematical validation has been performed. Computations cover orders two through four only; the unrestricted-order statement depends on the symbolic proof.

## References
1. F. Goldberg, D. Rajendraprasad, R. Mathew, *Domination in designs*, arXiv:1405.3436 (first submitted 2014-05-14), https://arxiv.org/abs/1405.3436.
2. L. Tang, S. Zhou, *Domination number in block designs*, arXiv:1603.07398 (first submitted 2016-03-24), https://arxiv.org/abs/1603.07398, Theorems 4.2–4.3.
3. T. Héger, Z. L. Nagy, *Dominating sets in projective planes*, arXiv:1603.02933 (first submitted 2016-03-09), https://arxiv.org/abs/1603.02933.
4. L. Tang, S. Zhou, J. Chen, *Domination number of incidence graphs of block designs*, Appl. Math. Comput. 363 (2019), article 124600, https://doi.org/10.1016/j.amc.2019.124600 (abstract inspected only).
