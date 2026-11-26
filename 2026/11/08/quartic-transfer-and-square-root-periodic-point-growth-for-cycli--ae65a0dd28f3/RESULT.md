# Quartic spectral reduction and sharp asymptotic for cycle diffusion

## Setting and finding

Consider synchronous integer diffusion on the labelled simple cycle \(C_n\), \(n\ge3\): each vertex simultaneously sends one unit to each neighbor whose value is smaller. Let \(R_n\) count classes of states periodic at time zero modulo common integer translation. There is no quotient by graph automorphisms. Use the known [zero-winding transfer census](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-zero-winding-transfer-law-for-recurrent-integer-diffusion-on-c--b28ddab7ef35/RESULT.md), \(R_n=[z^0]\operatorname{tr}M(z)^n\). Here \(M\) is indexed by sign pairs in \(\{-1,0,1\}^2\), with its only possibly nonzero entries on \((a,b)\to(b,c)\). The entry is 1 when \(b=0\) and \(a+c=0\); for \(b=\pm1\) it is \(\sum_{q=1}^{1-b(a+c)}z^{bq}\), with an empty sum interpreted as zero. All other entries vanish. The exponent records the signed edge difference; the constant term enforces closure around the labelled cycle.

Write \(s=1+z+z^{-1}\). The characteristic polynomial has the reduction
\[
\det(\lambda I-M(z))=(\lambda-1)
(\lambda^4-s\lambda^3-2\lambda^2-\lambda+1)
(\lambda^4+s\lambda^3+2\lambda^2-\lambda+1).
\]
If \(A_n(s),B_n(s)\) are the quartics' root power sums, and \(T_k=[z^0](1+z+z^{-1})^k=\sum_{j=0}^{\lfloor k/2\rfloor}k!/(j!^2(k-2j)!)\), then
\[
R_n=1+\sum_{k\ge0}T_k[s^k](A_n+B_n).
\]
Let \(\rho\) be the largest real root of \(\rho^4-3\rho^3-2\rho^2-\rho+1=0\), and put
\[
\sigma^2=\frac{2\rho^2}{4\rho^3-9\rho^2-4\rho-1}.
\]
The sharp periodic-point growth is
\[
R_n\sim\frac{\rho^n}{\sqrt{2\pi\sigma^2 n}},
\qquad \rho=3.6095709022238956\ldots,\quad
\sigma^2=0.4702157360865868\ldots.
\]
The prefactor is \(0.5817836156008666\ldots\). The \(n^{-1/2}\) factor measures the cost of requiring zero total edge difference rather than counting all closed walks of the sign-pair graph.

## Proof of the spectral reduction

The \((0,0)\) state is isolated with a unit loop. Denote the eight remaining states, in order, by
\[
(a_1,b_1,c_1,d_1,e_1,f_1,g_1,h_1)
=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)).
\]
Use \(a_1,\ldots,h_1\) also for the corresponding coordinates of a test vector in the equation \(M x=\lambda x\). Let \(P=z+z^2\) and \(Q=z^{-1}+z^{-2}\). The row relations for elimination are
\[
\begin{aligned}
\lambda a_1&=z^{-1}c_1,&\lambda h_1&=zf_1,\\
\lambda b_1&=e_1,&\lambda g_1&=d_1,\\
\lambda d_1&=z^{-1}b_1+Qc_1,&\lambda e_1&=Pf_1+zg_1,\\
\lambda c_1&=z^2s f_1+Pg_1+zh_1,&\lambda f_1&=z^{-2}s c_1+Qb_1+z^{-1}a_1.
\end{aligned}
\]
Let \(L=\lambda^4-1\). At generic \(\lambda\), the block on the six eliminated coordinates has determinant \(\lambda^2 L\): the first two coordinates have diagonal \(\lambda\), and \(b_1,e_1,g_1,d_1\) form a 4-cycle of product one. Solving the four middle equations gives \(L b_1=\lambda^2 P f_1+zQ c_1\) and \(L g_1=\lambda^2 Q c_1+z^{-1}P f_1\). As \(P Q=s+1\), \(z^{-1}P^2=z^2(s+1)\), and \(zQ^2=z^{-2}(s+1)\), the Schur complement on \(c_1,f_1\) has diagonal \(X/(\lambda L)\) and off-diagonals \(-z^{\pm2}Y/(\lambda L)\), where
\[
X=\lambda^2(\lambda^4-1)-\lambda^3(s+1),\qquad Y=s\lambda^5+\lambda^4+\lambda-1.
\]
Thus the eight-state determinant is \((X-Y)(X+Y)/L\). In order, the two factors have \(\lambda^2+1\) and \(\lambda^2-1\) times the displayed quartics. Cancellation proves the identity as a polynomial, including the exceptional \(\lambda\). The trace of a matrix power is the sum of the corresponding powers of the eigenvalues with their algebraic multiplicities, so taking the constant term gives the stated central-trinomial formula.

