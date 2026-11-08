# Collision-dark boson projector and size-two anomaly on complete bipartite networks

## Finding

For every integer \(a,b\ge2\), consider two indistinguishable, noninteracting bosons moving with uniform nonzero hopping \(J\) on the complete bipartite graph \(K_{a,b}\), with irreversible two-particle loss on simultaneous occupation of any vertex. All site-specific collision-loss strengths may be different, provided each is strictly positive. The full undamped subspace has only zero-energy states and an explicit orthogonal projector \(P_{\mathrm{dark}}\), below. Put \(N=a+b\). Its dimension is
\[
\boxed{\dim\mathcal D=\frac{(N-1)(N-4)}2+\mathbf1_{\{a=2\}}+\mathbf1_{\{b=2\}}.}
\]
At fixed \(N\), all bicliques with both parts of size at least three have the **same dark dimension**, while every part of size two adds one extra protected direction. The full projector nevertheless distinguishes different bipartitions.

For a state \(\rho\) (any density matrix on the symmetric two-particle Hilbert space), the total eventual loss probability is exactly
\[
\eta(\rho)=1-\operatorname{Tr}(P_{\mathrm{dark}}\rho).
\]
In particular, starting at one vertex in each part has capture probability
\[
\boxed{\eta_{AB}=\frac1a+\frac1b-\frac1{ab}.}
\]
For a pair at two distinct vertices of part \(A\), put \(D=2ab-a-b\). The capture probability is
\[
\boxed{\eta_{AA}=\begin{cases}1-\dfrac{2(b-1)}{(a-1)D},&a=2,\\[3pt]\dfrac2{a-1}-\dfrac{2(b-1)}{(a-1)D},&a\ge3.\end{cases}}
\]
Interchange \(a,b\) for a pair in part \(B\). For instance \(K_{2,4}\) has six dark states and capture \(5/8\) for opposite-part input, whereas \(K_{3,3}\) has five dark states and capture \(5/9\) for the same kind of input, despite both having six vertices.

## Assumptions and scope

Let \(A\) and \(B\) denote disjoint vertex classes of cardinalities \(a,b\ge2\). On \(\mathbb C^{N}\), \(T\) is the adjacency matrix of \(K_{a,b}\). The Hilbert space is \(\mathcal H=\operatorname{Sym}^{2}\mathbb C^N\). For distinct vertices define the orthonormal boson vectors \(|ij\rangle_+=(|i\rangle|j\rangle+|j\rangle|i\rangle)/\sqrt2\), and for coincident vertices \(|ii\rangle=|i\rangle|i\rangle\). Fix any real \(J\ne0\) and any \(\gamma_i>0\). The conditional (no-jump) effective Hamiltonian is
\[
H_{\rm eff}=J(T\otimes I+I\otimes T)|_{\mathcal H}-i\sum_{i=1}^N\gamma_i|ii\rangle\langle ii|.
\]
By eventual capture we mean \(1-\lim_{t\to\infty}\operatorname{Tr}(e^{-iH_{\rm eff}t}\rho e^{iH_{\rm eff}^{\dagger}t})\). We do not treat finite-time detection statistics, coherent two-body interactions, nonuniform hoppings, or vanishing detector strengths.

