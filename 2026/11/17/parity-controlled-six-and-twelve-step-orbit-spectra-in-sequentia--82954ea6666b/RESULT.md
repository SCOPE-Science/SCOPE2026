# Parity-controlled six- and twelve-step orbit spectra in sequential XOR friendship networks

## Finding
Let \(k\ge1\). The friendship graph \(\mathcal F_k\) comprises \(k\) edge-disjoint triangles sharing one hub \(h\), with each petal having distinct labelled vertices \(a_i,b_i\), \(1\le i\le k\). Give each vertex a binary state. During one sweep, update the hub and then \(a_1,b_1,a_2,b_2,\ldots,a_k,b_k\), each exactly once **in place**. At the instant of an update, replace the selected bit with its old value XOR all its neighbors' *currently held* bits. Repeat this same sweep indefinitely; call the induced map \(T_k\).

**The complete temporal census is determined only by the parity of the number of triangles.** All \(2^{2k+1}\) configurations are periodic from the start. For every positive integer \(t\), with \(g_k(t)=\dim_{\mathbb F_2}\ker(T_k^t-I)\),
\[
g_k(t)=\begin{cases}
1,&k\text{ even},\ 3\nmid t,\\
2k-1,&k\text{ even},\ 3\mid t,\ 2\nmid t,\\
2k+1,&k\text{ even},\ 6\mid t,\\
e(t)+2(k-1)\mathbf 1_{3\mid t},&k\text{ odd},
\end{cases}
\]
where \(e(t)=1\) when \(t\) is odd, \(e(t)=2\) when \(t\equiv2\pmod4\), and \(e(t)=3\) when \(4\mid t\). Consequently \(|\operatorname{Fix}(T_k^t)|=2^{g_k(t)}\).

The exact number \(P_d(k)\) of *states* of primitive temporal period \(d\) (not the number of cycles) is:

| Period \(d\) | Even \(k\ge2\) | Odd \(k\ge1\) |
|---|---:|---:|
| 1 | \(2\) | \(2\) |
| 2 | \(0\) | \(2\) |
| 3 | \(2^{2k-1}-2\) | \(2^{2k-1}-2\) |
| 4 | \(0\) | \(4\) |
| 6 | \(3\cdot2^{2k-1}\) | \(2^{2k-1}-2\) |
| 12 | \(0\) | \(2^{2k}-4\) |
| Other | \(0\) | \(0\) |

The number of temporal cycles of period \(d\) is \(P_d(k)/d\). For \(k=1\), the zero entries at periods 3, 6 and 12 leave periods \(\{1,2,4\}\). For even \(k\ge2\), the exact map order is six and the period set is \(\{1,3,6\}\). For odd \(k\ge3\), the exact order is twelve and every period in \(\{1,2,3,4,6,12\}\) occurs. Thus a single change in petal-count parity changes the longest clock. Exactly \(3/4\) of states have period six when \(k\) is even, while for odd \(k\to\infty\), the proportion with period twelve tends to \(1/2\).

## Assumptions and scope
The graph is simple, labelled, undirected, and has exactly \(2k+1\) vertices and \(3k\) edges. Binary arithmetic is in \(\mathbb F_2\). There are no self-loops: the selected vertex's own current value is retained in the XOR. Every local update is executed exactly once per sweep, and every sweep repeats the hub-first, paired-petal order above. The conclusions are about this specific deterministic sequential update convention, not synchronous XOR dynamics or arbitrary update orders.

## Proof
Write \(s_a=\sum_i a_i\), \(s_b=\sum_i b_i\) in \(\mathbb F_2\). Because the hub updates before every petal, the hub's post-sweep bit is \(h'=h+s_a+s_b\). Subsequent updates on each triangle give
\[
a_i'=a_i+b_i+h',\qquad b_i'=b_i+a_i'+h'=a_i.
\tag{1}
\]
Every individual local map is an involution (all its neighbors remain unchanged during that one update, so applying that update twice cancels the same XOR). Hence \(T_k\), a composition of invertible maps, is invertible. All states are therefore immediately periodic.

