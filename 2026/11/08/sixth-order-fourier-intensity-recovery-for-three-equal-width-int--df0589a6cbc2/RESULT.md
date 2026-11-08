# Sixth-order Fourier-intensity recovery for three equal-width intervals

## Finding
Let \(E\subset\mathbb R\) be the union of exactly three pairwise disjoint intervals of one common, *a priori unknown*, length. Write
\[
E=[x_0,x_0+L]\cup[x_0+u,x_0+u+L]\cup[x_0+u+v,x_0+u+v+L],
\qquad L>0,\quad u>L,\quad v>L.
\]
For angular Fourier frequency \(t\), set
\[
I(t)=\left|\int_E e^{-itx}\,dx\right|^2.
\]
The three numbers \(I(0)\), \(I''(0)\), and \(I^{(6)}(0)\) determine \(E\) up to translation and reflection, with the explicit reconstruction below. The intervening fourth derivative is redundant: \(I^{(4)}(0)\) is determined by \(I(0)\) and \(I''(0)\), and the entire Fourier-intensity jet through order five is insufficient for uniqueness. Thus **six is the minimal derivative order** for universal finite-jet recovery within this equal-width, three-interval class.

Define \(L=\sqrt{I(0)}/3\) and
\[
P_2=-\frac{I''(0)}{2L^2}-\frac34L^2,
\qquad P_4=\frac{P_2^2}{2},
\]
\[
P_6=-\frac{I^{(6)}(0)+5L^4P_4+2L^6P_2+\frac9{28}L^8}{2L^2},
\qquad A=\frac{P_2}{2}.
\]
There is a unique \(Q\in(0,A/3]\) satisfying
\[
3Q^2(A+Q)=P_6-2A^3.
\]
The two consecutive start spacings, unordered, are exactly
\[
\boxed{\quad
\{u,v\}=\left\{\frac{\sqrt{A+Q}+\sqrt{A-3Q}}2,
\frac{\sqrt{A+Q}-\sqrt{A-3Q}}2\right\}.\quad}
\]
The physical gaps between consecutive intervals are \(u-L\) and \(v-L\). Their order is the unavoidable reflection ambiguity.

The realizable derivative triples admit an exact test: after applying the displayed definitions, require \(L>0\), \(A>0\),
\[
0<P_6-2A^3\le\frac49 A^3,
\]
and require the smaller reconstructed spacing to exceed \(L\). These conditions are necessary and sufficient for realization by exactly three strictly disjoint equal-length intervals.

On any compact parameter family bounded away from zero length and zero physical gaps, the inverse is uniformly Hölder with exponent \(1/2\) in the three jet data, and is locally Lipschitz wherever \(u\ne v\). The exponent \(1/2\) cannot be improved at configurations with \(u=v>L\).

## Assumptions and scope
The intervals are real, bounded, and all have the same unknown positive length \(L\); consecutive starting-point separations are \(u,v>L\). Endpoint inclusion is immaterial. The comparison class for uniqueness has exactly the same structural assumption (three equal-length disjoint intervals); uniqueness is **not** asserted among arbitrary unions of intervals or arbitrary measurable sets. Fourier convention is angular, \(\widehat f(t)=\int f(x)e^{-itx}\,dx\); no \(2\pi\) appears in the exponent. Derivatives are exact values at \(t=0\).

