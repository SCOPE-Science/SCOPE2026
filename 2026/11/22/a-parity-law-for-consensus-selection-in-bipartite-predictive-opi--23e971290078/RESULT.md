# A parity law for consensus selection in bipartite predictive opinion loops

## Finding

In the perfect-prediction Friedkin--Johnsen loop of [1], a social network's number of peer-interaction steps can change **which population opinion is selected at eventual consensus** in a sharply nonmonotone manner, even though every inner and outer update is averaging. On **every finite connected undirected bipartite network**, with arbitrary positive reciprocal edge weights and two fixed peer-susceptibility levels, *all positive even peer-round lengths select exactly the same aggregate weights*, whereas every odd length selects another explicitly determined weight. The odd weights converge geometrically to the even weight and are always strictly on the same side of it unless susceptibilities agree. The aggregate law depends on the network only through its two degree-weighted initial opinion means, not through its edge arrangement or part sizes.

Precisely, let the nonempty bipartition be \(V=L\sqcup R\). Give vertices in \(L\) peer susceptibility \(a\in(0,1)\), and vertices in \(R\) susceptibility \(b\in(0,1)\). Let \(d_i>0\) be weighted degree, let \(E=\sum_{i\in L}d_i=\sum_{j\in R}d_j\), and write
\[
\bar x_L=E^{-1}\sum_{i\in L}d_i x_i^*,\qquad
\bar x_R=E^{-1}\sum_{j\in R}d_j x_j^*.
\]
For every integer \(K\ge1\), define the class-influence weight
\[
w_K=\begin{cases}
\displaystyle\frac{b(1-a)}{a(1-b)+b(1-a)},&K\text{ even},\\[6pt]
\displaystyle\frac{b(1-a)+(ab)^{q+1}(1-b)}{a(1-b)+b(1-a)+(ab)^{q+1}(2-a-b)},&K=2q+1,\ q\ge0.
\end{cases}
\]
For every common platform susceptibility \(0\le\beta<1\), the unique steady expressed-opinion vector \(x_{K,\beta}\) has the exact invariant weighted mean
\[
\sum_{i\in L}\frac{w_Kd_i}{E}(x_{K,\beta})_i+
\sum_{j\in R}\frac{(1-w_K)d_j}{E}(x_{K,\beta})_j
=w_K\bar x_L+(1-w_K)\bar x_R.
\]
In the high-platform-susceptibility limit it converges to genuine consensus at this same value:
\[
\boxed{\lim_{\beta\uparrow1}x_{K,\beta}
=\bigl(w_K\bar x_L+(1-w_K)\bar x_R\bigr)\mathbf1.}
\]
At exact \(\beta=1\) the same selection holds for prediction iteration initialized at \(x^*\).

Writing \(w_{\mathrm e}=b(1-a)/[a(1-b)+b(1-a)]\), \(D=a(1-b)+b(1-a)\), and \(t=(ab)^q\), odd lengths obey the strict sign and rate identity
\[
\boxed{\ w_{2q+1}-w_{\mathrm e}
=\frac{t\,ab\,(a-b)(1-ab)}{D\,[D+t\,ab(2-a-b)]}.\ }
\]
The difference of odd- and even-round selected consensus values equals \((w_{2q+1}-w_{\mathrm e})(\bar x_L-\bar x_R)\). It has the sign of \((a-b)(\bar x_L-\bar x_R)\) and vanishes when either factor is zero. When both factors are nonzero, consensus selection is genuinely nonmonotone in \(K\): all even lengths give the common value and the odd lengths give values on one strict side of it. The absolute odd-round deviation is of order \((ab)^q\), and the ratio of successive absolute odd-round deviations tends to \(ab\) as \(q\to\infty\).

For example, take any star with one hub in \(L\), arbitrarily many leaves in \(R\), \(a=1/5\), \(b=4/5\), hub innate opinion one and all leaf innate opinions zero. Then the consensus values at peer-round lengths \(K=1,2,3,4\) are exactly \(4/5,16/17,32/35,16/17\), **independently of the number of leaves**. The hub can determine \(16/17\) of the consensus value despite being one individual against arbitrarily many.

## Assumptions and scope

The network has \(N\ge2\) vertices, is connected and bipartite, and has a symmetric nonnegative adjacency matrix \(A\), no within-part edges, and strictly positive weights on all edges in its connected support. Define \(d_i=\sum_j A_{ij}>0\) and the receiving-neighbor row-stochastic matrix \(W_{ij}=A_{ij}/d_i\). Peer susceptibilities equal \(a\) on \(L\) and \(b\) on \(R\), with \(0<a,b<1\). Innate opinions \(x^*\in[0,1]^N\) are arbitrary. During each deployment period, the inner Friedkin--Johnsen update is \(z^{(k+1)}=(I-\Lambda_\alpha)z^{(0)}+\Lambda_\alpha Wz^{(k)}\), initialized from \(z^{(0)}=(1-\beta)x^*+\beta f\), and performed \(K\) times. Perfect prediction feeds the final expressed opinions into the following deployment period. The common platform susceptibility is \(\beta\in[0,1]\). The constant \(K\) is an integer, not a continuous-time interval. The result does not cover directed networks, part-dependent platform susceptibility, or peer susceptibilities varying inside a part.

