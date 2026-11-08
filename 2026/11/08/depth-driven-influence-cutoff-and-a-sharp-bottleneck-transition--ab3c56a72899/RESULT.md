# Depth-driven influence cutoff and a sharp bottleneck transition in multiplex DeGroot chains

## Finding
A hierarchy of directed topic layers can have an exact, sharply delayed response to a source opinion although every layer performs instantaneous internal averaging and the full opinion matrix has a depth-independent subdominant eigenvalue. A single interlayer bridge of strength of order the inverse depth destroys that sharp relative-time cutoff.

Precisely, for each integer \(d\geq1\), consider \(d+1\) topic layers, each containing \(n\geq2\) agents. The final layer is a source and every preceding layer receives influence only from the next layer. For \(j\leq d\), let \(b_j\in(0,1)\), let \(W_j\) be any row-stochastic \(n\times n\) matrix with a positive diagonal, and set
\[
 X_j(t+1)=(1-b_j)W_jX_j(t)+b_jX_{j+1}(t),\qquad
 X_{d+1}(t+1)=W_{d+1}X_{d+1}(t).
\]
Take \(X_{d+1}(0)=\mathbf1\) and \(X_j(0)=\mathbf0\) for \(j\leq d\). All agents on layer \(j\) then retain the same opinion, and the opinion \(u_d(t)\) on the first layer is exactly
\[
 \boxed{u_d(t)=\Pr\!\left\{G_1+\cdots+G_d\leq t\right\}},
 \qquad \Pr(G_j=k)=b_j(1-b_j)^{k-1}\quad (k=1,2,\ldots),
\]
for independent geometric waiting times. Consequently the response time has mean and variance
\[
 \mu_d=\sum_{j=1}^{d}\frac1{b_j},\qquad
 \sigma_d^2=\sum_{j=1}^{d}\frac{1-b_j}{b_j^2}.
\]
These formulas do not depend on the internal social network matrices.

When \(b_j=b\in(0,1)\) for every \(j\),
\[
 \boxed{u_d(t)=\Pr\{\operatorname{Bin}(t,b)\geq d\}},
\]
and, writing \(\Phi\) for the standard normal distribution function, for every fixed real \(s\),
\[
 \boxed{u_d\!\left(\left\lfloor\frac d b+s\frac{\sqrt{d(1-b)}}b\right\rfloor\right)\longrightarrow\Phi(s)}
 \quad\text{as }d\to\infty.
\]
The transition from near-zero to near-one opinion takes place around \(d/b\), within a window of order \(\sqrt d\). It persists more generally for triangular arrays with \(b_{j,d}\in[c,C]\subset(0,1)\), on the mean/standard-deviation scales \(\mu_d,\sigma_d\).

The fixed-gap obstruction is explicit: choosing every \(W_j=\mathbf1\mathbf1^\top/n\), the \(n(d+1)\times n(d+1)\) multiplex opinion matrix has characteristic polynomial
\[
 z^{(d+1)(n-1)}(z-1)(z-(1-b))^{d}.
\]
Its nontrivial spectral radius is the same \(1-b\) for every depth, but for each \(0<\eta<1\), the first-layer opinion at time \(\lfloor (1-\eta)d/b\rfloor\) tends to zero, and at time \(\lfloor (1+\eta)d/b\rfloor\) tends to one. Thus there is no depth-uniform relaxation estimate from the nontrivial spectral radius alone; the repeated nonnormal eigenvalue matters.

There is a sharp bottleneck scale. Fix \(b\in(0,1)\), let \(b_{2,d}=\cdots=b_{d,d}=b\), and choose an arbitrary \(b_{1,d}\in(0,1)\). The *relative-time response cutoff* defined by
\[
 \frac{G_{1,d}+\cdots+G_{d,d}}{\mathbb E(G_{1,d}+\cdots+G_{d,d})}\xrightarrow{\Pr}1
\]
occurs **if and only if** \(d b_{1,d}\to\infty\). At the critical bridge scale \(b_{1,d}=\kappa/d\), with fixed \(\kappa>0\) and \(d>\kappa\), the profile is no longer a step:
\[
 \boxed{u_d(\lfloor sd\rfloor)\longrightarrow
 \begin{cases}0,&s\leq1/b,\\1-e^{-\kappa(s-1/b)},&s>1/b.\end{cases}}
\]
For \(d b_{1,d}\to0\), the rescaled delay \(b_{1,d}(G_{1,d}+\cdots+G_{d,d})\) instead converges in distribution to an exponential random variable of mean one. The critical scale is therefore a genuine transition between a depth-averaged nearly deterministic response and a macroscopic waiting-time distribution.

