# A sharp linear reset-rate threshold for genuine GHZ entanglement under local depolarization

## Finding
For each integer \(n\geq3\), independent local qubit depolarization at rate \(\gamma>0\) together with common Poisson restoration of the \(n\)-qubit GHZ state at rate \(r>0\) has a unique stationary state. Its genuinely multipartite concurrence is exactly
\[
C_{\rm GM}(n,r,\gamma)=\max\{0,F_n(r/\gamma)\},
\qquad
F_n(\rho)=\frac{\rho}{\rho+n}-1+2^{1-n}\sum_{\substack{0\leq j\leq n\\j\ {\rm even}}}\binom nj\frac{\rho}{\rho+j}.
\]
The term at \(j=0\) is defined as \(1\) for \(\rho>0\). There is exactly one positive critical ratio \(\rho_n\), characterized by \(F_n(\rho_n)=0\), and the state is genuinely multipartite entangled if and only if \(r>\gamma\rho_n\). As \(n\to\infty\),
\[
\boxed{\rho_n=\frac{n}{\sqrt2}-\frac12+\frac{\sqrt2}{4}+O(n^{-1}).}
\]
For example, \(\rho_3=(\sqrt{73}-1)/4\) and \(\rho_4=\sqrt7\). The threshold refers to the **unconditioned stationary mixed state**, not to individual reset-conditioned trajectories, which have different entanglement diagnostics.

## Assumptions and scope
Write \(\lvert G_n\rangle=(\lvert0\rangle^{\otimes n}+\lvert1\rangle^{\otimes n})/\sqrt2\) and \(G_n=\lvert G_n\rangle\langle G_n\rvert\). Between resetting events, each site independently follows the depolarizing semigroup
\[
\mathcal D_t(A)=e^{-\gamma t}A+(1-e^{-\gamma t})\operatorname{tr}(A)I_2/2.
\]
A single independent Poisson clock of rate \(r\) replaces the full many-qubit state by \(G_n\) at each event. Both rates are constant and positive, and there is no coherent Hamiltonian, common environmental dephasing, partial reset, or measurement postselection. Genuine multipartite entanglement means *not representable as a convex mixture of states each separable across some nontrivial bipartition*. \(C_{\rm GM}\) is the usual convex-roof genuine multipartite concurrence, with \(C_{\rm GM}(G_n)=1\).

## Proof
**1. Stationary resolvent and matrix entries.** Since a Poisson reset erases the preceding state, the renewal identity and exponential contraction imply the unique stationary state
\[
\rho_*=r\int_0^\infty e^{-rt}\mathcal D_t^{\otimes n}(G_n)\,dt.
\]
Put \(z=e^{-\gamma t}\), \(u=(1+z)/2\), and \(v=(1-z)/2\). In the computational basis, the only off-diagonal entries are between the all-zero and all-one words, both equal to \(c=\frac12r/(r+n\gamma)\). Each binary word of Hamming weight \(k\) has diagonal value
\[
d_k=\frac r2\int_0^\infty e^{-rt}\big(u^{n-k}v^k+u^kv^{n-k}\big)\,dt,
\quad d_k=d_{n-k}.
\]
The endpoint populations are \(d_0=d_n\) and \(\sum_{k=0}^n\binom nkd_k=1\). All entries and their positivity follow from the completely positive channel integral.

**2. Exact genuine multipartite criterion.** The exact \(n\)-qubit X-state concurrence theorem [1], Eq. (13) and its appendix, applies here. For any nontrivial pair of complementary bitstrings the two corresponding populations equal each other. Since only the \((0^n,1^n)\) coherence is nonzero, the theorem reduces to
\[
C_{\rm GM}=2\max\Big\{0,c-\sum_{\{s,\bar s\}\ne\{0^n,1^n\}}d_{|s|}\Big\}
=\max\{0,2c+2d_0-1\}.
\]
This is an exact biseparability boundary, not an inference from negativity across individual cuts. In particular, for the biseparable side a constructive check is available: distribute the available pair populations across the \(2^{n-1}-1\) nontrivial complementary pairs, allocating coherence contributions \(c_s\in[0,d_{|s|}]\) with \(\sum c_s=c\); the inequality \(c\le\sum d_{|s|}\) ensures this. Since positivity of the original state gives \(d_0\ge c\), the corresponding four-word blocks with diagonal entries \(c_s,c_s,c_s,c_s\) and coherence \(c_s\) are separable under the bipartition indexed by \(s\) (they are two-qubit PPT blocks). Remaining diagonal entries are separable. This also verifies the zero-concurrence criterion directly.

