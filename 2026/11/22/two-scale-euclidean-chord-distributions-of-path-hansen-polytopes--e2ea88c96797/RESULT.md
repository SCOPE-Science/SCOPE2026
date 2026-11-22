# Two-scale Euclidean chord distributions of path Hansen polytopes

## Finding

For a path on \(n\) graph vertices, all squared Euclidean distances between distinct vertices of its Hansen polytope are determined by two rational generating functions. Unlike typical distances in an ordinary Fibonacci cube, the complete Hansen vertex set exhibits two distinct macroscopic distance populations. Within each population, the fluctuations are Gaussian with different explicit variances.

Let \(F_0=0,F_1=1,F_{m+2}=F_{m+1}+F_m\). For \(n\ge0\), write \(\mathcal I_n\) for the independent subsets of the path on \(n\) vertices, and set
\[H_n=\operatorname{conv}\{\pm(1,\mathbf1_I):I\in\mathcal I_n\}\subset\mathbb R^{n+1}.\]
Define the finite polynomial over distinct unordered vertex pairs
\[D_n(q)=\sum_{\{u,v\}\subset\operatorname{vert}(H_n)}q^{\|u-v\|_2^2}.\]
Put \(A_n(q)\) and \(B_n(q)\) for the coefficients in
\[\begin{aligned}
\sum_{n\ge0}A_n(q)t^n&=\frac{1+(1+q)t-qt^2}{1-(1+q)t-(1+q)t^2+qt^3},\\
\sum_{n\ge0}B_n(q)t^n&=\frac{1+(q+q^4)t-q^5t^2}{1-(1+q)t-(q+q^4)t^2+q^5t^3}.
\end{aligned}\]
Then the exact chord census, in every dimension, is
\[\boxed{D_n(q)=A_n(q)-F_{n+2}+q^4B_n(q).}\]
The same-sign polynomial \(A_n\) is already known as the ordered Fibonacci-cube Hosoya polynomial [3]; the opposite-sign polynomial \(B_n\), its coupling through the Hansen lift, and the following two-scale Euclidean limit are the contributions.

Let \(Q_n\) be the squared Euclidean distance between two distinct Hansen vertices chosen uniformly without replacement. Then
\[\boxed{\frac{Q_n}{n}\Longrightarrow \frac12\delta_{2/5}+\frac12\delta_{(8-2\sqrt5)/5}.}\]
Conditionally on the signs being equal or opposite, respectively,
\[\begin{aligned}
\frac{Q_n-\frac25n}{\sqrt n}&\Longrightarrow\mathcal N\!\left(0,\frac{14}{25\sqrt5}\right),\\
\frac{Q_n-\frac{8-2\sqrt5}{5}n}{\sqrt n}&\Longrightarrow\mathcal N\!\left(0,\frac{54-8\sqrt5}{25\sqrt5}\right).
\end{aligned}\]
Both sign classes have limiting probability \(1/2\). These are statements about the canonical Euclidean embedding and **all vertex pairs**, not the graph-theoretic edge metric or interior-volume sampling.

## Assumptions and scope

The path has \(n\) labeled vertices in their natural order. A permitted indicator word \(x_1\cdots x_n\) has entries in \(\{0,1\}\) and no consecutive ones. The ambient coordinates \((x_0,x_1,\ldots,x_n)\) use the standard Euclidean inner product, with \(x_0\in\{-1,1\}\) on the vertex set. The formula includes the harmless \(n=0\) base case, where \(H_0\) is a segment; the limit laws concern \(n\to\infty\). All \(2F_{n+2}\) listed points are vertices because the two supporting hyperplanes \(x_0=1\) and \(x_0=-1\) expose copies of a \(0/1\)-polytope, and every distinct \(0/1\) point is extreme.

## Proof

