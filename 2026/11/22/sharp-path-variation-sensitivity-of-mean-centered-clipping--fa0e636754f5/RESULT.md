# Sharp path-variation sensitivity of mean-centered clipping

## Finding
For every integer \(n\ge 2\), every threshold \(\tau>0\), and every real vector \(x\in\mathbb R^n\), let \(\bar x=n^{-1}\sum_{i=1}^{n}x_i\), let \(c_\tau(t)=\max\{-\tau,\min\{t,\tau\}\}\), and define the translation-equivariant, mean-centered clipping map
\[
 (T_{n,\tau}x)_i=\bar x+c_\tau(x_i-\bar x),\qquad 1\le i\le n.
\]
On the open path define the discrete total-variation seminorm \(V_n(h)=\sum_{i=1}^{n-1}|h_{i+1}-h_i|\). The exact **attained** two-input seminorm Lipschitz factor is
\[
 \sup_{V_n(x-y)>0}\frac{V_n(T_{n,\tau}x-T_{n,\tau}y)}{V_n(x-y)}
 = \frac{2}{n}\left\lfloor\frac{n^2}{4}\right\rfloor.
\]
In particular the factor equals \(1\) when \(n=2\), \(4/3\) when \(n=3\), \(2\) when \(n=4\), and is \(n/2\) for even \(n\) and \((n^2-1)/(2n)\) for odd \(n\). It is independent of \(\tau\). Nevertheless, every single input satisfies \(V_n(T_{n,\tau}x)\le V_n(x)\).

## Assumptions and scope
The data are arbitrary real samples on an ordered path, not necessarily monotone. There are \(n\ge2\) samples, their centering uses the **unweighted arithmetic mean**, and the same positive clipping threshold is used at all sites. The variation seminorm ignores constant sequences. The map is translation equivariant, \(T_{n,\tau}(x+a\mathbf1)=T_{n,\tau}(x)+a\mathbf1\), so the two-input ratio is well-defined on the quotient modulo constants. The nonlinear map generally does **not** preserve the arithmetic mean of its output: “mean-centered” describes the input reference level, not a conservation constraint. No claim is made for nonuniform mean weights, varying thresholds, or other graph structures.

## Proof
**1. Single-input diminution and translation invariance.** The scalar clip \(c_\tau\) is monotone and \(1\)-Lipschitz. Thus the difference of successive clipped entries has absolute value at most \(|x_{i+1}-x_i|\). Adding the common value \(\bar x\) does not affect any difference. A common translation of the input also translates \(\bar x\) by the same amount and does not change any centered deviation.

**2. Every affine Jacobian has the asserted universal upper bound.** Write \(P=\mathbf1\mathbf1^{\mathsf T}/n\). On each strict clipping-mask cell, the map is affine with linear part
\[
 J_d=\operatorname{diag}(d)+(I-\operatorname{diag}(d))P,
 \quad d_i=1\text{ on the unclipped sites, }\ d_i=0\text{ on the clipped sites}.
\]
In particular, \(J_d\mathbf1=\mathbf1\). At a clipping tie, the same formula with \(0\le d_i\le1\) describes directional slopes, and the following bounds remain valid. For \(1\le j<n\), let \(h^{(j)}\) be the step equal to zero through index \(j\) and one thereafter; set \(\mu=(n-j)/n\). The entries of \(J_dh^{(j)}\) lie in \([0,\mu]\) at the first \(j\) sites and in \([\mu,1]\) at the remaining sites. Each of the \(j-1\) left internal edges contributes at most \(\mu\), each of the \(n-j-1\) right internal edges contributes at most \(1-\mu\), and the bridging edge contributes at most \(1\). Consequently
\[
 V_n(J_dh^{(j)})\le(j-1)\mu+(n-j-1)(1-\mu)+1
 =\frac{2j(n-j)}{n}.
\]
Every input difference has the exact step decomposition
\[
 h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)h^{(j)},
 \qquad V_n(h)=\sum_{j=1}^{n-1}|h_{j+1}-h_j|.
\]
The triangle inequality and \(J_d\mathbf1=\mathbf1\) give \(V_n(J_dh)\le K_nV_n(h)\), with \(K_n=\max_{1\le j<n}2j(n-j)/n=2\lfloor n^2/4\rfloor/n\). Along any segment from \(x\) to \(y\), the map is continuous and piecewise affine; integrating its finitely many directional slopes (or partitioning at mask boundaries) transfers this bound to \(T_{n,\tau}x-T_{n,\tau}y\). A segment contained in a clipping boundary also satisfies the same directional bound by the interval-valued slope description. This proves the global upper bound.

