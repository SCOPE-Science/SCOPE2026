# A sharp inward-drift threshold for survival under rightmost-particle resetting

## Finding

Let \(N\geq 1\) Brownian particles be reset together, at independent Poisson rate \(r>0\), to the largest of their current positions. Between resets each has generator \(D\partial_{xx}-v\partial_x\), where \(D>0\) and \(v\in\mathbb R\). All particles start at \(x>0\); \(\tau\) is the *first* time any reaches zero. Define \(m_N=\mathbb E\max_{1\leq j\leq N}Z_j\) for independent standard normal \(Z_j\), and
\[
  v_c(N,D,r)=\sqrt{\frac{\pi Dr}{2}}\,m_N.
\]
Then, for every \(x>0\),
\[
\Pr_x\{\tau=\infty\}>0\quad\Longleftrightarrow\quad v<v_c(N,D,r),
\qquad
\Pr_x\{\tau<\infty\}=1\quad\Longleftrightarrow\quad v\geq v_c(N,D,r).
\]
The noncapture probability is strictly less than one for every finite \(x>0\) (because the initial Brownian excursion may hit zero before the first reset). In the surviving regime, almost surely on \(\{\tau=\infty\}\), **each** particle has the same exact asymptotic speed:
\[
  \lim_{t\to\infty}\frac{X_j(t)}t=v_c(N,D,r)-v>0
  \quad(1\le j\le N).
\]
The critical drift grows strictly with the particle count, satisfies \(v_c(1,D,r)=0\), \(v_c(2,D,r)=\sqrt{Dr/2}\), and obeys the large-count law
\[
 v_c(N,D,r)\sim\sqrt{\pi Dr\log N}\qquad(N\to\infty).
\]
For \(v<v_c\), the unconditional mean first hitting time is infinite because noncapture has positive probability. No claim about the mean hitting time in the captured phase is made.

## Assumptions and scope

The particles move independently between successive collective resets. A reset occurs at each event of a rate-\(r\) Poisson process independent of all Brownian drivers. Before \(\tau\), the entire group is relocated to the *current* rightmost position, not to its historical maximum or to a fixed site. Absorption is checked continuously during each interreset interval; this is the first-group-hit stopping rule (not the time until a majority hits zero). The model has constant drift \(-v\), *not* the harmonically confined drift \(-kx\). On paths already absorbed no further convention is needed. All quantifiers above apply to every integer \(N\ge1\), \(D,r,x>0\), and real \(v\).

## Proof

**1. Exact embedded random walk.** Put \(T_k\sim\operatorname{Exp}(r)\) for successive interreset durations and take independent standard Brownian motions \(W_{k,j}\), independent across cycles. Build an *unabsorbed reference process* which resets at the same epochs to the rightmost current position, even when a reference trajectory crosses zero. At its \(k\)-th reset all positions equal
\[
 S_k=x+\sum_{i=1}^kY_i,\qquad
 Y_i=-vT_i+\sqrt{2D}\max_{1\le j\le N}W_{i,j}(T_i).
\]
The variables \(Y_i\) are iid, nondegenerate and have finite second moments. Coupling this reference process with the absorbing experiment up to its first hit is exact; in particular, no absorption is equivalent to the event that *all* interreset paths of the reference process stay strictly positive.

Conditional on \(T_i=t\), the Gaussian maximum equals in distribution \(\sqrt t\,M_N\), where \(M_N=\max_j Z_j\). Since \(\mathbb ET_i=1/r\) and \(\mathbb E\sqrt{T_i}=\Gamma(3/2)/\sqrt r=\sqrt\pi/(2\sqrt r)\),
\[
 \mu:=\mathbb E Y_i=\frac{v_c(N,D,r)-v}{r}.
\]
Thus the sign of the *exact* reset-to-reset mean increment is the sign of \(v_c-v\). The expression for \(v_c\) contains no large-\(N\) approximation.

**2. Zero or negative increment mean forces capture.** If \(\mu<0\), the strong law gives \(S_k/k\to\mu<0\), hence some reset-epoch position must be nonpositive, making survival impossible. At \(\mu=0\), the iid increments have strictly positive finite variance and are nondegenerate. The classical one-dimensional centered-random-walk oscillation theorem (equivalently, the law of the iterated logarithm) gives \(\liminf_{k\to\infty}S_k=-\infty\) almost surely, again excluding survival. These conclusions include the equality boundary exactly and do not infer it from numerical simulation.

**3. Positive increment mean allows infinite survival from *every* starting point.** Let
\[
 H_i=\max_{1\le j\le N}\sup_{0\le s\le T_i}
 \bigl[vs-\sqrt{2D}\,W_{i,j}(s)\bigr]\vee0.
\]
This is the greatest drop below the common reset position within interval \(i\). The iid marked pairs \((Y_i,H_i)\) may be internally dependent, but \(H_i\) is independent of increments from *earlier* cycles. For \(r>0\), \(\mathbb E e^{\theta H_i}<\infty\) for sufficiently small positive \(\theta\): bound \(H_i\le |v|T_i+\sqrt{2D}\max_j\sup_{s\le T_i}|W_{i,j}(s)|\) and use Brownian reflection and exponential mixing in \(T_i\). Because \(\mu>0\), there exists such a \(\theta>0\) with \(a=\mathbb E e^{-\theta Y_i}<1\). Set \(b=\mathbb E e^{\theta H_i}<\infty\).

