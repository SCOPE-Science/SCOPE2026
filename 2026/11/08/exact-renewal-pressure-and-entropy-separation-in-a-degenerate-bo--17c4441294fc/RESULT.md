# Exact renewal pressure and entropy separation in a degenerate border-collision map

## Finding
For every integer \(q\ge3\), consider the continuous planar piecewise-affine map
\[
F_q(x,y)=\begin{cases}(-qx+y-1,0),&x\le0,\\(x+y-1,0),&x\ge0.\end{cases}
\]
Every orbit enters \(K_q\times\{0\}\), where \(K_q=[-1,q-1]\), in finitely many steps. The restriction is the interval map \(f_q(x)=-qx-1\) for \(x\le0\) and \(f_q(x)=x-1\) for \(x\ge0\). It has a unique absolutely continuous invariant probability \(\mu_q\), with density
\[
\rho_q(x)=\frac{2(q-j)}{q(q+1)}\quad\text{for }x\in I_j^\circ,\qquad
I_0=[-1,0],\quad I_j=[j-1,j]\ (1\le j\le q-1).
\]
Under \(\mu_q\), successive return intervals between visits to \(I_0\), starting after the first visit, are independent, each uniform on \(\{1,\ldots,q\}\). Let \(N_n\) count visits to \(I_0\) at times \(0,\ldots,n-1\). Then
\[
\frac{N_n-2n/(q+1)}{\sqrt n}\ \Longrightarrow\
\mathcal N\left(0,\frac{2(q-1)}{3(q+1)^2}\right).
\]
For every real \(t\), the pressure of this visit count is
\[
\mathcal P_q(t):=\lim_{n\to\infty}\frac1n\log\int e^{tN_n}\,d\mu_q
=\log\lambda_q(t),\qquad
\lambda_q(t)^q=\frac{e^t}{q}\sum_{j=0}^{q-1}\lambda_q(t)^j,
\]
where \(\lambda_q(t)\) is the unique positive Perron root of the displayed equation. The physical metric entropy and almost-everywhere Lyapunov exponent coincide:
\[
h_{\mu_q}(f_q)=\chi_{\mu_q}(f_q)=\frac{2\log q}{q+1}.
\]
In contrast, the topological entropy of the compact interval system is
\[
h_{\rm top}(f_q|_{K_q})=\mathcal P_q(\log q)=\log\lambda_q,\qquad
\lambda_q^q=\sum_{j=0}^{q-1}\lambda_q^j,\quad1<\lambda_q<2.
\]
The precise large-\(q\) separation is
\[
h_{\rm top}=\log2-2^{-q-1}+O(q4^{-q}),\qquad
h_{\mu_q}=\frac{2\log q}{q+1}\longrightarrow0,
\]
while for every fixed real \(s\) the rare-visit pressure has the nonzero crossover
\[
\boxed{\lim_{q\to\infty}\mathcal P_q(\log q+s)=\log(1+e^s).}
\]

## Assumptions and scope
The parameter \(q\) is any integer at least three. The underlying planar system is considered on \(\mathbb R^2\), but topological entropy is asserted only on its explicit compact attracting interval \(K_q\times\{0\}\). The piecewise derivative and all logarithmic derivative statements ignore the countable set of orbits hitting branch boundaries; this set has zero \(\mu_q\)-measure. Independence and central-limit statements refer to the stationary measure \(\mu_q\), not to every deterministic initial condition. The standard normal distribution is denoted by \(\mathcal N\). No statement of independent validation is made.

## Proof
**Finite capture and natural Markov partition.** After one iteration the transverse coordinate is zero. The interval \(K_q=[-1,q-1]\) is forward invariant. For any \(x>q-1\), repeated use of \(x\mapsto x-1\) reaches \(K_q\). For \(x<-1\), its next image is \(-qx-1>q-1\), so the same conclusion follows. The continuous turning point obeys the postcritical cycle \(0\mapsto-1\mapsto q-1\mapsto q-2\mapsto\cdots\mapsto1\mapsto0\), explaining the integer parameter sequence.

