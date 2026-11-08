# Exact consensus selection and parity-sensitive edge influence on triangular-book majority networks

## Finding

For each integer \(s\geq1\), let \(B_s=K_2\vee\overline{K_s}\) be the graph of two adjacent hubs \(u,v\), each connected to \(s\) mutually nonadjacent leaves. Each vertex has a bit in \(\{0,1\}\). At each discrete time, independently choose one of the \(s+2\) vertices uniformly; it adopts the strict majority bit of its **open** neighborhood and retains its current bit on a tie. For initial hub bits \(h_u,h_v\) and exactly \(j\) initially one-valued leaves, let \(p_s(h_u,h_v,j)\) denote the eventual all-one consensus probability.

Set \(r=\lfloor s/2\rfloor\), and define for \(0\leq j\leq s\)
\[
\Phi_s(j)=
\begin{cases}
1,&j\geq r,\\[2pt]
\dfrac{(s-r+1)(s-r+2)}{(s-j+1)(s-j+2)},&j<r.
\end{cases}
\]
**Theorem.** From every initial bit configuration, the process reaches unanimous consensus almost surely, and its complete absorption kernel is
\[
 p_s(h_u,h_v,j)=
 \begin{cases}
 \Phi_s(j),&h_u=h_v=1,\\
 1-\Phi_s(s-j),&h_u=h_v=0,\\
 0,&h_u\ne h_v,\ 2j<s,\\
 1/2,&h_u\ne h_v,\ 2j=s,\\
 1,&h_u\ne h_v,\ 2j>s.
 \end{cases}
\]
The formulas are exact for every \(s\ge1\) and every initial configuration; no distributional assumption on initial bits is required.

