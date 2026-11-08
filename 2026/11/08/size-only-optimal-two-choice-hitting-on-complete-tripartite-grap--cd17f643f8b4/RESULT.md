# Size-only optimal two-choice hitting on complete tripartite graphs

## Finding

Let \(G=K_{a,b,c}\), with integers \(a\ge 2\), \(b\ge c\ge1\), and distinguish a target vertex \(t\) in the part of size \(a\). At each step of a controlled walk, two neighbors are sampled independently and uniformly with replacement; exactly one offered neighbor must be visited. The objective is to minimize expected first hitting time of \(t\), allowing arbitrary adaptive randomized strategies.

**The optimal strategy is determined entirely by part sizes:** always prefer \(t\), followed by a vertex in the \(b\)-part, then one in the \(c\)-part, and lastly any nontarget vertex in the \(a\)-part. When \(b=c\), the two other parts are interchangeable; when \(b>c\), every strict comparison in this priority order holds. The optimal expected hitting times \(H_A,H_B,H_C\) from a nontarget vertex in the respective parts are the unique solution of the explicit three-by-three system below, and obey

\[
H_A>H_C\ge H_B>0,\qquad H_C=H_B\ \Longleftrightarrow\ b=c.
\]

Put
\[
q=\frac{c^2}{(b+c)^2},\quad s_c=\frac{a-1}{a+c},\quad t_c=\frac{c}{a+c},\quad s_b=\frac{a-1}{a+b},\quad t_b=\frac{b}{a+b}.
\]
Then
\[
\begin{pmatrix}
1&-(1-q)&-q\\
-s_c^2&1&-(t_c^2+2s_ct_c)\\
-s_b^2&-(t_b^2+2s_bt_b)&1
\end{pmatrix}
\begin{pmatrix}H_A\\H_B\\H_C\end{pmatrix}
=
\begin{pmatrix}1\\1\\1\end{pmatrix}.
\]

## Assumptions and scope

The graph is finite, unweighted, simple, complete tripartite with all parts nonempty, and \(a\ge2\). The target is in the \(a\)-part, so this part has at least one additional nontarget vertex. The two offers at each move are conditionally independent uniformly sampled neighbors, with repetition; the controller knows the current vertex, the target and the part sizes, and may use the entire history. Time is counted in traversed edges, including the final move to \(t\). The theorem is exact for all positive integer parameters in the stated range, not asymptotic.

## Proof

Call the target-containing part \(A\), and the others \(B,C\). Under the stated stationary priority rule, the expected remaining times from nontarget vertices depend only on their parts. At a vertex of \(A\), the two offers are drawn from \(B\cup C\), with \(B\) preferred. At a vertex of \(B\), the possible types are target (cost zero), \(C\), and nontarget \(A\), in that order. At a vertex of \(C\), the possible types are target, \(B\), and nontarget \(A\). Enumerating the ordered pairs of offers yields the displayed linear system.

Every nontarget state reaches the target under this rule with a uniformly positive probability within at most three steps: the first step from \(A\) reaches \(B\) or \(C\), and at either class the target is offered with positive probability. Thus its transient transition matrix has spectral radius strictly less than one and the linear system has a unique finite positive solution. In particular its determinant is positive.

For the exact comparison multiply the three rows by \((b+c)^2\), \((a+c)^2\), and \((a+b)^2\), respectively, obtaining the integer matrix

\[
L=\begin{pmatrix}
(b+c)^2&-(b^2+2bc)&-c^2\\
-(a-1)^2&(a+c)^2&-(c^2+2c(a-1))\\
-(a-1)^2&-(b^2+2b(a-1))&(a+b)^2
\end{pmatrix}.
\]

Write \(\Delta=\det L>0\), and let \(L_j\) denote the matrix obtained by replacing column \(j\), with columns indexed by \(A,B,C\), by \(((b+c)^2,(a+c)^2,(a+b)^2)^T\). Cramer's rule gives \(H_j=\det(L_j)/\Delta\). Elementary determinant expansion gives

\[
\Delta(H_C-H_B)=(b-c)(b+c)^2\bigl(2a(b+c+1)+2bc-b-c-2\bigr)=:N.
\]

The bracket is \((2a-1)(b+c)+2(a-1)+2bc>0\). Hence \(H_C\ge H_B\), with equality exactly when \(b=c\).

