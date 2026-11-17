# Exact normalized-heat variation amplification and a four-triangle stability boundary on friendship graphs

## Finding

Let \(F_m\) be the friendship graph obtained by joining \(m\ge1\) triangles at their common hub \(o\), each triangle having two private vertices \(v_j^+,v_j^-\). Put \(Q=D^{-1}A-I\) and \(H_t=e^{tQ}\) for \(t\ge0\). On real functions of the vertices use **edge-sum variation**
\[
J(f)=\sum_{\{u,v\}\in E(F_m)}|f(u)-f(v)|.
\]
Then the **exact, attained** quotient-seminorm of the heat operator is
\[
\boxed{N_m(t):=\sup_{J(f)>0}\frac{J(H_tf)}{J(f)}=\frac{2(m-1)}m e^{-t/2}-\frac{m-2}m e^{-3t/2}.} \tag{1}
\]
For every \(m\ge1\) and every \(t\ge0\), the indicator of the two private vertices of any one triangle realizes equality in (1).

There is an exact **four-triangle threshold**. For \(1\le m\le4\), the heat flow is strictly variation-contracting at every positive time. For \(m\ge5\), it initially increases some inputs' variation, has exactly one positive-time global norm maximum, and ultimately contracts. Its peak time and attained peak are
\[
 t_m=\log\!\frac{3(m-2)}{2(m-1)},\qquad
 M_m=\frac{4(m-1)}{3m}\sqrt{\frac{2(m-1)}{3(m-2)}}.
\]
Furthermore, \(N_m(t)\) increases strictly in \(m\) for every fixed \(t>0\), and the sharp envelope over all finite friendship graphs and times is
\[
\boxed{\sup_{m\ge1,t\ge0}N_m(t)=\frac43\sqrt{\frac23},}
\]
an **unattained** supremum, approached as \(m\to\infty\) and \(t\to\log(3/2)\).

## Assumptions and scope

All graphs are finite, connected, simple, with unit edge weights. Their \(2m+1\) vertices comprise the hub \(o\) and \(m\) pairs \(\{v_j^+,v_j^-\}\). The hub degree is \(2m\), peripheral degrees are two, and each pair's two vertices are adjacent. At every vertex, \(Qf(v)=\deg(v)^{-1}\sum_{u\sim v}f(u)-f(v)\), so all vertices jump away at total rate one. This is the **degree-normalized** generator, not the unnormalized combinatorial Laplacian. The inputs may be arbitrary real signals. Since \(J(f)=0\) exactly for constants, and \(Q\mathbf1=0\), the quotient norm is defined on the vector space modulo constants. No stationary-measure weighting enters \(J\).

## Proof

**1. Solve the full normalized heat equation.** For a signal \(f\), set
\[
 h=f(o),\quad s_j=\tfrac12(f(v_j^+)+f(v_j^-)),\quad a_j=\tfrac12(f(v_j^+)-f(v_j^-)),\quad \bar s=m^{-1}\sum_js_j.
\]
The heat equation gives the exact scalar system
\[
\dot h=\bar s-h,\qquad \dot s_j=\tfrac12(h-s_j),\qquad \dot a_j=-\tfrac32a_j.
\]
Hence \(\bar s-h\) and every \(a_j\) decay at rate \(3/2\), while each centered blade mean \(s_j-\bar s\) decays at rate \(1/2\). Write \(u=e^{-t/2}\) and \(v=e^{-3t/2}\); thus \(0<v\le u\le1\). For every input the evolved hub-relative peripheral values are
\[
 (H_tf)(v_j^\pm)-(H_tf)(o)
   =u(s_j-\bar s)+v(\bar s-h\pm a_j),
 \quad (H_tf)(v_j^+)-(H_tf)(v_j^-)=2va_j. \tag{2}
\]
The formula follows from the displayed ODE system for all nonnegative real times, including ties and all sizes.

