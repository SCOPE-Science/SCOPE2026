# A sharp transport crossover in two-lag Bernoulli recursive trees

## Finding

Consider the growing tree whose vertices are \(v_0,\ldots,v_{N-1}\), with the initial edge \(v_0v_1\). Independently for every \(k=2,\ldots,N-1\), attach \(v_k\) to \(v_{k-1}\) with probability \(p_N\) and otherwise to \(v_{k-2}\). Write \(\kappa_N\) for Kemeny's constant of the simple nearest-neighbor random walk on this finite tree, using zero first-hitting time at the starting vertex. The following assertions form one finite-size transport-crossover theorem.

**Macroscopic law.** If \(p_N\to p\in(0,1]\), then
\[
\frac{\kappa_N}{N^2}\xrightarrow{\mathbb P}\frac{1}{3(2-p)}.
\]
For a fixed \(p>0\), the convergence holds almost surely when the trees are coupled as initial segments of one infinite attachment sequence. In the sparse regime \(p_N\to0\), the two opposite sides of the threshold are
\[
Np_N\to\infty\quad\Longrightarrow\quad \frac{\kappa_N}{N^2}\xrightarrow{\mathbb P}\frac16,
\qquad
Np_N\to0\quad\Longrightarrow\quad \frac{\kappa_N}{N^2}\xrightarrow{\mathbb P}\frac13.
\]
In particular, the positive-parameter macroscopic limit jumps from \(1/6\) to \(1/3\) at the zero-attachment endpoint; the transition is at the scale \(p_N\asymp N^{-1}\).

**Single-bridge law and critical nonconcentration.** If the sole attachment to the immediately previous vertex occurs at index \(k\in\{2,\ldots,N-1\}\), put
\[
a=k-1,\qquad b=\left\lceil\frac{N-k}{2}\right\rceil,\qquad c=\left\lfloor\frac{N-k}{2}\right\rfloor.
\]
The resulting tree is a three-arm tree with arm lengths \(a,b,c\), and its Kemeny constant obeys the exact identity
\[
\boxed{\ \kappa_{\mathrm{path},N}-\kappa_N=\frac{2abc}{N-1},\quad
\kappa_{\mathrm{path},N}=\frac{2N^2-4N+3}{6}.\ }
\]
If \(Np_N\to\lambda\in(0,\infty)\), the probability of no immediately-previous attachment tends to \(e^{-\lambda}\), and that of exactly one tends to \(\lambda e^{-\lambda}\). Conditional on exactly one, with \(U\) uniform on \((0,1)\),
\[
\frac{\kappa_N}{N^2}\ \Longrightarrow\ \frac13-\frac12U(1-U)^2.
\]
These two positive-probability subevents imply that \(\kappa_N/N^2\) cannot converge in probability to any deterministic constant in the critical window. No complete critical-window distribution is asserted.

A quantitative finite-size sensitivity identity is
\[
\left.\frac{d}{dp}\mathbb E_p\kappa_N\right|_{p=0}
=-\frac{2}{N-1}\sum_{k=2}^{N-1}(k-1)
\left\lfloor\frac{N-k}{2}\right\rfloor
\left\lceil\frac{N-k}{2}\right\rceil
\sim-\frac{N^3}{24}.
\]
It specifies the first-order response to rare one-step attachments; it is not a uniform expansion in \(p\) when \(Np\) is order one.

## Assumptions and scope

The probability parameter may depend on \(N\) but is common to all independent attachment choices within a given tree. The number of vertices is \(N\ge2\), and the deterministic first edge is always present. Distances and arm lengths count graph edges. For Kemeny's constant, \(\pi_i=\deg(v_i)/(2(N-1))\) and
\[
\kappa_N=\sum_{j=0}^{N-1}\pi_j\mathbb E_i\tau_j,
\qquad \tau_j=\inf\{t\ge0:X_t=v_j\},
\]
which is independent of the starting vertex \(i\). Periodicity of the non-lazy walk does not invalidate this finite-chain identity. All limits concern this exact two-lag model; they do not apply to uniformly recruited parents, general preferential-attachment trees, or infinite-volume mixing times.

## Proof

