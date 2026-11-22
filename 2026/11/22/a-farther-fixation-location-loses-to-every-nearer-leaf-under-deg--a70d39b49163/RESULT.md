# A farther fixation location loses to every nearer leaf under degree-normalized colonization

## Finding
Consider the undirected tree \(T_k\) obtained from a root \(o\) by attaching (i) a hub \(h\) carrying \(k\) pendant leaves and (ii) a disjoint three-edge path \(o-v_1-v_2-v_3\). The hub is adjacent to \(o\), so the \(k\) hub leaves are at distance two from \(o\), while \(v_3\) is the **unique** vertex at distance three. Set \(k\ge1\).

In infinite-mutant-fitness birth–death Moran colonization, started with the unique mutant at \(o\), write \(q_k\) for the probability that the final wild-type vertex is \(v_3\). With \(a=1/2\), \(b=1/(k+1)\) and \(\mathcal L(z)=(a/(a+z))^3\), the following finite exact formula holds:

\[
q_k=\sum_{j=0}^k(-1)^j\binom{k}{j}\,H(jb),\qquad
H(z)=\begin{cases}\displaystyle\frac{a}{a-z}\bigl(\mathcal L(z)-\mathcal L(a)\bigr),&z\ne a,\\[4pt]
a\,\mathbb E[T e^{-aT}]=\frac{3}{16},&z=a,
\end{cases}
\]
where \(T\) has the gamma law with shape three and rate \(a\). Each of the \(k\) nearer leaves has terminal-location probability \((1-q_k)/k\).

For \(k=4\) (a nine-vertex tree) the exact values are
\[
q_4=\frac{40122073072}{243729729243},\qquad
\frac{1-q_4}{4}=\frac{203607656171}{974918916972},\qquad
\frac{1-q_4}{4}-q_4=\frac{43119363883}{974918916972}>0.
\]
Thus the unique farthest habitat is **strictly less likely** to be the last occupied by mutants than each of four closer terminal habitats. Moreover, for the entire family
\[
0<q_k\le\frac{(k+2)!2^{k-1}}{(k+1)^k}
=O\!\left(k^{5/2}(2/e)^k\right),
\]
so \(q_k=o(1/k)\) while each nearer leaf has probability asymptotic to \(1/k\). In particular this reversal holds for all sufficiently large \(k\), and its probability contrast becomes asymptotically unbounded in ratio.

## Assumptions and scope
All graphs are finite, connected, undirected, simple, and unweighted. The update is the standard birth–death Moran rule: select a reproducer proportional to fitness, then select an out-neighbor uniformly for replacement. The colonization limit lets resident reproduction vanish relative to mutant reproduction, so the mutant set is increasing and fixation occurs almost surely. Initial state is one mutant at \(o\); there are no mutations or recoveries. Degree is computed in the original graph. Only terminal **location**, not time or finite-selection fixation probability, is claimed.

## Proof
**1. Exact independent-clock embedding.** Give every mutant vertex an independent unit-rate Poisson reproduction clock. Each firing selects a neighboring vertex uniformly; firings into already mutant vertices are harmless. At every event time, the choice of reproducer is uniform among mutants, exactly matching the embedded discrete colonization chain (including harmless self-type replacements). Poisson thinning yields independent directed-edge clocks of rate \(1/\deg(u)\) outgoing from each occupied vertex \(u\). By memorylessness and the unique-path property of a tree, each vertex is first occupied after the sum of independent exponential waiting times along its root path. Conditional branch independence is genuine here because the reproduction clocks and their edge thinnings can be taken independent.

**2. Terminal competition.** The root has degree two, the hub degree \(k+1\), and the two internal vertices of the long path each have degree two. Therefore the infection time of the far endpoint is \(T_f=X_1+X_2+X_3\), where the \(X_i\) are independent exponential variables of rate \(a=1/2\). The hub infection time is \(X_h\sim\operatorname{Exp}(a)\); subsequent short-leaf waiting times are independent \(Y_i\sim\operatorname{Exp}(b)\), with \(b=1/(k+1)\). All these variables can be chosen mutually independent. The short terminal times are \(X_h+Y_i\); they share \(X_h\). Internal vertices cannot be the last to be occupied, so, with probability one, the final location is either \(v_3\) or one of the hub leaves. Hence
\[
q_k=\mathbb E\left[\mathbf1_{\{X_h<T_f\}}\left(1-e^{-b(T_f-X_h)}\right)^k\right].
\]
Symmetry of the hub leaves gives each probability \((1-q_k)/k\).

