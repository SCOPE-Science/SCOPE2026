# Complete packing–domatic colour spectra and witness partitions of complete multipartite graphs

## Finding

For every integer \(r\ge2\), every positive part-size sequence \((a_1,\ldots,a_r)\), and every palette size \(t\ge1\), the following theorem counts all packing colourings of \(G=K_{a_1,\ldots,a_r}\) by their maximum number of broadcast-dominating partition classes, and counts all partitions witnessing any prescribed number of classes. It also gives the entire packing–domatic chromatic spectrum, with a classification and exact multiplicity of every optimal colouring.

Put \(n=\sum_i a_i\), \(a=\max_i a_i\), and \(b=n-a+1\). Write \((x)_{\underline{h}}=x(x-1)\cdots(x-h+1)\), with \((x)_{\underline0}=1\) and value zero if \(0\le x<h\), and let \(\left\{\begin{smallmatrix}h\\k\end{smallmatrix}\right\}\) be a Stirling number of the second kind. Indicator brackets have value zero or one.

A packing colouring is a map \(f:V(G)\to\{1,\ldots,t\}\) such that two vertices of the same colour \(j\) are at graph distance greater than \(j\). A nonempty block \(B\subseteq V(G)\) is broadcast dominating for \(f\) if, for each vertex \(v\), some \(w\in B\) satisfies \(d(v,w)\le f(w)\). Let \(\kappa(f)\) be the maximum number of blocks in a partition of \(V(G)\) into broadcast-dominating blocks.

The **complete capacity enumerator** over labelled vertices and named colours is
\[
E_{G,t}(u)=\sum_{f\text{ packing}}u^{\kappa(f)}
=(t-1)_{\underline{n}}u^n
+\sum_{i=1}^{r}\sum_{s=1}^{a_i}
\binom{a_i}{s}(t-1)_{\underline{n-s}}
 u^{\,n-s+\mathbf{1}_{\{s=a_i\}}}.
\]
Thus the number of packing \(k\)-domatic colourings using the palette \(\{1,\ldots,t\}\) is \(\sum_{j=k}^{n}[u^j]E_{G,t}(u)\).

Let \(W_{G,t,k}\) count **pairs** consisting of a packing colouring and an *unordered* partition into exactly \(k\) nonempty broadcast-dominating blocks (the corresponding ordered-partition count is \(k!W_{G,t,k}\)). Then, for every integer \(1\le k\le n\),
\[
\begin{aligned}
W_{G,t,k}={}&(t-1)_{\underline{n}}
\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\\
&+\sum_{i=1}^{r}\sum_{s=1}^{a_i}
\binom{a_i}{s}(t-1)_{\underline{n-s}}
\left[
k^s\left\{\begin{smallmatrix}n-s\\k\end{smallmatrix}\right\}
+\mathbf{1}_{\{s=a_i\}}
\left\{\begin{smallmatrix}n-s\\k-1\end{smallmatrix}\right\}
\right].
\end{aligned}
\]

For \(1\le k\le n\), the minimum palette size \(\chi_{\rho,k}(G)\) is
\[
\chi_{\rho,k}(G)=
\begin{cases}
b,&k\le b,\\
k,&k>b\text{ and some }a_i=n-k+1,\\
k+1,&k>b\text{ and no }a_i=n-k+1.
\end{cases}
\]
For \(k>n\), no such nonempty-block partition exists.

The exact number \(M_{G,k}\) of optimal **named** colourings, with palette \(\{1,\ldots,\chi_{\rho,k}(G)\}\), is
\[
M_{G,k}=\begin{cases}
\#\{i:a_i=a\}(n-a)!,&k\le b,\\
\#\{i:a_i=n-k+1\}(k-1)!,&k>b,\ n-k+1\in\{a_i\},\\
k!\sum_i\binom{a_i}{n-k},&k>b,\ k<n,\ n-k+1\notin\{a_i\},\\
n!,&k=n,\ 1\notin\{a_i\}.
\end{cases}
\]
In the third case, all optimal colourings select precisely \(n-k\) vertices of one part for colour \(1\), while each of the remaining \(k\) vertices receives a different named colour in \(\{2,\ldots,k+1\}\). In the first two cases, the colour-\(1\) class is a whole part of the indicated size and the other vertices receive distinct remaining colours. In the last case colour \(1\) is unused.

For example, \(K_{3,3}\) has the spectrum \((4,4,4,4,6,7)\) for \(k=1,\ldots,6\). The jump from four to six at \(k=5\) is caused by the missing part size \(2\); this gap is not visible from the ordinary packing chromatic number alone.

## Assumptions and scope

Graphs are finite, simple, undirected, connected complete multipartite graphs with at least two nonempty parts. All vertices are individually labelled, and the numerical colour labels are distinguished; unused palette colours are allowed. Graph distance is the usual shortest-path distance. A vertex broadcasts to itself at distance zero. Partition blocks are required to be nonempty. For the Stirling numbers, \(\left\{\begin{smallmatrix}0\\0\end{smallmatrix}\right\}=1\) and other out-of-range arguments contribute zero. Each formula applies without symmetry quotients, for all listed integer parameters, including complete graphs (all part sizes one) and stars.

## Proof