**1. A deterministic distance comparison.** Let \(D_j=d(v_0,v_j)\), \(D_0=0\), and \(X_i=d(v_i,v_{i-1})\) for \(i\ge1\). For an attachment bit \(B_i\), where \(B_i=1\) means attachment to \(v_{i-1}\), the tree recursion gives
\[
X_1=1,\qquad X_i=\begin{cases}1,&B_i=1,\\1+X_{i-1},&B_i=0,\end{cases}\qquad i\ge2.
\]
Consequently, \(M_N=\max_{1\le i<N}X_i\) is one plus the longest terminally truncated run of zero attachment bits. For \(0\le i<j<N\), the ancestral path from \(v_j\) must first reach the labels \(\le i\) at either \(v_i\) or \(v_{i-1}\) (the latter only if \(i\ge1\)). In the first case \(d(v_i,v_j)=D_j-D_i\). In the second, its path goes through \(v_{i-1}\), and
\[
d(v_i,v_j)=D_j-D_{i-1}+X_i.
\]
Since \(|D_i-D_{i-1}|\le X_i\), in every case
\[
0\le d(v_i,v_j)-(D_j-D_i)\le2M_N.
\]
For any \(\mu\in[1,2]\), put \(\Delta_N(\mu)=\max_{0\le j<N}|D_j-j/\mu|\). Then
\[
\left|d(v_i,v_j)-\frac{j-i}{\mu}\right|\le2\Delta_N(\mu)+2M_N.
\]
Summing over \(i<j\), with Wiener index \(W_N=\sum_{i<j}d(v_i,v_j)\), gives
\[
\left|W_N-\frac{N(N^2-1)}{6\mu}\right|
\le N(N-1)\bigl(\Delta_N(\mu)+M_N\bigr).
\]
The classical exact identity for every tree on \(N\) vertices [2] is
\[
\kappa_N=\frac{2W_N}{N-1}-N+\frac12.
\]
Therefore the following **pathwise certificate**, valid for every choice of attachment bits and every \(\mu\in[1,2]\), follows by direct substitution:
\[
\boxed{\left|\frac{\kappa_N}{N^2}-\frac1{3\mu}\right|
\le\frac{1+2\Delta_N(\mu)+2M_N}{N}.}
\]
This inequality is deterministic and does not appeal to finite simulations.

There is also an exact stationary-mass check. If \(B_N=1\) is used solely as a boundary convention, then for every \(0\le j\le N-2\), counting edges internal to and crossing the prefix \(\{v_0,\ldots,v_j\}\) gives
\[
\sum_{i=0}^{j}\deg(v_i)=2(j+1)-B_{j+2}.
\]
Thus stationary mass in every insertion-label prefix differs from uniform mass by at most \(1/(N-1)\), for *every* attachment sequence. This supports the transport interpretation but is not needed for the Wiener-based argument.

**2. Uniform depth concentration.** Put \(\mu_N=2-p_N\). Reveal ancestral pointers from any fixed \(v_j\) backward: until reaching \(v_0\) or \(v_1\), the successive label decrements are independent, each equal to one with probability \(p_N\) and two otherwise. The depth differs by at most one from the renewal hitting count for level \(j-1\). Hoeffding bounds for bounded increments show, uniformly over \(p_N\in[0,1]\), that for each \(\varepsilon>0\) and all sufficiently large \(N\),
\[
\mathbb P\!\left(\Delta_N(\mu_N)>\varepsilon N\right)
\le C_\varepsilon N e^{-c_\varepsilon N}.
\]
For completeness: for \(j\le\varepsilon N/4\), both \(D_j\) and \(j/\mu_N\) lie between zero and \(j\), so their error is already small. For larger \(j\), deviations of \(D_j\) by \(\varepsilon N\) force a deviation of order \(\varepsilon N\) in the sum of at most \(N\) independent increments in \([1,2]\); apply Hoeffding and a union bound over \(j\). Hence \(\Delta_N(\mu_N)=o_{\mathbb P}(N)\). For a fixed parameter and a nested infinite sequence of choices, the summable bound yields the almost-sure version.

**3. Longest-run transition.** If \(L_N\) is the longest run of zero attachment bits among \(B_2,\ldots,B_{N-1}\), the initial run or a run immediately after a one gives, for integer \(r\ge1\),
\[
\mathbb P(L_N\ge r)\le(1+Np_N)(1-p_N)^r
\le(1+Np_N)e^{-p_Nr}.
\]
Because \(M_N=L_N+1\) up to an inessential endpoint convention, \(Np_N\to\infty\) implies \(M_N/N\to0\) in probability: substitute \(r=\lfloor\varepsilon N\rfloor\), noting that \((1+x)e^{-\varepsilon x}\to0\) as \(x\to\infty\). Combining with the certificate at \(\mu=\mu_N\) yields
\[
\frac{\kappa_N}{N^2}-\frac1{3(2-p_N)}\xrightarrow{\mathbb P}0.
\]
For fixed \(p>0\), an ordinary geometric-run union bound makes \(M_N=O(\log N)\) almost surely and establishes the almost-sure assertion. If \(Np_N\to0\), with probability at least \((1-p_N)^{N-2}\to1\) every bit is zero. The resulting graph is a path (with its labels interlaced), and the stated exact path formula applies. This proves the macroscopic regimes.

