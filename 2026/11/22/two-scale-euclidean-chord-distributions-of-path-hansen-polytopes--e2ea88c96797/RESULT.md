# Two-scale Euclidean chord distributions of path Hansen polytopes

## Finding

The squared Euclidean chord lengths of a path Hansen polytope split into two positive-mass populations with different linear centers and different Gaussian fluctuation variances. These populations arise from sampling a pair of vertices with the same or opposite signs in the canonical Hansen realization. We state the finite enumerators as inputs to the limit theorem: both are specializations of a known endpoint-weight/Hamming enumerator, not new counting formulas.

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
Here \(A_n\) is the ordered Fibonacci-cube Hosoya polynomial [3]. Both \(A_n\) and \(B_n\) follow from Khan's endpoint-weight refinement [5] by the substitutions given in the proof. The finite census fixes the normalizations for the two conditional laws below; the contribution is the asymptotic separation and its fluctuation constants in the Hansen realization.

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

**Specialization of the known pair enumerator.** Let
\[
P_n(a,b,x)=\sum_{I,J\in\mathcal I_n}a^{|I|}b^{|J|}x^{|I\triangle J|}.
\]
Theorem 7.1 of [5] gives
\[
\sum_{n\ge0}P_n(a,b,x)t^n=
\frac{1+(ax+bx+ab)t+abx^2t^2-a^2b^2x^2t^3}
     {1-t-(abx^2+ab+ax+bx)t^2-abx^2t^3+a^2b^2x^2t^4}.
\]
Thus \(A_n(q)=P_n(1,1,q)\) and \(B_n(q)=P_n(q^2,q^2,q^{-1})\), using \(2|I|+2|J|-|I\triangle J|=|I\triangle J|+4|I\cap J|\). In either case numerator and denominator have a common factor \(1+qt\); cancellation gives the displayed rational formulas. The second substitution is taken formally for nonzero \(q\), and the paired word weights are polynomials in \(q\), so the result includes evaluation at \(q=0\).

**Transfer matrix for the limit laws.** At each coordinate the pair \((X_i,Y_i)\) belongs to the four states \(S=\{00,10,01,11\}\). State \((a,b)\) may precede \((c,d)\) exactly when \(ac=bd=0\). Give the successor state weight \(q^{c\oplus d}\) for \(A_n\), and \(q^{(c\oplus d)+4cd}\) for \(B_n\), where \(\oplus\) is exclusive or. With
\[T_w(q)_{(a,b),(c,d)}=\mathbf1_{ac=bd=0}\,q^{w(c,d)},\qquad v_w(q)_{(a,b)}=q^{w(a,b)},\]
the corresponding one-variable enumerator \(A_n(q)\) or \(B_n(q)\) is \(v_w(q)^\mathsf T T_w(q)^{n-1}\mathbf1\) for \(n\ge1\). At \(q=1\), \(T_w\) is the product of the two identical Fibonacci transfer matrices and is primitive: every state can reach every other state in two steps through \(00\).

**Two Gaussian populations.** A uniformly chosen independent-set word of length \(n\) is the zero-one hard-core model of activity one on a path. In the infinite-volume stationary limit its occupancy probability, occupancy covariance and correlation ratio are
\[p=\frac{5-\sqrt5}{10},\quad v=p(1-p)=\frac15,\quad \rho=\frac{\sqrt5-3}{2}=-\varphi^{-2},\qquad \varphi=\frac{1+\sqrt5}{2},\]
\[\operatorname{Cov}(X_0,X_k)=v\rho^{|k|}.\]
These follow by diagonalizing the primitive Fibonacci transfer matrix \(\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\): its Perron eigenvalue is \(\varphi\) and its subleading eigenvalue is \(-\varphi^{-1}\), giving \(\rho=-\varphi^{-2}\). Two independent path words converge in every fixed interior window, with distance to both boundaries tending to infinity, to independent copies of this chain.

