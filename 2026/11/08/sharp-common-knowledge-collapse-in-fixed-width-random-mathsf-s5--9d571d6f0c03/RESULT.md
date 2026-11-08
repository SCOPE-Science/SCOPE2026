# Sharp common-knowledge collapse in fixed-width random \(\mathsf{S5}\) frames

## Finding

Fix integers \(b,r\ge 2\). For each integer \(N\ge1\), put \(n=bN\), and choose \(r\) independently and uniformly distributed equivalence relations \(E_1,\ldots,E_r\) on the labelled world set \([n]\), subject to every equivalence class of every \(E_i\) having cardinality exactly \(b\). This is a finite \(r\)-agent \(\mathsf{S5}\) frame with exactly \(b\) epistemic alternatives at each world for each agent.

For a proposition interpreted by an arbitrary set \(A\subseteq[n]\), denote its common-knowledge truth set by \(\mathcal C(A)\), and its universal-knowledge truth set by \(\mathcal U(A)\). Let \(\mathsf{Collapse}\) be the event that \(\mathcal C=\mathcal U\) as operations on **every** subset \(A\subseteq[n]\). Write
\[
\gamma=b(r-1)-r=(b-1)(r-1)-1,\qquad
\mu_N=\frac{N^r}{\binom{bN}{b}^{r-1}}.
\]
For every fixed \((b,r)\ne(2,2)\), one has \(\gamma\ge1\) and the sharp law
\[
\boxed{\Pr(\neg\mathsf{Collapse})=\mu_N+O_{b,r}(n^{-2\gamma})
=\frac{((b-1)!)^r}{b!}\,n^{-\gamma}
  \bigl(1+O_{b,r}(n^{-1})\bigr).}
\]
Conditioned on noncollapse, with probability \(1-O_{b,r}(n^{-\gamma})\) the common-knowledge equivalence relation has exactly two classes, one of size \(b\) and one of size \(n-b\). The exceptional \(b\)-class is uniform among all \(b\)-subsets of \([n]\) (exactly by label symmetry, conditional on this two-class event).

For \((b,r)=(2,2)\), in contrast, the exact collapse probability is
\[
\boxed{\Pr(\mathsf{Collapse})=
\frac{2^{2N-1}}{N\binom{2N}{N}}
\sim\frac{\sqrt\pi}{2\sqrt N}.}
\]
The exceptional perfect-matching case is a classical baseline, not presented as a new enumeration of matchings.

There is also an exact finite-order recurrence. Set \(T_0=A_0=1\), and for \(j\ge1\) define
\[
T_j=\frac{(bj)!}{(b!)^j j!},\quad A_j=T_j^r,\quad
K_j=A_j-\sum_{t=1}^{j-1}\binom{bj-1}{bt-1}K_tA_{j-t}.
\]
Then \(K_N\) counts all ordered \(r\)-tuples of the permitted equivalence relations whose common-knowledge operator collapses to universal knowledge, and \(\Pr(\mathsf{Collapse})=K_N/A_N\) exactly.

## Assumptions and scope

All random choices are independent, uniform over *labelled* partitions of a fixed set into \(N\) unlabelled blocks of size \(b\); neither uniform sampling over all Bell partitions nor sampling independent hyperedges is used. The intuitionistic information order, when considered, is equality, so these are also the induced intuitionistic \(\mathsf{S5}\) frames of the standard construction. The probability bounds are for fixed \(b,r\) and \(N\to\infty\), with \(b\mid n\); constants can depend on \(b,r\). No random valuation is needed because the operator identity is universal over all valuations.

For \(R=E_1\cup\cdots\cup E_r\), let \(J=R^*\) be its reflexive transitive closure. Since each \(E_i\) is an equivalence relation, \(J\) is the least equivalence relation containing them. Define \(\mathcal C(A)=\{w:J[w]\subseteq A\}\) and \(\mathcal U(A)=[n]\) if \(A=[n]\), and \(\mathcal U(A)=\varnothing\) otherwise. The operator identity \(\mathcal C=\mathcal U\) holds precisely when \(J\) has one class: if it does, both operations agree; if it does not, take \(A\) to be any nonempty proper \(J\)-class to separate them.

## Proof

