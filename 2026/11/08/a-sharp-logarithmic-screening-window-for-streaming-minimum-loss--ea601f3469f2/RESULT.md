# A sharp logarithmic screening window for streaming minimum-loss SGD

## Finding

For independent fresh batches of noisy scalar observations, selecting the observation of *smallest current squared loss* creates a sharp three-phase law when the screening batch grows logarithmically. Let \(0<\beta<1/2\) be the outlier probability, \(\alpha=1-\beta\), and let \(k_t=\lceil c\log(t+1)\rceil\) for \(t\ge1\), with \(c>0\). Define

\[
c_{\mathrm{entry}}=\frac{1}{\log(1/\beta)},\qquad
c_{\mathrm{escape}}=\frac{1}{\log(1/\alpha)},
\qquad 0<c_{\mathrm{entry}}<c_{\mathrm{escape}}.
\]

For the streaming minimum-loss gradient algorithm specified below, with a clean solution at \(0\), the following mutually exclusive cases hold from either initial state \(0\) or \(d\):

1. If \(0<c\le c_{\mathrm{entry}}\), the iterates visit both \(0\) and the corrupted value \(d\) infinitely many times almost surely, **even though** \(\Pr\{X_t=d\}\to0\).
2. If \(c_{\mathrm{entry}}<c\le c_{\mathrm{escape}}\), then almost surely \(X_t=0\) for every sufficiently large \(t\); this is the *exact almost-sure recovery window*.
3. If \(c>c_{\mathrm{escape}}\), then \(X_t\) stabilizes almost surely at a random value \(X_\infty\in\{0,d\}\), and both outcomes have strictly positive probability. In particular, incorrect permanent lock-in is possible from either starting state.

Thus increasing the number of candidate observations can worsen *pathwise* robustness: too little screening permits infinitely many corruptions; too much screening prevents recovery from an incorrectly selected observation. The critical endpoints are exact, including equality.

More generally, for any deterministic positive-integer sequence \(k_t\to\infty\), write
\[
P=\sum_{t\ge1}\beta^{k_t},\qquad Q=\sum_{t\ge1}\alpha^{k_t}.
\]
The exact classification is: \(Q=\infty\), \(P<\infty\) if and only if almost-sure eventual clean recovery; \(P=\infty\) if and only if infinitely many switches almost surely; and \(Q<\infty\) if and only if almost-sure stabilization with positive probabilities for both final labels. When \(Q=\infty\), the corrupted-state probability tends to zero as long as \(k_t\to\infty\), independently of whether paths converge.

For a fixed screening batch \(k_t\equiv k\), the corrupted-state stationary probability is exactly
\[
\pi_{\mathrm{bad}}(k)=\frac{\beta^k}{\alpha^k+\beta^k},
\]
and the nontrivial transition eigenvalue is \(1-\alpha^k-\beta^k\).

## Assumptions and scope

Take \(d>0\) and an i.i.d. stream \(B_{t,j}\in\{0,d\}\) with \(\Pr\{B_{t,j}=0\}=\alpha>\beta=\Pr\{B_{t,j}=d\}>0\), independent across times \(t\ge1\) and within each fresh candidate batch \(1\le j\le k_t\). At step \(t\), consider the individual convex quadratic losses
\[
f_{t,j}(x)=\tfrac12(x-B_{t,j})^2.
\]
Select any index of minimum loss and take one unit-length stochastic-gradient step:
\[
X_t=X_{t-1}-f'_{t,j_t}(X_{t-1})=B_{t,j_t},
\qquad j_t\in\arg\min_{1\le j\le k_t} f_{t,j}(X_{t-1}).
\]
Ties between observations with the same label do not matter. The initial point may be any real number; after the first update the process belongs to \(\{0,d\}\), and every classification concerns the subsequent chain. For the two-sided final-state probability statements, initial conditions are stated after this first projection as either \(0\) or \(d\). Screening is **with replacement from a fresh population**, not a finite subset without replacement. Each gradient step minimizes one selected quadratic exactly. The clean objective is \(x\mapsto x^2/2\), not the corrupted population mean loss.

