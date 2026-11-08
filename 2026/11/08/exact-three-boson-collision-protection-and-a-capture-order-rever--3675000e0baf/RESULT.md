# Exact three-boson collision protection and a capture-order reversal on complete quantum networks

## Finding

For every integer \(n\ge 3\), consider three identical, noninteracting bosons hopping with uniform nonzero real amplitude \(J\) on the complete graph \(K_n\). Each vertex has an on-site, irreversible three-boson loss channel with an arbitrary strictly positive rate. The complete permanently loss-free subspace \(\mathcal D\) has dimension
\[
\boxed{\dim\mathcal D=\binom{n+2}{3}-3n.}
\]
For an initially localized normalized occupation state, the eventual probability of a three-body loss event is exactly
\[
\boxed{\begin{aligned}
\eta_{(3)}(n)&=1,\\
\eta_{(2,1)}(n)&=\frac{n^2-2n+2}{(n-1)(n^2-3n+3)},\\
\eta_{(1,1,1)}(n)&=\frac{6(n-2)}{(n-1)(n^2-3n+3)}.
\end{aligned}}
\]
The subscripts denote, respectively, three atoms at one vertex, two atoms at one vertex and one at a different vertex, and three atoms at three distinct vertices. All expressions are independent of the individual positive loss rates and the magnitude and sign of \(J\).

The capture ordering reverses at a finite, exact network size: \(\eta_{(1,1,1)}>\eta_{(2,1)}\) precisely for \(3\le n\le5\), whereas \(\eta_{(1,1,1)}<\eta_{(2,1)}\) for every \(n\ge6\). Thus the configuration with three initially separated atoms is *more* susceptible to eventual triplet loss than an initially co-located pair on the smallest networks, but less susceptible on all larger networks.

## Assumptions and scope

The Hilbert space is \(\mathcal H_3=\operatorname{Sym}^3(\mathbb C^n)\), of dimension \(\binom{n+2}{3}\), with the standard normalized bosonic occupation basis. There are exactly three atoms initially, no two-body interaction, no on-site energy disorder, and all \(n(n-1)/2\) edges have the same real hopping amplitude \(J\ne0\). With bosonic operators \(b_v\), set
\[
H=J\sum_{v\ne w}b_v^\dagger b_w,
\qquad L_v=\sqrt{\gamma_v/6}\,b_v^3,\qquad\gamma_v>0.
\]
The loss operators take the three-atom sector to the vacuum; after a jump, no atoms remain, and there can be no further jump. Equivalently, conditional no-jump dynamics on \(\mathcal H_3\) have generator
\[
H_{\mathrm{eff}}=H-\frac{i}{2}\Gamma,
\qquad\Gamma=\sum_{v=1}^n\gamma_v |v,v,v\rangle\langle v,v,v|.
\]
Here \(|v,v,v\rangle\) is the normalized triple-occupancy state. For arbitrary initial density operator \(\rho\) supported in \(\mathcal H_3\), the asymptotic capture probability is \(\eta(\rho)=1-\operatorname{Tr}(P_{\mathcal D}\rho)\), where the complete projector \(P_{\mathcal D}\) is explicitly determined below. The result concerns eventual loss (infinite-time probability), not a decay rate or finite-time distribution.

## Proof

**1. Four free-energy sectors.** Let \(u=n^{-1/2}(1,\ldots,1)\) and let \(U=|u\rangle\langle u|\), \(W=I-U\). The one-body adjacency operator of \(K_n\) is \(nU-I\), with eigenvalues \(n-1\) on \(\mathbb Cu\) and \(-1\) on \(W\mathbb C^n\). In the three-particle symmetric tensor space, define the mutually orthogonal spectral projectors \(Q_r\), for \(0\le r\le3\), by restricting to the symmetric subspace the sum of the \(\binom3r\) tensor products that contain \(r\) factors \(W\) and \(3-r\) factors \(U\). Their eigenvalues and ranks are
\[
E_r=J(3(n-1)-nr),\qquad\operatorname{rank}Q_r=\binom{n+r-2}{r}.
\]
As \(J\ne0\), all four energies are distinct.

