# Exact two-opinion Bayesian lock-in and critical slow stabilization

## Finding
Consider a decision maker who alternates between two opinions by retaining the current opinion until its estimated reliability falls below a fixed threshold, then resets their learning history on switching. The **full distribution of the last opinion-change time** is explicitly solvable. A sharp reliability boundary distinguishes endless opinion switches from eventual fixation. In the fixation region the initial, less reliable opinion can retain an absolute majority of final choices, while at the boundary almost-sure fixation has infinite expected stabilization time.

Define, for \(p\in(0,1)\),
\[
 s_p=\max\left\{0,\frac{2p-1}{p}\right\},\qquad
 f_p(z)=\frac{1-\sqrt{1-4p(1-p)z^2}}{2pz}\quad(0<z<1),\quad f_p(0)=0.
\]
When the starting opinion is \(A\) or \(B\), the defective generating functions for the finite **last switch time** \(\tau\) are respectively
\[
 \boxed{G_A(z)=\frac{s_a+s_b f_a(z)}{1-f_a(z)f_b(z)},\qquad
 G_B(z)=\frac{s_b+s_a f_b(z)}{1-f_a(z)f_b(z)}.}
\]
Consequently, switching continues forever almost surely exactly when \(a\le1/2\) **and** \(b\le1/2\). In all other cases an opinion is ultimately fixed almost surely.

When both reliabilities exceed \(1/2\), the probability of permanent choice \(A\), starting from \(A\), is
\[
 \boxed{\mathbb P_A(\text{eventual }A)=\frac{b(2a-1)}{a+b-1}.}
\]
For \(1/2<a<b<1\) the *less* reliable starting opinion wins a strict majority of realizations if and only if
\[
 \boxed{a>\frac{3b-1}{4b-1}.}
\]
For example, at \(a=7/10\), \(b=9/10\), the inferior first option wins with probability \(3/5\). This is a positive-measure parameter region rather than a tie-boundary phenomenon.

At a critical reliability, \(a=1/2<b<1\), the fixation-time tails obey
\[
 \boxed{\begin{aligned}
 \lim_{t\to\infty}\sqrt t\,\mathbb P_A(\tau>t)
 &=\sqrt{\frac2\pi}\frac{b}{2b-1},\\
 \lim_{t\to\infty}\sqrt t\,\mathbb P_B(\tau>t)
 &=\sqrt{\frac2\pi}\frac{1-b}{2b-1}.
 \end{aligned}}
\]
Thus \(\tau<\infty\) almost surely, but \(\mathbb E[\tau]=\infty\) for either initial opinion. The symmetric statement holds when \(b=1/2<a\). Outside these critical lines, any almost-surely finite last-switch time has finite expectation.

## Assumptions and scope
Let the opinion set be \(\{A,B\}\), with respective true experience-success probabilities \(a,b\in(0,1)\). Each experience under opinion \(A\) is independently Bernoulli with parameter \(a\), and analogously for \(B\). Successes and failures in distinct runs are mutually independent; after *every* opinion change the agent forgets the earlier run and draws fresh experience outcomes. At the start of a run the reliability prior is \(\mathrm{Beta}(1,1)\). After \(u\) confirming and \(v\) disconfirming observations in that run, the posterior mean is \((u+1)/(u+v+2)\). The agent retains the current opinion if and only if the posterior mean is at least \(1/2\); on its first strict drop below \(1/2\) it changes to the other opinion and begins a fresh run. At equality it retains the opinion. This is the original paper's solo-agent/no-social-influence special case with equal positive reward and loss, without network effects or warm-up. A decision step is one Bernoulli experience followed by the threshold test.

The last-switch time is \(\tau=\sup\{t\ge1:\text{opinion changes at step }t\}\), taking \(0\) when the set is empty and \(\infty\) if unbounded. A formula \(G(z)=\mathbb E[z^\tau\mathbf1_{\{\tau<\infty\}}]\) is *defective* when eventual fixation is not almost sure. The generating functions above are defined on \(0\le z<1\), extending continuously to \(z=1\) when appropriate. The first-public source is the paper's arXiv version of May 16, 2023 (not its later journal publication).