## Proof of the growth law

At \(z=1\) the eight-state part is irreducible: there is a closed walk visiting \(c_1,g_1,d_1,b_1,e_1,f_1,a_1,c_1\), and \(h_1\) lies on the cycle \(c_1,h_1,f_1,c_1\). The latter and \(c_1,f_1,c_1\) have lengths three and two, so the block is primitive. Its Perron root must be \(\rho>3\): the first quartic is negative at 3 and positive at 4, while the second quartic is positive for real \(\lambda\ge3\). The full matrix has no other eigenvalue of modulus \(\rho\). For \(z=e^{i\theta}\), entrywise moduli are bounded by the entries at \(1\); the entry from \(c_1\) to \(f_1\) is \(z+z^2+z^3\), of modulus strictly less than three for \(0<|\theta|\le\pi\). The strict Perron comparison on the irreducible block gives spectral radius less than \(\rho\) there.

Let \(\lambda(\theta)\) be the simple eigenvalue near \(\rho\) for small real \(\theta\). Its analytic branch comes from the first quartic with \(s=1+2\cos\theta\). It is positive near zero, since the polynomial is real there and the unique root near \(\rho\) is real. Differentiation gives \(\lambda'(0)=0\) and \(- (\log\lambda)''(0)=\sigma^2\); the denominator in \(\sigma^2\) is positive for \(\rho>3\). Compactness away from zero and the spectral gap at zero bound all other contributions to the constant-term integral by \(O((\rho-\eta)^n)\) for some \(\eta>0\), using the trace identity for eigenvalues even if they collide. On a small symmetric interval around zero, \(\log(\lambda(\theta)/\rho)=-\sigma^2\theta^2/2+o(\theta^2)\), bounded above by \(-\sigma^2\theta^2/4\) on a sufficiently small interval. The substitution \(v=\sqrt{n}\theta\) and dominated convergence in \((2\pi)^{-1}\int_{-\pi}^{\pi}\operatorname{tr}(M(e^{i\theta})^n)\,d\theta\) give the stated constant and asymptotic.

## Verification and relationship to prior work

The determinant and the exact coefficient law can be compared by building \(M\) from its signs and taking a symbolic determinant or multiplying Laurent polynomials for small \(n\). For example \(R_3=19, R_4=47, R_5=171, R_6=517\); finite checks are not a proof of the asymptotic. The earlier zero-winding census already gives the transfer, finite counts and temporal-orbit relation; these are inputs rather than new claims. Duffy et al. [arXiv:1609.05792](https://arxiv.org/abs/1609.05792) and Long–Narayanan [arXiv:1704.04295](https://arxiv.org/abs/1704.04295) supply the eventual periodicity context. Mullen–Cox–Nowakowski [arXiv:2010.04750](https://arxiv.org/abs/2010.04750) treat period-two counts on paths up to isomorphism, not the labelled-cycle count with zero total gap. The spectral factorization and evaluated asymptotic concern this particular cycle transfer law; standard Perron and Laplace methods are not contributions. No claim is made about other graphs, unlabeled cycles, or basins of attraction.
