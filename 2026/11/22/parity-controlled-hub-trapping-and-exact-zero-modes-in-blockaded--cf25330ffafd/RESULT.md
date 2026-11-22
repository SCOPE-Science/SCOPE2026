# Parity-controlled hub trapping and exact zero modes in blockaded clique-windmill spin networks

## Finding
For integers \(m\ge1\) and \(r\ge2\), let \(G_{m,r}=K_1\vee\bigl(\bigsqcup_{a=1}^{m}K_r\bigr)\), with distinguished universal hub \(h\). On the Hilbert space spanned by the independent vertex subsets of \(G_{m,r}\), define the undetuned, unit-flip blockade Hamiltonian
\[
H|S\rangle=\sum_{x:\,S\triangle\{x\}\text{ is independent}}|S\triangle\{x\}\rangle.
\]
Let \(|h\rangle\) denote the basis state with only the hub excited, and let \(R_{m,r}(t)=|\langle h|e^{-itH}|h\rangle|^2\). Set
\[
T_{m,r}=[z^0](z+z^{-1}+r-1)^m
=\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!}{j!^2(m-2j)!}(r-1)^{m-2j}.
\]
Then \(\dim\ker H=T_{m,r}+1\) when \(m\) is odd and \(\dim\ker H=T_{m,r}-1\) when \(m\) is even. The vacuum-plus-hub component undergoes a sharp parity distinction:

For odd \(m\), define
\[
q_{m,r}=\frac1{r2^m}\sum_{j=0}^m\frac{\binom mj}{(m-2j)^2},\qquad w_{m,r}=\frac1{1+q_{m,r}}.
\]
The hub's zero-energy spectral weight is exactly \(w_{m,r}\), and for every real \(t\),
\[
R_{m,r}(t)\ge(2w_{m,r}-1)^2
=\left(\frac{1-q_{m,r}}{1+q_{m,r}}\right)^2,
\qquad \sqrt m\,q_{m,r}\longrightarrow \frac{\pi^{3/2}}{2\sqrt2\,r}
\quad(m\to\infty\text{ through odd integers}).
\]
In particular the hub return probability converges to one uniformly over all times as odd \(m\) grows.

For even \(m\), set
\[
p_m=\frac{\binom{m}{m/2}}{2^m},\quad
q^{\mathrm e}_{m,r}=\frac1{r2^m}\sum_{\substack{0\le j\le m\\j\ne m/2}}\frac{\binom mj}{(m-2j)^2},
\quad t_m=\frac{\pi}{2\sqrt{p_m}}.
\]
The hub's zero-energy spectral weight is zero, and
\[
R_{m,r}(t_m)\le4q^{\mathrm e}_{m,r},\qquad
\sqrt m\,q^{\mathrm e}_{m,r}\longrightarrow\frac{\pi^{3/2}}{6\sqrt2\,r}
\quad(m\to\infty\text{ through even integers}).
\]
Consequently \(R_{m,r}(t_m)\to0\) through even \(m\), while \(t_m\asymp m^{1/4}\). The two subsequences have incompatible coherent survival behavior in the same natural hub-initialized experiment.

## Assumptions and scope
All statements use finite simple graphs, perfect hard-neighbor blockade, real unit-amplitude single-site flips, zero on-site potential/detuning, \(\hbar=1\), and an initial localized hub excitation. There are \((r+1)^m\) independent subsets avoiding the hub (choose no excited site or exactly one of the \(r\) vertices in each peripheral clique), plus the hub-only configuration. Thus the constrained space has dimension \((r+1)^m+1\). The special case \(r=2\) is the friendship graph of \(m\) triangles. The return probability means probability of observing *exactly* the original hub-only configuration, not the mean hub occupation in an unconstrained thermal ensemble.

