# Exact stationary cut-entanglement statistics for all-to-all Bell measurements

## Finding
Consider the measurement-only Bell-pair matching process specified below. For **every** integer \(N\ge4\), single-site measurement probability \(0<p<1\), and subsystem \(A\) of size \(1\le a<N\), the chain of pairings is reversible with the **unique** stationary law
\[
\mathbb P_*(M)=\frac{w_N^{|M|}}{Z_N(w_N)},\qquad
w_N=\frac{1-p}{p(N-1)},\qquad
Z_n(w)=\sum_{k=0}^{\lfloor n/2\rfloor}
\frac{n!}{(n-2k)!\,2^k k!}w^k.
\]
Here \(M\) is any partial matching of the \(N\) labeled sites and \(|M|\) is its number of edges; \(Z_0(w)=1\).

Let \(S_A\) denote the entropy of \(A\) in **bits** (the number of Bell pairs with one endpoint in \(A\) and one in its complement). Put \(b=N-a\). Its **entire finite-size stationary probability law** is fixed by the polynomial
\[
\boxed{\mathbb E_*z^{S_A}=\frac{1}{Z_N(w_N)}
\sum_{j=0}^{\min(a,b)}\frac{(a)_j(b)_j}{j!}
[w_N(z-1)]^j Z_{N-2j}(w_N).}
\]
The falling factorial is \((m)_j=m(m-1)\cdots(m-j+1)\), with \((m)_0=1\). Equivalently, for every integer \(0\le j\le\min(a,b)\),
\[
\mathbb E_* (S_A)_j=(a)_j(b)_j w_N^j\frac{Z_{N-2j}(w_N)}{Z_N(w_N)}.
\]
In particular, the finite-size mean and variance are exactly
\[
\begin{split}
\mu_{N,a}&=ab w_N\frac{Z_{N-2}(w_N)}{Z_N(w_N)},\\
\operatorname{Var}_*(S_A)&=\mu_{N,a}+(a)_2(b)_2w_N^2
\frac{Z_{N-4}(w_N)}{Z_N(w_N)}-\mu_{N,a}^2.
\end{split}
\]

There is also a **sharp partition-dependent thermodynamic fluctuation law**. Hold \(p\in(0,1)\) fixed, let \(N\to\infty\), and take any sequence \(a=a_N\) with \(a_N/N\to\theta\in(0,1)\). Define \(c=(1-p)/p\), the unique \(u\in(0,1)\) solving \(u+cu^2=1\), and \(\rho=1-u\), \(h=\theta(1-\theta)\). Then
\[
\boxed{\lim_{N\to\infty}\frac{\mathbb E_*S_A}{N}=\rho h,\qquad
\lim_{N\to\infty}\frac{\operatorname{Var}_*(S_A)}{N}
=V(p,\theta)=\frac{h\rho}{2-u}
[u+2\theta\rho][u+2(1-\theta)\rho].}
\]
Consequently the ratio of stationary entropy variance to its mean obeys
\[
\boxed{\lim_{N\to\infty}\frac{\operatorname{Var}_*(S_A)}{\mathbb E_*S_A}
=u+\frac{4\theta(1-\theta)\rho^2}{2-u}
\le \frac{1}{2-u}<1.}
\]
The upper bound is attained **exactly** at the equal-half fraction \(\theta=1/2\). Thus all macroscopic bipartitions exhibit asymptotically sub-Poisson entropy-count fluctuations, with an exact squeezing coefficient. This is a statement about stationary trajectory-to-trajectory entanglement, not the mixed-state entropy of the outcome-averaged density matrix.

## Assumptions and scope
At each discrete time step, with probability \(p\), uniformly choose one of \(N\) sites and measure it in the computational basis. If it belongs to a Bell pair, its pair is destroyed. With probability \(1-p\), uniformly choose one **unordered pair** of distinct sites and make a complete Bell-basis measurement of that pair. The resulting pure state is a tensor product of Bell pairs and computational-basis unpaired states, as established for this protocol in Holdhusen--McAmis--Rahmani (2026). A Bell measurement creates an edge when both selected sites are unpaired, moves an edge when one is already paired, swaps the other partners when both are in different pairs, and leaves the matching unchanged when the measured sites were paired to each other. The measurement outcomes affect Bell labels, not this matching or its subsystem entropies. The initial state may be any state in that matching family. Uniform selection corresponds to the original model's spatial-exponent-zero limit. No conclusion is claimed for spatially biased selection, arbitrary initial entangled states, or \(p=0\) and \(p=1\).

