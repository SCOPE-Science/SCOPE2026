# Exact shattering polynomial and palette transition for complete-bipartite proper colourings

## Finding

Let \(m,n\geq1\) and \(q\geq2\) be integers, and write \(G=K_{m,n}\) with nonempty labelled parts \(A\) and \(B\). Each proper colouring \(f:V(G)\to[q]\) is a binary concept \(h_f\) on the **vertex--colour equality query domain** \(X=V(G)\times[q]\), given by \(h_f(v,a)=1\) if and only if \(f(v)=a\). Colour names are distinguishable; using every colour is not required.

For every palette size, the exact static and adaptive shattering ranks coincide:

\[
\boxed{\operatorname{VCdim}(\mathcal H_{m,n,q})=\operatorname{Ldim}(\mathcal H_{m,n,q})=
\begin{cases}
1,&q=2,\\
\max\{m,n\}+1,&q=3,\\
m+n,&q\geq4.
\end{cases}}
\]

More strongly, when \(q=3\), **every shattered support** \(S\subseteq V(G)\times[3]\) is characterized as follows. At most one query may concern any vertex. Such a support is shattered precisely in either of two cases:

1. All tested vertices lie in one bipartition class, and the colour names appearing in their queries number at most two; or
2. Both classes are tested, the queries within each class use one constant colour name, those two names are different, and at least one class contributes exactly one tested vertex.

The empty support is included in the first case. Write \(s_k(m,n)\) for the number of \(k\)-element shattered query supports at three colours. Their complete polynomial is

\[
\boxed{\begin{aligned}
\Phi_{m,n}(z)&=\sum_{k=0}^{m+n}s_k(m,n)z^k\\
&=1+3\bigl[(1+2z)^m-(1+z)^m+(1+2z)^n-(1+z)^n\bigr]\\
&\quad+6nz\bigl[(1+z)^m-1\bigr]+6mz\bigl[(1+z)^n-1\bigr]-6mnz^2.
\end{aligned}}
\]

In particular its degree is \(\max\{m,n\}+1\). For fixed \(m,n\geq2\), the three-colour rank deficit relative to the total number of graph vertices is \(\min\{m,n\}-1\), and this deficit disappears immediately at four colours. In contrast to the three-colour path and cycle examples, the complete-bipartite family has no VC--Littlestone gap.

## Assumptions and scope

All graphs are finite, simple and labelled. Both parts have at least one vertex; isolated parts are not allowed. A proper colouring sends endpoints of each edge to distinct palette names, with no surjectivity requirement. Tests are **binary equalities** \((v,a)\), not requests to predict the complete colour label or to recover an unknown graph. VC dimension is taken on subsets of the equality-query domain, while Littlestone dimension refers to realizable complete binary mistake trees on that same domain.

## Proof

**A. Elementary restrictions on supports.** If \(S\) contains two tests \((v,a)\), \((v,b)\) with \(a\neq b\), the trace assigning both label one is impossible. Thus every shattered support contains at most one test per graph vertex. For \(q=3\), denote by \(S_A,S_B\) the supports in the two classes, and by \(C_A,C_B\) the sets of their respective tested colour names.

Suppose first \(S_B=\varnothing\). The all-positive trace requires the colours in \(C_A\) to occur in \(A\); since \(B\neq\varnothing\) and every colour on \(B\) must differ from all colours on \(A\), this is possible only when \(|C_A|\leq2\). Conversely, if \(|C_A|\leq2\), choose a two-element palette containing \(C_A\). For each queried vertex of \(A\), set the vertex to its tested colour for a required one and to the other colour of the two-element palette for a required zero. Colour all other vertices of \(A\) within those same two colours and colour all of \(B\) with the unused third colour. This realizes every trace. The case \(S_A=\varnothing\) is symmetric.

