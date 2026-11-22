# Three Nyström landmark phases on highly asymmetric complete bipartite networks

## Finding

Let \(p\ge3\) be an integer. For every sufficiently large integer \(q\), consider the unweighted complete bipartite graph \(K_{p,q}\), its Laplacian \(L\), a screening parameter \(t>0\), and the positive-definite kernel \(K=(tI+L)^{-1}\). Select exactly two distinct vertices \(S\) to minimize the Nyström trace loss
\[
 E(S)=\operatorname{tr}\bigl(K-K_{:,S}K_{S,S}^{-1}K_{S,:}\bigr).
\]
There are exactly three possible landmark-pair orbits: \(AA\), two vertices in the \(p\)-vertex part; \(AB\), one in each part; and \(BB\), two in the \(q\)-vertex part. Two sharp transition points \(0<\alpha_{p,q}<\beta_{p,q}\) exist. Every optimum belongs to orbit \(AA\) for \(0<t<\alpha_{p,q}\), orbit \(AB\) for \(\alpha_{p,q}<t<\beta_{p,q}\), and orbit \(BB\) for \(t>\beta_{p,q}\). At each transition exactly the adjacent two orbits tie and the third is strictly worse. Within an optimal orbit, every pair is equally optimal. Moreover,
\[
 \alpha_{p,q}=\sqrt{p-1}-1+O_p(q^{-1}),\qquad
 \beta_{p,q}=\sqrt p+O_p(q^{-1}).
\]
In particular, the mixed-shore optimum occupies a nonvanishing interval in screening strength as the larger part grows. The lower transition is strictly positive for every fixed \(p\ge3\), in contrast to the degenerate \(p=2\) limit.

A fully effective finite-size criterion is given below: the transition theorem holds for any integers \(3\le p<q\) for which the coefficient and midpoint tests in the proof hold, without requiring a preselected asymptotic cutoff.

## Assumptions and scope

The graph has a unit-conductance edge between every pair of vertices in opposite parts, no other edges, and zero extra vertex killing beyond the uniform positive shift \(t\). The Laplacian is the combinatorial, unnormalized Laplacian. The two observations are noiseless and correspond to distinct selected columns. The objective is the total posterior variance, equivalently the trace of the positive-semidefinite Nyström residual, not determinant, expected randomized error, or a multistep objective. All assertions are exact; \(O_p(q^{-1})\) means a constant depending on fixed \(p\) times \(q^{-1}\) as \(q\to\infty\).

## Proof

**1. Covariance orbit reduction.** Write \(N=p+q\) and
\[
 x=t^{-1},\qquad y=(t+N)^{-1},\qquad u=(t+q)^{-1},\qquad v=(t+p)^{-1}.
\]
Spectral decomposition of the graph Laplacian into the constant, between-part, within-\(A\), and within-\(B\) eigenspaces, with eigenvalues \(0,N,q,p\), gives these entries of \(K\):
\[
 a=\frac{x}{N}+\frac{qy}{pN}+u\Bigl(1-\frac1p\Bigr),\quad
 b=\frac{x}{N}+\frac{qy}{pN}-\frac up,
\]
\[
 c=\frac{x}{N}+\frac{py}{qN}+v\Bigl(1-\frac1q\Bigr),\quad
 d=\frac{x}{N}+\frac{py}{qN}-\frac vq,
 \qquad e=\frac{x-y}{N}.
\]
Here \(a,c\) are diagonal entries on the respective parts, \(b,d\) are distinct-vertex same-part entries, and \(e\) is a cross-part entry. Let \(a_2,b_2,c_2,d_2,e_2\) denote the corresponding entries of \(K^2\); they are obtained by squaring \(x,y,u,v\) in the preceding five linear formulas (equivalently, differentiating with respect to \(t\) and negating).

The trace reduction \(H(S)=\operatorname{tr}(K_{S,S}^{-1}(K^2)_{S,S})\) satisfies \(E(S)=\operatorname{tr}K-H(S)\). Explicit two-by-two inversion yields the only three possible scores:
\[
 H_{AA}=\frac{a_2+b_2}{a+b}+\frac{a_2-b_2}{a-b},\qquad
 H_{BB}=\frac{c_2+d_2}{c+d}+\frac{c_2-d_2}{c-d},
\]
\[
 H_{AB}=\frac{ca_2+ac_2-2ee_2}{ac-e^2}.
\]
All denominators are positive because \(K\) is positive definite. Minimizing the trace loss is precisely maximizing these scores.

**2. Exact crossing numerators.** Define positive denominators
\[
 D_A=(t+1)(t+p)(t+q)(t+p+q-1)(t^2+t(p+q)+2q),
\]
\[
 D_B=(t+1)(t+p)(t+q)(t+p+q-1)(t^2+t(p+q)+2p).
\]
Direct common-denominator simplification, verifiable exactly by the companion checker, gives
\[
 H_{AA}-H_{AB}=\frac{U_{p,q}(t)}{D_A},\qquad
 H_{BB}-H_{AB}=\frac{V_{p,q}(t)}{D_B},
\]
where
\[
\begin{aligned}
 U_{p,q}(t)={}&(p-q)t^4+2(p^2-p-q^2+q+1)t^3\\
 &+(p^3+p^2q-2p^2-pq^2+2pq+2p-q^3+4q)t^2\\
 &+2q(pq+2p-q^2+q)t\\
 &-q(p^3-3p^2-pq^2-pq+2p+2q^2-2q),
\end{aligned}
\]
\[
\begin{aligned}
 V_{p,q}(t)={}&(q-p)t^4-2(p^2-p-q^2+q-1)t^3\\
 &+(-p^3-p^2q+pq^2+2pq+4p+q^3-2q^2+2q)t^2\\
 &-2p(p^2-pq-p-2q)t\\
 &+p(p^2q-2p^2+pq+2p-q^3+3q^2-2q).
\end{aligned}
\]

