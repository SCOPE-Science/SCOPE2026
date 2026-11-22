# Logarithmic Dirichlet concentration: Gumbel coupon completion and terminal rarity

## Finding
For each integer \(q\ge2\), draw a random categorical probability vector
\(P^{(q)}=(P_1,\ldots,P_q)\sim\operatorname{Dirichlet}(a_q,\ldots,a_q)\).
Conditional on this vector, sample independent categorical labels with probabilities \(P_i\), and let \(T_q\) be the first sample count at which every label has appeared. Assume
\[
\frac{a_q}{\log q}\longrightarrow\kappa\in(0,\infty).
\]
Define
\[
b_q=q a_q\big(q^{1/a_q}-1\big),\qquad
s_q=q^{1+1/a_q}.
\]
For every fixed real \(x\), the number \(U_q(m)\) of labels still unseen after \(m=\lfloor b_q+s_qx\rfloor\) draws converges to \(\operatorname{Poisson}(e^{-x})\). Consequently,
\[
\frac{T_q-b_q}{s_q}\xrightarrow{d}G,\qquad
\Pr(G\le x)=\exp(-e^{-x}).
\]
The explicit centering and scale satisfy
\[
\frac{b_q}{q\log q}\longrightarrow\kappa(e^{1/\kappa}-1),\qquad
\frac{s_q}{q}\longrightarrow e^{1/\kappa}.
\]
Let \(I_q\) be the label discovered last (almost surely unique in discrete sampling). Then its *latent*, before-sampling probability satisfies
\[
qP_{I_q}\xrightarrow{\mathbb P}e^{-1/\kappa}.
\]
In particular the normalized completion time and normalized latent mass converge jointly to \((G,e^{-1/\kappa})\). Although a uniformly chosen label has \(qP_i\to1\) in probability, the last missing label has a strictly smaller limiting relative mass.

## Assumptions and scope
The shape parameters \(a_q\) are arbitrary positive real numbers subject to the displayed logarithmic-concentration limit; their exact integrality is not required. The random vector is sampled once per \(q\) and held fixed while labels are drawn. The conclusion is annealed (averages over both the random probabilities and sampled labels). The variable \(U_q(m)\) counts zero-frequency labels, not singleton observations. In the asymptotic statements \(q\to\infty\), \(x\in\mathbb R\) and \(\kappa\in(0,\infty)\) are fixed. The centering and scale use the actual \(a_q\), not an unquantified approximation \(a_q=\kappa\log q\).

## Proof
Write \((z)^{\uparrow m}=z(z+1)\cdots(z+m-1)\) with \((z)^{\uparrow0}=1\), and \((q)_{\downarrow r}=q(q-1)\cdots(q-r+1)\). If a specified set of \(r<q\) labels is unseen after \(m\) draws, conditioning on the Dirichlet probabilities and applying the beta-sum identity gives the *exact* probability
\[
\Pr(\text{these }r\text{ labels unseen})
=\frac{((q-r)a_q)^{\uparrow m}}{(qa_q)^{\uparrow m}}.
\]
Therefore the \(r\)th falling factorial moment of the unseen count is
\[
\mathbb E[(U_q(m))_{\downarrow r}]
=(q)_{\downarrow r}\prod_{j=0}^{m-1}
\left(1-\frac{r a_q}{qa_q+j}\right).
\tag{1}
\]
For each fixed positive integer \(r\), expanding \(\log(1-u)=-u+O(u^2)\), uniformly here because \(r/q\to0\), and comparing the harmonic sum to an integral, yields
\[
\log\prod_{j=0}^{m-1}\left(1-\frac{r a_q}{qa_q+j}\right)
=-r a_q\log\left(1+\frac{m}{qa_q}\right)
+O_r\left(\frac{a_q+1}{q}\right).
\tag{2}
\]
The stated shape assumption makes the error vanish. For \(m=\lfloor b_q+s_q x\rfloor\), the definitions give
\[
1+\frac{m}{qa_q}
=q^{1/a_q}\left(1+\frac{x}{a_q}\right)+O\left(\frac1{qa_q}\right),
\]
so
\[
a_q\log\left(1+\frac{m}{qa_q}\right)
=\log q+a_q\log\left(1+\frac{x}{a_q}\right)+o(1)
=\log q+x+o(1).
\]
Equations (1)–(2) and \((q)_{\downarrow r}\sim q^r\) imply
\[
\mathbb E[(U_q(m))_{\downarrow r}]\longrightarrow e^{-rx}
\]
for every fixed \(r\ge1\). The factorial-moment criterion proves the Poisson limit, because the Poisson distribution is determined by its moments. Since \(\{T_q\le m\}=\{U_q(m)=0\}\), the Gumbel limit follows. Directly substituting \(a_q/\log q\to\kappa\) into \(b_q,s_q\) gives the scaling constants.

