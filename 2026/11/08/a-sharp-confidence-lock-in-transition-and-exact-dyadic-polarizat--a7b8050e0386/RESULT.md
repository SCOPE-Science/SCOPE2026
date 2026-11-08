# A sharp confidence lock-in transition and exact dyadic polarization clocks in directed random-time opinion dynamics

## Finding

A minimal three-agent random-time bounded-confidence network has a singular confidence threshold. With two fixed opposing source opinions, a central agent becomes permanently receptive to exactly one source almost surely for every \(1/2<c<1\), but continues fluctuating without almost-sure convergence when \(c\ge 1\). Along the natural dyadic confidence sequence \(c_m=1-2^{-m}\), \(m\in\mathbb Z\), \(m\ge2\), the exact mean waiting time until permanent removal of one directed influence is

\[
\mathbb E T_{c_m}=\frac{2^m-3}{2\lambda}.
\]

The fact that this time diverges as \(c\uparrow1\) explains why finite-duration simulations near the all-active threshold can resemble persistent disagreement even though eventual polarization is almost sure. The model-specific exact clock, rather than the standard Bernoulli stationary law by itself, is the asserted contribution.

## Assumptions and scope

There are three agents: agents \(L\) and \(H\) maintain opinions \(0\) and \(1\) for all time, and a flexible agent has opinion \(X(0)=1/2\). There are exactly two directed edges \(L\to X\) and \(H\to X\), no edges entering \(L\) or \(H\), and no other edges. Each edge has an independent rate-\(\lambda\) Poisson process for \(\lambda>0\). The source clocks never cease ringing, even if an update is rejected.

At a low-source event, the flexible opinion is replaced by \(X/2\) exactly when \(X<c\); otherwise it is unchanged. At a high-source event it is replaced by \((X+1)/2\) exactly when \(1-X<c\); otherwise it is unchanged. The confidence inequality is **strict** and \(c>0\). All statements concern this specific asymmetric, directed, three-agent model, not general bounded-confidence graphs.

Let \(N_c\) count **all source-clock rings**, including the ring at which the first rejection-generating region is entered, up to the first time the flexible opinion is outside the interval \((1-c,c)\). Let \(T_c\) be the continuous-time clock time of that ring. For \(1/2<c<1\), this is exactly the first instant when one edge becomes permanently inactive; before this instant both influence edges are active. The number of actual opinion changes through that instant also equals \(N_c\). For \(c_m=1-2^{-m}\), write \(N_m=N_{c_m}\).

## Proof

**1. Embedded fair marks and the three confidence regimes.** The superposition of the two rate-\(\lambda\) Poisson clocks has rate \(2\lambda\); its independent marks \(B_j\in\{0,1\}\) are fair and independent. Before any edge is rejected, the opinion immediately after the \(n\)-th event is

\[
X_n=2^{-(n+1)}+\sum_{j=1}^{n}2^{-(n-j+1)}B_j.
\]

For \(0<c\le1/2\), both sources initially lie at distance \(1/2\) and the strict inequality rejects both forever. If \(1/2<c<1\), both are active exactly on the open interval \((1-c,c)\). Once \(X\le1-c\), the high source is forever rejected, whereas the low source continues to be accepted; accepted low events contract \(X\) toward \(0\). The symmetric statement holds if \(X\ge c\). Thus an exit from \((1-c,c)\) is irreversible. No finite accepted sequence reaches a source exactly, but infinitely many subsequent same-source events occur almost surely and force convergence to its opinion.

For any \(c<1\), choose an integer \(L\) so that \(2^{-L}\le1-c\). If \(L\) consecutive low-source events occur while both edges are still active, their composition sends any opinion in \([0,1]\) to at most \(2^{-L}\), hence forces exit. Disjoint blocks of \(L\) fair marks are all low with probability \(2^{-L}\), independently. Therefore exit occurs almost surely, with finite mean event count by geometric domination. Interchanging low and high sources reflects every trajectory about \(1/2\), so the probabilities of the two eventual opinions are both \(1/2\).

For \(c\ge1\), both edges remain active at every finite time because the flexible opinion remains strictly between \(0\) and \(1\). Thus the embedded recursion is \(X_n=(X_{n-1}+B_n)/2\). Every fair mark occurs infinitely often. If \(X_n\) converged, subsequences of zero marks and one marks would force the same limit to satisfy simultaneously \(x=x/2\) and \(x=(x+1)/2\), an impossibility. In distribution, however, the uniform law on \([0,1]\) is invariant: the two maps take a uniform random variable to uniforms on the two half-intervals. Coupling to a stationary uniform state with the same marks gives

\[
W_1(\mathcal L(X(t)),\operatorname{Uniform}[0,1])\le\mathbb E[2^{-K(t)}]\le e^{-\lambda t},
\]

where \(K(t)\sim\operatorname{Poisson}(2\lambda t)\) is the number of clock rings. The uniform stationary-law fact is standard and is not asserted to be new.

**2. Exact coding of the dyadic exit.** Fix an integer \(m\ge2\) and set \(c_m=1-2^{-m}\). The all-active interval is \((2^{-m},1-2^{-m})\). For fewer than \(m-1\) marks, the embedded formula necessarily lies inside this interval. After precisely \(m-1\) marks, the path exits if and only if all those marks agree; a constant zero word lands exactly at \(2^{-m}\), and a constant one word lands at exactly \(1-2^{-m}\), which are rejected boundaries. At any step \(n\ge m\), provided no earlier exit occurred, the path exits if and only if its **last \(m\) marks are all identical**. Indeed, \(m\) low marks produce a value below \(2^{-m}\), while \(m\) high marks produce one above \(1-2^{-m}\); a mixed block of length \(m\) gives a value strictly between these bounds. This classification follows directly from the binary expansion displayed above; no approximation is involved.