Here is an explicit projector in the orthonormal distinct-pair basis. On the subspace spanned by \(|ij\rangle_+\) with \(i\in A,j\in B\), set
\[
P_{AB}=\left(I_a-\frac{\mathbf1_a\mathbf1_a^\mathsf T}{a}\right)\otimes\left(I_b-\frac{\mathbf1_b\mathbf1_b^\mathsf T}{b}\right).
\]
For \(m\ge3\), let \(C_m\) be the unsigned vertex-versus-edge incidence matrix of \(K_m\) and define \(R_m=I_{\binom m2}-C_m^\mathsf T(C_mC_m^\mathsf T)^{-1}C_m\). Define \(R_2=0\). Embed \(R_a,R_b\) on distinct-pair states internal to the corresponding class. Define
\[
|\phi\rangle=\frac1{a-1}\sum_{\{i,j\}\subset A}|ij\rangle_+-\frac1{b-1}\sum_{\{i,j\}\subset B}|ij\rangle_+,
\qquad \langle\phi|\phi\rangle=\frac{2ab-a-b}{2(a-1)(b-1)}.
\]
Then, with zero blocks on all collision states,
\[
\boxed{P_{\rm dark}=P_{AB}\oplus R_a\oplus R_b+\frac{|\phi\rangle\langle\phi|}{\langle\phi|\phi\rangle}.}
\]
The summands have orthogonal ranges; the direct-sum symbols specify the disjoint spatial pair supports, not an additional direct sum after the mixed rank-one term.

## Proof

**(1) Only zero-energy undamped eigenvectors.** The one-particle adjacency has eigenvectors \(u_\pm=(\mathbf1_A/\sqrt a\pm\mathbf1_B/\sqrt b)/\sqrt2\) with eigenvalues \(\pm\sqrt{ab}\), and a zero eigenspace \(Z\) of dimension \(N-2\). Both \(u_+\) and \(u_-\) have nonzero entries at every vertex. Here \(u\odot v\) means the symmetrized tensor \((u\otimes v+v\otimes u)/\sqrt2\) for orthogonal \(u,v\), and \(u\odot u=u\otimes u\). The bosonic two-particle energies, divided by \(J\), belong to \(\{\pm2\sqrt{ab},\pm\sqrt{ab},0\}\). The \(\pm2\sqrt{ab}\) eigenspaces are each spanned by \(u_\pm\odot u_\pm\), whose diagonal entries are nonzero. The \(\pm\sqrt{ab}\) eigenspaces are \(u_\pm\odot Z\); their diagonal entries are proportional to \((u_\pm)_i z_i\). Their complete vanishing forces \(z=0\). Thus any energy eigenvector vanishing on every diagonal has energy zero.

**(2) Complete zero-energy kernel.** Identify a symmetric two-particle vector with a complex symmetric \(N\)-by-\(N\) amplitude matrix \(X=\begin{psmallmatrix}P&M\\M^\mathsf T&Q\end{psmallmatrix}\), with blocks for \(A\) and \(B\). Vanishing on collision states says \(\operatorname{diag}P=\operatorname{diag}Q=0\). The equation \(TX+XT=0\), comparing blocks, is equivalent to
\[
M\mathbf1_b=0,\quad M^\mathsf T\mathbf1_a=0,\quad P\mathbf1_a=c\mathbf1_a,\quad Q\mathbf1_b=-c\mathbf1_b
\]
for some \(c\in\mathbb C\). To see this, the diagonal of the upper-left block of \(TX+XT\) equals \(2M\mathbf1_b\), and similarly on \(B\); the off-diagonal block is \(\mathbf1_a\mathbf1_b^\mathsf T Q+P\mathbf1_a\mathbf1_b^\mathsf T\).

The cross-block space of double-centered \(M\) has dimension \((a-1)(b-1)\) and projector \(P_{AB}\). The symmetric zero-diagonal \(P\) with zero row sums is \(\ker C_a\), of dimension \(a(a-3)/2\) for \(a\ge3\); for \(a=2\) it is zero. The assertion follows because \(C_a\) has rank \(a\) when \(a\ge3\): a vector orthogonal to all its columns must satisfy \(y_i+y_j=0\) for every edge, and any triangle forces \(y=0\). This produces \(R_a\), and analogously \(R_b\). The remaining one-dimensional class has nonzero constant row sums on each part with opposite signs; it is generated by \(|\phi\rangle\). Its component along each internal-edge kernel vanishes since those kernels have zero row sums. The four summands are therefore mutually orthogonal and exhaust the kernel.

