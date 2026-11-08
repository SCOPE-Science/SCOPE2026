# Sharp root-degree–leaf-count covariance in affine preferential-attachment trees

## Finding

Consider a random tree started from the edge on labeled vertices \(1,2\). Each new vertex connects to one existing vertex with probability proportional to that vertex's current degree plus \(\delta\), for any fixed real \(\delta>-1\). Let \(D_n\) be the degree of the distinguished initial vertex \(1\), and let \(L_n\) be the *total number* of degree-one vertices at size \(n\). These two statistics have strictly positive covariance for every integer \(n\ge4\), and

\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(D_n,L_n)}{\mathbb E(D_n+\delta)}=\frac1{3+2\delta}.
\]

More explicitly, putting \(\gamma=(2+\delta)^{-1}\),

\[
\operatorname{Cov}(D_n,L_n)\sim
\frac{(1+\delta)\Gamma(2-2\gamma)}{(3+2\delta)\Gamma(2-\gamma)}\,n^\gamma.
\]

For degree-proportional attachment, \(\delta=0\), this becomes \(\operatorname{Cov}(D_n,L_n)\sim 2\sqrt n/(3\sqrt\pi)\). The exact first nonzero covariance is

\[
\operatorname{Cov}(D_4,L_4)=\frac{(1+\delta)(2+\delta)}{2(4+3\delta)^2}>0.
\]

## Assumptions and scope

The initial tree is one undirected edge with distinct labeled endpoints; vertex \(1\) is fixed in advance, not chosen as the eventual maximum-degree vertex. At each integer size \(n\ge2\), the next vertex attaches by a single edge, and, conditionally on the current tree, vertex \(v\) is selected with probability

\[
\frac{d_v(n)+\delta}{(2+\delta)n-2}.
\]

There are no loops, deleted edges, or extra edges. The parameter \(\delta\) is fixed and satisfies \(\delta>-1\). Degrees count incident edges. A leaf means a vertex of undirected degree one, including any initial vertex that still has degree one. Limits are taken through integers \(n\to\infty\), for each fixed parameter \(\delta\). All expectations and covariance are over the growing random tree.

Set \(a=1+\delta>0\), \(b=2+\delta>1\), \(T=3+2\delta=a+b>1\), \(S_n=bn-2>0\), and \(\gamma=1/b\in(0,1)\). The symbols \(R_n=\mathbb E(D_n+\delta)\), \(h_n=\Pr(D_n=1)\), \(M_n=\mathbb E L_n\), and \(C_n=\operatorname{Cov}(D_n,L_n)\) denote deterministic sequences.

## Proof

**Step 1: one-step laws.** Conditional on the tree at size \(n\), write \(I_n\) for the event that the new vertex selects vertex \(1\), and \(J_n\) for the event that it selects *some* leaf. The updates are

\[
D_{n+1}=D_n+I_n,\qquad L_{n+1}=L_n+1-J_n.
\]

Their conditional probabilities satisfy

\[
\mathbb E(I_n\mid\mathcal F_n)=\frac{D_n+\delta}{S_n},\quad
\mathbb E(J_n\mid\mathcal F_n)=\frac{aL_n}{S_n},\quad
\mathbb E(I_nJ_n\mid\mathcal F_n)=\frac{a\mathbf1_{\{D_n=1\}}}{S_n}.
\]

Consequently, with initial values \(R_2=a\), \(h_2=1\), \(M_2=2\),

\[
R_{n+1}=\left(1+\frac1{S_n}\right)R_n,\quad
h_{n+1}=\left(1-\frac a{S_n}\right)h_n,\quad
M_{n+1}=\left(1-\frac a{S_n}\right)M_n+1.
\]

Since \(S_{n+1}-a=S_n+1\) and \(S_{n+1}=S_n+b\), induction gives the two exact identities

\[
R_n=(S_n-a)h_n,\qquad M_n=\frac{S_n+2b h_n}{T}.
\]

**Step 2: the mixed-moment recursion and strict sign.** Multiplying the two one-step updates, taking conditional expectations, and subtracting \(R_{n+1}M_{n+1}\), yields for every \(n\ge2\)

\[
C_{n+1}=\left(1-\frac\delta{S_n}\right)C_n
+\frac{aR_nM_n}{S_n^2}-\frac{a h_n}{S_n},\qquad C_2=0.
\]

Use \(R_n=(S_n-a)h_n\) to rewrite the forcing term as

\[
\frac{a h_n}{S_n}\left(\frac{(S_n-a)M_n}{S_n}-1\right).
\]

Every tree on at least two vertices has at least two leaves, hence \(M_n\ge2\). At \(n=2\), \(S_2=2a\) and the bracket is zero. For every \(n>2\), \(S_n>2a\), so the bracket is strictly positive; also \(1-\delta/S_n>0\). Therefore \(C_3=0\) and \(C_n>0\) for every \(n\ge4\). Substituting \(n=3\), where \(h_3=1/2\), \(M_3=2\), and \(S_3=4+3\delta\), gives the stated exact formula for \(C_4\).