**Distance splitting.** For independent sets \(I,J\), set \(X_i=\mathbf1_{i\in I}\), \(Y_i=\mathbf1_{i\in J}\). Same-sign pairs of vertices have squared chord distance \(\sum_i(X_i-Y_i)^2=|I\triangle J|\). Opposite-sign pairs have distance \(4+\sum_i(X_i+Y_i)^2=4+|I\triangle J|+4|I\cap J|\). Hence, defining
\[A_n(q)=\sum_{I,J\in\mathcal I_n}q^{|I\triangle J|},\quad B_n(q)=\sum_{I,J\in\mathcal I_n}q^{|I\triangle J|+4|I\cap J|},\]
the two sign copies contribute \(A_n-F_{n+2}\) distinct unordered same-sign pairs, and the cross-sign pairs contribute \(q^4B_n\). This proves the displayed expression for \(D_n\) once the generating functions are established. In particular \(D_n(1)=2F_{n+2}^2-F_{n+2}=\binom{2F_{n+2}}2\).

**Exact four-state transfer.** At each coordinate the pair \((X_i,Y_i)\) belongs to the four states \(S=\{00,10,01,11\}\). State \((a,b)\) may precede \((c,d)\) exactly when \(ac=bd=0\). Give the successor state weight \(q^{c\oplus d}\) for \(A_n\), and \(q^{(c\oplus d)+4cd}\) for \(B_n\), where \(\oplus\) is exclusive or. With
\[T_w(q)_{(a,b),(c,d)}=\mathbf1_{ac=bd=0}\,q^{w(c,d)},\qquad v_w(q)_{(a,b)}=q^{w(a,b)},\]
we have \(P_0=1\) and \(P_n=v_w(q)^\mathsf T T_w(q)^{n-1}\mathbf1\) for \(n\ge1\). Direct elimination of four linear state equations gives
\[\sum_{n\ge0}P_n t^n=1+t\,v_w(q)^\mathsf T(I-tT_w(q))^{-1}\mathbf1.\]
For \(w(c,d)=c\oplus d\), its reduced numerator and denominator are \(1+(1+q)t-qt^2\) and \(1-(1+q)t-(1+q)t^2+qt^3\). For \(w(c,d)=c\oplus d+4cd\), they are \(1+(q+q^4)t-q^5t^2\) and \(1-(1+q)t-(q+q^4)t^2+q^5t^3\). The cubic recurrences derived by clearing these denominators establish both identities for all \(n\), without relying on finite enumeration.

**Two Gaussian populations.** A uniformly chosen independent-set word of length \(n\) is the zero-one hard-core model of activity one on a path. In the infinite-volume stationary limit its occupancy probability, occupancy covariance and correlation ratio are
\[p=\frac{5-\sqrt5}{10},\quad v=p(1-p)=\frac15,\quad \rho=\frac{\sqrt5-3}{2}=-\varphi^{-2},\qquad \varphi=\frac{1+\sqrt5}{2},\]
\[\operatorname{Cov}(X_0,X_k)=v\rho^{|k|}.\]
These follow by diagonalizing the positive primitive Fibonacci transfer matrix \(\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\): its Perron eigenvalue is \(\varphi\) and its subleading eigenvalue is \(-\varphi^{-1}\), giving \(\rho=-\varphi^{-2}\). Two independent path words converge in every fixed interior window to independent copies of this chain.

