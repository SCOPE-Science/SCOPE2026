# Two disjoint optimal cooperation windows under a shared risk signal

## Finding
In a one-shot, finite-population collective-risk game, the optimal observed-risk policy need not be a monotone tolerance rule. If incumbent conditional cooperators simultaneously change their actions at a common risk cutoff, a best response can strictly prefer cooperation at intermediate and high risks but defection at risks between them. The following theorem gives exact necessary and sufficient conditions and the precise loss from imposing a single upper-tail tolerance.

**Theorem (two-window boundary and monotone-policy regret).** Fix an integer population size \(Z\ge N\ge2\), a quorum \(m\in\{1,\ldots,N\}\), a disaster endowment \(b>0\), a per-contribution cost \(0<c<b\), and a common risk cutoff \(\tau\in(0,1)\). For the focal player's \(Z-1\) possible co-players, specify arbitrary nonnegative integer counts of unconditional cooperators, unconditional defectors, and conditional cooperators who contribute precisely when the **same publicly observed** risk \(R\ge\tau\). The focal individual draws \(N-1\) distinct co-players uniformly without replacement. Risk \(R\) is independent of the draw and uniform on \([0,1]\). Disaster occurs with probability \(R\) if fewer than \(m\) group members contribute; contributions cost \(c\) regardless of success.

Let \(p_-\) and \(p_+\) be the respective probabilities of exactly \(m-1\) cooperating co-players for \(R<\tau\) and \(R\ge\tau\), with the focal's action excluded from those counts. If \(p_-,p_+>0\), put
\[
\alpha=\frac{c}{bp_-},\qquad \gamma=\frac{c}{bp_+}.
\]
The (almost-everywhere unique) optimal observed-risk policy has **exactly two disconnected positive-measure cooperation intervals** separated by a positive-measure defection interval, with the first cooperation interval below \(\tau\) and the second above it, **if and only if**
\[
\boxed{0<\alpha<\tau<\gamma<1.}
\]
In that case it cooperates exactly for \(R\in(\alpha,\tau)\cup(\gamma,1]\), apart from choices at measure-zero boundaries. Among all single-threshold rules that cooperate when \(R\ge t\), for \(t\in[0,1]\), the **exact payoff deficit of the best such rule** relative to the unrestricted best response is
\[
\boxed{\min\!\left\{\frac{bp_-}{2}(\tau-\alpha)^2,\;\frac{bp_+}{2}(\gamma-\tau)^2\right\}>0.}
\]
For every fixed incumbent composition and one cutoff \(\tau\), the set of risks at which contributing is strictly optimal has at most two connected interval components, including when \(p_-=0\) or \(p_+=0\).

**Exact finite-population realization.** Take \(Z=21\), \(N=3\), \(m=2\), \(\tau=1/2\). Apart from the focal individual, there are ten unconditional cooperators, eight incumbent conditional cooperators and two unconditional defectors. Set \(c=3b/19\). Then
\[
\boxed{p_-=\frac{10}{19},\quad p_+=\frac{18}{95},\quad
\alpha=\frac{3}{10},\quad \gamma=\frac56.}
\]
Thus cooperation is strictly preferable precisely for \(R\in(3/10,1/2)\cup(5/6,1]\). Excluding any fixed common observation charge, the unrestricted policy's expected gain over always defecting is \(b/76\), whereas the **best** single-upper-tail policy gains only \(b/380\). The exact policy-class restriction penalty is \(b/95\), and the ratio of these two gross decision gains is five. The two equally optimal upper-tail cutoffs are \(t=3/10\) and \(t=5/6\).

## Assumptions and scope
The quota \(m\) and co-player population composition are fixed; the focal player's choice does not change the actions of other individuals. Risk is shared among all group members, hence all adaptive incumbents change action simultaneously at \(\tau\). Sampling is without replacement from \(Z-1\) possible peers, before the common risk is realized, and is independent of that risk. Strategies are pure measurable risk-contingent choices; because risk has an atomless uniform distribution, behavior at single risk levels has no effect on the objective. A fixed information/observation charge common to every compared risk-observing policy cancels; no claim about whether to purchase that observation is made. These are conditional best-response, not population-evolution or equilibrium, statements.

## Proof
For every possible set of sampled peers, if the number of their contributors is other than \(m-1\), the focal action does not affect the probability of disaster. If exactly \(m-1\) peers contribute, the focal action changes the disaster probability from \(R\) to zero; the saved expected endowment is \(bR\) and its contribution costs \(c\). Hence the expected payoff difference between contributing and defecting, conditional on \(R=r\), is
\[
\Delta(r)=\begin{cases}bp_-r-c,&0\le r<\tau,\\bp_+r-c,&\tau\le r\le1.\end{cases}
\]
The **general pivotal-event calculation** is standard, and also appears, for a different uncertain-quota game, in Fernández Domingos et al. (2026); the present statement concerns the consequences of correlated incumbent responses to the shared *risk*.

For any measurable risk-conditioned policy \(a(r)\in\{0,1\}\), expected payoff relative to never contributing is \(\int_0^1 a(r)\Delta(r)\,dr\). This is maximized pointwise by \(a(r)=1\) iff \(\Delta(r)>0\), uniquely almost everywhere except zeros of \(\Delta\). On each side of \(\tau\), \(\Delta\) is increasing affine if the corresponding pivotal probability is positive, and constant negative if it vanishes. Thus there is at most one cooperation interval on either side. Two nonempty, separated positive-measure cooperation intervals exist precisely when \(\Delta\) crosses zero below \(\tau\), then jumps strictly negative at \(\tau\), and crosses zero again before risk one. This is equivalent to \(0<\alpha<\tau<\gamma<1\), proving necessity, sufficiency and the component bound. In particular \(p_->p_+\) is necessary in this regime.