**2. Reduce the induced norm to binary cuts.** Any real signal with distinct sorted values \(c_1<\cdots<c_r\) has the exact layer-cake expansion
\[
 f=c_1\mathbf1+\sum_{\ell=2}^r(c_\ell-c_{\ell-1})\mathbf1_{\{f\ge c_\ell\}},
 \qquad J(f)=\sum_{\ell=2}^r(c_\ell-c_{\ell-1})J(\mathbf1_{\{f\ge c_\ell\}}).
\]
The second equality holds edge by edge because the superlevel cuts are nested. Since \(H_t\) is linear and fixes constants, the triangle inequality yields
\[
 \frac{J(H_tf)}{J(f)}\le\max_{S:\,J(\mathbf1_S)>0}\frac{J(H_t\mathbf1_S)}{J(\mathbf1_S)}.
\]
Taking any cut as input supplies the converse. This works with arbitrary signed inputs, and is not merely a finite numerical enumeration.

**3. Reduce every cut to one triangle.** Because \(H_t\mathbf1=\mathbf1\), complementing a cut leaves its variation ratio unchanged. We may take \(o\notin S\). Each occupied triangle then contributes either one or two peripheral vertices to \(S\). Let \(S_j=S\cap\{v_j^+,v_j^-\}\). Their indicators have disjoint supports, satisfy \(\mathbf1_S=\sum_j\mathbf1_{S_j}\), and—crucially—have additive input variations,
\[
 J(\mathbf1_S)=\sum_j J(\mathbf1_{S_j})=2\#\{j:S_j\ne\varnothing\}.
\]
(One peripheral singleton cuts its hub edge and the private edge; a full pair cuts its two hub edges.) By the triangle inequality and linearity,
\[
J(H_t\mathbf1_S)\le\sum_jJ(H_t\mathbf1_{S_j}).
\]
Thus the global ratio is bounded by the larger of exactly two one-triangle ratios: a single peripheral vertex and a complete peripheral pair.

**4. Evaluate and compare both ratios.** For the complete peripheral pair in triangle one, its initial coordinates are \(h=0\), \(s_1=1\), \(s_j=0\) for \(j>1\), and all \(a_j=0\), so \(\bar s=1/m\). Formula (2) gives the hub-relative values
\[
 d_1=\frac{(m-1)u+v}{m}\ge0,\qquad d_j=\frac{v-u}{m}\le0\quad(j>1).
\]
All private edges have zero output difference, and the input variation is two. Therefore its exact variation quotient is
\[
 R_{\rm pair}=d_1+(m-1)|d_j|=\frac{2(m-1)}m u-\frac{m-2}m v. \tag{3}
\]
For an input selecting only \(v_1^+\), one has \(s_1=a_1=1/2\), \(s_j=a_j=0\) for \(j>1\), and \(\bar s=1/(2m)\). Its two hub-relative values in the chosen triangle are \(((m-1)u+(m+1)v)/(2m)\) and \((m-1)(u-v)/(2m)\), both nonnegative. Every other peripheral vertex has difference \((v-u)/(2m)\), and the chosen private edge has absolute difference \(v\). Summing all three edge types and dividing by its input variation two gives
\[
 R_{\rm singleton}=\frac{m-1}{m}u+\frac1m v.
\]
Subtracting yields \(R_{\rm pair}-R_{\rm singleton}=\frac{m-1}{m}(u-v)\ge0\). Equations (3) and the cut reductions prove (1), including sharp attainment and \(m=1\).

**5. Derive the complete time/size phase diagram.** For \(m=1\), (1) is \(e^{-3t/2}\). For \(m\ge2\), differentiation gives
\[
 N'_m(t)= -\frac{m-1}{m}e^{-t/2}+\frac{3(m-2)}{2m}e^{-3t/2}.
\]
This is negative for every \(t>0\) if \(m\le4\) (for \(m=4\), the derivative is zero only at \(t=0\)); the norm tends to zero. If \(m\ge5\), the derivative starts at \((m-4)/(2m)>0\), vanishes exactly once at \(t_m\), and is negative thereafter. Substitution of its critical-point identity gives the stated \(M_m>1\). Finally,
\[
 N_m(t)=2u-v-\frac2m(u-v),
\]
which strictly increases with \(m\) when \(t>0\). Its limit \(2u-v\) has a unique maximizer at \(t=\log(3/2)\), where the value is \(\tfrac43\sqrt{2/3}\). Every finite \(m\) has a strictly smaller value at every \(t>0\), and at time zero the norm is one. Thus the envelope is sharp and unattained.