**3. Rational threshold equation.** With \(\rho=r/\gamma\), the variable \(Z=e^{-\gamma T}\) for an independent stationary reset age \(T\sim\mathrm{Exp}(r)\) has density \(\rho z^{\rho-1}\), \(0<z<1\). Therefore
\[
2c+2d_0-1=\mathbb E\big[Z^n+((1+Z)/2)^n+((1-Z)/2)^n-1\big].
\]
Expanding the even powers and integrating \(\mathbb E Z^j=\rho/(\rho+j)\) gives exactly \(F_n(\rho)\). Define \(g_n(z)=z^n+((1+z)/2)^n+((1-z)/2)^n-1\). For \(0<z<1\),
\[
g_n'(z)=nz^{n-1}+\frac n2\left[((1+z)/2)^{n-1}-((1-z)/2)^{n-1}\right]>0.
\]
As \(\rho\) increases, \(Z=e^{-E/\rho}\) increases strictly for every \(E>0\), where \(E\sim\mathrm{Exp}(1)\). Hence \(F_n\) is strictly increasing and continuous, with \(F_n(0+)=2^{1-n}-1<0\) and \(F_n(\infty)=1\). The intermediate-value theorem proves existence and uniqueness of \(\rho_n\), and exactly characterizes all positive \(r\). Direct simplification yields
\[
F_3(\rho)=\frac{2\rho^2+\rho-9}{2(\rho+2)(\rho+3)},\qquad
F_4(\rho)=\frac{\rho^2-7}{(\rho+2)(\rho+4)}.
\]

**4. Sharp many-qubit threshold.** Put \(\rho=cn+d\), with \(c>0\) fixed and \(d\) bounded. Writing \(E\sim\mathrm{Exp}(1)\),
\[
F_n(\rho)=\mathbb E\left[e^{-nE/\rho}+\left(\frac{1+e^{-E/\rho}}2\right)^n+\left(\frac{1-e^{-E/\rho}}2\right)^n-1\right].
\]
The last positive term is at most \(2^{-n}\). Taylor expansion of \(\log[(1+e^{-x})/2]=-x/2+x^2/8+O(x^4)\), followed by exponentially weighted integration, gives uniformly for \(c\) on compact subintervals of \((0,\infty)\) and bounded \(d\):
\[
F_n(cn+d)=\frac c{c+1}+\frac{2c}{2c+1}-1
+\frac1n\left[\frac{d}{(c+1)^2}+\frac{2d}{(2c+1)^2}+\frac{2c}{(2c+1)^3}\right]+O(n^{-2}).
\]
The uniform remainder follows by splitting at \(E=K\log n\) with fixed sufficiently large \(K\): the Taylor remainder is bounded by an exponentially integrable polynomial in \(E\) on the first piece, while the second piece is \(O(n^{-K})\) by \(e^{-E}\) domination. The leading function is strictly increasing and vanishes exactly at \(c=1/\sqrt2\). Its derivative there is positive. Setting the \(n^{-1}\) coefficient to zero at this \(c\) gives \(d=-1/2+\sqrt2/4\). Strict monotonicity and the uniform expansion, with derivative of order \(1/n\) in \(\rho\), then yield \(\rho_n=cn+d+O(n^{-1})\).

## Verification
Run `python checker.py` using Python with SymPy and mpmath installed. The checker independently evaluates the stationary diagonal generator equations at rational rates, normalizes all populations exactly, compares the rational formula against direct Poisson-age quadrature, checks explicit small-size polynomials, numerically solves positive roots, and tests the two-term asymptotic. Its finite tests do not prove uniqueness or asymptotic error bounds; those follow from Steps 3–4. The checked numerical thresholds include \(\rho_3\approx1.886000936329383\) and \(\rho_4\approx2.645751311064591\).

## Relationship to prior work
The exact concurrence formula for arbitrary many-qubit X states is due to Hashemi Rafsanjani et al. [1], and is used rather than claimed here. Earlier work by Aolita et al. [2] studies scaling of GHZ entanglement without repeated collective restoration. Kulkarni and Majumdar [3] establish Poisson renewal averaging for quantum resetting, concentrating on closed unitary dynamics and a two-spin system. A different published amplitude-damping protocol with intermediate local NOT gates [4] treats a distinct noise mechanism. The present combined open-system GHZ problem gives a complete finite-size threshold and a two-term linear system-size asymptotic; the conclusion is specific to local depolarization plus full entangled-state resets and is not a blanket claim about arbitrary noise or resetting rules.

## Limitations
The resetting operation prepares an entangled many-qubit state and is therefore not an entanglement-generation protocol from separable local resources. The reset rate \(r\) and local depolarization rate \(\gamma\) are homogeneous, independent of qubit position. Entanglement across each bipartition alone is insufficient for this theorem; the stronger genuine multipartite criterion is used. Nothing is asserted about noisy reset fidelity, interactions between resets, dynamical Bell nonlocality, experimental implementation costs, or uniform finite-time error bounds. The novelty comparison is based on the inspected literature and search results; an undiscovered broader theorem could imply part of the result. Independent external scientific validation has not occurred.

## References
1. S. M. Hashemi Rafsanjani, M. Huber, C. J. Broadbent, and J. H. Eberly, “Genuinely Multipartite Concurrence of N-qubit X-matrices,” *Phys. Rev. A* **86**, 062303 (2012). https://arxiv.org/abs/1208.2706
2. L. Aolita, D. Cavalcanti, A. Acín, A. Salles, M. Tiersch, A. Buchleitner, and F. de Melo, “Scalability of GHZ and random-state entanglement in the presence of decoherence” (first posted 2008). https://arxiv.org/abs/0812.4203
3. M. Kulkarni and S. N. Majumdar, “Generating Entanglement by Quantum Resetting” (first posted 2023-07-14). https://arxiv.org/abs/2307.07485
4. “All-size entanglement-death thresholds for amplitude-damped GHZ states with intermediate partial NOT gates” (public research record, 2026-10-12). https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-all-size-entanglement-death-thresholds-for-amplitude-damped-ghz--f0bf2204cc39
