# A root-drift correction to pendant-path diffusion recurrences

## Finding

**Theorem.** Let \(H\) be any finite connected simple graph with a distinguished vertex \(r\). For an integer \(k\ge2\), let \(G_k\) be formed by joining \(r\) by a bridge to the first vertex of a new labelled path with \(k\) vertices. Under synchronous integer diffusion, count states modulo simultaneous addition of an integer to every vertex label. Let \(T_k(H,r)\) be the number of states already in a *primitive two-cycle* (both temporal phases counted separately). Define
\[
Z(H,r)=\#\{x\in\mathbb Z^{V(H)}/\mathbb Z\mathbf1:F_H^2(x)=x,\ (F_Hx)_r=x_r\}.
\]
Then, for **every** \(k\ge2\),
\[
\boxed{T_{k+4}-3T_{k+3}-2T_{k+2}-T_{k+1}+T_k=-4(Z(H,r)-1).}\tag{1}
\]
Thus the proposed homogeneous fourth-order path-tail recurrence holds on this rooted graph family **if and only if** \(Z(H,r)=1\). Every such sequence satisfies the universal homogeneous fifth-order recurrence
\[
\boxed{T_{k+5}-4T_{k+4}+T_{k+3}+T_{k+2}+2T_{k+1}-T_k=0.}\tag{2}
\]
For the rooted triangle \(H=K_3\), \(Z(K_3,r)=3\), so the right-hand side of (1) is \(-8\). In this case
\[
(T_2,T_3,T_4,T_5,T_6,T_7)=(122,468,1674,6028,21770,78564).
\]
The residual \(T_7-3T_6-2T_5-T_4+T_3=-8\) is an explicit counterexample to the unrestricted pendant-path recurrence conjectured in Mullen–Nowakowski–Cox (2020). This is a counterexample to a **conjectural extension**, not to their proved recurrence for paths.

## Assumptions and scope

All graphs are finite, connected, simple, undirected and have fixed vertex labels. A configuration is a vector \(x\in\mathbb Z^{V(G)}\), with update
\[
(F_Gx)_v=x_v-\sum_{w\sim v}\operatorname{sgn}(x_v-x_w),\qquad \operatorname{sgn}(0)=0.
\]
Two configurations are identified only if they differ by a constant integer vector; no graph automorphisms or temporal phase identifications are imposed. The root of \(H\) is normalized to value zero. The new path is \(r,v_1,\ldots,v_k\); its vertices are distinct from those of \(H\). Since \(H\) is connected, every fixed state modulo translation is constant, and a two-periodic state is either fixed or has primitive period two. The first public primary-source date for this diffusion model is 19 September 2016; the path-tail conjecture itself was stated in 2020.

## Proof

**1. Edge reversal is equivalent to initial two-periodicity.** Put \(b_G(x)_v=\sum_{w\sim v}\operatorname{sgn}(x_v-x_w)\), so \(F_Gx=x-b_G(x)\). Suppose \(F_G^2x=x\) and write \(y=F_Gx\). Then \(b_G(x)+b_G(y)=0\). Multiply this vector equation by \(x+y\), sum over vertices, and regroup edges to obtain
\[
0=\sum_{uv\in E(G)}[(x_u-x_v)+(y_u-y_v)]\,[\operatorname{sgn}(x_u-x_v)+\operatorname{sgn}(y_u-y_v)].
\]
Every summand is nonnegative, and it vanishes exactly when the two signs are opposite or both zero. Therefore each edge reverses its strict comparison in one step, or is flat in both steps. Conversely these edgewise conditions give \(b_G(y)=-b_G(x)\), hence \(F_Gy=y-b_G(y)=x\). In particular, on any nonflat edge \(uv\), the integer initial gap has absolute value at most \(\deg(u)+\deg(v)-1\), because it must cross zero after changes bounded by the two endpoint degrees. A connected graph therefore has finitely many initially two-periodic states modulo translation.

**2. Universal local tail weight.** Set \(s_i=\operatorname{sgn}(x_{v_i}-x_{v_{i-1}})\in\{-1,0,1\}\) for \(1\le i\le k\), with \(v_0=r\) and the fictitious terminal sign \(s_{k+1}=0\). For interior or terminal tail vertices, \(b_G(x)_{v_i}=s_i-s_{i+1}\). For \(2\le i\le k\), the number of integer choices of the difference \(x_{v_i}-x_{v_{i-1}}\) realizing reversal on the corresponding edge, given \((s_{i-1},s_i,s_{i+1})=(a,b,c)\), is
\[
m(a,b,c)=\begin{cases}
\mathbf1_{\{a=-c\}},&b=0,\\
\max\{1-b(a+c),0\},&b=\pm1.
\end{cases}\tag{3}
\]
The same formula counts choices on the first bridge if \(a\) is replaced by \(b_H(x)_r\), since the root's full outflow is \(b_H(x)_r-s_1\). All these gap choices are independent along the appended path because it has no cycles.