For the exact payoff-regret formula, write the positive low-risk integral and the magnitude of the intervening negative integral as
\[
E_-=\int_\alpha^\tau\!\Delta(r)dr=\frac{bp_-}{2}(\tau-\alpha)^2,
\qquad E_+=-\int_\tau^\gamma\!\Delta(r)dr=\frac{bp_+}{2}(\gamma-\tau)^2,
\]
and the high-risk positive integral as \(H=\int_\gamma^1\Delta(r)dr>0\). The unrestricted best response earns \(E_-+H\). For an upper-tail threshold \(t\), its gain is \(U(t)=\int_t^1\Delta(r)dr\), with derivative \(U'(t)=-\Delta(t)\) off the sole jump. Its only possible global maxima occur at \(t=\alpha\) and \(t=\gamma\), giving respectively \(E_- - E_+ +H\) and \(H\). The maximum is \(H+\max(0,E_--E_+)\). Subtraction yields exactly \(\min(E_-,E_+)\).

For the 21-person population, among the \(\binom{20}{2}=190\) possible unordered peer pairs, below \(\tau\) exactly one of the ten unconditional cooperators must be selected: \(10(8+2)=100\) pivotal pairs. Above \(\tau\), the eighteen contributing incumbents must be paired with one of the two defectors: \(18\cdot2=36\) pivotal pairs. Therefore \(p_-=100/190=10/19\), \(p_+=36/190=18/95\), and the two zero crossings are \(\alpha=3/10\) and \(\gamma=5/6\). Direct exact integration gives \(E_-=b/95\), \(E_+=b/95\), and \(H=b/380\), proving the claimed policy values and gap.

## Verification
Execute `python verify.py` using Python's standard library. It enumerates all 190 unordered peer pairs using exact fractions, verifies the focal payoff differences at representative risk values on both sides of the cutoff, and checks the exact integration identities, thresholds, best upper-tail choices and strict payoff gap. A finite grid over cutoffs is included only as a supplementary consistency check; the uncountable optimization and exact inequalities follow from the preceding proof, not from grid sampling.

## Relationship to prior work
Zhou, Han, Chen and Szolnoki (2026) introduce a collective-risk model with a shared uncertain risk and incumbent adaptive players using tolerance thresholds; their focus is fixation, mutation and the resulting group achievement. The present theorem studies a unilateral best response allowed to condition arbitrarily on the same risk, for a fixed finite mixed composition, and calculates precisely when it exceeds every monotone-tolerance rule.

Fernández Domingos, Ichinose, Tateishi and Lenaerts (2026), in their model with **uncertain collective quota but fixed disaster risk**, already derive the general marginal-contribution/pivotality formula and the pointwise optimal informed action, so neither of those elementary principles is claimed as original here. Their published main-model analysis does not give the one-shared-risk, synchronized-incumbent two-window classification or the finite-population exact upper-tail regret. Huynh et al. (2026) empirically evaluate risk responsiveness and scripted partners in a different multiround collective-risk game, not the present one-shot exact classification. Shadmehr and Bernhardt (2011) show that uncertainty can lead to nonmonotone individual strategic responses in a different, two-party collective-action game; general nonmonotone responses are not claimed as new. Hilbe et al. (2013) analyze multiround strategic timing, not the uniform-risk best response used here.

## Limitations
This result is a strict *conditional best-response* theorem at a fixed population state, not a Nash equilibrium, evolutionary selection result or welfare-optimal intervention. The observation cost is held fixed across policies; whether acquiring risk information pays is unproved. The full risk distribution is known, uniform and atomless; the co-players observe the same signal and use one common cutoff. With multiple distinct incumbent cutoffs, more than two cooperation windows may exist, outside the stated two-component bound. Nonuniform distributions with positive density preserve the pointwise action set but alter the explicit integrated regret. No experimental behavioral prediction, robustness to strategic adjustment by incumbents, or universal historical novelty is asserted. Independent scientific audit has not been performed.

## References
1. Chuanzhi Zhou, Ju Han, Xiaojie Chen and Attila Szolnoki, *Evolutionary dynamics of collective-risk social dilemma game with risk uncertainty and adaptive strategy*, arXiv:2611.07627v1, released 2026-11-05. https://arxiv.org/abs/2611.07627
2. Elias Fernández Domingos, Genki Ichinose, Wakaba Tateishi and Tom Lenaerts, *The Conditional Value of Costly Information in Collective-Risk Dilemmas*, arXiv:2610.33895v1, released 2026-10-24, §3.2, equations (6)–(8). https://arxiv.org/abs/2610.33895
3. Trung-Kiet Huynh et al., *Cooperation Without Adaptation: LLM Agents in a Collective-Risk Dilemma*, arXiv:2610.22882v1, 2026-10-16. https://arxiv.org/abs/2610.22882
4. Farhad Shadmehr and Dan Bernhardt, *Collective Action with Uncertain Payoffs: Coordination, Public Signals, and Punishment Dilemmas*, American Political Science Review (2011), doi:10.1017/S0003055411000359.
5. Christian Hilbe, Maria Abou Chakra, Philipp M. Altrock and Arne Traulsen, *The Evolution of Strategic Timing in Collective-Risk Dilemmas*, PLoS ONE 8(6):e66490 (2013). https://pmc.ncbi.nlm.nih.gov/articles/PMC3682992/
