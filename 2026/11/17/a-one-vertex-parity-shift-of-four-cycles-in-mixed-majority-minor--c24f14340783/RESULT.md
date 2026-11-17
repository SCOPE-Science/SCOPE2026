# A one-vertex parity shift of four-cycles in mixed majority–minority clique dynamics

## Finding
Let \(m,k\ge1\) and \(N=m+k\ge3\). Consider synchronous binary dynamics on the loopless complete graph \(K_N\): its \(m\) conformists adopt the strict majority bit among their neighbors, its \(k\) contrarians adopt the strict minority bit, and every vertex retains its old bit if neighboring zeros and ones tie. Write \(H\) for the number of fixed labelled configurations, \(C_2\) for primitive temporal two-orbits and \(C_4\) for primitive temporal four-orbits. Let \(E_j\) count initial labelled configurations whose *least* first-periodic-entry time is \(j\).

**Even order.** If \(N=2q\), set \(B=\binom{m}{m/2}\binom{k}{k/2}\) when both \(m,k\) are even, and \(B=0\) otherwise. Then
\[
H=2\mathbf1_{m>k},\qquad C_2=\tfrac12 B+\mathbf1_{m<k},\qquad C_4=\mathbf1_{m=k},
\]
\[
E_0=2+B+2\mathbf1_{m=k},\quad E_1=2^N-\binom Nq-2,\quad E_2=\binom Nq-B-2\mathbf1_{m=k}.
\]

**Odd order.** If \(N=2q+1\), the complete orbit census is
\[
(H,C_2,C_4)=\begin{cases}
(2,0,0),&k\le q,\\
(2\binom{k}{q},0,1),&k=q+1,\\
(2\binom{k}{q},1,0),&k\ge q+2.
\end{cases}
\]
Set \(E_0=H+2C_2+4C_4\), and
\[
E_2=\begin{cases}
2\binom Nq-2\binom m{q-k},&k\le q,\\
2\binom Nq-2\binom kq-2,&k=q+1,\\
2\binom Nq-2\binom kq,&k\ge q+2,
\end{cases}\qquad E_1=2^N-E_0-E_2.
\]

For every parameter choice all other orbit lengths and all entry times above two are absent; equivalently \(F^6=F^2\). Entry time two occurs for every \(N\ge5\). Its only exceptions for \(N\ge3\) are \((m,k)=(1,2)\) and \((2,2)\). A primitive four-cycle exists **if and only if** the populations are equal when \(N\) is even, or the contrarians exceed the conformists by exactly one when \(N\) is odd. For odd \(N\) with \(k\ge q+1\), all \(2\binom{k}{q}\) fixed configurations have no predecessor other than themselves: they are isolated equilibrium basins.

## Assumptions and scope
The vertices are labelled and partitioned into a fixed conformist group of size \(m\) and a fixed contrarian group of size \(k\). Neighborhoods exclude the vertex itself. Each update uses all neighbors simultaneously. A tied voter keeps its current bit, regardless of voter type. No noise, randomness, loops, or asynchronous updates are involved. Counts do not identify spatial permutations; temporal rotations of the states of a periodic orbit identify that orbit. The first-periodic-entry time \(T(x)\) is the smallest nonnegative integer \(j\) for which \(F^j(x)\) lies on a temporal cycle. In the formulas, both binomial arguments are nonnegative whenever used, and indicators have value zero or one according to the displayed relation.

## Proof
Write the state as \((X,Y)\), a conformist binary word \(X\) of length \(m\) and a contrarian binary word \(Y\) of length \(k\). Set \(a=|X|\), \(b=|Y|\), \(t=a+b\). Any vertex presently holding bit \(x\) sees precisely \(t-x\) neighboring ones. Thus evaluating majority and minority separately for the current-bit cases \(x=0,1\) gives the following *exact* update identities.

