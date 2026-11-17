# Exact entropy-gauge summation deficit and rigidity of logarithmic quasi-Banach sequences

## Finding

Let \(n\ge2\) be an integer, \(\mathbb F\in\{\mathbb R,\mathbb C\}\), and let \(X\) be the quasi-Banach sequence space of all \(x=(x_j)_{j\ge1}\) for which the **coordinate-entropy gauge**
\[
\mathcal E(x)=s(x)+\sum_{j:|x_j|>0}|x_j|\log\frac{s(x)}{|x_j|},\qquad s(x)=\sum_{j\ge1}|x_j|,
\]
is finite, with \(\mathcal E(0)=0\) and natural logarithms. This is the first explicit homogeneous gauge in Corollary 4.2 of Cabello Sánchez et al. (2026), at logarithmic exponent one; it is not the different increasing-rank rearrangement gauge in the same corollary.

**Sharp finite-summand theorem.** For all \(x_1,\ldots,x_n\in X\),
\[
\boxed{\ \mathcal E\!\left(\sum_{i=1}^{n}x_i\right)\le(1+\log n)\sum_{i=1}^{n}\mathcal E(x_i).\ }
\]
The coefficient is optimal. If \(\sum_i s(x_i)>0\), equality holds **if and only if** there exist distinct coordinates \(j_1,\ldots,j_n\), a number \(a>0\), and scalars \(\zeta_i\in\mathbb F\) with \(|\zeta_i|=1\), such that \(x_i=a\zeta_i e_{j_i}\) for every \(i\).

**Exact four-term deficit identity.** Write \(b_j=\sum_i|x_i(j)|\), \(y_j=\sum_i x_i(j)\), \(S=\sum_j b_j>0\), and \(\pi_{ij}=|x_i(j)|/S\). Let \(I\) and \(J\) be the discrete random indices with joint law \(\pi\); thus \(\alpha_i=\Pr(I=i)=s(x_i)/S\). Write \(u_n\) for the uniform distribution on \(\{1,\ldots,n\}\), \(D(\alpha\Vert u_n)=\sum_{i:\alpha_i>0}\alpha_i\log(n\alpha_i)\), and use natural-log Shannon entropy. Then
\[
\boxed{\begin{aligned}
&(1+\log n)\sum_i\mathcal E(x_i)-\mathcal E(y)\\
&=S D(\alpha\Vert u_n)+S(\log n)H(J\mid I)
  +S H(I\mid J)+\bigl[\mathcal E(b)-\mathcal E(y)\bigr].
\end{aligned}}
\]
Every term on the right is nonnegative; the final term measures cancellation.

**Quantitative rigidity.** Let the left-hand deficit divided by \(S\) be \(\delta\). Then
\[
\sum_i|\alpha_i-1/n|\le\sqrt{2\delta},\qquad
H(J\mid I)\le\frac{\delta}{\log n}.
\]
If \(\delta\le1/(8n^2)\), there exist **pairwise distinct** coordinates \(j_1,\ldots,j_n\) such that
\[
\boxed{\ \sum_i\sum_{j\ne j_i}|x_i(j)|\le\frac{S\delta}{\log n}.\ }
\]
Thus the sharp quasi-triangle extremizers are quantitatively isolated, modulo their supports, common magnitude and scalar phases, even for complex sequences.

## Assumptions and scope

The field is real or complex; the coordinate set is countably infinite; \(n\ge2\); every input has finite \(\mathcal E\). Zeros and arbitrary cancellations are allowed. Entropies of conditional laws are defined with \(0\log0=0\) and with zero-mass rows omitted. Finiteness of the input gauges implies \(H(J\mid I)<\infty\), hence \(H(J)<\infty\) because \(I\) has at most \(n\) states. The conclusion therefore holds on the complete quasi-Banach sequence space, not only its finite-support subspace.

For \(S=0\) all inputs vanish and the inequality is an equality; the nonzero equality classification and deficit identity apply only when \(S>0\). This theorem addresses the **specific** entropy gauge above. Constants for other equivalent Luxemburg or rearrangement gauges are not asserted to coincide.

## Proof

**1. Monotonicity and normalization.** For finite nonnegative vectors \(a\) of total mass \(T>0\),
\[\mathcal E(a)=T+T\log T-\sum_j a_j\log a_j.\]
Consequently, at a strictly positive coordinate, \(\partial\mathcal E/\partial a_j=1+\log(T/a_j)\ge1\). By continuity at zero and finite truncation, coordinatewise \(0\le a\le b\) implies \(\mathcal E(a)\le\mathcal E(b)\) whenever the upper gauge is finite; finite-coordinate truncations converge to the full gauge by the entropy chain rule or monotone convergence of \(\mathcal E\) under adding nonnegative coordinates. In particular \(\mathcal E(y)\le\mathcal E(b)\).

For \(S>0\), put \(\alpha_i=s(x_i)/S\), \(p_{j\mid i}=|x_i(j)|/s(x_i)\) when \(\alpha_i>0\), and \(\beta_j=b_j/S\). By the definition of Shannon entropy,
\[
\sum_i\mathcal E(x_i)=S\bigl(1+H(J\mid I)\bigr),\qquad
\mathcal E(b)=S\bigl(1+H(J)\bigr).
\]
The elementary identity \(H(I,J)=H(I)+H(J\mid I)=H(J)+H(I\mid J)\) yields
\[H(J)=H(I)+H(J\mid I)-H(I\mid J).\]
Substitute into the last two equations and use \(\log n-H(I)=D(\alpha\Vert u_n)\). Adding \(\mathcal E(b)-\mathcal E(y)\) proves the four-term identity exactly. Entropy and divergence are nonnegative and \(\log n>0\), proving the sharp inequality.

