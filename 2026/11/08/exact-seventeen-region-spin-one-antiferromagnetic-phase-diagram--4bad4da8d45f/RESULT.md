# Exact seventeen-region spin-one antiferromagnetic phase diagram on the truncated tetrahedron

## Finding

Consider the twelve-vertex truncated-tetrahedral graph \(G\), classical spins \(s_v\in\{-1,0,1\}\), uniform antiferromagnetic exchange \(J>0\), real magnetic field \(h\), and real single-ion crystal field \(D\). Set
\[
H(s)=J\sum_{\{u,v\}\in E(G)}s_us_v-h\sum_vs_v+D\sum_vs_v^2.
\]
For each spin configuration define its magnetization \(m=\sum_vs_v\), occupancy \(q=\sum_vs_v^2\), and dimensionless exchange energy \(e=\sum_{\{u,v\}\in E(G)}s_us_v\). Let \(x=h/J\) and \(d=D/J\).

**The exact ground-state energy for every \(x,d\in\mathbb R\) is**
\[
\frac{E_{\rm gs}}J=\min_{(m,q,e,g)\in\mathcal V}\{e-xm+dq\},
\]
where the following table defines \(\mathcal V\). A row with \(\pm m\) represents two separate entries, each with the displayed degeneracy \(g\).

| Magnetization \(m\) | Occupancy \(q\) | Minimum exchange \(e\) | Degeneracy \(g\) per entry |
|---:|---:|---:|---:|
| \(0\) | \(0\) | \(0\) | \(1\) |
| \(0\) | \(8\) | \(-8\) | \(6\) |
| \(0\) | \(12\) | \(-10\) | \(24\) |
| \(\pm2\) | \(10\) | \(-8\) | \(96\) |
| \(\pm4\) | \(4\) | \(0\) | \(30\) |
| \(\pm4\) | \(8\) | \(-4\) | \(24\) |
| \(\pm4\) | \(12\) | \(-6\) | \(30\) |
| \(\pm6\) | \(6\) | \(2\) | \(24\) |
| \(\pm8\) | \(8\) | \(6\) | \(30\) |
| \(\pm12\) | \(12\) | \(18\) | \(1\) |

All seventeen entries uniquely minimize the energy on a nonempty open set in the \((x,d)\)-plane; hence there are exactly seventeen open magnetization-occupancy ground-state regions. Every open region has the tabulated ground-state degeneracy. On boundaries, the degeneracy is the total number of minimizing spin configurations, including sectors that are not exposed on an open region; one must not merely add the listed \(g\)'s.

At the exact five-region intersection \((x,d)=(1,1)\), the ground-state energy is \(0\) and the total ground-state degeneracy is **1577**. At \((x,d)=(0,0)\), the energy is \(-10J\) and the degeneracy is \(24\). On the line \(d=0\) with \(x>0\), the open-interval magnetizations are \(0\) for \(0<x<1\), \(4\) for \(1<x<3\), and \(12\) for \(x>3\); the full two-parameter diagram thus reveals additional vacancy-driven regions that are invisible on that line.

## Assumptions and scope

The graph is represented without reliance on an external graph-data file. Its vertex set is \(V(G)=\{(i,j):i,j\in\{0,1,2,3\},\ i\ne j\}\). Two vertices are adjacent if their first indices agree, or if they are the reversed pair \((i,j),(j,i)\). There are four three-vertex cliques connected by six reversed-pair edges, giving twelve vertices, eighteen edges and degree three. This is the standard edge graph of the truncated tetrahedron. The labels are fixed and configurations are counted without identifying configurations under graph automorphisms or spin reversal.

All results are finite, at exactly zero temperature, with one uniform exchange constant and independent real field and crystal-field parameters. For the numbers in the table, \(q\) counts nonzero spins, so \(|m|\le q\le12\) and \(m\equiv q\pmod 2\). No thermodynamic-limit or quantum statement is made.

## Proof

1. **Complete finite state space.** Every labeled spin assignment is an element of \(\{-1,0,1\}^{12}\). There are exactly \(3^{12}=531441\) assignments. For every allowable pair \((m,q)\), let \(a_{m,q}\) be the least exchange energy and \(c_{m,q}\) the number of assignments attaining it. There are exactly \(91\) allowable pairs because for each \(0\le q\le12\), the possible magnetizations are \(-q,-q+2,\ldots,q\). The accompanying standalone program computes all \(91\) pairs by two distinct complete enumerations and compares their full microcanonical distributions, not merely the minima. The complete sector table is `certificates/sector_minima.csv`.

