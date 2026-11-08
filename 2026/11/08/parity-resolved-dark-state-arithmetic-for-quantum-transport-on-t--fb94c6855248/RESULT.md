# Parity-resolved dark-state arithmetic for quantum transport on three-path theta networks

## Finding

Let \(\Theta(L_1,L_2,L_3)\) be the simple theta graph made from three internally vertex-disjoint paths of integer edge lengths \(L_1,L_2,L_3\ge2\), meeting only at common terminals \(a,b\). Put uniform real hopping \(J\ne0\), equal onsite energies, and independent strictly positive irreversible capture rates at **both** terminals. The indefinitely surviving quantum subspace has an exact dimension determined solely by gcds and parities of the three path lengths.

For any tuple of integers \(\mathbf x=(x_1,\ldots,x_r)\) with \(r=2\) or \(3\), define \(g=\gcd(x_1,\ldots,x_r)\) and
\[
F(\mathbf x)=\begin{cases}
 g-1,&\text{if all }x_i/g\text{ have the same parity},\\
 \lfloor(g-1)/2\rfloor,&\text{otherwise}.
\end{cases}
\]
The dimension of the protected subspace is exactly
\[
\boxed{d_{\rm dark}=F(L_1,L_2)+F(L_1,L_3)+F(L_2,L_3)-F(L_1,L_2,L_3).}
\]
In particular, **every state is eventually captured** if and only if every pair of lengths has either gcd \(1\), or gcd \(2\) with residues \(0\) and \(2\) in some order modulo \(4\). Equivalently, persistent protection occurs if and only if at least one pair has gcd at least \(3\), or has gcd \(2\) and matching residues modulo \(4\).

There is also a complete site-resolved survival law. Write \(v_{i,j}\) for the internal site at distance \(j\) from terminal \(a\) on path \(i\), where \(1\le j<L_i\). For each \(1\le k<L_i\), put \(t=k/L_i\) and
\[
G_{i,k}=\{\ell\in\{1,2,3\}:tL_\ell\in\mathbb Z,\quad tL_\ell\equiv k\pmod2\}.
\]
Then the exact noncapture probability for a walker initially at \(v_{i,j}\) is
\[
\boxed{S_{i,j}=\frac2{L_i}\sum_{k=1}^{L_i-1}
\sin^2\!\left(\frac{\pi kj}{L_i}\right)
\left(1-\frac{L_i^{-1}}{\sum_{\ell\in G_{i,k}}L_\ell^{-1}}\right).}
\]
A walker initially at either absorbing terminal has noncapture probability zero. For an arbitrary normalized coherent initial state \(\psi\), the noncapture probability is \(\|P_{\rm dark}\psi\|^2\), with the projector constructed below. None of these eventual probabilities depends on the positive capture rates or the common nonzero hopping magnitude.

Examples: for lengths \((2,4,3)\), protection vanishes despite a nontrivial gcd between two paths. For lengths \((L,L,M)\) with \(\gcd(L,M)=1\), every internal site on either equal path has noncapture probability exactly \(1/2\), whereas the third path has noncapture probability zero. For three equal lengths \((L,L,L)\), the dimension is \(2(L-1)\), and every internal site has noncapture probability \(2/3\).

## Assumptions and scope

The Hilbert space is \(\mathbb C^{L_1+L_2+L_3-1}\), with its orthonormal vertex basis. The Hermitian coherent Hamiltonian is \(H=JA+\varepsilon I\), where \(A\) is the **adjacency** matrix (not the combinatorial Laplacian), \(J\in\mathbb R\setminus\{0\}\), and \(\varepsilon\in\mathbb R\). The no-capture evolution is \(\psi(t)=e^{-itH_{\rm eff}}\psi(0)\), with
\[
H_{\rm eff}=H-\frac i2\bigl(\gamma_a|a\rangle\langle a|+\gamma_b|b\rangle\langle b|\bigr),\qquad\gamma_a,\gamma_b>0.
\]
The total probability of never being captured is \(\lim_{t\to\infty}\|\psi(t)\|^2\). There are no additional loss channels, time-dependent perturbations, dephasing, or nonuniform hopping magnitudes. The paths have no shared internal vertices; their lengths count **edges**, not internal vertices. The result applies for all integers \(L_i\ge2\), including the smallest graph \(K_{2,3}\).