**Step 3: exact root-degree mean.** Because \(S_j=b(j-2\gamma)\), the first recurrence solves to

\[
R_n=a\prod_{j=2}^{n-1}\frac{j-\gamma}{j-2\gamma}
=a\frac{\Gamma(2-2\gamma)}{\Gamma(2-\gamma)}
\frac{\Gamma(n-\gamma)}{\Gamma(n-2\gamma)}.
\]

The gamma-ratio asymptotic yields \(R_n\sim r_\delta n^\gamma\), with \(r_\delta=a\Gamma(2-2\gamma)/\Gamma(2-\gamma)>0\). Also \(h_n=R_n/(S_n-a)=O(n^{\gamma-1})\).

**Step 4: asymptotic mixed covariance.** Define the deviation \(E_n=C_n-R_n/T\). The exact recurrences and the expression for \(M_n\) give

\[
E_{n+1}=q_nE_n+\varepsilon_n,\qquad
q_n=1-\frac\delta{S_n},\qquad
\varepsilon_n=\frac{2abR_nh_n}{T S_n^2}-\frac{a h_n}{S_n}.
\]

Each \(q_n>0\). Define \(Q_2=1\) and \(Q_n=\prod_{j=2}^{n-1}q_j\). The identity \(S_j-\delta=b(j-1)\) yields the exact positive product

\[
Q_n=\frac{\Gamma(n-1)\Gamma(2-2\gamma)}{\Gamma(n-2\gamma)}
\asymp n^{2\gamma-1}.
\]

From the bounds in Step 3, \(\varepsilon_n=O(n^{2\gamma-3}+n^{\gamma-2})\). Hence

\[
\sum_{n=2}^{\infty}\frac{|\varepsilon_n|}{Q_{n+1}}
<\infty,
\]

because its summands are \(O(n^{-2}+n^{-1-\gamma})\), and \(\gamma>0\). Iterating the inhomogeneous recursion gives \(E_n=Q_n[E_2+\sum_{j=2}^{n-1}\varepsilon_j/Q_{j+1}]\), so \(E_n=O(n^{2\gamma-1})=o(n^\gamma)=o(R_n)\), since \(0<\gamma<1\). Thus \(C_n/R_n\to1/T\), and the explicit asymptotic follows from Step 3.

All bounds are for fixed \(\delta>-1\); no uniformity as the parameter approaches its boundary or grows with \(n\) is asserted. This completes the proof.

## Verification

The included standalone Python checker uses exact rational arithmetic to enumerate the joint distribution of root degree and total leaves up to size \(11\), for six rational parameter choices, and independently checks the exact covariance, mean, and root-leaf recurrences. It also iterates the deterministic moment recurrences to size \(100000\) for six floating parameter choices, to illustrate the convergence and its parameter-dependent rate. Run with `python3 check_covariance.py`. The checker terminates with `ALL CHECKS PASS` when its assertions succeed. These finite computations verify identities and detect transcription errors; they are not a substitute for Steps 1–4, which establish the infinite asymptotic.

## Relationship to prior work

Hartle and Krapivsky (2026) analyze leafdegree and the fluctuations of the **total number of leaves**, including a closed one-dimensional leaf-count equation for degree-proportional attachment. Their inspected Sec. IV.1 and appendices do not compute the cross-covariance of one specified old vertex's degree with the global leaf count, nor a ratio law across all fixed affine offsets.

Krapivsky and Redner (2002) derive finite-size degree-count moments and covariance for **numbers of vertices of fixed degrees**, including the pair of degree-one and degree-two counts; those are not the degree of the initially specified root. The present statement distinguishes the root from the population and gives the mixed covariance of a sublinearly growing hub and a linearly growing fringe statistic.

A separately published exact root-degree–leaf covariance for the **uniform random recursive tree** is not a proof of this theorem for degree-proportional selection. Under uniform attachment the root's degree grows logarithmically, whereas under fixed affine preferential attachment it grows as a power. Comparing the mathematical implications does not reveal prior coverage of the present theorem.

## Limitations

Historical priority is subject to broader preferential-attachment moment identities not located in the consulted references. A general urn or joint-occupation theorem might imply the displayed result after a nontrivial specialization. The result concerns a single fixed old vertex, not the maximum-degree vertex or the vector of all degree counts. It supplies a covariance law, not a bivariate central limit theorem, a joint weak limit, or a pathwise monotonicity statement. The finite checker covers only rational choices and finite tree sizes; all infinite statements are analytical.

## References

1. H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021, first posted 2026-02-01. https://arxiv.org/html/2602.01021
2. P. L. Krapivsky and S. Redner, *Finiteness and Fluctuations in Growing Networks*, arXiv:cond-mat/0207107, 2002. https://arxiv.org/pdf/cond-mat/0207107
3. *Equal-share covariance of root degree and leaves in a random recursive tree*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f
