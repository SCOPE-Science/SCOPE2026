# Critical subset-exclusion spectra on a tetrahedral-rung Ising tube

## Finding
For every integer \(n\ge3\), consider the classical antiferromagnetic Ising system on the Cartesian product \(G_n=K_4\square C_n\), with four labelled legs, periodic column index, equal positive exchange \(J\), and uniform longitudinal field \(h\ge0\). At \(h=3J\), its ground energy is exactly \(-6nJ\). Writing \(S_i\subseteq\{1,2,3,4\}\) for the legs with negative spin in column \(i\), its **complete labelled ground-state set** consists precisely of cyclic sequences satisfying
\[
 |S_i|\in\{1,2\},\qquad S_i\cap S_{i+1}=\varnothing \quad(i\pmod n).
\]
Let \(R\) be the number of one-negative-spin columns; the total spin magnetization is \(M=2R\). The exact magnetization generating polynomial \(P_n(y)=\sum_{\sigma\text{ ground}}y^{M(\sigma)/2}\) is \(\operatorname{tr}(T(y)^n)\), where, indexing singleton subsets first and two-element subsets second,
\[
 T(y)=\begin{pmatrix}y(\mathbf 1_4\mathbf 1_4^{\mathsf T}-I_4)&B\\yB^{\mathsf T}&C\end{pmatrix},\quad
 B_{i,A}=\mathbf1_{\{i\notin A\}},\quad
 C_{A,A'}=\mathbf1_{\{A\cap A'=\varnothing\}}.
