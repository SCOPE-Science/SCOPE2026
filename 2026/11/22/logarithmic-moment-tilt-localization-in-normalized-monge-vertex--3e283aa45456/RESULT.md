# Logarithmic moment-tilt localization in normalized Monge vertex clouds

## Finding

For every integer \(n\ge2\), consider the normalized nonsymmetric Monge polytope \(\mathcal M_n\) of nonnegative real \(n\times n\) matrices whose entries sum to one and satisfy the Monge inequalities. Let \(V_n\) be uniform on its **distinct vertices**, and write \(T_n=\|V_n\|_F^2\), the sum of squares of its entries (also the probability that two independent sites drawn from the categorical distribution \(V_n\) coincide). For \(s\ge0\), let \(H_{n-1}^{(s)}=\sum_{j=1}^{n-1}j^{-s}\). Then the entire nonnegative Mellin-moment spectrum is exactly
\[
\boxed{\mathbb E(T_n^s)=\frac{(H_{n-1}^{(s)})^2+n^{1-s}}{n^2-n+1}.}
\]

A genuine localization transition occurs when the vertex law is tilted by \(T_n^s\). Under the normalized \(s\)-tilt, the probability of selecting a row or column-strip vertex vanishes for every fixed \(s\ge0\). The remaining vertex is a uniform choice of either orientation of a corner rectangle of side lengths \((A_n,B_n)\), with independent side-length probabilities proportional to \(a^{-s}\). Precisely:

- If \(0\le s<1\), the two normalized lengths \((A_n/n,B_n/n)\) converge to independent \(\operatorname{Beta}(1-s,1)\) variables.
- If \(s=1\), the logarithmic lengths \((\log A_n/\log n,\log B_n/\log n)\) converge to independent uniform variables on \([0,1]\).
- If \(s>1\), the unscaled pair converges in total variation to independent zeta-distributed positive integers, each with probability \(a^{-s}/\zeta(s)\).

The transition has an exact **logarithmic critical window**: for any fixed real \(\lambda\), set \(s_n=1+\lambda/\log n\). Under this tilt, the logarithmic side lengths converge independently to the distribution on \([0,1]\) whose density is
\[
\boxed{f_\lambda(t)=\frac{e^{-\lambda t}}{\int_0^1 e^{-\lambda u}\,du},\qquad 0\le t\le1.}
\]

For the untilted uniform vertex, \(n^2T_n\Rightarrow Z=(UV)^{-1}\) with independent uniform \(U,V\) on \([0,1]\). Its survival function is exactly
\[
\Pr(Z>z)=\frac{1+\log z}{z}\quad(z\ge1).
\]
In particular, \(\mathbb E(Z^s)<\infty\) exactly for \(s<1\). Correspondingly,
\[
\mathbb E[(n^2T_n)^s]\sim
\begin{cases}
(1-s)^{-2},&0\le s<1,\\
(\log n)^2,&s=1,\\
\zeta(s)^2 n^{2s-2},&s>1.
\end{cases}
\]
Thus a typical squared vertex norm is of order \(n^{-2}\), whereas its mean is of order \((\log n)^2/n^2\): rare highly concentrated extreme cost matrices dominate the mean. The \(s=1\) tilt has the direct meaning of conditioning on two independently sampled matrix sites coinciding.

## Assumptions and scope

A matrix \(C=(c_{ij})_{1\le i,j\le n}\) lies in \(\mathcal M_n\) if and only if \(c_{ij}\ge0\), \(\sum_{i,j}c_{ij}=1\), and \(c_{ij}+c_{i+1,j+1}\le c_{i,j+1}+c_{i+1,j}\) for \(1\le i,j<n\). The metric is ordinary Frobenius/Euclidean coordinate metric. The sampling law is uniform on distinct vertices, *not* Lebesgue-uniform in the polytope and *not* Gaussian-direction vertex exposure. The \(s\)-tilted law assigns vertex \(v\) probability proportional to \(\|v\|_F^{2s}\). Statements involving \((A_n,B_n)\) condition on the vertex being a corner-block vertex; this conditioning has probability tending to one under each stated fixed or logarithmic-window tilt. The two rectangle orientations are equiprobable. The exponent \(s\) is real and nonnegative, and all limit assertions are as \(n\to\infty\). The symbol \(\Rightarrow\) denotes weak convergence.