**Exact cut probability.** Any nonempty proper \(J\)-class is simultaneously saturated for each \(E_i\), meaning it is a union of that agent's blocks. A fixed \(bj\)-subset \(S\) is saturated by one random partition with probability
\[
\frac{\binom Nj}{\binom{bN}{bj}}
\]
(choose its \(j\) blocks in an exchangeable partition). Thus the expected number of common saturated subsets of cardinality \(bj\) is exactly
\[
Q_j=\frac{\binom Nj^{\,r}}{\binom{bN}{bj}^{r-1}}
\qquad (1\le j\le\lfloor N/2\rfloor).
\]
Every disconnected \(J\) has at least one class of size at most \(n/2\), so
\[
\Pr(\mathcal C\ne\mathcal U)\le\sum_{j=1}^{\lfloor N/2\rfloor} Q_j.
\]
Notice \(Q_1=\mu_N\).

**Tail estimate.** Assume \(\gamma>0\). For \(1\le j\le N/2\), elementary binomial inequalities give
\[
Q_j\le\left[e^r(j/N)^\gamma\right]^j,
\]
using \(\binom Nj\le(eN/j)^j\) and \(\binom{bN}{bj}\ge(N/j)^{bj}\). For the single term \(j=2\), direct fixed-index binomial asymptotics give \(Q_2=O_{b,r}(N^{-2\gamma})\). For \(3\le j\le N^{1/3}\), the displayed bound is a geometric bound with ratio \(e^rN^{-2\gamma/3}\), so the sum there is \(O_{b,r}(N^{-2\gamma})\). Select any fixed \(\delta>0\) with \(e^r\delta^\gamma<1/2\). For \(N^{1/3}<j\le\delta N\), the sum is at most \(O(2^{-N^{1/3}})\). Finally, uniformly for \(\delta N\le j\le N/2\), Stirling's formula gives
\[
\log Q_j=-\gamma N H(j/N)+O_{b,r}(\log N),
\quad H(t)=-t\log t-(1-t)\log(1-t),
\]
and since \(H(t)\ge H(\delta)>0\) on this interval, this last sum is exponentially small. Therefore
\[
\sum_{j=2}^{\lfloor N/2\rfloor}Q_j=O_{b,r}(N^{-2\gamma}). \tag{1}
\]

**Lower bound and exceptional structure.** Let \(X\) be the number of \(b\)-subsets that form a block of all \(r\) partitions. Every such subset is a whole \(J\)-class. Direct counting gives
\[
\mathbb EX=\mu_N,\qquad
\mathbb E[X(X-1)]
=\frac{[N(N-1)]^r}{[\binom{n}{b}\binom{n-b}{b}]^{r-1}}
=O_{b,r}(N^{-2\gamma}).
\]
Two distinct common blocks must be disjoint; the second identity counts ordered disjoint candidates. Bonferroni's inequality implies
\[
\mu_N-\tfrac12\mathbb E[X(X-1)]
\le\Pr(X\ge1)\le\mu_N.
\]
Since \(X\ge1\) implies noncollapse and (1) bounds all other disconnected configurations, the sharp probability formula follows. Moreover, outside an event of probability \(O(N^{-2\gamma})\), noncollapse is accompanied by exactly one common \(b\)-block and no common saturated subset of sizes \(2b,\ldots,\lfloor n/2\rfloor\). The remaining \(n-b\) worlds then form one \(J\)-class: otherwise they would contain another component of size at most \(n/2\), or a second \(b\)-class. Dividing the bad-event estimate by \(\Pr(\neg\mathsf{Collapse})=\Theta(N^{-\gamma})\) yields the conditional conclusion. Invariance under every label permutation makes the unique small class uniformly located.

**Leading constant.** For fixed \(b,r\),
\[
\mu_N=\frac{N^r}{\binom{bN}{b}^{r-1}}
=\frac{(b!)^{r-1}}{b^r}n^{-\gamma}
\left(1+O_{b,r}(n^{-1})\right)
=\frac{((b-1)!)^r}{b!}n^{-\gamma}
\left(1+O_{b,r}(n^{-1})\right).
\]
For example, the leading noncollapse probabilities are \(1/(2n)\) for \((b,r)=(2,3)\) and \(2/(3n)\) for \((b,r)=(3,2)\).

**Exceptional case.** For \(b=r=2\), fix the first perfect matching and contract its \(N\) edges into vertices. The union of the two matchings is connected if and only if the second matching creates a single alternating cycle. This occurs for exactly \(2^{N-1}(N-1)!\) second matchings: pick a cyclic order of the \(N\) first-matching edges, together with their relative orientations, modulo reversal. There are \((2N-1)!!=(2N)!/(2^NN!)\) equally likely second matchings. Their ratio is \(2^{2N-1}/(N\binom{2N}{N})\), and the asymptotic follows from the central binomial coefficient.

