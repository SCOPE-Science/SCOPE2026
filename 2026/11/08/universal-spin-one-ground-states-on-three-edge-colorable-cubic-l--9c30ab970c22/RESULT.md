# Universal spin-one ground states on three-edge-colorable cubic line graphs

## Finding

Let \(G\) be any finite simple cubic graph with a proper three-edge-coloring, and let \(n=|V(G)|\). Put classical spin-one variables \(\sigma_e\in\{-1,0,1\}\) at the vertices of its line graph \(L(G)\), one for each edge of \(G\). For uniform antiferromagnetic coupling \(J>0\), crystal field \(D\in\mathbb R\), and magnetic field \(h\in\mathbb R\), use
\[
H(\sigma)=J\sum_{\{e,f\}\in E(L(G))}\sigma_e\sigma_f+D\sum_{e\in E(G)}\sigma_e^2-h\sum_{e\in E(G)}\sigma_e.
\]
Writing \(\delta=D/J\) and \(b=|h|/J\), the **exact ground-state energy for every pair of fields** is
\[
\boxed{\frac{E_0(D,h)}J=n\min\!\left\{0,\frac{\delta-b}{2},-1+\delta,1+\delta-b,-1+\frac{3\delta-b}{2},3+\frac{3(\delta-b)}2\right\}.}
\]
There are six nonempty, strictly dominant local-composition regimes for \(b>0\). The table specifies their exact global occupation \(Q=\sum_e\sigma_e^2\), favored-direction magnetization \(|M|=|\sum_e\sigma_e|\), and ground-state count, away from ties among the six affine energies. Here \(p(G)\) is the number of perfect matchings and \(c_3(G)\) is the number of proper three-edge-colorings using three *labeled* colors.

| Local triangle spins (for \(h>0\)) | \(Q\) | \(M\) | Degeneracy |
|---|---:|---:|---:|
| \((0,0,0)\) | \(0\) | \(0\) | \(1\) |
| \((0,0,+1)\) | \(n/2\) | \(n/2\) | \(p(G)\) |
| \((-1,0,+1)\) | \(n\) | \(0\) | \(c_3(G)\) |
| \((0,+1,+1)\) | \(n\) | \(n\) | \(p(G)\) |
| \((-1,+1,+1)\) | \(3n/2\) | \(n/2\) | \(p(G)\) |
| \((+1,+1,+1)\) | \(3n/2\) | \(3n/2\) | \(1\) |

On the **zero-field vacancy coexistence line** \(h=0\), \(D=J\), the exact degeneracy is the even-cycle packing sum
\[
\boxed{\Omega_{\mathrm{vac}}(G)=\sum_{F\in\mathcal E(G)}2^{c(F)},}
\]
where \(\mathcal E(G)\) is the set of edge subsets that form disjoint unions of vertex-disjoint *even* cycles, including the empty set, and \(c(F)\) counts those cycles. On the distinct **field-saturation coexistence ray** \(h=4J\), \(D<0\), the degeneracy is the total matching count
\[
\boxed{\Omega_{\mathrm{sat}}(G)=\sum_{k=0}^{n/2}m_k(G),}
\]
where \(m_k(G)\) is the number of \(k\)-edge matchings (including \(m_0(G)=1\)). The same count holds with negative field by global spin reversal.

For the cuboctahedron \(L(Q_3)\), these two coexistence counts are respectively \(69\) and \(108\); its six strict-field phase degeneracies in the displayed order are \(1,9,24,9,9,1\).

## Assumptions and scope

The graph \(G\) is finite, simple, cubic, and three-edge-colorable; it need not be bipartite, planar or connected. Every exchange edge in \(L(G)\) has the same positive bilinear coupling \(J\). The crystal-field coefficient \(D\) and the longitudinal field \(h\) are real and uniform. The model is classical and at zero temperature. “Six regimes” refers to the six possible uniquely minimizing local compositions in the positive-field half-plane \(h>0\). At ties additional configurations may appear, and the open-regime multiplicities are not asserted there. At \(h<0\), reverse all nonzero spins; the energy expression depends only on \(|h|\).