## Proof

**1. Complete vertex parametrization.** Erickson and Kretschmann, Proposition 5.1 (2023), prove that the vertices of the normalized \(p\times q\) nonsymmetric Monge polytope are precisely the normalized upper-right and lower-left \(a\times b\) rectangular blocks with \(1\le a<p\), \(1\le b<q\), together with the normalized full row strips and normalized full column strips. There are \(2(p-1)(q-1)+p+q\) distinct vertices. Applying this published theorem with \(p=q=n\) gives exactly \(2(n-1)^2+2n=2(n^2-n+1)\) vertices. A normalized \(a\times b\) block has \(ab\) nonzero entries, each \(1/(ab)\), and therefore has squared Frobenius norm \(1/(ab)\). Every strip has \(n\) nonzero entries, each \(1/n\), so has squared norm \(1/n\). In particular the vertex types are not counted with artificial multiplicity.

**2. Exact moments and tilt probabilities.** Summing \(T_n^s\) over the vertex list and dividing by the total number gives
\[
\mathbb E(T_n^s)=\frac{2\sum_{a,b=1}^{n-1}(ab)^{-s}+2n\,n^{-s}}{2(n^2-n+1)}
=\frac{(H_{n-1}^{(s)})^2+n^{1-s}}{n^2-n+1}.
\]
Under the power tilt, the exact probability of a strip vertex is
\[
\rho_{n,s}=\frac{n^{1-s}}{(H_{n-1}^{(s)})^2+n^{1-s}}.
\]
Conditionally on a corner block, each orientation has probability \(1/2\) and the side lengths are independent with \(\Pr(A_n=a)=a^{-s}/H_{n-1}^{(s)}\), identically for \(B_n\). These identities are exact at every finite \(n\), including at dimension two.

**3. The three localization regimes.** By integral comparison,
\[
H_{n-1}^{(s)}\sim\begin{cases}n^{1-s}/(1-s),&0\le s<1,\\\log n,&s=1,\\\zeta(s),&s>1.\end{cases}
\]
Consequently \(\rho_{n,s}\to0\) in every fixed regime. For \(s<1\), the weighted partial sums to \(\lfloor nt\rfloor\), divided by \(H_{n-1}^{(s)}\), converge to \(t^{1-s}\) for every \(0<t\le1\). For \(s=1\), the partial harmonic sum to \(\lfloor n^t\rfloor\), divided by \(H_{n-1}^{(1)}\), converges to \(t\) for \(0\le t\le1\). For \(s>1\), the total variation distance between the truncated mass function \(a^{-s}/H_{n-1}^{(s)}\) and the full zeta distribution is bounded by the omitted zeta tail divided by \(\zeta(s)\), which tends to zero. Independence in each case proves the stated joint limits.

**4. The critical window.** Fix \(\lambda\in\mathbb R\) and put \(s_n=1+\lambda/\log n\). For all sufficiently large \(n\), the function \(x^{-s_n}\) decreases in \(x\), and integral comparison, with an error bounded uniformly in \(n\) for fixed \(\lambda\), gives
\[
H_{n-1}^{(s_n)}\sim (\log n)\int_0^1e^{-\lambda u}\,du.
\]
The same comparison for the partial sum through \(\lfloor n^t\rfloor\) gives the limiting distribution function
\[
\frac{\int_0^t e^{-\lambda u}\,du}{\int_0^1 e^{-\lambda u}\,du}.
\]
Since \(n^{1-s_n}=e^{-\lambda}\) while the square of the harmonic sum is of order \((\log n)^2\), the strip mass vanishes in the window. The two lengths remain conditionally independent, giving the joint density product and the formula for \(f_\lambda\).