**3. Closed form.** Expanding the power by the binomial theorem, the \(j\)-th conditional integral, for fixed \(T_f=t\), is
\[
\int_0^t a e^{-ax} e^{-jb(t-x)}\,dx
=\begin{cases}\frac{a}{a-jb}(e^{-jbt}-e^{-at}),&jb\ne a,\\a t e^{-at},&jb=a.\end{cases}
\]
The Laplace transform of \(T_f\) is \(\mathcal L(z)=(a/(a+z))^3\). In the coincident-rate case, \(a\mathbb E[T_fe^{-aT_f}]=3/16\). This proves the stated formula for every integer \(k\ge1\).

**4. Exact reversal.** Substitution of \(k=4\) yields the rational values displayed above. The difference is a strictly positive rational. The rational calculation is reproduced in `check.py`, which also compares the formula against an independently constructed finite-state colonization recursion.

**5. Family bound.** For \(x\ge0\), \(1-e^{-x}\le x\). Hence
\[
q_k\le\mathbb E\left[(T_f/(k+1))^k\right]
=\frac{2^k(k+2)!}{2(k+1)^k}.
\]
Stirling's formula gives the displayed exponentially decreasing upper bound because \(2/e<1\). Therefore \(kq_k\to0\), which implies \(q_k<(1-q_k)/k\) for every sufficiently large \(k\), and \(((1-q_k)/k)/q_k\to\infty\).

## Verification
Run `python3 check.py` with standard Python (no third-party modules). The checker implements the gamma-Laplace formula with exact rational arithmetic and separately solves the monotone colonization chain using states \((h,j,b)\): hub infection indicator \(h\), count \(j\) of infected hub leaves, and count \(b\) of consecutively infected long-path vertices. It verifies identity for \(1\le k\le17\), the exact nine-vertex witness, and three independent moment bounds. These finite checks supplement, but do not replace, the all-\(k\) proof.

## Relationship to prior work
Brewster, Lippner, Tkadlec and Nowak (arXiv:2605.26411, first submitted 2026-05-26) introduce fixation location and demonstrate nontrivial spatial distributions, including a five-vertex example where a farthest vertex does not maximize location probability; their examples involve a triangle attached to a star. Their paper also describes configuration-graph computation and colonization in small networks. The theorem here isolates a distinct **tree-only, unique farthest vertex** effect and an all-size exponential asymptotic within the same degree-normalized colonization rule.

Kopfová and Tkadlec (arXiv:2410.09476, 2024-10-12) study colonization **times**, providing a related process framework but not, in the accessible material checked, this particular terminal-location probability. Independent exponential first-passage constructions are classical; the clock representation itself is not claimed as new. The scientific claim is the exact family-level terminal-location comparison and explicit tree counterexample, not the general exponential-clock or binomial-expansion techniques.

## Limitations
This is a statement about the colonization (infinite-selection) limit of a Moran birth–death process. The comparison is not established uniformly for finite mutant fitness, other update mechanisms, or population extinction with recovery. Nine vertices are an explicit example, **not a proved minimal size** over all trees. A search and a full-text comparison of the main 2026 source found no identical family theorem, but historical priority across all first-passage-percolation and evolutionary-graph literature is not independently certified.

## References
- D. A. Brewster, G. Lippner, J. Tkadlec, and M. A. Nowak, *Fixation location in structured populations*, arXiv:2605.26411, 2026. https://arxiv.org/html/2605.26411
- L. Kopfová and J. Tkadlec, *Colonization times in Moran process on graphs*, arXiv:2410.09476, 2024. https://arxiv.org/abs/2410.09476
- J. A. Fill and R. Pemantle, *Percolation, first-passage percolation, and covering times for Richardson's model on the n-cube*, arXiv:math/0404015, 2004. https://arxiv.org/abs/math/0404015
