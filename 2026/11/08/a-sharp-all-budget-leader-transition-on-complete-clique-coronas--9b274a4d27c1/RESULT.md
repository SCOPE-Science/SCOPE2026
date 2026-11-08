# A sharp all-budget leader transition on complete-clique coronas

## Finding

Let \(n\ge2\) be an integer. Form \(H_n=K_n\circ K_1\) from a unit-edge clique with core vertices \(c_1,\ldots,c_n\) by attaching one private unit-edge pendant vertex \(p_i\) to each \(c_i\). For an integer \(1\le k\le2n\), choose exactly \(k\) noise-free leaders \(S\) and minimize the **unscaled** objective
\[
J_n(S)=\operatorname{tr}\bigl(L_{V(H_n)\setminus S,V(H_n)\setminus S}^{-1}\bigr),
\]
where \(L\) is the combinatorial Laplacian and the empty follower block has inverse trace zero.

Define the integer polynomial
\[
T_n(k)=nk^2+(2n^2+3n+2)k-2n(n+1)^2.
\]
The following list is an exhaustive characterization of **all** optimal leader sets (the positions selected in different clauses never have an unmentioned option).

1. For \(1\le k<n\) with \(T_n(k)<0\), choose exactly one **core** leader \(c_i\), plus \(k-1\) private leaves \(p_j\) with \(j\ne i\). There are \(n\binom{n-1}{k-1}\) optimal sets.
2. For \(1\le k<n\) with \(T_n(k)>0\), choose any \(k\) private leaves and no cores. There are \(\binom nk\) optimal sets.
3. For \(1\le k<n\) with \(T_n(k)=0\), both kinds in clauses 1 and 2, and only those, tie. Their counts add.
4. For \(n\le k\le2n\), choose all \(n\) leaves, together with any \(k-n\) cores. There are \(\binom n{k-n}\) optimal sets.

The first three cases give the exact minimum through the explicit rational expression \(F_{n,k}\):
\[
\begin{split}
q&=n-k,\qquad
h_{n,k}(\ell)=1-\frac{q}{n}-\frac{\ell}{n+1},\\
F_{n,k}(\ell)&=k-\ell+q+\frac{\ell}{n+1}+\frac{2q}{n}
+\frac{\ell/(n+1)^2+2q/n^2}{h_{n,k}(\ell)}.
\end{split}
\]
If \(T_n(k)<0\), \(J_{\min}=F_{n,k}(k-1)\); if \(T_n(k)>0\), \(J_{\min}=F_{n,k}(k)\); at equality the expressions coincide. For \(n\le k\le2n\), with \(r=2n-k\),
\[
J_{\min}=\frac{r(n+2-r)}{(n+1)(n+1-r)}.
\]
The unique positive real zero of \(T_n\) is \((\sqrt3-1)n+O(1)\) as \(n\to\infty\); hence the less-than-\(n\) leader allocation changes from one core to no core at a sharp budget near \(73.2\%\) of the number of core–leaf pairs. For instance, on \(H_{10}\), every optimal seven-leader set contains one core while every optimal eight-leader set contains no core. Optimal placements at successive budgets therefore need not form a nested chain.

## Assumptions and scope

All edges have conductance one, leaders are perfect fixed-state inputs, and every follower has equal unit-intensity state disturbance. The optimization is over subsets of **exactly** \(k\) vertices. The objective omits the conventional uniform factor \(1/2\) in steady-state variance; this factor does not alter its minimizers. There are no degree, diameter, or fixed-budget asymptotic approximations. The theorem applies for every integer \(n\ge2\) and every \(1\le k\le2n\). All comparisons are strict except the explicitly stated polynomial equality case.

## Proof

