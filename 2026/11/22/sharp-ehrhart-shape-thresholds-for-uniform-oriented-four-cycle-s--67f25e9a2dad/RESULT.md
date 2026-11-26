# Sharp Ehrhart-shape thresholds for uniform oriented four-cycle simplices

## Finding

For each integer \(w\ge2\), let \(e_j\) be the standard basis of \(\mathbb R^4\), with indices taken modulo four, and put \(P_w=\operatorname{conv}\{e_j+w e_{j-1}:1\le j\le4\}\). Its Ehrhart coefficient sequence is unimodal exactly for \(w\ge3\) and log-concave exactly for \(w\ge5\). Its Ehrhart numerator has only simple, real, strictly negative roots exactly for \(w\ge7\). In particular the last range gives the exact first weight for real-rootedness in this family, which is already known to be non-IDP at every \(w\ge2\).

## Assumptions and scope

The lattice on the affine span is induced from \(\mathbb Z^4\). Write \(\sum_{m\ge0}|mP_w\cap\mathbb Z^4|t^m=h^*(t)/(1-t)^4\). Unimodality means weakly increasing and then weakly decreasing; log-concavity means the two interior adjacent inequalities for the sequence \((h_0^*,h_1^*,h_2^*,h_3^*)\), including its trailing zero when \(w=2\). No assertion is made for other cycle sizes, orientations or nonuniform weights.

## Proof

**Input coefficients.** We give the specialization of prior lattice-point and symmetry results used in the shape test. The column matrix of vertices is \(M=I+wS\), where \((Sc)_i=c_{i+1}\). It has determinant \(1-w^4\), and the coordinate sum scales by \(w+1\). Thus the vertices are affinely independent and lie on \(\sum x_i=w+1\). On the quotient of \(\mathbb Z^4\) by the primitive sum-zero difference lattice, \(M\) multiplies by \(w+1\); on that difference lattice its determinant in absolute value is the normalized volume of \(P_w\). The volume is consequently \((w^4-1)/(w+1)=w^3-w^2+w-1\).

Reversing the vertex labels identifies the simplex with the equally weighted naturally oriented four-cycle of [1,2]. The nonvertex lattice points are exactly positive integer vectors summing to \(w+1\) by [1, Proposition 3.10], giving \(h_1^*=|P_w\cap\mathbb Z^4|-4=\binom w3\). Shifted reciprocity [2] gives \(h_3^*=h_1^*\). Subtracting these two coefficients and \(h_0^*=1\) from the volume gives
\[
h^*(t)=1+at+bt^2+at^3,\qquad a=\binom w3,\quad b=(2w^3+w-6)/3.
\]
The binomial coefficient is zero when \(w=2\). The non-IDP statement is [1, Theorem 4.5].

**Unimodality and log-concavity.** The difference \(b-a=(w^3+w^2-4)/2\) is positive for \(w\ge2\), so \((1,a,b,a)\) is unimodal exactly when \(a\ge1\), i.e. \(w\ge3\). The only potentially failing log-concavity inequality is \(a^2\ge b\). At \(w=2,3,4\), the respective differences \(a^2-b\) are \(-4,-16,-26\). For \(w=5+u\), \(u\ge0\), the identity
\[
36(a^2-b)=u^6+24u^5+238u^4+1224u^3+3289u^2+3828u+612
\]
proves positivity, hence the cutoff at five.

**Strict negative real-rootedness.** At \(w=2\) the numerator is \(1+4t^2\), with nonreal zeros. For \(w=3,4,5,6\), respectively, the discriminants of the cubic are \(-19088,-257488,-1491548,-3263536\), so none has three real zeros. For \(w\ge7\) set \(g(x)=1-ax+bx^2-ax^3\). We have \(g(0)=1>0\), \(g(1)=b-2a+1=(w-1)(w+1)(w+3)/3>0\), and \(g(x)\to-\infty\) as \(x\to\infty\). Here \(0<2/a<1\) and \(g(2/a)=-1+(4b-8)/a^2<0\) since, for \(w=7+u\),
\[
36(a^2-4b+8)=u^6+36u^5+538u^4+4176u^3+16993u^2+30780u+11412.
\]
The three sign changes exhibit one positive root of \(g\) in each of \((0,2/a),(2/a,1),(1,\infty)\); degree three makes them all simple and all the roots. Negating the roots proves the stated threshold for \(h^*\).

## Verification and relationship to other work

The supplied `checker.py` uses integer and rational arithmetic for the predicted coefficients, interior lattice points, finite dilation counts and root tests at weights two through nine. The infinite weight classification uses the inequalities and signs above, not extrapolation from those counts.

The exact polynomial used as input here follows from the prior count, general shifted reciprocity and the volume; it is not claimed as a new invariant. The same shifted-reciprocity work [2] gives a log-concavity threshold for the five-cycle, not the four-cycle. The general large-width theorem [3] already implies eventual simple negative real-rootedness along this family: a nonconstant integral functional represented by coefficient vector \(u\) modulo constants varies across the vertices by at least \((w-1)(\max_i u_i-\min_i u_i)\) by comparing the shifted copies of its maximum and minimum. That theorem is qualitative for the present purpose and does not give the first permissible weight. Likewise, oriented-cycle root polytopes defined from differences of basis vectors are not these weighted exponent simplices. The claim here is the exact comparison of the three finite cutoffs for one natural family, not the discovery of the weighted model, shifted reciprocity, non-IDP, or eventual real-rootedness at large width.

## References

1. J. Biermann, K.-N. Lin and A. O'Keefe, *Integer Decomposition Property of Edge Polytopes of Weighted Oriented Graphs*, [arXiv:2611.17047](https://arxiv.org/abs/2611.17047), Proposition 3.10 and Theorem 4.5.
2. [*Shifted Ehrhart symmetry and a sharp log-concavity threshold for weighted directed-cycle simplices*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-shifted-ehrhart-symmetry-and-a-sharp-log-concavity-threshold-for--b7680edb541b), shifted reciprocity and the five-cycle threshold.
3. B. Nill, [arXiv:2608.03635](https://arxiv.org/abs/2608.03635), Theorem 1.1, large lattice width and negative real roots.
