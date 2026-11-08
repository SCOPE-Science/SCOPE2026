# Fifth-round extinction and a complete temporal census for one-edge-defective bipartite excitation

## Finding

For every pair of integers \(m,n\ge2\), let \(G_{m,n}\) be the labelled complete bipartite graph \(K_{m,n}\) with one specified cross-edge deleted. Under synchronous three-state Greenberg–Hastings excitation (resting color \(0\), excited color \(1\), refractory color \(2\)), all initial colorings first enter an eventual orbit after at most five updates. The only eventual least periods are \(1,3,4\). In particular the exact global map identity is

\[F^{17}=F^5.\]

The maximum first-entry time is exactly five for **every** \(m,n\ge2\); all configurations attaining it eventually reach the unique all-rest fixed point, and their number is

\[\boxed{N_{5,1}(m,n)=2^m+2^n+2.}\]

The theorem further provides the complete exact fifteen-class joint census of first-entry time and eventual least period, expressed below by fixed three-by-three integer matrices. In contrast, the same three-state rule on the intact \(K_{m,n}\) has a sharp maximum first-entry time of four, for all \(m,n\ge2\); thus deleting just one edge creates an additional, explicitly counted extinction layer.

## Assumptions and scope

All graphs are finite, simple and labelled; the two bipartition shores have \(m\) and \(n\) vertices, with \(m,n\ge2\). The sole missing edge joins distinguished vertices \(a\) and \(b\). At each simultaneous step, each vertex in color \(1\) changes to \(2\), and each vertex in color \(2\) changes to \(0\), unconditionally. A vertex in color \(0\) changes to \(1\) precisely when at least one neighbor currently has color \(1\), otherwise remaining in \(0\). No probabilistic updates are used.

Let \(T(x)=\min\{t\ge0:F^t(x)\text{ is periodic}\}\), and let \(p(x)\) be the least period of that eventual orbit. Denote by \(N_{t,p}(m,n)\) the number of labelled initial colorings with \(T=t\) and \(p(x)=p\). A primitive temporal orbit is counted once, not once per phase.

For integers \(r\ge1\) and \(j\in\{1,2,3\}\), define the positive-support surjection count

\[s_j(r)=\sum_{h=0}^j(-1)^{j-h}\binom jh h^r,\quad s_1(r)=1,\quad s_2(r)=2^r-2,\quad s_3(r)=3^r-3\cdot2^r+3.\]

For \((t,p)\) in the following table, write \(C_{t,p}[j,k]\) for the entry in row \(j\), column \(k\), and put all unlisted \(C_{t,p}\) equal to the zero matrix. The complete exact formula is

\[\boxed{N_{t,p}(m,n)=\sum_{j=1}^3\sum_{k=1}^3 C_{t,p}[j,k]\,s_j(m-1)\,s_k(n-1).}\]

| First entry and period | Coefficient matrix |
|:--|:--|
| \(0,1\) | \(\begin{pmatrix}1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix}\) |
| \(0,3\) | \(\begin{pmatrix}0 & 0 & 0 \\ 0 & 3 & 6 \\ 0 & 6 & 9\end{pmatrix}\) |
| \(0,4\) | \(\begin{pmatrix}0 & 4 & 0 \\ 4 & 8 & 0 \\ 0 & 0 & 0\end{pmatrix}\) |
| \(1,1\) | \(\begin{pmatrix}15 & 8 & 0 \\ 8 & 4 & 0 \\ 0 & 0 & 0\end{pmatrix}\) |
| \(1,3\) | \(\begin{pmatrix}0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}\) |
| \(1,4\) | \(\begin{pmatrix}0 & 8 & 3 \\ 8 & 20 & 6 \\ 3 & 6 & 0\end{pmatrix}\) |
| \(2,1\) | \(\begin{pmatrix}25 & 15 & 3 \\ 15 & 4 & 0 \\ 3 & 0 & 0\end{pmatrix}\) |
| \(2,3\) | \(\begin{pmatrix}0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}\) |
| \(2,4\) | \(\begin{pmatrix}0 & 13 & 6 \\ 13 & 22 & 6 \\ 6 & 6 & 0\end{pmatrix}\) |
| \(3,1\) | \(\begin{pmatrix}18 & 12 & 3 \\ 12 & 4 & 0 \\ 3 & 0 & 0\end{pmatrix}\) |
| \(3,3\) | \(\begin{pmatrix}0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}\) |
| \(3,4\) | \(\begin{pmatrix}0 & 7 & 7 \\ 7 & 12 & 6 \\ 7 & 6 & 0\end{pmatrix}\) |
| \(4,1\) | \(\begin{pmatrix}12 & 8 & 3 \\ 8 & 0 & 0 \\ 3 & 0 & 0\end{pmatrix}\) |
| \(4,4\) | \(\begin{pmatrix}0 & 4 & 2 \\ 4 & 4 & 0 \\ 2 & 0 & 0\end{pmatrix}\) |
| \(5,1\) | \(\begin{pmatrix}10 & 2 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix}\) |

In particular, the unique fixed configuration is the all-rest coloring. Writing \(A=s_2(m-1)\), \(B=s_2(n-1)\), \(U=s_3(m-1)\), and \(V=s_3(n-1)\), the numbers of primitive three- and four-cycle orbits are respectively

\[Q_3=AB+2AV+2UB+3UV,\qquad Q_4=A+B+2AB.\]

The number entering the fixed point only at update five is the displayed \(2^m+2^n+2\), from the final matrix \(C_{5,1}\). For independent uniformly random initial colors, its probability is exactly \((2^m+2^n+2)/3^{m+n}\), whereas the probability of being already on a primitive period-three orbit tends to one when \(\min(m,n)\to\infty\).

## Proof

