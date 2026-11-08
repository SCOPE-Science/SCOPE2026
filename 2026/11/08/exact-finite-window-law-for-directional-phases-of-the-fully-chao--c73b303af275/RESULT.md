# Exact finite-window law for directional phases of the fully chaotic logistic map

## Finding

Let \(F(x)=4x(1-x)\) on \([0,1]\), started from its invariant arcsine probability \(d\nu(x)=dx/[\pi\sqrt{x(1-x)}]\). Define the directional sign \(S_j\) to be \(+1\) if \(F^{j+1}(x)>F^j(x)\), and \(-1\) otherwise. Equality occurs with probability zero at every time. The entire stationary sign process is exactly a first-order Markov chain with states \((+1,-1)\), transition matrix and stationary probabilities

\[
P=\begin{pmatrix}\tfrac12&\tfrac12\\1&0\end{pmatrix},\qquad
\boldsymbol\pi=(\tfrac23,\tfrac13).
\]

In particular, for every \(m\ge1\) and every sign word \(s_0\ldots s_{m-1}\),

\[
\nu\{S_0=s_0,\ldots,S_{m-1}=s_{m-1}\}
=\pi_{s_0}\prod_{j=0}^{m-2}P_{s_j s_{j+1}}.
\]

Thus precisely the finite words avoiding consecutive negative signs have positive probability. This is a statement about **all finite-dimensional stationary distributions**, not merely a two-symbol frequency or a list of forbidden words.

