# Semicircular matching cuts have an exact cyclic Green spectrum and a five-orientation crossover

## Finding

Fix an integer \(m\ge2\). Pair the \(2m\) clockwise labeled vertices of a circle uniformly at random into \(m\) chords. For every \(i\in\mathbb Z/(2m\mathbb Z)\), put
\[
 A_i=\{i,i+1,\ldots,i+m-1\}\pmod {2m},\qquad
 X_i=\#\{\{u,v\}\text{ in the matching}:|\{u,v\}\cap A_i|=1\}.
\]
The observation \(X_i\) counts chords joining the two halves of the circle at orientation \(i\). Since \(X_{i+m}=X_i\) identically, retain the \(m\)-component observation vector \(X=(X_0,\ldots,X_{m-1})\) and its covariance matrix \(K_m\). Define
\[
 \gamma_m=\frac{2m-2}{(2m-1)(2m-3)},\qquad
 h_m=\frac{(m-1)(m^2-m+1)}{3(2m-1)}.
\]
Then the exact means and covariance entries, for all \(i,j\in\{0,\ldots,m-1\}\), are
\[
 \mathbb E X_i=\frac{m^2}{2m-1},\qquad
 (K_m)_{ij}=\gamma_m\left(d^2+(m-d)^2-\frac{m^3}{2m-1}\right),\quad d=|i-j|.
\]
The matrix is circulant, positive definite, and has the **complete Fourier spectrum**
\[
 \boxed{\Lambda_{m,0}=\gamma_m m h_m,\qquad
 \Lambda_{m,j}=\gamma_m m\,\csc^2\!\left(\frac{\pi j}{m}\right)\quad(1\le j<m).}
\]
In particular, the covariance of the original \(2m\) observations has rank exactly \(m\), with all \(m\) complementary-half redundancies and no others.

There is also a **local precision representation**. Let \(L_m\) be the (undirected) cycle Laplacian with eigenvalues \(4\sin^2(\pi j/m)\); at \(m=2\), the cycle consists of two parallel edges, so \(L_2=\bigl(\begin{smallmatrix}2&-2\\-2&2\end{smallmatrix}\bigr)\). Let \(P_0=\mathbf1\mathbf1^{\mathsf T}/m\). Then
\[
 \boxed{K_m^{-1}=\frac{L_m}{4\gamma_m m}+\frac{P_0}{\gamma_m m h_m}.}
\]
Thus the only nonlocal precision correction is rank one, on the constant Fourier channel.

The strongest observation mode changes **exactly at five distinct orientations**: for \(2\le m\le4\), a first nonconstant Fourier character maximizes the variance, whereas for every \(m\ge5\) the constant character uniquely maximizes it. For \(m\le3\), the constant character minimizes the positive variance; for \(m\ge4\), the minimizers are precisely the characters nearest the alternating frequency. Writing \(\kappa_m=\lambda_{\max}(K_m)/\lambda_{\min}(K_m)\), one has the **sharp all-size condition ratio**
\[
 \boxed{\kappa_m=\begin{cases}
 3,&m=2,\\10/7,&m=3,\\2,&m=4,\\
 h_m\sin^2\!\left(\pi\lfloor m/2\rfloor/m\right),&m\ge5,
 \end{cases}\qquad
 \lim_{m\to\infty}\frac{\kappa_m}{m^2}=\frac16.}
\]
The result concerns the Euclidean covariance spectrum, not a normalized correlation matrix.

## Assumptions and scope

All \((2m-1)!!\) perfect matchings on the **fixed labeled endpoint set** are equally likely; no independence is assumed between different chords. The two halves are the equal consecutive cyclic vertex arcs specified above. Every cut-chord crossing is counted once; it need not be a geometric intersection of two chords. The independent observation set has exactly \(m\) orientations because reversing the two sides does not change the count. The Fourier transform uses the unnormalized circulant eigenvalue convention: an eigenvalue is the sum of covariance-row entries weighted by the corresponding character, with no division by \(m\). All finite formulas hold for integer \(m\ge2\).

## Proof