For each position, write centered variables \(u_i=X_i-p\), \(v_i=Y_i-p\), and \(s\in\{-1,+1\}\). The local squared-distance costs are
\[W_{s,i}=(X_i-Y_i)^2\ (s=-1),\qquad W_{s,i}=(X_i+Y_i)^2\ (s=+1).\]
They admit the common centered decomposition
\[W_{s,i}-\mathbb E W_{s,i}=(1+2sp)(u_i+v_i)+2s u_iv_i.\]
Independence between the two words therefore gives, for every integer \(k\),
\[\operatorname{Cov}(W_{s,0},W_{s,k})=\frac25(1+2sp)^2\rho^{|k|}+\frac4{25}\rho^{2|k|}.\]
The local means are \(\mu_-=2p-2p^2=2/5\) and \(\mu_+=2p+2p^2=(8-2\sqrt5)/5\). The two absolutely convergent covariance sums, using \((1+\rho)/(1-\rho)=1/\sqrt5\) and \((1+\rho^2)/(1-\rho^2)=3/\sqrt5\), are
\[\sigma_-^2=\frac{14}{25\sqrt5},\qquad \sigma_+^2=\frac{54-8\sqrt5}{25\sqrt5}.\]
For completeness, the finite-length distribution is a fixed-boundary nonnegative transfer product with a positive primitive matrix at \(q=1\). Its normalized moment generating function has, near zero, the analytic Perron form \(c_s(\theta)[\lambda_s(e^\theta)/\lambda_s(1)]^n(1+O(r^n))\), with \(c_s(0)=1\) and \(0<r<1\). Taylor expansion of the logarithm at \(\theta=0\), with the first two derivatives equal to \(\mu_s\) and \(\sigma_s^2\), proves the two central limit theorems by characteristic functions. The opposite-sign constant \(4\) is negligible after centering and dividing by \(\sqrt n\). The same-sign diagonal exclusion changes the law by exponentially vanishing total variation because \(|\mathcal I_n|=F_{n+2}\) grows exponentially. There are \(F_{n+2}(F_{n+2}-1)\) same-sign and \(F_{n+2}^2\) opposite-sign unordered pairs. Consequently both probabilities tend to \(1/2\), proving the two-atom limit and the conditional Gaussian laws.

## Verification

The accompanying portable \(check_hansen.py\) independently constructs the vertex set and its full pairwise squared-distance histogram for each \(0\le n\le12\); it checks every coefficient against both an independent four-state transfer and the two cubic recurrences and checks the total pair count. It also checks the conditional mean and variance per coordinate at lengths \(50\), \(100\), and \(200\) against the claimed asymptotic constants using exact-integer moment transfers. Running \(python3\ check_hansen.py\) yielded `HANSEN_PATH_CHORD_PASS`. The infinite-family polynomial identity and limit laws are proved above, not inferred from the finite checks.

## Relationship to prior work

Hansen polytopes were introduced in 1977; Freij–Henze–Schmitt–Ziegler [1] supply the canonical twisted-prism vertex description. The 2017 daisy-cube metric paper [2] treats the Fibonacci cube as a graph and counts induced cubes at given graph distances, rather than squared Euclidean chords in its Hansen lift. Klavžar–Mollard [3], Theorem 4.1, **already proves exactly the \(A_n\) generating function** as the ordered Hosoya polynomial of the Fibonacci cube; no originality is claimed for that part or for its mean \(2/5\). Aliniaeifard and coauthors [4] characterize stable-set-polytope one-skeleton distances, which again are not the full cross-sign chord distribution. The difference is mathematical: an opposite-sign chord weights simultaneous occupancy by four, creating a second rational polynomial and a macroscopically separated Gaussian branch. Related calculations for complete-bipartite Hansen polytopes concern a different graph class and their **polytope edges**, not all pairs of path Hansen vertices.

## Limitations

All results concern the exact canonical coordinates specified above; arbitrary affine images do not preserve the Euclidean conclusions. The result does not classify polytope edges, intrinsic volumes, or graph families beyond paths. The two Gaussian limits are conditional, not a single globally centered Gaussian law. The existing Fibonacci-cube Hosoya result is explicitly excluded from the novelty claim. Priority searches cannot rule out every unindexed equivalent formula for the weighted opposite-sign transfer; no independent mathematical audit is asserted.

## References

1. R. Freij, M. Henze, M. W. Schmitt, G. M. Ziegler, *Face numbers of centrally symmetric polytopes from split graphs*, arXiv:1201.5790 (first posted 2012-01-27), especially Section 2 and Lemma 2.4; original Hansen construction (1977).
2. S. Klavžar and M. Mollard, *Daisy cubes and distance cube polynomial*, arXiv:1705.08674 (first posted 2017-05-24), Sections 2–3.
3. S. Klavžar and M. Mollard, *Wiener index and Hosoya polynomial of Fibonacci and Lucas cubes*, MATCH Commun. Math. Comput. Chem. **68** (2012), 311–324, especially Theorem 4.1; https://users.fmf.uni-lj.si/klavzar/preprints/MATCH68%281%29_311-324.pdf.
4. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (first posted 2018-04-02).
