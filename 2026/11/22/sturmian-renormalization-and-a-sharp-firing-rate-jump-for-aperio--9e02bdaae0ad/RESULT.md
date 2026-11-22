# Sturmian renormalization and a sharp firing-rate jump for aperiodic opportunity clocks

## Finding

Consider a neuron that can fire only at an aperiodic set of temporal opportunities. For a constant reset-to-threshold travel time \(c\), its post-spike firing law is the forward-projection recursion
\[
t_{j+1}=\Pi_{\mathbb T}^{+}(t_j+c),\qquad
\Pi_{\mathbb T}^{+}(v)=\min\{u\in\mathbb T:u\ge v\}.
\]
For the two-gap Sturmian clocks specified below, the entire interval \(0<c\le b\) splits into two analytically solvable regimes. Passing through the short-gap duration \(a\) causes a strict firing-rate discontinuity, while the output interspike word remains Sturmian with an explicit change of slope.

Write \(\bar g=a\alpha+b(1-\alpha)\) and \(\beta=\alpha/(1-\alpha)\). For every starting firing opportunity, the rate \(\nu(c)=\lim_{N\to\infty}N/(t_N-t_0)\) exists and equals
\[
\boxed{\nu(c)=\begin{cases}
1/\bar g,&0<c\le a,\\
(1-\alpha)/\bar g,&a<c\le b.
\end{cases}}
\]
Thus \(\nu(a)-\lim_{c\downarrow a,\ c>a}\nu(c)=\alpha/\bar g\). In the first regime the successive physical interspike intervals form a mechanical Sturmian word of slope \(\alpha\) over the lengths \(a,b\). In the second regime, after at most one interspike interval, they form a mechanical Sturmian word of slope \(\beta\) over the lengths \(a+b,b\). Both are aperiodic, balanced, and have exactly \(n+1\) distinct factors of each positive length \(n\).

The cumulative physical timing errors obey strict, all-horizon bounds: in the first regime
\[
|t_N-t_0-N\bar g|<b-a,\qquad N\ge1,
\]
and, for any synchronized spike \(t_*\) in the second regime,
\[
|t_{*+N}-t_*-N(b+a\beta)|<a,\qquad N\ge1.
\]
Here \(t_{*+N}\) means the firing occurring \(N\) spikes after \(t_*\), not addition of real indices.

## Assumptions and scope

Fix \(0<\alpha<1/2\) irrational, \(\theta\in[0,1)\), and positive real \(a<b\). Define
\[
s_i=\lfloor(i+1)\alpha+\theta\rfloor-\lfloor i\alpha+\theta\rfloor\in\{0,1\},\qquad i\in\mathbb Z.
\]
Define \(u_0=0\) and the unique bilateral strictly increasing sequence \((u_i)_{i\in\mathbb Z}\) by \(u_{i+1}-u_i=a\) if \(s_i=1\), and \(u_{i+1}-u_i=b\) if \(s_i=0\). Its opportunity set \(\mathbb T=\{u_i:i\in\mathbb Z\}\) is a nonempty closed subset of \(\mathbb R\) unbounded in both directions; the gap lengths are bounded away from zero.

Consider any \(0<c\le b\) and begin at an arbitrary event \(t_0\in\mathbb T\). Subsequent event times follow the displayed forward-projection recurrence. This is the post-first-spike law of the structure-preserving constant-input leaky integrate-and-fire model of Kaymakçalan and Selçuk, provided its biophysical parameters yield classical travel time \(c\). No claim is made about the first spike generated from an arbitrary initial membrane potential, nor about travel times larger than \(b\).

## Proof

**1. Isolated short gaps.** Let \(r_i=\{i\alpha+\theta\}\in[0,1)\). Mechanical coding gives \(s_i=1\) exactly when \(r_i\in[1-\alpha,1)\). Since \(0<\alpha<1/2\), such a phase is sent by addition of \(\alpha\) modulo one into \([0,\alpha)\subset[0,1-\alpha)\). Thus \(s_i=s_{i+1}=1\) is impossible, for every integer \(i\).

**2. First regime.** When \(0<c\le a\), every opportunity gap is at least \(c\), so the next firing is always \(u_{i+1}\). The number of short gaps in the next \(N\) opportunities from index \(i\) is
\[
S_N=\sum_{j=i}^{i+N-1}s_j
=\lfloor(i+N)\alpha+\theta\rfloor-\lfloor i\alpha+\theta\rfloor.
\]
In particular \(|S_N-N\alpha|<1\), and the elapsed time is \(Nb-(b-a)S_N\). This proves the rate and the bound \(|t_N-t_0-N\bar g|<b-a\). Irrational rotation coding has exactly \(n+1\) factors of length \(n\); alternatively, the \(n+1\) partition intervals determined by the \(n\) distinct backward orbit points of the cut give this standard Sturmian complexity.

**3. Synchronization after at most one firing.** Define the eligible event indices
\[
E=\{i\in\mathbb Z:s_{i-1}=0\}
=\{i:r_i\in[\alpha,1)\}.
\]
If \(i\notin E\), then \(r_i\in[0,\alpha)\), forcing \(s_i=0\). For \(a<c\le b\), the next spike is at \(i+1\), which belongs to \(E\). For \(i\in E\), if \(s_i=0\), the next spike is at \(i+1\), also in \(E\), with interval \(b\). If \(s_i=1\), the gap \(a<c\) is skipped, the following gap must be \(b\), and the next spike is at \(i+2\) after interval \(a+b\). This target also lies in \(E\). Hence \(E\) is forward-invariant for the spike-index map and attracts every starting event in at most one firing.

