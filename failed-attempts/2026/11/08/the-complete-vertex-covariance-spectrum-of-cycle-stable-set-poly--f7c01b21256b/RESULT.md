# The complete vertex-covariance spectrum of cycle stable-set polytopes

## Finding

For every integer \(n\ge3\), let \(C_n\) be the simple cycle with vertices indexed modulo \(n\), and let
\[
 P_n=\operatorname{conv}\{\mathbf1_I\in\mathbb R^n:I\subseteq\mathbb Z/n\mathbb Z\text{ contains no adjacent pair}\}.
\]
Let \(X_n\) be uniformly distributed over the **distinct vertices** of \(P_n\) (not uniformly distributed by volume). Put
\[
 r=\frac{\sqrt5-3}{2}\in(-1,0),\qquad w_n=r^n,\qquad \theta_j=\frac{2\pi j}{n}.
\]
Then the exact covariance eigenvalues in the discrete Fourier modes \(j=0,\ldots,n-1\) are
\[
 \boxed{\lambda_0(n)=\frac{1-w_n}{5\sqrt5(1+w_n)}+\frac{n w_n}{5(1+w_n)^2}},
\]
\[
 \boxed{\lambda_j(n)=\frac{(1-r^2)(1-w_n)}{5(1+w_n)(1-2r\cos\theta_j+r^2)}}\quad(1\le j<n).
\]
In particular, **the unique smallest eigenspace is always the span of the all-ones vector**. The largest eigenspace is the alternating line for even \(n\), and the two-dimensional real space spanned by the highest-frequency sine and cosine modes for odd \(n\). All eigenvalues are strictly positive and the Euclidean covariance condition number satisfies
\[
 \boxed{\lim_{n\to\infty}\frac{\lambda_{\max}(n)}{\lambda_{\min}(n)}=5.}
\]
The multiplicity of each other real eigenvalue is two except the alternating mode for even \(n\), which has multiplicity one.

## Assumptions and scope

The canonical embedding is in \(\mathbb R^n\), with the standard Euclidean metric and with no rescaling or translation prior to computing covariance (translations do not alter covariance). Every stable-set indicator is a vertex: a \(0/1\) point cannot be a nontrivial convex combination of distinct \(0/1\) points. This measure is therefore exactly uniform over all independent sets of the cycle. The theorem applies to all integers \(n\ge3\). It does not concern the continuous uniform-volume measure or fractional stable-set polytope.

## Proof

**1. Vertex counts and the moment kernel.** Write \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\) and extend to \(F_{-1}=1\). The number of stable sets of \(C_n\) equals the Lucas number \(L_n=F_{n-1}+F_{n+1}\). This follows by the transfer matrix \(T_z=\bigl(\begin{smallmatrix}1&z\\1&0\end{smallmatrix}\bigr)\): the weighted stable-set enumerator is \(Z_n(z)=\operatorname{tr}(T_z^n)\), hence \(Z_n(1)=L_n\). For \(0\le k<n\), the first row of \(M=\mathbb E[X_nX_n^{\mathsf T}]\) is
\[
 q_k=\frac{F_{k-1}F_{n-k-1}}{L_n}.
\]
At \(k=0\), this says \(q_0=F_{n-1}/L_n\), the probability a prescribed vertex is occupied. For \(k\ne0\), if positions \(0\) and \(k\) are both occupied, their neighbors are vacant and the two intervening path interiors have \(k-3\) and \(n-k-3\) vertices. Counting their independent sets yields \(F_{k-1}F_{n-k-1}\); adjacency cases give zero. The formula, interpreted using \(F_{-1}\), covers \(n=3\) as well. The mean is \(\mathbb E X_n=q_0\mathbf1\), so
\[
 \operatorname{Cov}(X_n)=\operatorname{circ}(q_0,q_1,\ldots,q_{n-1})-q_0^2\mathbf1\mathbf1^{\mathsf T}.
\]

**2. Nonconstant Fourier spectrum.** Let \(\varphi=(1+\sqrt5)/2\) and \(\psi=(1-\sqrt5)/2\), so \(r=\psi/\varphi=-\varphi^{-2}\). Binet's formula, valid at index \(-1\), gives
\[
 q_k=\frac{\varphi^{n-2}}{5L_n}\bigl(1+r^{n-2}-r^{k-1}-r^{n-k-1}\bigr).
\]
For a nontrivial \(n\)th root of unity \(z=e^{i\theta_j}\), the constant terms vanish on summation. Summing the two geometric series in \(r\) gives
\[
 \sum_{k=0}^{n-1}q_kz^k
 =\frac{(1-r^2)(1-r^n)}{5(1+r^n)(1-2r\cos\theta_j+r^2)}.
\]
The rank-one centering correction vanishes on these nonconstant modes. This proves the asserted \(\lambda_j\) for \(1\le j<n\).

**3. Constant mode.** For variable fugacity \(z>0\), put
\[
 A(z)=\frac{1+\sqrt{1+4z}}2,\quad B(z)=\frac{1-\sqrt{1+4z}}2,\quad Z_n(z)=A(z)^n+B(z)^n.
\]
The total independent-set size \(N=\sum_i X_{n,i}\) has \(\operatorname{Var}(N)=\bigl[(z\partial_z)^2\log Z_n(z)\bigr]_{z=1}\), and \(\lambda_0=\operatorname{Var}(N)/n\). Writing \(u(z)=(B(z)/A(z))^n\), the first logarithmic derivatives of \(A,B\) are \(\tfrac12(1\mp(1+4z)^{-1/2})\), their second logarithmic derivatives are \(\pm z(1+4z)^{-3/2}\), and the two-state variance decomposition gives
\[
 \lambda_0=\frac{1-r^n}{5\sqrt5(1+r^n)}+\frac{n r^n}{5(1+r^n)^2}.
\]
This proves the complete exact spectrum.

