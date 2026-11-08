# Two origin-dependent completion-time limits for randomized zero forcing on \(K_{a,2}\)

## Finding
Consider synchronous randomized zero forcing (RZF) on the unweighted **bidirected** complete bipartite graph \(K_{a,2}\), where \(a\ge2\). A white vertex becomes blue in a round independently of the other white vertices, with probability equal to the fraction of its neighbors blue at the start of that round; blue is absorbing. Let \(T_a^{\mathrm{small}}\) and \(T_a^{\mathrm{large}}\) be the numbers of rounds until all vertices are blue, starting respectively from one blue vertex in the two-vertex part and from one blue vertex in the \(a\)-vertex part.

For each integer \(t\ge0\), define an integer-valued random variable \(G\) by
\[
\Pr(G>t)=2^{-t(t-1)/2}.
\]
In particular \(G\ge2\), and this survival sequence determines its entire distribution. Then, as \(a\to\infty\) through integers,
\[
T_a^{\mathrm{small}}\Longrightarrow 1+G,\qquad
\mathbb E T_a^{\mathrm{small}}\longrightarrow
c_*=1+\sum_{t=0}^{\infty}2^{-t(t-1)/2}
=3.641632560655154\ldots.
\]
By contrast,
\[
\frac{T_a^{\mathrm{large}}}{a}\Longrightarrow\operatorname{Exp}(2),
\qquad \frac{\mathbb E T_a^{\mathrm{large}}}{a}\longrightarrow\frac12,
\]
where \(\operatorname{Exp}(2)\) has survival probability \(e^{-2x}\) at \(x\ge0\). More quantitatively, with \(q_a=2/a-1/a^2\),
\[
\frac1{q_a}\le\mathbb ET_a^{\mathrm{large}}
\le\frac1{q_a}+\lceil\log_2(a-1)\rceil+3.
\]
Thus for all sufficiently large \(a\), starting in the smaller part gives strictly smaller expected completion time.

There is also an exact finite-\(a\) formula for the time \(G_a\) at which the *other* vertex of the two-vertex part first becomes blue when the process starts in that part. Put \((a)_k=a(a-1)\cdots(a-k+1)\), with \((a)_0=1\). For every integer \(t\ge1\),
\[
\Pr(G_a>t)=\frac1{a^{t-1}}
\sum_{\pi\in\mathcal P(\{1,\ldots,t-1\})}
(a)_{|\pi|}\,2^{-\sum_{B\in\pi}\max B}.
\]
Here \(\mathcal P(S)\) is the set of set partitions of \(S\), the empty set has one empty partition, and \(\Pr(G_a>0)=1\). For example, \(\Pr(G_a>3)=(a+1)/(8a)\). The finite formula and the two limiting orientation laws form one joint finding about the dependence of completion on the seed part.

## Assumptions and scope
The graph has exactly two parts of sizes \(a\) and \(2\), with one directed edge in each direction for every cross-part pair and no other edges. Every directed edge has unit weight. Updates are synchronous and conditionally independent across white vertices, using the *previous* round's blue set; this is recipient-side RZF, not the distinct sender-side probabilistic zero-forcing rule. Both initial conditions contain exactly one blue vertex. The asymptotic statements let the integer \(a\to\infty\) with the other part fixed at size two. Distributional convergence is weak convergence; the expectation limits are separately established.

## Proof
**1. First activation of the second small-part vertex.** When one of the two small-part vertices is blue and the other is white, each white vertex in the large part independently turns blue each round with probability \(1/2\). Until the second small-part vertex changes color, the large-part infection process may therefore be coupled to an auxiliary process in which that second small-part vertex is kept artificially white. Give every large-part vertex an independent geometric waiting time \(L_i\) with success probability \(1/2\), counted starting at one. At time \(s\) of this auxiliary process, the number of still-white large-part vertices is \(W_s=\sum_{i=1}^a\mathbf1_{\{L_i>s\}}\), with \(W_0=a\).

At round \(s+1\), conditional on this auxiliary process and on the second small-part vertex having remained white, its probability of *not* turning blue is \(W_s/a\). The random update for that vertex is independent of those for the large-part vertices. Hence, with \(G_a\) the first infection round of the second small-part vertex,
\[
\Pr(G_a>t\mid L_1,\ldots,L_a)
=\prod_{s=0}^{t-1}\frac{W_s}{a},\qquad t\ge0.
\tag{1}
\]
The coupling is valid up to and including the first change of the second small-part vertex, since all simultaneous updates use the state at the beginning of each round.

Expanding the product after removing \(W_0/a=1\) sums over assignments of large-part vertex labels to each time index \(1,\ldots,t-1\). The equality pattern is a set partition \(\pi\). Each block requires its assigned label to remain white through the largest index in that block, of probability \(2^{-\max B}\). There are \((a)_{|\pi|}\) distinct injective labelings of the blocks. Taking expectations in (1) gives exactly the finite-\(a\) formula above. It remains valid if some falling factorials are zero.

For each fixed nonnegative integer \(s\), the strong law gives \(W_s/a\to2^{-s}\) almost surely under a coupling across all \(a\). Each product in (1) lies between zero and one. Dominated convergence therefore yields, for every fixed \(t\ge0\),
\[
\Pr(G_a>t)\longrightarrow
\prod_{s=0}^{t-1}2^{-s}=2^{-t(t-1)/2}.
\tag{2}
\]
This establishes \(G_a\Rightarrow G\). For every integer \(t\ge1\), the product in (1) is at most \(W_{t-1}/a\), so
\[
\Pr(G_a>t)\le\mathbb E(W_{t-1}/a)=2^{-(t-1)}.
\tag{3}
\]
Consequently their integer-tail sums are uniformly summable and \(\mathbb E G_a\to\mathbb EG=\sum_{t\ge0}2^{-t(t-1)/2}\).