## Proof
**1. Exact block reduction.** Label each peripheral clique by local symbols \(0,1,\ldots,r\), where \(0\) means none excited. The peripheral basis is \((\mathbb C^{r+1})^{\otimes m}\). Its single-petal transition matrix \(L_r\) is the adjacency of the star \(K_{1,r}\); it has the spectrum \(\{\sqrt r,-\sqrt r,0^{[r-1]}\}\). Let \(|v\rangle=|0\rangle^{\otimes m}\) be the peripheral vacuum and \(A=\sum_{a=1}^m (L_r)_a\). The hub-only state flips only to the vacuum and vice versa, hence in the peripheral-plus-hub decomposition
\[
H=\begin{pmatrix}A&|v\rangle\\\langle v|&0\end{pmatrix}.
\]
Tensoring local eigenbases shows that the zero-eigenspace dimension of \(A\) is exactly the Laurent coefficient \(T_{m,r}\) stated above. Each local vacuum has squared projection \(1/2\) onto each of the two nonzero local eigenvectors and zero projection onto its \(r-1\) zero vectors. Therefore the spectral measure of \(A\) at \(|v\rangle\) places mass \(2^{-m}\binom mj\) on eigenvalue \((m-2j)\sqrt r\) for each \(0\le j\le m\).

**2. Kernel and hub spectral weight.** Let \(P_0\) project onto \(\ker A\), and let \(A^+\) be the Moore–Penrose inverse. The spectral measure gives
\[
\|P_0v\|^2=\begin{cases}0,&m\text{ odd},\\p_m,&m\text{ even},\end{cases}\qquad
\|A^+v\|^2=\begin{cases}q_{m,r},&m\text{ odd},\\q^{\mathrm e}_{m,r},&m\text{ even}.\end{cases}
\]
The excitation-parity involution anticommutes with \(A\) and fixes \(|v\rangle\), so \(\langle v,A^+v\rangle=0\). A zero vector of \(H\) with peripheral component \(x\) and hub amplitude \(a\) must satisfy \(Ax+av=0\) and \(\langle v,x\rangle=0\). If \(m\) is odd, \(P_0v=0\), and every zero vector is a sum of a free vector in \(\ker A\) and \(a(|h\rangle-A^+|v\rangle)\). This proves nullity \(T_{m,r}+1\), and the unique normalized zero vector that can overlap with \(|h\rangle\) has hub weight \(1/(1+q_{m,r})\). If \(m\) is even, \(P_0v\ne0\) forces \(a=0\); the remaining vectors are \(\ker A\cap v^\perp\), a codimension-one subspace of \(\ker A\). Thus nullity is \(T_{m,r}-1\) and the hub has no zero-energy weight.

**3. Uniform odd-parity return bound.** Decompose the hub state into its zero-mode projection of squared norm \(w\) and its orthogonal positive/negative energy part of squared norm \(1-w\). At all times its return amplitude is \(w\) plus a term of modulus at most \(1-w\). Because every nonzero \(|m-2j|\ge1\) for odd \(m\), one has \(q_{m,r}\le1/r<1\), so \(w>1/2\). The triangle inequality yields \(R_{m,r}(t)\ge(2w-1)^2\) for every real \(t\).

**4. Even-parity near-complete escape.** Write \(a=\sqrt{p_m}\), \(|z\rangle=P_0|v\rangle/a\) and \(|D\rangle=A^+|v\rangle\). These are normalized/orthogonal as required: \(\langle z,D\rangle=0\), \(\langle h,z\rangle=\langle h,D\rangle=0\), and \(\|D\|^2=q^{\mathrm e}_{m,r}\). Define \(|b\rangle=|h\rangle-|D\rangle\), so \(H|b\rangle=a|z\rangle\) and \(H|z\rangle=a(|b\rangle+|D\rangle)\). Introduce the explicitly computable approximate trajectory \(|u(t)\rangle=\cos(at)|b\rangle-i\sin(at)|z\rangle\). The initial error from \(|h\rangle\) has norm \(\|D\|\); the Schrödinger equation residual has norm \(a|\sin(at)|\,\|D\|\). Unitarity and Duhamel's estimate therefore give
\[
\|e^{-itH}|h\rangle-|u(t)\rangle\|
\le\left(1+\int_0^t a|\sin(as)|\,ds\right)\|D\|.
\]
At \(t_m=\pi/(2a)\), the integral equals \(1\) and \(|u(t_m)\rangle=-i|z\rangle\), orthogonal to \(|h\rangle\). It follows that the return amplitude is at most \(2\|D\|\), and \(R_{m,r}(t_m)\le4q^{\mathrm e}_{m,r}\).

