# Every nontrivial Gibbs partition can destroy two-step exact mixing

## Finding

Let \(E\) be a finite set of \(N\ge2\) states, let \(\pi\) be any strictly positive probability distribution on \(E\), and let \(\mathcal B\) be a partition into \(k\) nonempty blocks. Write \(\Pi(x,y)=\pi(y)\) for the stationary resampling kernel, and let \(G\) be the Gibbs kernel that resamples within the current block according to \(\pi\) conditioned on that block. For a \(\pi\)-stationary transition kernel \(P\), define the doubly averaged kernel \(Q=GPG\).

**Theorem (sharp universal partition obstruction).** The following property holds for every strictly positive \(\pi\)-stationary kernel \(P\) and every integer \(t\ge1\):

\[
\lVert (GPG)^t-\Pi\rVert_{F,\pi}
\le\lVert P^t-\Pi\rVert_{F,\pi}
\]

if and only if the partition is trivial, meaning \(k=1\) or \(k=N\). More strongly, for every partition with \(2\le k\le N-1\), and every strictly positive \(\pi\), there exist strictly positive, nonreversible, \(\pi\)-stationary kernels \(P\), arbitrarily close to \(\Pi\), for which

\[
P^2=\Pi,\qquad Q^t\ne\Pi\quad\text{for every integer }t\ge1.
\]

The construction has an exact one-dimensional projected mode: for some \(0<\varepsilon<1\),

\[
\lVert P-\Pi\rVert_{F,\pi}=\varepsilon,\qquad
\lVert Q^t-\Pi\rVert_{F,\pi}=(\varepsilon/2)^t
\quad (t\ge1).
\]

Thus Gibbs averaging improves the first-step distance by a factor of two, but destroys finite-step exact convergence from time two onward. The minimum number of states permitting the obstruction is three.

## Assumptions and scope

The kernels are row-stochastic matrices, acting on real functions through \((Pf)(x)=\sum_yP(x,y)f(y)\). A kernel is \(\pi\)-stationary when \(\sum_x\pi(x)P(x,y)=\pi(y)\), and reversible when it is self-adjoint on \(\ell^2(\pi)\). For a partition \(\mathcal B\),

\[
(Gf)(x)=\frac{\sum_{y\in B_x}\pi(y)f(y)}{\pi(B_x)},
\qquad
\pi(B_x)=\sum_{y\in B_x}\pi(y).
\]

This operator is the orthogonal projection onto block-constant functions in \(\ell^2(\pi)\). The weighted Frobenius (Hilbert–Schmidt) norm of an operator \(T\) is

\[
\lVert T\rVert_{F,\pi}^{2}=
\sum_{x,y\in E}\frac{\pi(x)}{\pi(y)}\,T(x,y)^2.
\]

All assertions concern finite state spaces, positive \(\pi\), and two-sided Gibbs averaging. The universal quantifier in the theorem is over strictly positive stationary kernels and every positive integer time.

## Proof

**1. Orthogonal splitting.** Work in the real Hilbert space \(H=\ell^2(\pi)\) with inner product \(\langle f,g\rangle_\pi=\sum_x\pi(x)f(x)g(x)\). Both \(G\) and \(\Pi\) are orthogonal projections and satisfy \(G\Pi=\Pi G=\Pi\). When \(2\le k\le N-1\), choose unit vectors

\[
a\in\operatorname{ran}(G)\cap\mathbf1^\perp,
\qquad b\in\ker(G).
\]

These subspaces have respective dimensions \(k-1\) and \(N-k\), both positive. They are orthogonal, and both are orthogonal to the constants. Define

\[
u=\frac{a+b}{\sqrt2},\qquad
v=\frac{a-b}{\sqrt2}.
\]

Then \(u,v\) are centered, orthonormal, and satisfy \(Gu=Gv=a/\sqrt2\).

**2. A positive chain with exact mixing in two steps.** Choose \(0<\varepsilon<1\) so small that \(1+\varepsilon u(x)v(y)>0\) for every \(x,y\). Define the rank-one perturbation

\[
P(x,y)=\pi(y)\bigl(1+\varepsilon u(x)v(y)\bigr),
\quad\text{or}\quad
P=\Pi+\varepsilon(u\otimes v),
\]

where \((u\otimes v)f=u\langle v,f\rangle_\pi\). Centering of \(v\) gives \(P\mathbf1=\mathbf1\), while centering of \(u\) gives \(\pi P=\pi\). The choice of \(\varepsilon\) makes every entry positive. Since \(\langle v,u\rangle_\pi=0\) and \(\Pi\) annihilates centered vectors,

\[
(P-\Pi)^2=\varepsilon^2(u\otimes v)^2=0,
\qquad P^2=\Pi.
\]

The adjoint of \(u\otimes v\) is \(v\otimes u\), which is different because \(u,v\) are orthogonal and nonzero. Thus \(P\) is nonreversible. Scaling \(\varepsilon\) to zero makes \(P\) arbitrarily close to \(\Pi\) in any finite-dimensional matrix norm. Its centered weighted Frobenius norm is exactly \(\varepsilon\), because the two factors are unit vectors.

**3. The projected chain retains a nonzero mode.** Using the action of \(G\) on \(u,v\),

\[
Q=GPG=\Pi+\frac{\varepsilon}{2}(a\otimes a).
\]