**4. A single bridge and the critical window.** With only \(B_k=1\), the previous \(k\) vertices form a path ending at \(v_{k-1}\), of length \(a=k-1\). The remaining vertices form two alternating chains starting at \(v_{k-1}\), of lengths \(b\) and \(c\) as displayed. For a three-arm tree, the edge-cut formula [2]
\[
W_N=\sum_{e}n_e(N-n_e)
=\sum_{\ell\in\{a,b,c\}}\sum_{t=1}^{\ell}t(N-t)
\]
shows, upon evaluating the polynomial sums, that
\[
W_{\mathrm{path},N}-W_N=abc.
\]
The Kemeny/Wiener identity now yields the exact penalty \(2abc/(N-1)\). If \(k/N\to x\in[0,1]\), division by \(N^2\) gives the continuous limit
\[
\frac{\kappa_N}{N^2}\to f(x)=\frac13-\frac12x(1-x)^2.
\]
At \(Np_N\to\lambda\in(0,\infty)\), the count of ones tends to Poisson\((\lambda)\). Given exactly one one, its label is uniform on \(\{2,\ldots,N-1\}\), so \(k/N\Rightarrow U\), establishing the stated conditional distribution. The zero-event subevent has limit \(1/3\), whereas on the one-event subevent \(f(U)<1/3\) almost surely. Both have asymptotically positive probability, so deterministic concentration is impossible.

**5. Derivative at zero.** For fixed \(N\), \(\mathbb E_p\kappa_N\) is a polynomial in \(p\). Its first derivative at zero sums the differences between each one-event configuration and the all-zero path, exactly the displayed negative finite sum. Under \(k/N=x\), the summand divided by \(N^2\) converges to \(x(1-x)^2/2\); the Riemann sum gives \(\int_0^1 x(1-x)^2/2\,dx=1/24\). This proves the stated asymptotic derivative.

## Verification

Run the standalone file `verify.py` with `python3 verify.py`; Python's standard library and SymPy are used. The script constructs trees from all binary attachment strings through eleven vertices, computes graph distances by independent breadth-first searches, checks the Wiener edge-cut identity and Kemeny/Wiener relation, verifies the deterministic certificate and the exact stationary-prefix identity, and compares selected cases with directly solved rational Markov first-hitting systems. It separately checks one-event penalties over a range of sizes, the universal three-arm polynomial identity, and finite-size approximations to the critical conditional curve. It prints `VERIFICATION_OK assertions=20859` when all 20,859 checks pass. These checks corroborate finite identities only; the probability-limit steps are proved in Sections 2–5 above.

## Relationship to prior work

Tang, Wang, and Wu [1] introduced this precise two-lag Bernoulli tree and derived its one-ended and infinite-collision properties, including spine/branch descriptions. Their inspected article does not state a finite-tree Kemeny or Wiener asymptotic, the \(Np_N\) crossover, or the single-bridge penalty. Jang, Kim, and Song [2] supply the general (already known) identity relating Kemeny's constant and Wiener index on *all* trees; neither this identity nor the general three-arm cut summation is claimed as independently novel. Ciardo, Dahl, and Kirkland [3] analyze extremal Kemeny constants at fixed order/diameter. Lesny, Neininger, and Schmieder [4] analyze different random caterpillars with a fixed initial spine and uniformly attached children. Bhutani and collaborators [5] analyze a different \(m\)-ary uniform-recruiter recursive tree, including Wiener limits. None of the inspected model assumptions subsumes the special two-lag attachment process with an \(N\)-dependent rare-bridge probability. The substantive new claim is the model-specific sharp transport crossover, including critical nonconcentration and its exact one-bridge mechanism, not the classical reduction to Wiener index.

## Limitations

The full random limiting law at \(Np_N\to\lambda\) is not identified; only the zero- and one-bridge conditional behavior and nonconcentration are proved. No central limit theorem, finite-\(N\) stochastic ordering in \(p\), monotonicity of an individual attachment flip, or mixing-time theorem is asserted. The limits are for the non-lazy simple walk's Kemeny constant, not its total-variation convergence from an initial state. Literature-priority uncertainty remains for other formulations of sparse two-lag recursive trees or random finite combs. Numerical tests do not substitute for the proof of an infinite limit.

## References

[1] J.-s. Tang, F. Wang, and X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916v1, July 3, 2026. https://arxiv.org/html/2607.02916v1

[2] J. Jang, S. Kim, and M. Song, *Kemeny's constant and Wiener index on trees*, arXiv:2209.11271v1, September 22, 2022, especially formulas (2)–(4). https://arxiv.org/html/2209.11271v1

[3] L. Ciardo, G. Dahl, and S. Kirkland, *On Kemeny's constant for trees with fixed order and diameter*, arXiv:2003.08286, March 18, 2020. https://arxiv.org/abs/2003.08286

[4] F. Lesny, R. Neininger, and M. Schmieder, *On topological indices of random caterpillar graphs*, arXiv:2606.09228, June 8, 2026. https://arxiv.org/abs/2606.09228

[5] K. Bhutani, R. Kalpathy, F. Lesny, H. Mahmoud, and R. Neininger, *Distances in m-ary recursive trees*, arXiv:2609.33636, September 27, 2026. https://arxiv.org/abs/2609.33636