**3. Boundary contraction and its exceptional eigenline.** Index a nine-state matrix by pairs \((a,b)\in\{-1,0,1\}^2\):
\[
M_{(a,b),(u,c)}=\mathbf1_{\{u=b\}}m(a,b,c),\qquad \beta_{(a,b)}=m(a,b,0).
\]
For each \(s_1\), enumerate normalized assignments on \(H\) whose core-edge comparisons reverse when the root additionally has tail sign \(s_1\). These form a finite set by the edge-gap bound above. Define the row vector \(\alpha\) by summing \(m(b_H(x)_r,s_1,s_2)\) over these core assignments for every pair \((s_1,s_2)\). It follows **exactly**, for every \(k\ge2\), that the total number of initially two-periodic translation classes is
\[
N_k=\alpha M^{k-2}\beta,\qquad T_k=N_k-1.\tag{4}
\]
Negating every core label and every tail edge sign leaves all counts unchanged; thus \(\alpha\) and \(\beta\) are invariant under \((a,b)\mapsto(-a,-b)\). On this invariant five-dimensional subspace, a basis formed by the four pairs of opposite nonzero sign states and the all-zero state gives
\[
M_{\rm even}=\begin{pmatrix}
0&0&1&0&0\\
0&0&0&1&0\\
1&2&3&0&0\\
0&1&2&0&0\\
0&0&0&0&1
\end{pmatrix}
=\operatorname{diag}(B,1).
\]
Direct multiplication gives \(B^4-3B^3-2B^2-B+I=0\). The isolated all-flat line is reached only by configurations whose entire appended path is flat at both times. They are in bijection with core two-periodic configurations for which the root has **zero one-step displacement**: there are exactly \(Z(H,r)\) of them. Therefore \(N_k=Z(H,r)+u_k\), where \(u_k\) satisfies the homogeneous quartic recurrence with characteristic polynomial \(\lambda^4-3\lambda^3-2\lambda^2-\lambda+1\). Since \(T_k=(Z-1)+u_k\) and this polynomial evaluates to \(-4\) at \(\lambda=1\), equation (1) follows. Multiplying by \(\lambda-1\) proves (2). The equivalence with \(Z=1\) follows because \(-4(Z-1)=0\) precisely then.

**4. Explicit rooted-triangle obstruction.** Normalize the root label to zero and write the other two core labels as \((a,b)\). Their possible absolute values do not exceed four in any periodic state after the bridge is attached. Exhaustively applying the core-edge reversal inequalities for bridge sign \(s_1\) yields the exact boundary row, arranged with \(s_1,s_2\in\{-1,0,1\}\):
\[
\alpha=\begin{pmatrix}14&21&28\\4&3&4\\28&21&14\end{pmatrix}.
\]
This finite table is independently reconstructible from the explicit integer inequalities in `code/check_transfer.py`. The core states with zero root displacement are exactly \((a,b)=(-1,1),(0,0),(1,-1)\), proving \(Z=3\). Substitution in (4) gives the six asserted values. In particular the displayed recurrence residual equals \(-8\), and its nonzero value persists for all \(k\ge2\).

## Verification

Run `python3 code/check_transfer.py` to rebuild the nine-state matrix, core boundary table, even-block matrix identity, counts through \(k=12\), and recurrence residuals; compare with `verification/transfer_stdout.txt`. Independently run `python3 code/check_direct.py` to enumerate every normalized state within mathematically exhaustive adjacent-gap bounds for \(k=2,3,4,5\); compare with `verification/direct_stdout.txt`. These are ordinary exact integer calculations. The proof of the universal all-core recurrence is the algebraic argument above, not an inference from the finite computations.

## Relationship to prior work

Duffy, Lidbetter, Messinger and Nowakowski (2016 preprint) introduced integer diffusion. Long and Narayanan (2017) established universal eventual periods one or two. Mullen, Nowakowski and Cox (2020, Section 3, Conjecture 1) proved the quartic count for paths and proposed that the same **homogeneous quartic** would apply to a graph joined by a bridge to a sufficiently long path. Equation (1) isolates the precise previously unaccounted-for flat-tail boundary term and proves that their proposed extension fails on the rooted triangle. Their published path theorem remains correct. An earlier exact transfer treatment of diffusion on cycles contains the nine-state Laurent matrix whose specialization at unit fugacity has the same quartic factor, but contains neither the root-drift boundary invariant, an arbitrary-core tail recurrence, nor a counterexample to the pendant-path conjecture. No priority claim is made for the model, the edge-reversal observation or the cycle transfer factorization.

## Limitations

The result concerns configurations **initially** in a one- or two-cycle, not preperiod lengths or basin sizes. Counts are of fixed labelled-vertex translation classes, not graph-isomorphism classes or temporal orbits; primitive orbit counts equal \(T_k/2\). The initial-source anchor dates the diffusion model, not the later conjecture. Searches of indexed literature and related published results do not establish historical uniqueness; a previously unindexed resolution or different normalization may remain to be compared independently. The proof does not extend equation (1) to disconnected cores, weighted graphs or alternative diffusion rules.

## References

1. C. Duffy, T. F. Lidbetter, M. E. Messinger, R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792, first version 19 September 2016; https://arxiv.org/html/1609.05792v5 .
2. J. Long, B. Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295, first version 13 April 2017; https://arxiv.org/abs/1704.04295 .
3. T. Mullen, R. J. Nowakowski, D. Cox, *Counting Path Configurations in Parallel Diffusion*, arXiv:2010.04750, first version October 2020; Section 3, Conjecture 1; https://arxiv.org/abs/2010.04750 .
