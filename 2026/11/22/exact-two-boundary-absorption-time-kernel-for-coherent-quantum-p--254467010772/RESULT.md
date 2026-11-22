# Exact two-boundary absorption-time kernel for coherent quantum paths

## Finding

For every integer \(N\ge2\), take a coherent nearest-neighbor quantum walk on the open path \(\{1,\ldots,N\}\), with hopping magnitude \(J>0\) and **equal Lindblad absorption rates** \(\kappa>0\) at both ends. Let \(A\) be the path adjacency matrix, let \(P=|1\rangle\langle1|+|N\rangle\langle N|\), and set
\[
K=\frac\kappa2P+\mathrm{i}JA,\qquad Q=\int_0^\infty e^{-K^\dagger t}e^{-Kt}\,dt.
\]
The integral is finite and positive definite. The following closed formula determines **all entries** of the integrated survival operator, including responses to arbitrary initial coherent superpositions. For \(1\le i\le j\le N\), put \(u=i\) and \(v=j\). Then
\[
\boxed{Q_{ij}=\begin{cases}
\displaystyle\frac{u(N+1-v)}{2\kappa}+\frac{\kappa(u-1)(N-v)}{8J^2},&j-i\text{ even},\\[5pt]
\displaystyle\frac{\mathrm{i}\,(N+1-u-v)}{4J},&j-i\text{ odd},
\end{cases}\qquad Q_{ji}=\overline{Q_{ij}}.}
\]
The symbol \(\mathrm{i}\) denotes the imaginary unit.

For a particle initially localized at site \(s\), the mean time until absorption at either boundary is exactly
\[
\boxed{T_{N,s}(\kappa)=\frac{s(N+1-s)}{2\kappa}+\frac{\kappa(s-1)(N-s)}{8J^2}.}
\]
For every interior starting site \(2\le s\le N-1\), this has exactly one positive minimizer,
\[
\boxed{\kappa^*_{N,s}=2J\sqrt{\frac{s(N+1-s)}{(s-1)(N-s)}},\qquad
T^*_{N,s}=\frac{\sqrt{s(N+1-s)(s-1)(N-s)}}{2J}.}
\]
At either absorbing endpoint \(s\in\{1,N\}\), \(T_{N,s}=N/(2\kappa)\) strictly decreases and has no finite optimizer. The interior optimal rate depends on both boundaries; for \(s/N\to\theta\in(0,1)\), it tends to \(2J\), whereas for fixed \(s\ge2\) and \(N\to\infty\) it tends to \(2J\sqrt{s/(s-1)}\). This is an exact finite-size boundary-interference law.

## Assumptions and scope

There is one excitation, uniform real nearest-neighbor hopping of magnitude \(J\), no onsite detuning, no bulk dissipation, no other decoherence, and precisely two independent, identical absorbing jump channels \(L_1=\sqrt\kappa|\emptyset\rangle\langle1|\), \(L_N=\sqrt\kappa|\emptyset\rangle\langle N|\). The vacuum is absorbing; \(\hbar=1\). The effective no-jump Hamiltonian is \(H_{\mathrm{eff}}=JA-\mathrm{i}\kappa P/2\), so the unnormalized surviving state evolves through \(e^{-Kt}\). The survival probability from a density matrix \(\rho\) is \(\operatorname{Tr}(e^{-Kt}\rho e^{-K^\dagger t})\), and its integrated value is \(\operatorname{Tr}(Q\rho)\). The theorem concerns the *sum* of the two absorption channels, not which end fires first. At \(N=2\), both sites are endpoints, and the same formulas hold. Neither zero loss nor zero hopping is included.

## Proof

**Step 1: absorption is certain.** The Hermitian part of \(K\) is \(\kappa P/2\ge0\); every eigenvalue has nonnegative real part. If an eigenvector had an eigenvalue on the imaginary axis, the associated quadratic-form equality would force its first and last coordinates to vanish. The first-row eigenvector equation then forces the second coordinate to vanish, and propagation along the connected tridiagonal chain forces every coordinate to vanish, a contradiction. Thus all eigenvalues of \(K\) have strictly positive real parts. Consequently \(e^{-Kt}\) decays exponentially; \(Q\) is positive definite and is the unique solution of the Lyapunov equation
\[
K^\dagger Q+QK=I.
\]
Its diagonal entries are mean absorption times by the survival-integral identity.