**4. First-return rotation and exact Sturmian renormalization.** On the eligible phase interval \(I=[\alpha,1)\), the event-index dynamics induces the first return of the circle rotation \(r\mapsto\{r+\alpha\}\). When \(r\in[\alpha,1-\alpha)\), this return uses one event step and sends \(r\) to \(r+\alpha\). When \(r\in[1-\alpha,1)\), it uses two steps and sends \(r\) to \(r+2\alpha-1\). Rescale \(I\) by \(y=(r-\alpha)/(1-\alpha)\). The two branches become precisely
\[
y\longmapsto\{y+\beta\},\qquad\beta=\frac{\alpha}{1-\alpha}\in(0,1).
\]
The two-step (long-interval) branch corresponds to \(y\in[1-\beta,1)\). Consequently, from any synchronized phase \(y_0=\eta\in[0,1)\), the subsequent long-interval indicators are
\[
w_j=\lfloor(j+1)\beta+\eta\rfloor-\lfloor j\beta+\eta\rfloor.
\]
Irrationality of \(\beta\) follows because a rational \(\beta\) would make \(\alpha=\beta/(1+\beta)\) rational. This is an aperiodic mechanical Sturmian word, and its factor complexity is \(n+1\) for each \(n\ge1\).

**5. Timing and rates.** The next \(N\) interspike intervals in the synchronized tail sum to \(Nb+aW_N\), where
\[
W_N=\sum_{j=0}^{N-1}w_j=\lfloor N\beta+\eta\rfloor-\lfloor\eta\rfloor.
\]
As \(|W_N-N\beta|<1\), the strict bound \(|t_{*+N}-t_*-N(b+a\beta)|<a\) follows. Dividing by \(N\) gives mean interspike duration \(b+a\beta\), hence rate \(1/(b+a\beta)=(1-\alpha)/\bar g\). The possible one-spike synchronization transient cannot change this asymptotic rate. The difference of the two rate values at \(c=a\) is \(\alpha/\bar g>0\), which is the claimed sharp jump.

## Verification

The accompanying standalone `check_sturmian.py` uses exact rational arithmetic to generate mechanical words, event times and the forward-projection spike recurrence for 204 rational parameter/phase combinations, four travel times in the two regimes, and eight starting events for each trial. It compares each actual jump with the asserted first-return code and verifies the exact time-error bounds. It additionally checks a 70-digit approximation to the golden slope over 2,500 induced symbols, obtaining factor complexity \(n+1\) for every tested \(1\le n\le12\). The finite numerical tests are diagnostics: the proof above, not the finite bounds, establishes the irrational and all-horizon statements.

For a concrete golden-clock choice, \(\alpha=(3-\sqrt5)/2=\varphi^{-2}\), with \(\varphi=(1+\sqrt5)/2\); then \(\beta=\varphi^{-1}\) and the exact rates are \(1/(a/\varphi^2+b/\varphi)\) and \(1/(b+a/\varphi)\).

## Relationship to prior work

Kaymakçalan and Selçuk (2026) derive the general post-first-spike forward-projection recurrence on arbitrary Hilger time scales. Their lattice example has one regular interspike interval. The result here specializes their time-scale law to an explicitly nonperiodic, two-gap opportunity clock and determines the complete first two firing-rate regimes, timing discrepancy, and exact recoded aperiodic output language. The induced-circle-rotation and Sturmian-factor-complexity ingredients themselves are classical, and no priority over those ingredients is claimed. Marzantowicz and Signerska (2011) study a different firing-map model under almost-periodic continuous-time forcing rather than a discrete opportunity clock. Peltomäki (2019) develops classical Sturmian combinatorics, not the physical firing-rate transition for this opportunity-clock model.

## Limitations

The complete rate law is proved only for \(0<c\le b\), only for irrational \(0<\alpha<1/2\), and for exactly two distinct positive event gaps. It does not address stochastic input, refractory periods, nonconstant reset-to-threshold travel times, or travel times exceeding the longer gap. The precise rotation induction is elementary but known; the contribution is the explicit connection to projected spiking, its sharp threshold and discrepancy bounds. Related prior results outside the inspected literature may cover an equivalent special case. Independent review has not been performed.

## References

1. B. Kaymakçalan and B. İ. Selçuk, *Structure-Preserving Leaky Integrate-and-Fire Dynamics on Arbitrary Time Scales*, arXiv:2611.17219v1, first posted 2026-11-12. https://arxiv.org/html/2611.17219v1
2. W. Marzantowicz and J. Signerska, *Firing map of an almost periodic input function*, arXiv:1106.3309, 2011. https://arxiv.org/abs/1106.3309
3. J. Peltomäki, *Abelian periods of factors of Sturmian words*, arXiv:1905.06138, 2019. https://arxiv.org/abs/1905.06138
4. M. Morse and G. A. Hedlund, *Symbolic Dynamics II: Sturmian Trajectories*, 1940 (classical Sturmian rotation coding and factor complexity).