**3. Unique crossings and their order.** Fix any integer \(p\ge3\) and take \(q\) sufficiently large. The coefficients of \(U_{p,q}\), in descending powers \(t^4,t^3,t^2,t,t^0\), then have signs \((-,-,-,-,+)\). The corresponding coefficients of \(V_{p,q}\) have signs \((+,+,+,+,-)\). In each case Descartes' rule, together with the opposite signs at zero and at positive infinity, proves exactly one positive root, called \(\alpha_{p,q}\) and \(\beta_{p,q}\) respectively. Moreover, coefficientwise as \(q\to\infty\),
\[
 q^{-3}U_{p,q}(t)\longrightarrow p-2-2t-t^2,
 \qquad q^{-3}V_{p,q}(t)\longrightarrow t^2-p.
\]
Both limiting polynomials have simple positive roots, respectively \(\sqrt{p-1}-1\) and \(\sqrt p\). Continuity of a simple root (or the implicit function theorem in \(1/q\)) gives the two asserted \(O_p(q^{-1})\) asymptotics. Since \(\sqrt{p-1}-1<\sqrt p\), the order \(\alpha_{p,q}<\beta_{p,q}\) holds for all sufficiently large \(q\).

The signs of the two score differences are consequently: before \(\alpha_{p,q}\), \(H_{AA}>H_{AB}>H_{BB}\); between \(\alpha_{p,q}\) and \(\beta_{p,q}\), \(H_{AB}>H_{AA}\) and \(H_{AB}>H_{BB}\); after \(\beta_{p,q}\), \(H_{BB}>H_{AB}>H_{AA}\). At the boundaries, only the adjacent orbits tie. This proves the complete set of optimum landmark pairs.

For any given finite integers \(3\le p<q\), the same conclusion is effective without an unknown large-\(q\) threshold: calculate the five coefficients of each displayed quartic, verify the stated sign patterns, and verify \(U_{p,q}(\sqrt p-1/2)<0\) and \(V_{p,q}(\sqrt p-1/2)<0\). The first two tests prove unique positive roots; the midpoint tests place the \(U\) root before \(\sqrt p-1/2\) and the \(V\) root after it. Thus all statements hold for this individual \((p,q)\). For every fixed \(p\ge3\), these finite tests eventually hold because both limiting polynomial values at the midpoint are strictly negative.

## Verification

Run `python verify.py` with SymPy. The program derives the exact five covariance entries, independently checks the two quartic identities and their limits, then constructs and inverts the actual rational Laplacian matrices for complete bipartite graphs with multiple part sizes and screening strengths. It compares the scores of every possible two-vertex selection to the orbit formulas. It additionally checks quartic coefficient signs and the midpoint inequalities on representative parameter families. The exact verifier returned 7,082 passing assertions. These finite instances do not prove the universal asymptotic statement; that follows from the coefficientwise polynomial argument above.

For example, with \(p=3,q=30\), the roots are approximately \(\alpha_{3,30}=0.5078303637\) and \(\beta_{3,30}=1.5215002460\). Their limiting values are \(\sqrt2-1\) and \(\sqrt3\).

## Relationship to prior work

Gaussian-process sensor selection and kernel-column Nyström completion are established general frameworks. Guestrin, Krause, and Singh (2005) study information-based sensor placement; Krause, Singh, and Guestrin (2008) develop submodular mutual-information selection; and Belabbas and Wolfe (2009), especially their optimal landmark problem and trace-error characterization, give the general approximation objective. None of these inspected full texts states this exact all-\(p\) asymmetric-biclique three-phase classification. General matrix identities imply the score formulas but not the optimal-orbit transition structure without comparing all three signs.

The two-vertex smaller-part case is not the claim here: its first asymptotic crossing collapses to screening zero, whereas the theorem covers every fixed \(p\ge3\) and gives a nonzero first critical value. More recent general column-selection literature may contain unindexed equivalent consequences; this has not been excluded categorically.

## Limitations

The theorem is asymptotic in the larger shore for each fixed \(p\), and does not claim to identify the smallest permissible \(q\) for every \(p\). The finite-size polynomial test is sufficient, not necessary. The scope is exactly two noiseless landmarks and uniform screening of an unweighted biclique, not weighted edges, observation noise, general multipartite graphs, or arbitrary sensor budgets. Novelty is based on accessible comparisons rather than a guarantee of publication priority. Independent external validation has not been conducted.

## References

1. C. Guestrin, A. Krause, and A. P. Singh, "Near-Optimal Sensor Placements in Gaussian Processes," ICML, August 7, 2005. https://www.cs.cmu.edu/~guestrin/Publications/ICML2005-GP/icml2005-gp.pdf
2. A. Krause, A. Singh, and C. Guestrin, "Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies," *Journal of Machine Learning Research* 9 (2008), 235–284. https://jmlr.csail.mit.edu/papers/volume9/krause08a/krause08a.pdf
3. M.-A. Belabbas and P. J. Wolfe, "On Landmark Selection and Sampling in High-Dimensional Data Analysis," arXiv:0906.4582, June 24, 2009. https://arxiv.org/pdf/0906.4582
4. M. Fornace and M. Lindsey, "Column and Row Subset Selection Using Nuclear Scores," arXiv:2407.01698 (2024). https://arxiv.org/abs/2407.01698
