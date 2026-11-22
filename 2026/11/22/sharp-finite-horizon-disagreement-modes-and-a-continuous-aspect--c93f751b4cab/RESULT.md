# Sharp finite-horizon disagreement modes and a continuous aspect-ratio speedup law for bipartite gossip

## Finding

Let \(2\le p\le q\) be integers and consider independent uniformly selected edges of the complete bipartite graph \(K_{p,q}\). Each edge selection replaces both endpoint values by their arithmetic mean, leaving all other values unchanged. Denote by \(e_k\) the state after \(k\) updates with its conserved global mean removed. Define the orthogonal projections \(P_A,P_B,P_C\) onto, respectively, zero-sum fluctuations within the \(p\)-vertex shore, zero-sum fluctuations within the \(q\)-vertex shore, and the one-dimensional inter-shore-contrast subspace.

Set
\[
 d=\left(\frac1p,\frac1q,\frac1p+\frac1q\right),\qquad
 w=\left(1-\frac1p,1-\frac1q,\frac1p+\frac1q\right),
 \quad M_{ij}=(1-d_i)\delta_{ij}+\frac{d_iw_j}{4}.
\]
For every integer \(k\ge0\), if \((a_k,b_k,c_k)^{\mathsf T}=M^k(1,1,1)^{\mathsf T}\), then the exact expected squared disagreement is
\[
 \mathbb E\|e_k\|_2^2=a_k\|P_Ae_0\|_2^2+b_k\|P_Be_0\|_2^2+c_k\|P_Ce_0\|_2^2.
\]
For every \(k\ge1\), \(b_k>a_k>c_k\) if \(p<q\), while \(b_k=a_k>c_k\) if \(p=q\). Consequently **a nonzero within-the-larger-shore contrast is always a sharp worst-case initial state**, and when the shores are equal both within-shore contrast spaces are optimal. The exact worst-case finite-horizon factor is \(b_k\), with
\[
 b_1=\nu_{p,q}:=1-\frac1{2q},\qquad
 0<b_k<\nu_{p,q}^k\quad(k\ge2).
\]
The sharp asymptotic factor \(\rho_{p,q}=\lim_{k\to\infty}b_k^{1/k}\) is the unique root in \((1-1/q,1)\) of
\[
 \sum_{i\in\{A,B,C\}}\frac{d_iw_i}{4(\rho_{p,q}-1+d_i)}=1.
\]
If \(p,q\to\infty\) with \(p/q\to r\in(0,1]\), then the ratio between the true logarithmic decay rate and the familiar one-step spectral-bound decay rate has the sharp limit
\[
 \frac{-\log\rho_{p,q}}{-\log\nu_{p,q}}\longrightarrow
 R(r)=\frac{3(1+r)-\sqrt{9(1-r)^2+4r}}{4r}.
\]
The function \(R\) is strictly decreasing on \((0,1]\), with \(R(1)=1\) and \(\lim_{r\downarrow0}R(r)=4/3\). The same \(4/3\) limit holds for **each fixed** \(p\ge2\) as \(q\to\infty\).

## Assumptions and scope

All edges of the simple unweighted \(K_{p,q}\) are sampled with probability \(1/(pq)\), independently at successive discrete integer times. Pair averaging is exact, synchronous within the selected pair, and has relaxation one. Initial values are arbitrary real numbers; the expectation is only over edge choices. The ordered shores have sizes \(2\le p\le q\). No assertion concerns quenched or almost-sure contraction factors, noisy communication, changing graph topology, or worst-case per-realization error.

Write \(n=p+q\), \(H=\{x\in\mathbb R^n:\mathbf 1^{\mathsf T}x=0\}\). Let \(P_A\) and \(P_B\) project onto vectors supported on their respective shores and summing to zero there. Let \(P_C\) project onto the line through the vector with entries \(1/p\) on the first shore and \(-1/q\) on the second. Then \(P_A+P_B+P_C=I_H\), and all three spaces have positive dimension because \(p,q\ge2\).

## Proof