**Packing-colour structure.** Distinct vertices of a complete multipartite graph are at distance one if they belong to different parts and two if they are in the same part. Hence a colour \(j\ge2\) can occur on at most one vertex, whereas all vertices of colour \(1\), if any, lie in a unique part \(V_i\). Conversely every labelling with this structure is packing. If the colour-\(1\) class has size \(s\) in \(V_i\), the remaining \(h=n-s\) vertices receive an injection into the \(t-1\) higher colours; there are \(\binom{a_i}{s}(t-1)_{\underline{h}}\) labellings. If colour \(1\) is absent there are \((t-1)_{\underline{n}}\).

**Broadcast-partition structure.** Each vertex of colour at least two broadcasts to every vertex, because the graph has diameter at most two. Every block containing one such vertex is therefore dominating. A nonempty block containing only colour-\(1\) vertices cannot cover any other colour-\(1\) vertex outside that block; it is dominating if and only if it is the entire colour-\(1\) class and that class equals one whole part \(V_i\). Consequently, if \(h\) vertices have colours at least two, \(\kappa(f)=h+1\) exactly when the colour-\(1\) class is an entire part, and otherwise \(\kappa(f)=h\). If colour \(1\) is absent, \(\kappa(f)=n\). In the nonexceptional case, partition the \(h\) high-colour vertices into singleton blocks and attach all colour-\(1\) vertices arbitrarily; in the exceptional case retain the entire colour-\(1\) part as its own extra block. These constructions attain the bounds.

**Enumerators.** Summing the mutually exclusive cases in the first two paragraphs proves \(E_{G,t}\). A partition with every block containing a high-colour vertex is made by partitioning those \(h\) vertices into \(k\) nonempty *unlabelled* blocks in \(\left\{\begin{smallmatrix}h\\k\end{smallmatrix}\right\}\) ways, then independently sending each of the \(s\) colour-\(1\) vertices to one of these \(k\) blocks: \(k^s\) ways. The only other possibility is exactly one block containing no high-colour vertex; then the colour-\(1\) class must be a whole part, and the \(h\) other vertices form \(k-1\) nonempty blocks, yielding \(\left\{\begin{smallmatrix}h\\k-1\end{smallmatrix}\right\}\) choices. Summing proves \(W_{G,t,k}\). The constructions and obstruction are exhaustive, so there are no extra terms.

**Minimum palette and all optimizers.** Every colouring requires at least \(h\) distinct colours greater than one, so \(t\ge h+1\). A colour-\(1\) class has size at most \(a\); this forces \(t\ge b=n-a+1\). Furthermore \(\kappa(f)\le t\), so \(t\ge k\). If \(k\le b\), taking colour \(1\) on a largest part and assigning all remaining vertices distinct higher colours attains \(t=b\). If \(k>b\), equality \(t=k\) requires \(h=k-1\), with the whole colour-\(1\) class an entire part of size \(n-k+1\); this condition is also sufficient. When no such part exists, \(t\ge k+1\); it is attained by selecting \(n-k\) vertices from a largest part for colour \(1\) if \(k<n\), or by using colours \(2,\ldots,n+1\) bijectively when \(k=n\). The injection count in each equality case gives precisely the four displayed multiplicity formulas. This completes the unrestricted proof.

## Verification

The accompanying `verify.py` independently enumerates all colour functions on 116 labelled complete-multipartite graph/palette instances, constructs the actual graph distances, tests the packing condition, enumerates set partitions via a subset recursion, and compares their broadcast-dominating capacities and partition counts with both symbolic formulas. It checks 67,470 feasible packing colourings, together with 96 graph/partition-size optimality and optimal-multiplicity cases. All checks pass with `VERIFY_OK`. Exhaustive small-instance checks corroborate, rather than replace, the unrestricted argument above.

## Relationship to prior work

Brešar, Ferme and Hu introduced packing \(k\)-domatic colourings and proved, among other results, the general equality \(\chi_{\rho,3}(G)=\chi_\rho(G)\) when the minimum degree is at least two, as well as path and cycle cases [1]. The scalar \(k=2,3\) overlap with their general results is not claimed as new. The contribution here is the all-palette, all-capacity enumeration and the all-\(k\) multipartite spectrum, including gaps determined by *which* part sizes occur and exact numbers of colourings and witnessing partitions. Packing total colourings [2] and correspondence/list packing of proper graph colourings [3] involve different objects and constraints; neither implies these broadcasting-partition counts. A search of relevant mathematical records found no equivalent formula. Historical priority remains provisional because the entire 26-page manuscript of [1] could not be read at the consulted access points; the accessible abstract cannot rule out an unstated overlapping proposition.

## Limitations

This theorem is specific to complete multipartite graphs and ordinary distance-based packing colours \(1,2,\ldots\). It does not give formulas for arbitrary graph families or an arbitrary \(S\)-packing sequence. Non-surjective palettes and unordered witnessing partitions are part of the normalization; ordered partitions multiply \(W_{G,t,k}\) by \(k!\). The available primary-text comparison for [1] was abstract-level, not whole-document; priority is therefore provisional. Self-review is not independent mathematical audit.

## References

1. B. Brešar, J. Ferme, W. Hu, *Partitioning an \(S\)-packing coloring into broadcast dominating sets*, arXiv:2610.03477, first submitted 2026-10-02. https://arxiv.org/abs/2610.03477
2. J. Ferme, J. Hedžet, P. Melicharova, D. Mesarič Štesl, *On \(S\)-packing total colorings*, arXiv:2609.10107, 2026-09-09. https://arxiv.org/abs/2609.10107
3. S. Cambie, R. Hämäläinen, *Packing colourings in complete bipartite graphs and the inverse problem for correspondence packing*, arXiv:2303.01944, 2023-03. https://arxiv.org/abs/2303.01944