Partition \(K_q\) into the \(q\) unit intervals \(I_0,\ldots,I_{q-1}\) displayed above. The first branch maps \(I_0\) linearly onto all of \(K_q\) with absolute slope \(q\); for \(j\ge1\), \(I_j\) maps by translation onto \(I_{j-1}\). Thus the adjacency matrix \(A_q\) has all entries in its first row equal to one and has a one in each position \((j,j-1)\), \(1\le j\le q-1\), all other entries zero. It is irreducible and aperiodic. Every admissible word of length \(q+1\) visits the expanding cell, so the coding cylinders shrink uniformly to points, up to endpoint duplications.

**Invariant law, renewal structure and uniqueness.** Let the density be constant with value \(d_j\) on \(I_j\). The Frobenius--Perron equations are \(d_{q-1}=d_0/q\) and \(d_j=d_0/q+d_{j+1}\) for \(0\le j<q-1\), yielding \(d_j=(q-j)d_0/q\). Normalizing the interval lengths gives \(d_0=2/(q+1)\), the asserted strictly positive density. Under this density, the partition itinerary is a stationary Markov chain with transition matrix
\[
P_{0j}=1/q\quad(0\le j<q),\qquad P_{j,j-1}=1\quad(1\le j<q),
\]
and all remaining entries zero. To verify the Markov property rather than only one-step transition probabilities, note that every nonempty cylinder maps affinely onto its final unit cell, and its conditional distribution there is uniform. The stationary vector is \(\pi_j=d_j\).

From state zero the next state is uniform over \(0,\ldots,q-1\); a choice \(j\) deterministically counts down through \(j-1,\ldots,0\), so the return delay is exactly \(j+1\). Strong Markov regeneration at state zero proves independent uniform return delays. The finite primitive Markov chain is mixing, hence the invariant interval measure is ergodic. Since its density is bounded away from zero on \(K_q\), its Birkhoff-generic set has full Lebesgue measure. Any other absolutely continuous invariant probability must be concentrated on that same generic set and therefore integrate every continuous observable identically; uniqueness follows. Finite capture and the affine rank-one planar projection also give a full planar-Lebesgue basin in the usual almost-everywhere sense.

**Entropy, derivative fluctuations and pressure.** The return time \(R\) has \(\mathbb ER=(q+1)/2\) and \(\operatorname{Var}R=(q^2-1)/12\). The renewal counting central-limit theorem (obtained by applying the i.i.d. central-limit theorem to partial sums of \(R\) and inverting the counting process) gives variance \(\operatorname{Var}R/(\mathbb ER)^3=2(q-1)/(3(q+1)^2)\) per unit time. The stationary initial delay changes the count by a bounded random number at fixed \(q\) and does not affect the limit. The derivative multiplier is \(q\) in cell zero and \(1\) elsewhere, so the log derivative over \(n\) steps is \((\log q)N_n\) almost surely. The Markov-chain entropy-rate identity gives \(h_{\mu_q}=\pi_0\log q\), since only the transitions out of state zero are random. Both equal the displayed physical rate.

For any \(t\in\mathbb R\), weight the row of \(P\) corresponding to state zero by \(e^t\). The resulting primitive nonnegative matrix \(P_t\) has Perron eigenvalue \(\lambda_q(t)\), and \(\mathbb E_{\mu_q}e^{tN_n}=\pi^\top P_t^n\mathbf1\). An eigenvector calculation with coordinates proportional to \(1,\lambda^{-1},\ldots,\lambda^{-(q-1)}\) gives the displayed polynomial equation. Perron--Frobenius convergence proves the pressure formula. At \(t=\log q\), the weighted matrix is \(A_q\). Because the Markov partition is generating, the growth rate of admissible symbolic words is exactly the topological entropy, giving \(h_{\rm top}=\log\rho(A_q)\).