**5. Heavy tail and moment nonuniformity.** At \(s=0\), the fraction of strip vertices is \(n/(n^2-n+1)\to0\), and conditioned on a corner block, \(A_n,B_n\) are independent uniform integers in \(\{1,\dots,n-1\}\). Hence \((A_n/n,B_n/n)\Rightarrow(U,V)\) for independent uniforms on \([0,1]\). The continuous mapping theorem applies to \((u,v)\mapsto (uv)^{-1}\), since the axes have limiting probability zero. For \(z\ge1\), direct integration yields \(\Pr(UV<1/z)=(1+\log z)/z\). A further direct integral gives \(\mathbb E[(UV)^{-s}]=(1-s)^{-2}\) for \(s<1\), whereas it diverges for \(s\ge1\). Finally, multiply the exact moment formula from step 2 by \(n^{2s}\) and apply the same harmonic-sum asymptotics. This proves all three displayed moment regimes and shows why finite-dimensional moment limits fail at and above the threshold. In the integer case, \(T_n^s\) is the probability of \(s\) independent pairwise coincidence events among entries sampled from the normalized matrix, giving the tilt its direct sampling interpretation.

## Verification

The standalone `VERIFY.py` checks the full claimed vertex list for distinctness, normalization and each defining Monge inequality for \(2\le n\le9\). It uses exact rational arithmetic to compare independently calculated squared norms and all five integer moments \(s=0,1,2,3,4\) with the closed formula. A separate finite-size calculation compares the three explicit critical-window distribution functions for \(\lambda=-3,0,3\) at length \(n=100000\) and three logarithmic quantiles. Run `python3 VERIFY.py`; the expected output begins with `MONGE_VERTEX_MOMENT_TILT_PASS`. These checks corroborate, but do not replace, the published vertex parametrization and the all-order analytic proof.

## Relationship to prior work

Erickson and Kretschmann (2023), Proposition 5.1, give the complete vertex parametrization and count from which the first proof step begins. Their classification and the elementary harmonic-sum estimates are explicitly credited. Their work does not state the vertex-uniform Frobenius collision-moment spectrum, its Pareto–logarithmic limit, or the two-sided critical exponent/window for power-biased vertex selection. Published studies on uniform *interior-volume* samples and Gaussian *directional-exposure* of two-row Monge polytopes address different measures from the present discrete vertex-uniform family. Likewise, published inball and enclosing-ball classifications of Monge polytopes do not identify this moment-tilt distribution. A general cone-extreme-ray antecedent of Rudolf and Woeginger (1995) may make the block parametrization available in older language; no new assertion is made about the block parametrization itself.

## Limitations

The proof concerns square, normalized, nonsymmetric Monge polytopes with the canonical coordinate metric; it does not assert universality under arbitrary affine changes of coordinates, nonuniform vertex weights, or rectangular aspect-ratio growth. The finite numerical tests are not proofs of the weak limits or the critical window. Priority remains provisional: equivalent probability laws might exist in unindexed transport/Monge literature, and not all relevant historical full texts were accessible. Independent mathematical audit has not been performed.

## References

1. W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, first publicly posted 2023-11-13, Proposition 5.1 and Sections 3–5, https://arxiv.org/abs/2311.07522.
2. R. Rudolf and G. J. Woeginger, *The cone of Monge matrices: extremal rays and applications*, Mathematical Methods of Operations Research 42 (1995), 161–168, https://doi.org/10.1007/BF01415751 (historical antecedent; full text not inspected).
3. W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508, posted 2026-09-08, https://arxiv.org/abs/2609.09508 (abstract-level comparison).
4. *Uniform two-row Monge polytopes have a Laplace limit shape and independent Gumbel edges* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-uniform-two-row-monge-polytopes-have-a-laplace-limit-shape-and-i--7c7e590d3b3c.
5. *A sharp rare-vertex mean-width correction for two-row Monge polytopes* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-rare-vertex-mean-width-correction-for-two-row-monge-poly--bf1db1bc9d42.
6. *A sharp outer-sphere and contact collapse for two-row Monge polytopes* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-sharp-outer-sphere-and-contact-collapse-for-two-row-monge-poly--400d92285f9e.
7. *Gcd-controlled Euclidean inballs of rectangular Monge polytopes* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-gcd-controlled-euclidean-inballs-of-rectangular-monge-polytopes--3e50eb77bbfb.
