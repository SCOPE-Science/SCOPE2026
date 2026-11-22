# Early homotopy and complete degree-zero furtherness persistence of upper-truncated Boolean posets

## Finding
For integers \(2\le r<n\), let
\[
P_{n,r}=\{A\subseteq[n]:|A|\ge r\}
\]
be ordered by inclusion, with its lower Alexandrov topology. Fix \(S\in P_{n,r}\) of size \(r\le k=|S|<n\). Write \(U_A=\{B\in P_{n,r}:B\subseteq A\}\). The *centered furtherness filtration* is the order complex
\[
F_S(t)=\Delta\bigl(\{A\in P_{n,r}:\Psi_S(A)=|U_A\setminus U_S|\le t\}\bigr),\qquad t\in\mathbb R_{\ge0},
\]
with the natural inclusion maps. Define the nonnegative integers
\[
\begin{aligned}
 d&=\binom nr-\binom kr,\\
 a&=(n-k)\binom{k}{r-1},\\
 i&=d-a,\\
 b&=(n-k)(k-r)\binom{k}{r-1},\\
 c&=r\left(\binom n{r+1}-\binom k{r+1}\right)-d.
\end{aligned}
\]
**Theorem (early homotopy phases).** The homotopy types, including all components, are
\[
F_S(t)\simeq
\begin{cases}
\mathrm{pt},&0\le t<1,\\
\mathrm{pt}\ \sqcup\ \bigsqcup^{d}\mathrm{pt},&1\le t<r+1,\\
\left(\bigvee^{b}S^1\right)\ \sqcup\ \bigsqcup^{i}\mathrm{pt},&r+1\le t<r+2,\\
\bigvee^{c}S^1,&r+2\le t<\binom{r+2}{r}+1.
\end{cases}
\]
Here a wedge of zero circles is a point. In particular, \(b\) and \(c\) are **integral** first Betti numbers; every other positive-dimensional integral homology group vanishes in the displayed stages. The inclusion \(F_S(r+1)\hookrightarrow F_S(r+2)\) induces a **split injective** map on \(H_1(-;\mathbb Z)\), of rank \(b\) into rank \(c\), with free cokernel of rank \(c-b\).

**Theorem (complete degree-zero barcode).** For all real filtration levels, not just the displayed early stages, the ordinary degree-zero persistence barcode over every field consists of exactly
\[
\boxed{[0,\infty)\quad\text{once};\qquad [1,r+1)\quad\text{with multiplicity }a;\qquad [1,r+2)\quad\text{with multiplicity }i.}
\]
The same statement holds as a direct-sum decomposition of the degree-zero integral persistence module into free interval modules. There are no additional degree-zero births after level one. No assertion is made about the full positive-degree barcode after the early stages.

For example, at \((n,r,k)=(6,2,3)\), \((d,a,i,b,c)=(12,9,3,9,26)\). Thus the degree-zero finite bars comprise nine \([1,3)\) and three \([1,4)\), while the first connected component changes from a bouquet of nine circles at level three to a bouquet of 26 circles at level four.

## Assumptions and scope
All subsets are labelled; the poset **includes** the full set \([n]\) and omits every subset of size below \(r\), including the empty set. The order complex has one vertex for each poset point and simplices for its strict inclusion chains. Downsets \(U_A\) are calculated *inside* \(P_{n,r}\), not inside the full Boolean lattice. The threshold is inclusive; a bar \([u,v)\) is present at birth and absent at death. Integral homology is the usual unreduced homology of the realization, with reduced homology implicit only in wedge notation. No assumption about probability, genericity, field coefficients or high-dimensional collapse algorithms is used. The restriction \(r\ge2\) isolates the new truncated-rank family from the established full nonempty-Boolean case \(r=1\).

