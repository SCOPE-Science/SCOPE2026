# An aperiodic seam-response law for the universal NOR two-cycle on cubic ladders

## Finding

Consider synchronous binary open-neighborhood NOR on two labelled cubic graphs with \(2n\) vertices: the ordinary prism \(P_n=C_n\square K_2\) and the Möbius ladder \(M_n\), for every integer \(n\ge3\). Let \(B_P(n)\) and \(B_M(n)\) denote the numbers of initial configurations eventually reaching the universal primitive two-cycle \(\varnothing\leftrightarrow V\), including its two states.

Let \(D_m\) be the number of dominating sets (closed-neighborhood domination) of the cycle \(C_m\). Then the complete all-size basin formulas are
\[
B_P(n)=1+\begin{cases}D_{2n},&n\text{ odd},\\D_n^2,&n\text{ even},\end{cases}
\qquad
B_M(n)=1+\begin{cases}D_n^2,&n\text{ odd},\\D_{2n},&n\text{ even}.\end{cases}
\]
Put \(v_0=3\), \(v_1=1\), \(v_2=-1\), and for all \(k\ge3\),
\[v_k=v_{k-1}-v_{k-2}-v_{k-3}.\]
The exact **twisted-seam response** is
\[
\boxed{B_M(n)-B_P(n)=-2v_n\qquad(n\ge3).}
\]
This difference never vanishes. Its sign is neither eventually constant nor eventually periodic: on **every infinite arithmetic progression of positive rung counts** both signs occur infinitely often. Nevertheless its relative magnitude decreases exponentially, at rate at most \(\bigl(1.3563/3.3829\bigr)^n\) up to a constant factor.

## Assumptions and scope

A vertex in state one is selected. The synchronous map on subsets of the vertex set is
\[F_G(S)=\{v\in V(G):N_G(v)\cap S=\varnothing\},\]
where \(N_G(v)\) is the **open** neighborhood, without the vertex itself. The graph \(P_n\) has columns \((i,0),(i,1)\), with horizontal edges within each row modulo \(n\) and a rung between rows in every column. In \(M_n\) the closing horizontal edges are replaced by twisted ones: \((n-1,0)\) joins \((0,1)\), and \((n-1,1)\) joins \((0,0)\). Both graphs are simple and three-regular for \(n\ge3\). No self-influence or tie convention is used. The result concerns **only the basin of the particular empty/full two-cycle**, not a classification of all other attractors.

## Proof

**Step 1 (the immediate-two-step projection and the target basin).** On any finite undirected graph without isolated vertices, \(F_G^3=F_G\). Indeed, if \(T=F_G(S)\), no vertex in \(S\) neighbors any vertex in \(T\); hence \(S\subseteq F_G(T)\). Conversely, if \(v\in T\), every neighbor \(w\) of \(v\) has \(v\in T\) among its neighbors, so \(w\notin F_G(T)\). Thus \(v\in F_G(F_G(T))\), proving \(F_G(S)\subseteq F_G^3(S)\). Antitonicity applied to \(S\subseteq F_G^2(S)\) gives the reverse inclusion. Therefore every state is on a fixed point or a two-cycle after at most one update. Since \(F_G(\varnothing)=V\) and \(F_G(V)=\varnothing\), the initial basin of this specific two-cycle consists precisely of \(\varnothing\) together with the sets \(S\) having \(F_G(S)=\varnothing\). The latter are exactly the **total dominating sets** of \(G\): every vertex has a selected open neighbor. Hence \(B_G=1+T_G\).

**Step 2 (turn open domination into closed cycle domination).** For each graph, form an auxiliary graph \(H\) on the same labelled vertex set by changing the row at exactly one endpoint of each horizontal edge joining successive columns (including the two possibly twisted seam edges), while discarding the rungs. Every vertex of \(H\) has degree two. At the vertex \((i,1-r)\), the three closed-neighborhood positions in \(H\) are exactly the three open neighbors of \((i,r)\) in \(G\): the rung opposite, plus the two horizontal neighbors of \((i,r)\). Consequently, selection of \(S\) is a total dominating set of \(G\) if and only if the same selected vertices constitute a closed-neighborhood dominating set of \(H\). Across every interior column boundary, edges of \(H\) switch the row. At the closing seam they switch the row for the ordinary prism but preserve it for the Möbius ladder. Therefore after one circuit of \(n\) columns, the row switches an odd number of times exactly when \(n+\epsilon\) is odd, with \(\epsilon=0\) for the untwisted prism and \(\epsilon=1\) for the Möbius seam. Thus \(H=C_{2n}\) when \(n+\epsilon\) is odd and \(H=C_n\sqcup C_n\) otherwise. Counts for disjoint cycles multiply. This proves both displayed formulas for \(B_P\) and \(B_M\).