**1. Pair-indicator covariance becomes scalar on a degree-zero edge space.** Put \(N=2m\), and let \(I_e\) be the indicator that unordered vertex pair \(e\) belongs to the random matching. Directly fixing one edge, or two disjoint edges, gives
\[
 p=\mathbb EI_e=\frac1{N-1},\qquad
 q=\mathbb E(I_eI_f)=\frac1{(N-1)(N-3)}\quad(e\cap f=\varnothing);
\]
for distinct incident edges the joint expectation is zero. Denote by \(A\) the adjacency matrix of the line graph of the complete graph on \(N\) vertices and by \(J\) its all-ones matrix. The edge-indicator covariance is
\[
 \Sigma=(p-q)I-qA+(q-p^2)J.
\]
For each cut, let \(c_i(e)\in\{0,1\}\) indicate that candidate edge \(e\) crosses the cut. Each vertex has exactly \(m\) potential neighbors across a semicircle, hence
\[
 v_i(e)=c_i(e)-\frac{m}{N-1}
\]
satisfies \(\sum_{e\ni u}v_i(e)=0\) for every vertex \(u\), and \(\sum_e v_i(e)=0\). The unsigned vertex-edge incidence identity \(B^{\mathsf T}B=2I+A\) now implies \(Av_i=-2v_i\), while \(Jv_i=0\). Therefore
\[
 \Sigma v_i=(p+q)v_i=\gamma_m v_i,
 \qquad \operatorname{Cov}(X_i,X_j)=\gamma_m\langle v_i,v_j\rangle,
\]
where adding the constant shift in \(\langle v_i,I\rangle\) does not affect covariance. This also verifies the stated value of \(\gamma_m\).

