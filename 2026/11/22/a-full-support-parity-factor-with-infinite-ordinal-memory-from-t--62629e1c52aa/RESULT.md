# A full-support parity factor with infinite ordinal memory from two skew tent maps

## Finding
For every pair of real parameters \(0<c,d<1\), the coordinatewise XOR of the consecutive rise/fall signs of two independent, Lebesgue-stationary skew tent trajectories has **infinite Markov order**, although each input sign process is an exact first-order Markov chain and their joint dynamical system is exponentially mixing. The parity observation has full binary symbolic support; its infinite memory is **not** a forbidden-word phenomenon.

More quantitatively, set \(a=1-c\), \(b=1-d\), \(D=(2-c)(2-d)\) and, for each integer \(n\ge1\),
\[
F_n=\Pr(U_0=U_1=\cdots=U_{n-1}=0).
\]
Then
\[
F_1=\frac{1+ab}{D},\qquad F_2=\frac{2ab+cd}{D},\qquad
F_{n+2}=cdF_{n+1}+abF_n,
\]
and the **exact, nonvanishing, alternating Hankel defect** is
\[
\boxed{F_nF_{n+2}-F_{n+1}^2=
\frac{ab(c+d-2cd)^2}{D^2}(-ab)^{n-1}\ne0\quad(n\ge1).}
\]
In particular the continuation probabilities \(r_n=F_{n+1}/F_n\) satisfy \((-1)^{n-1}(r_{n+1}-r_n)>0\) for all \(n\ge1\) and converge exponentially to
\[
\lambda_+=\frac{cd+\sqrt{c^2d^2+4ab}}2.
\]

## Assumptions and scope
For each \(t\in(0,1)\), define the full-branch skew tent map
\[
T_t(x)=\begin{cases}x/t&0\le x\le t,\\(1-x)/(1-t)&t<x\le1.\end{cases}
\]
Lebesgue probability on \([0,1]\) is invariant: both inverse branches have constant contraction factors \(t\) and \(1-t\), which sum to one. Choose \(X,Y\) independently with this distribution. At times \(j\ge0\), write
\[
S^c_j=\mathbf1_{\{T_c^{j+1}(X)>T_c^j(X)\}},\qquad
S^d_j=\mathbf1_{\{T_d^{j+1}(Y)>T_d^j(Y)\}},\qquad
U_j=S^c_j\oplus S^d_j.
\]
The sign \(1\) is an ascent, and \(\oplus\) denotes addition modulo two. Equal consecutive values form null events, so tie conventions do not affect the laws. The process is stationary. The asserted Markov-order obstruction is probabilistic, under the given stationary measure, not a claim of non-sofic symbolic support.

## Proof
**1. Each input sign stream is exactly first-order Markov.** Put \(u_t=1/(2-t)\). A rise is equivalent, up to endpoints, to the current coordinate lying in \(I_1=(0,u_t)\), while a decline means \(I_0=(u_t,1)\). The admissible one-step transitions have the following full affine subbranches, each of which maps onto the **entire** destination sign interval:

- \(I_0\to I_1\): the right branch on \((u_t,1)\);
- \(I_1\to I_1\): the left branch on \((0,tu_t)\);
- \(I_1\to I_0\): the left branch on \((tu_t,t)\) and the right branch on \((t,u_t)\).

Because every finite allowed sign cylinder is the union of compositions of such full affine inverse branches, conditional on **any** finite observed sign history, the present coordinate is uniform on its current \(I_0\) or \(I_1\). Thus the entire sign stream has the stationary two-state Markov law, with state order \(0,1\),
\[
P_t=\begin{pmatrix}0&1\\1-t&t\end{pmatrix},\qquad
\pi_t=\left(\frac{1-t}{2-t},\frac1{2-t}\right).
\]
This is a full-history assertion, not just a one-step transition calculation.

**2. Exact equal-sign survival law.** Independence gives a four-state joint Markov chain for the pairs \((S_j^c,S_j^d)\), with transition matrix \(P_c\otimes P_d\), and stationary law \(\pi_c\otimes\pi_d\). The parity symbol \(U_j=0\) is observed exactly at hidden states \((0,0)\) and \((1,1)\). On those two states, in that order, the substochastic transition matrix and unnormalized initial row are
\[
Q=\begin{pmatrix}0&1\\ab&cd\end{pmatrix},\qquad
w=\frac1D(ab,1).
\]
Hence for every \(n\ge1\),
\[
F_n=wQ^{n-1}\binom11.
\]
Since \(Q^2=cdQ+abI\), the recurrence and first two values follow immediately.

