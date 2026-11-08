# Three-valued persistent Markov entropy on vanishing grids of a zero-entropy interval map

## Finding
Let \(f:[0,1]\to[0,1]\) be the continuous, nonincreasing map
\[
f(x)=\max\{0,\tfrac35-2x\}.
\]
For every integer \(N\ge 10\), partition \([0,1]\) into \(N\) equal cells \(I_j=[j/N,(j+1)/N]\), \(0\le j<N\), with common endpoints ignored when assigning measure. Define the **exact uniform-cell transition matrix**
\[
P^{(N)}_{ij}=N\,\operatorname{Leb}\{x\in I_i:f(x)\in I_j\}.
\]
Write \(m=\lfloor3N/5\rfloor\) and \(r=3N-5m\in\{0,1,2,3,4\}\). This matrix has a **unique stationary probability vector**, given by
\[
\pi_0=\tfrac12,\quad \pi_{m-2}=\tfrac{5-r}{20},\quad
\pi_{m-1}=\tfrac14,\quad \pi_m=\tfrac r{20},
\]
with all other entries zero (so the last displayed entry is zero when \(r=0\)). Its stationary Markov Shannon entropy rate, in natural-log units, is exactly
\[
\boxed{\quad h_N=-\frac12\left[
\frac{5-r}{10}\log\frac{5-r}{10}+\frac12\log\frac12+
\frac r{10}\log\frac r{10}\right],\quad r\equiv3N\pmod5,\quad}
\]
using the convention \(0\log0=0\).
The rates take **three distinct positive values** across residue classes:
\[
\begin{aligned}
r=0:&\quad h_N=0.346573590279973\ldots,\\
r=1,4:&\quad h_N=0.471674196164520\ldots,\\
r=2,3:&\quad h_N=0.514826507032287\ldots.
\end{aligned}
\]
In contrast, \(f\) has zero topological entropy. Its physical invariant probability is \(\mu=(\delta_0+\delta_{3/5})/2\), which has zero measure-theoretic entropy. If \(\nu_N\) spreads the mass \(\pi_j\) uniformly through each cell \(I_j\), then \(\nu_N\Rightarrow\mu\) weakly, despite \(h_N\ge(\log2)/2>0\) for all \(N\ge10\) and the absence of an entropy-rate limit.

## Assumptions and scope
All maps, matrices, and partitions are deterministic and exact. The weighting corresponds to uniformly selecting a fresh point within the current cell for each Markov transition, equivalent to infinite sampling in a finite-grid transition model. The stationary entropy is the Shannon entropy rate of this *resampled Markov chain*; it is not the Kolmogorov–Sinai entropy of a coded deterministic trajectory. There is no PageRank teleportation or additional graph filtration. The theorem treats every integer \(N\ge10\) and does not require smoothness beyond continuity and piecewise affinity of \(f\).

## Proof
**1. The deterministic dynamics has zero entropy.** Every iterate \(f^t\) is monotone (increasing for even \(t\), decreasing for odd \(t\)). If \(x_1<\cdots<x_M\) are \((n,\varepsilon)\)-separated, each adjacent pair has at least one iterate \(0\le t<n\) whose images differ by more than \(\varepsilon\). Since each \(f^t\) is monotone and takes values in \([0,1]\),
\[
(M-1)\varepsilon<\sum_{t=0}^{n-1}\sum_{j=1}^{M-1}|f^t(x_{j+1})-f^t(x_j)|\le n.
\]
Thus the separated-set count is \(O(n/\varepsilon)\), and \(h_{\mathrm{top}}(f)=0\).

The fixed point \(1/5\) is repelling. Put \(g=f^2\). Direct calculation gives \(g(x)=0\) for \(0\le x\le3/20\), \(g(x)=4x-3/5\) for \(3/20\le x\le3/10\), and \(g(x)=3/5\) for \(3/10\le x\le1\). For \(3/20<x<1/5\), successive applications of \(g\) strictly decrease until reaching the zero branch in finite time; points below \(3/20\) reach that branch immediately. For \(1/5<x<3/10\), iterations strictly increase until reaching the constant branch, while points at least \(3/10\) reach that branch immediately. Therefore every orbit except that of \(1/5\) enters the two-cycle \(0\mapsto3/5\mapsto0\) after finitely many steps. The two-cycle is the unique physical attractor and \(\mu\) is its physical probability. Its entropy is zero because it has two points.