## Proof
**1. A gap in the furtherness weights.** If \(A\subseteq S\), then \(\Psi_S(A)=0\). If \(|A|=r\) and \(A\not\subseteq S\), its downset in \(P_{n,r}\) is \(\{A\}\), so \(\Psi_S(A)=1\). If \(|A|=r+1\) and \(A\not\subseteq S\), its downset comprises \(A\) and its \(r+1\) subsets of cardinality \(r\). Precisely one of these smaller subsets lies inside \(S\) when \(|A\setminus S|=1\); none does when \(|A\setminus S|\ge2\). Therefore
\[
\Psi_S(A)=\begin{cases}r+1,&|A\setminus S|=1,\\r+2,&|A\setminus S|\ge2.\end{cases}
\]
If \(|A|\ge r+2\) and \(A\not\subseteq S\), choose a subset \(B\subseteq A\) of size \(r+2\) containing at least one element outside \(S\). Since downsets grow under inclusion,
\[
\Psi_S(A)\ge\Psi_S(B)
=\sum_{j=r}^{r+2}\binom{r+2}{j}-\sum_{j=r}^{|B\cap S|}\binom{|B\cap S|}{j}
\ge\binom{r+2}{r}+1>r+2.
\]
The second sum is zero when \(|B\cap S|<r\). The lower bound is attained among such \(B\) when exactly one element lies outside \(S\); the last strict inequality uses \(r\ge2\). Thus through the whole half-open window \(0\le t<\binom{r+2}{r}+1\), all points outside \(U_S\) in the filtration have rank only \(r\) or \(r+1\), with appearance times exactly as above.

**2. The relative graph model.** The initial order complex \(K_0=\Delta(U_S)\) is contractible because \(S\) is its maximum. At every stage of the displayed window, a strict chain with a vertex outside \(U_S\) has length at most two: the first outside point has rank at least \(r\), and the last outside point has rank at most \(r+1\); no point in \(U_S\) can lie above an outside point. The only edges outside \(K_0\) are thus those from \(r\)-subsets to their containing \((r+1)\)-subsets, with at least one endpoint outside \(U_S\). There are **no** higher-dimensional simplices touching the complement of \(K_0\). Since \(K_0\) is a contractible CW subcomplex, collapsing it to one vertex preserves homotopy type, and these collapses are compatible with inclusion across the early stages. The resulting spaces are ordinary graphs, possibly together with isolated vertices.

**3. First two phase transitions.** At \(t=1\), all \(d=\binom nr-\binom kr\) exterior \(r\)-subsets appear, isolated from \(K_0\) and each other. No new points appear before \(r+1\). At \(t=r+1\), fix one outside element \(j\in[n]\setminus S\). This introduces \(\binom{k}{r}\) points of rank \(r+1\) of the form \(T\cup\{j\}\) (with \(|T|=r\), \(T\subseteq S\)); the \(\binom{k}{r-1}\) exterior rank-\(r\) points of the form \(R\cup\{j\}\) are already present. Each rank-\((r+1)\) point has exactly \(r\) adjacent exterior rank-\(r\) points and one adjacent rank-\(r\) point of \(K_0\). All these new vertices lie in one component with the core, because every \((r-1)\)-subset of \(S\) extends to an \(r\)-subset of \(S\). For each \(j\), the relative number of edges minus newly connected vertices is
\[
(r+1)\binom{k}{r}-\binom{k}{r}-\binom{k}{r-1}
=(k-r)\binom{k}{r-1}.
\]
Summing over the \(n-k\) outside elements gives \(b\) circles in the core component. Exactly \(i=d-a\) rank-\(r\) vertices having at least two elements outside \(S\) remain isolated. This proves the third homotopy phase, including its component count.

At \(t=r+2\), **every** rank-\((r+1)\) point is present. The graph is now connected: any two rank-\(r\) subsets are joined in the usual Johnson graph by successive one-element swaps, each swap realized through the common rank-\((r+1)\) superset; and at least one rank-\(r\) subset lies in \(S\), joining the graph to the core. Outside the core, the graph has
\[
V_{\mathrm{new}}=\left(\binom nr-\binom kr\right)+\left(\binom n{r+1}-\binom k{r+1}\right)
\]
vertices and
\[
E_{\mathrm{new}}=(r+1)\left(\binom n{r+1}-\binom k{r+1}\right)
\]
edges, because every exterior rank-\((r+1)\) point is incident with all \(r+1\) rank-\(r\) subsets. A connected finite graph has first Betti number \(E-V+1\); accounting for the single collapsed core vertex yields \(E_{\mathrm{new}}-V_{\mathrm{new}}=c\). This proves the fourth phase, and the uniform weight gap proves the asserted interval of constancy.

**4. Persistence maps and all subsequent degree-zero stages.** The graph at \(r+1\) is literally a subgraph of the one at \(r+2\) after simultaneously collapsing the fixed core. An inclusion of graphs induces an injection on integral first homology: its cycle lattice is the kernel of the integral vertex-incidence map, and existing cycles cannot become boundaries because no two-cells are added. Moreover, the image is saturated: a cycle in the larger graph having an integer multiple supported on the old edges is itself supported there, so its quotient lattice is torsion-free. Therefore the map is split injective, with free cokernel of rank \(c-b\).