**Exact uniform reduction.** The \(m-1\) ordinary left vertices have identical neighborhoods (the entire right shore), and similarly for the \(n-1\) ordinary right vertices. Two ordinary vertices on the same shore having the same color now have identical next color and continue together forever. Thus one can track only the distinguished colors \(a,b\in\{0,1,2\}\) and the nonempty sets \(S,T\subseteq\{0,1,2\}\) of currently present colors on the two ordinary shores. There are exactly \(3^2(2^3-1)^2=441\) possible signatures.

Let \(u(c,e)=(c+1)\bmod3\) for \(c=1,2\), and \(u(0,e)=e\) for \(e\in\{0,1\}\). Write \(\chi_S=\mathbf1_{\{1\}\subseteq S}\) and \(\chi_T=\mathbf1_{\{1\}\subseteq T}\). Then the signature update is the explicit map

\[(a,b,S,T)\mapsto\left(u(a,\chi_T),\ u(b,\chi_S),\ \{u(c,\max\{\chi_T,\mathbf1_{b=1}\}):c\in S\},\ \{u(c,\max\{\chi_S,\mathbf1_{a=1}\}):c\in T\}\right).\]

Every possible labelled update projects exactly to this formula. Repeatedly applying this finite map to all 441 signatures gives the fifteen joint \((T,p)\) classes and the coefficient matrices displayed above. This finite exhaustive statement is not an extrapolation over graph sizes: it covers the entire quotient at once. The standalone `quotient_checker.py` implements precisely the displayed update, enumerates all 441 signatures, and verifies every entry of all fifteen matrices against independent literal values.

**Lifting the quotient to labelled trajectories.** A support-set orbit need not, in general, have the same period as its labelled lift. The certificate explicitly checks the missing condition: each of the 41 periodic signatures carries every initially present ordinary color through one quotient period back to **itself**, not merely back to the same support set. Hence each labelled configuration lying above a periodic signature is periodic at the same time with the same least period (the distinguished colors and supports also force the converse). Conversely, periodic labelled configurations must project to periodic signatures. Therefore the first-entry times and periods computed from the signatures are exactly those for the original labelled dynamics, for arbitrary shore sizes.

**Exact multiplicities.** Given a fixed ordinary-shore support of \(j\) colors, the number of length-\(m-1\) labelled words using exactly those \(j\) colors is \(s_j(m-1)\), by inclusion–exclusion; similarly the right support has \(s_k(n-1)\) realizations. Summing the weights of all signatures in each verified class yields the matrix formula. The fifth-entry class has only \(C_{5,1}[1,1]=10\) and \(C_{5,1}[1,2]=C_{5,1}[2,1]=2\), giving

\[N_{5,1}=10+2(2^{m-1}-2)+2(2^{n-1}-2)=2^m+2^n+2>0.\]

The 41 periodic signatures have least periods in \(\{1,3,4\}\); their phase counts yield the formulas for \(Q_3\) and \(Q_4\). Because every state becomes periodic by update five and every eventual period divides twelve, \(F^{17}=F^5\). For the intact complete bipartite graph the analogous (unbroken) support reduction has 49 signatures and a maximum first-entry time four; in every periodic signature its support-color maps are bijective, so first entry lifts unchanged. The bound four is attained by a support pattern with one shore all resting and the other containing both resting and excited vertices. This establishes the one-edge sharp contrast.

## Verification

`quotient_checker.py` exhausts all 441 exact signatures, checks the 41 periodic-signature color returns, the 15 numerical coefficient matrices, the sharp fifth-entry class, and sums all classes to \(3^{m+n}\) for 196 pairs with \(2\le m,n\le15\). The same checker verifies the intact 49-state support reduction's sharp first-entry time four.

Independently, `labelled_checker.cpp` directly implements individual vertex updates without using the support dynamics; its compiled run exhausts 1,185,921 labelled configurations across 25 pairs with \(2\le m,n\le6\), comparing every first-entry class against the matrix formula. The captured standard outputs are `quotient_output.txt` and `labelled_output.txt`. Both checks passed. The infinite-family proof rests on the exact 441-state quotient and lifting argument, not on the finite-size direct simulation.

To replay: run `python3 quotient_checker.py`; compile with `c++ -O2 -std=c++17 labelled_checker.cpp -o labelled_checker` and run `./labelled_checker`. No third-party packages are required.

## Relationship to prior work

The three-state Greenberg–Hastings rule was introduced by Greenberg and Hastings (1978). Gravner, Lyu and Sivakoff (arXiv:1610.07320v1, October 24, 2016) give a general excitation/winding characterization and a diameter bound for synchronizing initial configurations on finite graphs. In particular, their general theorem predicts which initial configurations eventually synchronize, but does not provide the above complete finite-time \((T,p)\) census, the primitive period-four count, or the one-edge sharp five-update tail.

The same undamaged biclique and single-edge-defective biclique have been studied for related **different** three-color contact-update rules. Rule equivalence cannot be inferred from their shared color set: refractory \(1\to2\to0\) is unconditional here, unlike the three-color cyclic contact rule. The present census is restricted to the three-state Greenberg–Hastings rule on one-edge-defective complete bipartite graphs.

## Limitations

This is a deterministic, finite-graph theorem, not an assertion about stochastic excitation, higher state counts, alternative excitation thresholds, or general edge-deleted bipartite graphs. The graph-size-independent quotient is exact, but the independent labelled enumeration is finite (through shore size six). Full historical priority against unindexed publications is not certified; an older equivalent treatment may exist. The foundational 1978 source was available here at abstract level, not as a fully inspected manuscript.

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523, DOI: 10.1137/0134040.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, publicly posted 2016-10-24. See especially the model definitions in Section 1 and Theorem 3 in Section 2.