## Proof

**Exact reduction.** At state \(X_{t-1}=0\), the selected observation is clean if at least one of the \(k_t\) candidates is clean. The state jumps to \(d\) precisely when *every* candidate is corrupted, with probability \(p_t=\beta^{k_t}\). At state \(X_{t-1}=d\), the corrupted candidates have zero loss, so a jump to \(0\) requires *all* candidates to be clean, with probability \(q_t=\alpha^{k_t}\). Hence the exact time-dependent transition matrix, with rows and columns ordered \((0,d)\), is
\[
K_t=\begin{pmatrix}1-p_t&p_t\\q_t&1-q_t\end{pmatrix}.
\]
Since \(k_t\ge1\) and \(\alpha+\beta=1\), \(0<p_t,q_t<1\) and \(p_t+q_t\le1\). For a constant \(k\), solving \(\pi K=\pi\) gives the stated unique invariant probability and second eigenvalue.

**Almost-sure recovery when \(P<\infty\) and \(Q=\infty\).** The event of a \(0\)-to-\(d\) transition at time \(t\) is contained in the event that the entire fresh batch is corrupted, whose probability is \(p_t\). Thus Borel--Cantelli implies that only finitely many \(0\)-to-\(d\) transitions occur almost surely if \(P<\infty\). For any deterministic \(T\), conditional on \(X_T=d\), the probability of remaining at \(d\) for all future steps is
\[
\prod_{t>T}(1-q_t)=0
\]
when \(Q=\infty\). A countable union over \(T\) shows that no trajectory can eventually remain at \(d\). Since entries into \(d\) are almost surely finite, the path must reach \(0\) and stay there eventually.

**Infinite switching when \(P=\infty\).** As \(\alpha>\beta\), \(q_t\ge p_t\), so \(Q=\infty\). For every deterministic \(T\), the probability of staying forever at \(0\) conditional on \(X_T=0\) is \(\prod_{t>T}(1-p_t)=0\); the corresponding forever-at-\(d\) probability is \(\prod_{t>T}(1-q_t)=0\). On a two-state sequence, finitely many changes mean eventual constancy. Taking the countable union over potential last-change times, the path must therefore switch infinitely often almost surely.

**Permanent-lock-in regime when \(Q<\infty\).** Here \(P\le Q<\infty\). The chance of switching at step \(t\), irrespective of the state distribution, is at most \(p_t+q_t\); hence the expected total number of switches is finite. Consequently only finitely many switches occur almost surely, and the state stabilizes. From initial \(d\), the event of never leaving \(d\) has probability \(\prod_{t\ge1}(1-q_t)>0\). From initial \(0\), the event of first moving to \(d\) and never leaving afterward has probability at least \(p_1\prod_{t\ge2}(1-q_t)>0\). Reversing the labels shows that clean final lock-in also has strictly positive probability from either initial state. Positivity of the infinite products follows from summability and \(0<p_t,q_t<1\).

**Convergence in probability in the recurrent regime.** Write \(u_t=\Pr\{X_t=d\}\), \(s_t=p_t+q_t\) and \(r_t=p_t/s_t\). The Markov recurrence is exactly
\[
u_t=(1-s_t)u_{t-1}+s_t r_t.
\]
If \(k_t\to\infty\), then \(r_t=[1+(\alpha/\beta)^{k_t}]^{-1}\to0\). If \(Q=\infty\), then \(\sum_t s_t=\infty\); products of \(1-s_t\) over any sufficiently late tail tend to zero. For every \(\varepsilon>0\), choose \(T\) so that \(r_t<\varepsilon\) after \(T\). Iterating the convex-combination recurrence gives \(\limsup_t u_t\le\varepsilon\), hence \(u_t\to0\). This remains valid when the path visits \(d\) infinitely often.

