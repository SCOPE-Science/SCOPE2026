# A six-state visibility threshold for binary observation of irreversible Markov circulation

## Finding
Consider a homogeneous continuous-time nearest-neighbor walk on the cyclic states \(\mathbb Z/n\mathbb Z\), with clockwise rate \(a>0\) and counterclockwise rate \(b>0\). A detector records only a fixed binary label \(Y_t=f(X_t)\in\{0,1\}\), not the state or the directed jumps. Begin the walk in its uniform stationary law.

**Sharp state-count threshold.** For every \(3\le n\le5\), every binary labeling \(f\), and all \(a,b>0\), the *entire continuous-time binary observed process* is reversible under time reversal. This remains true when \(a\ne b\), for which the unobserved steady entropy-production rate is \((a-b)\log(a/b)>0\). At \(n=6\), for the labeling
\[
(f(0),f(1),f(2),f(3),f(4),f(5))=(1,1,0,1,0,0),
\]
the observed process is irreversible whenever \(a\ne b\). In fact, with
\[
\Delta(\varepsilon)=\Pr(Y_0=Y_{\varepsilon}=Y_{3\varepsilon}=1)-\Pr(Y_0=Y_{2\varepsilon}=Y_{3\varepsilon}=1),
\]
one has the sharp short-time expansion
\[
\boxed{\Delta(\varepsilon)=\frac{(a-b)(a^2+ab+b^2)}6\varepsilon^3+O(\varepsilon^4),\qquad\varepsilon\downarrow0.}
\]
Thus three observations at unequal successive time gaps suffice to reveal the direction of circulation in the smallest possible homogeneous ring, for every nonzero bias. Two-time binary observations never reveal a stationary arrow, and three equally spaced binary observations never reveal it either. A four-frame equally spaced readout can express the same signal, since the difference between the probabilities of binary words `1101` and `1011` equals \(\Delta(\varepsilon)\).

## Assumptions and scope
The state count is an integer \(n\ge3\); clockwise and counterclockwise jump rates \(a,b\) are constant across all bonds, strictly positive, and time independent. Time is continuous, and the initial state is uniform on the \(n\) states. Observed labels are a deterministic, fixed mapping into exactly two possible values, although one of the values may not occur. The time-reversed observed path reverses the chronological order but does not change the binary label. The result concerns stationary path distributions rather than pathwise reversibility of the hidden walk. No claim is made about heterogeneous rings, additional jump channels, imperfect detectors, or arbitrary \(n>6\) labelings.

Writing the row generator as
\[
Q_{i,i+1}=a,\quad Q_{i,i-1}=b,\quad Q_{ii}=-(a+b),
\]
with indices modulo \(n\), both the row and column sums of \(Q\) vanish. Hence \(\pi_i=1/n\) is stationary and is unique by irreducibility. The time-reversed generator is \(Q^\mathsf T\), which exchanges \(a\) and \(b\). Stationary edge current is \((a-b)/n\) and cycle affinity is \(n\log(a/b)\), giving the stated entropy production.

## Proof
**1. Reflection symmetry implies complete invisibility.** If a reflection \(R_j:i\mapsto j-i\pmod n\) preserves the coloring \(f\), then conjugating the walk by \(R_j\) exchanges clockwise and counterclockwise jumps but leaves the observed labels unchanged. The stationary time reversal also exchanges the rates. Consequently, the original and time-reversed binary processes have identical finite-dimensional distributions at *every* set of observation times. For \(n\le5\), after possibly complementing both output labels, every binary coloring has at most two marked vertices. Any set of zero or one marked vertex is reflection-invariant. For two marked vertices \(u,v\), reflection \(i\mapsto u+v-i\pmod n\) exchanges them. Therefore every binary coloring on every ring of size three, four, or five has the required reflection, proving the full no-go statement.

**2. The six-state witness is asymmetric.** The marked sites \(\{0,1,3\}\subset\mathbb Z/6\mathbb Z\) have successive clockwise gaps \((1,2,3)\). Reversing orientation gives \((3,2,1)\), not a cyclic rotation of \((1,2,3)\), so no reflection preserves the marking. This observation alone is *not* used to infer irreversibility; the following exact calculation supplies the witness.