**1. An optimal set never contains a fully led pair and an untouched pair simultaneously.** Classify pair \(\{c_i,p_i\}\) as type \(B\) (both leaders), \(C\) (core alone a leader), \(P\) (pendant alone a leader), or \(U\) (neither a leader). Suppose a pair of type \(B\) and a pair of type \(U\) coexist. Move the selected pendant in the type-\(B\) pair to the pendant in the type-\(U\) pair, without moving the selected core. The first pendant becomes an isolated follower joined only to an already fixed leader, and contributes exactly one to the new inverse trace. In the original follower matrix \(Q\), the newly selected pendant was a follower with its own core also following. Removing this pendant strictly lowers the inverse trace by more than one: the diagonal entry of \(Q^{-1}\) at that pendant is \(1+R\), where \(R>0\) is the corresponding grounded-core diagonal inverse after elimination of the pendant. Furthermore, deleting a row and column of a positive-definite grounded Laplacian never increases the inverse trace of the remaining block, as is explicit from the block inverse formula. The move therefore strictly improves the objective. Thus no optimum has both a \(B\) pair and a \(U\) pair.

Writing \(B,C,P,U\) also for the counts, we have
\[
B+C+P+U=n,\qquad 2B+C+P=k,\qquad B-U=k-n.
\]
Consequently for \(k<n\) every optimum has \(B=0\), whereas for \(k\ge n\) every optimum has \(U=0\).

**2. Exact trace for every occupancy profile.** Let \(P\) and \(U\) denote the numbers of core followers with and without a selected private leaf. Eliminate the follower leaves by Schur complement. The remaining grounded core matrix is
\[
D-\mathbf1\mathbf1^{\mathsf T},\qquad
D=\operatorname{diag}\bigl(\underbrace{n+1,\ldots,n+1}_{P},\underbrace{n,\ldots,n}_{U}\bigr).
\]
If \(P+U>0\), its inverse follows from the Sherman–Morrison identity with
\[
h=1-\frac{P}{n+1}-\frac{U}{n}>0.
\]
Each type-\(C\) pair contributes an isolated follower leaf of variance one; each type-\(U\) pair contributes a leaf with inverse-trace contribution \(1\) in addition to an extra copy of the core diagonal. Therefore
\[
\boxed{\quad
J(B,C,P,U)=C+U+\frac{P}{n+1}+\frac{2U}{n}
+\frac{P/(n+1)^2+2U/n^2}{1-P/(n+1)-U/n}.
\quad}
\]
When \(P=U=0\), the objective is \(C\). The formula is exact for all leader sets, including \(P+U=0\), if the displayed fraction is interpreted as zero in that case (the denominator is then one).

**3. Budgets below \(n\).** By step 1, \(B=0\). Hence \(U=n-k=:q>0\), \(P=\ell\in\{0,\ldots,k\}\), and \(C=k-\ell\). Substitution in step 2 gives \(J=F_{n,k}(\ell)\). The denominator \(h_{n,k}(\ell)\) is positive throughout \(0\le\ell\le k\). Differentiation of this rational function in the real variable \(\ell\) gives
\[
F_{n,k}''(\ell)=\frac{2n[2n(n+1)-k(n+2)]}{[k(n+1)-n\ell]^3}>0
\qquad(1\le k<n).
\]
For \(2\le k<n\), exact subtraction yields
\[
F_{n,k}(k-1)-F_{n,k}(k-2)
=-\frac{nk^2+4n^2k+3nk+2k-4n^2-2n}{(k+n)(k+2n)(n+1)}<0.
\]
The numerator is positive already at \(k=2\), where it equals \(4n^2+8n+4\), and increases with \(k\). Convexity means every preceding consecutive difference is also negative. Thus for \(k\ge2\) the only possible minimizers are \(\ell=k-1\) and \(\ell=k\); the assertion is immediate for \(k=1\). Finally,
\[
F_{n,k}(k)-F_{n,k}(k-1)
=-\frac{T_n(k)}{k(k+n)(n+1)},
\]
which gives clauses 1–3 and proves that no other profile ties.

