# An exact near-isometry threshold and conditioning reversal for one-collision sketches of unicyclic incidence spaces

## Finding
Let a connected, simple, unweighted unicyclic graph have \(n\ge3\) vertices and \(n\) edges, and unique cycle length \(3\le\ell\le n\). Choose any orientations, delete any one vertex column of its oriented edge–vertex incidence matrix \(B\), and set
\[
U=B(B^{\mathsf T}B)^{-1/2},\qquad U^{\mathsf T}U=I_{n-1}.
\]
For an independent uniform signed one-sparse CountSketch \(S\in\mathbb R^{m\times n}\), set
\[
G_S=U^{\mathsf T}S^{\mathsf T}SU,\qquad \delta(S)=\|G_S-I_{n-1}\|_2.
\]
The sharp distribution of *strictly subunit* distortion is, for every \(0\le\varepsilon<1\),
\[
\boxed{\Pr(\delta(S)\le\varepsilon)=\frac{(m)_n+\ell(n-\ell)(m)_{n-1}\mathbf1_{\{\varepsilon\ge\sqrt{1-1/\ell}\}}}{m^n},}
\]
where \((m)_k=m(m-1)\cdots(m-k+1)\), set to zero when \(k>m\). For one collision, the complete exceptional Gram spectrum (beside \(n-3\) eigenvalues equal to one) is:

| Colliding edge pair | Sketch-sign relation | Two exceptional Gram eigenvalues | Full rank? |
|---|---|---|---|
| Both on cycle | Favorable | \(2,\;2/\ell\) | Yes |
| Both on cycle | Unfavorable | \(0,\;2-2/\ell\) | No |
| One cycle, one bridge | Either | \(1+\sqrt{1-1/\ell},\;1-\sqrt{1-1/\ell}\) | Yes |
| Both bridges | Either | \(2,\;0\) | No |

Here *favorable* means that the signed collision's kernel direction has a nonzero circulation pairing, equivalently \(\tau c_e c_f=-1\), with the circulation signs and \(\tau\) defined below. For a cycle with at least one attached bridge, a favorable cycle–cycle collision has \(\delta=1\) and \(\kappa(SU)=\sqrt\ell\); a cycle–bridge collision has *smaller* \(\delta=\sqrt{1-1/\ell}<1\) but *larger* condition number
\[
\boxed{\kappa(SU)=\sqrt\ell\bigl(1+\sqrt{1-1/\ell}\bigr)>\sqrt\ell.}
\]
Thus spectral distortion and the conditioning of the injected sketch can strictly rank the same two types of successful collisions in opposite orders. The explicit full-column-rank probability for this graph family was already established in prior work and is not asserted as new here.

## Assumptions and scope
The graph has exactly one simple cycle, unit edge conductances, and arbitrary trees attached to cycle vertices. Orientations and the deleted vertex column do not affect the result. Hashes of the \(n\) input coordinates are independent and uniform on \(m\ge1\) buckets; signs are independent fair Rademacher variables. Gram eigenvalues refer to the **whitened incidence subspace** \(\operatorname{col}(B)\), not to the raw non-orthonormal incidence columns. The distortion is the squared-norm operator distortion \(\|U^{\mathsf T}S^{\mathsf T}SU-I\|_2\), not its square root. The displayed probability covers \(0\le\varepsilon<1\) and makes no assertion for larger tolerances.

## Proof
A unit circulation \(c\in\{0,-1,1\}^n\) has nonzero signed entries on precisely the \(\ell\) cycle edges. Since the graph is connected and unicyclic, its oriented incidence columns span the hyperplane \(c^\perp\), and
\[
P=UU^{\mathsf T}=I_n-\frac{cc^{\mathsf T}}\ell.
\]
If there is no hash collision, every input coordinate occupies a distinct output bucket, \(S^{\mathsf T}S=I_n\), so \(G_S=I_{n-1}\).

Suppose one collision occurs between distinct edge coordinates \(e,f\), all others occupying singleton buckets. Let \(\tau\in\{-1,1\}\) be their sign product. Then
\[
S^{\mathsf T}S=I_n+\tau(e_e e_f^{\mathsf T}+e_f e_e^{\mathsf T})
=I_n+vv^{\mathsf T}-uu^{\mathsf T},
\quad u=(e_e-\tau e_f)/\sqrt2,\quad v=(e_e+\tau e_f)/\sqrt2.
\]
On the hyperplane \(c^\perp\), this perturbation has rank at most two. Let
\[
a=\frac{(c_e-\tau c_f)^2}{2\ell},\qquad b=\frac{(c_e+\tau c_f)^2}{2\ell}.
\]
Since \(\|Pu\|^2=1-a\), \(\|Pv\|^2=1-b\), and \(\langle Pu,Pv\rangle=-(c^{\mathsf T}u)(c^{\mathsf T}v)/\ell\), the two possibly nonzero eigenvalues of \(vv^{\mathsf T}-uu^{\mathsf T}\) after compression have sum \(a-b\) and product \(-(1-a-b)\). For \(\ell\ge3\), \(a+b=(c_e^2+c_f^2)/\ell\le2/\ell<1\), so they are both nonzero. The two exceptional eigenvalues \(\lambda_\pm\) of \(G_S\) therefore satisfy
\[
\lambda_\pm=1+\frac{a-b\pm\sqrt{(a-b)^2+4(1-a-b)}}2.
\]
Substituting \((c_e^2,c_f^2)=(1,1),(1,0),(0,0)\) and the two cycle-sign possibilities gives exactly the four rows of the displayed table. The remaining \(n-3\) Gram eigenvalues are one (including the case \(n=3\), with zero such eigenvalues).