**3. Strict-mask witnesses attain the bound.** Choose \(j=\lfloor n/2\rfloor\) and prescribe unclipped masks that alternate with clipped masks on both sides of the cut, taking the two sites \(j,j+1\) to be unclipped. For the step \(h^{(j)}\), each left internal edge then has absolute output difference \(\mu\), each right internal edge has difference \(1-\mu\), and the bridge has difference \(1\). Thus its linearized output variation equals \(2j(n-j)/n\).

These masks can be realized with strict inequalities and centered input. Let \(C\) be the set of clipped sites and let \(c=|C|\). If \(c=0\), use the zero input. If \(c\ge2\) is even, assign deviations \(+2\tau\) and \(-2\tau\) to equally many clipped sites, and deviation zero to all unclipped sites. If \(c\ge3\) is odd, assign \(+2\tau\) at \((c+1)/2\) clipped sites and \(-2\tau(c+1)/(c-1)\) at the other \((c-1)/2\), assigning zero to all unclipped sites. If \(c=1\), assign \(+3\tau/2\) to that site and \(-3\tau/[2(n-1)]\) to each of the other \(n-1\) sites; this case occurs only for \(n\ge3\). In each construction the mean is zero, every designated clipped site lies strictly outside the threshold, and every designated unclipped site lies strictly inside. For sufficiently small \(\varepsilon>0\), the inputs \(x\) and \(x+\varepsilon h^{(j)}\) remain in the same affine mask cell. Their variation ratio equals \(V_n(J_dh^{(j)})/V_n(h^{(j)})=K_n\) exactly. When \(n=2\), both sites can be kept strictly unclipped and the map is locally the identity. This also proves attained sharpness for every positive \(\tau\). \(\square\)

## Verification
The standalone Python program `verify_centered_clipping.py` uses exact rational arithmetic. Executing `python verify_centered_clipping.py` exhausts all clipping masks and step cuts for \(2\le n\le10\), constructs strict-mask attaining pairs for \(2\le n\le100\), and checks 2,400 seeded rational input pairs for the global two-input inequality, one-input diminution, and translation equivariance. These computations are checks of finite instances, not a replacement for the all-dimensional proof in the preceding section.

## Relationship to prior work
Kitić et al., *Consistent Iterative Hard Thresholding for Signal Declipping* (public preprint March 5, 2013, arXiv:1303.1023), explicitly define coordinatewise hard clipping in Section 3, equation (4), and study sparsity-based recovery from saturated audio. Their forward map uses a fixed absolute reference, without input-dependent mean centering, and their restoration results do not give a two-input discrete-BV seminorm coefficient. Chen and Selesnick, *Translation-Invariant Shrinkage/Thresholding of Group Sparse Signals* (public preprint March 29, 2013, arXiv:1304.0035), study nonlinear group shrinkage for denoising, not the specific mean-centered coordinatewise clipping map or its sharp path-variation gain. The present theorem concerns forward perturbation stability, not successful declipping or reconstruction.

The sharpness mechanism differs from Euclidean-ball or radial group-soft-threshold estimates: here independent zero-or-one coordinate slopes alternate on either side of a single-jump perturbation. The factor is therefore not obtained from a Euclidean radial derivative bound, an ordinary scalar clipping inequality, or individual-input variation diminution. A search of relevant indexed findings and the accessible prior research claims did not reveal an implication-equivalent exact formula; this search does not establish historical priority.

## Limitations
The calculation is for finite real paths, unweighted centering, a uniform fixed clip level, and one application. It does not assert stability under nonuniform centering, unequal per-site clipping levels, cycles or arbitrary graphs; these variants require new feasibility and edge-count analysis. The finite checker does not certify the theorem in untested dimensions. The pre-existing literature may contain unindexed equivalent results; independent audit and external priority verification have not been performed.

## References
1. S. Kitić, L. Jacques, N. Madhu, M. P. Hopwood, A. Spriet, and C. De Vleeschouwer, *Consistent Iterative Hard Thresholding for Signal Declipping*, arXiv:1303.1023, first public March 5, 2013. https://arxiv.org/abs/1303.1023
2. P.-Y. Chen and I. W. Selesnick, *Translation-Invariant Shrinkage/Thresholding of Group Sparse Signals*, arXiv:1304.0035, first public March 29, 2013. https://arxiv.org/abs/1304.0035
