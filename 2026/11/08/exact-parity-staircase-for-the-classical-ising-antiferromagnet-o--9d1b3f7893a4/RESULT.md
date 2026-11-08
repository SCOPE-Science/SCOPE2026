# Exact parity staircase for the classical Ising antiferromagnet on truncated simplices

## Finding
For each integer \(n\geq3\), let \(G_n\) have vertices \((i,j)\), where \(1\leq i,j\leq n\) and \(i\ne j\). Join \((i,j)\) to \((i,k)\) for distinct \(j,k\ne i\), and join each \((i,j)\) to \((j,i)\). Thus \(G_n\) is the clique truncation of \(K_n\), with \(n(n-1)\) spins and \(n(n-1)^2/2\) edges. In particular \(G_4\) is the truncated tetrahedral graph.

For the uniform antiferromagnetic Ising Hamiltonian
\[
\mathcal H_h(\sigma)=J\sum_{uv\in E(G_n)}\sigma_u\sigma_v-h\sum_{v\in V(G_n)}\sigma_v,\qquad J>0,\quad h\geq0,\quad \sigma_v\in\{-1,+1\},
\]
put \(x=h/J\), \(M=\sum_v\sigma_v\), and \(N=n(n-1)\). The exact ground-state energy for every \(x\geq0\) is
\[
\frac{E_0(x)}J=\min\left\{n\left[\frac{k^2}{2}+(1-x)k-(n-1)\right]:\ 0\le k\le n-1,\ k\equiv n-1\pmod2\right\}
\]
when \(n\) is odd; when \(n\) is even, the minimum additionally includes \(n/2-n(n-1)\).

At any noncritical positive field the ground-state magnetization is **unique**, as follows.

* For odd \(n\), its critical fields are precisely \(x=2,4,\ldots,n-1\). On the interval \(k<x<k+2\), with \(k\in\{0,2,\ldots,n-3\}\), one has \(M=nk\); for \(x>n-1\), \(M=N\). In particular \(M=0\) for \(0<x<2\).
* For even \(n\), its critical fields are precisely \(x=1,3,\ldots,n-1\). One has \(M=0\) for \(0\le x<1\). On \(k<x<k+2\), \(k\in\{1,3,\ldots,n-3\}\), one has \(M=nk\); for \(x>n-1\), \(M=N\). The first jump at \(x=1\) is from \(0\) to \(n\), whereas for odd \(n\) it is from \(0\) to \(2n\) at \(x=2\).

There are no additional transition fields. At each critical field \(x=t>0\), the full set of ground states consists exactly of the configurations described by the equality conditions below: no reversed-pair edge has two down spins, and every row spin sum belongs to \(\{t-2,t\}\). For even \(n\) at \(t=1\) this means row sums \(-1\) or \(1\); at higher critical fields it gives the analogous adjacent parity-compatible values. At \(x=0\) the even-\(n\) ground states have zero magnetization, row sums \(\pm1\), and no doubly-down reversal pair; the odd-\(n\) ground states have zero row sums and no doubly-down reversal pair.

## Assumptions and scope
All graph edges have identical antiferromagnetic coupling \(J\). This is a **classical longitudinal-field** model, not a quantum transverse-field or Heisenberg Hamiltonian. Vertices of the graph are ordered pairs and the only edges are clique-within-row edges and reversal edges. Fields are nonnegative; negative fields follow by global spin flip. Statements hold for all integers \(n\ge3\) and exactly at all real \(x=h/J\ge0\). Ground-state degeneracies are not asserted in closed form.

## Proof
For each \(i\) define the row sum \(r_i=\sum_{j\ne i}\sigma_{ij}\). The \(n\) disjoint row cliques contribute
\[
\sum_i\sum_{j<k,\,j,k\ne i}\sigma_{ij}\sigma_{ik}
=\frac12\sum_i(r_i^2-(n-1)).
\]
Let \(a\) count reversal pairs \(\{(i,j),(j,i)\}\) bearing \((+1,+1)\) and \(b\) count those bearing \((-1,-1)\). The reversal-edge energy in units of \(J\) is \(-n(n-1)/2+2(a+b)\), while the magnetization is \(M=2(a-b)=\sum_i r_i\). Consequently the following identity is exact for **every** spin assignment:
\[
\boxed{\frac{\mathcal H_h(\sigma)}J=-n(n-1)+\sum_{i=1}^n\left[\frac{r_i^2}{2}+(1-x)r_i\right]+4b.}
\tag{1}
\]
Each \(r_i\) belongs to \(\{-(n-1),-(n-3),\ldots,n-1\}\), and \(b\ge0\). Write \(f_x(r)=r^2/2+(1-x)r\). Its minimizers on this finite parity lattice are precisely those lattice points closest to \(x-1\). Thus the sum in (1) is bounded below by \(n\min_r f_x(r)\). When \(n\) is odd and \(x>0\), these minimizers are \(r=k\) on \(k<x<k+2\), where \(k\) ranges through the even nonnegative values, with ties between \(t-2\) and \(t\) at \(x=t\) even. When \(n\) is even and \(x\ge1\), the minimizers are the analogous positive odd values, with ties at positive odd \(x=t\). Saturation occurs at \(r_i=n-1\) beyond the final breakpoint. The lower bound is attained as shown next.