**4. Budgets at or above \(n\).** By step 1, \(U=0\), and thus \(B=k-n\) and \(C+P=r:=2n-k\), with \(0\le r\le n\). Write \(P=\ell\). Step 2 simplifies to
\[
H_r(\ell)=r-\ell+\frac{\ell}{n+1}+
\frac{\ell}{(n+1)(n+1-\ell)}.
\]
For integer \(0\le\ell<r\), the exact consecutive difference is
\[
H_r(\ell+1)-H_r(\ell)
=-\frac{n}{n+1}+\frac1{(n-\ell)(n+1-\ell)}<0
\]
because \(n\ge2\) and \(\ell\le n-1\). The unique optimal profile is \(P=r\), \(C=0\), which means that all leaves are leaders and exactly \(k-n\) cores are leaders. Inserting \(P=r\) gives the formula in the finding. The case \(k=2n\) has \(r=0\) and zero objective.

**5. Counts and threshold.** All \(n\) pairs are exchangeable. In clause 1 choose the sole core-leader pair in \(n\) ways and then \(k-1\) distinct other pairs in \(\binom{n-1}{k-1}\) ways; in clause 2 choose \(k\) leaf pairs in \(\binom nk\) ways. In clause 4 choose the \(k-n\) doubly led pairs. The positive root of \(T_n(k)\) is unique because its derivative is positive for nonnegative \(k\), and dividing the polynomial by \(n^3\) at \(k=\alpha n\) yields \(\alpha^2+2\alpha-2\), whose positive zero is \(\sqrt3-1\). This proves all assertions.

## Verification

The included `verify.py` constructs grounded Laplacians independently of the Schur formula and computes exact rational inverse traces using Gauss–Jordan elimination. It exhaustively checks every nonempty leader set for \(n=2,3,4,5\), verifying both the exact occupancy formula and all minimizing leader profiles/counts. Separately, it examines **every** occupancy profile for all budgets \(1\le k\le2n\) and all \(2\le n\le60\), comparing exact rational objectives with the theorem. A successful replay prints `PASS: 1356 exhaustive exact grounded-matrix calculations on n=2..5; 635312 exact occupancy comparisons on n=2..60.` These finite tests support but do not replace the proof for arbitrary \(n\).

## Relationship to prior work

Lin, Fardad, and Jovanović formulate and relax the general noise-free leader-selection inverse-trace optimization. Fitch and Leonard express the performance through joint centrality and give explicit results for paths and cycles. Patterson, McGlohon, and Dyagilev provide optimal leader-selection algorithms for weighted one-dimensional paths and rings. None of the specific evaluated results inspected in those primary texts supplies the complete-clique corona's all-budget allocation threshold, optimizer counts, or closed-form sharp core-abandonment polynomial. The new classification is compatible with, rather than contradictory to, their general formulations. A previously published general formula would cover this theorem if it could be specialized to the same four occupancy types and yield the same comparisons; no such decisive stronger coverage was found in the inspected material.

## Limitations

The proof concerns only the unweighted complete-clique, one-private-leaf corona and the unscaled grounded inverse-trace objective with uniform follower disturbances. It does not cover arbitrary core graphs, arbitrary pendant multiplicities, noise-corrupted leaders, or heterogeneous weights. Literature and database searches do not prove priority or independence. Some sources beyond the inspected accessible primary texts may contain equivalent specializations. No independent mathematical validation is claimed.

## References

- F. Lin, M. Fardad, and M. R. Jovanović, “Algorithms for Leader Selection in Stochastically Forced Consensus Networks,” first publicly posted 2013-02-03, https://arxiv.org/abs/1302.0450 (especially formulation of noise-free leader selection and Section IV).
- K. E. Fitch and N. E. Leonard, “Joint Centrality Distinguishes Optimal Leaders in Noisy Networks,” first publicly posted 2014-07-07, https://arxiv.org/abs/1407.1569 (especially Theorem 1 and special cases).
- S. Patterson, N. McGlohon, and K. Dyagilev, “Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations,” first publicly posted 2014-12-20, https://arxiv.org/abs/1412.6595 (path and cycle algorithms).
