# Parity-controlled vacancy condensation in antiferromagnetic spin-one wheel graphs

## Finding

Let \(W_{n+1}=K_1\vee C_n\) be a wheel with \(n\ge3\) rim vertices, and assign classical spins \(\sigma_v\in\{-1,0,1\}\). At zero magnetic field, take uniform antiferromagnetic coupling \(J>0\) and an arbitrary real single-ion crystal field \(D\):
\[
 H(\sigma)=J\sum_{uv\in E(W_{n+1})}\sigma_u\sigma_v+D\sum_{v\in V(W_{n+1})}\sigma_v^2,
 \qquad \delta=D/J.
\]
The **exact** dimensionless ground energy, including all coexistence parameters, is
\[
\frac{E_0}{J}=\begin{cases}
\min\{-n+(n+1)\delta,\,-n+n\delta,\,0\},&n\text{ even},\\[2pt]
\min\{-(n-1)+(n+1)\delta,\,-(n-2)+(n-1)\delta,\,0\},&n\text{ odd}.
\end{cases}
\]

The ground-state occupancy \(Q=\sum_v\sigma_v^2\) and number of distinct spin assignments are **completely classified**:

- **Even rim length \(n\ge4\):** for \(\delta<0\), \(Q=n+1\) (4 states); at \(\delta=0\), occupancies \(n+1,n\) (4 and 2 states; total 6); for \(0<\delta<1\), \(Q=n\) (2 states); at \(\delta=1\), occupancies \(n,0\) (2 and 1 states; total 3); for \(\delta>1\), \(Q=0\) (1 state).
- **Odd rim length \(n\ge5\):** put \(\delta_*(n)=(n-2)/(n-1)\). For \(\delta<1/2\), \(Q=n+1\) (\(2n\) states); at \(\delta=1/2\), occupancies \(n+1,n-1\) (\(2n\) and \(4n\) states; total \(6n\)); for \(1/2<\delta<\delta_*(n)\), \(Q=n-1\) (\(4n\) states); at \(\delta=\delta_*(n)\), occupancies \(n-1,0\) (\(4n\) and 1 states; total \(4n+1\)); for \(\delta>\delta_*(n)\), \(Q=0\) (1 state).
- **Exceptional triangle rim \(n=3\):** the two thresholds coalesce at \(\delta=1/2\). Strictly below it, \(Q=4\) (6 states); at it, occupancies \(4,2,0\) occur with multiplicities 6, 12, 1 (total 19); strictly above it, the all-zero assignment is unique.

Thus an odd rim supports a **positive-width intermediate two-vacancy ground-state phase** that does not exist for even rims. Its width is \((n-3)/(2(n-1))\), tending to \(1/2\) along odd rim lengths. This is a finite-wheel statement; the limiting width does not assert a bulk thermodynamic transition.

## Assumptions and scope

The graph has one hub adjacent to all vertices of a simple cycle, with one edge between each pair of consecutive rim vertices. All edges carry the same positive classical bilinear antiferromagnetic interaction. A spin may be \(-1\), \(0\), or \(+1\); the zero spin contributes no bilinear or crystal-field interaction. No magnetic field, disorder, anisotropic bonds, quantum effects, or thermal averaging enter the claim. Degeneracy counts distinguish labeled vertex-spin assignments, with no quotient by rotations or global spin reversal. The results cover every integer \(n\ge3\) and every real \(\delta\).

## Proof

Write the hub spin as \(t\in\{-1,0,1\}\) and the cyclically indexed rim spins as \(s_i\in\{-1,0,1\}\). Let \(r=\sum_i s_i^2\), \(q=r+t^2\), and let \(B\) denote the exchange energy divided by \(J\). A direct identity, with \(s_{n}=s_0\), is
\[
 B=\sum_i(s_i s_{i+1}+t s_i)
   =-r+\sum_i \phi_t(s_i,s_{i+1}),\qquad
 \phi_t(a,b)=\frac{(a+b)(a+b+t)}2.
\]
For all three allowed values of \(t\) and all allowed spins, \(\phi_t(a,b)\ge0\). If \(t=0\), it is \((a+b)^2/2\), and vanishes precisely when \(b=-a\). If \(t=\pm1\), it vanishes precisely when \(a+b\in\{0,-t\}\), and otherwise is a positive integer. Consequently \(B\ge-r\) always.

**Even rim.** When \(n\) is even, the full alternating rim has \(B=-n\) with any hub spin. For \(\delta<0\), the bound
\[
 B+\delta q\ge(\delta-1)r+\delta t^2\ge-n+(n+1)\delta
\]
is sharp only at a fully occupied alternating rim and a nonzero hub. For \(0<\delta<1\), the same inequality is bounded below by \(-n+n\delta\), attained only with an alternating full rim and zero hub. For \(\delta>1\), the exchange lower bound gives nonnegative energy, with equality only at the all-zero spin assignment. At \(\delta=0\) all six full-alternating-rim choices, with hub 0 or \(\pm1\), tie; at \(\delta=1\), just the two zero-hub alternating rims and the all-zero assignment tie. These facts prove both the even-rim energy envelope and its degeneracies.

**Odd rim, occupancy inequalities.** Assume \(n\) odd. For \(t=0\) and \(0<r<n\), the occupied rim vertices form one or more nonempty paths. Each occupied path contributes at least one to \(\sum_i\phi_0\) from the two occupied-vacant boundary edges. Therefore \(B\ge1-r\). For \(t=0,r=n\), an odd ring cannot alternate everywhere: at least one rim edge joins equal spins, costing two units of \(\phi_0\), so \(B\ge-n+2\).