For \(T\ge1\) put \(K_T=\#\{0\le j<T:S_j=-1\}\) and \(M_T=T^{-1}\sum_{j=0}^{T-1}S_j=1-2K_T/T\). The exact finite-time counting generating function is

\[
\mathbb E[z^{K_T}]=\boldsymbol\pi D(z)(PD(z))^{T-1}\mathbf1,
\quad D(z)=\operatorname{diag}(1,z),\quad\mathbf1=(1,1)^\mathsf T.
\]

Its coefficient of \(z^k\) is the exact probability of \(k\) downward steps in a \(T\)-step observation. All covariances and the finite-window variance are

\[
\mathbb E[S_j]=\frac13,\qquad
\operatorname{Cov}(S_0,S_k)=\frac89\left(-\frac12\right)^k
\quad(k\ge0),
\]
\[
\boxed{\operatorname{Var}(M_T)=\frac8{27T}+\frac{32}{81T^2}\bigl(1-(-\tfrac12)^T\bigr).}
\]

The entropy rate of this two-symbol observation is \(\frac23\log2\), strictly below the source map's metric entropy \(\log2\). Its finite-word support is the golden-mean (no consecutive negative symbols) shift, of topological entropy \(\log[(1+\sqrt5)/2]\).

## Assumptions and scope

The parameter is exactly four. The initial state has the absolutely continuous invariant arcsine distribution. Statements about probabilities and stationarity use this distribution; they are not exact finite-time laws for a deterministic point mass initial condition. Natural logarithms are used for entropy. The sign at exceptional fixed-point/preimage states is immaterial because their invariant measure is zero. No spatial coupling, perturbation, observational error, or parameter uncertainty is assumed.

## Proof

**Conjugacy and threshold.** Write \(x=\sin^2(\pi t/2)\) for \(0\le t\le1\). The map \(F\) is conjugate to the symmetric full tent map \(Q(t)=2\min\{t,1-t\}\). Lebesgue measure in \(t\) corresponds to \(\nu\) in \(x\), and is invariant under \(Q\). Since \(F(x)-x=x(3-4x)\), the positive sign interval in tent coordinates is \(I_+=[0,2/3)\); the negative interval is \(I_-=(2/3,1]\). Boundaries and all their preimages are null sets.

**Full-branch decomposition.** The tent map has these monotone pieces, each mapping bijectively *onto* the indicated target sign interval, with slope magnitude two:

\[
[0,\tfrac13]\longrightarrow I_+;\qquad
[\tfrac13,\tfrac12]\longrightarrow I_-;\qquad
[\tfrac12,\tfrac23]\longrightarrow I_-;\qquad
[\tfrac23,1]\longrightarrow I_+.
\]

The first three pieces have source sign \(+\); the fourth has source sign \(-\). These are the complete lists, up to endpoints. In particular, the only sign transitions are \(+\to+\), \(+\to-\), and \(-\to+\). Under Lebesgue measure conditioned on \(I_+\), the first has probability \((1/3)/(2/3)=1/2\), the next two together have probability \((1/3)/(2/3)=1/2\); conditioned on \(I_-\), its only transition is to \(I_+\), with probability one.

**Higher-order conditional law.** We prove by induction over the length of any positive-probability sign history that, given that history, the current tent coordinate is uniform on the interval indexed by its final sign. This is true for a one-symbol history because the initial tent coordinate is uniform. Given the assertion at one time, restrict to any permitted next sign and pull the appropriate full branches back. Every branch has slope magnitude two and maps *onto the full target interval*. Consequently its pushforward conditional law is uniform on the target interval; a mixture of these identical uniform laws is again uniform. This completes the induction, proving the full word formula for every \(m\), not just pairwise transitions. Both stationary probabilities are immediate from the lengths of \(I_+\) and \(I_-\), or by solving \(\boldsymbol\pi P=\boldsymbol\pi\).

**Finite sampling and correlations.** With \(D(z)=\operatorname{diag}(1,z)\), multiplying the initial state by its weight and then each transition by the next state's weight yields the generating matrix product as written. The nontrivial eigenvalue of \(P\) is \(-1/2\); the mean sign is \((2/3)-(1/3)=1/3\), and the centered sign variance is \(1-(1/3)^2=8/9\). Therefore the covariance at lag \(k\) is \((8/9)(-1/2)^k\). In the finite sum \(\sum_{j=0}^{T-1}S_j\), expanding the variance gives

\[
\operatorname{Var}(M_T)=\frac8{9T^2}\left[T+2\sum_{k=1}^{T-1}(T-k)(-\tfrac12)^k\right].
\]

Summation of this geometric-arithmetic series gives the claimed exact formula. The entropy rate is the stationary mean of the row entropies: \((2/3)\log2+(1/3)\cdot0\). All words avoiding \(--\) have strictly positive product probability; their counts satisfy the Fibonacci recurrence, which yields the golden-mean support and its topological entropy. The process entropy is less than \(\log2\) because two symbols of a deterministic map need not retain all information carried by the original orbit.

## Verification

The accompanying `CHECK.py` uses exact rational arithmetic and the independent circle representation \(x=\sin^2(\pi z)\), with \(z\mapsto2z\pmod1\). It partitions \([0,1]\) at every preimage of the directional threshold \(z\in\{1/3,2/3\}\) through the requested word length, computes exact cylinder lengths, and compares these with the proposed Markov products. It verifies all nonzero cylinder probabilities through length eleven, the full counting-polynomial distribution, means, finite-window variances, and covariances through lag nine. Execute `python CHECK.py`; expected final line is `VERIFY_OK checks=646 exact rational cylinders through length 11`. The proof, rather than this finite check, establishes assertions for arbitrarily long words.

## Relationship to prior work

The direction-phase observable and its time average were introduced in Wang, Liu and Hu (2000), later analyzed around crises by Shrimali and Ramaswamy (2002), and used as a prediction target by Dixit, Chauhan and Shrimali (2026). Their publicly inspected treatments address net directional order and learning across parameters; the present claim instead gives a complete stationary distribution at the endpoint parameter four, including exact finite-window fluctuations. Hirata and Amigó (2023) present symbolic dynamics and exact frequencies for length-three ordinal patterns of the same logistic map. Those frequencies already yield the two-step sign probabilities, but a finite table of ordinal frequencies does not establish the first-order conditional law for *all* histories or the resulting every-window generating function. It is also previously known that downward signs cannot be adjacent, and that their typical frequency is one third; neither fact by itself determines arbitrary cylinder probabilities. The tent-map conjugacy and Markov-state calculations are standard mathematical tools, not claimed as inventions.

## Limitations

This is an exact benchmark for the uncoupled, parameter-four map in stationarity, not a theorem about an arbitrary logistic parameter or the coupled-map-lattice transition. It predicts no machine-learning system's accuracy and gives no nonstationary finite-time distribution from a prescribed starting point. The literature comparison leaves a priority risk from specialized earlier treatments of ordinal Markov codings and the full 2002 crisis paper, which was not accessible for complete inspection. No external independent validation or historical-priority certification is asserted.

## References

1. S. Dixit, S. Chauhan and M. D. Shrimali, *Predicting Phase Ordering in Chaotic Maps and Coupled Map Lattices* (2026), arXiv:2609.00983, first posted 2026-09-01. https://arxiv.org/abs/2609.00983
2. W. Wang, Z. Liu and B. Hu, *Phase Order in Chaotic Maps and in Coupled Map Lattices*, Physical Review Letters 84, 2610–2613 (2000), doi:10.1103/PhysRevLett.84.2610.
3. M. D. Shrimali and R. Ramaswamy, *Phase Ordering at Crises*, Physics Letters A 295, 273–279 (2002), doi:10.1016/S0375-9601(02)00179-2.
4. Y. Hirata and J. M. Amigó, *A review of symbolic dynamics and symbolic reconstruction of dynamical systems*, Chaos 33 (2023), doi:10.1063/5.0146022.
5. E. W. Weisstein, *Logistic Map--r=4*, MathWorld. https://mathworld.wolfram.com/LogisticMapR=4.html
