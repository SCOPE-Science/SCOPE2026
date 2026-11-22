# Exact synchronization shells and a critical slowing transition for NOR dynamics on de Bruijn digraphs

## Finding

Let \(q\ge2\), \(d\ge1\), and let \(D(q,d)\) be the directed de Bruijn graph whose vertices are all words of length \(d\) over an alphabet \(\Sigma\) of size \(q\). Under synchronous incoming-neighbor NOR, every configuration first becomes spatially constant by update \(d\); the bound is sharp and the sole recurrent orbit is the alternation of the two uniform configurations. For independent Bernoulli\((p)\) initial bits, with \(p_0=p\) and \(p_{t+1}=(1-p_t)^q\), the exact first-constant-time distribution is

\[
 \Pr_p(T\le t)=p_t^{q^{d-t}}+(1-p_t)^{q^{d-t}},\qquad 0\le t\le d.
\]

Here \(T\) is the earliest time at which the entire graph has a common value. In particular, the exact number of labelled initial configurations with \(T\le t\) is

\[
 A_t=a_t^{q^{d-t}}+b_t^{q^{d-t}},\quad
 a_0=b_0=1,\quad a_{t+1}=b_t^q,\quad b_{t+1}=2^{q^{t+1}}-b_t^q.
\]

The count of states entering at precisely \(t\) is \(A_t-A_{t-1}\) for \(1\le t\le d\), with \(A_0=2\). The fraction of initial states at the uniform-one phase at update \(d\) is \(a_d/2^{q^d}\).

There is also a sharp change of typical synchronization scale. Let \(p_*(q)\) be the unique solution in \((0,1)\) of \(p=(1-p)^q\). For fixed \(p\in(0,1)\) distinct from \(p_*\), as \(d\to\infty\),

\[
 T=2\log_q d+O_{\mathbb P}(1).
\]

At the critical bias \(p=p_*\), however,

\[
 \Pr_{p_*}(d-T\ge s)=p_*^{q^s}+(1-p_*)^{q^s}
 \quad(0\le s\le d),
\]

so \(T=d-O_{\mathbb P}(1)\) instead. Thus the typical clock changes from order \(\log d\) to the full graph depth \(d\) at one explicitly characterized initialization bias.

## Assumptions and scope

A vertex is a word \(w=w_1\cdots w_d\in\Sigma^d\). There is an arc from \(a u\) to \(u b\) for every \(a,b\in\Sigma\) and \(u\in\Sigma^{d-1}\); constant-word self-loops are retained. Each vertex has precisely \(q\) distinct incoming neighbors. A Boolean configuration is \(x:\Sigma^d\to\{0,1\}\), and

\[
 (F x)(u b)=\prod_{a\in\Sigma}(1-x(a u)).
\]

All vertices update simultaneously. In particular, a constant-one state maps to constant zero and conversely. There are no additional self-inputs beyond the directed self-loops specified by the graph. The probability statements assume that all \(q^d\) initial vertex values are independent with the same probability \(p\) of being one. The asymptotic parameter is the word length \(d\); \(q\) and \(p\) are fixed. Both endpoints \(p=0,1\) yield \(T=0\) and are excluded from the off-critical asymptotic statement.

## Proof

**1. Exact nested-tree block representation.** For any \(t\ge0\), define the Boolean function \(\Phi_t\) of \(q^t\) inputs by \(\Phi_0(z)=z\), and let \(\Phi_{t+1}\) be the NOR of the \(q\) successive disjoint blocks evaluated with \(\Phi_t\). For \(0\le t\le d\), induction on the update rule gives

\[
 (F^t x)(u v)=\Phi_t\big((x(a u))_{a\in\Sigma^t}\big),
 \qquad |u|=d-t,\quad |v|=t.
\]