**2. Exact bright ranks and dark projector.** Put \(\ell_v=|v,v,v\rangle\) and define \(C_r:\mathbb C^n\to\mathcal H_3\) by \(C_re_v=Q_r\ell_v\). Each spectral sector has a bright space \(\operatorname{ran}C_r\). Its Gram matrix is
\[
G_r(v,w)=\langle\ell_v,Q_r\ell_w\rangle
=\frac{\binom3r}{n^3}
\begin{cases}
(n-1)^r,&v=w,\\
(-1)^r,&v\ne w.
\end{cases}
\]
Write \(M_r=n^3G_r/\binom3r\). On the all-ones direction and its \((n-1)\)-dimensional orthogonal complement, the corresponding eigenvalues of \(M_r\) are, respectively,
\[
\begin{array}{c|cc|c}
r&\text{uniform}&\text{zero-sum}&\operatorname{rank}G_r\\\hline
0&n&0&1\\
1&0&n&n-1\\
2&n(n-1)&n(n-2)&n\\
3&n(n-1)(n-2)&n(n^2-3n+3)&n
\end{array}
\]
The last two rows are strictly positive for \(n\ge3\). Consequently the total number of independent bright directions is exactly \(1+(n-1)+n+n=3n\), and the complementary loss-free dimension is the stated binomial formula.

Writing \(G_r^+\) for the Moore--Penrose inverse, the full orthogonal dark projector is
\[
\boxed{P_{\mathcal D}=I_{\mathcal H_3}-\sum_{r=0}^{3}C_rG_r^+C_r^\dagger.}
\]
The terms in the sum are orthogonal projections onto bright spaces lying in different energy sectors. This also supplies the complete dark space, not merely its dimension.

**3. All positive rates give the same eventual capture.** Because every \(\gamma_v\) is strictly positive, \(\ker\Gamma\) is exactly the common orthogonal complement of the vectors \(\ell_v\). The largest \(H\)-invariant subspace contained in \(\ker\Gamma\) is \(\mathcal D=\bigoplus_r(\operatorname{ran}Q_r\cap\ker\Gamma)\). Both \(H\) and \(\Gamma\) reduce \(\mathcal D\oplus\mathcal D^\perp\). Every eigenvalue of \(H_{\mathrm{eff}}\) on \(\mathcal D^\perp\) has strictly negative imaginary part: if the imaginary part vanished, the corresponding eigenvector would be in \(\ker\Gamma\) and also be an eigenvector of \(H\), contradicting its orthogonality to \(\mathcal D\). Finite dimensionality therefore implies complete long-time decay on \(\mathcal D^\perp\) while \(\mathcal D\) evolves unitarily. The no-jump norm tends to \(\operatorname{Tr}(P_{\mathcal D}\rho)\), proving the capture rule for every initial density matrix and every set of positive rates.

**4. Exact occupation-resolved probabilities.** Take a normalized localized three-particle occupation state \(|a,b,c\rangle_{\mathrm B}\), and let \(N_\pi\in\{1,3,6\}\) be the number of its distinct ordered permutations. For each vertex \(v\), let \(t_v\) count how many of \(a,b,c\) equal \(v\). A direct expansion of the tensor projectors gives
\[
\langle\ell_v|Q_r|a,b,c\rangle_{\mathrm B}
=\frac{\sqrt{N_\pi}}{n^3}p_r(t_v),\quad
p_r(t)=\sum_{j=0}^r\binom tj\binom{3-t}{r-j}(n-1)^j(-1)^{r-j}.
\]
For the three initial occupancy patterns, the populations of vertices with each value of \(t_v\) are:
\[
\begin{array}{c|cccc|c}
\text{pattern}&t=0&t=1&t=2&t=3&N_\pi\\\hline
(3)&n-1&0&0&1&1\\
(2,1)&n-2&1&1&0&3\\
(1,1,1)&n-3&3&0&0&6
\end{array}
\]
With \(b_r=(\langle\ell_v|Q_r|a,b,c\rangle_{\mathrm B})_{v=1}^n\), the exact bright weight is \(\eta=\sum_{r=0}^3 b_r^\dagger G_r^+ b_r\). Substitute the displayed polynomial and Gram eigenvalues, separately accounting for the uniform and zero-sum components. Elementary rational simplification gives the three capture formulas in the Finding. The symbolic checker reproduces this calculation without finite-\(n\) interpolation.

