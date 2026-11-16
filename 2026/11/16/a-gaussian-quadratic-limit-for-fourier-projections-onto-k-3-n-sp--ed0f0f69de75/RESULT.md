# A Gaussian quadratic limit for Fourier projections onto \(K_{3,n}\) spanning trees

## Finding
For each integer \(n\ge2\), let \(G_n=\mathbb F_2^{E(K_{3,n})}=\mathbb F_2^{3n}\), with edges indexed by the three left vertices and \(n\) right vertices. Let \(\mathcal T_n\subseteq G_n\) consist of the indicator vectors of all spanning trees. The Fourier projection onto \(\mathcal T_n\), denoted \(P_n\), has sharp endpoint norm
\[
\boxed{\displaystyle
\|P_n\|_{\ell^1\to\ell^1}
=\|P_n\|_{\ell^\infty\to\ell^\infty}
=n(3/2)^n\left(\frac{2\sqrt2-1}{3}+o(1)\right).}
\]
In addition, the following is an **exact finite-parameter identity**, not merely an asymptotic. Define \(\Phi(x,y,z)=xy+xz+yz\). Let the independent random vectors \(X_i\in\mathbb R^3\) each have distribution
\[
\begin{array}{c|c}
\text{vector}&\text{probability per vector}\\\hline
\pm(1/3,1/3,1/3)&1/4\\
\pm(1,-1,-1),\ \pm(-1,1,-1),\ \pm(-1,-1,1)&1/12.
\end{array}
\]
Then
\[
\boxed{\displaystyle\|P_n\|_{\ell^1\to\ell^1}
=(3/2)^n\,\mathbb E\left|\Phi(X_1+\cdots+X_n)\right|.}
\]
Here a pair of signs denotes two distinct vectors; there are exactly eight possibilities and the probabilities sum to one.

## Assumptions and scope
All groups and characters are binary and all normed spaces are complex-valued functions with counting-measure \(\ell^1\) or \(\ell^\infty\) norms. The Fourier characters are \(\chi_t(x)=(-1)^{\langle t,x\rangle}\). The unnormalized Walsh transform of the tree indicator at \(y\in G_n\) is
\[
W_n(y)=\sum_{t\in\mathcal T_n}(-1)^{\langle y,t\rangle}.
\]
The projection is convolution by \(K_n(y)=2^{-3n}W_n(y)\); no probability measure is inserted in the definition of the projection itself. For a translation-invariant convolution on a finite group, both endpoint norms equal the sum of the absolute values of its kernel. The \(\ell^1\) equality is attained on a delta mass; the \(\ell^\infty\) equality is attained by phase alignment against one kernel row. The theorem covers every integer \(n\ge2\), with a limit as \(n\to\infty\), and claims no effective convergence rate.

## Proof
**1. Signed spanning-tree identity.** Fix a sign assignment on the \(3n\) edges and write \((a_i,b_i,c_i)\in\{\pm1\}^3\) for the three edges at right vertex \(i\). Put
\[
s_i=a_i+b_i+c_i,\qquad
v_i=\left(\frac{a_ib_i}{s_i},\frac{a_ic_i}{s_i},\frac{b_ic_i}{s_i}\right).
\]
Each \(s_i\) is one of \(\pm1,\pm3\), hence is nonzero. Every spanning tree has \(n+2\) edges. Each right vertex has degree at least one, so precisely two edges are present in excess of one per right vertex. Thus either one right vertex has degree three and all others degree one, or two right vertices have degree two and the others degree one. In the latter case, the two degree-two vertices must connect different pairs of left vertices: equal pairs leave the third left vertex disconnected.

For a single degree-three vertex \(i\), the signed contribution is \(a_ib_ic_i\prod_{h\ne i}s_h\). For degree-two vertices \(i<j\), there are six choices of distinct pair-types from \(\{ab,ac,bc\}\), with signed contribution given by their products times \(\prod_{h\ne i,j}s_h\). On expanding \(\Phi(\sum_i v_i)\) and multiplying by \(\prod_i s_i\), the cross terms are exactly these six choices. For each diagonal term,
\[
\Phi(v_i)=\frac{a_ib_i+a_ic_i+b_ic_i}{s_i^2}
=\frac{a_ib_ic_i}{s_i},
\]
where the last equality follows from \(a_i^2=b_i^2=c_i^2=1\). This proves the exact identity
\[
\boxed{W_n(a,b,c)=\left(\prod_{i=1}^n s_i\right)
\Phi\left(\sum_{i=1}^n v_i\right).}
\]
Setting all signs equal to one also recovers the known tree count \(|\mathcal T_n|=n^2 3^{n-1}\), consistent with the general complete-bipartite spanning-tree formula.

**2. Absolute-value change of measure.** A uniformly random Walsh frequency makes the triples \((a_i,b_i,c_i)\) independent and uniform in \(\{\pm1\}^3\). Since \(\mathbb E_0|s_i|=\frac18(2\cdot3+6\cdot1)=3/2\), define the tilted single-column law
\[
\mathbb P_*(a,b,c)=\frac{|a+b+c|}{12}.
\]
The identity in step 1 and the positive weights give exactly
\[
2^{-3n}\sum_y|W_n(y)|
=(3/2)^n\mathbb E_*\left|\Phi\left(\sum_i X_i\right)\right|,
\qquad X_i=v_i.
\]
The eight sign triples produce the eight stated values of \(X_i\). Specifically, each of the two all-equal triples has weight \(3/12\), and each of the six other triples weight \(1/12\). This proves the finite-parameter identity and sharpness of both endpoint norms.

