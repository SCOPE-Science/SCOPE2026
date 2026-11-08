# Exact absorption-time Gramian and optimal sink strength on a finite quantum path

## Finding

Let \(N\ge2\) be an integer, and let the coherent hopping frequency \(\Omega>0\) and boundary absorption rate \(\kappa>0\) be arbitrary. On the \(N\)-site open path, take the hopping Hamiltonian and Lindblad absorber
\[
H=\Omega I-\frac{\Omega}{2}\sum_{j=1}^{N-1}(|j\rangle\langle j+1|+|j+1\rangle\langle j|),
\qquad L=\sqrt\kappa\,|\emptyset\rangle\langle1|.
\]
The effective Hamiltonian on the surviving walker sector is \(H_{\mathrm{eff}}=H-i\kappa|1\rangle\langle1|/2\). Its **integrated survival operator**
\[
Q=\int_0^\infty e^{iH_{\mathrm{eff}}^\dagger t}e^{-iH_{\mathrm{eff}}t}\,dt
\]
has the following exact matrix, valid at every length, site pair and positive absorption rate. For \(1\le a\le b\le N\),
\[
Q_{ab}=\begin{cases}
(N-b+1)\left(\dfrac a\kappa+\dfrac{(a-1)\kappa}{\Omega^2}\right),& b-a\text{ even},\\[3pt]
-\dfrac{i(N-b+1)}{\Omega},&b-a\text{ odd},
\end{cases}\qquad Q_{ba}=\overline{Q_{ab}}.
\]
Every initial state is eventually absorbed with probability one. For a walker initially at site \(j\), its exact mean absorption time is
\[
\boxed{\mathbb E_j T=(N-j+1)\left(\frac j\kappa+\frac{(j-1)\kappa}{\Omega^2}\right).}
\]
For every \(2\le j\le N\), the **unique** positive absorption-rate minimizer is
\[
\boxed{\kappa_j^*=\Omega\sqrt{\frac j{j-1}},\qquad
\min_{\kappa>0}\mathbb E_j T=\frac{2(N-j+1)\sqrt{j(j-1)}}{\Omega}.}
\]
The optimal rate is independent of the total chain length. At the absorber itself \(j=1\), the lifetime is \(N/\kappa\) and is strictly decreasing, with no finite positive minimizer.

In particular, at optimal rate the far-end starting position \(j=N\) has a linear \(2\sqrt{N(N-1)}/\Omega\) absorption time, whereas any sequence of bulk positions with \(j/N\to\theta\in(0,1)\) has the quadratic asymptotic \(2\theta(1-\theta)N^2/\Omega\). For a uniformly mixed initial site the exact mean and optimal rate are
\[
\overline T_N=\frac{(N+1)(N+2)}{6\kappa}+\frac{(N^2-1)\kappa}{6\Omega^2},\qquad
\overline\kappa_N^*=\Omega\sqrt{\frac{N+2}{N-1}}.
\]

## Assumptions and scope

The walker occupies precisely the finite path \(\{1,\ldots,N\}\). The endpoints are reflecting for coherent hopping, except that the leftmost site is connected to an absorbing vacuum state through the specified Markovian Lindblad jump. There are no bulk losses, onsite detunings, additional dephasing, traps, gain, hopping disorder, or resets. The sole adjustable rate is \(\kappa\), with \(N,j,\Omega\) fixed. The definition of arrival is loss through that physical sink, not repeated projective position measurement. Units are chosen so that \(\hbar=1\); the uniform onsite term in \(H\) only supplies a global phase.

An arbitrary initial normalized pure state \(|\psi\rangle\) has mean absorption time \(\langle\psi|Q|\psi\rangle\); for an initial density matrix \(\rho\), it is \(\operatorname{tr}(Q\rho)\). The explicit site-local optimum is not claimed to minimize these times for all coherent superpositions simultaneously.

## Proof

Set \(B=\sum_{j=1}^{N-1}(|j\rangle\langle j+1|+|j+1\rangle\langle j|)\), \(P=|1\rangle\langle1|\), and discard the scalar onsite term. The no-jump generator is
\[
A=\frac{i\Omega}{2}B-\frac\kappa2 P.
\]
Since \(\operatorname{Re}\langle v,Av\rangle=-\kappa|v_1|^2/2\), every eigenvalue lies in the closed left half-plane. An eigenvector with an imaginary-axis eigenvalue must satisfy \(v_1=0\); the first-row eigenvector equation then forces \(v_2=0\), and inductively the tridiagonal equations force all other entries to vanish. Thus every eigenvalue has strictly negative real part. Consequently the integral \(Q=\int_0^\infty e^{A^\dagger t}e^{At}\,dt\) converges, is positive definite, and is the unique solution of the Lyapunov equation
\[
A^\dagger Q+QA=-I.
\]