Finally,
\[
\eta_{(1,1,1)}-\eta_{(2,1)}
=\frac{-n^2+8n-14}{(n-1)(n^2-3n+3)}.
\]
The denominator is positive for every integer \(n\ge3\). The numerator has real roots \(4-\sqrt2\) and \(4+\sqrt2\), so it is strictly positive at the integers \(3,4,5\) and strictly negative for \(n\ge6\). No integer equality case exists.

## Verification

The standalone script `verify_symbolic.py` reconstructs all four Gram eigenvalue pairs, evaluates the projected collision-polynomial weights symbolically for all three occupation types, and checks the exact rational formulas and capture-order difference as identities in \(n\). It requires Python and SymPy.

Independently, `verify_fock.py` constructs the bosonic hopping matrix directly in the normalized occupation basis, diagonalizes it, finds the nullspaces of the triple-collision detection maps in each energy sector, and compares dark dimensions and capture probabilities for every \(n=3,4,5,6,7,8\). It also checks the count of undamped non-Hermitian eigenvalues using nonuniform positive loss rates for \(n=3,4,5,6\). It requires NumPy and SciPy. The finite tests support, but do not replace, the all-size proof above.

Representative exact values are
\[
\begin{array}{c|c|cc}
n&\dim\mathcal D&\eta_{(2,1)}&\eta_{(1,1,1)}\\\hline
3&1&5/6&1\\
4&8&10/21&4/7\\
5&20&17/52&9/26\\
6&38&26/105&8/35\\
8&96&50/301&36/301
\end{array}
\]

## Relationship to prior work

Krovi and Brun (2006) identify spectral dark subspaces in quantum walks, including continuous-time settings. Their result supplies the general symmetry/degeneracy mechanism but not a three-boson, all-to-all hopping, local triple-annihilation model, the four exact collision Gram ranks, or the occupation-order reversal. Daley and collaborators (2008) derive and motivate on-site three-body Lindblad loss in lattice bosons, while Diehl and collaborators (2009) develop a general theory for three-body-constrained lattice Bose gases; these works address dissipative constraints and many-body behavior rather than the present exactly solved three-particle complete-graph asymptotics. The mathematical claim here is the evaluated projector, rank formula, and occupation-resolved capture probabilities, not the general Lindblad description or the general dark-space idea.

## Limitations

The hopping graph must be the complete graph with uniform edges; on-site energy disorder, additional two-body interactions, zero loss rates, higher initial particle number, and finite-time decay laws are outside the theorem. The infinitely long survival probabilities do not imply a hard-core constraint for all initial conditions. Numerical verification was performed only on stated finite sizes. The literature comparison does not establish absolute historical priority, and independent validation has not been performed.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094 (first public version 2006-06-10), https://arxiv.org/html/quant-ph/0606094v1.
2. A. J. Daley, J. M. Taylor, S. Diehl, M. Baranov and P. Zoller, *Atomic three-body loss as a dynamical three-body interaction*, arXiv:0810.5153 (first public version 2008-10-28), https://arxiv.org/abs/0810.5153.
3. S. Diehl, M. Baranov, A. J. Daley and P. Zoller, *Quantum Field Theory for the Three-Body Constrained Lattice Bose Gas, Part I: Formal Developments*, arXiv:0912.3192 (first public version 2009-12-16), https://arxiv.org/abs/0912.3192.