**1. Exact second-moment reduction.** For a selected edge \((i,j)\), let \(z=e_i-e_j\) and \(Q=I-zz^{\mathsf T}/2\). It is an orthogonal projector, fixes the consensus vector, and contracts every Euclidean norm. Let \(B_0=I_H\) and \(B_{k+1}=\mathbb E[Q B_k Q]\); independent identically distributed edges (whose finite words have the same probability when reversed) imply \(\mathbb E\|e_k\|^2=e_0^{\mathsf T}B_ke_0\). Shore-permutation invariance and symmetry make each \(B_k\) a linear combination \(a_kP_A+b_kP_B+c_kP_C\).

The edge-vector projection lengths are independent of the chosen edge:
\[
 z^{\mathsf T}P_Az=1-1/p,\quad z^{\mathsf T}P_Bz=1-1/q,\quad
 z^{\mathsf T}P_Cz=1/p+1/q.
\]
The matrix \(D=\mathbb E[zz^{\mathsf T}]\), restricted to \(H\), acts as \(d_AP_A+d_BP_B+d_CP_C\). Writing \(s_k=w_Aa_k+w_Bb_k+w_Cc_k=z^{\mathsf T}B_kz\), expand \(Q B_k Q\) and average to obtain
\[
 B_{k+1}=B_k-\tfrac12(DB_k+B_kD)+\tfrac14s_kD.
\]
Therefore \(m_{i,k+1}=(1-d_i)m_{i,k}+d_i s_k/4\) with \(m_{i,0}=1\). This is precisely the stated three-by-three transfer matrix.

**2. Sharp ordering for every horizon.** For any deterministic edge sequence, appending an orthogonal projection cannot increase squared error. Consequently \(B_{k+1}\preceq B_k\), hence every \(m_{i,k}\) and the common forcing \(s_k=\sum_iw_i m_{i,k}\) are nonincreasing. Since \(\sum_iw_i=2\) and \(0\le m_{i,k}\le1\), one also has \(0\le s_k/4\le1/2\).