## Proof
**1. A run is a skip-free gambler's-ruin episode.** After \(u\) successes and \(v\) failures the posterior threshold inequality is precisely \(u-v\ge0\). The signed evidence walk starts at \(0\), increases by \(+1\) on success, decreases by \(-1\) on failure, and the opinion first changes when it first visits \(-1\). Write \(T_p\) for this first-passage time, \(T_p=\infty\) if the walk never hits \(-1\). The classical ballot reflection count of nonnegative paths of length \(2n\) followed by a final down-step gives, for every integer \(n\ge0\),
\[
 \mathbb P(T_p=2n+1)=C_n p^n(1-p)^{n+1},\quad
 C_n=\frac1{n+1}\binom{2n}{n}.
\]
In particular \(T_p\) is odd when finite. The Catalan generating identity \(\sum_{n\ge0}C_nx^n=(1-\sqrt{1-4x})/(2x)\) yields
\[
 f_p(z)=\mathbb E[z^{T_p}\mathbf 1_{\{T_p<\infty\}}]
 =\frac{1-\sqrt{1-4p(1-p)z^2}}{2pz}.
\]
Evaluating at \(z=1\) gives \(f_p(1)=1\) if \(p\le1/2\) and \(f_p(1)=(1-p)/p\) if \(p>1/2\). Hence the probability of a run that never ends is \(s_p=1-f_p(1)\). No independence across *opinions* is assumed beyond independent outcomes in distinct visits; the renewal argument below uses precisely the stated reset rule.

**2. The full stabilization-time law.** A run in opinion \(A\) either lasts forever with probability \(s_a\), giving \(\tau=0\), or lasts a finite time \(T_a\) and is followed by a statistically fresh run under \(B\). Writing \(G_A,G_B\) for the last-switch-time defective generating functions gives the exact renewal system
\[
 G_A(z)=s_a+f_a(z)G_B(z),\qquad
 G_B(z)=s_b+f_b(z)G_A(z).
\]
Solving these two equations gives the displayed closed forms for all \(0\le z<1\). If \(a,b\le1/2\), each individual run ends almost surely; by countable intersection all successive runs end, and switching never ceases. If at least one reliability exceeds \(1/2\), \(s_a+s_b>0\), while \(f_a(1)f_b(1)<1\); therefore \(G_A(1)=G_B(1)=1\), so eventual fixation occurs almost surely. The phase boundary includes the equality cases exactly as stated.

**3. Which opinion ultimately wins.** Let \(L_A^A\) denote the probability of final choice \(A\) starting in \(A\), and \(L_A^B\) its counterpart starting in \(B\). With \(q_p=f_p(1)=1-s_p\), the renewal equations are
\[
 L_A^A=s_a+q_a L_A^B,\qquad L_A^B=q_b L_A^A.
\]
When at least one \(s_p>0\), solving yields \(L_A^A=s_a/(1-q_aq_b)\) and \(L_A^B=q_b s_a/(1-q_aq_b)\). For \(a,b>1/2\), substituting \(s_a=(2a-1)/a\), \(q_a=(1-a)/a\) and their \(b\)-analogues simplifies the first expression to \(b(2a-1)/(a+b-1)\). For \(1/2<a<b\), requiring this to exceed \(1/2\) is exactly \(a(4b-1)>3b-1\). The frontier lies strictly between \(1/2\) and \(b\), since \(b-(3b-1)/(4b-1)=(2b-1)^2/(4b-1)>0\). The exact witness \((a,b)=(7/10,9/10)\) has \(L_A^A=3/5\).