**Finite recurrence.** Among all \(A_N=T_N^r\) ordered partition tuples, classify each by the connected component of world \(1\). If this component has size \(bt\), there are \(\binom{bN-1}{bt-1}\) choices for its remaining labels, \(K_t\) ways to place connected tuples on that component, and \(A_{N-t}\) unrestricted tuples on the complement. Sum over \(1\le t\le N\) and isolate the term \(t=N\). This proves the recurrence without making an asymptotic approximation.

## Verification

The accompanying standard-library `checker.py` enumerates partitions directly and evaluates connectivity by a union-find algorithm. It independently checks the exact recurrence, the first and second factorial moment identities, and the exceptional perfect-matching count for all tested cases: \((b,N,r)=(2,1\ldots4,2),(2,1\ldots3,3),(3,1\ldots2,2),(4,2,2),(3,2,3)\). It returns `ALL_FINITE_CHECKS_OK`.

A useful finite-order consistency interval, valid for \(N\ge2\), follows directly from the proof:
\[
\mu_N-\frac{[N(N-1)]^r}{2[\binom n b\binom{n-b}b]^{r-1}}
\le\Pr(\neg\mathsf{Collapse})\le
\sum_{j=1}^{\lfloor N/2\rfloor} \frac{\binom Nj^r}{\binom n{bj}^{r-1}}.
\]
The checker does not prove the uniform entropy estimate or the infinite asymptotic; those are supplied by the analytic argument above.

## Relationship to prior work

Zenger's 2026 *Intuitionistic Common Knowledge*, arXiv:2605.00523v1, defines common knowledge through the reflexive transitive closure of agent accessibility and explicitly embeds classical \(\mathsf{S5}\) models into intuitionistic \(\mathsf{S5}\) by the equality information order. It gives logical soundness, completeness and complexity results, not a sharp random fixed-width frame classification.

Pittel (2000) and Canfield (2001) study the join of **unrestricted** independent uniformly random set partitions, whose measure gives positive weight to every block-size profile. Their Bell-number setting and its sharp join asymptotics are not the fixed-\(b\), uniform equipartition probability space here. Eberhard and Garzoni (2021, 2022) study random permutation generators of prescribed cycle types and prove qualitative transitivity laws; fixed-block partitions correspond to the cycle supports of disjoint \(b\)-cycles, but their inspected theorems do not supply the present relative error \(O(n^{-\gamma})\) or conditional exceptional-component law across all \(r\). Lugo (2009) discusses the alternating-cycle structure of two random perfect matchings, credited for the classical boundary case. Greenhill, Isaev and Liang (2021) concern uniformly sampled *simple* regular hypergraphs and spanning trees, a different ensemble from the colored, potentially parallel hyperedges naturally generated by independently selected block partitions.

## Limitations

The sharp law requires fixed \(b,r\) and \(\gamma>0\); it is not uniform when either parameter grows with \(n\), and it does not apply to arbitrary block-size distributions or the uniform simple-regular-hypergraph measure. The exact recurrence can be evaluated for finite inputs but is not claimed to be computationally efficient for large ones. This mathematical result is not an independent certification of historical novelty: broader random permutation/hypergraph theorems may imply portions of it, and independent audit remains to be performed. The finite checker confirms only tested finite cases, not the asymptotic proof.

## References

- L. Zenger, *Intuitionistic Common Knowledge*, arXiv:2605.00523v1 (first public May 1, 2026), https://arxiv.org/html/2605.00523v1 .
- B. Pittel, *Where the Typical Set Partitions Meet and Join*, Electron. J. Combin. 7 (2000), R5, https://doi.org/10.37236/1483 .
- E. R. Canfield, *Meet and Join within the Lattice of Set Partitions*, Electron. J. Combin. 8 (2001), R15, https://doi.org/10.37236/1559 .
- S. Eberhard and D. Garzoni, *Random generation with cycle type restrictions*, Algebraic Combinatorics 4 (2021), 1–25, https://doi.org/10.5802/alco.149 .
- S. Eberhard and D. Garzoni, *Probability of generation by random permutations of given cycle type*, arXiv:2205.07573 (2022), https://arxiv.org/abs/2205.07573 .
- M. Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604 (2009), https://arxiv.org/abs/0911.3604 .
- C. Greenhill, M. Isaev and G. Liang, *Spanning trees in random regular uniform hypergraphs*, arXiv:2005.07350 (2020; version March 2021), https://arxiv.org/pdf/2005.07350 .