For any \(d\in(0,1]\), consider the scalar recurrence \(u_0(d)=1\), \(u_{k+1}(d)=(1-d)u_k(d)+d s_k/4\). It is represented by independently resetting a scalar register at step \(k\) to \(s_k/4\) with probability \(d\), otherwise retaining its previous value. Couple two such processes by the same uniform variables when \(d'<d''\). Every reset of the smaller rate is also a reset of the larger rate, so the last reset time for \(d''\) is at least that for \(d'\). The assigned values \(s_k/4\) decrease with reset time and lie below the initial value one. Thus \(u_k(d'')\le u_k(d')\), strictly for \(k\ge1\) because the final step has a positive probability of resetting only the larger-rate process. Since \(d_B\le d_A<d_C\), this gives the stated strict or tied ordering. The supremum Rayleigh quotient of \(B_k\) is exactly \(b_k\), with precisely the asserted maximizing spaces.

**3. Exact rate and strict improvement over a spectral-bound power.** Each entry of \(M\) is positive, since all \(d_i,w_i\) are positive. Its row sums are \(1-d_i/2\), with largest \(\nu_{p,q}=1-1/(2q)\). At least one row sum is strictly smaller, and positivity of \(M\) implies \(M^k\mathbf1<\nu_{p,q}^k\mathbf1\) for \(k\ge2\). Hence the strict finite-horizon bound. Perron–Frobenius yields a unique positive simple dominant eigenvalue \(\rho_{p,q}<\nu_{p,q}\), and \(b_k\) has a positive Perron component, proving \(\lim b_k^{1/k}=\rho_{p,q}\). The matrix determinant lemma applied to the diagonal-plus-rank-one expression for \(M\) gives the secular equation. Its left side decreases strictly from infinity to below one on \((1-1/q,1]\), because \(\rho(M)<\nu_{p,q}<1\); thus the root in that interval is unique.

**4. Sharp aspect-ratio law.** For \(p/q\to r\in(0,1]\) and both sizes diverging, the matrix \(q(I-M)\) tends to a block lower-triangular matrix whose upper two-by-two block is
\[
 A(r)=\frac14\begin{pmatrix}3/r&-1/r\\-1&3\end{pmatrix}.
\]
The third diagonal eigenvalue of the limiting matrix is \(1+1/r\), exceeding the smaller eigenvalue of \(A(r)\). Hence, by continuity of eigenvalues and the Perron mode,
\[
 q(1-\rho_{p,q})\longrightarrow
 \gamma(r)=\frac{3(1+r)-\sqrt{9(1-r)^2+4r}}{8r}.
\]
As \(-\log\nu_{p,q}=1/(2q)+O(q^{-2})\), the displayed expression for \(R(r)=2\gamma(r)\) follows. Its smaller-root branch is characterized by \((3-2rR)(3-2R)=1\), with \(1\le R<4/3\), and implicit differentiation gives
\[
 R'(r)=-\frac{R(3-2R)}{r(3-2R)+(3-2rR)}<0.
\]
Evaluation at \(r=1\) and the limit as \(r\downarrow0\) give one and four thirds.

For fixed \(p\ge2\), put \(\varepsilon=1/q\). At \(\varepsilon=0\), the transfer matrix has a simple eigenvalue one with right eigenvector \((1/3,1,1/3)^{\mathsf T}\) and left eigenvector \((0,1,0)\); the remaining two modes have spectral radii below one. Differentiating the middle row of \(M(\varepsilon)\) yields \(\rho_{p,q}=1-2/(3q)+O_p(q^{-2})\). Thus the ratio of logarithmic rates tends to \(4/3\), independently of fixed \(p\).

## Verification

The standalone `check_gossip.py` uses only the Python standard library. It compares the exact transfer-matrix moments against the independently computed, full \((p+q)\)-dimensional covariance recursion for six shore-size pairs and nine successive horizons; it also checks exact fractional mode ordering and strict spectral improvement over a wider parameter grid. Floating-point tests check the secular-root asymptotics. Running `python check_gossip.py` produced `PASS 17019 total checks including asymptotic spectral-root tests`. Exact finite computations corroborate the formulas but are not substituted for the all-size proof.

## Relationship to prior work

Boyd, Ghosh, Prabhakar and Shah (2004, 2006) establish the classical randomized pairwise gossip model, its mean-preserving projection update, and the one-step spectral rate bound. Agaskar, Wang and Lu (2014) give a general exact tensor-power mean-square formula for randomized Kaczmarz; on the mean-zero subspace this general identity also applies to pairwise gossip, and therefore the mere existence of a matrix-power formula is **not** claimed as new. Their full text treats arbitrary row systems and Gaussian numerical examples rather than the exact shore-dependent maximizers, the three-sector reduction, or the sharp monotone aspect-ratio law above.

The specific all-horizon identification of the larger-shore difference space, the strict finite-horizon comparison in this two-parameter family, and the continuous \(1\)-to-\(4/3\) asymptotic improvement law are the mathematical contributions claimed here. A star is a distinct one-vertex-shore boundary case, excluded from the stated domain; its two-sector formula alone does not determine the two-nontrivial-shore theorem.

## Limitations

This analysis concerns worst-case **expected squared** error under independent uniform edge selection. It does not determine pathwise convergence exponents or high-probability quantiles. The proportional-growth limit assumes a positive fixed limiting aspect ratio; the fixed-small-shore limit is justified separately. The standard one-step comparison bounds a product of per-step expected contractions and is not itself the exact long-run mean-square rate. Prior general tensor-power methods permit calculating this example by further specialization, and equivalent previously unindexed family-specific expressions could limit publication priority. Independent external validation has not been undertaken.

## References

1. S. Boyd, A. Ghosh, B. Prabhakar and D. Shah, *Analysis and Optimization of Randomized Gossip Algorithms*, IEEE CDC (2004), 5310–5315, https://doi.org/10.1109/CDC.2004.1429652 . Online publication recorded May 16, 2005 by IEEE: https://ieeexplore.ieee.org/document/1429652/ . Open author PDF: https://web.stanford.edu/~boyd/papers/pdf/gossip_opt.pdf .
2. S. Boyd, A. Ghosh, B. Prabhakar and D. Shah, *Randomized Gossip Algorithms*, IEEE Transactions on Information Theory **52** (2006), 2508–2530, https://doi.org/10.1109/TIT.2006.874516 . Open author PDF: https://web.stanford.edu/~boyd/papers/pdf/gossip.pdf .
3. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP (2014), 389–393, https://doi.org/10.1109/GlobalSIP.2014.7032145 . Lawful open PDF: https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content .