\]
Here \(B\) is \(4\times6\), \(C\) is \(6\times6\), and \(A,A'\) range over two-element subsets of \(\{1,2,3,4\}\). Its characteristic polynomial factors exactly as
\[
 \det(\lambda I_{10}-T(y))=(\lambda-1)^2
 [\lambda^2-(1+3y)\lambda-3y]
 [\lambda^2+(1+y)\lambda-y]^3.
\]
Thus the **total critical degeneracy** is
\[
 D_n=(2+\sqrt7)^n+(2-\sqrt7)^n
 +3(-1+\sqrt2)^n+3(-1-\sqrt2)^n+2,
\]
with zero-temperature residual entropy per spin \(\lim_{n\to\infty}(4n)^{-1}\log D_n=\frac14\log(2+\sqrt7)\). For even \(n\), the coefficient of \(y^0\) in \(P_n(y)\) is \(6\); for odd \(n\), the minimum power is \(y^2\), with coefficient \(12n(n-2)\). The maximal power \(y^n\) always has coefficient \(3^n+3(-1)^n\). For each fixed \(n\), these distinct extreme magnetizations imply a genuine field-selected crossing at \(h=3J\): immediately below it the preferred critical states have \(M=0\) for even \(n\) or \(M=4\) for odd \(n\), whereas immediately above it they have \(M=2n\). This immediate-left statement does not claim a global odd-period low-field diagram.

For a uniformly sampled configuration among the \(D_n\) critical ground states,
\[
 \frac{R-n\mu}{\sqrt n}\ \Longrightarrow\ \mathcal N(0,\nu),\qquad
 \mu=\frac12+\frac{\sqrt7}{14},\quad \nu=\frac{3\sqrt7}{49}.
\]
In particular, the zero-temperature mean magnetization per spin tends to \(\mu/2\), strictly between zero and one half.

The same model has a complete high-field classification: for \(3J<h<5J\), the ground energy is \(-2nh\), every column has exactly one negative spin, neighboring negative-spin legs differ, and the degeneracy is \(3^n+3(-1)^n\). At \(h=5J\), the ground energy is \(-10nJ\); each column has zero or one negative spin, neighboring negative-spin subsets are disjoint, and the degeneracy is \((2+\sqrt5)^n+(2-\sqrt5)^n+3(-1)^n\), with residual entropy per spin \(\frac14\log(2+\sqrt5)\). For \(h>5J\), the unique ground state is fully positive. For even \(n\), the six alternating balanced-column states are additionally the only ground states throughout \(0\le h<3J\). No complete low-field classification is asserted for odd \(n\).

## Assumptions and scope
The graph has \(4n\) distinguishable vertices labelled \((i,a)\), with \(i\in\mathbb Z/n\mathbb Z\), \(a\in\{1,2,3,4\}\), all six intracolumn \(K_4\) bonds, and the four longitudinal bonds \((i,a)(i+1,a)\) for each \(i\). The case \(n=3\) uses the simple cycle \(C_3\), not a multigraph. Each spin \(\sigma_{i,a}\) belongs to \(\{-1,+1\}\). The energy is exactly
\[
 H(\sigma)=J\sum_{\{u,v\}\in E(G_n)}\sigma_u\sigma_v-h\sum_{u\in V(G_n)}\sigma_u,
\]
with no additive normalization or factor of one half, and \(J>0\). Degeneracies count fully labelled spin assignments, not symmetry orbits. The limiting entropy counts one physical binary spin per vertex. The Gaussian claim takes \(n\to\infty\) at the **exact** field \(h=3J\), and is a statement about a uniform ground-state sample; it is not a finite-temperature phase-transition claim.

## Proof
Let \(r_i=|S_i|\), \(t_i=|S_i\cap S_{i+1}|\), and \(x=h/J\). A column with \(r_i\) negative spins contributes \(6-8r_i+2r_i^2\) to the exchange energy. The longitudinal bonds between columns \(i\) and \(i+1\) contribute \(4-2r_i-2r_{i+1}+4t_i\). The field term is \(-x(4-2r_i)\). Hence the **global identity**, without any approximation, is
\[
 H/J=(10-4x)n+2\sum_i\{r_i^2+(x-6)r_i\}+4\sum_i t_i.\tag{1}
\]
At \(x=3\), this becomes
\[
 H/J+6n=2\sum_i(r_i-1)(r_i-2)+4\sum_i t_i.\tag{2}
\]
Each summand is nonnegative for integer \(0\le r_i\le4\), and equality means \(r_i\in\{1,2\}\) and \(t_i=0\). A cyclic sequence of distinct singletons exists for every \(n\ge3\), proving attainability and the complete characterization. The magnetization formula follows from \(\sum_a\sigma_{i,a}=4-2r_i\): allowed columns with \(r_i=1\) have spin sum \(2\), and those with \(r_i=2\) have spin sum \(0\).

The permitted transitions between subsets give precisely \(T(y)\); the weight \(y\) is attached to an arriving singleton, so \(\operatorname{tr}(T(y)^n)\) records each labelled closed sequence once. To derive the characteristic polynomial without an unproved computer determinant, observe that \(BB^{\mathsf T}=2I_4+\mathbf1_4\mathbf1_4^{\mathsf T}\). On the constant-vector subspaces of singleton and pair coordinates, \(T(y)\) has block \(\bigl(\begin{smallmatrix}3y&3\\2y&1\end{smallmatrix}\bigr)\). On each of the three standard zero-sum singleton directions and its image under \(B^{\mathsf T}\), it has block \(\bigl(\begin{smallmatrix}-y&2\\y&-1\end{smallmatrix}\bigr)\), using \(CB^{\mathsf T}u=-B^{\mathsf T}u\) for \(\sum u_i=0\). The remaining two-dimensional pair subspace is \(\ker B\), on which \(C\) is the identity. These blocks account for all ten dimensions and yield the asserted factorization. Setting \(y=1\) and taking the trace of the \(n\)th power gives \(D_n\). The largest eigenvalue is the simple Perron root \(2+\sqrt7\), strictly larger in modulus than the other eigenvalues, proving the entropy limit.

The coefficient statements follow by expanding the displayed factorization, or the equivalent recurrences: if \(U_0=V_0=2\), \(U_1=1+3y\), \(V_1=-(1+y)\), then
\[
 U_n=(1+3y)U_{n-1}+3yU_{n-2},\qquad
 V_n=-(1+y)V_{n-1}+yV_{n-2},\tag{3}
\]
for \(n\ge2\), and \(P_n(y)=U_n(y)+3V_n(y)+2\) for \(n\ge1\). The constant term is \(3+3(-1)^n\). The coefficient of \(y\) vanishes when \(n\) is odd, while the coefficient of \(y^2\) in that case is \(12n(n-2)\). More explicitly, the odd-length coefficient series obtained from (3) is
\[
 \sum_{k\ge0}[y^2]P_{2k+3}(y)z^{2k+3}=\frac{12z^3(3+6z^2-z^4)}{(1-z^2)^3}
 =\sum_{k\ge0}12(2k+3)(2k+1)z^{2k+3}.
\]
The coefficient of \(y^n\) counts proper four-colourings of an \(n\)-cycle, giving \(3^n+3(-1)^n\). Because the finite configuration space has a strictly positive gap above the \(h=3J\) ground energy, sufficiently small one-sided field perturbations select the minimum or maximum magnetization among these critical states; this proves the immediate crossing asserted above.

For the central limit theorem, the dominant eigenvalue at \(y\) near \(1\) is analytically
\[
 \rho(y)=\frac{1+3y+\sqrt{(1+3y)^2+12y}}2.
\]
There is a strict spectral gap at \(y=1\); consequently, in a complex neighbourhood of \(t=0\), \(\log\mathbb E[e^{tR}]=n\{\log\rho(e^t)-\log\rho(1)\}+O(\eta^n)\) for some \(0<\eta<1\), with the error and its derivatives uniform on a smaller neighbourhood. Direct differentiation gives \(\left.\frac{d}{dt}\log\rho(e^t)\right|_{t=0}=\frac12+\frac{\sqrt7}{14}\) and \(\left.\frac{d^2}{dt^2}\log\rho(e^t)\right|_{t=0}=\frac{3\sqrt7}{49}>0\). Expanding at imaginary \(t=iu/\sqrt n\) proves convergence of characteristic functions to the stated Gaussian law.

At \(x=5\), identity (1) yields
\[
 H/J+10n=2\sum_i r_i(r_i-1)+4\sum_i t_i.\tag{4}
\]
Equality requires \(r_i\in\{0,1\}\) and disjoint adjacent negative sets. The five-state transition matrix, indexed by the empty set and the four singletons, is \(\bigl(\begin{smallmatrix}1&\mathbf1_4^{\mathsf T}\\\mathbf1_4&\mathbf1_4\mathbf1_4^{\mathsf T}-I_4\end{smallmatrix}\bigr)\). Its characteristic polynomial is \((\lambda+1)^3(\lambda^2-4\lambda-1)\), proving the second critical degeneracy and entropy. For \(3<x<5\), interpolating the bounds from (2) and (4) gives \(H/J\ge-2xn\), and equality holds exactly for the intersection of both critical sets: \(r_i=1\) and disjoint neighbors. For \(x>5\), use \(H_x=H_5-(h-5J)M\), \(M\le4n\), to conclude that only the all-positive configuration can minimize. Finally, at \(x=0\), each \(K_4\) column has energy at least \(-2J\), and each longitudinal four-bond interface has energy at least \(-4J\). Their simultaneous equality requires balanced columns that alternate by complementation; for even \(n\) this gives exactly six states. Interpolating the lower bounds at \(x=0\) and \(x=3\) proves the even-period assertion.

## Verification
The included standalone `check.py` implements two *independent* descriptions: the original 16-state-column Hamiltonian with a finite-state energy-and-magnetization dynamic program, and the ten- or five-state disjoint-negative-subset transition enumerator. It compares exact ground energies and full magnetization polynomials for \(n=3,\dots,9\) at both critical fields; the two transfer counts and their spectral recurrences are checked for \(n=3,\dots,16\). For \(n=3,4\), direct enumeration of every labelled spin configuration checks the original-Hamiltonian recurrence at fields \(h/J\in\{0,3,4,5,6\}\). The reported outcome is `K4_CYCLE_ISING_CHECKS_PASSED 163`. These finite checks are supplementary; equations (1)–(4), the block decomposition, and analytic perturbation prove the unlimited-size statements.

Reproduce from an unpacked package with `python3 check.py` (standard library only). 

## Relationship to prior work
Frustrated magnetic ladders and tetrahedral spin units are established physical models. Chattopadhyay and Bose (2001, arXiv:cond-mat/0107393) study quantum two-chain ladders with tetrahedral blocks alternating with dimers, not the classical \(K_4\square C_n\) graph. Strečka, Michaud and Mila (2013, arXiv:1305.6703) analyze spin-one Ising–Heisenberg two-leg ladders with a different interaction topology and rung conservation. Gómez Albarracín, Arlego and Rosales (2014, Phys. Rev. B 90, 174403; see also the accessible 2014 conference account) analyze a quantum four-leg tube with square plaquettes, not complete four-spin rungs with four matching longitudinal bonds. Jurčišinová and Jurčišin (2014) solve a recursive tetrahedron lattice, again a distinct inter-unit graph.

A previously published exact three-leg classical Ising tube result concerns \(C_3\square C_n\), which is not this model: its rung state space, allowed critical-transition graph, characteristic roots, and entropy differ. The local-energy method and transfer-matrix idea are standard, but the specific full ten-state disjoint-subset spectrum, magnetization law, fluctuation coefficient and two field-boundary counts above were not found in the inspected sources or semantic research searches. This is a best-evidence originality assessment, not a proof of historical novelty; specialized unpublished work or an unrecognized equivalent transfer solution could cover the claim.

## Limitations
No complete characterization is asserted for odd \(n\) and fields below \(3J\). The Gaussian limit describes uniform **zero-temperature ground states exactly at** \(h=3J\); finite-temperature or continuum critical exponents are not inferred. The model is classical with binary spins and equal exchange; unequal inter-rung bonds, quantum fluctuations, and open boundaries are not covered. The four-leg quantum-tube journal article and the recursive tetrahedron article were not available in accessible full journal text; comparison uses their abstracts and available closely related full public text. Independent scientific audit has not been performed, and historical priority is not guaranteed.

## References
- E. Chattopadhyay and I. Bose, *Magnetization of coupled spin clusters in ladder geometry*, arXiv:cond-mat/0107393, first submitted 2001-07-19. https://arxiv.org/abs/cond-mat/0107393
- J. Strečka, F. Michaud and F. Mila, *Exact ground states of frustrated spin-1 Ising–Heisenberg and Heisenberg ladders in a magnetic field*, arXiv:1305.6703, first submitted 2013-05-29. https://arxiv.org/abs/1305.6703
- F. A. Gómez Albarracín, M. Arlego and H. D. Rosales, *Magnetization plateaus and jumps in a frustrated four-leg spin tube under a magnetic field*, Phys. Rev. B **90**, 174403 (2014). https://doi.org/10.1103/PhysRevB.90.174403
- H. D. Rosales, M. Arlego and F. A. Gómez Albarracín, *Magnetization plateaux and jumps in frustrated four-leg spin tubes in magnetic fields*, J. Phys.: Conf. Ser. **568**, 042023 (2014). https://doi.org/10.1088/1742-6596/568/4/042023
- E. Jurčišinová and M. Jurčišin, *Solution of the antiferromagnetic Ising model on a tetrahedron recursive lattice*, Phys. Rev. E **89**, 032123 (2014). https://doi.org/10.1103/PhysRevE.89.032123
