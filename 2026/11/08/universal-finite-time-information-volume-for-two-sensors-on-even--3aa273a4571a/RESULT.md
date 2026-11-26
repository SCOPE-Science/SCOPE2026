# Universal finite-time information volume for two sensors on even cycles

## Finding

Let \(M\ge2\), \(N=2M\), and let \(A\) be the adjacency matrix of the undirected simple cycle on \(\mathbb Z_N\). Its distinct eigenvalues are \(a_k=2\cos(\pi k/M)\), \(0\le k\le M\). Let \(\phi\) be a complex-valued function on these points, set \(b_k=\phi(a_k)\), and define \(B=\phi(A)\) by spectral functional calculus. For \(1\le d<N\), form the square observation matrix \(O_{M,d}(B)\) whose rows, in time-major order, are
\[
 e_0^{\mathsf T}B^t,\quad e_d^{\mathsf T}B^t,\qquad t=0,\ldots,M-1.
\]
With \(V_{-}=\prod_{0\le i<j\le M-1}(b_j-b_i)\) and \(V_{+}=\prod_{1\le i<j\le M}(b_j-b_i)\), the exact determinant law is
\[
 |\det O_{M,d}(B)|=
 \begin{cases}
 N^{1-M}|V_{-}V_{+}|,&\gcd(d,N)=1,\\
 0,&\gcd(d,N)>1.
 \end{cases}
\]
In particular, when the \(b_k\) are pairwise distinct, precisely the \(\varphi(N)\) coprime separations give full reconstruction in the dimension-count minimum of \(M\) time samples. Every one of them is determinant-optimal. More generally, at a coprime separation the exact spectral requirement is that both lists \((b_0,\ldots,b_{M-1})\) and \((b_1,\ldots,b_M)\) be pairwise distinct: the only possible equality between different spectral indices is \(b_0=b_M\).

For \(B=A\) and coprime \(d\), the integer matrix \(O_{M,d}(A)\) has determinant \(\pm1\). Hence integer initial signals can be recovered from the integer observations using integer coefficients.

## Assumptions and scope

The nearest-neighbor adjacency acts by \((Af)(x)=f(x-1)+f(x+1)\). Two distinct coordinate sensors at \(0,d\) are read simultaneously at the \(M\) consecutive integer times starting at zero, with unit weights. The source space is the full \(\mathbb C^N\), not a graph-frequency band, and \({\mathsf T}\) is ordinary transpose. The optimization is that of determinant magnitude, equivalently \(\det(O^*O)=|\det O|^2\). It is not an optimization of the smallest singular value or spectral condition number.

## Proof

Let \(\zeta=e^{2\pi i/N}\) and \(v_k=(1,b_k,\ldots,b_k^{M-1})^{\mathsf T}\). The orthonormal Fourier eigenvector of frequency \(j\) has coordinate \(N^{-1/2}\zeta^{jx}\) at vertex \(x\). The Fourier frequencies \(k,N-k\) for \(1\le k<M\) have the same adjacency eigenvalue, and \(0,M\) are singleton frequencies. Right-multiply \(O\) by the unitary Fourier matrix and group its rows by sensor, neither of which changes determinant magnitude. After omitting a common factor \(N^{-1/2}\) from each column, the paired columns have sensor blocks \((v_k,\zeta^{kd}v_k)\) and \((v_k,\zeta^{-kd}v_k)\); the singleton columns are \((v_0,v_0)\) and \((v_M,(-1)^dv_M)\).