## Assumptions and scope
The system is discrete-time, finite-dimensional, nonnegative, synchronous and row-stochastic. Each individual updates on every topic according to the same scalar interlayer coefficient \(b_j\), though the within-layer stochastic matrices may differ freely. All opinion values are in \([0,1]\). Every layer has an allowed positive self-edge; the special all-to-all averaging matrices are primitive and strictly positive. The source layer is initially unanimous at one and other layers are initially unanimous at zero; this deliberately isolates **inter-topic propagation** rather than arbitrary initial intra-topic disagreement. The depth limit varies the number of topics, not the number of individuals. The critical bottleneck asymptotics assume the one exceptional rate is the first rate, with all others fixed at \(b\).

The relative cutoff is defined here as concentration of the response hitting-time distribution at its own mean. It is not an assertion about total-variation mixing of an irreducible Markov chain. The geometric variables are a representation of deterministic expectation weights, not a claim that the original opinion update randomly samples a topic.

## Proof
**Uniform-layer reduction.** Every row-stochastic matrix obeys \(W_j\mathbf1=\mathbf1\). Inductively, the prescribed initial state remains in the subspace where opinions are uniform across agents within each layer. The scalar recursion is
\[
 u_j(t+1)=(1-b_j)u_j(t)+b_ju_{j+1}(t),\quad u_{d+1}(t)=1,\quad u_j(0)=0\ (j\leq d).
\]
Define a stochastic chain on topic indices \(1,\ldots,d+1\) that stays at index \(j\leq d\) with probability \(1-b_j\), advances to \(j+1\) with probability \(b_j\), and absorbs at \(d+1\). The recursion is exactly the backward equation for its probability of absorption by time \(t\). The independent geometric waiting times spent at successive indices have the displayed laws by the strong Markov property. This proves the exact identity, mean and variance.

**Constant bridge strength.** Couple the chain to independent Bernoulli\((b)\) indicators for advances at each clock tick until absorption. Absorption by time \(t\) occurs precisely when at least \(d\) indicators succeed. For \(t_d(s)=\lfloor d/b+s\sqrt{d(1-b)}/b\rfloor\), the binomial mean equals \(d+s\sqrt{d(1-b)}+O(1)\) and its standard deviation is \(\sqrt{d(1-b)}(1+o(1))\). The classical binomial central limit theorem gives \(u_d(t_d(s))\to\Phi(s)\). The law of large numbers at \(t=\lfloor(1\pm\eta)d/b\rfloor\) gives the two-sided depth-delay assertion.

**Heterogeneous bounded strengths.** For \(b_{j,d}\in[c,C]\subset(0,1)\), all centered geometric waiting times have uniformly bounded absolute third moments; also \(\sigma_d^2\) is bounded above and below by positive constant multiples of \(d\). Lyapunov's central limit theorem therefore applies to their sum and gives \(u_d(\lfloor\mu_d+s\sigma_d\rfloor)\to\Phi(s)\). In particular \(\sigma_d/\mu_d\to0\).

**Depth-independent eigenvalues.** Set \(W_j=\mathbf1\mathbf1^\top/n\). The full influence matrix is upper block triangular. Its first \(d\) diagonal blocks are \((1-b)W_j\), the final diagonal block is \(W_{d+1}\), and the superdiagonal blocks are \(bI_n\). Each \(W_j\) has eigenvalues \(1,0,\ldots,0\). The characteristic polynomial is thus the product stated above. For constant \(b\), the uniform-layer subspace contains a size-\(d\) Jordan block with eigenvalue \(1-b\), explaining why the eigenvalue modulus alone does not control response across growing depths.

