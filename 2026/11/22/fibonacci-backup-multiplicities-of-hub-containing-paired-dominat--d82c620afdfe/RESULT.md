# Fibonacci backup multiplicities of hub-containing paired domination in wheels

## Finding

Let \(n\ge3\) and let \(W_{n+1}=K_1\vee C_n\) be the labelled wheel with a distinguished hub \(h\) and cyclically labelled rim vertices \(0,\ldots,n-1\). A subset \(S\) is paired-dominating if it dominates the wheel and the induced graph \(W_{n+1}[S]\) has a perfect matching. Put \(\mu(S)\) equal to the **number of distinct perfect matchings** of that induced graph, and write
\[
H_n(z,y)=\sum_{\substack{S\text{ paired-dominating}\\h\in S}}z^{|S|}y^{\mu(S)}.
\]
The exponent of \(y\) counts backup-pairing choices *per selected vertex set*, rather than treating each matching as another vertex set. Define the rational formal series
\[
A(x,z,y)=\frac{x^2zy}{(1-x)(1-x^2z^2y)},\qquad
E(x,z)=\frac{x^3z^2}{(1-x)(1-x^2z^2)}.
\]
Then for every \(n\ge3\), with coefficient extraction in \(x\),
\[
\boxed{H_n(z,y)=nz[x^n]\frac{A(x,z,y)}{1-E(x,z)}
+\mathbf1_{\{n\text{ odd}\}}z^{n+1}y^n.}
\]
This determines the *entire joint distribution* of the number of selected guards and the number of possible backup pairings for hub-containing configurations.

With \(F_0=0\), \(F_1=1\), \(F_{k+2}=F_{k+1}+F_k\), the following three exact identities hold:
\[
\boxed{\begin{aligned}
\#\{S\ni h:S\text{ paired-dominating}\}&=nF_{n-1}+\mathbf1_{\{n\text{ odd}\}},\\
\#\{S\ni h:S\text{ paired-dominating},\ \mu(S)=1\}&=nF_{n-2},\\
\sum_{S\ni h\text{ paired-dominating}}\mu(S)&=nF_n.
\end{aligned}}
\]
The middle line counts configurations that have a **unique possible pairing**; the bottom line counts configurations together with an explicitly chosen backup pairing. Thus the fraction of hub-containing paired-dominating configurations with unique pairing tends to \(\varphi^{-1}\), and their mean number of backup pairings tends to \(\varphi\), where \(\varphi=(1+\sqrt5)/2\).

For a proper, nonempty selected rim subset, exactly one selected cyclic run has odd length \(2a+1\); all other selected runs have even length, and the unique odd run gives exactly \(a+1\) perfect matchings of the induced wheel. The possible multiplicities among proper hub-containing configurations are exactly \(1,\ldots,\lfloor n/2\rfloor\). The exceptional full-rim selected configuration is paired-dominating with hub only for odd \(n\), where its multiplicity is \(n\).

## Assumptions and scope

The graph is simple and unweighted. Each wheel has \(n\) labelled rim vertices and one distinguished hub; configurations are counted as labelled vertex subsets, without quotienting by rotation. Every subset containing the hub automatically dominates the graph. The extra condition is the existence of a perfect matching on the *selected induced graph*. In the polynomial, \(z\) tracks the number of selected vertices, while the exponent of \(y\) is the integer number of induced perfect matchings. This is different from a matching-witness polynomial in which each matching contributes one monomial. The empty rim subset is excluded by parity: a singleton hub does not admit a perfect matching. No claim is made about hub-avoiding configurations, whose counting reduces to previously studied paired domination of cycles.

## Proof

