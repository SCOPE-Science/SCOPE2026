# Homogeneous directional rates uniquely maximize geodesic growth on the three-cube

## Finding

Consider Richardson growth on the three-dimensional Boolean cube, with a single initially infected corner and permanent infection. Each infected-to-uninfected edge parallel to either of the first two coordinate axes transmits at rate one; an edge parallel to the third axis transmits at rate \(t>0\). Equivalently, give the twelve undirected cube edges independent exponential first-passage weights with rates \((1,1,t)\) according to their coordinate directions. The earliest infection path from \(000\) to its antipode \(111\) is almost surely unique. Let \(L_t\) denote the number of edges on this path.

Write
\[
D(t)=8(t+1)^2(t+2)^3(t+4)^2(3t+2)^2,
\]
\[
\begin{aligned}
N_3(t)={}&54t^9+1035t^8+8229t^7+35054t^6+88714t^5\\
&+139614t^4+137585t^3+82162t^2+26912t+3616,\\
N_5(t)={}&18t^9+213t^8+890t^7+1851t^6+2428t^5\\
&+2814t^4+3334t^3+3076t^2+1728t+448,\\
N_7(t)={}&9t^6+21t^5+16t^4+4t^3+t^2+8t+16.
\end{aligned}
\]
Then the **entire length distribution** is
\[
\boxed{\Pr(L_t=3)=\frac{N_3(t)}{D(t)},\quad
\Pr(L_t=5)=\frac{N_5(t)}{D(t)},\quad
\Pr(L_t=7)=\frac{(t+2)N_7(t)}{D(t)}.}
\]
All three values have positive probability, and no other length is possible. The probability of a geodesic (three-edge) arrival path has its **unique global maximum over \(t>0\)** at \(t=1\), with
\[
\boxed{\max_{t>0}\Pr(L_t=3)=\frac{6973}{7200}.}
\]
At this isotropic point the other two probabilities are \(7/225\) and \(1/2400\). At the extreme anisotropies, \(\lim_{t\downarrow0}\Pr(L_t=3)=113/128\), whereas \(\lim_{t\to\infty}\Pr(L_t=3)=3/4\). Increasing \(t\) strictly decreases the antipodal first-passage time under the natural common-weight coupling, even though it decreases geodesic probability once \(t>1\).

## Assumptions and scope

The graph has vertex set \(\{0,1\}^3\) and edges differing in exactly one coordinate. The source is \((0,0,0)\), the target \((1,1,1)\), and the twelve edge passage times are independent exponentials with directional rates \(1,1,t\). There is no recovery, resetting, external arrival, or direction-dependent forward/backward asymmetry along an edge. Every statement applies to each real \(t>0\), not just integer or sampled parameters. All paths are simple because edge weights are strictly positive. In this dimension the possible odd simple-path lengths between antipodes are exactly \(3,5,7\). On the two-cube, all antipodal simple paths have length two, so dimension three is the first cube dimension admitting the detour phenomenon.

## Proof

For a partially infected configuration, assign to each infected vertex \(v\) its genealogical depth \(h(v)\), initially \(h(000)=0\), and give uninfected vertices the label \(-1\). Whenever a previously uninfected \(v\) is first infected from an infected neighbor \(u\), set \(h(v)=h(u)+1\). This parent pointer is the predecessor on the minimum-weight path from the source: for positive continuous edge weights, the Dijkstra exploration discovers each vertex via its uniquely cheapest incoming boundary edge. The memoryless property of exponential weights identifies this exploration with a continuous-time growth process in which each infected-to-uninfected boundary edge \((u,v)\) competes at its assigned rate \(r_{uv}\).

For any labeled state \(h\) before target arrival, let \(\partial h\) be the ordered edge set from infected to uninfected vertices, and let \(B(h)=\sum_{(u,v)\in\partial h}r_{uv}\). The conditional probability that the next infection follows \((u,v)\) is exactly \(r_{uv}/B(h)\). Define \(F_\ell(h)\) to be the probability of eventual target depth \(\ell\). For terminal states, \(F_\ell(h)={\bf1}_{\{h(111)=\ell\}}\); for all other states the first-step law is
\[
F_\ell(h)=\frac{1}{B(h)}\sum_{(u,v)\in\partial h}r_{uv}
 F_\ell(h^{u\to v}),\qquad \ell\in\{3,5,7\},
\]
where \(h^{u\to v}\) sets \(h(v)=h(u)+1\). Every recurrence increases the infected set, so this is a terminating exact finite induction, not a truncated approximation. There are 289 reachable labeled states when stopped upon target arrival. Expanding these rational recurrences and collecting over their common denominator gives exactly \(N_3/D\), \(N_5/D\), and \((t+2)N_7/D\), as checked by the standalone exact symbolic program. An independently constructed exhaustive enumeration of 7,368 elementary infection-parent histories gives the same fractions at six rational parameter values; the symbolic recurrence, not the numerical samples, certifies the identity for all positive \(t\).