For \(N=2q\), degrees are odd and there are no ties:
\[
F(X,Y)=\begin{cases}
(\mathbf0_m,\mathbf1_k)=A,&t<q,\\
(\overline X,Y),&t=q,\\
(\mathbf1_m,\mathbf0_k)=B_*,&t>q.
\end{cases} \tag{1}
\]
Here \(\mathbf0_j,\mathbf1_j\) are length-\(j\) constant words, and \(\overline X\) complements each bit. The totals at \(A,B_*\) are \(k,m\). If \(m>k\), these two states are fixed; if \(m<k\), they interchange in one primitive two-cycle. When \(m=k=q\), the four distinct states follow
\[
A\longrightarrow(\mathbf1_m,\mathbf1_k)\longrightarrow B_*\longrightarrow(\mathbf0_m,\mathbf0_k)\longrightarrow A.
\]
Any state in the central layer \(t=q\) maps to a state with \(m+q-2a\) ones. This is still central precisely when \(a=m/2\), equivalently \(b=k/2\). Such balanced states alternate under complementing \(X\) and cannot be fixed because \(m\ge1\). Their number is \(B\), giving \(B/2\) primitive two-cycles. Every other central state maps outside the layer and therefore to a macro orbit by the following update. The two macro states \(A,B_*\) themselves belong to the central layer exactly when \(m=k\). Consequently the central layer consists of \(B\) two-periodic states, another two periodic states if \(m=k\), and \(\binom Nq-B-2\mathbf1_{m=k}\) states with entry time two. Outside the central layer exactly two macro states are already periodic; all remaining states have entry time one. This yields the even-order formulas.

For \(N=2q+1\), the degree is \(2q\) and retaining old opinions on ties matters. A conformist maps to zero for \(t\le q\) and to one for \(t\ge q+1\). Contrarians map to one for \(t<q\), retain their bits for \(q\le t\le q+1\), and map to zero for \(t>q+1\). Hence
\[
F(X,Y)=\begin{cases}
A=(\mathbf0_m,\mathbf1_k),&t<q,\\
(\mathbf0_m,Y),&t=q,\\
(\mathbf1_m,Y),&t=q+1,\\
B_*=(\mathbf1_m,\mathbf0_k),&t>q+1.
\end{cases} \tag{2}
\]
If \(k\le q\), then \(A\) and \(B_*\) are fixed. If \(k=q+1\), then \(m=q\), and the same four distinct macro configurations form \(A\to(\mathbf1_m,\mathbf1_k)\to B_*\to(\mathbf0_m,\mathbf0_k)\to A\). If \(k\ge q+2\), then \(A\) and \(B_*\) interchange. For the two central layers, \(t=q\) has a fixed state exactly when \(X=\mathbf0_m\) and \(|Y|=q\), and \(t=q+1\) has a fixed state exactly when \(X=\mathbf1_m\) and \(|Y|=k-q\). These states exist if and only if \(k\ge q+1\) and total \(2\binom{k}{q}\). For a state with \(t=q\), the successor's total is \(b\): if \(b<q\), it next maps to \(A\); if \(b=q\), it is already fixed. For \(t=q+1\), the successor's total is \(m+b\): if \(a<m\), it next maps to \(B_*\); if \(a=m\), it is fixed. Thus there are no other recurrent states or entry times beyond two.

There are \(2\binom Nq\) states in the two central layers. For \(k\le q\), precisely \(\binom m{q-k}\) configurations in the \(t=q\) layer map immediately to \(A\), because their \(Y\) block is full of ones, and precisely the same number in the \(t=q+1\) layer map immediately to \(B_*\), because their \(Y\) block is all zero. All other central states have entry time two. For \(k\ge q+1\), subtract the \(2\binom kq\) fixed central states. At the boundary \(k=q+1\), subtract additionally the two macro states \(A,B_*\) which already belong to the four-cycle and central layers. This proves all odd-order counts and the global iterate identity.

The sharpness assertions follow from the explicit nonnegative expressions for \(E_2\), or by choosing a central state which is neither recurrent nor sent directly to \(A\) or \(B_*\): all splits with \(N\ge5\) allow one, while the only zero cases for \(N\ge3\) are \((m,k)=(1,2)\) and \((2,2)\). Finally, for \(k\ge q+1\), consider a fixed configuration \((\mathbf0_m,Y)\) with \(|Y|=q\). An off-central state cannot map to it (the macro outputs have an all-zero or all-one contrarian block), and the \(t=q+1\) branch of (2) has conformist block all ones. Any predecessor is therefore in the \(t=q\) branch, forcing its conformist block to be zero and its contrarian block to equal \(Y\), namely the fixed state itself. The second fixed family is symmetric. This establishes isolation.