## Proof

**1. The finite-round matrix.** Write \(Z=\Lambda_\alpha W\) and \(B=I-\Lambda_\alpha\). The linear map taking any initialization to its opinion after \(K\) inner steps is the row-stochastic matrix
\[
\Psi_K=\sum_{r=0}^{K-1}Z^rB+Z^K.
\]
Because \(0<a,b<1\), \(Z\) has row sums less than one. Each \(\Psi_K\) is irreducible with positive diagonal: for \(K=1\), \(B+Z\) has the edges of the connected graph and a positive diagonal; for \(K\ge2\), its nonnegative summands include \(B\) and \(ZB\), which have those same properties. Therefore every \(\Psi_K\) is primitive and has a unique positive stationary probability row \(\pi_K\).

**2. A graph-independent two-dimensional left-invariant space.** Define probability rows supported on the two parts by
\[
(q_L)_i=\begin{cases}d_i/E,&i\in L,\\0,&i\in R,\end{cases}
\quad
(q_R)_i=\begin{cases}0,&i\in L,\\d_i/E,&i\in R.\end{cases}
\]
Symmetry of edge weights gives, for every \(j\in R\),
\( (q_LW)_j=E^{-1}\sum_{i\in L}d_iA_{ij}/d_i=d_j/E\), and similarly \(q_RW=q_L\). Thus
\[
q_LZ=a q_R,\quad q_RZ=b q_L,\quad
q_LB=(1-a)q_L,\quad q_RB=(1-b)q_R.
\]
In the basis \((q_L,q_R)\), left multiplication by \(Z\) and \(B\) is represented by the two-by-two matrices
\[
H=\begin{pmatrix}0&a\\b&0\end{pmatrix},\qquad
J=\begin{pmatrix}1-a&0\\0&1-b\end{pmatrix}.
\]
Consequently the invariant two-dimensional space carries the stochastic matrix
\[
T_K=\sum_{r=0}^{K-1}H^rJ+H^K
=T_\infty+H^K(I-T_\infty),
\quad T_\infty=(I-H)^{-1}J
=\frac1{1-ab}\begin{pmatrix}1-a&a(1-b)\\b(1-a)&1-b\end{pmatrix}.
\]
The stationary row of this two-state matrix gives \(\pi_K=w_Kq_L+(1-w_K)q_R\). Since \(\Psi_K\) is primitive, this row must be its **unique** stationary probability.

**3. Parity and exact weights.** Since \(H^2=abI\), for \(K=2q\), \(q\ge1\), the equality \(T_K=(1-(ab)^q)T_\infty+(ab)^qI\) shows its off-diagonal ratio—and hence stationary distribution—is independent of \(q\). The stationary left weight is \(w_{2q}=T_{K,21}/(T_{K,12}+T_{K,21})=b(1-a)/D\). For \(K=2q+1\), \(H^K=(ab)^q H\), so the off-diagonal entries are
\[
(T_K)_{12}=\frac{a(1-b)+(ab)^{q+1}(1-a)}{1-ab},\qquad
(T_K)_{21}=\frac{b(1-a)+(ab)^{q+1}(1-b)}{1-ab}.
\]
Taking their ratio gives the displayed odd formula. Subtraction from \(w_{\mathrm e}\), and the elementary identity \(a(1-b)^2-b(1-a)^2=(a-b)(1-ab)\), yield the exact sign-and-rate expression. Its denominator is positive. Since \(0<ab<1\), the odd weights approach the even value geometrically, and the difference is nonzero exactly when \(a\ne b\).

**4. Platform equilibrium and selected consensus.** The perfect-prediction recursion is \(f^{(t+1)}=\Psi_K[(1-\beta)x^*+\beta f^{(t)}]\). For \(0\le\beta<1\), its unique fixed point is
\[
x_{K,\beta}=(1-\beta)(I-\beta\Psi_K)^{-1}\Psi_K x^*.
\]
Multiplying its fixed-point equation by \(\pi_K\), and using \(\pi_K\Psi_K=\pi_K\), gives \(\pi_Kx_{K,\beta}=\pi_Kx^*\), the asserted exact weighted mean. Primitivity implies \(\Psi_K^t\to\mathbf1\pi_K\) as \(t\to\infty\). Accordingly the Abel limit \((1-\beta)\sum_{t\ge0}\beta^t\Psi_K^{t+1}\to\mathbf1\pi_K\) proves the consensus formula as \(\beta\uparrow1\). At \(\beta=1\), the prediction recursion is \(f^{(t+1)}=\Psi_K f^{(t)}\), so initialization \(f^{(1)}=x^*\) yields the same limit.