2. **Reduction to seventeen affine functions.** The seventeen entries \(\mathcal V\) coincide with the sector minima and multiplicities in the full enumeration. For each of the other \(74\) pairs \((m,q)\), `certificates/phase_polytope.json` supplies between one and three entries of \(\mathcal V\) and exact nonnegative rational weights \(\lambda_i\) satisfying
\[
\sum_i\lambda_i=1,\quad
\sum_i\lambda_i m_i=m,\quad
\sum_i\lambda_i q_i=q,\quad
\sum_i\lambda_i e_i\le a_{m,q}.
\]
Consequently, for every real \(x,d\),
\[
a_{m,q}-xm+dq\ge\sum_i\lambda_i(e_i-xm_i+dq_i)
\ge\min_{v\in\mathcal V}(e_v-xm_v+dq_v).
\]
Thus no omitted sector can lower the ground-state energy for any real field parameters. The provided verification script rechecks every rational identity using exact integer fractions.

3. **Exactly seventeen open regions.** For each entry \(v\in\mathcal V\), the same certificate contains rational parameters \((x_v,d_v)\) and a strictly positive rational gap separating its energy from the other ninety sector minima. Hence every listed entry is the unique minimizing sector on a nonempty open neighborhood. Conversely, the preceding domination result excludes any additional open-sector phase. Each unique-sector region is an intersection of strict affine half-planes and is therefore connected.

4. **Boundary counts.** Directly summing the complete microcanonical histogram over assignments with \(e-xm+dq\) equal to its minimum gives the stated degeneracies. At \((x,d)=(1,1)\), this sum is \(1577\); at the origin it is \(24\). The verifier performs both exact integer checks. No approximations or numerical searches over real parameter space enter the final proof.

## Verification

Run `python verify.py` with Python 3.9 or later, from any working directory. The program has no third-party dependencies and loads `certificates/phase_polytope.json` relative to its own path. Its independent enumerations are (a) recursion over twelve spins, accumulating every incident edge only after its second endpoint is assigned, and (b) a product of the twenty-seven states of each of four triangular blocks, with the six linking edges added afterward. Their entire exchange/magnetization/occupancy histograms must match, and both must sum to \(531441\).

The script also checks every one of the \(74\) rational domination certificates, all seventeen strict rational exposure witnesses, each tabulated multiplicity, and the special-field degeneracy. The deterministic canonical full-histogram digest is `35dea54d5dddbc058df29197a4e4b33c552866fb96af0c481299873533db577d` (SHA-256). Its exact checks cover all configurations of this finite graph; they do not assert mathematical priority over unindexed literature.

## Relationship to prior work

Coffey and Trugman, arXiv:cond-mat/9206011, investigate classical-vector and quantum spin-one-half Heisenberg antiferromagnetism on the *same* truncated-tetrahedral cluster, motivated as a small fullerene analogue. Their interaction has no vacancy state or independent Blume–Capel crystal field, and their spectral/correlation results do not imply the present two-field integer ground-state diagram. Fytas, arXiv:1011.4780, studies the Blume–Capel Hamiltonian on an *infinite triangular ferromagnetic lattice*, focusing on finite-temperature behavior rather than the present frustrated finite geometry. Krčmár, Gendiar and Nishino, arXiv:1512.09059, use “truncated tetrahedral model” for a different object: twelve possible local spin-vector directions on a square lattice, rather than twelve spatial sites with spin values \(-1,0,1\). These apparent naming and geometry coincidences do not yield the present classification.

Previous exact tables for three-color Potts spins on the same twelve-site graph and for spin-one Ising systems on different graph families concern different edge interactions or different adjacency matrices. A three-color Potts edge cost penalizes equal zero-color neighbors, whereas a Blume–Capel zero spin has vanishing exchange energy against every neighbor; their full field-dependent energy diagrams do not follow by renaming colors. These comparisons are evidence of a distinct mathematical statement, not proof of historical priority.

## Limitations

This is a finite combinatorial ground-state classification, not an infinite-system phase transition, prediction of a synthesized molecule, or quantum-spin theorem. Boundary degeneracies away from the two highlighted parameter choices are computable from the complete sector table and verifier but are not individually displayed as a long boundary catalogue. Published but unindexed evaluations, especially specialized magnetic-cluster tables, could contain equivalent or stronger results; no claim of absolute historical uniqueness is made.

## References

- D. Coffey and S. A. Trugman, *Correlations for the S=1/2 Antiferromagnet on a Truncated Tetrahedron*, arXiv:cond-mat/9206011v1 (first public version 1992-06-26), https://arxiv.org/abs/cond-mat/9206011.
- N. G. Fytas, *Wang-Landau study of the triangular Blume-Capel ferromagnet*, arXiv:1011.4780v1 (2010-11-22), https://arxiv.org/abs/1011.4780.
- R. Krčmár, A. Gendiar and T. Nishino, *Phase diagram of a truncated tetrahedral model*, arXiv:1512.09059v1 (2015-12-30), https://arxiv.org/abs/1512.09059.