**Large-parameter limit and sharp crossover.** For \(t=\log q+s\), the eigenvalue equation, with \(\lambda>1\) for all sufficiently large \(q\), becomes \(\lambda-1=e^s(1-\lambda^{-q})\). Its unique solution lies below \(1+e^s\); for any fixed \(0<\epsilon<e^s\) it eventually lies above \(1+e^s-\epsilon\). Hence \(\lambda\to1+e^s\), giving the crossover. With \(s=0\), \(\lambda_q\to2\) and \((2-\lambda_q)\lambda_q^q=1\). Writing \(\epsilon_q=2-\lambda_q\) yields \(\epsilon_q=2^{-q}+O(q4^{-q})\), which upon taking logarithms gives the stated topological-entropy expansion. Meanwhile \(\pi_0\log q=2\log q/(q+1)\to0\). This proves all assertions.

## Verification
Run the standalone Python 3 standard-library program `verify.py`. It checks the stationary vector and the characteristic polynomial at enough integer arguments for the tested degrees, the exact geometric first-return partition, and the renewal variance for \(q=3,\ldots,9\); it numerically checks Perron pressure roots at \(q=10,20,40,80\). The independent mathematical proof above establishes all \(q\ge3\) and all real tilts, while finite checking only corroborates it.

## Relationship to prior work
Simpson's 2026 boundary-Hopf paper derives the two-parameter border-collision map containing this slice: set left trace to \(-q\), right trace to \(1\), and the forcing parameter to \(-1\). The published bifurcation study is largely qualitative and numerical; it does not derive these renewal fluctuations and pressure limits. The 2024 zero-determinant classification provides broader parameter-space context. Simpson's 2026 first-return theorem assumes an expanding right-hand focus, specifically determinant greater than one, so it does not cover the doubly rank-one slice here.

There is an **exact older equivalence** that must be retained when assessing novelty: under \(u=-2x\), the interval system is \(u\mapsto u+2\) on \(u\le0\) and \(u\mapsto -qu+2\) on \(u\ge0\), exactly the \(\beta=2,s=q\) map in Botella-Soler--Oteo--Ros--Glendinning (2012). That paper explicitly computes the density, Lyapunov exponent and golden-ratio topological entropy for \(q=2\), and discusses integer slopes more generally. None of those \(q=2\) facts is asserted as new here. The statement for \(q\ge3\) adds the all-integer uniform renewal coding, its exact central-limit variance and tilted pressure, and the sharp large-parameter separation and crossover. General invariant-density and Markov-chain theorems explain parts of the method but do not themselves supply this evaluated quantitative package without specialization.

## Limitations
This result is confined to the integer postcritical slice with **both** planar determinant branches zero, and applies to the dynamics on the compact attracting interval. The planar invariant probability is singular with respect to planar area, even though its interval marginal is absolutely continuous. The central-limit theorem is distributional under the stationary law, not a pointwise rate for every trajectory. It does not establish robustness of the pressure crossover under noninteger slopes or nonzero right determinant. Independent scientific validation and exhaustive historical priority verification have not been performed.

## References
1. D. J. W. Simpson, *Boundary Hopf bifurcations in three-dimensional Filippov systems*, arXiv:2604.06570 (first posted 2026-04-08), Section 4.
2. V. Botella-Soler, J. A. Oteo, J. Ros and P. Glendinning, *Families of piecewise linear maps with constant Lyapunov exponent*, arXiv:1205.5360 (first posted 2012-05-24), Sections 2--4.
3. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790 (first posted 2024-08-08).
4. D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901 (first posted 2026-06-08).
5. P. Góra, *Invariant densities for piecewise linear maps of the unit interval*, Ergodic Theory Dynam. Systems 29 (2009), 1549--1583 (general density framework).
