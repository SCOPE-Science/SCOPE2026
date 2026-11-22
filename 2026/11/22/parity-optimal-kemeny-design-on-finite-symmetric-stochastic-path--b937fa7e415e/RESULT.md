# Parity-optimal Kemeny design on finite symmetric stochastic paths

## Finding

Consider the symmetric, irreducible, nonnegative stochastic transition matrices supported on the path with \(n\ge3\) vertices, with edge transition probabilities \(w_i=P_{i,i+1}=P_{i+1,i}>0\). Define the zero-diagonal-convention Kemeny constant by
\[
\mathcal K(P)=\sum_{j=2}^n\frac1{1-\lambda_j(P)}=\operatorname{tr}((I-P)^+).
\]
Set \(c_i=i(n-i)\), \(O=\sum_{i\text{ odd}}c_i\), \(E=\sum_{i\text{ even}}c_i\), and \(S=\sqrt O+\sqrt E\). Among **all** such path kernels, the **unique** minimizer has
\[
w_i^*=\begin{cases}\sqrt O/S,&i\text{ odd},\\\sqrt E/S,&i\text{ even},\end{cases}
\qquad \mathcal K_* =S^2/n.
\]
Every interior vertex has zero holding probability at this unique optimum. For odd \(n\), the optimizer has every edge probability equal to \(1/2\). For even \(n\), odd-numbered edge probabilities strictly exceed \(1/2\), and even-numbered probabilities are strictly below \(1/2\):
\[
w^*_{\mathrm{odd}}=\frac{\sqrt{n^2+2}}{\sqrt{n^2+2}+\sqrt{n^2-4}},\quad
w^*_{\mathrm{even}}=\frac{\sqrt{n^2-4}}{\sqrt{n^2+2}+\sqrt{n^2-4}}.
\]
The sharp optimal values are
\[
\mathcal K_* = \begin{cases}
(n^2-1)/3,&n\text{ odd},\\
(\sqrt{n^2+2}+\sqrt{n^2-4})^2/12,&n\text{ even}.
\end{cases}
\]
The previously known path kernel minimizing the second-largest eigenvalue modulus has every edge probability \(1/2\). Thus it also minimizes \(\mathcal K\) if and only if \(n\) is odd. For even \(n\), its *exact* Kemeny excess is
\[
\Delta_n=\frac{n^2-1-\sqrt{n^4-2n^2-8}}6>0,
\qquad \Delta_n\sim\frac{3}{4n^2}.
\]

There is also a non-asymptotic exact **global excess decomposition**. Put \(Q_i=O\) for odd \(i\), \(Q_i=E\) for even \(i\), \(\eta_0=0\), and recursively \(\eta_i=c_i/Q_i-\eta_{i-1}\) for \(1\le i\le n-1\). Then \(\eta_i>0\) for every \(1\le i\le n-2\), \(\eta_{n-1}=0\), and for every feasible strictly positive edge vector \(w\),
\[
\boxed{\mathcal K(w)-\mathcal K_*=
\frac1n\sum_{i=1}^{n-1}\frac{c_i(w_i-w_i^*)^2}{w_i(w_i^*)^2}
+\frac{S^2}{n}\sum_{i=1}^{n-2}\eta_i(1-w_i-w_{i+1}).}
\]
Both terms are nonnegative. It quantifies both wrong edge weights and positive interior holding probabilities without invoking an unproved asymptotic estimate.

## Assumptions and scope

Vertices are \(1,\dots,n\) in path order, and the only off-diagonal transitions are the two directions along each consecutive edge. All \(w_i>0\); the diagonal entries are determined by stochasticity, and feasibility is exactly \(w_i+w_{i+1}\le1\) for \(1\le i\le n-2\). Endpoint holding is then automatically nonnegative. No independent conductance budget, edge-price constraint, nonuniform stationary distribution, nonsymmetric transition, or additional shortcut is included. With the alternative convention that the mean recurrence time of the target itself contributes, Kemeny's constant increases uniformly by one, so the optimizer and excess remain unchanged.

## Proof