The reference process has no crossing exactly when \(x+\sum_{j<i}Y_j>H_i\) for every \(i\). A union bound and Markov's inequality give the constructive estimate
\[
 1-\Pr_x\{\tau=\infty\}
 \le \sum_{i\ge1}\Pr\!\left\{H_i-\sum_{j<i}Y_j\ge x\right\}
 \le\frac{b}{1-a}e^{-\theta x}.
\]
Here the expectation factorization uses independence of the present-cycle mark from past increments, not any false independence between \(Y_i\) and \(H_i\) within the same cycle. Consequently survival has positive probability from all sufficiently large starting positions. From any \(x>0\), there is a positive probability that the first reset occurs at a finite positive time while every path remains above zero and at least one arrives beyond such a large position. The postreset future is independent of that event; hence survival is positive from **every** \(x>0\).

**4. Exact speed on noncaptured trajectories.** The strong law gives \(S_k/k\to\mu\). The Poisson reset count satisfies \(N_t/t\to r\). For each interreset cycle its maximal absolute drifted Brownian excursion has an exponential tail for sufficiently small exponential parameter (as above); a Borel–Cantelli argument yields excursion amplitude divided by the cycle index converging to zero almost surely. Combining these statements, each reference particle obeys \(X_j(t)/t\to r\mu=v_c-v\) almost surely. The absorbing process coincides with the reference process on \(\{\tau=\infty\}\), establishing the conditional-path statement.

**5. Dependence on group count.** The maximum \(M_N\) grows strictly in mean with \(N\), and \(m_1=0\). For \(N=2\), \(\max(Z_1,Z_2)=(Z_1+Z_2+|Z_1-Z_2|)/2\), yielding \(m_2=1/\sqrt\pi\). The standard Gaussian-maximum asymptotic \(m_N\sim\sqrt{2\log N}\) gives the displayed growth of \(v_c\).

## Verification

The companion script `check.py` directly quadratures the exact finite-\(N\) Gaussian maximum, checks \(m_1=0\), \(m_2=1/\sqrt\pi\) and \(m_3=3/(2\sqrt\pi)\), tests strict monotonicity for small \(N\), and compares the exact single-reset increment expectation to independent simulations under multiple population sizes. It does not certify the zero-drift random-walk theorem or prove infinite-horizon survival; those points are proved above using the random-walk oscillation theorem and the exponential-mark bound.

To reproduce: with Python, NumPy and SciPy installed, execute `python check.py` in the directory containing the complete package. The outputs are finite diagnostics independent of the mathematical proof.

## Relationship to prior work

Lee, Yang and Lizana (2026, arXiv:2604.24406) investigate the *same rightmost-particle reset protocol and the same first-group-hit event* in a harmonic well. The result above instead asks for the **exact absorption-versus-escape boundary under spatially constant inward drift**, including the critical equality and the almost-sure speed of surviving trajectories. Their harmonic quasi-stationary first-passage approximation and finite-horizon numerical data do not establish the present drift phase diagram. Lee, Yang, Park and Lizana (arXiv:2412.02524; Phys. Rev. Research 8, 013227, 2026) develop the more general group-reset kernel and stationary harmonically confined observables; its extreme-value kernel is credited, but neither it nor its stationary mean directly yields this first-passage classification. The special zero-drift subcase \(v=0\) is not singled out as a new conclusion; the assessed extension is the complete **drift-controlled threshold**, the critical equality case and the conditional ballistic law. The novel assertion is the full drift-controlled sharp threshold, including critical capture, and the conditional ballistic speed. Majumdar, Sabhapandit and Schehr (2015) study a *single lattice walker* returning to its historical maximum, not \(N\) walkers resetting to their current maximum; their ballistic law does not imply the present killing boundary.

## Limitations

The analysis applies to independent Brownian particles, constant drift and Poissonian synchronized rightmost resetting, with the first-group-hit absorption criterion. It is not a theorem for harmonic confinement, interacting dynamics, median-group hitting, finite observation censoring, time-dependent reset rates or historical-maximum relocation. It determines whether eventual capture occurs, but not the full absorption-time distribution in either phase. The exponential distance bound is not claimed sharp. Literature inspection cannot exclude unpublished or unindexed equivalent statements. Independent external mathematical validation has not been carried out.

## References

- J. Lee, S.-G. Yang and L. Lizana, *Beyond average: heterogeneous first-passage dynamics in many-particle systems with resetting*, arXiv:2604.24406, first public 27 April 2026. https://arxiv.org/abs/2604.24406
- J. Lee, S.-G. Yang, H. J. Park and L. Lizana, *General theory for group resetting with application to avoidance*, arXiv:2412.02524, first public 3 December 2024; *Physical Review Research* **8**, 013227 (2026). https://doi.org/10.1103/zxff-tkq5
- S. N. Majumdar, S. Sabhapandit and G. Schehr, *Random walk with random resetting to the maximum position*, *Physical Review E* **92**, 052126 (2015). https://doi.org/10.1103/PhysRevE.92.052126
- Standard results employed: strong law, law of the iterated logarithm for iid centered finite-variance random walks, Brownian reflection principle, Borel–Cantelli lemma and Gaussian-maximum asymptotics.
