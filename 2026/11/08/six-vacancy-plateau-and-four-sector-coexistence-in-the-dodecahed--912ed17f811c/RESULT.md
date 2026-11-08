# Six-vacancy plateau and four-sector coexistence in the dodecahedral spin-one antiferromagnet

## Finding

Let \(G\) be the dodecahedral graph, and put a classical spin \(s_v\in\{-1,0,1\}\) at each of its twenty vertices. For every \(J>0\) and real crystal-field strength \(D\), the zero-field Blume–Capel Hamiltonian is
\[
H(s)=J\sum_{uv\in E(G)}s_us_v+D\sum_{v\in V(G)}s_v^2.
\]
Writing \(d=D/J\), its exact ground-state energy is
\[
\boxed{E_0/J=\min\{-18+20d,\,-15+14d,\,0\}.}
\]
There are precisely two crystal-field crossings, at \(d=1/2\) and \(d=15/14\). The complete zero-temperature occupancy and labeled-configuration degeneracy diagram is:

| Crystal field | Active-spin count \(Q=\sum s_v^2\) | Ground-state count |
| --- | --- | ---: |
| \(d<1/2\) | \(20\) | 250 |
| \(d=1/2\) | \(14,16,18,20\) | 40, 390, 600, 250 respectively; total 1280 |
| \(1/2<d<15/14\) | \(14\) | 40 |
| \(d=15/14\) | \(0,14\) | 1 and 40 respectively; total 41 |
| \(d>15/14\) | \(0\) | 1 |

Thus the open intermediate regime has exactly six nonmagnetic vacancies, not a gradually changing occupancy. Each of its forty ground states has total magnetization \(\sum s_v=0\). In the fully occupied regime, the 250 zero-field configurations split into magnetizations \(-4,0,4\) with multiplicities \(5,240,5\). The 250 fully occupied states are previously known; the asserted contribution is the crystal-field classification and the vacancy/coexistence counts.

## Assumptions and scope

The graph is the standard dodecahedral graph, equivalently the generalized Petersen graph \(GP(10,2)\), with vertices \(a_i,b_i\) indexed modulo ten, and edges \(a_i a_{i+1}\), \(a_i b_i\), and \(b_i b_{i+2}\). It has 20 vertices, 30 edges, and twelve pentagonal faces. The model is **classical and discrete**; it is not a quantum spin-one Heisenberg Hamiltonian. The magnetic field is exactly zero. Labels on the twenty sites are fixed for degeneracy counts; geometric isomorphism classes are not being counted. All real \(D\), all \(J>0\), and all \(3^{20}\) configurations are included. The term phase or plateau refers only to the finite zero-temperature energy envelope, not a thermodynamic singularity.

## Proof

For an integer \(q\) between zero and twenty, define
\[
e(q)=\min_{s:\,\sum s_v^2=q}\ \sum_{uv\in E(G)}s_us_v,\qquad
g(q)=\#\{s:\sum s_v^2=q,\ \sum s_us_v=e(q)\}.
\]
The exhaustive **exact** sector-minimum calculation is recorded in `sector_minima.csv`. Its entries for \(q=0,1,\ldots,20\), in ascending order, are
\[
(e(q))_{q=0}^{20}=(0,0,-1,-2,-3,-4,-5,-6,-7,-8,-10,-11,-12,-13,-15,-15,-16,-16,-17,-17,-18).
\]
The corresponding exact multiplicities are in the accompanying CSV. Every entry is obtained by finite variable elimination, as follows.

Attach a three-state factor to each vertex assigning occupancy degree \(s_v^2\) and zero interaction energy; attach a factor to each edge assigning degree zero and interaction cost \(s_us_v\). Values of a factor are tables indexed by the boundary spins, with a finite array indexed by accumulated occupancy \(q\). A table entry stores the **minimum** accumulated integer interaction energy and the **number of assignments attaining that minimum**. Multiplication of factors convolves occupancy indices, adds costs and multiplies counts; summation over an eliminated spin selects the minimum cost at each occupancy, adding counts on ties. This is exact by the elementary distributive law for minimization over independent internal choices. Starting with these vertex and edge factors, eliminate vertices in the order encoded in `verify_dp.py`; the largest intermediate scope has seven spin variables. No approximation, cutoff, or statistical sample is made. The final empty-boundary factor lists all \((e(q),g(q))\). The complete algorithm is in `verify_dp.py` and can be executed with the Python standard library.

