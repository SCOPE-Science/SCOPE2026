# A sharp Braess-type sign law for sandpile avalanches on chorded cycles

## Finding
For every integer \(n\ge4\), let \(C_n\) have vertices \(0,1,\ldots,n-1\) and edges between successive indices modulo \(n\). Fix the single sink at vertex \(0\), and add one grain at vertex \(1\) to a uniformly chosen recurrent stable state. Count the **total number of individual nonsink topplings**, with repeated topplings counted repeatedly, and denote its mean by \(M(G)\).

For integers \(1\le i<j\le n-1\) with \(j-i\ge2\), add the previously absent chord \(\{i,j\}\), and put \(d=j-i\). Then
\[
M(C_n)=\frac{n-1}{2},\qquad
M(C_n+\{i,j\})-M(C_n)=
\frac{d^2(n-i-j)}{2\bigl[n+d(n-d)\bigr]}.
\]
This gives a complete sign classification: the additional edge **increases** mean avalanche topplings exactly when \(i+j<n\), has no effect exactly when \(i+j=n\), and **decreases** them exactly when \(i+j>n\). The smallest positive case is \(n=5\), with chord \(\{1,3\}\) and increase \(2/11\); the only nonsink chord for \(n=4\) is neutral.

For every \(n\ge5\), a chord \(\{1,k\}\) with \(3\le k\le n-2\) strictly increases the mean. In this subfamily the ratio \(M(C_n+\{1,k\})/M(C_n)\) is always less than \(2\), yet the choice \(k=n-\lfloor\sqrt n\rfloor\) yields a ratio converging to \(2\) as \(n\to\infty\).

## Assumptions and scope
The graphs are finite, connected, undirected, unweighted and simple. Stable heights are integers from \(0\) to \(\deg(v)-1\) at every nonsink vertex. An unstable vertex topples by sending one grain along each incident edge; grains reaching the sink disappear. Both before and after edge insertion, the initial configuration is sampled uniformly from that graph's own recurrent configurations. There is one deterministic addition at vertex \(1\). Toppling **count** is not avalanche area or number of distinct vertices that topple. The chord is required to have two nonsink endpoints and not to be an existing cycle edge; no claim is made about chords touching the sink or other injection vertices.

## Proof
Write \(L\) for the reduced graph Laplacian, indexed by nonsink vertices. A grain addition at vertex \(1\) is a permutation of the finite sandpile recurrent group. If \(\eta\) and \(\eta'\) are its initial and final stable states and \(T\) is the integer vector of all topplings, then \(\eta'=\eta+e_1-LT\). Stationarity of the uniform recurrent law implies \(\mathbb E\eta'=\mathbb E\eta\), hence \(L\mathbb ET=e_1\). As \(L\) is invertible, the mean total number of topplings is \(\mathbf1^\top L^{-1}e_1=(L^{-1}\mathbf1)_1\). This identity is a standard consequence of finite sandpile stationarity; the contribution here is its evaluation after the chord perturbation.

For the cycle, the reduced Laplacian is the \((n-1)\)-dimensional path Dirichlet Laplacian. Its Green function and Poisson solution are
\[
(L^{-1})_{ab}=\frac{\min(a,b)\,[n-\max(a,b)]}{n},
\qquad (L^{-1}\mathbf1)_a=\frac{a(n-a)}2,
\qquad 1\le a,b\le n-1.
\]
These follow by checking the second finite differences and the Dirichlet boundary conditions at indices \(0\) and \(n\). In particular \(M(C_n)=(n-1)/2\).

Let \(b=e_i-e_j\). The chord changes the reduced Laplacian to \(L'=L+bb^\top\). Sherman–Morrison gives
\[
L'^{-1}=L^{-1}-\frac{L^{-1}bb^\top L^{-1}}{1+b^\top L^{-1}b}.
\]
Putting \(u=L^{-1}\mathbf1\) and \(d=j-i\), the explicit Green function yields
\[
(L^{-1}b)_1=\frac dn,\qquad
b^\top u=-\frac{d(n-i-j)}2,\qquad
b^\top L^{-1}b=\frac{d(n-d)}n.
\]
Consequently \((L'^{-1}\mathbf1)_1-(L^{-1}\mathbf1)_1\) equals the stated rational expression. Its denominator is positive, proving all three sign cases.

For an incident chord \(i=1\), write \(d=k-1\), so \(1\le d\le n-3\) (and \(d\ge2\) for an actual chord). Then
\[
\frac{M(C_n+\{1,k\})-M(C_n)}{M(C_n)}
=\frac{d^2(n-d-2)}{(n-1)[n+d(n-d)]}<1,
\]
because \(d<n-1\) and \(n-d-2<n-d\). If \(k=n-\lfloor\sqrt n\rfloor\), then \(d/n\to1\), \((n-d)/\sqrt n\to1\), and \((n-d-2)/\sqrt n\to1\); the displayed quotient tends to \(1\). Thus the new-to-old mean ratio tends to \(2\), with strict finite-size upper bound \(2\) in this incident-chord family.

## Verification
The standalone `verify_chord_sandpile.py` script uses exact rational Gaussian elimination to compare the formula against the reduced-Laplacian inverse for all \(120\) valid non-sink chords on cycles of size \(4\) through \(11\). Independently, for sizes \(4\) through \(7\), it enumerates every stable configuration, applies the burning test to obtain exactly the recurrent configurations, performs complete grain-addition stabilizations, and compares their exact average toppling counts for all \(20\) chord instances. It also checks the expected number of recurrent states by the spanning-tree count \(n+d(n-d)\) and evaluates the near-doubling sequence at four larger sizes. These finite checks are supplementary, not a replacement for the all-\(n\) proof.

## Relationship to prior work
The finite recurrent-state permutation and burning/spanning-tree facts are standard, reviewed by Járai (2011), and are not claimed as new. Austin et al. (2016), Section 4, explicitly calculate toppling polynomials on **unmodified cycles**, but the inspected cycle results do not give a comparative chord-addition formula, its sign boundary, or its sharp amplification ratio. Eldan, Rácz and Schramm (2015) study an edge-addition paradox for **normalized-Laplacian spectral gaps** in random graphs, not for stationary sandpile avalanche counts. The present computation is an explicit cycle-specific dynamical response to a non-sink edge perturbation, not a claimed new matrix inversion identity or general Green-function theorem.

## Limitations
This establishes an exact first-moment statement, not stochastic dominance of the entire avalanche-size distribution. The factor-two statement concerns only source-incident chords and an asymptotic sequence, not an all-graph optimality theorem. Published general Green-function identities and rank-one inversion make the result derivable by a short but nontrivial specialization; an earlier unindexed derivation or a stronger formula for chorded cycle sandpiles may exist. No independent scientific audit has been performed.

## References
- D. Austin, M. Chambers, R. Funke, L. D. García Puente, and L. Keough, “The Avalanche Polynomial of a Graph,” arXiv:1605.02713v1, first public 2016-05-09, https://arxiv.org/abs/1605.02713 (especially Section 4, cycle toppling polynomials).
- A. A. Járai, “Abelian sandpiles: an overview and results on certain transitive graphs,” arXiv:1106.5358v1, first public 2011-06-27, https://arxiv.org/abs/1106.5358 (finite recurrent dynamics, burning test and stationary measure).
- R. Eldan, M. Z. Rácz, and T. Schramm, “Braess's paradox for the spectral gap in random graphs and delocalization of eigenvectors,” arXiv:1504.07669v1, first public 2015-04-28, https://arxiv.org/abs/1504.07669 (a different edge-addition observable).