## Proof

**Triangle decomposition and sharp lower bound.** Each vertex \(v\) of the cubic base \(G\) has exactly three incident edges \(e_1,e_2,e_3\), forming a triangle of interaction edges in \(L(G)\). Every interaction edge occurs in exactly one such triangle; every spin lies in exactly two. Thus the normalized Hamiltonian is the sum over \(v\in V(G)\) of
\[
\Phi_{\delta,b}(s_1,s_2,s_3)=\sum_{1\le i<j\le3}s_i s_j+\frac\delta2\sum_{i=1}^3s_i^2-\frac b2\sum_{i=1}^3s_i,
\]
after globally reversing spins if \(h<0\). The ten unordered triples of three-state spins reduce to six contenders when \(b\ge0\): a triple with negative total magnetization is dominated by its spin reversal (with equality possible at \(b=0\)). The six remaining triples, their pair energies, occupation numbers and magnetizations are:

| Triple | Pair energy | Local \(Q\) | Local \(M\) | \(\Phi_{\delta,b}\) |
|---|---:|---:|---:|---|
| \((0,0,0)\) | \(0\) | \(0\) | \(0\) | \(0\) |
| \((0,0,+1)\) | \(0\) | \(1\) | \(1\) | \((\delta-b)/2\) |
| \((-1,0,+1)\) | \(-1\) | \(2\) | \(0\) | \(-1+\delta\) |
| \((0,+1,+1)\) | \(1\) | \(2\) | \(2\) | \(1+\delta-b\) |
| \((-1,+1,+1)\) | \(-1\) | \(3\) | \(1\) | \(-1+(3\delta-b)/2\) |
| \((+1,+1,+1)\) | \(3\) | \(3\) | \(3\) | \(3+3(\delta-b)/2\) |

This yields the displayed lower bound with prefactor \(n\). Fix a proper labeled three-edge-coloring of \(G\), assign to its color classes the three spins in any minimizing triple, and observe that every base vertex sees exactly that triple. Therefore all local minima are attained simultaneously and the lower bound is an equality at **every** \((\delta,b)\). Six exact rational strict-dominance witnesses (respectively in the table order) are \((\delta,b)=(2,1/4),(3/2,5/2),(1/2,1/4),(1,4),(-1,1),(-1,8)\). This proves all six regimes are nonempty, not merely candidate lines.

**Open-regime multiplicities.** When one composition strictly minimizes the six local functions, a global ground state must realize that composition at *every* base vertex. In each of the three compositions containing exactly one distinguished spin and two identical spins, the edges bearing the distinguished spin form a perfect matching, and the remaining spins are forced. For the composition \((-1,0,+1)\), the edge labels themselves form a proper *labeled* three-edge-coloring. The all-zero and all-positive compositions determine unique states. Counting these gives precisely the open-regime multiplicities above. Global reversal handles negative field.

**Vacancy coexistence.** At \((\delta,b)=(1,0)\), inspection of the exact local table shows that the only minimizing triples are \((0,0,0)\) and \((-1,0,+1)\). The occupied edges of \(G\) therefore have at every base vertex degree either zero or two, and at degree-two vertices the two signs must be opposite. Consequently the occupied edges are disjoint even cycles, each with exactly two alternating sign assignments. Conversely every such weighted even-cycle union attains all local minima. This proves \(\Omega_{\mathrm{vac}}(G)\).

**Saturation coexistence.** At \(b=4\) and \(\delta<0\), the only minimizing local triples are \((+1,+1,+1)\) and \((-1,+1,+1)\). The negative-spin edges can therefore contain no adjacent pair: they form an arbitrary matching. Every matching, including the empty one, yields one state by making all other spins positive. This proves \(\Omega_{\mathrm{sat}}(G)\).

## Verification