**1. Trace-to-cut identity.** Write \(L=I-P\), the conductance Laplacian of the path with conductance \(w_i\) on edge \(i\). The nonzero eigenvalues of \(L\) are \(1-\lambda_j(P)\), so \(\mathcal K=\operatorname{tr}(L^+)\). Electrical resistance between vertices \(u<v\) on a tree is \(R_{uv}=\sum_{i=u}^{v-1}1/w_i\). Since \(\sum_{u<v}R_{uv}=n\operatorname{tr}(L^+)\), and exactly \(i(n-i)\) vertex pairs cross edge \(i\),
\[
\mathcal K(w)=\frac1n\sum_{i=1}^{n-1}\frac{c_i}{w_i}.
\]
The objective is strictly convex throughout the positive orthant; its Hessian is diagonal with entries \(2c_i/(n w_i^3)>0\).

**2. Candidate feasibility and dual certificate.** The proposed positive vector satisfies \(w_i^*+w_{i+1}^*=1\) for every interior vertex. Moreover, \(S^2(c_i/Q_i)=c_i/(w_i^*)^2\). Consider minimizing \(n\mathcal K=\sum_i c_i/w_i\) subject to the interior capacity inequalities. Set nonnegative Lagrange multipliers \(S^2\eta_i\) for these inequalities, with \(\eta_0=\eta_{n-1}=0\). Stationarity for edge \(i\) is
\[
\frac{c_i}{(w_i^*)^2}=S^2(\eta_{i-1}+\eta_i),
\]
which follows from the stated recursion. Because \(\sum_{i\text{ odd}} c_i/O=\sum_{i\text{ even}}c_i/E=1\), the last recursion indeed gives \(\eta_{n-1}=0\).

To verify the remaining, essential, signs rather than assume them, put \(O_k=\sum_{j=1}^k c_{2j-1}\), \(E_k=\sum_{j=1}^k c_{2j}\), and \(E_0=0\). Direct recurrence yields
\[
\eta_{2k}=\frac{O E_k-E O_k}{OE},\qquad
\eta_{2k-1}=\frac{E O_k-O E_{k-1}}{OE}.
\]
For even \(n=2r\), \(O=r(2r^2+1)/3\), \(E=2r(r^2-1)/3\), and exact summation gives
\[
O E_k-E O_k=\frac{2kr(r-k)(2k+2r^2-r+1)}3,
\]
\[
E O_k-O E_{k-1}=\frac{2kr(r-k)(-2k+2r^2+r+1)}3.
\]
The factors are strictly positive for \(1\le k\le r-1\), and the final odd-index multiplier at \(k=r\) vanishes as required. For odd \(n=2r+1\), \(O=E=r(r+1)(2r+1)/3\), and
\[
O E_k-E O_k=\frac{2kr(r-k)(r+1)(2r+1)}3,
\]
\[
E O_k-O E_{k-1}=\frac{2kr(r+1)(2r+1)(r-k+1)}3.
\]
Here the first expression is positive for \(1\le k<r\), the second for \(1\le k\le r\), and the last even-index multiplier at \(k=r\) is zero. All the interior multipliers are thus **strictly positive** in every dimension \(n\ge3\). Consequently the KKT stationarity, dual feasibility, primal feasibility, and complementary slackness conditions hold. Convexity proves global optimality, and strict convexity proves uniqueness. This argument is analytic for every \(n\), not a finite-size inference.

**3. Exact excess identity.** For any \(z,z_*>0\), the elementary identity
\[
\frac1z-\frac1{z_*}=-\frac{z-z_*}{z_*^2}+\frac{(z-z_*)^2}{zz_*^2}
\]
holds. Substitute \(z=w_i\), \(z_*=w_i^*\), sum with weights \(c_i\), and use stationarity to reorganize the linear term as
\[
-\sum_i\frac{c_i(w_i-w_i^*)}{(w_i^*)^2}
=S^2\sum_{j=1}^{n-2}\eta_j(1-w_j-w_{j+1}).
\]
The displayed boxed identity follows after division by \(n\). It also supplies a direct second certificate of uniqueness.