The first row yields \(H_A=1+(1-q)H_B+qH_C\), so \(\Delta(H_A-H_C)=\Delta-(1-q)N=:P\). We prove \(P>0\) by a positive-coefficient identity. Set \(u=a-2\), \(v=c-1\), \(w=b-c\); all are nonnegative integers. Exact polynomial expansion gives

\[
P=P_0(u,v)+wP_1(u,v)+w^2P_2(u,v)+w^3P_3(u,v),
\]
\[
\begin{aligned}
P_0={}&4(v+1)^2(2u+2v+5)(u^2+4uv+8u+2v^2+10v+12),\\
P_1={}&2(v+1)(4u^3+29u^2v+51u^2+42uv^2+175uv+173u\\
&\qquad+17v^3+114v^2+251v+178),\\
P_2={}&2u^3+26u^2v+37u^2+46uv^2+172uv+146u\\
&\qquad+22v^3+135v^2+270v+169,\\
P_3={}&2(2u^2+4uv+10u+2v^2+10v+13).
\end{aligned}
\]

Each \(P_j\) is strictly positive on \(u,v\ge0\), and \(w\ge0\), so \(P>0\). This proves \(H_A>H_C\ge H_B\). The two determinant identities can be reproduced with exact arithmetic using `verify.py`. In particular, both identities compare polynomials of degree at most six in each of \(a,b,c\); the checker verifies them on seven distinct values of each variable. Polynomial interpolation makes this an exact universal algebraic verification rather than an experiment on selected graph orders.

With this established ordering, the announced priority rule always chooses a neighbor with smallest remaining hitting value from the two offers. Therefore its values satisfy the Bellman minimum equations. As the target is reached almost surely with finite mean under this rule, the standard finite stochastic-shortest-path comparison proves that these values are minimal among **all** history-dependent strategies. If \(b>c\), the strict inequalities also force the stated preference whenever differing neighbor types are offered. If \(b=c\), choices between \(B\) and \(C\) are indifferent. This completes the proof.

## Verification

Run `python3 verify.py` using Python 3 with no third-party dependencies. The checker uses integer determinants and `fractions.Fraction`. It verifies both degree-bounded polynomial identities on \(7^3\) triples (686 identity checks), and independently constructs the entire labeled-vertex transition system for 45 graphs with \(2\le a\le4\), \(1\le c\le b\le5\). These give 720 exact full-vertex Bellman/value comparisons. Expected output is `VERIFY_OK algebra_identities=686 full_graphs=45 exact_full_vertex_checks=720`. The exact symbolic identities, combined with the degree bound and coefficient positivity, establish the all-parameter sign result; the finite full-vertex tests are independent corroboration.

## Relationship to prior work

Georgakopoulos, Haslegrave, Sauerwald and Sylvester introduce the two-offer choice random walk and establish in their Lemma 7.1 that preferring lower optimal hitting values is optimal on arbitrary graphs; their Theorem 1.6 supplies a general polynomial-time strategy algorithm. Their Table 1 includes the complete graph but not complete tripartite graphs. The present result does not claim the Bellman principle or the existence of an optimal stationary policy as new. It identifies, without running any graph-specific optimization, the exact optimal ranking from part sizes across the infinite three-parameter complete-tripartite family, and provides a three-state exact hitting-time formula. The 2020 conference treatment is a precursor to that work. Other relevant results on controlled cover walks and distance-priority rules address different objectives or graph families.

## Limitations

This is an expected hitting-time statement, not an all-deadline stochastic-domination theorem. It assumes two independent offers with replacement, no holding moves, one vertex target, and exactly three complete parts. It neither solves arbitrary complete multipartite graphs with four or more parts nor gives finite-sample uncertainty guarantees. General historical priority beyond the sources compared remains an open bibliographic risk; no independent mathematical audit is asserted.

## References

1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170, first posted November 12, 2019; later *Combinatorics, Probability and Computing* 31 (2022), 73–100. https://arxiv.org/abs/1911.05170 . Relevant sections: 1.2, 2, 7.1, particularly Lemma 7.1 and Theorem 1.6.
2. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *Choice and Bias in Random Walks*, ITCS 2020, article 76. https://doi.org/10.4230/LIPIcs.ITCS.2020.76 . An earlier treatment of the controlled-walk model.