**2. Exact transition weights.** The image of \(I_0\) is
\[
f(I_0)=[3/5-2/N,3/5].
\]
Multiplying by \(N\), this is \([m+r/5-2,m+r/5]\). Since the slope is \(-2\) throughout \(I_0\), the fractions of inputs mapping to the three successive cells are exactly
\[
P^{(N)}_{0,m-2}=\frac{5-r}{10},\qquad P^{(N)}_{0,m-1}=\frac12,\qquad P^{(N)}_{0,m}=\frac r{10}.
\]
There are no other transitions out of \(I_0\). For \(N\ge10\),
\[
\frac{m-2}{N}\ge\frac35-\frac3N\ge\frac3{10}.
\]
Therefore every target cell with positive weight lies entirely in the constant branch of \(f\), where \(f=0\), and returns to \(I_0\) with probability one. Hence these two or three cells and \(I_0\) form a closed communicating class.

**3. Uniqueness of stationarity.** Every nonempty cell contains an interval of points unequal to \(1/5\) that enter the constant branch after finitely many iterates. Choosing a point away from the finitely many intermediate grid boundaries, and using continuity on the affine branches, yields a positive-measure cylinder of initial points with a finite chain of positive matrix transitions ending at \(I_0\). Thus every state of \(P^{(N)}\) reaches the displayed closed communicating class. A finite Markov chain with only one closed communicating class has a unique stationary probability, and its balance equations give
\[
\pi_0=\tfrac12,\quad\pi_{m-2}=\tfrac12P_{0,m-2},\quad
\pi_{m-1}=\tfrac12P_{0,m-1},\quad\pi_m=\tfrac12P_{0,m}.
\]
This proves the stated vector.

**4. Entropy and limit.** All positive-weight rows in the stationary support except row \(0\) are deterministic. Thus the stationary row-entropy average is exactly one half of the Shannon entropy of the three probabilities in step 2. The residues of \(3N\) modulo \(5\) cycle through all five possibilities as \(N\) increases. Symmetry of Shannon entropy identifies \(r=1\) with \(r=4\), and \(r=2\) with \(r=3\). Strict concavity makes the three levels distinct and orders them as displayed. Finally, \(I_0\) shrinks to \(0\), and the other at most three supporting cells all shrink to \(3/5\), with total mass \(1/2\), proving \(\nu_N\Rightarrow\mu\).

## Verification
Run `python verification/check.py` using Python 3 (standard library only). The program constructs all exact rational row weights for \(10\le N\le200\), tests stochasticity, checks the three-cell formula, proves for each tested matrix that all states can reach \(I_0\), verifies the exact stationary balance equations, and prints the three numerical entropy values. The infinite claim rests on the preceding proof, not on the finite tests.

## Relationship to prior work
Jaworek and Pilarczyk (arXiv:2608.17905v1, Sections 3.1–3.2 and 4.3) use sampled cell transitions, stationary distributions, and a Markov entropy rate to characterize finite-resolution dynamical behavior. The present calculation replaces sampling by its exact uniform-cell probabilities and studies the **nonconvergence** of that particular Markov statistic for a fixed, zero-entropy map. Their paper does not state this example or an all-resolution residue-class formula, and does not assert that finite-grid Markov entropy always converges to deterministic entropy. Froyland's work on Ulam entropy estimates treats additional hyperbolicity requirements; Froyland–Junge–Ochs explicitly distinguish rigorous graph entropy upper bounds from actual symbolic dynamics. None of those notions should be conflated with the entropy rate calculated here.

## Limitations
This is a mathematical boundary example for one continuous piecewise-affine interval map, not evidence of erroneous calculations in any particular numerical experiment. The result does not describe the finite-sampling estimator at a fixed sample count, the PageRank-teleported chain with fixed teleportation, nor the entropy of the full deterministic itinerary process. Weak convergence of the reconstructed invariant measures does not imply entropy convergence. Independent verification and exhaustive historical priority checks have not been performed.

## References
1. W. Jaworek and P. Pilarczyk, *Set-Oriented Approach to the Analysis of Chaotic Itinerancy*, arXiv:2608.17905v1 (publicly posted 2026-08-18), https://arxiv.org/abs/2608.17905 .
2. G. Froyland, *Using Ulam's Method to Calculate Entropy and Other Dynamical Invariants*, *Nonlinearity* **12** (1999), 79–101, https://doi.org/10.1088/0951-7715/12/1/006 .
3. G. Froyland, O. Junge, and G. Ochs, *Rigorous Computation of Topological Entropy with Respect to a Finite Partition*, *Physica D* **154** (2001), 68–84, https://web.maths.unsw.edu.au/~froyland/topentabstract.html .
4. M. Moreau and B. Gaveau, *New Remarks on the Kolmogorov Entropy of Certain Coarse-Grained Deterministic Systems*, *AIMS Mathematics* **8** (2023), 26328–26342, https://doi.org/10.3934/math.20231343 .