The rank-one operator \(a\otimes a\) is an orthogonal projection, annihilates constants, and has weighted Frobenius norm one. Therefore, for every integer \(t\ge1\),

\[
Q^t=\Pi+\left(\frac{\varepsilon}{2}\right)^t(a\otimes a),
\qquad
\lVert Q^t-\Pi\rVert_{F,\pi}=\left(\frac{\varepsilon}{2}\right)^t>0.
\]

By contrast, \(P^t=\Pi\) for every \(t\ge2\). The claimed universal inequality therefore fails already at \(t=2\) for every nontrivial partition.

**4. Endpoint partitions and sharpness.** If \(k=1\), then \(G=\Pi\) and \(GPG=\Pi\) for every stationary \(P\). If \(k=N\), then \(G=I\) and \(GPG=P\). Hence both endpoint partitions satisfy the inequality universally. For \(N=2\) only the endpoint partitions exist, whereas \(N=3\) admits a nontrivial two-block partition. This completes the if-and-only-if and minimality proofs.

**5. Exact three-state witness.** Under the uniform distribution \(\pi=(1/3,1/3,1/3)\), take blocks \(\{1,2\}\) and \(\{3\}\) and transition matrix

\[
P=\begin{pmatrix}
1/4&1/2&1/4\\
1/3&1/3&1/3\\
5/12&1/6&5/12
\end{pmatrix},\qquad
G=\begin{pmatrix}
1/2&1/2&0\\
1/2&1/2&0\\
0&0&1
\end{pmatrix}.
\]

Direct multiplication gives \(P^2=\Pi\) and

\[
Q=GPG=\begin{pmatrix}
17/48&17/48&7/24\\
17/48&17/48&7/24\\
7/24&7/24&5/12
\end{pmatrix}.
\]

The centered operator \(Q-\Pi\) has eigenvalues \(1/8,0,0\), while \(P-\Pi\) is a nonzero square-zero matrix. Consequently \(\lVert Q^t-\Pi\rVert_{F,\pi}=8^{-t}\) for every \(t\ge1\).

## Verification

The included standalone Python program `verify.py` uses only the standard library and exact rational arithmetic. It checks the displayed three-state matrices and their power identity. It also enumerates nontrivial partitions of state sets of sizes three through six, with uniform and unequal rational stationary distributions, constructs independent rational rank-one witnesses, and verifies positivity, stationarity, two-step exactness, surviving projected modes, and exact Frobenius-power identities. The completed run passed 13,899 assertions. The analytic argument in the preceding section proves the theorem for every finite \(N\), every strictly positive \(\pi\), every eligible partition, and all positive integer times; finite calculations are diagnostic rather than a substitute for those quantifiers.

## Relationship to prior work

Choi and Wang (2026, arXiv:2610.39239v1), Theorem 4.1, proves an all-time weighted-Frobenius improvement under Gibbs averaging for **reversible** ergodic kernels, using self-adjointness. The present theorem addresses the sharp failure of that universal statement without reversibility, and quantifies failure at time two while retaining strict positivity and arbitrary prescribed stationary distributions and partitions.

The earlier Choi–Wang paper (2025, arXiv:2509.02996v1), Section 7.1.6, already provides a **different nonreversible averaging slowdown** (a one-sided group average of a cycle sampler), so the general phenomenon that averaging need not improve nonreversible mixing is not new. The present conclusion is not merely that slowdown: it characterizes all partitions for a *two-sided conditional Gibbs projection*, and shows that a chain mixing exactly in two steps can be sent to one with no finite exact mixing time.

Choi, Lim and Wang (2025, arXiv:2512.13067v1), Proposition 6.2, identifies the nontrivial spectrum of \(GPG\) with that of the induced projection chain. That spectral description is consistent with the new construction but does not establish the existence of a square-zero centered \(P\) for **every** intermediate partition whose compressed centered kernel has nonzero spectrum. Classical exact lumpability theory addresses a different question about faithful block-process reduction.

## Limitations

The theorem concerns the universal *pointwise-in-time weighted-Frobenius inequality* and exact finite-step convergence; it does not assert that \(Q\) is slower than \(P\) at every threshold of total-variation mixing time, nor that Gibbs averaging is harmful in typical applications. The constructed projected chain is still strictly positive, converges geometrically, and is reversible. The construction is finite-state and does not directly address continuous state spaces or other averaging operators. The historical-priority comparison is based on the inspected papers and targeted searches, not an exhaustive proof that no equivalent theorem exists elsewhere.

## References

1. Michael C. H. Choi and Youjia Wang, *Bregman projections and partition design for accelerating finite Markov chains*, arXiv:2610.39239v1 (first public version, 29 October 2026), especially Section 4. https://arxiv.org/html/2610.39239v1
2. Michael C. H. Choi and Youjia Wang, *Group-averaged Markov chains: mixing improvement*, arXiv:2509.02996v1 (3 September 2025), especially Section 7.1.6. https://arxiv.org/html/2509.02996v1
3. Michael C. H. Choi, Ryan J. Y. Lim and Youjia Wang, *Group-averaged Markov chains II: tuning of group action in finite state space*, arXiv:2512.13067v1 (15 December 2025), especially Propositions 3.2 and 6.2. https://arxiv.org/html/2512.13067v1
4. Peter Buchholz, *Exact and ordinary lumpability in finite Markov chains*, Journal of Applied Probability 31 (1994), 59–75, DOI:10.2307/3215235.