## Proof
**1. Reversibility and uniqueness.** Write \(q=(1-p)/\binom N2\) for the probability of selecting any particular unordered Bell-measurement pair. In the matching graph, addition of a specified edge between two monomers occurs with transition probability \(q\). Its reverse, removal of that edge by a one-site measurement at either endpoint, occurs with transition probability \(2p/N\). Their ratio is \(q/(2p/N)=w_N\). Other nontrivial transitions preserve the number of edges: moving an edge by choosing a monomer and a paired endpoint has exactly one reverse pair selection of equal probability \(q\); swapping the endpoints of two separate pairs has exactly two selections in each direction, hence equal aggregate probability \(2q\). All other selections are self-transitions. Therefore detailed balance holds under \(\mathbb P_*(M)\propto w_N^{|M|}\) for every pair of states. The coefficient of \(w^k\) in \(Z_N\) counts the \(N!/[(N-2k)!2^k k!]\) partial matchings with \(k\) edges, verifying normalization. With \(0<p<1\), every matching can reach the empty matching by sequential single-site measurements, and every matching can be formed from the empty one by sequential two-monomer Bell measurements. Finite irreducibility yields the unique stationary law.

**2. Exact cut statistics.** Select an **ordered list** of \(j\) distinct cross-cut edges. There are \((a)_j(b)_j\) such lists. Every fixed collection of the \(j\) edges occupies \(2j\) vertices, has Gibbs weight \(w_N^j\), and leaves an unrestricted partial matching on the other \(N-2j\) vertices, with partition function \(Z_{N-2j}\). Summing the indicators of all ordered distinct cross-cut edges gives the falling-factorial moment formula. Expanding \(z^{S_A}=[1+(z-1)]^{S_A}\) gives the claimed polynomial, whose coefficients determine the full law. The \(j=1,2\) cases give the displayed finite-size mean and variance.