For each position, write centered variables \(u_i=X_i-p\), \(v_i=Y_i-p\), and \(s\in\{-1,+1\}\). The local squared-distance costs are
\[W_{s,i}=(X_i-Y_i)^2\ (s=-1),\qquad W_{s,i}=(X_i+Y_i)^2\ (s=+1).\]
They admit the common centered decomposition
\[W_{s,i}-\mathbb E W_{s,i}=(1+2sp)(u_i+v_i)+2s u_iv_i.\]
Independence between the two words therefore gives, for every integer \(k\),
\[\operatorname{Cov}(W_{s,0},W_{s,k})=\frac25(1+2sp)^2\rho^{|k|}+\frac4{25}\rho^{2|k|}.\]
The local means are \(\mu_-=2p-2p^2=2/5\) and \(\mu_+=2p+2p^2=(8-2\sqrt5)/5\). The two absolutely convergent covariance sums, using \((1+\rho)/(1-\rho)=1/\sqrt5\) and \((1+\rho^2)/(1-\rho^2)=3/\sqrt5\), are
\[\sigma_-^2=\frac{14}{25\sqrt5},\qquad \sigma_+^2=\frac{54-8\sqrt5}{25\sqrt5}.\]
The finite-word moment generating function from the transfer matrix has, near zero, the analytic Perron form \(c_s(\theta)[\lambda_s(e^\theta)/\lambda_s(1)]^n(1+O(r^n))\), with \(c_s(0)=1\) and \(0<r<1\), uniformly in a sufficiently small complex neighborhood of zero. This follows from the simple separated Perron eigenvalue and positivity of its weight at zero. The stationary pair chain has the same limiting log moment generating function per coordinate: tilting its transitions by \(e^{\theta w}\) gives a matrix diagonally similar to \(T_w(e^\theta)/\lambda_s(1)\), using the positive right Perron vector of \(T_w(1)\). Only the boundary vectors differ. Differentiating the analytic Perron form for this stationary chain gives the limiting first two cumulants per coordinate, which equal \(\mu_s\) and the absolutely summable covariance rate \(\sigma_s^2\) computed above. Taylor expansion at \(\theta=0\) then proves the two finite-word central limit theorems by characteristic functions. The opposite-sign constant \(4\) is negligible after centering and dividing by \(\sqrt n\). The same-sign diagonal exclusion changes the law by exponentially vanishing total variation because \(|\mathcal I_n|=F_{n+2}\) grows exponentially. There are \(F_{n+2}(F_{n+2}-1)\) same-sign and \(F_{n+2}^2\) opposite-sign unordered pairs. Consequently both probabilities tend to \(1/2\), proving the two-atom limit and the conditional Gaussian laws.

## Verification

The accompanying portable \(check_hansen.py\) independently constructs the vertex set and its full pairwise squared-distance histogram for each \(0\le n\le12\); it checks every coefficient against both an independent four-state transfer and the two cubic recurrences and checks the total pair count. It also checks the conditional mean and variance per coordinate at lengths \(50\), \(100\), and \(200\) against the claimed asymptotic constants using exact-integer moment transfers. Running \(python3\ check_hansen.py\) yielded `HANSEN_PATH_CHORD_PASS`. The infinite-family polynomial identity and limit laws are proved above, not inferred from the finite checks.

## Relationship to prior work

Freij–Henze–Schmitt–Ziegler [1] supply the canonical twisted-prism vertex description. The daisy-cube metric paper [2] studies graph distance, and Aliniaeifard and coauthors [4] study the one-skeleton of stable-set polytopes. Klavžar–Mollard [3], Theorem 4.1, gives the exact same-sign generating function. Khan [5], Theorem 7.1, also gives the stronger finite enumerator from which the opposite-sign formula and full finite census follow by substitution. Accordingly the present result does not claim a new finite enumeration, nor novelty for ordinary Fibonacci-cube distance moments. Its focus is the Euclidean sign mixture and the explicitly separated conditional fluctuations in the Hansen lift: same-sign chords measure disagreement, while opposite-sign chords give four units of squared distance to simultaneous occupancy.

## Limitations

All results concern the exact canonical coordinates specified above; arbitrary affine images do not preserve the Euclidean conclusions. The result does not classify polytope edges, intrinsic volumes, or graph families beyond paths. The two Gaussian limits are conditional, not a single globally centered Gaussian law. The finite enumerator and its two specializations are credited above. Historical priority for the asymptotic result is not asserted exhaustively; asymptotic analyses of weighted Fibonacci-word pair enumerators could yield related constants.

## References

1. R. Freij, M. Henze, M. W. Schmitt, G. M. Ziegler, *Face numbers of centrally symmetric polytopes from split graphs*, arXiv:1201.5790 (first posted 2012-01-27), especially Section 2 and Lemma 2.4; original Hansen construction (1977).
2. S. Klavžar and M. Mollard, *Daisy cubes and distance cube polynomial*, arXiv:1705.08674 (first posted 2017-05-24), Sections 2–3.
3. S. Klavžar and M. Mollard, *Wiener index and Hosoya polynomial of Fibonacci and Lucas cubes*, MATCH Commun. Math. Comput. Chem. **68** (2012), 311–324, especially Theorem 4.1; https://users.fmf.uni-lj.si/klavzar/preprints/MATCH68%281%29_311-324.pdf.
4. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (first posted 2018-04-02).
5. Ali Ejaz Khan, *Fixed-Weight Hamming Distance Distributions of Fibonacci Strings*, Mathematical Reflections 6 (2026), Theorem 7.1 and Proposition 7.4, https://www.awesomemath.org/wp-pdf-files/math-reflections/mr-2026-06/mr_6_2026_hamming_distance_fibonacci_distributions.pdf.
