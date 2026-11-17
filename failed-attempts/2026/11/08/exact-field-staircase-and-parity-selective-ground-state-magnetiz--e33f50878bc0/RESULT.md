# Exact field staircase and parity-selective ground-state magnetization on triangular Ising graphs

## Finding

Let \(T_n=L(K_n)\) be the triangular graph, whose spin sites are the \(N=\binom n2\) edges of a complete graph on \(n\ge 3\) labeled vertices. For spins \(\sigma_e\in\{-1,+1\}\), coupling \(J>0\), and any real field \(h\), consider

\[
H_{n,J,h}(\sigma)=J\sum_{\substack{\{e,f\}\in E(T_n)}}\sigma_e\sigma_f-h\sum_{e\in E(K_n)}\sigma_e.
\]

For each integer \(m\in\{0,\ldots,N\}\), write \(2m=nq+r\), with \(0\le r<n\), and set \(d=2q-(n-1)\). The exact minimum **interaction** energy among states with precisely \(m\) positive spins is

\[
E_n(m)=\frac J2\left[(n-r)d^2+r(d+2)^2-n(n-1)\right].
\]

Every minimizer in that magnetization sector, and no other state, is obtained by selecting a simple graph of positive-spin edges whose vertex degrees are all \(q\) or \(q+1\), with exactly \(r\) vertices of degree \(q+1\). Such graphs exist for every \(m\).

Consequently the entire ground-state set in every field \(h\) consists of those balanced-degree configurations in sectors minimizing \(E_n(m)-h(2m-N)\). The distinct transition fields, including negative fields and zero when present, are **exactly** the following sets (fields at which at least two magnetization sectors are degenerate):

For even \(n\),
\[
\mathcal H_n=\{\,2J(2q-n+2):q=0,\ldots,n-2\,\}.
\]

For odd \(n\),
\[
\mathcal H_n=
\{\,2J(2q-n+2):q=0,\ldots,n-2\,\}
\ \cup\
\{\,2J(2q-n+3):q=0,2,\ldots,n-3\,\}.
\]

These sets have respectively \(n-1\) and \(3(n-1)/2\) distinct elements. They determine every plateau and degeneracy by the displayed explicit energy formula, without enumerating spin configurations.

At zero field, the possible total magnetizations \(M=\sum_e\sigma_e\) are exactly

\[
\begin{array}{c|c}
n\text{ even}&-n/2,-n/2+2,\ldots,n/2\\
n\equiv1\pmod4&0\\
n\equiv3\pmod4&-1,+1.
\end{array}
\]

For even \(n\), an arbitrarily small positive field selects \(M=n/2\) and an arbitrarily small negative field selects \(M=-n/2\), a finite-size magnetization discontinuity of size \(n\). At \(h=0\) there are \(n/2+1\) distinct magnetization sectors. For odd \(n\), the corresponding zero-field jump is zero when \(n\equiv1\pmod4\) and two when \(n\equiv3\pmod4\).

## Assumptions and scope

The graph \(T_n\) is the line graph of a simple complete graph, **not** a two-dimensional triangular lattice. The coupling is uniform antiferromagnetic \(J>0\); the field is uniform \(h\in\mathbb R\); no thermodynamic limit or quantum effects are assumed. Spins are classical and take values \(\pm1\). The magnetization is a total spin sum, not a density.

At a transition field, all minimizing magnetization sectors and their balanced-degree graph configurations are ground states. The formula identifies the states and energies exactly, but does not claim a closed binomial formula for the number of labeled near-regular graphs at every sector.

## Proof

**Interaction identity.** Interpret positive spins as edges of a spanning graph \(G\subseteq K_n\). Let \(k_v\) be its vertex degrees, so \(\sum_v k_v=2m\), and let \(D_v=\sum_{e\ni v}\sigma_e=2k_v-(n-1)\). Each adjacent pair of spin sites in \(T_n\) has exactly one common endpoint in \(K_n\). Therefore

