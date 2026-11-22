# A sharp three-regime local weak-order law for binomial-adjusted tau leaping

## Finding
For the binomial-adjusted \(\theta\)-trapezoidal tau-leaping (B\(\theta\)TTLe) method, an initial pair of successive propensity ratios gives an exact, three-regime classification of the **unconditional** local weak defect. Let \(c_\theta=1-2\theta+2\theta^2\), with \(1/2\le\theta<1\), and write \(r_1=a_1/a_0\), \(r_2=a_2/a_0\). For every bounded real test function, the one-step defect \(D_h(f)=\mathbb E[f(Y_h)]-\mathbb E[f(X_h)]\) obeys:

1. If \(r_1<c_\theta\), then
   \[
   D_h(f)=\frac{a_0(r_1-c_\theta)}{2\theta}\,[f(1)-f(0)]h+O(h^2).
   \]
   Thus even first-order local weak consistency with the original generator fails, with \(f=\mathbf1_{\{1\}}\) a sharp witness.
2. If \(r_1\ge c_\theta>r_2\), set \(p=(r_2+2\theta-1)/(2\theta^2)\), so \(0\le p<1\). Then
   \[
   D_h(f)=\frac{\theta^2a_0^2}{2}h^2\big[(1-p)^2f(0)+2p(1-p)f(1)+(p^2-1)f(2)\big]+O(h^3).
   \]
   Hence the local weak defect is \(O(h^2)\) for every bounded \(f\), but not \(O(h^3)\): take \(f=\mathbf1_{\{2\}}\).
3. If \(r_2\ge c_\theta\), then \(D_h(f)=O(h^3)\) for every bounded \(f\): second-order local weak consistency holds. The condition is sharp.

Since \(r_2\le r_1\) and \(c_\theta=\frac12+2(\theta-\frac12)^2\), the three cases partition the full parameter domain, including equality boundaries. For a ratio \(r\in[1/2,1)\), its crossing occurs exactly at \(\theta_r=(1+\sqrt{2r-1})/2\); ratios below \(1/2\) never cross the safe frontier. In particular, no admissible \(\theta\) gives second-order local weak consistency if \(r_2<1/2\), and none gives even first-order local weak consistency if \(r_1<1/2\).

## Assumptions and scope
Fix a bounded nonincreasing propensity sequence \(a_0\ge a_1\ge\cdots\ge0\) with \(a_0=A>0\), and consider the pure-birth continuous-time chain \(X_t\) on the nonnegative integers, started at zero, with generator \((\mathcal Lf)(j)=a_j[f(j+1)-f(j)]\). The nonnegative sequence can include zeros. The time step is \(h>0\); all asymptotics hold as \(h\downarrow0\) for fixed \(\theta\in[1/2,1)\), fixed propensity sequence and bounded real \(f\). The finite constants in the remainders may depend on these fixed inputs.

Define \(c=c_\theta\) and draw \(P\sim\operatorname{Poisson}(\theta Ah)\). For \(m=P\), set \(r_m=a_m/A\). If \(r_m\ge c\), let
\[
Y_h=m+\operatorname{Poisson}\!\left(\frac{A(r_m-c)}{2\theta}h\right),
\]
with an independent second-stage Poisson variable. Otherwise set
\[
Y_h=\operatorname{Binomial}\!\left(m,\frac{r_m+2\theta-1}{2\theta^2}\right).
\]
These are precisely the single-channel rules of Scott--McCallum--Foster's B\(\theta\)TTLe, including the convention that equality takes the nondegenerate Poisson branch. Each binomial parameter lies in \([0,1]\) because \(\theta\ge1/2\) and \(r_m<c\).

## Proof
Let \(f_j=f(j)\). For the exact chain, bounded rates make the generator bounded on bounded functions. Thus the Markov semigroup has an operator-norm Taylor expansion through degree two, giving
\[
\begin{aligned}
\mathbb P(X_h=0)&=1-Ah+\tfrac12A^2h^2+O(h^3),\\
\mathbb P(X_h=1)&=Ah-\tfrac12 A(A+a_1)h^2+O(h^3),\\
\mathbb P(X_h=2)&=\tfrac12 Aa_1h^2+O(h^3),\\
\mathbb P(X_h\ge3)&=O(h^3).
\end{aligned}
\]
These coefficients follow from \(\mathcal Lf(0)=A(f_1-f_0)\) and \(\mathcal L^2f(0)=Aa_1(f_2-f_1)-A^2(f_1-f_0)\).