The order of the \(q^t\) inputs can be chosen recursively; it has no effect on the Boolean NOR tree. For fixed prefix \(u\), the output is independent of \(v\). The \(q^{d-t}\) distinct prefixes \(u\) index disjoint sets of initial coordinates \(\{a u:a\in\Sigma^t\}\), together partitioning all \(q^d\) vertices. Consequently, at update \(d\) the state is spatially uniform, and any uniform state thereafter alternates with its complement. Every recurrent configuration therefore belongs to the unique uniform two-cycle, and every initial state enters it no later than \(d\).

To see that \(d\) is sharp, observe that every tree \(\Phi_t\) is surjective: choosing all its inputs zero gives output one when \(t=1\), and recursively either desired output can be realized by selecting inputs to its immediately preceding gates. More concretely, \(\Phi_t\) on uniform input bits has outputs zero and one at opposite input polarities, since a uniform input remains uniform and toggles with each update. At \(t=d-1\) there are \(q\ge2\) disjoint prefix blocks. Choose one block with output zero and another with output one; the resulting state is not uniform at \(d-1\). It therefore has \(T=d\).

**2. Exact counting and biased law.** Let \(a_t\) and \(b_t\) count input assignments for which \(\Phi_t\) respectively equals one and zero. Each of its \(q\) child blocks must output zero for the next gate to output one, so \(a_{t+1}=b_t^q\), while \(a_{t+1}+b_{t+1}=2^{q^{t+1}}\). For arbitrary independent Bernoulli\((p)\) leaves, the one-probability instead obeys \(p_{t+1}=(1-p_t)^q\). Because the prefix blocks partition the original coordinates, their output values at time \(t\) are independent and identically distributed Bernoulli\((p_t)\). Spatial uniformity at that time requires all \(q^{d-t}\) outputs to be one or all to be zero. This proves the asserted probability and counting formulas. Once uniform, a state is always uniform, so the displayed cumulative distribution is exactly the first-entry distribution.

**3. Bias-critical scale.** Put \(\phi(x)=(1-x)^q\) and \(h=\phi\circ\phi\). The decreasing function \(\phi\) has a unique fixed point \(p_*\in(0,1)\). The increasing function

\[
 h(x)=\big[1-(1-x)^q\big]^q
\]

has exactly three fixed points \(0,p_*,1\). Indeed, its derivative

\[
 h'(x)=q^2\big[(1-x)(1-(1-x)^q)\big]^{q-1}
\]

is strictly unimodal on \((0,1)\) (its inner factor has derivative zero only at \((1-x)^q=1/(q+1)\)). Hence \(h(x)-x\) has at most three distinct zeros by Rolle's theorem, and these three are already known. Moreover, writing \(r=1-p_*\), the fixed-point equation \(r+r^q=1\) implies

\[
 1=r^{q-1}(1+r+\cdots+r^{q-1})<q r^{q-1},
\]

so \(|\phi'(p_*)|>1\). Therefore iteration of \(h\) starting below \(p_*\) decreases toward zero, while starting above it increases toward one. Near zero, \(h(x)=q^q x^q(1+O(x))\); near one, \(1-h(1-x)=q x^q(1+O(x^q))\). Thus for any fixed noncritical initial bias there are positive constants \(c,C\), and \(t_0\), with the smaller of \(p_t\) and \(1-p_t\), denoted \(\varepsilon_t\), satisfying

\[
 \exp(-Cq^{t/2})\le\varepsilon_t\le\exp(-cq^{t/2})
 \qquad(t\ge t_0).
\]

For \(m=q^{d-t}\), the exact nonuniformity probability is

\[
 \Pr(T>t)=1-(1-\varepsilon_t)^m-\varepsilon_t^m.
\]

Here \(\Pr(T>t)\to1\) if \(m\varepsilon_t\to\infty\), and \(\Pr(T>t)\to0\) if \(m\varepsilon_t\to0\), given \(m\to\infty\) and \(\varepsilon_t\to0\). Choose \(t=\lfloor2\log_q d-K\rfloor\) or \(t=\lceil2\log_q d+K\rceil\). As \(d\to\infty\), choosing \(K\) sufficiently large and fixed makes the first limit one and the second zero, by the exponential bounds above. Therefore \(T-2\log_q d\) is bounded in probability. At \(p=p_*\), every \(p_t=p_*\), so evaluating the exact CDF at \(t=d-s\) gives the critical tail identity. Its right side decreases doubly exponentially in \(s\), uniformly in \(d\), proving \(d-T=O_{\mathbb P}(1)\).

## Verification

The attached `verify_direct.py` builds the directed incoming neighborhoods from word overlap and independently enumerates all configurations for \((q,d)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1),(4,2)\). In each case it computes first periodic-entry times by genuine synchronous updates, verifies the exact shell formula and the sharp maximum, and checks the uniform-one phase count. For example, the first-entry histogram for \((q,d)=(2,4)\) is \((2,6560,2400,36288,20286)\), totaling \(65536\) configurations. At \((q,d)=(3,2)\) it is \((2,342,168)\), totaling \(512\).