**One weak bridge and necessity/sufficiency.** Put \(H_d=\sum_{j=2}^{d}G_{j,d}\). For fixed \(b\), \(H_d/d\to1/b\) in probability by the law of large numbers, and it is independent of \(G_{1,d}\). If \(d b_{1,d}\to\infty\), then \(\mathbb E G_{1,d}/d=1/(d b_{1,d})\to0\); Markov's inequality shows \(G_{1,d}/d\to0\), and the total response time divided by its mean converges in probability to one. Conversely, if \(d b_{1,d}\) does not diverge, choose a subsequence along which it tends to \(\lambda\in[0,\infty)\). If \(\lambda>0\), then \(G_{1,d}/d\) tends in distribution to an exponential law with rate \(\lambda\) and the total response time divided by its mean has a non-degenerate shifted exponential limit. If \(\lambda=0\), the identity \(\Pr(b_{1,d}G_{1,d}>s)=(1-b_{1,d})^{\lfloor s/b_{1,d}\rfloor}\to e^{-s}\), together with \(b_{1,d}H_d\to0\) in probability, shows that the ratio to the mean tends to a mean-one exponential law. Neither subsequence concentrates at one. This proves the 'if and only if' cutoff criterion, the critical-scale profile, and the slower bottleneck limit.

## Verification
The standalone file `check.py` independently evaluates the deterministic multiplex recursion in exact rational arithmetic and compares it with a direct convolution of independent geometric waiting times for multiple population sizes, chain depths, bridge strengths, and internal averaging matrices. It also separately checks the binomial-tail formula in the homogeneous case. The commands and expected output are in `VERIFICATION.md`. The computations are finite consistency tests, not substitutes for the general probabilistic proofs or the asymptotic theorems.

## Relationship to prior work
Zender, Shi, Hickok, Chu and Porter (2026) introduced the acyclic interlayer multiplex DeGroot update and proved convergence and formulas for eventual opinions. Their source-layer limit theorem does not itself quantify the time at which information traverses a growing hierarchy. The result here supplies the exact transient law, a central-limit response window, the fixed-eigenvalue delayed-response obstruction, and a sharp one-bridge bottleneck threshold for a canonical chain specialization. The finite-state absorption representation and geometric and binomial limit theorems use classical probability, which is not asserted to be new.

Earlier studies of DeGroot convergence times, including network-community spectral approaches and asynchronous updates, study different geometries or clock rules; they do not explicitly give this joint hierarchy-depth/bottleneck profile. The negative-binomial approximation in a 2020 paper on directed hierarchical social influence concerns stochastic majority-rule propagation rather than the synchronous averaging law here. More general birth-and-death-chain cutoff theorems address Markov-chain mixing or separation under other assumptions, and supply background, not a specific result about these deterministic multiplex opinions. These comparisons are not proof that no equivalent unindexed specialization exists.

## Limitations
Uniform initial opinions within each layer are essential for network-topology independence of the entire transient profile. The full model with arbitrary within-layer initial polarization generally has additional decaying modes. The result does not bound convergence times uniformly for arbitrary directed acyclic interlayer graphs, does not cover state-dependent or signed influence, and does not claim standard irreducible-chain mixing cutoff. The Gaussian scaling requires uniformly nondegenerate bridge strengths, while the bottleneck formula assumes exactly one weak bridge and fixed remaining strengths. No independent mathematical audit has been performed.

## References
1. M. Zender, K. Shi, A. Hickok, W. Chu, and M. A. Porter, *DeGroot Dynamics on Multiplex Networks with Directed and Acyclic Interlayer Connectivities*, arXiv:2610.27198v1, first submitted 19 October 2026, https://arxiv.org/abs/2610.27198 .
2. *The Impact of Community Structure on the Convergence Time of Opinion Dynamics*, 2017, https://doi.org/10.1155/2017/9396824 .
3. *The asynchronous DeGroot dynamics*, Random Structures & Algorithms (2024), https://doi.org/10.1002/rsa.21248 .
4. *Organisational Social Influence on Directed Hierarchical Graphs, from Tyranny to Anarchy*, Scientific Reports (2020), https://www.nature.com/articles/s41598-020-61196-8 .
5. P. Diaconis and L. Saloff-Coste, *Separation cut-offs for birth and death chains*, arXiv:math/0702411 (2007), https://arxiv.org/abs/math/0702411 .