For a permitted positive plateau value \(k\ge0\), with \(k\equiv n-1\pmod2\), choose a simple \(k\)-regular graph \(P\) on the original \(n\) labels; one exists because \(0\le k\le n-1\) and \(nk\) is even. Put both spins \(\sigma_{ij}=\sigma_{ji}=+1\) on each edge of \(P\). The complement \(Q=K_n\setminus P\) has even degree \(n-1-k\) at every vertex and hence admits an Eulerian orientation (also if it is disconnected: orient each Eulerian component). On an oriented edge \(i\to j\) of \(Q\), assign \(\sigma_{ij}=+1\) and \(\sigma_{ji}=-1\). Then \(b=0\) and the directed contributions within every row balance, giving \(r_i=k\) for all \(i\). This constructs an exact optimizer for every positive-field plateau and at either endpoint of every adjoining transition.

For even \(n\) and \(0\le x\le1\), first restrict to configurations with \(M\ge0\), which is legitimate by global spin flip (strictly favored for \(x>0\)). Since each row sum is odd, \(r_i^2\ge1\); (1) gives
\[
\frac{\mathcal H_h}J\ge \frac n2-n(n-1)+(1-x)M+4b\ge\frac n2-n(n-1).
\]
To attain equality choose a perfect matching \(F\) of \(K_n\), orient the even-regular graph \(K_n\setminus F\) Eulerian, and orient the matching edges so that half the labels gain one outgoing and half one incoming edge. Put opposite spins on every reversal pair according to these orientations. Then \(b=0\), \(r_i\in\{-1,+1\}\) with equal counts, and \(M=0\). This proves the exceptional zero-magnetization plateau and its boundary at \(x=1\).

For odd \(n\) and \(x=0\), the rowwise minimizers of \(f_0\) include \(r=-2,0\). Equality with \(b=0\) would force \(M=\sum_i r_i\le0\), whereas \(M=2a\ge0\). Thus every row must have \(r_i=0\); the Eulerian orientation construction with \(k=0\) attains the bound. At positive critical fields, equality in (1) holds exactly when \(b=0\) and every \(r_i\) is one of the two tied minimizers; conversely every such configuration attains the common minimum. No other row minimizer can enter between successive listed thresholds. This proves the complete energy, magnetization and equality-condition claims.

## Verification
The standalone `check.py` enumerates every one of the \(2^{n(n-1)}\) spin assignments for \(n=3,4,5\) by an integer-mask cut recurrence, independent of the proof's row reduction. At half-integer field grid values from zero through \(n+2\), it compares exact lower envelopes against the theorem and verifies off-critical magnetizations. It also checks selected sector multiplicities. Running `python3 check.py` reports 80 successful assertions. In the truncated-tetrahedral case \(n=4\), the open plateaux have magnetizations \(0,4,12\) with degeneracies \(24,30,1\) respectively; in the \(n=5\) case they are \(0,10,20\) with degeneracies \(24,444,1\). These finite tests corroborate but do not establish the all-\(n\) theorem; the constructive inequalities above supply that proof.

## Relationship to prior work
Coffey and Trugman, arXiv:cond-mat/9206011 (first submitted 26 June 1992), investigate the truncated tetrahedron as a quantum and classical **Heisenberg** antiferromagnet with distinct triangle and intertriangle couplings, focusing on correlations and zero-field states. The accessible full-text sections concerning the Hamiltonian and classical approximation do not give the uniform classical Ising longitudinal-field staircase. Strečka, Karľová and Madaras, arXiv:1502.04449v1 (16 February 2015), compute field magnetizations and magnetocaloric behavior for the **five Platonic solids**; their graph-theoretic discussion does not give the infinite truncation family here. The Ising-to-cut transformation in that work is general background; neither it nor the known truncated-tetrahedral geometry is asserted to be new. The new contribution is the parity-sensitive all-order family theorem and the exact zero-temperature ground-state characterization via Eulerian orientations.

## Limitations
This is a finite-graph, zero-temperature theorem; it does not provide finite-temperature partition functions, exact closed degeneracy formulae at all critical fields, or any thermodynamic phase transition. The literature comparison supports novelty only relative to examined sources, not an independent historical-priority certification. Results on other graph truncations or nonuniform coupling do not follow from the proof.

## References
1. D. Coffey and S. A. Trugman, *Correlations for the S=1/2 Antiferromagnet on a Truncated Tetrahedron*, arXiv:cond-mat/9206011v1 (26 June 1992), https://arxiv.org/abs/cond-mat/9206011; doi:10.1103/PhysRevB.46.12717.
2. J. Strečka, K. Karľová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449v1 (16 February 2015), https://arxiv.org/html/1502.04449v1.