**Step 2: explicit kernel.** For \(1\le i,j\le N\), define three real matrices
\[
G_{ij}=\mathbf1_{i\equiv j\ ({\rm mod}\,2)}\min(i,j)[N+1-\max(i,j)],
\]
\[
B_{ij}=\mathbf1_{i\equiv j\ ({\rm mod}\,2)}[\min(i,j)-1][N-\max(i,j)],
\]
\[
C_{ij}=\mathbf1_{i\not\equiv j\ ({\rm mod}\,2)}\operatorname{sgn}(j-i)[N+1-i-j].
\]
These definitions give symmetric \(G,B\), skew-symmetric \(C\), and a zero first and last row and column for \(B\). Direct finite-difference identities, valid for every \(N\ge2\), are
\[
AG=GA,\qquad PB=BP=0,\qquad PC+CP=AB-BA,
\]
\[
PG+GP-(CA-AC)=4I.
\]
Here is an all-size verification of those identities. The ordinary Dirichlet Green kernel on \(N\) vertices is \(\min(i,j)[N+1-\max(i,j)]\), equal to \((N+1)(2I-A)^{-1}_{ij}\). Taking its same-parity part gives
\[
G=\frac{N+1}{2}[(2I-A)^{-1}+(2I+A)^{-1}],
\]
which commutes with \(A\). Likewise \(B\), on sites \(2,\ldots,N-1\), is the same-parity Dirichlet Green kernel of that shorter path and is zero at the endpoints. Therefore \(AB-BA\) is supported in endpoint rows and columns. There, for \(j\ge2\), its entries are \((AB-BA)_{1j}=B_{2j}\) and \((AB-BA)_{Nj}=B_{N-1,j}\), with opposite signs after transposition. These agree with \(PC+CP\) from the affine formula for \(C\). Finally, \((CA-AC)_{ij}=\sum_{k\sim j}C_{ik}-\sum_{k\sim i}C_{kj}\). For distinct interior indices, the two adjacent affine differences cancel; for an interior diagonal index it equals \(-4\), while at either endpoint diagonal it equals \(2(N-2)\). For distinct boundary entries it agrees with \((PG+GP)_{ij}\) (including opposite endpoints). Thus \(PG+GP-(CA-AC)=4I\) entrywise, with no appeal to a finite-size experiment. The \(N=2\) case follows from the same formulas or directly from \(P=I\).

Now set
\[
X=\frac{G}{2\kappa}+\frac{\kappa B}{8J^2}+\frac{\mathrm{i}C}{4J}.
\]
It is Hermitian and its entries are precisely those in the finding. Substituting \(K=\kappa P/2+\mathrm{i}JA\), and collecting the constant and \(\kappa/J\) terms, gives
\[
K^\dagger X+XK=\frac{PG+GP-(CA-AC)}4
+\frac{\mathrm{i}\kappa}{8J}[PC+CP-(AB-BA)]=I.
\]
Lyapunov uniqueness forces \(X=Q\), proving the kernel for **all lengths and all positive rates**.

**Step 3: optimization.** Substitution of \(i=j=s\) gives the displayed time. For interior \(s\) both coefficients in \(a/\kappa+b\kappa\) are strictly positive. Its second derivative is \(2a/\kappa^3>0\), and the unique stationary point is the stated positive square root. The minimum equals \(2\sqrt{ab}\). At either boundary \(b=0\); the time strictly decreases. The asymptotics follow directly by taking the indicated ratios, without interchanging the infinite-chain and long-time limits.

## Verification

The accompanying `verify.py` checks four exact integer matrix identities at all **338,349** index positions across lengths \(2\) through \(100\), without requiring external numerical packages. As an independent computational check, NumPy/SciPy Sylvester solves for **21** combinations of length, hopping and absorption rate reproduce the full complex kernel, including off-diagonal entries, with errors below \(2\cdot10^{-9}\). Execute `python3 verify.py`. These finite checks reinforce, but do not replace, the all-length algebraic proof.

## Relationship to prior work

Kassal and Aspuru-Guzik [1], first publicly posted January 25, 2012, analyze coherent exciton transport on finite uniform paths with **one localized trap**, uniform competing loss and optional dephasing. They develop rational finite-dimensional calculations of transfer efficiency rather than the two-terminal, loss-only integrated lifetime operator or its all-length optimizer. Razzoli, Paris and Bordone [2] use a **single trap** and classify eventual transport efficiencies; their conclusion explicitly leaves multiple traps and transfer times for further study. Riberi [3] studies an exact **semi-infinite, single-sink** Lindblad walk and likewise lists multiple absorbers and finite geometry as extensions. The complete finite **single-end** survival Gramian [4] has different boundary conditions and a length-independent localized-source optimum; its theorem does not imply this two-boundary kernel or the dependence on source distance from both ends. An indexed two-loss **infinite-line, fixed-energy scattering** theorem [5] optimizes absorption of incoming stationary flux, not the integrated lifetime of a localized excitation on a finite segment.

The standard Lindblad/no-jump and Lyapunov formulations are established methods; only the explicit two-end kernel, exact site-resolved optimum and boundary-scaling consequences are asserted as the substantive finding. The comparison establishes no claim of priority over every possible unindexed derivation.

## Limitations

The equal end-loss constraint and uniform hopping are essential to this formula. It does not classify unequal absorber rates, coherent-superposition optimal loss rates, additional sinks, finite-time quantum control, projective quantum measurements, or an infinite half-line. The result supplies average **total** capture times, not separate capture-channel probabilities or complete first-passage distributions. There may exist an earlier unindexed equivalent closed form in quantum transport or control-theoretic Gramian literature; the source survey is not a uniqueness certificate. No external independent scientific audit has been performed.

## References

1. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202v1, first posted 2012-01-25, https://arxiv.org/abs/1201.5202; *New Journal of Physics* **14** (2012), 053041.
2. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794v1, first posted 2020-11-27, https://arxiv.org/abs/2011.13794; *Entropy* **23** (2021), 85.
3. F. Riberi, *An Exactly Solvable Absorbing Quantum Walk*, arXiv:2605.08056v1, first posted 2026-05-08, https://arxiv.org/abs/2605.08056.
4. *Exact absorption-time Gramian and optimal sink strength on a finite quantum path*, published mathematical finding, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-absorption-time-gramian-and-optimal-sink-strength-on-a-fin--76980aefd4f5/RESULT.md.
5. *Exact parity dichotomy and uniquely optimal loss allocation for two absorbing lattice sites*, published mathematical finding, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-parity-dichotomy-and-uniquely-optimal-loss-allocation-for--64802ff320ee/RESULT.md.