Put \(A=\begin{pmatrix}1&1\\1&0\end{pmatrix}\), so \(A^3=I\). Equation (1) says that each petal pair is transformed by \(A\) plus the *same* additive vector \((h',0)\).

**Odd petal count.** If \(k\) is odd, introduce the aggregate pair \((s_a,s_b)\) and deviations \(d_i=(a_i+s_a,b_i+s_b)\). They satisfy \(\sum_i d_i=0\), providing an invertible change of variables into a three-dimensional aggregate block and \(2(k-1)\) deviation coordinates. In these coordinates (1) gives
\[
(h,s_a,s_b)\longmapsto (h+s_a+s_b,\ h,\ s_a),\qquad d_i\longmapsto A d_i.
\tag{2}
\]
The aggregate block has matrix \(Q=\begin{pmatrix}1&1&1\\1&0&0\\0&1&0\end{pmatrix}\). Writing \(J=Q+I\), direct multiplication gives \(J^3=0\), \(J^2\ne0\), and hence one Jordan block of size three at eigenvalue one. The deviation space is a direct sum of \(k-1\) copies of the two-dimensional order-three \(A\)-module. Because \(A\) has irreducible minimal polynomial \(x^2+x+1\) over \(\mathbb F_2\), its fixed-space contribution to \(T_k^t\) is zero unless \(3\mid t\), in which case it is \(2(k-1)\). On the aggregate block, \(Q^t=(I+J)^t\) has fixed-space dimension one, two, or three according as \(t\) is odd, \(t\equiv2\pmod4\), or \(4\mid t\). This proves the odd formula for \(g_k(t)\).

**Even petal count.** Let \(K=\{h=s_a=s_b=0\}\). On the invariant space \(K\) equation (1) is just \(A\) on each petal, so \(T_k^3|_K=I\). The induced map on the three-dimensional quotient with coordinates \((h,s_a,s_b)\) is
\[
Q_0:(h,s_a,s_b)\longmapsto(h+s_a+s_b,\ s_a+s_b,\ s_a),
\]
which has \(Q_0^3=I\) and characteristic polynomial \((x+1)(x^2+x+1)\). Therefore \(N=T_k^3+I\) has image inside \(K\) and \(N^2=0\). Iterating (1) three times also shows that the difference between the resulting and original pair is *identical on every petal*; the hub difference is zero. Thus \(\operatorname{im}N\) lies in the two-dimensional constant-petal-pair subspace. Applying \(N\) to the state with \(a_1=1\) and every other bit zero produces the constant vector with all \(a_i=1\), all \(b_i=0\) and hub zero. As \(N\) commutes with \(T_k\), applying \(T_k\) to this image gives the independent constant vector with all \(a_i=b_i=1\) and hub zero (here \(k\) is even). Hence \(\operatorname{rank}N=2\), so \(\dim\ker(T_k^3-I)=2k-1\) and \(T_k^6=I\). The characteristic polynomial of \(T_k\), obtained from the invariant-space/quotient decomposition, is \((x+1)(x^2+x+1)^k\). Its only eigenvalue one is simple, so for \(3\nmid t\) the fixed space has dimension one. For odd multiples of three, \((I+N)^{t/3}=I+N\), giving dimension \(2k-1\); for multiples of six it is the entire space. This proves the even formula.

Finally, the primitive-period populations follow from \(|\operatorname{Fix}(T^t)|=\sum_{d\mid t}P_d\) by Möbius inversion. The displayed populations are nonnegative, sum to \(2^{2k+1}\), and establish occurrence and sharpness of the global periods, including the exceptional triangle \(k=1\). Their fractions give the asymptotics stated above.

## Verification
The included `checks/verify_state.py` applies the literal hub-first, petal-paired in-place updates to every binary state for \(1\le k\le7\), computes the least return time by direct iteration and compares every period population with the formula. That is \(43,688\) distinct initial states. The independently constructed binary matrix in `checks/verify_linear.py` checks the fixed-space dimensions at twelve exponents for each \(1\le k\le40\), including exact period identities. The stored outputs in `checks/state_output.txt` and `checks/matrix_output.txt` show successful replay. These experiments are supporting checks; the above argument proves all \(k\ge1\).

## Relationship to prior work
Wolfram's 1983 foundational article introduced and analyzed elementary cellular automata. Macauley, McCammond and Mortveit's 2007 preprint develops sequential updates, and their later open-access article studies the group of locally invertible Rule-150 maps on **cycle graphs**. Those papers establish the conceptual setting and invertibility but not the present period-six/period-twelve friendship-graph spectrum. In particular, the 2010 work analyzes a group generated by all cycle-vertex updates, not the iterates of this fixed hub-first scan on an intersecting-triangle graph. The complete published results *Scan-order phase diagram and exact Rule 150 cycle census on binary rings* and *A seven-element parity-switching semigroup on friendship graphs* were compared directly: the former solves fixed sweeps only on simple rings; the latter studies **synchronous** self-inclusive neighborhood-parity updates on friendship graphs (whose square is a rank-one map), unlike the invertible in-place sweep here. Defant (2015) likewise proves an exact census for identity scans restricted to simple cycle graphs.

## Limitations
The update order is fixed and deliberately specified; this does not classify arbitrary update permutations. The law does not address stochastic or synchronous dynamics. Finite computations alone do not establish the arbitrary-\(k\) statement; the proof uses an exact decomposition over \(\mathbb F_2\). The closest two published repository findings were inspected in full; unindexed or other earlier stronger literature remains a residual historical-priority risk. No independent external mathematical audit has been performed.

## References
1. S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics 55 (1983), 601–644, first published 1983-07-01. https://doi.org/10.1103/RevModPhys.55.601
2. M. Macauley, J. McCammond, H. S. Mortveit, *Order independence in asynchronous cellular automata*, first arXiv version 2007-07-16, https://arxiv.org/abs/0707.2360
3. M. Macauley, J. McCammond, H. S. Mortveit, *Dynamics groups of asynchronous cellular automata*, Journal of Algebraic Combinatorics 33 (2011), 11–35; first online 2010-05-08. https://doi.org/10.1007/s10801-010-0231-y
4. C. Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata*, arXiv:1511.06966, first posted 2015-11-22, especially Theorem 4.1 and Section 5. https://arxiv.org/abs/1511.06966
5. *Scan-order phase diagram and exact Rule 150 cycle census on binary rings*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-scan-order-phase-diagram-and-exact-rule-150-cycle-census-on-bina--a8edc73752da
6. *A seven-element parity-switching semigroup on friendship graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-seven-element-parity-switching-semigroup-on-friendship-graphs--eff3ebbe1409