**3. Covariance and central limit.** The distribution is symmetric under \(X\mapsto-X\), so \(\mathbb E_*X=0\). Directly summing the eight outcomes yields
\[
\Sigma=\mathbb E_*(XX^{\mathsf T})
=\begin{pmatrix}
5/9&-1/9&-1/9\\
-1/9&5/9&-1/9\\
-1/9&-1/9&5/9
\end{pmatrix}
=\frac23 I_3-\frac19 J_3.
\]
The variance in the normalized all-ones direction is \(1/3\), and in the orthogonal plane each variance is \(2/3\). By the ordinary multivariate central limit theorem,
\[
\frac1{\sqrt n}\sum_{i=1}^n X_i\ \Rightarrow\ Z\sim N(0,\Sigma).
\]
The polynomial \(\Phi\) is homogeneous of degree two. Since \(|\Phi(x)|\le\|x\|_2^2\) and the independent summands are bounded and centered, \(\sup_n\mathbb E\|n^{-1/2}\sum_iX_i\|_2^4<\infty\). Consequently the sequence \(|\Phi(n^{-1/2}\sum_iX_i)|\) is uniformly integrable. Thus convergence in distribution upgrades to convergence of these expectations:
\[
\lim_{n\to\infty}\frac{\|P_n\|}{n(3/2)^n}=\mathbb E|\Phi(Z)|.
\]

**4. Gaussian integral.** In the orthonormal eigenbasis of \(\Sigma\), let \(N_0,N_1,N_2\) be independent standard real normals. Using \(\Phi(x)=\frac12((x_1+x_2+x_3)^2-\|x\|_2^2)\) gives
\[
\Phi(Z)=\frac13\left(N_0^2-N_1^2-N_2^2\right).
\]
Put \(A=N_0^2\) and \(B=N_1^2+N_2^2\). They are independent chi-square variables with degrees of freedom one and two. The total \(A+B\) has expectation three, and the independent ratio \(A/(A+B)\) has the beta distribution with parameters \((1/2,1)\), which is the distribution of \(U^2\) for \(U\) uniform on \([0,1]\). Therefore
\[
\begin{aligned}
\mathbb E|\Phi(Z)|
&=\tfrac13\mathbb E(A+B)\,\mathbb E\left|2\frac{A}{A+B}-1\right|\\
&=\int_0^1|2u^2-1|\,du
=\frac{2\sqrt2-1}{3}.
\end{aligned}
\]
This proves the asserted asymptotic and all normalization claims.

## Verification
The accompanying standalone Python program `check_k3n.py` uses only the standard library. It independently enumerates every spanning tree and computes every Walsh coefficient for \(1\le n\le5\); verifies both the degree-classification signed tree formula and the exact rational Schur formula for each sign assignment; and compares the resulting sharp norm with a separate integer-weighted three-dimensional walk computation. It propagates the tilted walk exactly through \(n=16\) and verifies the covariance matrix. Complete checks cover \(8+64+512+4096+32768=37448\) Walsh frequencies. Run `python3 check_k3n.py` from the extracted package directory. Expected concluding marker: `K3N_SIGNED_TREE_FOURIER_AND_TILT_DP_PASS`. These finite tests are corroboration, not an infinite proof.

## Relationship to prior work
Goodall's *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis* (public arXiv version June 30, 2008) establishes finite Fourier methods for graphical invariants, notably Tutte-polynomial weight enumerators and Fourier \(\ell^2\) relationships; it does not state this signed-tree \(\ell^1\) asymptotic. Dall and Pfeifle's *A Polyhedral Proof of the Matrix Tree Theorem* (April 15, 2014 preprint) treats weighted graphical and regular-matroid tree enumeration, a general algebraic antecedent to the signed polynomial identity; it does not evaluate the random-sign absolute first moment or the Gaussian quadratic constant. The current argument uses a direct combinatorial tree-degree expansion and computes a new endpoint invariant for the specific fixed-side complete-bipartite family. Classical tree counts and Fourier second moments alone do not determine the absolute first moment.

## Limitations
The result is an asymptotic for the fixed three-vertex side only. It asserts neither an all-\(n\) elementary closed form for the norm nor an error rate. The finite computations are not substituted for the central-limit and uniform-integrability argument. Historical priority is based on a bounded literature comparison; an unindexed earlier signed-tree \(\ell^1\) calculation could overlap. Independent mathematical review has not been performed.

## References
1. Andrew Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848v1 (first submitted June 30, 2008), https://arxiv.org/abs/0806.4848.
2. Aaron Dall and Julian Pfeifle, *A Polyhedral Proof of the Matrix Tree Theorem*, arXiv:1404.3876 (initial version April 15, 2014), https://arxiv.org/abs/1404.3876.