## Verification

The standalone standard-library script `CHECK.py` independently constructs every graph's degree-normalized generator, decomposes its exact heat operator as a polynomial in \(q=e^{-t/2}\), and checks the generator/eigenspace equations on coordinate bases. It then exhausts all cuts omitting the hub up to six triangles at rational values of \(q\), checks precise pair-cut attainment, tests arbitrary signed signals, and checks integer threshold cases by rational arithmetic. The recorded diagnostics include 48 generator polynomial identities, 32,724 nontrivial cut comparisons, 36 pair-witness attainments, 1,800 signed-input inequalities, and 29 threshold comparisons. Run `python3 CHECK.py` with Python 3; only the standard library is required. The all-size and all-time statements are established by Steps 1–5, **not** extrapolated from finite checks.

## Relationship to prior work

The graph-variation and coarea treatment by van Gennip, Guillen, Osting, and Bertozzi (2013 preprint; published 2014) provides the general discrete cut and heat-flow setting but studies graph curvature, threshold dynamics, and nonlinear phase-field flows rather than the exact two-input normalized-heat edge-variation seminorm of friendship graphs. The friendship graph itself and its adjacency-spectral characterization occur in Abdollahi, Janbaz, and Oboudi (2013), and generalized friendship normalized Laplacian spectra are investigated by Berman and collaborators (2018); these spectral facts do not determine the sign-sensitive operator norm (1).

Closest publicly available related mathematical results include an **unnormalized** clique-bouquet heat-variation contraction classification and an exact **Wasserstein-one** transport formula for unnormalized heat on equal-blade windmills. Neither implies (1): degree-normalized and unnormalized generators differ on the nonregular friendship graphs with more than one triangle, and \(W_1\) transport of signed vertex masses is dual to the *maximum* edge slope, not the *sum* of absolute edge slopes. The former unnormalized classification has a different nonexpansivity boundary, while the latter uses a different norm and decay rates. A published sorted-cut theorem for weighted graph-edge variation of **normalized** heat on complete bipartite graphs likewise does not cover friendship graphs, which have peripheral triangle edges.

The new claim is the exact normalized-generator, **unweighted edge-sum variation** norm, four-triangle threshold, and sharp all-size amplification envelope. The formula is not asserted to give the mixing time, \(W_1\)-contraction, graph-Lipschitz norm, or the combinatorial-heat norm. No historical uniqueness is claimed beyond the checked comparisons; an unindexed equivalent antecedent remains possible.

## Limitations

Only equal unit-weight triangles joined at a single hub, counting vertex signals, total exit rate one at every vertex, unweighted edge-sum variation, and real continuous-time heat are covered. The theorem is not asserted for unequal clique blades, generic trees, arbitrary weighted graphs, unnormalized combinatorial heat, discrete powers of the non-lazy random walk, other variation geometries, or nonlinear heat flows. The source comparison is bounded and is not an independent priority determination.

## References

1. Yves van Gennip, Nestor Guillen, Braxton Osting, and Andrea L. Bertozzi, *Mean curvature, threshold dynamics, and phase field theory on finite graphs*, arXiv:1307.0045, first public 2013-06-28; https://arxiv.org/abs/1307.0045. Published in *Milan Journal of Mathematics* 82 (2014), 3–65.
2. Alireza Abdollahi, Shahrooz Janbaz, and Mohammad Reza Oboudi, *Graphs cospectral with a friendship graph or its complement*, arXiv:1307.5411, first public 2013-07-20; https://arxiv.org/abs/1307.5411.
3. Abraham Berman, Dong-Mei Chen, Zhi-Bing Chen, Wen-Zhe Liang, and Xiao-Dong Zhang, *A family of graphs that are determined by their normalized Laplacian spectra*, arXiv:1805.10832, first public 2018-05-28; https://arxiv.org/abs/1805.10832.
