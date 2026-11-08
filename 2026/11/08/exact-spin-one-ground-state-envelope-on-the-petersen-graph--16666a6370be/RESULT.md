# Exact spin-one ground-state envelope on the Petersen graph

## Finding

Let \(P=GP(5,2)\) be the ten-vertex Petersen graph, and let every vertex carry a classical variable \(\sigma_v\in\{-1,0,+1\}\). For uniform antiferromagnetic coupling \(J>0\), arbitrary real crystal field \(D\), and arbitrary real longitudinal magnetic field \(h\), define
\[
H(\sigma)=J\sum_{uv\in E(P)}\sigma_u\sigma_v+D\sum_{v\in V(P)}\sigma_v^2-h\sum_{v\in V(P)}\sigma_v.
\]
Put \(\delta=D/J\) and \(b=|h|/J\). For **every** \((D,h)\in\mathbb R^2\), the exact minimum is
\[
\boxed{\frac{E_0(D,h)}J=\min\bigl\{-9+10\delta-2b,\ -6+6\delta,\ -3+4\delta-2b,\ 0,\ 4\delta-4b,\ 3+6\delta-6b,\ 15+10\delta-10b\bigr\}.}
\]
Each of the seven displayed branches uniquely minimizes on a nonempty open set in the half-plane \(h>0\). Consequently the full \((D,h)\)-plane has twelve open ground-state chambers (two field-reflected copies for each of the five branches with strictly positive magnetization, and one connected chamber each for the two zero-magnetization branches). In the order of the seven branches above, the strictly exposed sector data \((K,M,\Omega)\)—occupied sites, total magnetization when \(h>0\), and labeled-spin degeneracy—are

| \(E/J\) branch | \(K\) | \(M\) | \(\Omega\) |
|---|---:|---:|---:|
| \(-9+10\delta-2b\) | 10 | 2 | 5 |
| \(-6+6\delta\) | 6 | 0 | 20 |
| \(-3+4\delta-2b\) | 4 | 2 | 10 |
| \(0\) | 0 | 0 | 1 |
| \(4\delta-4b\) | 4 | 4 | 5 |
| \(3+6\delta-6b\) | 6 | 6 | 5 |
| \(15+10\delta-10b\) | 10 | 10 | 1 |

At zero field an exact two-step vacancy/magnetization cascade occurs:
\[
\frac{E_0(D,0)}J=\min\{-9+10\delta,-6+6\delta,0\}.
\]
For \(\delta<3/4\), the ground states have \(K=10\), \(M=\pm2\) and total degeneracy \(10\); for \(3/4<\delta<1\), they have \(K=6\), \(M=0\) and degeneracy \(20\); for \(\delta>1\), only the all-vacant state remains. At \(\delta=3/4\) the degeneracy is \(30\), and at \(\delta=1\) it is \(21\). Thus introducing vacancies first eliminates the nonzero ground magnetization and only subsequently empties the graph.

## Assumptions and scope

Label the outer vertices \(u_i\) and inner vertices \(v_i\), where \(i\in\mathbb Z/5\mathbb Z\). The fifteen undirected edges are exactly \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), five of each. There are no other edges or boundary terms. All spins are classical, all three values are allowed independently, the coupling is uniform and positive, and the temperature is strictly zero. Occupancy is \(K=\sum_v\sigma_v^2\), magnetization is \(M=\sum_v\sigma_v\), and exchange energy is the integer \(e=\sum_{uv}\sigma_u\sigma_v\). Degeneracies count all labeled spin configurations, not configurations modulo graph automorphisms. Negative \(h\) follows by reversing every spin.

## Proof

**1. Finite exact sector classification.** There are exactly \(3^{10}=59049\) spin configurations. Direct integer enumeration gives \(318\) occupied exchange-energy/occupancy/magnetization triples \((e,K,M)\). The spin-flip symmetry \((e,K,M)\mapsto(e,K,-M)\) reduces the energy minimization for \(b\ge0\) to the \(36\) sectors with \(M\ge0\), indexed by \((K,M)\). For each such sector, the minimum integer exchange energy \(e_{K,M}\) and the number of attaining configurations are the entries of `certificate.json` under `sector_bounds`. `enumerate_direct.py` checks every one of those entries against all \(59049\) configurations; `enumerate_shell.py` reconstructs the same sector counts by independently contracting the outer pentagon, inner step-two pentagon, and five spokes.

**2. Exact global dominance certificates.** Let the seven triples \((e_i,K_i,M_i)\) be the rows of `certificate.json` under `active`, in the displayed branch order. For each of the \(36\) sector minima \((e,K,M)\), `sector_bounds` supplies seven nonnegative rational numbers \(\lambda_i\) satisfying
\[
\sum_i\lambda_i=1,\quad \sum_i\lambda_iK_i=K,\quad \sum_i\lambda_iM_i\ge M,\quad \sum_i\lambda_ie_i\le e.
\]
It follows for every real \(\delta\) and \(b\ge0\) that
\[
e+\delta K-bM\ge\sum_i\lambda_i(e_i+\delta K_i-bM_i)\ge\min_i(e_i+\delta K_i-bM_i).
\]
Configurations above their own sector minimum cannot improve it, so no omitted spin state can lower the seven-branch envelope. Both inequalities and all \(36\) lists of rational coefficients are checked **exactly** using `fractions.Fraction`; no floating-point tolerances enter this proof certificate.