**4. Finite-mean versus critical heavy-tail fixation.** For \(p\ne1/2\), the discriminant of \(f_p(z)\) is strictly positive at \(z=1\), so \(f_p'(1)<\infty\). If at least one \(s_p>0\), differentiating the two closed generating functions at \(z=1\) shows \(\mathbb E[\tau]<\infty\) whenever \(a,b\ne1/2\). On the critical line \(a=1/2<b\), put \(q=(1-b)/b\), \(s=(2b-1)/b=1-q\). Then \(f_{1/2}(z)=(1-\sqrt{1-z^2})/z\) and, as \(z\uparrow1\),
\[
 f_{1/2}(z)=1-\sqrt{2(1-z)}+O(1-z),\qquad f_b(z)=q+O(1-z).
\]
The closed forms become \(G_A(z)=s f_{1/2}(z)/(1-f_{1/2}(z)f_b(z))\), \(G_B(z)=s/(1-f_{1/2}(z)f_b(z))\). Consequently,
\[
 1-G_A(z)\sim \frac{\sqrt{2(1-z)}}s,\qquad
 1-G_B(z)\sim\frac{q\sqrt{2(1-z)}}s.
\]
For any finite nonnegative integer-valued \(\tau\), \((1-G(z))/(1-z)=\sum_{t\ge0}\mathbb P(\tau>t)z^t\). Applying the standard Tauberian transfer for eventually nonincreasing survival probabilities (exponent \(1/2\), \(\Gamma(1/2)=\sqrt\pi\)) establishes the two limits in the finding. Their positive \(t^{-1/2}\) coefficients force infinite expected fixation time even though \(G_A(1)=G_B(1)=1\). Swapping \(A,B\) proves the remaining critical line.

## Verification
The bundled standalone `verify.py` uses only Python standard-library integer arithmetic and rational fractions. It checks Catalan first-ruin path counts by direct independent word enumeration, rational defective first-passage coefficients, a grid of exact renewal identities, the generating-function coefficient equations, the exact suboptimal-win witness, and the fair critical first-passage survival identity \(\mathbb P(T_{1/2}>2n)=\binom{2n}{n}/4^n\). Execute `python verify.py`; its expected final line begins `VERIFY_OK`. Finite checks support transcription and implementation, not proof of the infinite statements, which follow from the four mathematical steps above.

## Relationship to prior work
Meylahn and Searle introduce precisely the experience-based posterior threshold and reset-on-switch dynamics in *Opinion dynamics beyond social influence* (2023 arXiv preprint; 2024 *Network Science*). Their paper models solo and networked agents and studies network outcomes using experiments, without a two-opinion exact final-choice distribution or the last-switch-time generating function. The earlier work *Trusting: Alone and together* by Meylahn, den Boer and Mandjes derives, in a one-institution setting, the **single-run** quit probability using random-walk absorption; its Lemma 3 in particular subsumes the one-run \(s_p\) calculation here. This finding does not claim that gambler's ruin, Catalan enumerations, or renewal generating functions are new. The distinct contribution is their joint consequence for **perpetually reset alternating choices**: the complete fixation phase diagram, a sharp inferior-opinion majority-lock region, and the exact critical stabilization-time tail. The latter are not conclusions about the one-institution exit process because that process ends at its first exit rather than switching into a second competing opinion.

## Limitations
The theorem concerns an isolated agent with exactly two choices and no information sharing or changing network threshold. It does not imply any corresponding outcome for the multi-agent network model or for general Beta priors, non-Bernoulli experiences, asymmetric payoff thresholds, correlated successive episodes, or nonresetting beliefs. The weak conclusion that some less reliable choices can persist is known qualitatively in social learning; the contribution is the exact law for this specified model. One-run exit probabilities and the underlying analytic tools are classical. An unindexed equivalent two-choice alternating-renewal treatment cannot be excluded by literature search; no external independent scientific audit has been performed.

## References
- B. V. Meylahn and C. Searle, *Opinion dynamics beyond social influence*, arXiv:2305.09398v1 (first public May 16, 2023), especially §§2 and 4; final open-access journal version, *Network Science* **12** (2024), 339–365, DOI: 10.1017/nws.2024.14. https://arxiv.org/abs/2305.09398 ; https://doi.org/10.1017/nws.2024.14
- B. V. Meylahn, A. V. den Boer and M. R. H. Mandjes, *Trusting: Alone and together*, arXiv:2303.01921v1 (2023), especially §3.2, Lemma 3 (one-run quit probability). https://arxiv.org/abs/2303.01921
- Classical reflection principle/Catalan first-passage enumeration; standard monotone Tauberian theorem for generating functions (background results, not claimed as new).