**Sharp logarithmic cutoffs.** For any \(0<z<1\),
\[
z(t+1)^{-c\log(1/z)}\le z^{\lceil c\log(t+1)\rceil}\le (t+1)^{-c\log(1/z)}.
\]
Therefore \(\sum_t z^{k_t}\) diverges if and only if \(c\log(1/z)\le1\). Applying this once with \(z=\beta\) and once with \(z=\alpha\) produces the two displayed critical slopes. Since \(\alpha>\beta\), the good-state escape cutoff is strictly larger, so the recovery interval is nonempty; both endpoint conventions follow from divergence of the harmonic series. The general classification proves all three regimes.

## Verification

The standalone standard-library program `verify.py` verifies the exact transition probabilities by exhaustive enumeration of all candidate-label batches through size eight for four rational corruption probabilities. It independently propagates inhomogeneous two-state probabilities, checks the constant-screening eigenvalue/stationary-law identity as an exact rational equality and verifies ordering and monotonicity of the logarithmic thresholds. Executing `python3 verify.py` from the package reports `PASS: 952 exact-rational and deterministic consistency checks`. These finite tests check algebraic implementation; the almost-sure and infinite-time assertions follow solely from the proof above.

## Relationship to prior work

Shah, Wu and Sanghavi (2020) introduce minimum-\(k\)-loss SGD, analyze the scalar quadratic outlier setting for fixed screening size, and explicitly observe that increasing the screening size can trap the method near an outlier. That **fixed-size trapping observation and the loss-selection mechanism are prior art**, not claimed here. Battaglia et al. (2026) establish finite-horizon guarantees with logarithmic fresh-sample screening for a different *quantile Kaczmarz* rule under streaming Massart noise. Haddock, Ma and Rebrova (2026) analyze fixed-size lower-quantile loss filtering over finite sampled index sets. The new assertion is a complete, sharp **time-inhomogeneous, pathwise** classification for growing \(k_t\) in the fresh-batch minimum-loss quadratic model, including the exact open/closed logarithmic recovery interval and the gap between convergence in probability and eventual almost-sure recovery.

Classical Borel--Cantelli and time-inhomogeneous two-state Markov arguments supply the proof tools, not a previously asserted application-specific classification. Broad Markov-chain ergodicity criteria may imply portions of the behavior, and unindexed equivalent specializations cannot be ruled out.

## Limitations

The two observation centers have identical unit quadratic curvature and the step size is exactly one. The outlier fraction is strictly below one half; batches are independent and freshly sampled with replacement; the schedule is deterministic. A pathwise theorem for general convex losses, finite-data sampling without replacement, variable curvature or step sizes other than one is not established. Exact almost-sure recovery does not assert a computational optimum for the screening cost, and convergence in probability must not be read as eventual pathwise correctness.

## References

1. V. Shah, X. Wu and S. Sanghavi, *Choosing the Sample with Lowest Loss Makes SGD Robust*, AISTATS/PMLR 108 (2020), arXiv:2001.03316. https://arxiv.org/abs/2001.03316
2. E. Battaglia, J.-F. Cai, J. Chen, A. Ma, D. Needell and T. Wu, *Quantile Randomized Kaczmarz for Streaming Linear Systems with Massart Noise*, first public submission 2026-08-28, arXiv:2608.27968. https://arxiv.org/abs/2608.27968
3. J. Haddock, A. Ma and E. Rebrova, *Quantile-based Loss Filtering for Outlier-Robust Stochastic Gradient Descent*, first public submission 2026-09-11, arXiv:2609.13040. https://arxiv.org/abs/2609.13040
4. D. Coppersmith and C. W. Wu, *Conditions for Weak Ergodicity of Inhomogeneous Markov Chains*, Statistics & Probability Letters 78 (2008), 3082--3085, DOI:10.1016/j.spl.2008.05.012 (general context, not a claimed application-specific predecessor).