For the numerical method, \(P\ge3\) has probability \(O(h^3)\). The second-stage Poisson mean, whenever active, is at most \(A(1-\theta)h\). Thus all contributions through order \(h^2\) are determined by \(P\in\{0,1,2\}\) and the first two conditional Poisson counts. Specifically,
\[
\begin{aligned}
\mathbb P(P=0)&=1-\theta Ah+\tfrac12\theta^2A^2h^2+O(h^3),\\
\mathbb P(P=1)&=\theta Ah-\theta^2A^2h^2+O(h^3),\\
\mathbb P(P=2)&=\tfrac12\theta^2A^2h^2+O(h^3).
\end{aligned}
\]
For \(P=0\), the second-stage rate is \(A(1-\theta)\). If \(r_1\ge c\), then for \(P=1\) the second-stage rate is \(A(r_1-c)/(2\theta)\). A direct multiplication gives
\[
\begin{aligned}
\mathbb P(Y_h=0)&=1-Ah+\tfrac12A^2h^2+O(h^3),\\
\mathbb P(Y_h=1)&=Ah-\tfrac12A^2(1+r_1)h^2+O(h^3),\\
\mathbb P(Y_h=2)&=\tfrac12A^2r_1h^2+O(h^3)
\end{aligned}
\]
**provided also \(r_2\ge c\)**. This establishes the third regime.

If instead \(r_1<c\), the \(P=1\) stage is binomial with success probability \(p_1=(r_1+2\theta-1)/(2\theta^2)\), rather than the nondegenerate update. Comparing its \(O(h)\) mass with the nondegenerate formula changes the probability of state one by \(\theta A(p_1-1)h=A(r_1-c)h/(2\theta)\), with the opposite sign at state zero. This gives the first displayed defect, whose coefficient is nonzero for \(f=\mathbf1_{\{1\}}\).

Finally suppose \(r_1\ge c>r_2\). Then the only change through second order occurs on \(P=2\), with probability \(\theta^2A^2h^2/2+O(h^3)\). The nondegenerate branch would retain its two first-stage jumps at this order. The degenerate branch thins them independently with probability \(p\), producing states zero, one and two with probabilities \((1-p)^2,2p(1-p),p^2\). Subtraction gives the second displayed defect. Because \(p<1\), its \(f=\mathbf1_{\{2\}}\) coefficient is strictly negative. Thus the classifications are necessary as well as sufficient, and no unexamined terms can cancel the stated leading witnesses.

## Verification
Run the embedded `verify.py` with Python and SymPy: `python verify.py`. The checker establishes the ordinary-branch Taylor coefficient identities symbolically for arbitrary \(A,\theta,r_1\), verifies the two defect polynomials, and checks 2,376 exact rational triples in the three regions. These finite tests supplement, but do not replace, the preceding proof.

With \(\theta=1/2\), \(A=1\), \(r_1=1/4\), \(r_2=1/8\), the \(f=\mathbf1_{\{1\}}\) defect starts at \(-h/4\). With \(r_1=3/4\), \(r_2=1/4\), the \(f=\mathbf1_{\{2\}}\) defect starts at \(-3h^2/32\). With \(r_1=3/4\), \(r_2=2/3\), the local defect is \(O(h^3)\) for every bounded test function.

## Relationship to prior work
Scott, McCallum and Foster introduce the binomial-adjusted method, its exact sampling rules and a local-error analysis that treats degenerate reaction channels. Their Theorem 2 states a general \(O(h)\) bound under degenerate-event assumptions; it does not classify the unconditional local weak order by the first two propensity ratios. The present theorem works with the **unconditional** law of one entire completed step from a fixed state; neither a conditional error estimate nor the paper's proposed modified generator is substituted for that law. Earlier \(\theta\)-trapezoidal and binomial tau-leap treatments do not directly cover this new specific binomial-adjusted branch. Standard generator-Taylor calculations are used with attribution rather than claimed as new machinery.

## Limitations
This is a single-channel, fixed-state, bounded nonincreasing pure-birth model, not a theorem for general chemical networks, state-dependent coupled reactions, negative stoichiometries or an adaptive timestep algorithm. An \(O(h^3)\) local weak defect is not by itself a proven global second-order rate, and the classification asserts nothing about finite-step accuracy or optimal runtime. Positivity is built into the single-channel count update but is not a claim about other reaction networks. Priority against unindexed algebraically equivalent special cases is not independently settled.

## References
1. Maximilian Scott, Sam McCallum, and James Foster, *A binomial-adjusted \(\theta\)-trapezoidal tau-leaping method for chemical kinetic systems*, arXiv:2611.16975v1 (first submitted November 12, 2026), https://arxiv.org/html/2611.16975v1, Sections III--IV and Appendix A.
2. Tamás Székely Jr., Kevin Burrage, Radek Erban, and Konstantinos C. Zygalakis, *A higher-order numerical framework for stochastic simulation of chemical reaction systems*, BMC Systems Biology 6:85 (2012), https://pmc.ncbi.nlm.nih.gov/articles/PMC3529698/.
3. Yucheng Hu, Tiejun Li, and Bin Min, *A weak second order tau-leaping method for chemical kinetic systems*, Journal of Chemical Physics (2011), DOI:10.1063/1.3609119.