**2. Sharpness and complete equality.** Choose distinct coordinates and let \(x_i=a\zeta_i e_{j_i}\). Then \(\sum_i\mathcal E(x_i)=na\), whereas \(\mathcal E(\sum_i x_i)=na(1+\log n)\), so the constant is attained. Conversely, if the deficit vanishes, every nonnegative term in the identity vanishes. \(D(\alpha\Vert u_n)=0\) forces \(\alpha_i=1/n\) for all \(i\); \(H(J\mid I)=0\) forces each nonzero input to be supported at exactly one coordinate; and \(H(I\mid J)=0\) forces those coordinates to be distinct (if two positive rows occupied one coordinate, the conditional law of \(I\) at that coordinate would have positive entropy). The equal row masses imply a common modulus \(a\). Conversely these data make every defect term zero.

**3. Quantitative stability.** Dividing the exact identity by \(S\) gives \(D(\alpha\Vert u_n)\le\delta\), \((\log n)H(J\mid I)\le\delta\), and \(H(I\mid J)\le\delta\). Pinsker's inequality for natural logarithms gives \(\|\alpha-u_n\|_1\le\sqrt{2\delta}\). For each row of positive mass, choose a coordinate \(j_i\) of maximal conditional probability \(p_i^*=\max_j p_{j\mid i}\). Such a maximum exists for any probability sequence on a countable set. Since \(H(p_{\cdot\mid i})\ge-\log p_i^*\ge1-p_i^*\),
\[
\sum_i\sum_{j\ne j_i}|x_i(j)|=S\sum_i\alpha_i(1-p_i^*)\le S H(J\mid I)\le\frac{S\delta}{\log n}.
\]
It remains to prove the chosen coordinates are distinct under the stated small-deficit assumption. If \(\delta\le1/(8n^2)\), Pinsker and the fact that a single coordinate deviation is at most half the total variation give
\[\alpha_i\ge1/n-\sqrt{\delta/2}\ge 3/(4n).\]
Also \(H(p_{\cdot\mid i})\le\delta/(\alpha_i\log n)\le1/(6n\log n)\le1/(12\log2)<\log2\). Thus \(p_i^*>1/2\). If two chosen maxima coincide at a column \(j\), that column has unnormalized joint masses at least \(3/(8n)\) in each of two distinct rows. For any pair of masses \(v,w>0\), the binary entropy inequality
\[(v+w)h\!\left(\frac{v}{v+w}\right)\ge2(\log2)\min(v,w)\]
shows that the contribution of that column to \(H(I\mid J)\) is at least \(3\log2/(4n)\), strictly greater than \(1/(8n^2)\ge\delta\). Contradiction. The chosen coordinates are pairwise distinct. This completes the stability claim.

The monotone truncation argument is independent of the sign or phase of the inputs. No finite experiment is used to infer an infinite-dimensional statement.

## Verification

The proof is self-contained from the displayed definitions, the elementary Shannon chain rule, and the standard Pinsker inequality. The accompanying standard-library script checks the four-term identity and nonnegative deficits on 8,400 deterministic random real finite arrays of varying sizes, plus exact-attainment arrays. These are diagnostics, not a substitute for the all-dimensional proof. Execute \(`python3 check.py`\) after extracting the embedded files.

The only nonstandard infinite-sequence step is truncation continuity of \(\mathcal E\) for nonnegative sequences of finite entropy: the finite-prefix masses increase to the total mass, the finite-prefix entropy numerator \(-\sum a_j\log a_j\) converges after splitting finitely many entries above one from the tail below one, and the resulting finite-prefix gauges increase to the complete value. This justifies passage from finite to countable coordinates.

## Relationship to prior work

Cabello Sánchez, Castillo, Martínez-Bohórquez and Navarro Garmendia (2026) introduce this exact coordinate-entropy homogeneous quasi-gauge as an equivalent model for logarithmic Orlicz spaces (Corollary 4.2) and prove logarithmic-order, rather than exact all-\(n\), summation estimates for their Serre-closure criterion (Lemma 4.3 and related results). Their second equivalent gauge is based on increasing logarithmic **rank weights**, whereas this result uses entropy of coordinate masses. The precise constants of equivalent quasi-gauges are not interchangeable.

Kalton (1981) supplies the earlier log-convexity and three-space context, not a claimed novelty in Shannon's chain rule. Other research on concave-Orlicz gauges yields sharp leading asymptotic amplification for different Luxemburg-type models. Neither the general chain rule nor any equivalence between gauge topologies by itself determines the present exact summation coefficient, equality family, or quantitative cancellation/overlap deficit identity.

## Limitations

The theorem is specific to the exponent-one coordinate-entropy gauge; no exact analogue for higher logarithmic powers, and no equality classification for alternative equivalent quasinorms, is claimed. The stability threshold \(1/(8n^2)\) is a convenient sufficient cutoff and is **not** asserted to be sharp. The probability identities are standard; novelty concerns their exact synthesis into the named quasi-Banach summation problem. Earlier literature under information-theoretic or entropy-sequence terminology might imply the same theorem and requires further independent priority review. No independent mathematical audit has been performed.

## References

1. F. Cabello Sánchez, J. M. F. Castillo, R. Martínez-Bohórquez, J. Navarro Garmendia, *The Serre closure of Banach spaces*, arXiv:2610.35259v1 (first submitted 26 October 2026), especially §3 and Corollary 4.2 in §4. https://arxiv.org/abs/2610.35259
2. N. J. Kalton, *Convexity, type and three space problem*, Studia Mathematica 69 (1981), 247–287. DOI: 10.4064/sm-69-3-247-287. https://doi.org/10.4064/sm-69-3-247-287