## Proof

**1. Identification of the protected subspace.** Set \(\Gamma=\gamma_a|a\rangle\langle a|+\gamma_b|b\rangle\langle b|\). Along the no-capture evolution,
\[
\frac{d}{dt}\|\psi(t)\|^2=-\langle\psi(t),\Gamma\psi(t)\rangle\le0.
\]
Any eigenvector of \(H_{\rm eff}\) with a real eigenvalue must have zero amplitudes at both terminals and must be an eigenvector of \(H\). Conversely, every \(H\)-eigenvector vanishing at both terminals is unaffected by \(\Gamma\) and remains loss-free. The span \(\mathcal D\) of all such eigenvectors reduces both \(H\) and \(\Gamma\). On its orthogonal complement all eigenvalues of the finite matrix \(H_{\rm eff}\) have strictly negative imaginary part: an eigenvalue with vanishing imaginary part would produce an additional eigenvector in \(\mathcal D\). Its semigroup therefore decays to zero even in the presence of Jordan blocks. Thus \(\lim_{t\to\infty}\|\psi(t)\|^2=\|P_{\mathcal D}\psi(0)\|^2\).

**2. Dirichlet modes on the three arms.** Shift by \(\varepsilon I\) and divide by \(J\). Since dark states vanish at terminals, their restriction to an internal path of length \(L_i\) is a Dirichlet standing wave. All possible frequencies have the unique form \(t\in(0,1)\cap\mathbb Q\), with \(tL_i=k_i\in\{1,\ldots,L_i-1\}\), and energy \(\varepsilon+2J\cos(\pi t)\). A normalized unit-arm mode is
\[
u_{i,t}(v_{i,j})=\sqrt{2/L_i}\sin(\pi tj),\qquad j=1,\ldots,L_i-1,
\]
and is zero on every other vertex. Distinct rational frequencies have distinct energies because cosine is injective on \((0,\pi)\).

**3. Boundary cancellation.** Fix \(t\) and let \(I_t=\{i:tL_i\in\mathbb Z\}\). The general interior eigenvector at this frequency is \(\sum_{i\in I_t}\beta_i u_{i,t}\). The eigenvalue equations at the zero-amplitude terminals are exactly
\[
\sum_{i\in I_t}c_i\beta_i=0,\qquad
\sum_{i\in I_t}(-1)^{k_i+1}c_i\beta_i=0,
\quad c_i=\sqrt{2/L_i}\sin(\pi t)>0.
\]
Adding and subtracting the equations separates the arms into two parity classes, by \(k_i\bmod2\). Each nonempty parity class must satisfy **one** independent weighted-sum-zero constraint. A class containing \(r\) arms contributes precisely \(r-1\) dark states. Its exact coefficient-space projector is \(I-cc^*/\|c\|^2\), where \(c=(c_i)\) ranges over that class. Summing these mutually orthogonal projectors over all frequencies and parity classes constructs \(P_{\mathcal D}\).

**4. Gcd formula.** For any collection of two or three arms with lengths \(x_1,\ldots,x_r\) and gcd \(g\), their shared frequencies are exactly \(t=h/g\), \(1\le h<g\). Their mode-number parities are those of \(h(x_i/g)\). If all reduced lengths have the same parity, every one of the \(g-1\) frequencies has matching parities. Otherwise only even \(h\) do, in number \(\lfloor(g-1)/2\rfloor\). This is exactly \(F(\mathbf x)\). At a fixed frequency, for at most three arms, the sum over parity classes of \((r-1)\) equals the number of compatible arm pairs minus one if all three are compatible. Hence the dimension equals the sum of the three pair-overlap counts minus the triple-overlap count, proving the boxed gcd formula.

A compatible pair exists exactly when there is a frequency on both paths whose two mode numbers have equal parity. If their gcd \(g\ge3\), such a frequency exists: either both reduced lengths are odd and any \(h\) works, or \(h=2\) works. If \(g=2\), the only shared frequency has \(h=1\), so compatibility holds precisely when the two reduced lengths are equally odd or equally even, equivalently when the two original lengths have the same residue modulo \(4\). If \(g=1\), no frequency is shared. These observations prove the stated if-and-only-if complete-capture criterion.