## Verification
The standalone `verify.py` applies the update independently, vertex by vertex, by counting the actual opinions of all other vertices. It then traverses each complete labelled functional graph without using (1) or (2), extracts orbit lengths and minimal entry times, and compares them with every displayed formula for all 104 nonempty type splits of graph orders \(3\le N\le15\). The complete captured output is in `verification_output.txt`. These finite tests are regression checks, not the justification for the infinite-parameter theorem. No experiment asserts anything about an untested graph size.

## Relationship to prior work
Cannings (2009) studied mixed conformist/contrarian updating on complete and other graphs; the published abstract covers period and equilibrium questions but the complete paper was not available for full comparison. Haslegrave and Cannings (2016, Introduction) explicitly attribute to Cannings the possible periods one, two and four on complete graphs and the equal-type-count condition for a four-cycle in the strict, no-tie regime. The current theorem does not claim those previously known facts as new; it gives an exact all-size orbit and first-entry census for both parities **under explicit tie retention**, including the odd-order four-cycle at a one-voter contrarian excess, an exponentially large fixed family and its isolated basins. The accessible complete-graph equal-population census already established for even order gives the \(m=k\) specialization of the even-order formulas here; it does not imply unbalanced or odd-order counts, and its stated limitations exclude them. Cao and Yang (2014, Theorem 5) prove the exact **existence criterion** for pure fixed points on this very complete-graph conformist/rebel game: they exist when conformists outnumber contrarians, or when the order is odd; this existence result is explicitly prior and not claimed novel here. The present theorem adds the exact fixed-state multiplicities, isolated-predecessor structure, complete temporal-orbit census and first-entry times. Cao, Qin, Yang and Zhang (2013) study the same conformist/rebel best-response tie convention on networks, focusing on lines, rings and stars rather than a full complete-graph orbit census. The overlap risk from the inaccessible full Cannings work remains material.

## Limitations
All formulas concern synchronous binary update on one complete simple graph with both behavioral types present, and keeping the previous opinion on exact ties. Altering tie breaking, including the updating vertex among its neighbors, or allowing asynchronous updates changes the map. We do not claim a new universal period restriction (already known in related complete-graph settings) or independent validation. Cannings (2009) studies exactly the broad object class, and because its complete original text was inaccessible, historical duplication of some formulas cannot be excluded. The result is therefore a self-review subject to independent literature priority checking.

## References
1. C. Cannings, *The majority and minority models on regular and random graphs*, GameNets (2009), DOI: 10.1109/GAMENETS.2009.5137464. Public bibliographic record, dated 2009-06-26: https://eudl.eu/doi/10.1109/gamenets.2009.5137464.
2. J. Haslegrave and C. Cannings, *Majority dynamics with one nonconformist*, arXiv:1606.05496 (first posted 2016-06-17), https://arxiv.org/abs/1606.05496.
3. Z.-G. Cao, C.-Z. Qin, X.-G. Yang and B.-Y. Zhang, *A Heterogeneous Network Game Perspective of Fashion Cycle*, working paper dated 2013-05-03, https://studylib.net/doc/8848534/a-heterogeneous-network-game-perspective-of-fashion-cycle-%E2%88%97.
4. Z. Cao and X. Yang, *The fashion game: Network extension of Matching Pennies*, *Theoretical Computer Science* 540–541 (2014), 169–181, DOI: 10.1016/j.tcs.2014.05.009, especially Section 4.3 and Theorem 5. Open full text: https://ml2.inf.ethz.ch/courses/tcsod/TCS-Seminar-papers/The%20fashion%20game%3A%20Network%20extension%20of%20Matching%20Pennies.pdf.
5. *Exact oscillatory basins for a balanced complete-graph majority–minority system*, public mathematical research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-exact-oscillatory-basins-for-a-balanced-complete-graph-majority--6d2b4fc7152d/RESULT.md.