**4. Strict identification of the smallest eigenvalue.** Set \(a=-r=(3-\sqrt5)/2\), so \(3/8<a<2/5\), and
\[
 B_n=\frac{1-r^n}{5\sqrt5(1+r^n)}.
\]
For \(1\le j<n\), because \(r<0\) and \(\cos\theta_j<1\), \(\lambda_j>B_n\). If \(n\) is odd, \(r^n<0\), hence \(\lambda_0<B_n\). For \(n=4\), the exact values are \(\lambda_0=5/49\) and \(\lambda_1=\lambda_3=1/7\). For even \(n\ge6\), the smallest nonconstant eigenvalue is \(\lambda_1\), and
\[
 \lambda_1-B_n=B_n\frac{2a(1-\cos(2\pi/n))}{1+2a\cos(2\pi/n)+a^2}.
\]
Here \(a<2/5\) implies \(w_n=a^n<(2/5)^6<1/200\), whence
\(B_n>1/12\). Also \(2a>3/4\), \(1-\cos(2\pi/n)\ge8/n^2\), and the denominator is smaller than \(49/25\). Therefore \(\lambda_1-B_n>25/(98n^2)\). But
\[
 \lambda_0-B_n=\frac{na^n}{5(1+a^n)^2}<\frac n5(2/5)^n<\frac{25}{98n^2},
\]
where the last inequality holds for \(n\ge6\): \(n^3(2/5)^n\) decreases from \(n=6\), and its value there is \(216(2/5)^6<125/98\). Thus \(\lambda_0<\lambda_1\) also for even \(n\). Together with \(n=3\) in the odd argument, this proves strict minimum-mode uniqueness for every \(n\ge3\).

**5. Top eigenspace and limit.** Since the nonzero-mode denominator \(1+2a\cos\theta_j+a^2\) strictly increases with \(\cos\theta_j\), its minimum occurs exactly at \(j=n/2\) for even \(n\), or at \(j=(n-1)/2,(n+1)/2\) for odd \(n\). Their real Fourier spans are as claimed, and \(\lambda_0\) is strictly below all these modes. Finally \(r^n\to0\), and the relevant cosine tends to \(-1\), giving
\[
 \lambda_0\to\frac1{5\sqrt5},\qquad
 \lambda_{\max}\to\frac{1-r^2}{5(1+r)^2}=\frac1{\sqrt5},
\]
so the ratio tends to \(5\).

## Verification

Run \(`python3 verify.py`\) using Python 3 standard library. It enumerates all stable sets of cycles \(3\le n\le16\); checks every entry of the independent-set second-moment kernel as exact rational numbers; checks the complete Fourier spectrum numerically against the closed formula; and verifies the eigenvalue ordering also for \(17\le n\le250\). The recorded successful execution checked 5771 individual vertices and 266 moment/DFT entries. The proof above supplies the all-dimensional justification; no finite test is represented as an infinite certificate.

## Relationship to prior work

Davis and Kohl (2022, arXiv:2207.14759) study stable-set polytopes and related matching/Ehrhart polynomials; their article gives the stable-set-polytope context but does not present this vertex-moment spectrum. Oriolo and Stauffer (2022) investigate facets of circular-interval-graph stable-set polytopes, a different invariant; their accessible full text does not provide this covariance classification. Ehrenborg (2024) studies Ehrhart and face polynomials of the cyclic graph polytope \(\{x\ge0:x_i+x_{i+1}\le1\}\), which agrees with the stable-set polytope when \(n\) is even, but describes different invariants. The one-dimensional hard-core model's transfer-matrix partition function and two-point correlations are classical ingredients, **not** claimed to be new. The contribution here is the all-dimensional closed polytope covariance spectrum and rigorous exact identification of both extremal Fourier eigenspaces, including the limiting sharp condition number.

## Limitations

Novelty is subject to priority verification: classical hard-core-model correlation/structure-factor literature could imply parts of the formula after Fourier transformation, even where not described using polytope language. The full text of the Ehrenborg article was not accessible for direct comparison, so only its identified stated aims and abstract can be assessed; it is a residual risk, not a proof of noncoverage. The conclusion is about the **vertex-uniform** measure, not the uniform-volume covariance, John ellipsoid, Ehrhart series, or graph Laplacian spectrum.

## References

- R. Davis and F. Kohl, *Perfectly Matchable Set Polynomials and \(h^*\)-polynomials for Stable Set Polytopes of Complements of Graphs*, arXiv:2207.14759, first posted July 29, 2022. https://arxiv.org/abs/2207.14759
- G. Oriolo and G. Stauffer, *On the facets of stable set polytopes of circular interval graphs*, Annals of Operations Research 312 (2022), 1007–1029. https://doi.org/10.1007/s10479-021-04449-7
- R. Ehrenborg, *The Ehrhart and face polynomials of the graph polytope of a cycle*, European Journal of Combinatorics 118 (2024), 103906. https://doi.org/10.1016/j.ejc.2023.103906
- F. Bencs, P. Csikvári, P. Srivastava, and J. Vondrák, *On complex roots of the independence polynomial*, SODA 2023, pp. 675–699. https://doi.org/10.1137/1.9781611977554.ch29