Now suppose \(S_A\) and \(S_B\) are both nonempty. The all-positive trace requires \(C_A\cap C_B=\varnothing\). If \(|C_A|\geq2\), choose a trace making every test of \(A\) positive and every test of \(B\) negative. The vertices of \(A\) then use both colours in \(C_A\), so every vertex of \(B\) is forced to the single remaining colour, the colour common to its tested queries. This contradicts the required negatives. The same argument interchanging the parts forces \(|C_B|=1\). Thus each side's tested name is constant, say \(\alpha\) on \(A\) and \(\beta\) on \(B\), with \(\alpha\neq\beta\).

If both \(|S_A|\geq2\) and \(|S_B|\geq2\), choose a trace with at least one positive and at least one negative test on each side. A negative test in \(A\) then cannot take \(\alpha\) (its own forbidden colour) or \(\beta\) (used by a positive test on \(B\)); hence it must use the third colour \(\gamma\). The same argument forces a negative tested vertex of \(B\) also to use \(\gamma\), violating adjacency. Therefore \(\min\{|S_A|,|S_B|\}=1\) is necessary.

It is sufficient. Suppose, without loss, that \(S_B\) is the singleton test with target \(\beta\), while every test of \(A\) has target \(\alpha\neq\beta\), and let \(\gamma\) be the third colour. For a required positive answer on \(B\), colour all of \(B\) with \(\beta\), and assign tested vertices in \(A\) either \(\alpha\) or \(\gamma\) according to their requested one/zero labels. For a required negative answer on \(B\), colour all of \(B\) with \(\gamma\), and assign the tested \(A\)-vertices \(\alpha\) or \(\beta\) accordingly. Colour unqueried \(A\)-vertices \(\alpha\). Every required trace extends to a proper colouring. This proves the complete support classification.

**B. Enumerating the supports.** For \(k\geq1\) distinct tested vertices contained in one part, the number of assignments of tested colour names using at most two of the three names is
\(3+3(2^k-2)=3(2^k-1)\). Hence the one-part contributions are
\(3[(1+2z)^m-(1+z)^m]\) and the symmetric expression with \(n\). For the cross-part supports with \(|S_A|=a\geq1\) and \(|S_B|=1\), the choices are \(6\binom ma n\) (two distinct ordered colour names). Their generating expression is \(6nz[(1+z)^m-1]\), and the symmetric expression is \(6mz[(1+z)^n-1]\). The supports with one test on each side were counted twice, so subtract \(6mnz^2\). Add the empty support to obtain the displayed polynomial. Its largest nonzero coefficient occurs in degree \(\max\{m,n\}+1\), where a full larger-part support and one smaller-part test provide an explicit witness.

**C. Three-colour Littlestone rank.** Every proper three-colouring uses disjoint colour-name sets on \(A\) and \(B\); therefore at least one side is monochromatic. There are \(3\cdot2^n\) proper colourings monochromatic on \(A\), and \(3\cdot2^m\) monochromatic on \(B\), with the six colourings monochromatic on both sides counted twice. Thus
\[
|\mathcal H_{m,n,3}|=3(2^m+2^n-2).
\]
The action of permuting the three colour names is transitive on the possible value at any fixed vertex. Consequently, for **every** vertex--colour query, precisely \(2^m+2^n-2\) hypotheses answer one. Writing \(N=\max\{m,n\}\), this number is strictly smaller than \(2^{N+1}\). A complete binary mistake tree of depth \(N+2\) would require at least \(2^{N+1}\) *distinct* hypotheses in the positive child of its root, a contradiction. Hence \(\operatorname{Ldim}\leq N+1\). The degree-\(N+1\) shattered support in Part B gives \(\operatorname{VCdim}\geq N+1\), and \(\operatorname{VCdim}\leq\operatorname{Ldim}\), establishing equality.

**D. Other palette sizes.** If \(q=2\), connectedness gives exactly two proper colourings, one with \(A\) colour one and \(B\) colour two, and the other with their names swapped. A nonconstant equality test witnesses dimension one, while the two-hypothesis count bounds Littlestone dimension by one.

