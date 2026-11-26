# Sibling–tuft asymmetry in connected threshold graphs: exact joint enumeration and limiting separation

## Finding

For each integer \(n\ge3\), let \(\mathcal T_n\) be the set of isomorphism classes of connected simple threshold graphs on \(n\) vertices. The *sibling number* \(s(G)\) is the largest number of other vertices having the same closed neighborhood as a vertex, and the *tuft number* \(t(G)\) is the largest number of degree-one neighbors of a vertex. Both are the parameters of Fürnsinn–Gangl–Rubey [1].

For any nonnegative integers \(S,T\), put
\[
H_{S,T}(z)=\sum_{n\ge3}z^n\#\{G\in\mathcal T_n:s(G)\le S,\ t(G)\le T\}.
\]
Define the finite sums \(J_h(z)=\sum_{j=1}^{h}z^j\) and \(R_h(z)=\sum_{j=2}^{h}z^j\), with empty sums equal to zero. Put
\[
\begin{aligned}
A_S&=zJ_S+\frac{z^2J_{S+1}}{1-z},
& B_S&=\frac{zJ_{S+1}}{1-z},\\
C_{S,T}&=\frac{zR_{S+1}}{1-z}+zJ_T,
& E_{S,T}&=zR_S+\frac{z^2R_{S+1}}{1-z}+zR_T.
\end{aligned}
\]
Then the complete bounded joint enumerator is the rational function
\[
\boxed{H_{S,T}(z)=E_{S,T}(z)+\frac{A_S(z)C_{S,T}(z)}{1-B_S(z)}.}
\]
Every exact joint coefficient is recovered by two discrete differences in \(S,T\), interpreting a negative-bound count as zero.

