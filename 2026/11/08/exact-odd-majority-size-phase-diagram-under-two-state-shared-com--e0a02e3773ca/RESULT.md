# Exact odd-majority size phase diagram under two-state shared competence

## Finding

Consider a binary decision whose difficulty is shared by all voters. Conditional on an unobserved good environment of probability \(w\), individual answers are independently correct with probability \(p\); conditional on the other environment, they are independently correct with probability \(q\). Let \(1/2<p<1\), \(0<q<1/2\), and \(0<w<1\). Among odd majority-voting panels of sizes \(2m+1\), for every integer \(m\ge0\), the accuracy admits a **complete global phase classification**: finite maximizing sizes, all adjacent ties, the no-finite-optimum regimes, and a sharp divergence law near the equal-complementary-competence boundary.

Write \(s_p=p(1-p)\), \(s_q=q(1-q)\), and
\[
R=\frac{w(2p-1)s_p}{(1-w)(1-2q)s_q},\qquad z=\frac{s_q}{s_p}.
\]
The exact sign of the difference between the accuracies of \(2m+3\) and \(2m+1\) voters is the sign of \(R-z^m\). Consequently:

- **Peak regime** \(p+q>1\) (hence \(z>1\)). If \(R<1\), one voter is uniquely optimal; if \(R=1\), one and three voters are the only optima; if \(R>1\), let \(\tau=\log R/\log z\). When \(\tau\notin\mathbb Z\), the unique optimum is \(2\lceil\tau\rceil+1\); when \(\tau\in\mathbb Z\), exactly \(2\tau+1\) and \(2\tau+3\) tie for the maximum.
- **Trough regime** \(p+q<1\) (hence \(z<1\)). The accuracy either increases toward its limit or decreases and then increases with at most one (possibly tied) minimum. Its supremum over finite odd panels is \(\max\{wp+(1-w)q,w\}\). A finite maximum exists exactly when \(wp+(1-w)q\ge w\), in which case the unique maximizing size is one voter; otherwise the supremum \(w\) is not attained by any finite panel.
- **Complementary regime** \(p+q=1\) (hence \(z=1\)). The sequence strictly increases if \(w>1/2\), strictly decreases if \(w<1/2\), and equals \(1/2\) at every size if \(w=1/2\).

In the peak regime, a group larger than one is strictly better than one voter exactly when
\[
w>\frac{(1-2q)q(1-q)}{(2p-1)p(1-p)+(1-2q)q(1-q)}.
\]
For each fixed \(0<q<1/2\) and \(1/2<w<1\), as \(p=1-q+\delta\) approaches \(1-q\) from above (\(\delta\downarrow0\)), every optimal odd size \(n_{\mathrm{opt}}\) satisfies
\[
n_{\mathrm{opt}}\sim \frac{2q(1-q)}{1-2q}\,\frac{\log(w/(1-w))}{\delta}.
\]
Thus the optimal finite panel can grow without bound at a quantified inverse-distance rate.

## Assumptions and scope

One task is decided by a strict majority of \(n=2m+1\) exchangeable voters, with \(m\in\mathbb Z_{\ge0}\). A single latent Bernoulli environment is shared by every voter in the panel. Conditional on that environment, votes are independent with common accuracy \(p\) or \(q\). The environment is not observed when choosing panel size, there is no cost penalty for voters, and a new panel is evaluated on the same distribution of tasks. This is not independent voting after the environment is marginalized. Parameters satisfy strict inequalities above; boundary values \(p=1\), \(q=0\), or \(w\in\{0,1\}\) are outside the theorem.

Define
\[
B_m(t)=\Pr\bigl(\operatorname{Bin}(2m+1,t)\ge m+1\bigr),\quad
J_m=wB_m(p)+(1-w)B_m(q).
\]
An "optimal" size is a global maximizer of \(J_m\) over all nonnegative integers \(m\), not a maximizer over an experimentally truncated range. An infinite-size *supremum* is not represented as a finite optimum.

## Proof

**Step 1: exact increment.** Conditioning on the majority among \(2m+1\) voters, then adding two independent voters, gives
\[
B_{m+1}(t)-B_m(t)=\binom{2m+1}{m}(2t-1)[t(1-t)]^{m+1}.
\]
Indeed, a switch from losing to winning requires exactly \(m\) old successes and two new successes, whereas a switch from winning to losing requires \(m+1\) old successes and two new failures; subtracting their binomial probabilities yields the identity, including \(m=0\). By conditional independence, average the two environment-specific identities:
\[
J_{m+1}-J_m=\binom{2m+1}{m}(1-w)(1-2q)s_q^{m+1}\left(Rz^{-m}-1\right).
\]
Every factor preceding the parentheses is positive, and \(z^m>0\); hence \(\operatorname{sgn}(J_{m+1}-J_m)=\operatorname{sgn}(R-z^m)\).

**Step 2: phase and global maxima.** Since
\[
s_q-s_p=(p-q)(p+q-1),
\]
\(z>1\), \(z<1\), and \(z=1\) correspond precisely to the three cases for \(p+q\). If \(z>1\), \(z^m\) strictly increases from one to infinity; thus all increments are negative when \(R<1\), the first is zero and all later are negative when \(R=1\), and otherwise the sign switches exactly once from positive to negative, with a zero increment only when \(R=z^m\) at an integer \(m\). This proves all unique maxima and adjacent ties in the peak regime. The comparison \(R>1\) rearranges to the displayed critical threshold in \(w\).