For the polarized initial configuration consisting of two one-valued hubs and \(s\) zero-valued leaves, let \(W_s\) be the probability that the initial two-vertex minority wins. Then
\[
 W_s=\frac{(s-r+1)(s-r+2)}{(s+1)(s+2)},\qquad \lim_{s\to\infty}W_s=\frac14.
\]
Compare the graph \(K_{2,s}\), obtained by removing the hub-hub edge, under exactly the same asynchronous update rule and polarized initial bits. Its all-one probability \(W_s^{\mathrm{bip}}\) is obtained by replacing \(r\) with \(r'=\lceil s/2\rceil\). Consequently
\[
 W_s-W_s^{\mathrm{bip}}=
 \begin{cases}
 0,&s\text{ even},\\[2pt]
 \dfrac{s+3}{(s+1)(s+2)},&s\text{ odd}.
 \end{cases}
\]
Thus one added hub edge changes the exact fixation probability for every odd leaf count, but not for even leaf counts.

## Assumptions and scope

The graph has labelled vertices, no self-loops and an edge between its two hubs. The update is random sequential with independent uniform vertex selection at every step, including choices that leave the configuration unchanged. All colors are initially public and fixed; the tie rule is retention of the vertex's **current**, not initial or private, opinion. The comparison with \(K_{2,s}\) concerns only the explicitly given polarized initial configuration, not its complete absorption kernel.

The claimed probability includes the randomness of the update sequence and is conditional on the specified initial configuration. In particular, the model is not synchronous majority, voter copying, or a random-neighbor sampling protocol.

## Proof

**1. Absorption and fixed states.** Let \(E_{\neq}(x)\) be the number of edges with unequal endpoint bits. Whenever a vertex actually flips under strict open-neighbor majority, more incident edges cease to disagree than begin to disagree, so \(E_{\neq}\) decreases by at least one. Every nonabsorbing configuration has an eligible flipping vertex, which under uniform random selection is eventually chosen with probability one. Only finitely many flips occur, and the chain almost surely reaches a fixed configuration.

If both hubs agree, every leaf with the opposite bit is unstable. If the hubs disagree, the leaves see a tie and cannot move; writing \(j\) for the number of one-valued leaves, a hub currently holding one is stable only if \(2j\ge s+1\), while a hub currently holding zero is stable only if \(2j\le s-1\). These inequalities cannot hold simultaneously. Therefore the only fixed configurations are all zero and all one.

**2. Equal one-hubs.** Suppose \(h_u=h_v=1\). While the hubs agree, each zero-valued leaf flips to one upon selection and each one-valued leaf stays one. Each hub sees \(1+j\) one-neighbors and \(s-j\) zero-neighbors, and therefore remains stable precisely when \(j\ge r=\lfloor s/2\rfloor\). If initially \(j\ge r\), the hubs never flip and all leaves almost surely become one.

For \(j<r\), each hub is an eligible zero-flip and each of the \(s-j\) currently zero-valued leaves is an eligible one-flip. Null selections do not affect the relative order of effective changes. If a hub flips to zero before the leaf-one count reaches \(r\), no leaf can change while the hubs disagree, and the zero-valued hub cannot revert: its neighbor-one count is \(1+j<s-j\). The remaining one-valued hub then flips to zero almost surely, followed by all leaves. Hence all-one consensus occurs **if and only if** \(r-j\) distinct zero-valued leaves flip before either hub is selected for an effective flip.

At successive stages, the probability that the next effective change is a leaf flip is \((s-j-i)/(s-j-i+2)\). Multiplying for \(0\le i<r-j\) gives
\[
 \Pr(\text{one-consensus})=
 \prod_{i=0}^{r-j-1}\frac{s-j-i}{s-j-i+2}
 =\frac{(s-r+1)(s-r+2)}{(s-j+1)(s-j+2)}.
\]
This proves the first case including the empty-product boundary \(r=0\). The equal zero-hub case follows by exchanging zero and one, replacing \(j\) by \(s-j\).

**3. Opposite hubs.** Suppose one hub holds one and the other zero. Leaves see a tie and retain their bits until a hub changes. When \(2j<s\), the one-hub is the only unstable hub and flips to zero; when \(2j>s\), the zero-hub is the only unstable hub and flips to one. At \(2j=s\), which requires even \(s\), both hubs are unstable, and either is equally likely to be the first selected hub. After that first hub change, the now-unanimous hubs are stable, and all leaves almost surely adopt their bit. This yields probabilities \(0\), \(1/2\), and \(1\), respectively. All cases of the kernel have been proved.

**4. Edge addition and asymptotics.** Without the hub-hub edge, initially unanimous one-hubs each see exactly the \(s\) leaves and remain stable if and only if at least \(r'=\lceil s/2\rceil\) leaves hold one. The same first-effective-selection argument, with \(r'\) in place of \(r\), gives
\[
W_s^{\mathrm{bip}}=\frac{(s-r'+1)(s-r'+2)}{(s+1)(s+2)}.
\]
If \(s\) is even, \(r=r'\), so the difference is zero. If \(s\) is odd, \(r'=r+1\), and subtraction simplifies exactly to \((s+3)/((s+1)(s+2))\). Since \(r/s\to1/2\), the formula for \(W_s\) tends to \(1/4\).

## Verification

Three independent Python 3 programs accompany the theorem. `check_count_chain.py` computes the exact rational absorbing Markov chain on the count states \((h_u,h_v,j)\) and compares all four hub-bit assignments and every leaf count with the theorem for 35 distinct leaf counts up to 100. `check_labelled.py` constructs the graph explicitly by its edge list and computes exact rational absorption probabilities for all \(8184\) labelled initial configurations with \(1\le s\le10\). `check_edge_effect.py` independently constructs both graphs and computes their exact polarized-state Markov-chain probabilities for every \(1\le s\le11\). All programs terminate with their stated PASS messages, and their actual stdout files are included.

The finite checks corroborate but do not replace the exact proof for all \(s\). Rational arithmetic avoids Monte Carlo error.

## Relationship to prior work

Auletta, Caragiannis, Ferraioli, Galdi and Persiano analyze asynchronous tie-retaining majority dynamics on social networks, especially the **existence** of update sequences that overturn a majority, and characterize worst-case-robust graphs. Their 2014 preprint does not supply a random-uniform selection probability kernel on triangular books. The theorem here answers a different distributional question and specifies the precise finite graph and initial states.

Feldman, Immorlica, Lucier and Weinberg analyze non-Bayesian asynchronous social learning with private information, unreported initial opinions and private-signal tie breaking. Their star-network and expander results concern a different protocol and do not imply the fixed-public-initial-state kernel given here. Both strands motivate asking for exact outcomes on minimally clustered networks.

## Limitations

The result applies to two adjacent hubs and mutually nonadjacent leaves, with uniformly random single-vertex updates and retention on current ties. It does not establish the full absorption-time distribution, results for larger hub cliques, nonuniform update rates, other update conventions or population-wide inference under random private signals. Historical novelty is based on targeted literature and database comparison, not a proof of global priority. Independent scientific validation has not been performed.

## References

1. V. Auletta, I. Caragiannis, D. Ferraioli, C. Galdi, G. Persiano, *Minority Becomes Majority in Social Networks*, arXiv:1402.4050, first submitted 2014-02-17. https://arxiv.org/abs/1402.4050
2. M. Feldman, N. Immorlica, B. Lucier, S. M. Weinberg, *Reaching Consensus via non-Bayesian Asynchronous Learning in Social Networks*, arXiv:1408.5192, first submitted 2014-08-22. https://arxiv.org/abs/1408.5192