\[
\sum_{\{e,f\}\in E(T_n)}\sigma_e\sigma_f
=\frac12\sum_{v=1}^n\left(D_v^2-(n-1)\right).
\]

The total magnetization is \(M=2m-N=\frac12\sum_vD_v\).

**Balancing and existence.** Fix \(m\). If vertices \(u,v\) have \(k_u\ge k_v+2\), some vertex \(w\notin\{u,v\}\) satisfies \(uw\in E(G)\) and \(vw\notin E(G)\). Otherwise the neighbor inclusion after deleting \(u,v\) would give \(k_u\le k_v+1\), a contradiction. Replacing \(uw\) by \(vw\) preserves \(m\), changes \((k_u,k_v)\) to \((k_u-1,k_v+1)\), and strictly reduces \(\sum_v k_v^2\), by \(2(k_u-k_v-1)>0\). Repeating this finite descent starting from any \(m\)-edge graph produces degrees differing by at most one. Conversely, strict convexity of squares shows that any nonbalanced degree sequence cannot be optimal. Thus all and only the optimal configurations at fixed \(m\) have \(n-r\) degrees \(q\) and \(r\) degrees \(q+1\). Substituting \(D_v=d,d+2\) yields \(E_n(m)\).

**Exact field transitions.** Let \(\Delta_m=E_n(m+1)-E_n(m)\), \(0\le m<N\). For even \(n\), the remainder \(r\) is even. During an increment with \(2m=nq+r\), including the rollover from \(r=n-2\) to \(q+1,r=0\), direct subtraction gives
\[
\Delta_m=4J(2q-n+2).
\]
Each \(q=0,\ldots,n-2\) occurs, and these values increase strictly with \(q\).

For odd \(n\), \(r\) has the parity of \(q\). Except at a rollover with even \(q\) and \(r=n-1\),
\[
\Delta_m=4J(2q-n+2).
\]
At that exceptional rollover the balanced degree multiset replaces one entry \(q\) by \(q+2\), giving
\[
\Delta_m=4J(2q-n+3).
\]
At a rollover with odd \(q\) the ordinary formula still holds. The resulting slope sequence is nondecreasing: the extra even-\(q\) value lies strictly between the adjacent ordinary values. The distinct slopes are precisely twice the fields in \(\mathcal H_n\). Since \(E_n(m)-h(2m-N)\) has successive differences \(\Delta_m-2h\), a field is critical exactly when \(2h\) is a slope. At other fields the minimizing sector is unique. At critical fields the sectors attaining the minimum are consecutive, and all balanced graph configurations in them minimize the Hamiltonian.

**Zero-field arithmetic.** If \(n\) is even, every \(D_v\) is odd, so the smallest possible \(\sum_v D_v^2\) is \(n\). It is achieved precisely when every \(D_v=\pm1\). The number \(r\) of \(+1\) values must be even because \(\sum_v k_v\) is even, and every even \(r\in[0,n]\) is realizable by the balancing argument. Then \(M=\frac12\sum_vD_v=r-n/2\), giving the stated complete progression.

If \(n\equiv1\pmod4\), the integer \((n-1)/2\) is even and a regular graph with those degrees exists by balancing at \(m=N/2\); all \(D_v=0\), so \(M=0\). If \(n\equiv3\pmod4\), a graph with all degrees \((n-1)/2\) would have an odd total degree and cannot exist. At the two nearest edge counts, balancing gives exactly one \(D_v=+2\) or one \(D_v=-2\), all others zero. Thus \(M=\pm1\), and these are the only zero-field ground sectors. The small-field selections follow from the slope classification.

In particular the zero-field minimum energies are \(-Jn(n-2)/2\) for even \(n\), \(-Jn(n-1)/2\) for \(n\equiv1\pmod4\), and \(-Jn(n-1)/2+2J\) for \(n\equiv3\pmod4\).

## Verification