The sector values obey the two rational lower bounds
\[
e(q)\ge-\frac{15q}{14}\quad(0\le q\le14),\qquad
e(q)\ge-8-\frac q2\quad(14\le q\le20).
\]
The first bound is tight only at \(q=0,14\). The second is tight precisely at \(q=14,16,18,20\), with \(q=14,20\) as endpoints. Consequently the lower convex envelope of \((q,e(q))\) has vertices \((0,0),(14,-15),(20,-18)\); the intermediate points \((16,-16),(18,-17)\) lie on its final edge. Minimizing \(e(q)+dq\) proves the boxed energy formula for all real \(d\), and identifies all sectors participating at the two boundaries. Summing their \(g(q)\) values gives 1280 and 41. The magnetization-resolved assertions follow from `sector_magnetization.csv`.

## Verification

`verify_dp.py` independently evaluates all sector minima and counts by exact factor elimination; `verify_gray.cpp` enumerates all \(3^{20}=3,486,784,401\) assignments with a reflected-ternary Gray code, updates the energy locally, and records minima and counts in each occupancy/magnetization sector. The latter uses 64-bit integer counters. With Python 3 and a C++17 compiler, from the directory containing the files, run:

```bash
python3 verify_dp.py > dp.out
cmp sector_minima.csv dp.out
g++ -O3 -std=c++17 verify_gray.cpp -o gray_check
./gray_check > mag.out
cmp sector_magnetization.csv mag.out
```

The C++ program also checks that the enumeration visits exactly \(3^{20}\) states. Summing its counts over minimizing magnetizations agrees with all 21 outputs of the independent factor-elimination method. The 250 full-occupancy result agrees with the published Ising baseline. The two boundary degeneracies follow by integer addition from the data; no floating-point comparisons are involved in the proof.

## Relationship to prior work

The dodecahedral fullerene's frustration and magnetic response motivate this finite cluster: Konstantinidis studies quantum Heisenberg spins on this geometry, while Lopez-Bezanilla and collaborators study binary Ising quantum dynamics and explicitly report the 250 all-antiferromagnetic classical ground states. Neither model contains the adjustable classical vacancy state \(s_v=0\) with \(D\sum s_v^2\); their stated results therefore do not determine the sector values for \(q<20\), the six-vacancy plateau, or coexistence counts. Earlier antiferromagnetic Blume–Capel studies investigate extended two-dimensional lattices, not the twenty-site dodecahedral graph. The present classification concerns the **specific interaction-energy–occupancy envelope** rather than a general formula for all spin-one systems.

## Limitations

This is a fully finite, zero-temperature, zero-magnetic-field result. It makes no claim about positive-temperature critical phenomena, the full two-parameter \((D,h)\) diagram, the quantum spin-one Heisenberg model, or experimental measurement on a particular molecule. The 250 fully occupied configurations and the fact that the dodecahedron is frustrated were known. Historical coverage by unindexed exact tables remains possible; literature priority is not mathematically certified.

## References

1. N. P. Konstantinidis, *The Antiferromagnetic Heisenberg Model on Clusters with Icosahedral Symmetry*, arXiv:cond-mat/0503658, first submitted 29 March 2005. https://arxiv.org/abs/cond-mat/0503658
2. A. Lopez-Bezanilla et al., *Quantum dynamics in frustrated Ising fullerenes*, arXiv:2505.08994, first submitted 13 May 2025. https://arxiv.org/abs/2505.08994
3. J. D. Kimel, S. Black, P. Carter and Y.-L. Wang, *Monte Carlo study of the antiferromagnetic two-dimensional Blume–Capel model*, Physical Review B 35, 3347 (1987). https://doi.org/10.1103/PhysRevB.35.3347
4. M. Blume, *Theory of the First-Order Magnetic Phase Change in UO2*, Physical Review 141, 517 (1966). https://doi.org/10.1103/PhysRev.141.517