Differentiation and exact polynomial reduction yield
\[
\frac{\mathrm d}{\mathrm dt}\Pr(L_t=3)
=-\frac{(t-1)R(t)}{8(t+1)^3(t+2)^4(t+4)^3(3t+2)^3},
\]
with
\[
\begin{aligned}
R(t)={}&297t^{10}+5724t^9+43542t^8+180178t^7+461900t^6\\
&+785388t^5+919752t^4+752864t^3+423552t^2\\
&+150528t+25600.
\end{aligned}
\]
Every coefficient in \(R\) is positive, so \(R(t)>0\) for \(t>0\). All denominator factors are positive as well. Thus the geodesic probability is strictly increasing on \((0,1)\), strictly decreasing on \((1,\infty)\), and uniquely maximized at \(t=1\). Direct substitution gives its claimed exact value. The remaining distribution, positivity, normalization, and limits follow directly from the displayed polynomials.

For the passage-time comparison, take independent unit-rate variables \(E_e\) for all edges. Give third-axis edges weights \(E_e/t\) and other edges weights \(E_e\). Every source-to-target path uses at least one third-axis edge; hence for \(t_2>t_1>0\), each path has strictly smaller cost at \(t_2\). Since a finite graph has finitely many simple paths, the minimum passage time is also strictly smaller for every realization with positive weights. This proves the claimed speed–directness tradeoff.

## Verification

Run `python verify_symbolic.py` with SymPy installed; it reconstructs the complete recurrence in symbolic \(t\), proves each rational identity by exact cancellation, verifies the derivative factorization, and recomputes geodesic probability from a different Boolean-state recursion. Its state counts are 289 full-depth states and 265 geodesic-flag states. Run `python verify_histories.py` using only the Python standard library; it independently enumerates all 7,368 edge-parent infection histories and checks the complete length distribution exactly at six distinct rational positive rates. Both programs completed successfully. No floating-point or simulation output is needed for the proof.

## Relationship to prior work

Fill and Pemantle, *Percolation, First-Passage Percolation, and Covering Times for Richardson's Model on the \(n\)-Cube* (first accessible arXiv posting 2004), formulate exponential passage times and high-dimensional oriented/unoriented first-passage questions. Martinsson, *Unoriented First-Passage Percolation on the \(n\)-Cube* (arXiv posted 2014), proves high-dimensional passage-time and asymptotic path-length results, and explicitly identifies the length of the minimizing route as a natural object. These established statements are compatible with the present calculation, but do not furnish an exact finite three-cube directional-rate law or a unique anisotropy optimizer. Published analyses of anisotropic bootstrap percolation concern threshold updates, not this weighted exponential arrival genealogy. The Markovian Richardson–first-passage equivalence is established prior work and is not claimed as new.

## Limitations

The exact rational optimization theorem concerns the smallest nontrivial cube \(Q_3\), with only one coordinate rate varying while the other two remain equal. It does not establish that full isotropy maximizes geodesicity among three arbitrarily varying axis rates, nor does it imply a corresponding optimization theorem in higher cube dimensions or for nonexponential passage times. The novelty comparison is limited to the inspected and indexed literature; an unindexed prior finite calculation or a stronger unpublished formula could subsume it. No external independent scientific audit has been performed.

## References

1. J. A. Fill and R. Pemantle, *Percolation, First-Passage Percolation, and Covering Times for Richardson's Model on the \(n\)-Cube*, Annals of Applied Probability 3 (1993), 593–629. Accessible preprint: https://arxiv.org/abs/math/0404015 (arXiv posting 2004-04-01).
2. A. Martinsson, *Unoriented First-Passage Percolation on the \(n\)-Cube*, Annals of Applied Probability 26 (2016), 2597–2625. https://arxiv.org/abs/1402.2928 (first arXiv posting 2014-02-12), https://doi.org/10.1214/15-AAP1155.
3. A. C. D. van Enter and A. Fey, *Metastability Thresholds for Anisotropic Bootstrap Percolation in Three Dimensions*, Journal of Statistical Physics 147 (2012), 97–112. https://doi.org/10.1007/s10955-012-0455-4. Distinct threshold-activation model.