**2. Two-cut geometry.** A fixed semicircle has \(m^2\) potential crossing edges, and therefore \(\mathbb EX_i=m^2p\). When two semicircle starts are separated by \(d\in\{0,\ldots,m-1\}\), the four blocks cut out by their endpoints have respective sizes \(m-d,d,m-d,d\). A potential edge crosses *both* cuts iff its endpoints belong to the opposing blocks of sizes \(m-d,m-d\) or \(d,d\); hence \(\langle c_i,c_j\rangle=(m-d)^2+d^2\). Since \(\#E(K_{2m})=m(2m-1)\) and \(\sum_e c_i(e)=m^2\), centering yields
\[
 \langle v_i,v_j\rangle=d^2+(m-d)^2-\frac{m^3}{2m-1}.
\]
This proves the exact covariance. The displayed function is unchanged under replacing \(d\) by \(m-d\), so it defines a circulant matrix.

**3. Exact cyclic Fourier transform.** Let \(z=\exp(-2\pi i j/m)\), \(1\le j<m\). Differentiating the finite geometric sum twice and substituting \(z^m=1\), \(z\ne1\), gives the finite identity
\[
 \sum_{d=0}^{m-1}d(m-d)z^d=\frac{2mz}{(1-z)^2}.
\]
The nonconstant transform of \(d^2+(m-d)^2=m^2-2d(m-d)\) is consequently
\[
 -\frac{4mz}{(1-z)^2}=m\csc^2(\pi j/m).
\]
For \(j=0\), using \(\sum_{d=0}^{m-1}d(m-d)=m(m^2-1)/6\), the centered row sum is
\[
 \sum_{d=0}^{m-1}\left[d^2+(m-d)^2-\frac{m^3}{2m-1}\right]
 =\frac{m(m-1)(m^2-m+1)}{3(2m-1)}=m h_m.
\]
Multiplying by \(\gamma_m\) proves every eigenvalue. Because \(\gamma_m,h_m\) and every squared cosecant are positive, \(K_m\) has full rank. Identical opposite observations form a two-block duplication matrix, with spectrum consisting of \(2\Lambda_{m,j}\) and \(m\) additional zeros; hence its rank is exactly \(m\).

**4. Precision and exact extremizers.** The cycle Laplacian has Fourier eigenvalue \(4\sin^2(\pi j/m)\); it vanishes precisely on the constants, whereas \(P_0\) is identity on that channel and zero elsewhere. Their stated linear combination therefore has eigenvalues \(1/\Lambda_{m,j}\), including at \(m=2\), proving the inverse formula.

Among nonconstant Fourier characters, \(\csc^2(\pi j/m)\) is strictly largest at \(j=1,m-1\) (only one character at \(m=2\)) and strictly smallest at \(j=\lfloor m/2\rfloor\) and, when distinct, \(j=\lceil m/2\rceil\). To compare with the constant mode, note the strictly positive derivatives, for real \(t\ge4\),
\[
 \frac{d}{dt}h_t=\frac{t(4t^2-7t+4)}{3(2t-1)^2}>0,
 \quad
 \frac{d}{dt}\frac{h_t}{t^2}
 =\frac{3t^3-8t^2+8t-2}{3t^3(2t-1)^2}>0.
\]
Here \(h_t=(t-1)(t^2-t+1)/[3(2t-1)]\). Thus for \(m\ge4\), \(h_m\ge h_4=13/7>\sec^2(\pi/8)\ge \min_{j\ne0}\csc^2(\pi j/m)\); the right inequality follows because the frequency nearest \(m/2\) differs from it by at most one half and \(m\ge4\). The constant mode is therefore not a minimizer for \(m\ge4\). Direct evaluation gives \(h_2=1/3\), \(h_3=14/15\) and the asserted small-size minima.

It remains to compare the constant mode to the *largest* nonconstant eigenvalue. Direct checks at \(m=2,3,4\) give \(h_m<\csc^2(\pi/m)\). At \(m=5\), \(h_5=28/9\), and
\[
 h_5\sin^2(\pi/5)=\frac{7(5-\sqrt5)}{18}>1.
\]
For \(t\ge5\), both \(h_t/t^2\) and \(t\sin(\pi/t)\) are strictly increasing; for the second, differentiating yields \(\sin u-u\cos u>0\) with \(u=\pi/t\). Their product squared gives \(h_t\sin^2(\pi/t)\), which is therefore greater than one at every integer \(m\ge5\). This proves the unique constant-mode maximum there. Combining maximum and minimum eigenvalues gives all four condition-ratio cases. Finally \(h_m/m^2\to1/6\) and \(\sin(\pi\lfloor m/2\rfloor/m)^2\to1\), proving the sharp limiting coefficient. \(\square\)

## Verification

The standalone `verify.py` uses only the Python 3 standard library. It enumerates *every* pairing for \(m=2,3,4,5,6,7\), respectively \(3,15,105,945,10395,135135\) matchings; directly computes each orientation's chord-cut count; and checks the complete exact-rational mean/covariance entries, totaling **7,021,287** matching-by-matrix-cell comparisons. It multiplies the conjectured exact inverse by the covariance over rational numbers for every \(2\le m\le17\), testing **1,784** entries. It also checks the claimed Fourier extrema and exact condition-number formulas for all \(2\le m<500\). The script prints `All checks passed.` on success. None of these finite checks replaces the general argument in the Proof section.

## Relationship to prior work

Paguyo (2021) studies the same uniform chord-diagram ensemble but proves normal and Poisson approximation bounds for **global chord crossings** and **simple-chord counts**; its three principal theorems do not assert spatial semicircle-cut covariances or Fourier conditioning. Acan (2015) studies random chord intersection graphs and chord-degree statistics. Those statistics are not the cut-crossing process defined here. The established result *Exact crossing-cut Green kernel and Gaussian bridge for uniform pairings* analyzes counts of chords exiting **nested prefixes** and their nonstationary Green covariance; it does not derive the **rotating equal-half cut** circulant spectrum, its inverse, or its five-orientation extremal crossover. The established result *Exact two-mode covariance spectrum of circular chord-length histograms* concerns counts classified by **chord length**, not by cut orientation. All these works inform or overlap the elementary matching-indicator input, which is not claimed as new. The evaluated contribution is the complete specialized cyclic Green/precision theorem and its sharp global extremizer classification.

## Limitations

The ensemble consists only of uniformly weighted perfect matchings on a fixed even number of labeled circle points. The formulas concern second moments and Euclidean linear reconstruction, not joint Gaussianity, nonlinear identification, arbitrary asymmetric arcs, nonuniform matching weights or the geometry of literal intersecting chords. There may be an earlier general fixed-matching incidence/association-scheme identity or a specialized cut-process treatment from which the theorem follows; historical priority has not been independently confirmed. The sharp cutoff is a statement about this natural semicircle observation family, not about all possible sampling windows.

## References

1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first publicly posted 2021-04-02. https://arxiv.org/abs/2104.01134. Sections 1–3.
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first publicly posted 2015-01-07. https://arxiv.org/abs/1501.01489.
3. *Exact crossing-cut Green kernel and Gaussian bridge for uniform pairings*, public published-finding corpus finding dated 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-crossing-cut-green-kernel-and-gaussian-bridge-for-uniform--1361e88632a1.
4. *Exact two-mode covariance spectrum of circular chord-length histograms*, public published-finding corpus finding dated 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-two-mode-covariance-spectrum-of-circular-chord-length-hist--6e004b32ef71.