**5. Site-resolved formula.** For initial state \(|v_{i,j}\rangle\), the coefficient on the normalized arm mode \(u_{i,k/L_i}\) is \(\sqrt{2/L_i}\sin(\pi kj/L_i)\). The diagonal of the coefficient-space dark projector for its parity class is
\[
1-\frac{c_i^2}{\sum_{\ell\in G_{i,k}}c_\ell^2}
=1-\frac{L_i^{-1}}{\sum_{\ell\in G_{i,k}}L_\ell^{-1}}.
\]
Different frequencies are mutually orthogonal. Squaring and summing the projected coefficients yields the stated site law. The discrete sine basis identity \((2/L)\sum_{k=1}^{L-1}\sin^2(\pi kj/L)=1\) proves the two equal-arm and three equal-arm examples immediately. Terminal amplitudes vanish on every dark mode, giving zero terminal survival.

## Verification

The standalone program `verify_theta.py` checks all \(7^3=343\) ordered path-length triples in \(\{2,\ldots,8\}^3\). For each, it builds the complete adjacency Hamiltonian, independently diagonalizes it and finds the joint kernel of the two terminal evaluations in every eigenspace. It compares the resulting spectral projector with the formula's explicit orthogonal projector, checks idempotence and commutation, compares the exact closed gcd dimension, and checks the binary full-capture criterion. This covers 4116 internal vertex positions and 126 full-capture graphs. A separate program `check_dynamics.py` evaluates the actual non-Hermitian matrix exponential at long times for 28 graph/rate combinations using unequal positive loss rates, checking 282 localized survival probabilities. Both checks passed; the dynamics check is finite-time numerical corroboration, not an infinite-time proof.

Reproduce with `python verify_theta.py` and `python check_dynamics.py`, using Python 3 with NumPy and SciPy available. The proof is analytic for **every** permitted triple; finite computations only test it.

## Relationship to prior work

Caruso, Chin, Datta, Huelga and Plenio (arXiv:0901.4454, first public 2009-01-28) develop dark/invariant subspaces and analyze a fully connected dissipative network; their Appendix A.5 provides a general eigenbasis construction, but no three-path/two-terminal gcd-parity law. Le, Donati, Severini and Caruso (arXiv:1707.07482, first public 2017-07-24; published 2018), section 2.1, explicitly give sine eigenvectors of an isolated path and discuss path, complete-graph and cylindrical examples; the present terminal-pair cancellation and three-arm classification are not stated there. Razzoli, Paris and Bordone (arXiv:2011.13794, first public 2020-11-27; published 2021) treat the **Laplacian** Hamiltonian with a single trap on selected graph families, not the present two-terminal adjacency model.

The spectral-resonance observation uses standard discrete Dirichlet modes and the general dark-state framework; those are not claimed as new. The specific closed pair-minus-triple gcd formula, the exceptional gcd-two parity obstruction, and the site-resolved arbitrary-positive-rate theta-network law constitute the claimed result.

## Limitations

The theorem concerns eventually surviving probability, not short-time transfer efficiency or optimized mean absorption time. Nonuniform arm hoppings, unequal internal site energies, dephasing, interactions and additional absorbing vertices can change the classification. The originality comparison is evidence-based and not an exhaustive priority guarantee; equivalent results in unindexed graph-control, metric-quantum-graph, or spectral-theta literature may exist. No independent external scientific audit or formal certification is claimed.

## References

1. F. Caruso, A. W. Chin, A. Datta, S. F. Huelga and M. B. Plenio, *Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport*, arXiv:0901.4454 (2009), https://arxiv.org/abs/0901.4454.
2. T. P. Le, L. Donati, S. Severini and F. Caruso, *How to suppress dark states in quantum networks and bio-engineered structures*, J. Phys. A 51 (2018) 365306, arXiv:1707.07482, https://arxiv.org/abs/1707.07482.
3. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, Entropy 23 (2021) 85, arXiv:2011.13794, https://arxiv.org/abs/2011.13794.