By multilinearity the paired columns can be replaced by \((v_k,0)\) and \((0,v_k)\) after extracting the scalar \(\zeta^{-kd}-\zeta^{kd}\) from the determinant for each pair. This identity holds even when the scalar vanishes: the original columns are then identical. In the remaining determinant take the part of the first singleton in the first sensor block and the part of the second singleton in the second block, or vice versa. Putting both singletons in the same block contributes zero. The two surviving terms have the same Vandermonde product \(V_-V_+\), with opposite signs before the singleton scalar is applied. Consequently
\[
 |\det O_{M,d}(B)|=N^{-M}\,|(-1)^d-1|\prod_{k=1}^{M-1}|\zeta^{-kd}-\zeta^{kd}|\;|V_-V_+|.
\]
No eigenvalue distinctness is used in this identity. If \(d\) is even the singleton factor is zero, and if \(d\) is odd with \(g=\gcd(d,M)>1\) the paired factor at \(k=M/g\) is zero. If \(\gcd(d,N)=1\), then \(d\) is odd and multiplication by \(d\) permutes the nonzero residue classes modulo \(M\). The paired product is therefore \(M\): its factors are \(2|\sin(\pi kd/M)|\), and \(\prod_{k=1}^{M-1} 2\sin(\pi k/M)=M\) follows by evaluating \((x^M-1)/(x-1)\) at \(x=1\) and factoring over the roots of unity. The remaining scalar is \(N^{-M}\cdot 2M=N^{1-M}\). This proves the formula and the precise spectral requirement: every pair of different spectral indices occurs together in at least one of the two Vandermondes, except the pair \(0,M\).

Fewer than \(M\) time samples give fewer than \(2M\) scalar rows. The determinant proves injectivity at this dimension-count minimum exactly for the placements and spectral values just described. If either Vandermonde vanishes, every placement has zero determinant at this horizon.

For adjacency evolution and \(d=1\), order the signal coordinates as \(0,1,-1,2,-2,3,\ldots,-(M-1),M\), reducing subscripts modulo \(N\). At time zero the two coordinates \(0,1\) are read directly. At time \(1\le t\le M-1\), walks from vertex \(0\) of length \(t\) only contribute coordinates already listed by the preceding times or the new vertex \(-t\); the second row similarly adds \(1+t\). Each new vertex is reached by a unique walk of length \(t<N/2\). Thus the permuted observation matrix is triangular with unit diagonal. The determinant law transfers its absolute determinant of one to every coprime separation for adjacency evolution. The adjugate formula gives an integer inverse.

## Verification and limitations

The determinant proof is exact, including the spectral collision case. In particular for \(N=4,d=1\) and \((b_0,b_1,b_2)=(0,1,0)\), each Vandermonde has absolute value one and the raw determinant has absolute value \(1/4\), despite the collision. The accompanying `CHECK.py` tests adjacency and three affine spectral evolutions using exact integer determinant arithmetic. Its previously recorded run covered 185 matrices; the finite tests do not certify the general theorem or the collision case. This result concerns only the specified square minimal-horizon matrix: failure at \(M\) snapshots is not in general a claim of failure with more time samples. Equal determinant magnitudes do not imply equal noise conditioning.

## Relationship to prior work

Parlangeli and Notarstefano study sensor reachability and observability for cycles and paths through stacked Laplacian observations. The rank of a longer observation matrix is distinct from the determinant of the particular square observation matrix here. Related work on graph Paley–Wiener sampling concerns graph-frequency bands and numerical frame bounds. The closely related even-cycle rank analysis in the record `SCOPE-exact-arithmetic-rank-loss-and-one-snapshot-recovery-on-even-cyc--b4ea4f0f2c79` studies ranks at \(M\) and \(M+1\) snapshots for injective spectral functions. The record `SCOPE-raw-trajectory-volume-factorization-and-optimal-two-sensor-gaps--d1a88d067af2` gives a raw-sample Gram determinant for a rectangular low-pass observation matrix, not this full-state square matrix. Neither statement gives the endpoint-deleted Vandermonde law here or the adjacency integer inverse. Fourier diagonalization and the Vandermonde and root-of-unity products are classical ingredients.

## References

- G. Parlangeli and G. Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs*, IEEE Transactions on Automatic Control 57 (2012), 743–748, https://arxiv.org/abs/1109.3556.
- I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, https://arxiv.org/abs/2609.25472.
- *Exact arithmetic rank loss and one-snapshot recovery on even cycle graphs*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-arithmetic-rank-loss-and-one-snapshot-recovery-on-even-cyc--b4ea4f0f2c79.
- *Raw-trajectory volume factorization and optimal two-sensor gaps on finite cycles*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-raw-trajectory-volume-factorization-and-optimal-two-sensor-gaps--d1a88d067af2.