**3. A three-time finite-dimensional witness.** Let \(f=(1,1,0,1,0,0)^\mathsf T\), \(D_f=\operatorname{diag}(f)\), and
\[
F(t,s)=\Pr(Y_0=Y_t=Y_{t+s}=1)=\frac16 f^\mathsf T e^{tQ}D_f e^{sQ}f.
\]
The time-reversed comparison of \(F(t,s)\) is \(F(s,t)\), by stationarity. Expand the matrix exponentials at \(t,s=0\). The coefficients antisymmetric under exchange of \(t,s\) vanish through total degree two: for example, \(f^\mathsf T QD_ff=f^\mathsf T D_fQf\), and terms with a zero exponent reduce to a reversible two-time binary event. The leading antisymmetric coefficient is calculated directly from the stated six-by-six generator:
\[
f^\mathsf T QD_fQ^2f-f^\mathsf T Q^2D_fQf=(a-b)(a^2+ab+b^2).
\]
Taylor's factorials and the uniform factor \(1/6\) give
\[
F(t,s)-F(s,t)=\frac{(a-b)(a^2+ab+b^2)}{12}\,ts(s-t)+O((t+s)^4).
\]
Setting \(t=\varepsilon\) and \(s=2\varepsilon\) gives the claimed \(1/6\) coefficient. Since \(a^2+ab+b^2>0\), the difference is nonzero for all sufficiently small positive \(\varepsilon\) whenever \(a\ne b\); moreover its sign identifies which direction has the higher jump rate.

**4. Minimal observation count.** Every stationary binary process, even if non-Markovian, has symmetric two-time probabilities because \(\Pr(Y_0=0,Y_t=1)=\Pr(Y_0=1,Y_t=0)\) by stationarity. For any equally spaced three-frame stationary binary readout, the only nonpalindromic words are `001`/`100` and `011`/`110`. Their probabilities agree by comparing the first and second adjacent-pair marginals and subtracting the common three-fold word. Hence asymmetric successive time gaps are necessary when only three binary frames are read. With four equal-spaced frames, expanding the middle `0` in `1011` and `1101` gives
\[
\Pr(1101)-\Pr(1011)=\Delta(\varepsilon),
\]
which is nonzero for the witness at sufficiently short lag.

## Verification
The standalone `check.py` uses symbolic powers of the six-state generator to reproduce the exact cubic coefficient and explicitly checks all binary labelings for \(n=3,4,5\) (a finite consistency check, not the reason the all-coloring statement holds). It also compares direct matrix-exponential propagators over multiple rates, labelings and times, tests stationarity and two-/three-time identities, and verifies convergence of the observed short-lag asymmetry toward the analytic coefficient. Run `python check.py` with Python, NumPy, SciPy and SymPy. The supplied checker completed 458 assertions. Analytic symmetry and the exact matrix coefficient, rather than finite numerical tests, prove the claims for every permitted positive rate.

## Relationship to prior work
Thermodynamic inference from incomplete observations and cycle-affinity bounds were established in van der Meer, Ertel and Seifert (2022); their principal observations are transitions on selected edges and their waiting times, not a single deterministic binary state partition. Liang and Pigolotti (2023) bound finite-time asymmetry between individually resolved states, which does not imply that an arbitrary two-color projection retains an arrow of time. Blom and collaborators (2023) explain the limitations of lumping and introduce milestoning, while Degünther, van der Meer and Seifert (2023) develop trajectory/snippet approaches and hidden-driving detection. None of the inspected relevant treatments states this homogeneous-ring *six-state minimum together with its explicit three-time binary witness*. Related published results on exact sampled full-state reversibility of biased rings concern a different observation map; full-state asymmetry does not establish a binary readout is asymmetric. This is a bounded literature-comparison finding, not a proof of publication priority.

## Limitations
The threshold is specific to spatially homogeneous nearest-neighbor rings and deterministic binary labelings. Observation noise and discrete sampling at arbitrary fixed intervals can conceal the short-lag witness; it is nonzero only guaranteed at sufficiently small unequal time gaps. The cubic signal may be statistically weak for small bias or coarse sampling. The theorem does not reconstruct the magnitude of the rates from the single asymmetry statistic, establish a lower bound for general nonuniform networks, or assert complete binary-coloring classifications above six states. The originality comparison depends on the inspected literature and remains subject to independent review; no independent scientific validation has been performed.

## References
1. J. van der Meer, B. Ertel, U. Seifert, *Thermodynamic inference in partially accessible Markov networks: A unifying perspective from transition-based waiting time distributions*, Phys. Rev. X 12, 031025 (2022), first public arXiv version 2022-03-22, https://arxiv.org/abs/2203.12020.
2. S. Liang, S. Pigolotti, *Thermodynamic bounds on time-reversal asymmetry*, first public arXiv version 2023-08-28, https://arxiv.org/abs/2308.14497.
3. K. Blom, K. Song, E. Vouga, A. Godec, D. E. Makarov, *Milestoning estimators of dissipation in systems observed at a coarse resolution: When ignorance is truly bliss*, first public arXiv version 2023-10-10, https://arxiv.org/abs/2310.06833.
4. J. Degünther, J. van der Meer, U. Seifert, *Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility*, first public arXiv version 2023-09-14, https://arxiv.org/abs/2309.07665.