For completeness, verify the proposed matrix by substitution rather than by a finite-dimensional enumeration. Put \(\ell_b=N-b+1\), \(F_a=a/\kappa+(a-1)\kappa/\Omega^2\), and extend its entries by zero beyond the path. These two sequences are affine in their indices. For each \(2\le a<b\le N\), parity of \(b-a\) and the affine identities \(\ell_{b-1}+\ell_{b+1}=2\ell_b\) and \(F_{a-1}+F_{a+1}=2F_a\) give
\[
Q_{a,b-1}+Q_{a,b+1}-Q_{a-1,b}-Q_{a+1,b}=0.
\]
The adjacent case \(b=a+1\) uses the diagonal entries in exactly the same identity. For \(2\le a\le N\), Hermitian symmetry and \(\ell_a-\ell_{a+1}=1\) yield
\[
\frac{i\Omega}{2}\left(Q_{a,a-1}+Q_{a,a+1}-Q_{a-1,a}-Q_{a+1,a}\right)=-1.
\]
At the absorbing boundary the same parity rules, including the zero-extension \(\ell_{N+1}=0\), give for \(2\le b\le N\)
\[
\frac{i\Omega}{2}(Q_{1,b-1}+Q_{1,b+1}-Q_{2,b})-\frac\kappa2 Q_{1b}=0.
\]
Finally, the upper-left diagonal entry is
\[
\frac{i\Omega}{2}(Q_{12}-Q_{21})-\kappa Q_{11}=(N-1)-N=-1.
\]
The lower triangle follows by Hermitian conjugation. These are precisely all entries of \(A^\dagger Q+QA=-I\). Uniqueness of the stable Lyapunov solution identifies the proposed formula with the time integral for **every** \(N\ge2\).

The total survival probability of a site-localized initial state is \(S_j(t)=\|e^{At}|j\rangle\|^2\). It satisfies \(-S_j'(t)=\kappa|\langle1|e^{At}|j\rangle|^2\), and \(S_j(t)\to0\) exponentially. Thus the displayed positive density integrates to one and integration by parts gives \(\mathbb E_jT=\int_0^\infty S_j(t)\,dt=Q_{jj}\). For \(j\ge2\), the function of \(\kappa\) is strictly convex with derivative proportional to \(-j/\kappa^2+(j-1)/\Omega^2\), proving the unique optimizer and its value. The endpoints, interior scaling and uniform-mixture identities follow by direct substitution and the sums of \(j(N-j+1)\) and \((j-1)(N-j+1)\).

## Verification

The attached `verify.py` evaluates **4,960 exact rational Lyapunov matrix entries** at lengths from one to fifteen and four rational parameter pairs. A separately implemented spectral integration of the killed propagator and an independent numerical Lyapunov solve agree with the closed form for **90 starting-site cases** across six lengths and three independent rate pairs. The finite tests corroborate the entry formulas; the arbitrary-length conclusion is established by the symbolic all-index substitution above. Run `python3 verify.py` with NumPy and SciPy installed.

## Relationship to prior work

Riberi, arXiv:2605.08056v1 (May 8, 2026), defines precisely this Lindblad boundary-sink mechanism on the **semi-infinite** nearest-neighbor path and obtains its full propagator and incomplete long-time absorption probability. The paper explicitly lists finite geometries as future work. Here the finite reflecting second endpoint changes the limiting behavior to complete absorption, and the result is the exact integrated finite-path operator, a site-resolved lifetime formula, and a sharp optimal rate independent of total length. The semi-infinite propagator alone does not state these finite-length formulas.

Varbanov, Krovi and Brun, arXiv:0803.3446v1, develop hitting times under **Poisson-triggered projective measurements**. Their general inverse-superoperator formula and weak/strong-measurement asymptotics are relevant context, but their monitoring channel and path Hamiltonian differ from the autonomous one-site Lindblad sink here. Gupta, arXiv:2512.15130v2, studies finite periodic chains with a **real Hermitian onsite defect** and unitary evolution, which does not produce absorption times. The standard Lyapunov integral representation is not claimed as new; the explicit all-size parity kernel and consequences are the substantive statement.

## Limitations

The theorem does not cover the infinite half-line, arbitrary graphs, nonuniform hopping, onsite disorder, many-particle interactions, additional loss sites, or finite-time optimal control. For \(N\to\infty\), the finding concerns a sequence of finite systems with sink optimized separately; it does not interchange the finite-chain and long-time limits. Site-dependent optimality does not assert optimality over coherent initial states with interference. The cited literature review and indexed searches cannot exclude an unindexed earlier specialization of the standard stable-Lyapunov framework, which remains a publication-priority risk. No independent external mathematical audit has been conducted.

## References

1. F. Riberi, *An Exactly Solvable Absorbing Quantum Walk*, arXiv:2605.08056v1, first publicly posted May 8, 2026, https://arxiv.org/html/2605.08056v1; revised as *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056v4, https://arxiv.org/html/2605.08056.
2. M. Varbanov, H. Krovi and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446v1, https://arxiv.org/pdf/0803.3446, *Phys. Rev. A* **78**, 022324 (2008).
3. S. Gupta, *Dynamics and steady states of tight-binding chains in presence of isolated defects*, arXiv:2512.15130v2, https://arxiv.org/html/2512.15130v2.
4. *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, *Entropy* **23** (2021), 85, https://www.mdpi.com/1099-4300/23/1/85.