For stability let \(\mathcal K\) be any compact collection of parameter triples \((L,u,v)\) contained in \(\{L>0,u>L,v>L\}\). If \(J(L,u,v)=(I(0),I''(0),I^{(6)}(0))\), and
\[
d((L,u,v),(L',u',v'))=|L-L'|+
\min\bigl\{|u-u'|+|v-v'|,\,|u-v'|+|v-u'|\bigr\},
\]
then some \(C_{\mathcal K}<\infty\) satisfies
\[
d\bigl((L,u,v),(L',u',v')\bigr)
\le C_{\mathcal K}\,\|J(L,u,v)-J(L',u',v')\|_\infty^{1/2}
\]
for all pairs in \(\mathcal K\). On compact subfamilies satisfying \(|u-v|\ge\eta>0\), the right side may instead use exponent \(1\).

## Proof
Translate the left endpoint to zero and put \(\operatorname{sinc}(z)=\sin(z)/z\), with value \(1\) at zero. Factoring the common interval transform gives
\[
I(t)=L^2\operatorname{sinc}^2(Lt/2)
\bigl[3+2\cos(ut)+2\cos(vt)+2\cos((u+v)t)\bigr]. \tag{1}
\]
The first factor is nonzero near zero and the second is even. With
\(P_{2j}=u^{2j}+v^{2j}+(u+v)^{2j}\), the second factor expands as
\[
9-P_2t^2+\frac{P_4}{12}t^4-\frac{P_6}{360}t^6+O(t^8).
\]
Meanwhile
\[
\operatorname{sinc}^2(Lt/2)
=1-\frac{L^2t^2}{12}+\frac{L^4t^4}{360}
-\frac{L^6t^6}{20160}+O(t^8).
\]
Multiplying verifies, with no omitted factorials,
\[
I(0)=9L^2,\qquad I''(0)=-2L^2P_2-\frac32L^4,
\]
\[
I^{(4)}(0)=2L^2P_4+2L^4P_2+\frac35L^6,
\]
\[
I^{(6)}(0)=-2L^2P_6-5L^4P_4-2L^6P_2-\frac9{28}L^8. \tag{2}
\]
This proves the formulas recovering \(L,P_2,P_6\).

Write \(A=u^2+uv+v^2\) and \(Q=uv\). Direct expansion gives the two key identities
\[
P_2=2A,\qquad P_4=2A^2=\frac{P_2^2}{2},
\qquad P_6=2A^3+3Q^2(A+Q). \tag{3}
\]
The second identity proves fourth-derivative redundancy, namely the explicit relation
\[
I^{(4)}(0)=L^2P_2^2+2L^4P_2+\frac35L^6.
\]
Since \(u,v>0\), \(Q>0\); and \(A-3Q=(u-v)^2\ge0\), so \(Q\le A/3\). The map \(Q\mapsto3Q^2(A+Q)\) has positive derivative \(3Q(2A+3Q)\) for \(Q>0\). Thus equation (3) determines precisely one \(Q\) in the admissible interval. Because \((u+v)^2=A+Q\) and \((u-v)^2=A-3Q\), the displayed reconstruction follows. The maximum at \(Q=A/3\) is \(4A^3/9\), proving both directions of the realizability test after checking \(\min(u,v)>L\).

Every odd derivative of \(I\) at zero vanishes by evenness. At fixed \(L\) and \(A\), equation (3) shows that \(I(0),I''(0),I^{(4)}(0)\), and hence the entire order-five jet, remain fixed. The positive ellipse \(u^2+uv+v^2=A\) contains a nontrivial arc around each interior admissible pair \(u,v>L\). Distinct points on that arc need not be related by interchanging \(u,v\). Hence no order-five jet is globally injective.

For stability, on \(\mathcal K\), equation (2) makes \(L,A,P_6\) Lipschitz functions of the three measured derivatives. The admissible \(Q=uv\) has a positive lower bound on \(\mathcal K\), so the inverse of \(Q\mapsto3Q^2(A+Q)\) is uniformly Lipschitz there, including under variation of \(A\). The expression \(\sqrt{A+Q}\) is Lipschitz, while \(|\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}\) for \(x,y\ge0\). This yields the stated uniform exponent \(1/2\). If \(|u-v|\ge\eta\) on the chosen compact family, \(A-3Q\) stays uniformly positive and both square roots are Lipschitz.

Sharpness at the reflection-symmetric configuration follows by fixing \(L>0\), \(w>L\) and \(A=3w^2\), then setting, for small \(\varepsilon>0\),
\[
Q_\varepsilon=\frac A3-\frac{\varepsilon^2}{3},\quad
u_\varepsilon=\frac{\sqrt{A+Q_\varepsilon}+\varepsilon}{2},\quad
v_\varepsilon=\frac{\sqrt{A+Q_\varepsilon}-\varepsilon}{2}.
\]
Here \(u_\varepsilon,v_\varepsilon>L\), their distance from \((w,w)\) up to interchange is of order \(\varepsilon\), and their \(I(0),I''(0),I^{(4)}(0)\) are identical to those at \((w,w)\). Differentiating the polynomial in (3) at \(Q=A/3\) gives
\[
P_6(u_\varepsilon,v_\varepsilon)-P_6(w,w)
=-A^2\varepsilon^2+O(\varepsilon^4),
\]
so \(I^{(6)}_\varepsilon(0)-I^{(6)}_0(0)
=2L^2A^2\varepsilon^2+O(\varepsilon^4)\). No inverse Hölder exponent greater than \(1/2\) is possible there.

## Verification
Run the standalone script `python CHECK.py` with Python 3, SymPy and mpmath installed. It symbolically checks the three power-sum identities and the Fourier-intensity Taylor coefficients through sixth order; checks the feasibility endpoint and monotonicity derivative; reconstructs the parameters at 27 rationally generated positive examples (including coincident consecutive spacings); and tests the sharp square-root perturbation across four scales. The recorded execution produced `EQUAL_WIDTH_THREE_INTERVAL_JET_CHECKS_PASSED 164`. These tests verify formulas at finite examples, while the preceding algebra supplies the proofs for arbitrary real parameters.

## Relationship to prior work
Xia and Xu (2026) establish Fourier-magnitude uniqueness for one or two intervals and show that general unions of three or more intervals need not be unique. Their separation-condition result yields a sufficient global-magnitude uniqueness criterion. The present class is different: it assumes three *equal widths* and determines the **minimal order of a single local intensity jet**; its explicit sixth-order inverse, fourth-order blind spot, exact feasibility criterion, and sharp local Hölder threshold are not consequences of the cited full-data uniqueness/nonuniqueness statements.

Huang and Dokmanić (2018/2021) study recovery of point configurations from the entire multiset of pairwise distances and its noisy variants. Their full-distance-data approach explains why three start locations have natural turnpike structure, but does not imply that the two low-order Fourier-intensity derivatives suffice once interval width is factored out or that the fourth order is redundant. The present result is specific to three equal-width intervals rather than a general turnpike algorithm.

## Limitations
There is no claim of uniqueness among arbitrary unequal-width three-interval objects, among general real signals, or when the number of intervals is unknown. Stability is with respect to **exact local derivative data**, not directly measured noisy intensities on a frequency grid; computing sixth derivatives experimentally can amplify noise. The uniform stability estimate requires compact positive bounds on lengths and interval gaps and worsens at symmetrical configurations, where exponent \(1/2\) is optimal. No claim of publication priority or independent audit is made.

## References
1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, first publicly submitted 2026-06-18. https://arxiv.org/abs/2606.19855
2. Shuai Huang and Ivan Dokmanić, *Reconstructing Point Sets from Distance Distributions*, arXiv:1804.02465 (2018); IEEE Transactions on Signal Processing 69 (2021), 1811–1827. https://arxiv.org/abs/1804.02465