**3. Exact Hankel defect.** Write \(H_n=F_nF_{n+2}-F_{n+1}^2\). Direct substitution of the initial values and recurrence yields
\[
H_1=\frac{ab(c+d-2cd)^2}{D^2}.
\]
The same recurrence implies the Cassini identity \(H_{n+1}=-abH_n\). Thus the boxed identity holds for every positive integer. Its prefactor is strictly positive because \(a,b>0\) and \(c+d-2cd=c(1-d)+d(1-c)>0\). As \(F_n>0\),
\[
r_{n+1}-r_n=\frac{H_n}{F_nF_{n+1}}\ne0
\]
with alternating sign for every \(n\). The two eigenvalues of \(Q\) are \(\lambda_+>0\) and \(\lambda_-=(cd-\sqrt{c^2d^2+4ab})/2<0\); moreover \(|\lambda_-|<\lambda_+\). Perron theory, or the explicit order-two recurrence, gives \(r_n\to\lambda_+\) with geometric error \(O((|\lambda_-|/\lambda_+)^n)\).

**4. No finite Markov order.** If the stationary parity observation were order-\(m\) Markov for a finite \(m\), every positive-probability all-zero history of length \(n\ge m\) would give the same conditional probability of the next zero: \(r_n\) would be eventually constant. The proved strict inequality for every consecutive pair contradicts this. This works at all interior \(c,d\), without exceptions or genericity assumptions.

**5. Full symbolic support and exponential mixing.** Hidden state \((1,1)\) admits a positive self-transition and can move with positive probability to either \((1,0)\) or \((0,1)\). A run of parity ones is possible by alternating \((1,0)\leftrightarrow(0,1)\); either of those states can return to \((1,1)\), and all such transitions are positive. Thus every finite binary parity word has strictly positive cylinder probability, proving that the closed output support is the full two-shift. Each \(P_t\) is irreducible and aperiodic (its \(1\to1\) self-loop has positive probability); their product is primitive. Its stationary output factor is therefore exponentially strongly mixing, by domination of total-variation mixing coefficients. This supplies a full-support exponentially mixing process that nevertheless has no finite Markov order.

## Verification
The standalone \(\texttt{verify_parity_skew.py}\) uses Python 3's standard-library exact rational arithmetic. It determines the marginal probabilities of finite rise/decline words by independent backward iteration of the **original piecewise affine interval maps**, taking exact inverse images and intersections with the rise/decline intervals. It then sums products of these two geometric word probabilities for each equal-sign parity-zero word. For the four rational parameter pairs \((c,d)=(1/2,1/2),(1/3,2/3),(1/4,3/5),(3/7,4/9)\), and lengths \(1\) through \(8\), these independent geometric counts agree exactly with \(wQ^{n-1}\mathbf1\). The script also checks the alternating determinant identity at all computable adjacent indices through those lengths. All **84 exact checks** passed. This is corroboration, not an exhaustive check of all real parameters; the displayed algebra and full-branch argument prove the universal claims.

## Relationship to prior work
Maga and Szepessy (2026) address the complexity of ordinal patterns for Lebesgue-preserving interval maps, principally the asymptotic growth of higher-order permutation entropy rather than the two-source parity factor above. A published exact study of the five three-point ordinal atoms of skew tent maps supplies a five-state Markov representation, but neither introduces independent parity fusion nor derives this infinite-order all-parameter defect. Riechers and Crutchfield (2017) show that hidden Markov processes can exhibit infinite memory and develop general spectral complexity methods, including a distinct Golden-Parity process family. Their general mechanism encompasses the use of a finite hidden transition matrix here; it does **not** give the displayed two-map ordinal XOR construction, determinant, or all-parameter nonvanishing property. The general fact that a hidden Markov factor need not be finite-order Markov is not claimed as new.

## Limitations
The finding assumes independent stationary initial coordinates, two full-branch skew tent maps with \(0<c,d<1\), and error-free consecutive strict-rise observations. It does not address dependent inputs, unequal sampling periods, noisy observations, or boundary parameters. The explicit matrix and Hankel identity do not imply a closed form for the parity entropy rate. The novelty assessment is comparative rather than a certification of priority: an unindexed existing exact treatment of XORs of two golden-mean Markov chains could cover the algebraic statement. All conclusions are mathematical claims requiring independent review before external reliance.

## References
1. B. Maga and S. Szepessy, *The generic behavior of permutation entropy for continuous maps*, arXiv:2611.12789v1, first posted 2026-11-09, https://arxiv.org/abs/2611.12789.
2. *Exact Markov law, spectral decay, and entropy loss for skew-tent ordinal dynamics*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-markov-law-spectral-decay-and-entropy-loss-for-skew-tent-o--2660877e45ea.
3. P. M. Riechers and J. P. Crutchfield, *Spectral Simplicity of Apparent Complexity, Part II: Exact Complexities and Complexity Spectra*, arXiv:1706.00883 (2017), https://arxiv.org/abs/1706.00883.
4. R. J. Ara et al., *Partial Autoinformation to Characterize Symbolic Sequences*, Frontiers in Physiology 9 (2018), https://pmc.ncbi.nlm.nih.gov/articles/PMC6194330/.