**5. Star example.** In a star, the degree total on either side equals the sum of the edge weights. The two degree-weighted means are the hub opinion and the edge-weighted mean of the leaf opinions. Substitution of \(a=1/5\), \(b=4/5\) into the formulas gives \(w_1=4/5\), \(w_2=w_4=16/17\), and \(w_3=32/35\); these fractions do not contain the number of leaves. With innate profile one at the hub and zero at the leaves, they are the selected consensus values for any positive edge weights.

## Verification

The accompanying `verify.py` is standalone Python using only the standard library's exact `fractions.Fraction`. Running `python3 verify.py` constructs actual full network matrices, solves the finite-\(\beta\) equilibrium linear system by exact rational Gaussian elimination, and checks the claimed stationary weights and conserved means on 4,752 cases from connected bipartite graphs with one through four vertices per class, including randomly generated irregular positive reciprocal rational edge weights, six peer-round lengths and three pairs of susceptibilities. It also checks the star fractions. The proof above, not finite computations, establishes the statements for arbitrary graph size, weights and integer \(K\).

## Relationship to prior work

Wu, Abebe and Mendler--Dünner [1] introduce the nested platform/peer model, give the general finite-\(K\) transition matrix and fixed-point resolvent, and prove high-susceptibility consensus. Their main variance theorem assumes regular graphs and homogeneous peer susceptibility. Their source does not state the all-connected-bipartite **parity** law, the horizon-independent even-round stationary weights, or the one-hub size-independent consensus selection. These structural results are not claimed to be independent of the originating model's matrix formulas: those formulas are starting premises.

A published related result [2] constructs an invariant measure and a sharp weighted-disagreement contraction for arbitrary reciprocal graphs with heterogeneous peer susceptibilities, but **only at infinitely many peer updates per prediction round**. Its invariant measure agrees with the even-\(K\) formula on bipartite networks; this limiting case is credited and is not independently claimed new. It explicitly does not treat finite peer-relaxation lengths. Boudourides [3] develops fixed-boundary FJ Green operators and influence centralities, rather than an iterated platform-prediction feedback. Standard random-walk reversibility and Perron--Frobenius convergence are used without novelty claim. The contribution is the unexpected **finite-\(K\)** alternating structural classification across *all* reciprocal bipartite networks, not the generic fixed-point resolvent or the already-known infinite-\(K\) stationary measure.

## Limitations

The formula requires a connected bipartite reciprocal network with classwise constant peer susceptibility and uniform platform susceptibility. Within-class heterogeneous susceptibilities or directed edges can destroy the two-dimensional closure. The source model assumes perfect deterministic opinion observation and noiseless predictions; it is not a causal or empirical prediction about real platforms. At any fixed \(0\le\beta<1\), the equilibrium is consensual exactly when \(\Psi_K x^*\) is constant: the fixed-point equation for a constant equilibrium reduces to \(c\mathbf1=(1-\beta)\Psi_K x^*+\beta c\mathbf1\), and the converse follows from uniqueness. For example, on one edge at \(K=1\) with \(a+b=1\), both rows of \(\Psi_1\) are \((b,a)\), so distinct innate opinions can yield consensus even at \(\beta=0\). The high-\(\beta\) limit ensures consensus for every innate profile at fixed network and \(K\). No statement is made about simultaneous limits in graph size and \(\beta\), or about general heterogeneity inside each part. Priority against unindexed or inaccessible historical publications remains open for independent review.

## References

1. J. Wu, R. Abebe, C. Mendler--Dünner, *Opinion Dynamics in Learning Systems* (v1, 2026-03-12), revised as *Reaching a Consensus in Predictive Loops* (v2, 2026-05-06), arXiv:2603.12137. https://arxiv.org/abs/2603.12137 ; https://arxiv.org/pdf/2603.12137 .
2. *Invariant-weight polarization contraction and a minimal counterexample in predictive opinion loops*, publicly indexed mathematical finding, 2026-10-18, https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-invariant-weight-polarization-contraction-and-a-minimal-countere--1f26affbf64c/RESULT.md .
3. M. Boudourides, *Boundary-Value Friedkin--Johnsen Dynamics and Influence-Based Centralities on Networks*, arXiv:2602.08704, first public 2026-02-09; https://arxiv.org/abs/2602.08704 .
4. N. Friedkin and E. Johnsen, *Social influence and opinions*, Journal of Mathematical Sociology 15 (1990), 193--205. Classical FJ mechanism.
