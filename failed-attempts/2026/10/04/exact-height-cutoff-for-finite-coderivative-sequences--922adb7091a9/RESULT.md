# Exact height cutoff for finite coderivative sequences
## Finding

Let \(K\) be a finite nonempty poset. Write \(\operatorname{Up}(K)\) for its complete Heyting algebra of upsets, and let \(\nabla\) be the point-free coderivative. For every upset \(X\subseteq K\), Kocsis's Alexandroff-space characterization gives
\[
\nabla(X)=\{w\in K:\forall v>w,\ v\in X\}.
\]

For a finite subposet \(Q\), let \(\operatorname{ht}(Q)\) denote the maximum number of points in a chain, with \(\operatorname{ht}(\varnothing)=0\). Then for every integer \(k\ge 0\),
\[
w\notin\nabla^k(X)
\quad\Longleftrightarrow\quad
\text{there is a chain }w=w_0<w_1<\cdots<w_k\text{ contained in }K\setminus X.
\]
Consequently,
\[
\nabla^k(X)=K
\quad\Longleftrightarrow\quad
k\ge \operatorname{ht}(K\setminus X).
\]

Now put
\[
\Delta(\varphi):=\forall Y.\bigl(Y\vee(Y\to\varphi)\bigr),
\]
so that \(\Delta\) is interpreted by \(\nabla\), and let
\[
M:=\forall X.(\Delta(X)\to X)\to X.
\]
For \(N\ge0\), define the truncated free-coderivative theory
\[
T_N=\{M\}\cup\{\Delta(P_{j+1})\to P_j:0\le j<N\}.
\]
If \(h=\operatorname{ht}(K)\), then \(M\) is valid in \(\operatorname{Up}(K)\), and for every \(0\le i\le N\),
\[
T_N\models_{\operatorname{Up}(K)} P_i
\quad\Longleftrightarrow\quad
N-i\ge h.
\]
Thus the forced variables form an exact initial segment:
\[
P_0,\ldots,P_{N-h}
\]
when \(N\ge h\), and none of \(P_0,\ldots,P_N\) is forced when \(N<h\). In particular, the least truncation length that forces \(P_0\) is exactly the height of \(K\).

## Assumptions and scope

The order on \(K\) is a finite partial order and validity is complete-Heyting-algebra validity in the single algebra \(\operatorname{Up}(K)\). Height counts points, not strict inequalities: a one-point poset has height \(1\).

The result concerns the finite truncations \(T_N\) of the free \(\nabla\)-sequence used by Kocsis. It does not assert strong completeness of second-order intuitionistic propositional logic, nor does it alter the infinite counterexample from the source paper.

## Proof

Let \(Q=K\setminus X\). Because \(X\) is an upset, \(Q\) is a downset.

We first prove the iterate formula by induction on \(k\). For \(k=0\), \(w\notin X\) exactly when the one-point chain \(w=w_0\) lies in \(Q\). Assume the statement for \(k\). By the coderivative characterization,
\[
w\notin\nabla^{k+1}(X)
\]
iff some \(v>w\) satisfies \(v\notin\nabla^k(X)\). By the inductive hypothesis, this is equivalent to a chain
\[
v=w_1<w_2<\cdots<w_{k+1}
\]
inside \(Q\). Since \(Q\) is a downset and \(w<v\), also \(w\in Q\), so adjoining \(w=w_0\) gives the required chain of \(k+2\) points. The converse reverses the same argument. Hence \(\nabla^k(X)=K\) exactly when \(Q\) has no chain of \(k+1\) points, which is equivalent to \(k\ge\operatorname{ht}(Q)\).

Next, \(M\) is valid in \(\operatorname{Up}(K)\). Kocsis proves that \(M\) denotes the least fixed point of \(\nabla\). A finite poset has no proper fixed upset. Indeed, if \(X\ne K\), choose a maximal point \(q\) of the nonempty downset \(K\setminus X\). Every strict successor of \(q\) lies in \(X\), so
\[
q\in\nabla(X)\setminus X.
\]
Thus the only fixed point is \(K\), and the least fixed point is \(K\).

Finally, suppose a valuation satisfies \(T_N\). Each sequence axiom means
\[
\nabla(P_{j+1})\subseteq P_j.
\]
Iterating and using monotonicity gives
\[
\nabla^{N-i}(P_N)\subseteq P_i.
\]
If \(N-i\ge h\), then \(\varnothing\subseteq P_N\) and monotonicity yield
\[
K=\nabla^{N-i}(\varnothing)\subseteq\nabla^{N-i}(P_N)\subseteq P_i,
\]
so \(P_i=K\).

Conversely, if \(N-i<h\), define for \(0\le j\le N\)
\[
P_j:=\nabla^{N-j}(\varnothing).
\]
Every sequence axiom then holds with equality, and \(M\) is valid as proved above. But
\[
P_i=\nabla^{N-i}(\varnothing)\ne K
\]
because \(N-i<h\). Hence \(P_i\) is not semantically forced. This proves the exact profile.

## Verification

The proof uses only the explicit coderivative formula on upsets, finiteness of \(K\), and monotonicity of \(\nabla\).

A standalone checker exhaustively enumerates every labelled poset on at most four points and every upset. It verifies the iterate formula and the exact height at which \(\nabla^k(X)\) reaches the top. It also checks that the top upset is the unique fixed point for every nonempty finite poset.

As an independent semantic check, for every labelled poset on at most three points and every \(N\le3\), the checker exhaustively enumerates all valuations of \(P_0,\ldots,P_N\) by upsets satisfying the sequence inequalities. It confirms that \(P_i\) is forced exactly when \(N-i\) is at least the poset height.

The finite enumeration is not used as a proof of the general theorem.

## Relationship to prior work

Kocsis defines the point-free coderivative, proves its strict-successor characterization on upset algebras, defines \(\Delta\), \(M\), and the free \(\nabla\)-sequence, and uses the truncated theories \(T_N\) to prove failure of strong completeness for complete Heyting algebra semantics. In the proof of nonderivability, the paper observes for the special case \(X=\varnothing\) that failure of membership in \(\nabla^N(\varnothing)\) is witnessed by a strict chain of length \(N\) above a point.

The present result turns that observation into a complete finite-poset classification. It handles arbitrary starting upsets \(X\), identifies the exact iterate-to-top time as the height of the complement, proves that \(M\) is automatically valid on every finite upset algebra, and determines exactly which variables in every truncated free sequence are semantically forced.

Targeted searches for the free \(\nabla\)-sequence together with finite poset height, chain length, truncation depth, and exact semantic forcing did not locate this finite-height cutoff statement.

## Limitations

The height formula relies on finiteness. For infinite posets, finite iterations need not reach the least fixed point, and transfinite iteration may be relevant.

The theorem concerns upset algebras of finite posets. Although every finite Heyting algebra has a finite Esakia dual, this package does not state a dual reformulation for arbitrary finite Heyting algebras.

Search non-detection is not a proof of novelty; an equivalent finite-height observation could occur under different terminology.

## References

[1] Zoltan A. Kocsis, “Two applications of the point-free coderivative,” arXiv:2609.29436, first posted 24 September 2026.

[2] Harold Simmons, “An algebraic version of Cantor–Bendixson analysis,” in *Categorical Aspects of Topology and Analysis*, Lecture Notes in Mathematics, 1982, DOI:10.1007/BFb0092888.