At threshold \(r+1\), the \(a\) one-outside rank-\(r\) points join the distinguished component, killing exactly \(a\) classes born at level one. At threshold \(r+2\), the remaining \(i\) isolated vertices join, killing exactly \(i\) more. Above \(r+2\), every newly entering poset point of rank at least \(r+2\) contains a rank-\(r\) subset that was already present; hence it immediately attaches to the existing connected component. There are no further connected-component births or mergers. The unique component initially born at zero persists indefinitely. These connectivity statements, including the natural maps, give the claimed complete degree-zero barcode and its integral free-interval splitting.

## Verification
The standalone Python 3 file `verify.py` computes literal truncated-poset downset differences rather than relying on the displayed closed formulas. It enumerates vertices, comparable pairs and three-element chains at five thresholds, constructs simplicial degree-one and degree-two boundary matrices, and separately reduces them over \(\mathbb F_2\). For every \(3\le n\le7\), \(2\le r<n\), \(r\le k<n\), it compares actual degree-zero and degree-one ranks with the theorem and checks injectivity of the degree-one map through its image modulo the later boundary group. Its reproducible standard output is

```
VERIFY_OK cases=35 2_simplices_scanned=8380 H1_injections=35
```

The proof, not this finite enumeration, establishes the unbounded-in-\(n\) integral homotopy and persistence statements. The checker covers mod-two homology and does not by itself certify integral torsion-freeness; the graph quotient and saturated integral cycle lattices supply that argument.

## Relationship to prior work
Badra and Singh's *Furtherness in finite topological spaces* (arXiv:2603.18580, first posted March 19, 2026) introduces the asymmetrical furtherness metric. Their *Persistence diagrams of finite topological spaces* (arXiv:2610.16386v1, first posted October 12, 2026, primary MSC2020 55N31) defines the centered filtration and proves general degree-zero birth and stability statements, but does not give these truncated Boolean homotopy phases, explicit death multiplicities or integral first-homology injections.

The published result *Complete integral furtherness barcodes of Boolean subset posets* handles the **different finite space** of **all nonempty** subsets, which includes rank-one points and has furtherness weights \(2^{|A|}-2^{|A\cap S|}\). Its all-degree scale-doubling barcode is not a statement about the rank-truncated posets here: removing all ranks below \(r\) alters both downsets and every rank-\((r+1)\) entrance weight. The published *Extremal-root furtherness barcodes on Boolean sphere posets* instead uses all nonempty **proper** subsets with roots only at extreme ranks; it cannot imply this rank-truncated family. The published *Complete integral persistence of rank-span filtered proper Boolean lattices* varies allowable *chain rank spans* rather than the center's furtherness threshold, so its homotopy classifications and formulas concern a different filtration. General graph homology calculations explain how to count circles once the early graph model is proved, but do not supply that model, the sharp stage thresholds or the coefficient-independent persistence assertions.

## Limitations
The homotopy classification is established only through the explicitly stated early filtration window. The complete barcode assertion concerns degree zero only. Positive-degree intervals can subsequently die when higher-rank poset points enter, and no full positive-degree barcode, canonical graph basis, or classification for arbitrary rank-selected posets is claimed. The asserted first-homology injection is only between the two specified early stages, not through all later maps. Existing full-Boolean and proper-Boolean results are not claimed as new. Equivalent unindexed or unpublished literature may exist; independent mathematical validation has not been performed.

## References
1. A. Badra and H. K. Singh, *Persistence diagrams of finite topological spaces*, arXiv:2610.16386v1 (October 12, 2026), https://arxiv.org/abs/2610.16386 .
2. A. Badra and H. K. Singh, *Furtherness in finite topological spaces*, arXiv:2603.18580v1 (March 19, 2026), https://arxiv.org/abs/2603.18580 .
3. *Complete integral furtherness barcodes of Boolean subset posets*, public mathematical research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-complete-integral-furtherness-barcodes-of-boolean-subset-posets--d2db8c5d42da/RESULT.md .
4. *Extremal-root furtherness barcodes on Boolean sphere posets*, public mathematical research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-extremal-root-furtherness-barcodes-on-boolean-sphere-posets--06baeffcb578/RESULT.md .
5. *Complete integral persistence of rank-span filtered proper Boolean lattices*, public mathematical research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-complete-integral-persistence-of-rank-span-filtered-proper-boole--8ff573fb2efc/RESULT.md .