For the terminal label, Dirichlet conjugacy gives an exact conditional distribution for each coordinate after its label is not observed:
\[
P_i\mid\{\text{label }i\text{ unseen at time }m\}
\sim\operatorname{Beta}(a_q,(q-1)a_q+m).
\]
Thus its conditional normalized mean and variance are
\[
\mathbb E[qP_i\mid i\text{ unseen}]
=\frac{qa_q}{qa_q+m}\longrightarrow e^{-1/\kappa},
\]
\[
\operatorname{Var}(qP_i\mid i\text{ unseen})
=\frac{q^2a_q((q-1)a_q+m)}{(qa_q+m)^2(qa_q+m+1)}\longrightarrow0.
\]
At each fixed \(x\), the expected number of unseen labels is bounded and converges to \(e^{-x}\), by (1) with \(r=1\). Consequently the expected number of unseen labels with \(|qP_i-e^{-1/\kappa}|>\varepsilon\) tends to zero, by the conditional variance bound and Markov's inequality. Fix \(L>0\) and observe the unseen labels at \(\lfloor b_q-Ls_q\rfloor\): except on an event of limiting probability \(\exp(-e^{L})\), the final label is among them. Letting \(q\to\infty\) and then \(L\to\infty\) proves \(qP_{I_q}\to e^{-1/\kappa}\) in probability. Slutsky's theorem gives the joint limit. Finally, the marginal Dirichlet variance shows \(\operatorname{Var}(qP_i)=O(1/a_q)\), so a uniformly chosen label has normalized mass converging to one.

## Verification
The standalone `verify.py` implements exact Dirichlet–multinomial composition probabilities with rational arithmetic and tests the factorial-moment identity (1) for \(2\le q\le5\), integer shapes \(1,2,3\), and \(0\le m\le8\). It independently checks the conditional beta variance identity for \(2\le q\le6\). A finite-size diagnostic evaluates the logarithmic factorial-moment ratios at several \(q\) and \(\kappa\), observing decreasing discrepancies at the largest sampled sizes. Run `python3 verify.py`; Python's standard library suffices. These computations do not establish the limits: the proof above supplies the all-size argument.

## Relationship to prior work
Holst's 2000 preprint (published 2001), especially Sections 2 and 3.1, proves Fréchet-type limits for coupon completion with an iid fixed distribution of latent positive weights, including fixed-shape gamma weights and their Pólya-urn interpretation. The fixed-shape Fréchet law and the Poisson embedding belong to that earlier work. The present statement instead concerns a triangular array with \(a_q\) increasing at the critical logarithmic rate, identifies the exact Gumbel centering and scale in that window, and localizes the hidden probability of the final color. Neither the growing-shape normalization nor the terminal-mass localization is stated in the inspected Holst preprint. Neal's 2008 theorems study deterministic, unequal sampling probabilities and are applicable as general context, not as the same random-environment theorem. The calculation here is independent and direct through exact Dirichlet factorial moments. It does not claim that all possible moving-shape regimes or general random-weight coupon models are new.

## Limitations
The theorem is annealed and does not assert a quenched limit conditional on the full random probability vector. It covers \(a_q/\log q\to\kappa\in(0,\infty)\), not fixed \(a_q\) or arbitrary faster/slower shape sequences. It gives convergence in distribution, not a quantitative total-variation rate, nor asymptotic convergence of completion-time moments. Mathematical priority relative to all triangular-array extremes literature has not been independently established; the stated novelty is limited to the precise growing-concentration and terminal-label conclusions.

## References
1. L. Holst, *Extreme Value Distributions for Random Coupon Collector and Birthday Problems*, public preprint dated 2000-09-06, published in *Extremes* **4** (2001), 129–145. https://www2.seas.gwu.edu/~simhaweb/intsci/course/modules/appendix/whyscientists/coupon.pdf
2. P. Neal, *The Generalised Coupon Collector Problem*, *Journal of Applied Probability* **45** (2008), 621–629. https://doi.org/10.1239/jap/1222441818