**5. Asymptotic constants.** For fixed admissible integer \(k=m-2j\), the central binomial local limit gives \(\sqrt m\,2^{-m}\binom{m}{(m-k)/2}\to\sqrt{2/\pi}\), while the maximum binomial probability is bounded by \(C/\sqrt m\) uniformly in \(k\). Dominated convergence applies to the summable weights \(1/k^2\). For odd \(m\) sum over all nonzero odd \(k\), with \(\sum_{k\in2\mathbb Z+1}k^{-2}=\pi^2/4\); for even \(m\) sum over nonzero even \(k\), with \(\sum_{k\in2\mathbb Z\setminus\{0\}}k^{-2}=\pi^2/12\). Multiplication by \(\sqrt{2/\pi}/r\) yields both announced constants. Finally Stirling's formula gives \(p_m\sim\sqrt{2/(\pi m)}\), so \(t_m\asymp m^{1/4}\).

## Verification
The standalone program `verify.py` constructs the independent-set flip Hamiltonian directly from graph edges and full spin bitmasks, rather than using the tensor-product eigenbasis. It checks the exact modular rank and floating-point zero-mode count for \((r,m)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3)\), evaluates the hub's zero spectral weight independently, checks the even-time upper bounds and multiple odd-time lower bounds, and evaluates two large-size finite sums against their proved limits. These finite checks corroborate but do not replace the uniform all-size algebraic proof.

Reproduce with `python verify.py` in an environment with Python, NumPy and SciPy. Each pair of finite indices, the arithmetic formulas, and the expected tolerance are explicitly coded in the complete standalone verifier.

## Relationship to prior work
Lesanovsky's 2010 Rydberg-blockade analysis motivates the constrained spin-flip term on a one-dimensional lattice; it does not give the clique-windmill model. Buijsman's 2022 PXP zero-mode paper derives zero-mode counts/bounds for open and periodic chains using chiral and inversion symmetries, not exact kernel and hub-overlap formulas on clique windmills. Desaules and collaborators (2022) analyze hypergrid-like graph structures, including *two hypercubes sharing a vertex*, rather than a pendant vertex adjoining the vacuum corner of a Cartesian product of \(m\) stars. Zhao and collaborators (2023) show generally that projected spin flips are walks on the independent-set graph, which is the starting equivalence here; the new statements concern a particular infinite family, its exact nullity, and a parity-dependent all-time-versus-vanishing return contrast. Related published clique-windmill graph-spectrum and independent-set Walsh-convolution results address other matrices, not this PXP operator or observable. None of these general constructions alone supplies the displayed weight, Duhamel bound, or parity contrast without additional analysis.

## Limitations
The result is strictly about ideal coherent, undetuned finite-dimensional dynamics under the specified Hamiltonian, not generic dissipative or noisy Rydberg experiments. The hub return probability concerns a single configuration. No robustness bound against detuning, disordered flip rates, or long-range interactions is claimed; nor does an exponentially large zero-mode count alone imply scarring or thermal nonergodicity for arbitrary initial states. Historic priority may be affected by less-indexed work on pendant hypercubes or equivalent arrowhead Hamiltonians; no independent scientific audit has been performed.

## References
- I. Lesanovsky, *Many-body spin interactions and the ground state of a dense Rydberg lattice gas*, arXiv:1010.2349 (first posted 2010-10-12), https://arxiv.org/abs/1010.2349.
- W. Buijsman, *Number of zero-energy eigenstates in the PXP model*, arXiv:2203.09264 (first posted 2022-03-17), https://arxiv.org/abs/2203.09264.
- J.-Y. Desaules, K. Bull, A. Daniel and Z. Papić, *Hypergrid subgraphs and the origin of scarred quantum walks in many-body Hilbert space*, arXiv:2112.06885 (2021), https://arxiv.org/abs/2112.06885.
- X. Zhao et al., *Quantum Hamiltonian Algorithms for Maximum Independent Sets*, arXiv:2310.14546 (first posted 2023-10-23), https://arxiv.org/abs/2310.14546.
