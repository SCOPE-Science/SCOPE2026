# Nonvanishing Witten indices and exponential supersymmetric zero-mode protection on step-three generalized Petersen networks

## Finding
For every integer \(n\ge7\), let \(G_n=\mathrm{GP}(n,3)\), and equip the hard-neighbor-exclusion fermionic Hilbert space with the standard equal-amplitude supersymmetric Hamiltonian \(H_n=\{Q,Q^\dagger\}\) described below. Its exact Witten index is
\[
 W_n=\sum_{q(\lambda)=0}\lambda^n+2\cos(\pi n/3),\qquad q(z)=z^5-z+1,
\]
where roots are counted with multiplicity. This index is **never zero**. It equals \(1,3,-11,4,1,6\) for \(n=7,8,9,10,11,12\), respectively, and has sign \((-1)^n\) for every \(n\ge13\).

Let \(\rho\) denote the unique positive real root of \(\rho^5-\rho-1=0\) (\(\rho\approx1.1673039783\)). Then
\[
 W_n=(-\rho)^n+O((11/10)^n),\qquad \dim\ker H_n\ge |W_n|.
\]
In particular, the model has a supersymmetric zero-energy state for **every** \(n\ge7\), and its number of zero-energy states has exponential lower-growth rate
\[
 \liminf_{n\to\infty}\frac{\log(\dim\ker H_n)}{2n}\ge\frac{\log\rho}{2}\approx0.0773484.
\]
For \(n\ge25\), the completely explicit lower bound \(\dim\ker H_n\ge(7/6)^n-4(11/10)^n-2>0\) also holds.

## Assumptions and scope
The graph has vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/n\mathbb Z\), and exactly the edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+3}\). The restriction \(n\ge7\) makes this an ordinary simple, cubic graph with distinct step-three edges. The Hilbert space has one orthonormal vector \(|I\rangle\) for each independent vertex set \(I\subseteq V(G_n)\), with fermion number \(F|I\rangle=|I||I\rangle\). Set
\[
 Q=\sum_{j\in V(G_n)}c_j^\dagger\prod_{k\sim j}(1-c_k^\dagger c_k),\quad H_n=QQ^\dagger+Q^\dagger Q.
\]
The usual ordered-fermion signs are understood; the hard-core operators act only on allowed independent-set configurations. All nonzero local supercharge amplitudes are one. No onsite disorder, boundary twist, or additional hopping is included. The Witten index is the graded trace \(W_n=\operatorname{Tr}((-1)^F e^{-\beta H_n})\), independent of \(\beta\ge0\).

## Proof
**1. Graded trace and ground states.** The supercharge satisfies \(Q^2=0\), and every positive-energy eigenspace of \(H_n\) pairs opposite fermion parity. Consequently
\[
 W_n=\sum_{I\text{ independent in }G_n}(-1)^{|I|}=b_n-f_n,
\]
where \(b_n,f_n\) count even- and odd-fermion **zero-energy** states, respectively (not all independent sets). Thus \(\dim\ker H_n=b_n+f_n\ge|W_n|\).

**2. An exact finite-state transfer.** A column \(i\) may be empty, occupied at \(u_i\), or occupied at \(v_i\); encode these by \(0,1,2\). A cyclic word \((a_i)_{i\in\mathbb Z/n\mathbb Z}\) represents an independent set exactly when adjacent columns never both carry \(1\) and columns separated by three never both carry \(2\). On the \(27\) ordered triples \((a,b,c)\in\{0,1,2\}^3\), define \(T_{(a,b,c),(b,c,d)}=(-1)^{\mathbf1_{d\ne0}}\) if \((c,d)\ne(1,1)\) and \((a,d)\ne(2,2)\), and zero otherwise. Each closed length-\(n\) transfer walk is uniquely one labelled cyclic independent configuration, and its product of weights is \((-1)^{|I|}\). Hence \(W_n=\operatorname{tr}(T^n)\) for every \(n\ge7\).

Exact integer determinant expansion gives
\[
 \det(zI-T)=z^{20}(z^2-z+1)(z^5-z+1).
\]
The 20 zero roots contribute nothing for positive \(n\); the quadratic roots contribute \(2\cos(\pi n/3)\), proving the displayed formula. This includes a complete formula for every \(n\), not a finite extrapolation.