Run `python3 verify_triangular_ising.py` with Python 3 (standard library only). The script independently enumerates all \(33{,}864\) spin configurations for \(n=3,4,5,6\), compares every fixed-magnetization minimum to the formula, tests the complete critical-slope identities and zero-field sectors for \(3\le n\le100\), and uses explicit edge switches to realize \(2{,}622\) balanced-degree graphs across all edge counts for \(3\le n\le25\).

All checks passed when the supplied script was executed. Finite computations corroborate the theorem but do not prove its universal quantifiers; the graph-switching argument, energy identity and exact difference calculation above provide the all-\(n\) proof.

## Relationship to prior work

Max-cut and antiferromagnetic ground-state formulations are classical. Arbib (1988) and Guruswami (1999) establish general polynomial-time solvability of certain cut problems on line graphs; their general algorithms and the zero-field maximum-cut viewpoint are not claimed as new here. **Caravelli and Markopoulou (arXiv:1008.1340, first posted 2010) study essentially the same complete-root line-graph Ising Hamiltonian** as an effective model of dynamical graphs: their Eqs. (30)–(31), with loop coupling set to zero and binary edge occupancy converted to spins, give the same class of couplings and uniform field up to constants and reparametrization. Their paper derives the mapping and analyzes finite-temperature and low-temperature *mean-field* valence behavior, rather than the exact finite-order ground-state sector and parity-resolved field-threshold classification stated here. The model and its dynamical-graph interpretation are theirs, not claimed as new.

Dyer, Heinrich, Jerrum and Müller (arXiv:2005.07944, publicly available 2020) prove general approximate counting and sampling results for antiferromagnetic Ising models on line graphs, including uniform external fields, and discuss hardness of exact finite-temperature counting. Their examined full arXiv text does not give these triangular-graph exact finite-size field thresholds or parity sectors. Metcalf and Yang (1978) investigate field-induced degeneracy in other antiferromagnets, specifically square and two-dimensional triangular lattices, not the triangular graph \(T_n=L(K_n)\).

The present claim is the explicit joint infinite-family zero-temperature phase classification, not the already-known Hamiltonian, its graphity interpretation, the general energy-to-cut identity, graph-switching move, or algorithmic line-graph tractability. An exact equivalent under graph cut profiles, balanced degree sequences, or further graphity work remains a historical-priority risk.

## Limitations

The theorem concerns \(T_n=L(K_n)\), not arbitrary line graphs, finite positive temperature, or long-time stochastic dynamics. The zero-field total-magnetization discontinuity is order \(n\), whereas \(T_n\) has order \(n^2\) spin sites, so this is **not** a claim of a nonzero thermodynamic magnetization-density jump. No experimental realization is asserted. Two particularly relevant older algorithmic papers were not available in full text during literature comparison; possible previously published equivalent closed formulas remain a priority uncertainty.

## References

- B. D. Metcalf and C. P. Yang, "Degeneracy of antiferromagnetic Ising lattices at critical magnetic field and zero temperature," *Physical Review B* **18** (1978), 2304, https://doi.org/10.1103/PhysRevB.18.2304 (published September 1, 1978).
- C. Arbib, "A polynomial characterization of some graph partitioning problems," *Information Processing Letters* (1988), https://doi.org/10.1016/0020-0190(88)90144-5.
- V. Guruswami, "Maximum Cut on Line and Total Graphs," *Discrete Applied Mathematics* **92** (1999), 217–221, https://doi.org/10.1016/S0166-218X(99)00056-6.
- F. Caravelli and F. Markopoulou, "Properties of Quantum Graphity at Low Temperature," *Physical Review D* **84** (2011), 024002, arXiv:1008.1340 (first posted August 7, 2010), https://arxiv.org/abs/1008.1340.
- M. Dyer, M. Heinrich, M. Jerrum, and H. Müller, "Polynomial-time approximation algorithms for the antiferromagnetic Ising model on line graphs," arXiv:2005.07944 (first posted May 16, 2020), https://arxiv.org/abs/2005.07944.