For \(t=\pm1,r=n\), the same odd-cycle obstruction forces at least one positive integer \(\phi_t\), giving \(B\ge-n+1\). For \(t=\pm1,r=n-1\), there is one zero rim spin and an even-length path of occupied spins. Equality in \(B\ge-r\) would force the two ends of this path to be \(-t\) and every internal neighboring pair to have opposite signs; that is impossible for an even-length alternating path. Thus \(B\ge-r+1=-(n-2)\). Combining the cases, the complete bounds needed for every occupancy are
\[
\begin{array}{c|c}
q&\text{exchange-energy bound}\\\hline
0&B=0\\
1\le q\le n-1&B\ge 1-q\\
q=n&B\ge-(n-2)\\
q=n+1&B\ge-(n-1).
\end{array}
\]
The bound at \(q=n-1\) is attained both by a zero hub and one vacant rim vertex with alternating occupied path, and by a nonzero hub and two adjacent vacant rim vertices with an alternating odd occupied path. The bound at \(q=n+1\) is attained by a nonzero hub and a fully occupied rim with exactly one defective equal-spin edge of sign \(-t\).

For \(\delta\le1\), minimizing \(B+\delta q\) over \(1\le q\le n-1\) using the displayed bounds selects \(q=n-1\); the separate \(q=n\) bound is dominated by either \(q=n-1\) when \(\delta\ge0\), or the full \(q=n+1\) branch when \(\delta\le0\). For \(\delta\ge1\), no nonzero occupancy can beat energy zero. Hence the only potentially minimizing affine functions are those at \(q=n+1,n-1,0\), giving the claimed odd-rim envelope. Their crossings are \(\delta=1/2\) and \(\delta=(n-2)/(n-1)\), coincident precisely when \(n=3\).

**Odd-rim multiplicities.** The full-occupancy minimizers have a hub sign \(\pm1\) and a single adjacent \((-t,-t)\) defect on the rim, giving \(2n\) choices. Among the \(q=n-1\) minimizers, a zero hub and one rim vacancy give \(2n\) alternating-path choices. With a nonzero hub, equality in \(\phi_t\ge0\) and exactly two rim vacancies forces the vacancies to be adjacent: two separated occupied paths could both have boundary spins \(-t\) only if both path lengths were odd, but their total length \(n-2\) is odd. Adjacent vacancies leave one odd occupied path, uniquely alternating with endpoints \(-t\), giving another \(2n\) choices. Thus there are exactly \(4n\) minimizers of occupancy \(n-1\). The unique zero-occupancy state contributes one. Counting the tied branches yields the boundary counts above, including the triple coexistence for \(n=3\).

## Verification

The bundled standalone program `verify_exhaustive.py` independently enumerates every \(3^{n+1}\) spin assignment for each \(3\le n\le10\), evaluating energies exactly at representative rational crystal fields and at every claimed coexistence boundary. It compares the energy, occupied-site set, and multiplicity with the theorem. The separately implemented boundary-state contraction `verify_transfer.py` computes exact sector minima and counts for all occupancies at every \(3\le n\le70\), and independently checks the envelope and coexistence multiplicities. Both scripts use only the Python standard library and report `PASS` when run by `python verify_exhaustive.py` and `python verify_transfer.py` from their containing directory.

The finite computations corroborate the result but do **not** constitute an infinite-family proof. The proof is the local nonnegative-bond identity, the odd-path parity obstruction, the complete occupancy bounds, and the explicit equality classifications given above.

## Relationship to prior work

Pawłowski's open preprint studies the spin-one antiferromagnetic Blume–Capel model and antiferromagnetic/vacancy competition on the square lattice, using finite-temperature Wang–Landau sampling; it does not treat cone-over-cycle wheels or parity-dependent finite-cluster multiplicities. Guo and collaborators analyze an exactly solvable infinite sawtooth chain with a field, using its distinct periodic corner-sharing-triangle structure. Kimel and collaborators consider a two-dimensional square lattice; Hwang and collaborators study the kagomé lattice. Their cited statements do not imply the wheel-specific finite-size boundary \(\delta=(n-2)/(n-1)\) or the \(4n\) vacancy-sector multiplicity. The general possibility of transfer-matrix computation is not claimed as new; the explicit all-size wheel ground-state and degeneracy classification is the claimed contribution.

## Limitations

The result is at strictly zero magnetic field and zero temperature, on finite wheel graphs with exactly uniform couplings. It does not classify the full nonzero-field phase diagram, temperature-dependent thermodynamics, disordered wheels, or quantum spins. No proof of absolute publication priority is possible from the inspected sources; an unindexed treatment of wheel spin-one models could already contain an equivalent theorem. All counts are for labeled spins, not symmetry orbits.

## References

1. G. Pawłowski, *Multiphase structure of finite-temperature phase diagram of the Blume-Capel model: Wang-Landau sampling method*, arXiv:cond-mat/0703299, first posted 2007-03-12. https://arxiv.org/abs/cond-mat/0703299
2. Y.-P. Guo, Z.-Q. Liu, Y.-L. Xu and X.-M. Kong, *Exactly solvable antiferromagnetic Blume-Capel model on a sawtooth chain*, Physical Review E **93** (2016), 052151. https://doi.org/10.1103/PhysRevE.93.052151
3. J. D. Kimel, S. Black, P. Carter and Y.-L. Wang, *Monte Carlo study of the antiferromagnetic two-dimensional Blume-Capel model*, Physical Review B **35** (1987), 3347. https://doi.org/10.1103/PhysRevB.35.3347
4. C.-O. Hwang, S. Park and W. Kwak, *Study of the Antiferromagnetic Blume-Capel Model on kagome Lattice*, Journal of Physics: Conference Series **750** (2016), 012016. https://doi.org/10.1088/1742-6596/750/1/012016