**3. Exposure and phase completeness.** The positive-field rational pairs \((\delta,b)\) listed under `witnesses` in `certificate.json` make each corresponding branch strictly smaller than the other six branches. Thus all seven sectors occur in genuine open regions. All seven affine functions are distinct, and a convex-dominance equality for a nonlisted sector is possible on an open region only if its energy, occupancy and magnetization coincide with an active sector, in which case its multiplicity is already included in that sector's enumeration. Spin reversal duplicates exactly the five positive-magnetization chambers for \(h<0\); the two zero-magnetization chambers extend across \(h=0\). This gives twelve open chambers on the whole parameter plane, apart from phase-coexistence curves.

**4. Zero-field coexistence.** Substitute \(b=0\) in the seven-branch formula and compare the affine functions. The lower envelope simplifies to the three terms claimed above, crossing at exactly \(\delta=3/4\) and \(\delta=1\). Exact enumeration of every spin state at those rational parameters gives the degeneracies \(30\) and \(21\). Specifically, the first crossing comprises \(20\) configurations with \((K,M,e)=(6,0,-6)\) and five each with \((10,+2,-9)\) or \((10,-2,-9)\); the second comprises the \(20\) six-spin configurations and the single empty configuration.

## Verification

Run from one directory with a Python 3 interpreter and no third-party libraries:

```text
python3 enumerate_direct.py
python3 enumerate_shell.py
```

The scripts consume the **bundled** `certificate.json`, check the complete integer sector counts and both rational coexistences, and verify all sector-dominance coefficients and seven strict-exposure witnesses. The first script reconstructs energies from fifteen explicit edges; the second constructs exchange energies from two independently enumerated pentagons and their matching spokes. Both completed successfully on the enclosed files. The rational certificate is fully supplied and independently checked by standard-library arithmetic; no certificate-generation dependency is required.

## Relationship to prior work

The antiferromagnetic Blume–Capel model and competing occupancy/ordering effects are established subjects; Kimel, Rikvold, and Wang (1992) analyze a square-lattice thermodynamic phase diagram, **not** this ten-site graph. Yang, Yang, Dai, and Xiang (2007) explicitly describe the neutral spin state as a hole in a spin-one **quantum chain**, and derive chain-sector decompositions; their chain result does not provide these Petersen-graph ground energies. Zaslavsky (2012) studies signed Petersen graphs and their frustration indices, which overlap the **fully occupied zero-field Ising subproblem** but do not evaluate the two-parameter spin-one vacancy/magnetization envelope. In particular, a pre-existing spin-\(1/2\), zero-field Petersen maximum-cut result can recover the full-occupancy exchange energy, not the six other branches, phase exposures, or vacancy coexistence counts. A result on the line graph of the Petersen graph concerns a fifteen-vertex **different** spin network and does not imply this ten-vertex classification. The result is an exact finite frustrated-cluster benchmark, not a new general theorem about all cubic graphs.

## Limitations

The result applies only to the specific ten-site graph, uniform nearest-neighbor antiferromagnetic bilinear exchange, uniform fields, and exactly zero temperature. It neither determines excitation gaps nor any positive-temperature or thermodynamic-limit transition. The proof uses exhaustive *finite* enumeration plus exact rational polyhedral certificates and does not establish an infinite-graph statement. The literature comparison cannot exclude equivalent results in unindexed publications, especially older treatments of graph-frustration indices or finite spin-one clusters. The main conclusion concerns exact energy, labeled ground-state multiplicities on open chambers, and the two stated zero-field coexistence points; multiplicities at other boundary intersections are not tabulated here, although they are computable from the supplied full sector table.

## References

1. J. D. Kimel, P. A. Rikvold, and Y.-L. Wang, “Phase diagram for the antiferromagnetic Blume-Capel model near tricriticality,” *Physical Review B* **45**, 7237 (1992), https://doi.org/10.1103/PhysRevB.45.7237 (publisher public date 1992-04-01).
2. Z. Yang, L. Yang, J. Dai, and T. Xiang, “Rigorous Solution of the Spin-1 Quantum Ising Model with Single-ion Anisotropy,” https://arxiv.org/abs/0709.0337 (first arXiv posting 2007-09-04).
3. T. Zaslavsky, “Six signed Petersen graphs, and their automorphisms,” *Discrete Mathematics* **312**, 1558–1583 (2012), https://doi.org/10.1016/j.disc.2011.12.010 (related frustration-index results, not a spin-one field classification).