**Structural matching lemma.** Let \(T=S\setminus\{h\}\) be a nonempty proper rim selection. The induced rim subgraph \(C_n[T]\) is a disjoint union of path components given by positive cyclic runs. In a perfect matching of \(W_{n+1}[S]\), the hub is paired to one vertex \(v\) of exactly one component; after deleting that vertex, every component must have a perfect matching. Paths have perfect matchings exactly at even orders. Therefore exactly one selected rim path has odd order \(2a+1\), and all others have even positive orders. In the odd path, the eligible hub partners are exactly its \(a+1\) odd-positioned vertices, because removing one leaves two even paths. Every remaining even path has a unique perfect matching, so \(\mu(S)=a+1\). Conversely these conditions construct all matchings. If all rim vertices are selected, removing any hub partner leaves a path of order \(n-1\), which is matchable precisely when \(n\) is odd; exactly \(n\) choices of partner then work.

**Complete joint generating function.** In a proper configuration there is one *distinguished* odd selected run, whose first vertex determines a unique cyclic starting point. An odd run of length \(2a+1\) followed by an omitted run of length \(b\ge1\) has weight \(x^{2a+1+b}z^{2a+1}y^{a+1}\). Summation over \(a\ge0\) and \(b\ge1\) yields \(A(x,z,y)\). Each subsequent even selected run of length \(2c\) with \(c\ge1\), followed by an omitted run of length \(b\ge1\), has weight \(x^{2c+b}z^{2c}\); summation yields \(E(x,z)\). There may be any number of such even runs, so their generating factor is \(1/(1-E)\). The first vertex of the unique odd run can be positioned at any of the \(n\) labelled rim vertices, with no rotational overcounting; the hub contributes another \(z\). Thus the proper configurations give \(nz[x^n]A/(1-E)\). The sole all-rim exception for odd \(n\) adds \(z^{n+1}y^n\). This proves the displayed complete polynomial.

**First Fibonacci count.** Specializing \(z=y=1\), simple cancellation gives
\[
\frac{A(x,1,1)}{1-E(x,1)}=\frac{x^2}{1-x-x^2}.
\]
The coefficient of \(x^n\) is \(F_{n-1}\). Adding the odd full-rim exception establishes \(nF_{n-1}+\mathbf1_{\{n\text{ odd}\}}\).

**Unique-pairing count.** In proper configurations \(\mu(S)=1\) exactly when \(a=0\), so the odd selected run is a singleton. Accordingly, replace \(A\) by \(A_1(x,z)=x^2z/(1-x)\). At \(z=1\),
\[
\frac{A_1(x,1)}{1-E(x,1)}
=\frac{x^2(1-x^2)}{1-x-x^2}.
\]
For every \(n\ge3\), its coefficient at \(x^n\) is \(F_{n-1}-F_{n-3}=F_{n-2}\). The odd all-rim exception has \(n\ge3\) matchings, not one, so it contributes none. This yields \(nF_{n-2}\).

**Matching-witness total.** Count pairs \((S,M)\) with \(h\in S\), \(S\) paired-dominating, and \(M\) a perfect matching of the selected induced graph. Choose the matching edge at \(h\) by first choosing its rim endpoint in \(n\) ways. Remove this endpoint. The remaining rim is a path on \(n-1\) vertices, and choosing \(S\setminus\{h,v\}\) together with a perfect matching of that induced path is equivalent to choosing an ordinary matching of the entire \((n-1)\)-vertex path: the chosen matching's endpoints are exactly the selected vertices. The number of ordinary matchings of an \((n-1)\)-vertex path is \(F_n\), by the usual first-vertex deletion recurrence with initial counts one and one. Conversely, the matching of the path and the chosen hub partner reconstruct \((S,M)\) uniquely. Since the hub dominates the whole wheel, no further constraint is required. This proves the exact total \(nF_n\) independently of coefficient extraction.

**Multiplicity support and limits.** In a proper hub-containing configuration with a unique selected odd run of length \(2a+1\), at least one rim vertex is omitted, giving \(2a+1\le n-1\) and \(1\le a+1\le\lfloor n/2\rfloor\). Every such value occurs by selecting exactly \(2a+1\) consecutive rim vertices, with the hub, leaving the rest omitted; the selected odd run has \(a+1\) matchings. For odd \(n\) the full rim provides the additional multiplicity \(n\), while for even \(n\) it is impossible. Finally, the Fibonacci ratio limit follows from the Binet formula or elementary recurrence, and the additive odd exception is negligible compared with \(nF_{n-1}\).