**3. Total-pair saddle.** Let \(K=|M|\). Its exact law is
\[
\mathbb P_*(K=k)=\frac{N!\,w_N^k}{(N-2k)!2^k k!\,Z_N(w_N)}.
\]
Set \(x=k/N\) and \(w_N=c/(N-1)\). Uniform Stirling estimates on compact subsets of \(0<x<1/2\) give log-weight \(Nf(x)+O(\log N)\), where
\[
f(x)=-(1-2x)\log(1-2x)-x\log(2x)+x\log c-x.
\]
We have \(f'(x)=\log[c(1-2x)^2/(2x)]\) and \(f''(x)=-4/(1-2x)-1/x<0\). The unique maximizer is \(x_*=(1-u)/2=\rho/2\). Strict concavity gives exponentially small weight outside any fixed neighborhood of \(x_*\); Stirling's local quadratic expansion and Gaussian-sum estimates, including exponentially bounded tails, yield
\[
\frac{\mathbb E_*K}{N}\to\frac\rho2,
\qquad
\frac{\operatorname{Var}_*(K)}{N}\to
v=\frac{1}{-f''(x_*)}=\frac{\rho u}{2(2-u)}.
\]
This is a direct finite-sum Laplace argument, not an inference from numerical convergence or an unproved independent-site approximation.

**4. Cut variance.** Conditioned on \(K=k\), the matching is uniformly drawn from all \(k\)-edge matchings. Define
\[
q_N=\frac{2ab}{N(N-1)},\quad
r_N=\frac{4a(a-1)b(b-1)}{N(N-1)(N-2)(N-3)}.
\]
The conditional factorial moments satisfy \(\mathbb E[S_A\mid K]=q_NK\) and \(\mathbb E[(S_A)_2\mid K]=r_NK(K-1)\), giving exactly
\[
\operatorname{Var}_*(S_A)=(q_N-r_N)\mathbb E_*K+(r_N-q_N^2)(\mathbb E_*K)^2+r_N\operatorname{Var}_*(K).
\]
With \(a/N\to\theta\), \(q_N\to2h\), \(r_N\to4h^2\), and
\[
N(r_N-q_N^2)\to-4h(2\theta-1)^2.
\]
Substituting the two saddle limits and simplifying yields \(V(p,\theta)\). Division by the positive mean limit gives the Fano expression. Since \(4\theta(1-\theta)\le1\), and
\[
u+\frac{(1-u)^2}{2-u}=\frac1{2-u}<1,
\]
the sharp sub-Poisson statement follows. Equality in the partition-fraction bound holds only when \(\theta=1/2\).

## Verification
The included Python 3 standard-library program `verify.py` enumerates every partial matching for \(4\le N\le8\), forms the actual one-site and Bell-measurement transition kernels at three exact-rational choices of \(p\), and tests detailed balance, stationarity, all factorial moments, and the full probability-generating polynomial for every nontrivial cut. It additionally sums the independent total-pair distribution for \(N=1000,3000,6000\) and compares the mean and variance coefficients at several probabilities and block fractions. Running `python verify.py` gave **74,636 passing deterministic assertions**. These checks are finite supporting evidence; the infinite-size result follows from the saddle proof above.

## Relationship to prior work
Holdhusen, McAmis and Rahmani (arXiv:2609.28743v1, publicly submitted 2026-09-23) introduce the matching automaton, the outcome-independent Bell-pair entropies, and the \(\alpha=0\) mean-field evolution and leading entropy mean. Their supplemental combinatorial calculation samples uniform pairings conditional on occupied sites and employs an independent-site approximation for the occupied-site counts; it does not state the exact finite-size reversible law, the stationary complete cut-entanglement counting polynomial, or the derived fluctuation coefficient. The present proof independently identifies the **exact** Gibbs measure of the discrete stochastic dynamics rather than treating its correlations as negligible.

The monomer--dimer Gibbs ensemble and its partition-function methods are established prior mathematical physics: Heilmann--Lieb (1972), Alberici--Contucci--Fedele--Mingione (2015/2016) and Chen (2015/2016) investigate general matching measures and monomer-density fluctuations. These works cover, by specialization, aspects of the **total number of dimers** once the Gibbs identification is made. They are not claimed to be new here. The proposed advance is the invariant-measure identification for this measurement-only quantum matching process together with its **full cut-entanglement distribution**, its exact macroscopic variance and sharp partition-dependent sub-Poisson bound. Zhu (arXiv:2605.25845, 2026-05-25) studies a different long-range measurement-only circuit with competing two- and three-qubit measurements; that model does not supply this matching stationary law.

## Limitations
This result is specific to uniform pair selection and positive probabilities for both measurement mechanisms. It is about the classical matching projection of the quantum trajectories, not the full Bell-label dynamics. The large-size limits require fixed \(p\in(0,1)\) and a nondegenerate cut fraction \(0<\theta<1\); no uniformity at \(p\to0,1\) is claimed. A general known theorem about equilibrium matching models may provide an alternative proof of some counting and asymptotic formulas once their applicability is established; the precise prior coverage of the physical matching dynamics and full cut-statistics remains a publication-priority risk. The proof does not assert a central limit theorem for cut entropy, a spectral gap, or dynamical concentration rates.

## References
1. W. Holdhusen, B. M. McAmis, A. Rahmani, *Classical Cellular Automaton for Measurement-Only Entanglement Transitions*, arXiv:2609.28743v1 (2026-09-23), https://arxiv.org/abs/2609.28743 .
2. O. J. Heilmann, E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics **25** (1972), 190--232, https://doi.org/10.1007/BF01877590 .
3. D. Alberici, P. Contucci, M. Fedele, E. Mingione, *Limit theorems for monomer-dimer mean-field models with attractive potential*, Communications in Mathematical Physics **346** (2016), 781--799, arXiv:1506.04241.
4. W.-K. Chen, *Limit theorems in the imitative monomer-dimer mean-field model via Stein's method*, Journal of Mathematical Physics **57** (2016), 083302, arXiv:1506.08484.
5. W.-K. Lam, A. Sen, *Central limit theorem in disordered monomer-dimer model*, Random Structures & Algorithms **66** (2025), https://doi.org/10.1002/rsa.21256 (first online 2024-08-07).
6. B. Zhu, *Steady-state phases in long-range measurement-only quantum circuits*, arXiv:2605.25845 (2026-05-25), https://arxiv.org/abs/2605.25845 .