Writing \(F_1=F_2=1\) for the Fibonacci sequence, for every \(n\ge3\),
\[
\boxed{\#\{G\in\mathcal T_n:s(G)=0\}=F_{n-2},\qquad
\#\{G\in\mathcal T_n:t(G)=0\}=2^{n-3}.}
\]
Thus the two parameters, although jointly equidistributed over all connected graphs and even over all connected chordal graphs [1], are not equidistributed over connected threshold graphs for any \(n\ge4\).

If \(G_n\) is sampled uniformly from \(\mathcal T_n\), then
\[
\mathbb E\,t(G_n)=1,\qquad
\operatorname{Var}(t(G_n))=2-2^{3-n},\qquad
\frac{s(G_n)}{\log_2 n}\xrightarrow{\mathbb P}1.
\]
More precisely, \(t(G_n)\) converges to the law with mass \(1/2\) at zero and \(2^{-j-1}\) at each positive integer \(j\); consequently
\[
\boxed{d_{\mathrm{TV}}(\mathcal L(s(G_n)),\mathcal L(t(G_n)))\longrightarrow1.}
\]

## Assumptions and scope

All graphs are finite, undirected and simple. A threshold graph is obtained by successively adjoining an isolated vertex (symbol \(0\)) or a vertex adjacent to all preceding vertices (symbol \(1\)). Up to graph isomorphism a connected threshold graph on \(n\ge2\) vertices has a unique normalized creation word of length \(n\), whose first symbol is \(0\) and last symbol is \(1\). The intermediate \(n-2\) symbols are arbitrary [2,3]. All distributions here are **uniform over unlabeled graph isomorphism classes**, not over labeled realizations.

For a nonempty graph \(G\), the closed neighborhood is \(N[v]=N(v)\cup\{v\}\). The sibling number counts the maximum cardinality of a closed-neighborhood equivalence class minus one. The tuft number is \(\max_v|N(v)\cap\{u:\deg(u)=1\}|\). The exceptional two-vertex graph is excluded throughout the generating function and asymptotic statements to avoid the mutual-leaf boundary.

## Proof

**Canonical runs and the two statistics.** Decompose the normalized word uniquely into alternating maximal nonempty runs
\[
0^{a_1}1^{b_1}\,0^{a_2}1^{b_2}\cdots0^{a_q}1^{b_q},
\qquad q\ge1,\quad a_i,b_i\ge1.
\]
Within a run of adjoining universal vertices, all vertices are pairwise closed-neighborhood twins. The initial symbol \(0\) joins the first such twin class precisely when \(a_1=1\). Vertices from different one-runs cannot be twins, because an intermediate zero-vertex distinguishes their neighborhoods; no two zero-vertices are adjacent, so they cannot be closed twins. Therefore
\[
s(G)=\max\left\{b_1-1+\mathbf1_{a_1=1},\ b_2-1,\ldots,\ b_q-1\right\}.
\]
For \(n\ge3\), precisely the zero-vertices lying after the penultimate one-symbol have degree one, and they are all adjacent to the final one-vertex. If the final one-run has more than one symbol, there are no leaves. Consequently
\[
t(G)=\begin{cases}a_q,&b_q=1,\\0,&b_q\ge2.\end{cases}
\]
These descriptions also cover a word with a single pair of runs.

**Rational joint enumerator.** Impose \(s\le S\) and \(t\le T\). A first run pair \(0^{a_1}1^{b_1}\) contributes \(A_S\): if \(a_1=1\), then \(1\le b_1\le S\); otherwise \(a_1\ge2\) and \(1\le b_1\le S+1\). Any internal run pair has \(a\ge1\) and \(1\le b\le S+1\), contributing \(B_S\). The final pair, provided there is an earlier pair, contributes \(C_{S,T}\): either \(b\ge2\), with \(t=0\), or \(b=1\) and \(1\le a\le T\). If there is only one pair and the word has length at least three, its allowed contributions are exactly \(E_{S,T}\); the excluded word \(01\) has length two. Thus the sum over two or more run pairs is
\[
A_SC_{S,T}\sum_{h\ge0}B_S^h=\frac{A_SC_{S,T}}{1-B_S},
\]
proving the formula in formal power series; \(B_S(0)=0\).

**Zero classes.** The event \(s=0\) forces the word to begin with \(00\) and to have no adjacent ones, while the last symbol is \(1\). These binary strings are counted by \(F_{n-2}\), using the Fibonacci recurrence obtained by splitting at the next bit. The event \(t=0\) is equivalent to the word ending in \(11\), leaving exactly \(n-3\) free binary positions, and thus gives \(2^{n-3}\). For \(n=3\) both counts are one; for \(n\ge4\) the second is strictly larger, proving failure of marginal, hence joint, symmetry in this subclass.

**Uniform laws.** There are \(2^{n-2}\) normalized connected words. The last one-run has length at least two with probability \(1/2\), giving \(\Pr(t=0)=1/2\). For \(1\le j\le n-3\), exactly \(j\) zeros immediately precede the final one and an earlier one separates them from the initial zero; hence
\[
\Pr(t=j)=2^{-j-1},\quad
\Pr(t=n-2)=0,\quad
\Pr(t=n-1)=2^{-(n-2)}.
\]
These disjoint events exhaust the sample space. Summing their first and second moments gives \(\mathbb E t=1\) and \(\operatorname{Var}(t)=2-2^{3-n}\). The displayed limiting law follows.

Let \(L_n\) be the longest string of consecutive ones in the normalized creation word. The run formula gives \(L_n-1\le s(G_n)\le L_n\). For any fixed \(\eta\in(0,1)\), a union bound on the possible starting positions of a run of length \(\lceil(1+\eta)\log_2 n\rceil\) gives probability tending to zero. For a run length \(\lfloor(1-\eta)\log_2 n\rfloor\), divide the \(n-2\) free symbols into disjoint blocks of that length. The probability none is all ones is at most
\[
\exp\left[-\left\lfloor\frac{n-2}{\lfloor(1-\eta)\log_2 n\rfloor}\right\rfloor 2^{-\lfloor(1-\eta)\log_2 n\rfloor}\right]\longrightarrow0.
\]
Thus \(s(G_n)/\log_2 n\to1\) in probability. In particular, the event \(\{0,1,\dots,\lfloor\tfrac12\log_2 n\rfloor\}\) has probability tending to one for \(t(G_n)\) but to zero for \(s(G_n)\). By the variational definition of total variation and the universal upper bound one, the total-variation limit is one.

## Verification

The standalone Python 3 file `verify.py` independently constructs every connected threshold graph from its normalized word for orders \(3\le n\le13\), calculates both graph statistics directly from vertex neighborhoods, and separately calculates them from the run description. It checks all \(4094\) graphs, all \(539\) bounded generating-function comparisons for \(0\le S,T\le6\) and \(3\le n\le13\), and the exact finite marginal and moment formulas. Run: `python3 verify.py`. The program uses only Python's standard library and integer/rational arithmetic. Finite enumeration corroborates but does not replace the all-order proof above.

## Relationship to prior work

Fürnsinn, Gangl and Rubey [1] prove joint symmetry of sibling and tuft numbers over all unlabeled connected graphs and, more strongly, within the connected chordal graphs. They do not state the threshold-subclass joint enumerator or its strong asymptotic failure; a symmetry over a class does not imply the same symmetry in a strict subclass. The original May 2025 preprint and its 2026 journal version were compared for these parameters, including the refined reduction theorem.

The canonical binary representation and the associated twin blocks are standard in threshold-graph theory [2,3]. Sciriha and Farrugia [2] describe coduplicate/duplicate structure in this family, but their structural classification does not count the maximum closed-twin class jointly with the maximum leaf tuft. Galvin, Wesley and Zacovic [3] enumerate threshold graphs according to order, connectivity and other statistics, but not this two-parameter distribution. The result combines these standard encodings to locate and quantify a sharp restriction boundary of [1].

## Limitations

This is a result about unlabeled connected **threshold** graphs, not arbitrary connected chordal graphs, for which [1] establishes symmetry. It does not construct a bijection between the two statistics on all connected graphs. The finite rational generating function uses upper-bound variables \(S,T\); a full bivariate polynomial at fixed order is obtained by finite differences. No independent external scientific audit has been performed. Historical priority beyond the inspected papers and indexed mathematical-record searches remains open to further review.

## References

1. F. Fürnsinn, M. Gangl and M. Rubey, *Unexpectedly, a symmetry on unlabeled graphs*, arXiv:2505.03665, first public May 6, 2025; *Electronic Journal of Combinatorics* 33(4) (2026), #P4.32, https://arxiv.org/abs/2505.03665 and https://doi.org/10.37236/15312.
2. I. Sciriha and S. Farrugia, *On the Spectrum of Threshold Graphs*, *International Scholarly Research Notices* (2011/2012), Article 108509, https://doi.org/10.5402/2011/108509.
3. D. Galvin, G. Wesley and B. Zacovic, *Enumerating threshold graphs and some related graph classes*, *Journal of Integer Sequences* 25 (2022), Article 22.2.7, https://cs.uwaterloo.ca/journals/JIS/VOL25/Galvin/galvin2.html.