When at least two independent input-coordinate collisions occur, the number of occupied hash buckets is at most \(n-2\); consequently \(\dim\ker S\ge2\). The \((n-1)\)-dimensional space \(c^\perp\) must intersect this kernel nontrivially. Thus \(SU\) is rank deficient, and \(\delta(S)\ge1\). The table also shows that among single collisions, only cycle–bridge pairs yield \(\delta<1\): their value is exactly \(\sqrt{1-1/\ell}\); the other rows all have \(\delta=1\). The no-collision probability is \((m)_n/m^n\). Each specified unordered pair is the sole collided pair with probability \((m)_{n-1}/m^n\); there are exactly \(\ell(n-\ell)\) cycle–bridge pairs. Summing these mutually disjoint events proves the exact near-isometry probability.

For a favorable cycle–cycle collision the two nonunit singular values of \(SU\) are \(\sqrt2\) and \(\sqrt{2/\ell}\), so the condition number is \(\sqrt\ell\). For a cycle–bridge collision they are \(\sqrt{1\pm s}\), with \(s=\sqrt{1-1/\ell}\). The singular-value ratio is
\[
\sqrt{\frac{1+s}{1-s}}=\sqrt\ell(1+s),
\]
which is strictly greater than \(\sqrt\ell\); its distortion \(s\) is strictly less than one. This proves the asserted criterion reversal.

## Verification
The included standard-library-only `verify.py` computes exact rational Gram characteristic polynomials on the circulation hyperplane and checks every edge-pair and sign case for all orders from three through nine, across the admissible cycle lengths and both orientations. It also enumerates all signed hash configurations at the minimal sketch size for a triangle and a triangle with a pendant edge, confirming the predicted event probabilities. Execute `python verify.py`. The recorded output is:

`PASS: 1260 exact rational characteristic-polynomial checks; 216-case triangle and 1296-case pendant-triangle enumerations`

For a triangle with one pendant edge \((n,\ell,m)=(4,3,3)\), the probability of distortion less than or equal to \(9/10\) is \(2/9\). The separate probability of full column rank is \(1/3\), consistent with (but logically weaker than) the prior rank theorem. Finite checks are verification of algebra, not proof for arbitrary graph order.

## Relationship to prior work
Clarkson and Woodruff's sparse subspace-embedding construction (arXiv:1207.6365) supplies the generic one-sparse sketch and collision/birthday analysis, not this exact graph-family spectral law. Hu, Ubaru, Gittens, Clarkson, Horesh and Kalantzis (arXiv:2102.05758) study graph-based sparse embeddings and distortion guarantees but not the exact unicyclic one-collision compressed spectrum. Closest is *Exact signed CountSketch rank survival for weighted unicyclic incidence matrices* (2026): its theorem already gives an exact algebraic rank-success probability for all positive edge weights; its hyperplane and collision argument is directly applicable here. Its inspected theorem and proof do **not** state the exact Gram eigenvalues, the sharp \(\varepsilon<1\) norm-distortion probability, or the strict conditioning-vs-distortion reversal. The present work therefore makes no novelty claim for rank survival, and a short spectral extension of that result is its core scope.

## Limitations
The classification describes a **single collision** and the sharp event with distortion strictly below one; it does not classify all Gram spectra when several hash buckets collide, nor bound distortion at or above one. It uses unit graph-edge scales; arbitrary positive scales have different circulation ratios and need new analysis. Probability assumptions require independent hashes and signs. The condition number is that of \(SU\) with orthonormalized columns, not of an unscaled incidence matrix. Novelty depends on the inspected prior sources; unindexed equivalent formulations, particularly in codimension-one CountSketch or frame-compression literature, remain possible. Independent validation has not been performed.

## References
1. K. L. Clarkson and D. P. Woodruff, *Low Rank Approximation and Regression in Input Sparsity Time*, arXiv:1207.6365, first public 2012-07-26, https://arxiv.org/abs/1207.6365 .
2. D. Hu, S. Ubaru, A. Gittens, K. L. Clarkson, L. Horesh and V. Kalantzis, *Sparse graph based sketching for fast numerical linear algebra*, arXiv:2102.05758, first public 2021-02-10, https://arxiv.org/abs/2102.05758 .
3. *Exact signed CountSketch rank survival for weighted unicyclic incidence matrices*, published 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-signed-countsketch-rank-survival-for-weighted-unicyclic-in--6f43abc6393e/RESULT.md .