**Step 3 (derive the cubic trace).** A subset dominates \(C_m\) precisely when its cyclic binary indicator contains no run of three zeros; equivalently each cyclic triple \((s_{i-1},s_i,s_{i+1})\) is not \((0,0,0)\). With states \(00,01,10,11\), the transfer from pair \((a,b)\) to pair \((b,c)\) is allowed unless \((a,b,c)=(0,0,0)\). Its explicit matrix and characteristic polynomial are
\[
A=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&1\end{pmatrix},\qquad\det(XI-A)=X(X^3-X^2-X-1).
\]
Thus for \(m\ge3\),
\[D_m=\lambda_1^m+\lambda_2^m+\lambda_3^m,\]
where the \(\lambda_i\) are the distinct roots of \(X^3-X^2-X-1\). This also follows directly from the cyclic transfer: valid cyclic length-\(m\) paths are precisely valid indicator words. Their elementary symmetric functions satisfy \(\sum\lambda_i=1\), \(\sum_{i<j}\lambda_i\lambda_j=-1\), \(\lambda_1\lambda_2\lambda_3=1\). Therefore the three pairwise products \(\mu_i\) have characteristic polynomial \(X^3+X^2+X-1\). Their negatives are the roots of \(Q(X)=X^3-X^2+X+1\); hence
\[
D_n^2-D_{2n}=2\sum_{i<j}(\lambda_i\lambda_j)^n=2(-1)^nv_n,
\qquad v_n=\sum_{Q(\zeta)=0}\zeta^n.
\]
The initial values and recurrence for \(v_n\) follow from Newton's identities and \(Q(\zeta)=0\). Swapping the parity cases from Step 2 gives \(B_M(n)-B_P(n)=-2v_n\) for all \(n\ge3\).

**Step 4 (nonvanishing and aperiodic sign).** The initial values \(v_0,v_1,v_2\) are odd and the recurrence preserves oddness modulo two, so \(v_n\ne0\). The discriminant of \(Q\) is \(-44\), and it has no rational root; hence its splitting field has Galois group \(S_3\) and its maximal abelian Galois subfield is \(\mathbb Q(\sqrt{-11})\). Write the roots as \(\gamma\in(-1,0)\) and \(\rho e^{\pm i\theta}\), with \(\rho>1\). The angle \(\theta/\pi\) is irrational: if \(e^{2i\theta}\) were a root of unity, its cyclotomic field would be an abelian Galois subfield of the splitting field, hence inside \(\mathbb Q(\sqrt{-11})\), which has no roots of unity other than \(\pm1\). Neither \(e^{2i\theta}=1\) (distinct nonreal roots) nor \(-1\) (opposite conjugate roots would give \(\gamma=1\), impossible) holds. Thus
\[v_n=2\rho^n\cos(n\theta)+\gamma^n.\]
For any positive integer modulus \(d\) and any residue class \(a\pmod d\), the phases \((a+kd)\theta\pmod{2\pi}\) are dense on the circle. Since \(|\gamma|<\rho\), there are infinitely many such integers \(n\) for which \(v_n>0\), and infinitely many for which \(v_n<0\). This proves the sign assertion and rules out eventual periodicity. Finally the positive real root \(\Lambda>3\) of \(X^3-3X^2-X-1\) dominates the basin counts, while \(\rho\approx1.3562\) and \(\Lambda\approx3.3830\), so the **relative difference**, normalized by either basin, is \(O((\rho/\Lambda)^n)\).

## Verification

The standalone `verify_nor_seam.py` builds the 16-state local transfer independently of the cycle-decomposition proof and checks its ordinary and row-swapped traces against the cubic formulas for every integer \(3\le n\le40\). It also exhaustively enumerates all \(4^n\) initial binary states of each graph for \(3\le n\le9\), verifies the global two-cycle basin counts, and checks the identity \(F^3=F\) configuration by configuration. Both paths agree.

| \(n\) | \(B_P(n)\) | \(B_M(n)\) | \(B_M(n)-B_P(n)\) |
|---:|---:|---:|---:|
|3|40|50|10|
|4|122|132|10|
|5|444|442|-2|
|6|1522|1500|-22|
|7|5072|5042|-30|
|8|17162|17156|-6|
|9|58036|58082|46|
|10|196250|196332|82|

The proof, not the finite checks, supplies the assertions for all \(n\ge3\).

## Relationship to prior work

The local NOR update mechanism and general period restrictions of undirected Boolean systems are established in Aledo–Martinez–Valverde (2015). The prism total-domination enumeration is **already known**: OEIS A296102 records the full sequence since April 2018, and a separate 2026 prism-domination result states the sharper parity factorization \(T_{P_n}=D_{2n}\) or \(D_n^2\). Neither the prism sequence nor that factorization is claimed here as new. The present assertion is the **comparison with the Möbius closure** for the global NOR attraction basin, including an exact cubic seam response, strict non-equality for every order, and infinitely oscillating sign on every arithmetic progression. Existing indexed Möbius results for minimum/minimal total domination and nearby majority/parity dynamics concern different invariants. The related prism treatment was available as an indexed abstract; complete source text could not be inspected, and historical-priority uncertainty remains.

## Limitations

This result counts exactly one distinguished two-cycle's initial basin; other fixed states and two-cycles on these graphs are not classified. The eventual sign is aperiodic in the precise non-eventual-periodicity sense, not a claim of randomness or uniformly distributed sign frequencies. The available literature search and indexed evidence cannot certify absolute historical novelty; in particular the related full-text prism-domination treatment was inaccessible. Finite verification cannot substitute for the all-size proof. No independent external mathematical audit has been performed.

## References

1. J. A. Aledo, S. Martinez, J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), article 594294, first published 24 March 2015. https://doi.org/10.1155/2015/594294
2. E. W. Weisstein and A. Howroyd, *Number of total dominating sets in the n-prism graph*, OEIS A296102 (sequence recorded 16 April 2018). https://oeis.org/A296102
3. *Parity-twisted cycle domination enumerates all total dominating sets of cycle prisms*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-parity-twisted-cycle-domination-enumerates-all-total-dominating--c74f62af476e
4. E. W. Weisstein and A. Howroyd, *Number of minimal total dominating sets in the n-Moebius ladder*, OEIS A303162 (2018). This counts inclusion-minimal sets only, not all total dominating sets. https://oeis.org/A303162