## Verification

Two standalone exact checkers are supplied. `verify_redundancy.py` directly constructs wheel adjacency lists, checks domination and computes the exact number of induced perfect matchings of *every* even-cardinality selected subset by memoized recursion, then compares every cardinality–multiplicity coefficient with the independent positive-composition enumeration of the displayed formula for rim orders 3 through 15. This validates the joint distribution, not only the three univariate totals. `verify_redundancy.cpp` separately constructs wheel adjacency bitsets and tabulates perfect matching counts by a subset dynamic program on all vertex masks, independently testing the three Fibonacci identities through rim order 16. Both were executed from their current source paths and passed; their actual output appears in `verification_output.txt`. These finite checks are additional evidence, while the all-order theorem is established by the bijective and generating-function proof.

## Relationship to prior work

Haynes and Slater introduced ordinary paired domination as a protection-and-backup pairing model in 1998. An earlier enumeration of all paired-dominating sets of *cycles* also supplies hub-avoiding wheel counts, which are excluded from the present claim: it says nothing about the number of perfect matchings in a hub-containing induced subgraph. Earlier published results on generalized windmill graphs classify the ordinary paired-domination polynomial for several disjoint clique blades, not wheels or pairing multiplicity. Closely related work counts matching witnesses for circular ladders and distributions of pairing multiplicities for subdivided cliques, so the distinction between distinct deployments and backup-pairing witnesses is established and relevant, but those graph families do not cover a wheel. Searches of wheel paired-domination polynomials, Fibonacci matching multiplicities and related indexed results found no exact covering theorem for the hub-conditioned bivariate multiplicity distribution, the three Fibonacci identities, or the pairing-uniqueness fraction. This does not establish absolute literature priority; particularly, a 2016 abstract on paired-domination polynomials of unspecified standard graph families lacks an accessible accompanying complete paper, leaving a residual possible-coverage risk. The directly relevant wheel sections (Sections 3.1 and 4.2) of Eakawinrujee’s 2023 dissertation were inspected and concern the minimum paired-domination number and its minimum-set exchange graph, rather than the backup multiplicity distribution.

## Limitations

This is an exact infinite-family enumeration of labelled hub-containing configurations only, not a statement about every paired-dominating set of the wheel. The variable \(y\) records each configuration's *number* of perfect matchings; derivatives or specialization can separately yield witness counts. The asymptotic ratio concerns uniform choice among hub-containing paired-dominating vertex subsets, not uniform choice among perfect matchings or minimum-cardinality configurations. The 2016 conference abstract does not identify its treated standard graph families, and an accessible full paper was not found; this remains an originality risk. The relevant wheel sections of the 2023 dissertation were read, but broader unindexed historical coverage is not established. No independent scholarly validation has been performed.

## References

1. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206, DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F. Publisher's first-online date: 1998-12-07.
2. S. Sh. Kahat, A. J. M. Khalaf, and R. Hasni, *Dominating Sets and Domination Polynomial of Wheels*, Asian Journal of Applied Sciences 2 (2014), 287–290, https://ajouronline.com/index.php/AJAS/article/view/1223/662 (ordinary domination rather than paired domination).
3. Puttaswamy, A. Alwardi, and S. R. Nayaka, *Introduction to Paired Domination Polynomial of a Graph*, 2016 conference abstract, https://publications.waset.org/abstracts/52964/introduction-to-paired-domination-polynomial-of-a-graph.
4. P. Eakawinrujee, *Total and Paired Domination Numbers and γ-Total and γ-Paired Dominating Graphs of Some Graphs*, 2023 dissertation, https://ethesisarchive.library.tu.ac.th/thesis/2023/TU_2023_6109320413_17206_27705.pdf.
5. *A rational paired-disjunctive domination census of cycles*, available full result (different domination predicate), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-rational-paired-disjunctive-domination-census-of-cycles--a8c84103b33c.
6. *Paired-domination polynomial of generalized windmill graphs*, available full result, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-paired-domination-polynomial-of-generalized-windmill-graphs--f2d90fcc066b.