The independent `verify_formula.py` computes finite NOR-tree truth tables without constructing the graph and validates the recursive counts for several alphabet sizes and depths. It also checks all four weighted first-entry CDF values for \(q=2,d=3,p=1/3\) by exact rational weighted enumeration. Executing both scripts with Python 3 standard library produces the recorded results in `verification_output.txt`. Finite checks support the finite formulas but do not replace the all-size proof or establish the asymptotic limits.

## Relationship to prior work

McIntosh's treatment of de Bruijn diagrams explains their word-overlap and path-counting structure, but does not analyze the nonlinear incoming-NOR dynamical rule or its first-entry distribution. Pearl's 1980 minimax-tree study already contains the alternating Boolean tree recursion, an unstable critical Bernoulli bias and rapid off-critical convergence: none of these separate one-dimensional tree properties is claimed as new here. The specific contribution is the de Bruijn network's exact, disjoint-block temporal basin partition and the resulting comparison between a doubly-logarithmic typical synchronization clock and a maximal-depth critical clock.

The indexed prior exact hitting law for incoming-OR on directed de Bruijn graphs uses a single OR over every ancestor. This differs from the alternating nested NOR tree and cannot yield the present biased first-entry distribution or critical slowdown by specialization. General results on directed Boolean-NOR systems allow other recurrent periods on other digraphs; they do not determine the unique cycle or the distribution on this family. The standard undirected symmetric-threshold two-cycle theorem also does not supply this directed nonlinear enumeration.

## Limitations

The graph includes its canonical constant-word loops; deleting them changes the recurrence. Results concern incoming rather than outgoing neighbors, synchronous rather than sequential updates, and independent identically distributed initial bits. The asymptotic law holds for fixed branching alphabet size and fixed noncritical initialization bias; no uniform estimate is claimed when the initial bias approaches its critical value with \(d\). Existing minimax-tree asymptotics overlap with one component of the argument, and equivalent previously unindexed de Bruijn/NOR calculations may exist. No claim of external or independent scientific validation is made.

## References

- J. Pearl, *Asymptotic Properties of Minimax Trees and Game-Searching Procedures*, Artificial Intelligence **14** (1980), 113–138, DOI: 10.1016/0004-3702(80)90037-5. Lawfully available full text: https://ftp.cs.ucla.edu/pub/stat_ser/r21.pdf.
- H. V. McIntosh, *Linear Cellular Automata via de Bruijn Diagrams*, 1991 manuscript: https://delta.cs.cinvestav.mx/~mcintosh/comun/cf/debruijn.pdf.
- C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974 (first posted 2011-08-15): https://arxiv.org/abs/1108.2974.
- *Coexistence of Periods in Parallel and Sequential Boolean Graph Dynamical Systems over Directed Graphs*, Mathematics **8** (2020), 1812: https://www.mdpi.com/2227-7390/8/10/1812.