**3. Dominance and nonvanishing.** Exact rational root isolation for \(q(z)=z^5-z+1\) shows that its sole real root is \(-\rho\), with \(-6/5<-\rho<-7/6\), and all four remaining roots satisfy \(|z|<11/10\). One set of certified rational enclosures for the two complex-conjugate pairs has positive imaginary representatives in the rectangles
\[
 -0.1813<\Re z<-0.1812,\quad 1.0839<\Im z<1.0840,
\]
\[
 0.7648<\Re z<0.7650,\quad0.3524<\Im z<0.3526.
\]
Each rectangle lies strictly inside \(|z|<11/10\); the exact isolating intervals and their completeness are replayable in `verify_transfer.py` using rational arithmetic. It follows that
\[
 |W_n-(-\rho)^n|\le4(11/10)^n+2.
\]
At \(n=25\), \((7/6)^{25}>4(11/10)^{25}+2\); since the left-to-right growth ratio is at least \((7/6)/(11/10)=35/33>1\), the strict domination persists for all larger \(n\). Thus \(W_n\) has sign \((-1)^n\) and is nonzero for every \(n\ge25\). Exact transfer traces for \(7\le n\le24\) are
\[
 (1,3,-11,4,1,6,-12,13,-7,3,-16,29,-18,8,-23,43,-45,30),
\]
ordered by increasing \(n\), establishing all remaining cases. Finally the negative real root has strictly larger modulus than every other root, yielding the stated asymptotic and exponential ground-state lower bound.

## Verification
Execute `python verify_transfer.py` with SymPy installed: it constructs the 27-state matrix, computes its exact characteristic polynomial and the 7–24 trace values, isolates all quintic roots in certified rational rectangles, and proves the large-size dominance bound. Independently execute `python verify_graph.py` with Python 3.10 or later: it directly builds the actual cubic graphs and computes their signed independent-set sums using vertex deletion and closed-neighborhood recursion for every \(7\le n\le14\). Both checks passed on the embedded versions. The recursive identity is \(W(G)=W(G-v)-W(G-N[v])\). The infinite-size conclusions follow from the symbolic determinant and certified root bounds, not the finite checks.

## Relationship to prior work
Fendley, Schoutens and de Boer introduced the supersymmetric hard-core graph Hamiltonian and the graded-index identity in 2002, including examples on periodic chains and cubes; those mechanisms are not claimed as new. Later triangular-lattice and ladder work uses transfer matrices to study Witten indices and degeneracy. Pandey's 2026 generalized-Petersen independence-polynomial study explicitly introduces transfer-matrix evaluation for arbitrary steps and computes finite ranges for steps including three; that general transfer principle and those finite counts are also not claimed as new. The new statement assessed here is the **all-size nonzero-index theorem with eventual parity sign and a strictly positive exponential protection rate for \(\mathrm{GP}(n,3)\)**; it requires the exact specialized characteristic factor, global root separation, and a uniform sign proof. A published calculation of the homotopy type of \(\operatorname{Ind}(\mathrm{GP}(9,3))\) already implies the particular value \(W_9=-11\); that single-size case is not separately claimed. The step-two generalized-Petersen homotopy classification does not imply this step-three all-size theorem.

## Limitations
The result is a lower bound on supersymmetric ground-state degeneracy, **not** an exact degeneracy or a claim that every ground state has one parity. The index can have cancellations between zero-energy parity sectors. Its exponential exponent is only a guaranteed lower rate. The theorem assumes the uniform hard-core supersymmetric Hamiltonian, specific step-three generalized Petersen graphs, and simple cyclic boundary conditions; perturbations that break supersymmetry are not covered. It does not prove a thermodynamic phase transition or the full excited-state spectrum. Historical priority is assessed against the cited accessible literature and indexed records, not certified against every possible unindexed computation.

## References
1. P. Fendley, K. Schoutens, J. de Boer, *Lattice Models with N=2 Supersymmetry*, arXiv:hep-th/0210161v1, first posted 2002-10-17, https://arxiv.org/abs/hep-th/0210161 .
2. L. Huijse, D. Mehta, N. Moran, K. Schoutens, J. Vala, *Supersymmetric lattice fermions on the triangular lattice: superfrustration and criticality*, New Journal of Physics 14 (2012) 073002, https://doi.org/10.1088/1367-2630/14/7/073002 .
3. R. Pandey, *Parity-Dependent Real-Rootedness in Independence Polynomials of Generalized Petersen Graphs*, arXiv:2601.03293v1, first posted 2026-01-05, https://arxiv.org/abs/2601.03293 .
4. Y. Kim, *Perfect matching complexes of antiprism graphs and independence complexes of generalized Petersen graphs GP(n,2)*, arXiv:2611.22021v1, first posted 2026-11-17, https://arxiv.org/abs/2611.22021 .