**2. Completion after the second small-part vertex activates.** If at time \(G_a\) there are still white large-part vertices, then in the *next* round all of them turn blue with probability one, since both small-part vertices are now blue. Thus exactly
\[
T_a^{\mathrm{small}}=G_a+\mathbf1_{\{W_{G_a}>0\}}.
\tag{4}
\]
For any integer \(R\ge1\), using that the auxiliary white counts decrease in time,
\[
\Pr(W_{G_a}=0)\le\Pr(G_a>R)+\Pr(W_R=0)
\le2^{-(R-1)}+(1-2^{-R})^a.
\]
First take \(a\to\infty\) and then \(R\to\infty\): the probability tends to zero. Equations (2)–(4), together with the uniform integrability furnished by (3), give both the distributional and mean convergence to \(1+G\).

**3. The opposite initial part.** If the initial blue vertex lies in the large part, all other large-part vertices have zero blue neighbors until the first small-part vertex becomes blue. The two still-white small-part vertices independently turn blue in each round with probability \(1/a\). Thus the time \(H_a\) of the first such infection is geometric with parameter
\[
q_a=1-(1-1/a)^2=2/a-1/a^2.
\]
In particular \(\mathbb EH_a=1/q_a\) and, for each \(x\ge0\),
\[
\Pr(H_a/a>x)=(1-q_a)^{\lfloor ax\rfloor}
\longrightarrow e^{-2x}.
\tag{5}
\]
After the first small-part infection, every other large-part vertex has a blue neighbor, and its conditional chance of becoming blue in any subsequent round is at least \(1/2\), independently of the other white vertices. Coupling with fresh independent fair coins bounds the time to finish the large part by \(M_a\), the maximum of \(a-1\) independent \(\operatorname{Geom}(1/2)\) variables. Once that part is blue, the possible remaining small-part vertex becomes blue within one further round. Therefore, in a coupling,
\[
H_a\le T_a^{\mathrm{large}}\le H_a+M_a+1.
\tag{6}
\]
For integer \(u\ge0\), a union bound gives \(\Pr(M_a>u)\le\min\{1,(a-1)2^{-u}\}\). Summing these tails yields
\[
\mathbb EM_a\le\lceil\log_2(a-1)\rceil+2.
\tag{7}
\]
Equations (5)–(7) imply \((T_a^{\mathrm{large}}-H_a)/a\to0\) in probability and in \(L^1\), giving the exponential weak limit and the displayed expectation bounds. In particular the large-origin mean diverges linearly, while the small-origin mean approaches a finite constant, proving the final strict asymptotic comparison. \(\square\)

## Verification
A standard-library Python verifier in `verification/check.py` independently implements the exact synchronous Markov transition probabilities for both initial parts. It compares the first small-part activation survival probability against two other derivations: a frozen-process binomial recurrence and the set-partition formula, for each \(2\le a\le8\) and \(0\le t\le6\). It also checks the exact no-small-part-activation geometric law from the large origin, finite-size bounds, and the numerical evaluation of \(c_*\). The extracted script passes 209 assertions. These are finite calculations; the limit theorems follow from the analytic couplings, strong law, tail domination, and geometric limit proved above.

## Relationship to prior work
Geneson, Hicks, Lichtenberg, Moon and Robles define this recipient-side synchronous process and in Theorem 3.7 give \(O(\min\{m\log n,n\log m\})\) for the *optimal-seed* expected time on bidirected \(K_{m,n}\); their Conjecture 3.12 compares starting parts. Neither the stated bound nor the conjecture implies the two orientation-dependent limit laws, the exact q-series small-part distribution, or the linear-scale exponential large-part limit. Lichtenberg's 2025 thesis addresses computational methods and special graph families, but its full text could not be inspected; overlap risk with that source remains unresolved. Earlier probabilistic zero forcing is a distinct sender-side update mechanism, and its graph-family propagation bounds do not directly imply these formulas. Published mathematical-result searches returned related complete-bipartite *deterministic* forcing and domination classifications, but no equivalent recipient-side stochastic hitting-time claim. No exhaustive historical-priority conclusion is asserted.

## Limitations
The result covers only unweighted bidirected \(K_{a,2}\), one initial blue vertex, and the one-sided limit \(a\to\infty\). It does not establish the original starting-part inequality for all finite \(a>b\) or for general \(b\ge3\), nor does it quantify total-variation convergence. The 2025 thesis was accessible only by abstract because the institutional repository denied full-text access and an authorized institutional retrieval route was unavailable; this is a genuine remaining originality risk. No independent review has been performed.

## References
1. Noah Fan Lichtenberg, *Randomized Zero Forcing*, Rice University thesis, repository record dated 2025-08-11, https://hdl.handle.net/1911/118627 (abstract inspected; thesis full text unavailable).
2. Jesse Geneson, Illya Hicks, Noah Lichtenberg, Alvin Moon and Nicolas Robles, *Randomized Zero Forcing*, arXiv:2602.16300v1, submitted 2026-02-18, https://arxiv.org/abs/2602.16300 (full HTML text inspected, especially Definition 1.1 and Section 3.6).
3. Yu Chan, Emelie Curl, Jesse Geneson, Leslie Hogben, Kevin Liu, Issac Odegard and Michael S. Ross, *Using Markov chains to determine expected propagation time for probabilistic zero forcing*, arXiv:1906.11083, https://arxiv.org/abs/1906.11083 (distinct update model).