If \(z<1\), the sequence \(z^m\) decreases from one toward zero, so the increments can only change from negative to positive, never from positive to negative. Moreover, by the elementary binomial law of large numbers, \(B_m(p)\to1\) and \(B_m(q)\to0\), giving \(J_m\to w\). A unimodal trough or monotonic nondecreasing sequence has supremum equal to the larger of its initial value and its limit. When the initial value equals the limiting value, all subsequent finite values are below that value if \(R<1\): the initial strict decrease and subsequent strict increase toward its limit rule out finite equality. When \(R\ge1\), the sequence strictly increases eventually and its limit strictly exceeds its initial value; thus the same finite-maximizer classification holds. In particular, if \(J_0\ge w\), then \(R<1\), so \(m=0\) is uniquely optimal. If \(J_0<w\), no finite maximum exists. If \(z=1\), \(q=1-p\), \(B_m(q)=1-B_m(p)\), and \(J_m=(1-w)+(2w-1)B_m(p)\), giving all three subcases.

**Step 3: long optimal-panel boundary.** Fix \(0<q<1/2\), \(1/2<w<1\). Write \(p=1-q+\delta\), \(0<\delta<q\). Then \(s_p=s_q-(1-2q)\delta-\delta^2\). Thus
\[
\log z=\frac{1-2q}{q(1-q)}\delta+O(\delta^2),\qquad
\log R=\log\frac{w}{1-w}+O(\delta).
\]
For small positive \(\delta\), \(z>1\) and \(R>1\). All maximizing \(m\) are within one of \(\log R/\log z\) by Step 2; using \(n=2m+1\) yields the stated asymptotic. No claim is made about a uniform error bound as \(q\) or \(w\) approaches its own boundary.

**Exact witness.** At \(p=9/10\), \(q=2/5\), \(w=1/2\), one has \(R=3/2\) and \(z=8/3\); so \(0<\log R/\log z<1\) and exactly three voters maximize accuracy globally. The first three accuracies, evaluated without rounding, are \(J_0=13/20\), \(J_1=331/500\), \(J_2=16361/25000\). The sign argument, not enumeration, proves no larger odd panel surpasses \(J_1\).

## Verification

Run `python3 checker.py` with Python 3 and its standard library from the directory containing the file. It independently computes binomial tails in exact rational arithmetic, verifies the conditional binomial-increment identity on 990 rational parameter-index cases, tests the three-regime first-difference sign and single-switch behavior on a rational grid, and checks the exact witness. The packaged run reported `PASS 3095 finite exact rational assertions`. These finite assertions corroborate the algebra; Steps 1–3 prove the statements for arbitrarily large integer \(m\).

## Relationship to prior work

Kao and Couzin (2014) explicitly analyze a shared fluctuating-cue environment with conditional individual accuracies \(r+\varepsilon\) and \(r-\varepsilon\) and shared cue-state probability \(g\). Their reported phase plot shows solitary, intermediate and arbitrarily large best panels. Our \((p,q,w)=(r+\varepsilon,r-\varepsilon,g)\) specializes exactly to that mechanism where the conditional accuracies straddle one half. The novel candidate statement is the closed-form, all-integer optimizer/tie and critical scaling classification, **not** the model or the observation that intermediate panels can outperform larger ones. The inspected open-access indexed text and displayed figure do not state the present increment-sign theorem; the underlying binomial-tail formula makes it a potentially derivable corollary, so independent historical priority still requires verification against complete primary and supplementary texts.

Galesic, Barkoczi and Katsikopoulos (2016 online; 2018 issue) likewise study majority decisions across easy and difficult tasks and motivate the practical importance of panel size. The accessible abstract and institutional account characterize finite optima but do not resolve whether a closed-form exact version already appears in inaccessible pages. Kaniovski and Zaigraev study homogeneous juries with correlated votes, including quota design; no implication from the accessible abstract to this exact shared-environment size phase was established. The present result is limited to its stated conditional-iid mixture and does not cover their general correlation specifications.

## Limitations

Conditional independence is essential; arbitrary positive pairwise voting correlation or endogenous communication is not covered. The theorem optimizes idealized accuracy, not social welfare, representativeness, committee cost or ethical election rules. When there is no finite maximum, the asymptotic supremum is explicitly marked as unattained. Exact source novelty is provisional because a full historical search, all supplements, and one closest relevant 2016 article's complete text were not available; general binomial difference identities are standard. The checker is finite and is not a machine proof of the infinite theorem. Self-review is separate from independent validation, which has not been performed.

## References

1. Kao, A. B. and Couzin, I. D., *Decision accuracy in complex environments is often maximized by small group sizes*, Proceedings of the Royal Society B 281 (2014), article 20133305; first online 2014-04-23. https://doi.org/10.1098/rspb.2013.3305 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4043084/.
2. Galesic, M., Barkoczi, D. and Katsikopoulos, K., *Smaller crowds outperform larger crowds and individuals in realistic task conditions*, Decision 5 (2018), 1–15; online release 2016-05-17. https://doi.org/10.1037/dec0000059 ; https://eprints.soton.ac.uk/439024/.
3. Kaniovski, S. and Zaigraev, A., *Optimal jury design for homogeneous juries with correlated votes*, Theory and Decision, DOI https://doi.org/10.1007/s11238-009-9170-2.