Consequently \(\dim\mathcal D=(a-1)(b-1)+f(a)+f(b)+1\), where \(f(2)=0\), \(f(m)=m(m-3)/2\) for \(m\ge3\). Elementary simplification yields the boxed dimension formula.

**(3) Eventual capture.** For \(\Gamma=\sum_i\gamma_i|ii\rangle\langle ii|\), every real-eigenvalue eigenvector of \(H_{\rm eff}=H_0-i\Gamma\) lies in \(\ker\Gamma\): taking imaginary parts of its eigenvalue inner product gives \(\langle\psi,\Gamma\psi\rangle=0\). Such an eigenvector must also be an eigenvector of \(H_0\), hence belongs to the computed dark space. On its orthogonal complement the finite matrix \(H_{\rm eff}\) has spectrum strictly in the lower half-plane. There can be no growing Jordan contribution with zero decay there, so the complement decays; the dark space evolves unitarily and is orthogonal to that complement. Thus the survival limit equals \(\operatorname{Tr}(P_{\rm dark}\rho)\) for all density matrices, regardless of the positive rates.

**(4) Localized capture.** The diagonal of \(P_{AB}\) on a cross-pair basis element is \((a-1)(b-1)/(ab)\). For distinct vertices of \(A\), the \(R_a\) diagonal equals \((a-3)/(a-1)\) when \(a\ge3\), and zero when \(a=2\). This follows by \(C_aC_a^\mathsf T=(a-2)I+\mathbf1_a\mathbf1_a^\mathsf T\) and direct inversion. The rank-one term contributes \(2(b-1)/((a-1)(2ab-a-b))\), and the formulas follow on subtracting from one. The \(B\)-side case follows by symmetry.

## Verification

Two separately organized exact-arithmetic scripts are included: `verification/check_biclique.py` constructs the claimed rational projector and confirms symmetry, idempotence, annihilation by the full boson hopping operator, rank, and all three capture probabilities for ten choices \((a,b)\) through \((5,5)\). `verification/check_krylov.py` independently forms the complete symmetric two-particle hopping matrix and an observability matrix using collision amplitudes through powers zero to four; exact ranks agree for six choices through \((4,4)\), including both two-site anomalies. These checks are finite corroboration only; Steps (1)–(4) are the infinite-family proof.

Reproduce from this directory with `python verification/check_biclique.py` and `python verification/check_krylov.py` after installing the open-source `sympy` Python package. No floating-point comparisons enter either checker.

## Relationship to prior work

Krovi and Brun (2006) develop the general phenomenon of undetectable eigenstates and infinite quantum-walk hitting times. Gamble et al. (2010) formulate noninteracting two-boson walks on graphs through a symmetric Kronecker sum, primarily for graph-isomorphism questions. Thiel et al. (2019) give spectral bright/dark formulas for a different, stroboscopic repeated-measurement protocol. These general mechanisms and the bosonic Hamiltonian are not claimed as new. The contribution here is the exact continuous-loss projector, total-dimension formula with its two-vertex exception, and different localized capture laws across the entire biclique family. The special four-cycle and one-hub star limits have related prior treatments; only the new complete-bipartite classification is assessed here.

## Limitations

The result applies only to uniform coherent edge hoppings, noninteracting identical bosons, complete bipartite networks and strictly positive loss at every collision site. It establishes eventual capture, not finite-time decay or spectral gaps. The novelty assessment is based on inspected sources and semantic record searches, not an exhaustive historical index; an equivalent unindexed exact biclique calculation remains possible. The general projector concept is known, and this claim concerns its nontrivial explicit evaluation on this family.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, first public arXiv version June 10, 2006, https://arxiv.org/abs/quant-ph/0606094.
2. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, first public arXiv version February 16, 2010, https://arxiv.org/abs/1002.3003.
3. F. Thiel, I. Mualem, D. A. Kessler and E. Barkai, *Quantum total detection probability from repeated measurements II. Exploiting symmetry*, first public arXiv version September 4, 2019, https://arxiv.org/abs/1909.02114.