Let \(W_m\) be the first index at which an iid fair binary word contains \(m\) identical consecutive marks. Its classical exact mean is \(\mathbb E W_m=2^m-1\). For completeness, write \(E_r\) for the expected remaining number of marks when the current run has length \(r\), for \(1\le r\le m\), and \(E_m=0\). Conditioning on the next mark gives

\[
E_r=1+\tfrac12E_{r+1}+\tfrac12E_1\quad(1\le r<m),\qquad E_r=2^m-2^r.
\]

Starting with no mark, \(\mathbb E W_m=1+E_1=2^m-1\). For our confidence-exit clock, \(N_m=W_m\) unless the *first \(m-1\) marks* are identical. That exceptional event has probability \(2^{2-m}\). Conditional on it, the system exits at time \(m-1\), whereas the ordinary \(m\)-run clock has expected additional duration \(E_{m-1}=2^{m-1}\). Consequently,

\[
\mathbb E N_m=\mathbb E W_m-2^{2-m}E_{m-1}=2^m-3.
\]

The event marks are independent of the Poisson waiting times, which have mean \(1/(2\lambda)\). Conditioning on \(N_m\) therefore gives

\[
\mathbb E T_{c_m}=\frac{\mathbb E N_m}{2\lambda}=\frac{2^m-3}{2\lambda}.
\]

In particular the result includes the boundary case \(m=2\), where the very first interaction removes one edge, giving \(\mathbb E T_{3/4}=1/(2\lambda)\).

**3. Divergence at the threshold.** Couple all confidence values using the same marked event stream and the same virtual pre-exit all-active recursion. The first exit index from \((1-c,c)\) is nondecreasing in \(c\). For any \(c\in[c_m,c_{m+1}]\),

\[
\frac{2^m-3}{2\lambda}\le\mathbb E T_c\le\frac{2^{m+1}-3}{2\lambda}.
\]

Because \(1-c_m=2^{-m}\), this implies \(\mathbb E T_c=\Theta((1-c)^{-1})\) as \(c\uparrow1\). This is an order statement, not a claim of a universal limiting prefactor at arbitrary nondyadic confidence levels.

## Verification

The accompanying standalone `verify.py` implements an **independent finite-state run-length recurrence** to calculate \(\mathbb E N_m\) by exact rational arithmetic for \(2\le m\le20\) and compares it with the closed form. It checks selected boundary-state binary expansions with exact fractions and the first-event case. The recurrence results are corroborative finite checks only: the argument above proves the statement for all integers \(m\ge2\) and all stated confidence values. Run `python verify.py`; expected output is `VERIFY_OK`.

## Relationship to prior work

Chu and Porter [1] supply the directed, strictly thresholded, independent-renewal-edge update convention used here and study its dynamics, but do not state the two-opposed-fixed-source dyadic exit-time formula. Acemoglu, Como, Fagnani and Ozdaglar [2] establish persistent disagreement for gossip with stubborn sources **without confidence rejection**, so their setting corresponds to the always-active mechanism, not the finite irreversible edge exit. Cao and Cortez [3] analyze stationary Bernoulli convolutions, explicitly including a uniform law at halfway compromise; that invariant distribution is credited here rather than claimed as new. Li, Luo and Porter [4] analyze heterogeneous and adaptive confidence in different discrete-time models. The elementary fair-run mean \(2^m-1\) is classical; the strict confidence boundary makes the first-run exception yield the distinct offset \(-3\). A related published record analyzes logarithmic switching near a deterministic, seven-agent, nonfreezing bounded-confidence example, whereas this exact clock is for a three-agent random-time absorbing configuration.

## Limitations

The theorem assumes an initially centered single flexible agent, two fixed opposing sources, equal independent exponential-clock rates, strict confidence, exactly halfway compromises, and the directed update rule. It does not classify unequal rates, other initial conditions, non-Poisson waiting times, arbitrary networks, or confidence-dependent stationary laws outside this model. Uniform limiting distribution at \(c\ge1\) means convergence **in law**, not sample-path convergence. The dyadic formulas and inverse-gap order do not give an exact nondyadic distribution or universal inverse-gap constant. Novelty is subject to unindexed equivalent work or more detailed treatments of stubborn-source bounded-confidence specializations; independent expert verification remains outstanding.

## References

1. W. Chu and M. A. Porter, *Bounded-confidence opinion models with random-time interactions*, arXiv:2409.15148v1 (first public 2024-09-23), https://arxiv.org/abs/2409.15148; multiple-process update rule, Section III.1.
2. D. Acemoglu, G. Como, F. Fagnani, and A. Ozdaglar, *Opinion fluctuations and disagreement in social networks*, arXiv:1009.2653, https://arxiv.org/abs/1009.2653; Section 2 and stubborn-source disagreement.
3. F. Cao and R. Cortez, *Fractal opinions among interacting agents*, arXiv:2408.01624, https://arxiv.org/abs/2408.01624; Section 4.1, Proposition 4.3.
4. G. J. Li, J. Luo, and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563, https://arxiv.org/abs/2303.07563.