All verification code uses the Python standard library and is embedded with this result. Run `python verification/exhaustive_cube.py`, `python verification/combinatorial_cube.py` and `python verification/other_cubic_graphs.py` from the package root. The first script evaluates all \(3^{12}=531441\) cuboctahedral configurations and confirms the six exact rational witnesses and two coexistence counts. The second independently enumerates all cube matching sets, proper edge-colorings, and even-cycle unions without spin energies. The third exhaustively checks the smaller nonbipartite base \(K_4\) (\(3^6=729\) spin states) and bipartite base \(K_{3,3}\) (\(3^9=19683\) states). The proof of the all-graph result is the sharp local decomposition, not extrapolation from these finite checks.

For \(Q_3\), the matching polynomial is \(1+12t+42t^2+44t^3+9t^4\); at \(t=1\), it gives \(108\). The even-cycle packing weights, grouped by number of occupied base edges \(0,4,6,8\), are respectively \(1,12,32,24\), summing to \(69\). The cube has \(9\) perfect matchings and \(24\) labeled proper three-edge-colorings. Additional checks on \(K_4\) give boundary counts \(7,10\), while \(K_{3,3}\) gives \(31,34\), in vacancy/saturation order.

## Relationship to prior work

Barry and Muttalib (2002) study an exactly mapped kagomé spin-one model with **triquadratic triangle** interactions, not the present bilinear exchange; their finite-temperature mapping does not imply the six-line formula. Xu and Moore (2007) explicitly identify the classical \((-1,0,+1)\) constraint for \(0<D<J\) and zero field in the kagomé spin-one XXZ model, so that particular regime is **known**. Their magnetic-field treatment is restricted to weak fields and does not furnish this exact full two-control result. Hwang, Park and Kwak (2016) identify the zero-temperature kagomé Blume–Capel critical field \(h/J=4\) at the parameter choice they examine; this threshold is **known**, but their paper explicitly reserves simultaneous nonzero anisotropy and magnetic field for future investigation. Rousochatzakis, Läuchli and Mila (2007) motivate the physical relevance of the cuboctahedron through a Heisenberg kagomé-like cluster, with a different Hamiltonian. An earlier three-state Potts line-graph calculation also uses three-edge-colorability and gives a distinct four-branch field envelope and different weighted matching count; that model's equality indicators cannot be substituted for the present bilinear spin interactions. The claimed contribution is the **joint** universal six-branch classical Blume–Capel envelope with graph-invariant open-phase counts and the two exact coexistence enumerators, not the already-known special-phase facts.

## Limitations

The result gives zero-temperature finite-graph ground energies and degeneracies, **not** positive-temperature transition curves, mixing rates, quantum entanglement or thermodynamic-limit critical exponents. The formulas are not asserted for cubic graphs without a proper three-edge-coloring or for nonuniform couplings. Complete degeneracy formulas at all other tie curves are not supplied. Literature comparison is extensive but cannot exclude every unindexed or unpublished equivalent treatment; independent scientific audit has not been performed.

## References

1. J. H. Barry and K. A. Muttalib, *S=1 kagomé Ising model with triquadratic interactions, single-ion anisotropy and magnetic field: exact phase diagrams*, arXiv:cond-mat/0204632, initially posted 2002-04-30. https://arxiv.org/abs/cond-mat/0204632
2. C. Xu and J. E. Moore, *Global phase diagram of the spin-1 antiferromagnet with uniaxial anisotropy on the kagome lattice*, arXiv:cond-mat/0701635, initially posted 2007-01-25. https://arxiv.org/abs/cond-mat/0701635
3. I. Rousochatzakis, A. M. Läuchli and F. Mila, *Highly frustrated magnetic clusters: The kagomé on a sphere*, arXiv:0711.3231, initially posted 2007-11-20. https://arxiv.org/abs/0711.3231
4. C.-O. Hwang, S. Park and W. Kwak, *Study of the Antiferromagnetic Blume-Capel Model on kagomé Lattice*, J. Phys.: Conf. Ser. 750 (2016) 012016, DOI:10.1088/1742-6596/750/1/012016. https://scholar.gist.ac.kr/handle/local/14085