**4. Parity and comparison.** Summing \(i(n-i)\) over alternating parities yields, for odd \(n\), \(O=E=n(n^2-1)/12\); for even \(n\), \(O=n(n^2+2)/12\), \(E=n(n^2-4)/12\). Substitute these expressions into the candidate and optimum value. At the uniformly half-weighted walk, \(\mathcal K=(2/n)\sum_i c_i=(n^2-1)/3\). For even \(n\), subtract the optimal value to obtain \(\Delta_n\) above. Strict positivity follows from \((n^2-1)^2-(n^4-2n^2-8)=9>0\); expansion at infinity gives the asserted leading term. For odd \(n\), the two designs coincide exactly.

## Verification

Run `python verify.py` with SymPy installed. It checks the four finite-sum polynomial identities and multiplier factorizations symbolically; for every \(3\le n\le500\) it checks exact rational positivity of every interior multiplier and the closing zero; for \(3\le n\le10\) it computes the matrix resolvent trace independently using rational matrices; and it checks the exact global excess decomposition symbolically for rational feasible edge vectors. An actual invocation passed 126807 assertions. These finite and symbolic computations confirm algebra used by the proof but are **not** a replacement for the all-dimension positive-factor argument.

## Relationship to prior work

The spectral minimax path solution assigning \(1/2\) to every edge is Boyd–Diaconis–Sun–Xiao's established fastest-mixing theorem; this note neither reproves it as novel nor claims spectral improvement. Doyle's Kemeny discussion gives the standard hitting-time and resolvent interpretation. Patel–Agharkar–Bullo present the **general** constrained reversible Kemeny minimization problem and its semidefinite formulation, which applies to paths numerically but does not explicitly give the alternating-parity all-size optimizer, objective value, exact multiplier signs, or sharp equality/excess identity in the inspected material. Ghosh–Boyd–Saberi derive the tree resistance sum and solve a different problem with a **single total conductance budget**; this does not enforce the separate row-stochastic vertex capacities that are active and crucial here. The main contribution is the path-specific closed solution and exact dual rigidity under those local stochastic constraints, not the general convexity, effective-resistance formula, or optimization formulation.

## Limitations

The parity advantage over the spectral path optimum is \(O(n^{-2})\) in absolute Kemeny units for even sizes; a large practical speedup is not claimed. The proof does not optimize transient total variation, finite-horizon detection, nonsymmetric chains, unequal stationary masses, or arbitrary network topologies. A general prior SDP supplies an alternative numerical route, and further unindexed or specialized literature could conceivably contain an equivalent closed formula. Publication priority is therefore qualified, and no independent expert audit is asserted.

## References

1. S. Boyd, P. Diaconis, J. Sun and L. Xiao, *Fastest mixing Markov chain on a path*, submitted October 2003, revised July 2004, American Mathematical Monthly 113 (2006), 70–74. Open text: https://stanford.edu/~boyd/papers/pdf/fmmc_path.pdf
2. P. G. Doyle, *The Kemeny constant of a Markov chain*, arXiv:0909.2636v1, first posted 14 September 2009. https://arxiv.org/html/0909.2636v1
3. P. Agharkar, R. Patel and F. Bullo, *Robotic surveillance and Markov chains with minimal first passage time*, IEEE CDC (2014). Open text: https://motion.me.ucsb.edu/pdf/2014b-apb-conference.pdf
4. R. Patel, P. Agharkar and F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, IEEE Trans. Automatic Control 60 (2015), 3156–3167. Open text: https://motion.me.ucsb.edu/pdf/2014b-pab.pdf
5. A. Ghosh, S. Boyd and A. Saberi, *Minimizing effective resistance of a graph*, SIAM Review 50 (2008), 37–66. Open text: https://stanford.edu/~boyd/papers/pdf/eff_res.pdf
6. F. Durastante, M. Gnazzo and B. Meini, *Kemeny's constant minimization for reversible Markov chains via structure-preserving perturbations*, BIT Numerical Mathematics 66 (2026), 59. https://doi.org/10.1007/s10543-026-01152-6