For any \(q\) and any class of single-valued functions on a set of \(t\) vertices, encoded as equality tests \((v,a)\), a complete mistake tree cannot have depth exceeding \(t\): follow the path that takes the positive child at every level. A repeated tested vertex would have its colour fixed by the earlier positive test, leaving one of the two later children empty. Thus this all-positive branch contains at most \(t\) tests. Apply this to \(t=m+n\). When \(q\geq4\), test all vertices of \(A\) for colour one and all vertices of \(B\) for colour three. Any binary trace is realized by giving vertices of \(A\) colours one or two, and vertices of \(B\) colours three or four, according to the required labels. The palettes are disjoint, so every extension is proper. Thus \(m+n\) tests are VC-shattered. Combined with the general upper bound and \(\operatorname{VCdim}\leq\operatorname{Ldim}\), both ranks equal \(m+n\).

## Verification

Run `python3 verify.py` with Python 3.10 or later; the script requires only the standard library. It independently enumerates all proper three-colourings and candidate query supports on eight biclique parameter pairs, through \((m,n)=(4,4)\), and checks the **entire** predicted polynomial rather than merely its degree. It separately computes the complete-mistake-tree recursion on fifteen smaller parameter/palette combinations, including \(q=2,3,4,5\), and checks a full-support witness when \(q\geq4\). The recorded output is in `checker_output.txt`. These are finite checks; Parts A--D give proofs for every claimed parameter.

## Relationship to prior work

Blanca, Chen, Štefankovič and Vigoda (2017) study the space of proper graph colourings as graph homomorphisms, but their structure-learning problem recovers the unknown **graph** from sampled colourings; it does not compute VC or online ranks for an unknown **colouring** queried through equality literals. Guingona, Kolesnikov, Nierwinski and Soucy (2021) prove equality of the two dimensions for zero sets of linearly independent functions; those linear-combination concept families do not contain the present constrained-colouring class as an identified instance, and do not yield the support polynomial. Walker (2022) supplies general tree-shattering background, not these exact values.

The published work *Forced three-colouring polynomial of complete bipartite graphs* (2026) gives an exact probability/generating polynomial for **partial assignments that force an entire colouring**. Its side-colour rigidity is compatible with Part C, but forcing an entire colouring is a different property from realizing every binary trace. It does not give the query-support characterization or the polynomial above. Earlier path- and cycle-colouring shattering calculations concern different graph families; indeed the complete-bipartite family here has no static/adaptive gap. The contextual observations that two-colour connected bipartite graphs have two colourings and that four colour names suffice for full-vertex shattering of every bipartite graph are not asserted as novel. The assessed contribution is the complete three-colour shattered-support classification and generating polynomial, with the resulting all-palette exact rank theorem.

## Limitations

The theorem does not describe the full shattered-support polynomial for palettes of size four or greater, nor does it claim extension to arbitrary bipartite graphs or to multicolour-valued predictions rather than equality tests. The finite enumerations cannot establish the infinite-parameter cases by themselves. Priority checks covered relevant accessible literature and research records but cannot rule out a synonymous earlier characterization; independent scientific review has not been performed.

## References

1. A. Blanca, Z. Chen, D. Štefankovič, E. Vigoda, *Structure Learning of H-colorings*, arXiv:1708.05118, first submitted 17 August 2017. https://arxiv.org/abs/1708.05118
2. V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first submitted 10 September 2021. https://arxiv.org/abs/2109.04805
3. R. Walker, *Tree Dimension and the Sauer--Shelah Dichotomy*, arXiv:2203.12211, first submitted 23 March 2022. https://arxiv.org/abs/2203.12211
4. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, ALT 2021, PMLR 132, pp. 686--696. https://proceedings.mlr.press/v132/ghazi21a.html
5. *Forced three-colouring polynomial of complete bipartite graphs*, publicly posted 4 October 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69/RESULT.md
