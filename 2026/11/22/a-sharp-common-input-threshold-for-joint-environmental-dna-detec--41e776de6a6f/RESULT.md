# A sharp common-input threshold for joint environmental DNA detection under asymmetric inhibition

## Finding

**Theorem.** Fix any real \(A,b,C>0\). Two independently assayed targets receive the same positive amount \(x\) of a homogeneous environmental DNA extract. Suppose successful amplifiable target-molecule counts are independent Poisson random variables of respective means \(Axe^{-bx}\) and \(Cx\). The probability of detecting *both* targets is
\[
F(x)=\bigl(1-e^{-Axe^{-bx}}\bigr)\bigl(1-e^{-Cx}\bigr),\qquad x>0.
\]
There is exactly one maximizer \(x_*\in(1/b,\infty)\). More sharply,
\[
\begin{aligned}
x_*&>2/b&&\Longleftrightarrow&& C<Ae^{-2},\\
x_*&=2/b&&\Longleftrightarrow&& C=Ae^{-2},\\
1/b<x_*&<2/b&&\Longleftrightarrow&& C>Ae^{-2}.
\end{aligned}
\]
Thus the optimum for a *single* inhibited assay, \(1/b\), is always strictly too small when the objective requires simultaneous detection. In the asymptotic regime \(A/C\to\infty\) with \(b,C\) fixed, \(bx_* = \log(A/C)+o(1)\).

## Assumptions and scope

The three parameters are finite and strictly positive; \(x\) is a mathematical input-volume/dose coordinate without an imposed maximum. Each target has a separate detection event conditional on that coordinate; their Poisson successful-count variables are independent. A target is detected if and only if its count is nonzero. The inhibited mean is \(Axe^{-bx}\), modeling simultaneous gain in available molecules with input and loss of amplifiability from inhibitor accumulation. The second assay is modeled as inhibitor-resistant, with mean \(Cx\). No empirical source is claimed to establish this exact exponential functional law. The result applies to this precisely stated idealized probabilistic model, not to all qPCR chemistries. If a maximum allowable input \(M>0\) is imposed, the constrained optimum follows as \(\min\{x_*,M\}\).

## Proof

Write \(y=bx\), \(u=A/b\), and \(v=C/b\); then \(u,v>0\). Put
\[
R(t)=\frac{t}{e^t-1}\quad(t>0),\qquad
G(s)=\log(1-e^{-e^s})\quad(s\in\mathbb R).
\]
The function \(R\) is positive and strictly decreasing, because
\[
R'(t)=\frac{e^t(1-t)-1}{(e^t-1)^2}<0
\]
for every \(t>0\) (the numerator starts at zero and has derivative \(-te^t<0\)). Consequently \(G'(s)=R(e^s)>0\) and \(G''(s)=e^sR'(e^s)<0\). Thus \(G\) is strictly increasing and strictly concave.

The logarithm of the objective in rescaled coordinates is
\[
\log F(y/b)=G(\log u+\log y-y)+G(\log v+\log y).
\]
Both inner arguments are strictly concave functions on \(y>0\), and their compositions with increasing concave \(G\) are strictly concave: for unequal \(y_1,y_2\), strict concavity of either inner argument and strict monotonicity of \(G\) give a strict Jensen inequality, followed by the concavity inequality for \(G\). Therefore \(\log F(y/b)\) is strictly concave. Its value tends to \(-\infty\) as \(y\downarrow0\), since each success probability tends to zero; it also tends to \(-\infty\) as \(y\to\infty\), since \(uye^{-y}\to0\) while the other success probability is bounded by one. A unique interior global maximizer therefore exists. Strict concavity makes the derivative strictly decrease and change sign exactly once.

Direct differentiation gives the exact normalized first-order equation
\[
H(y):=y\,\frac{d}{dy}\log F(y/b)
=(1-y)R(uye^{-y})+R(vy).
\]
For \(0<y\le1\) both terms are nonnegative and the second is strictly positive; hence the unique optimum obeys \(y_*>1\). At \(y=2\),
\[
H(2)=R(2v)-R(2ue^{-2}).
\]
Strict decrease of \(R\), together with uniqueness of the zero of the derivative, shows that \(y_*>2\) precisely when \(v<ue^{-2}\), is equal to \(2\) precisely when \(v=ue^{-2}\), and otherwise lies strictly between \(1\) and \(2\). Restoring parameters gives all three sharp inequalities.

For completeness, fix \(v>0\) and let \(u\to\infty\). For each fixed \(y>1\), \(R(uye^{-y})\to0\), while \(R(vy)>0\); thus \(H(y)>0\) eventually. Hence \(y_*\to\infty\). Write \(Q=uy_*e^{-y_*}\), \(V=vy_*\), and \(r=Q/V=(u/v)e^{-y_*}\). At the optimum,
\[
(y_*-1)R(Q)=R(V).
\]
Once \(y_*>2\), strict decrease of \(R\) gives \(Q>V\), so \(r>1\). Writing \(R(t)=te^{-t}/(1-e^{-t})\) gives
\[
V(r-1)=\log((y_*-1)r)+\log\frac{1-e^{-V}}{1-e^{-Q}}\le\log(y_*-1)+\log r.
\]
Since \(\log r\le r-1\), we obtain
\[
0<r-1\le\frac{\log(y_*-1)}{V-1}\longrightarrow0,
\]
where \(V=vy_*\to\infty\). Finally, \(y_*=\log(u/v)-\log r=\log(A/C)+o(1)\), proving the asymptotic claim.

## Verification

For \(A=10,b=1\), the sharp boundary is \(C=10e^{-2}\approx1.353352832366127\). With \(C=0.5\), the unique optimum is \(x_*\approx2.5574766199846604\), with joint success \(F(x_*)\approx0.6221829276335893\); with \(C=1\), \(x_*\approx2.191227443359104\); with \(C=2\), \(x_*\approx1.7370102215292271\). At the exact parameter boundary, the optimizer is exactly \(2\). These numerical examples are *illustrations*; the proof above covers every positive parameter triple.

Run the accompanying standalone `check.py` with Python 3 and SciPy to reproduce a deterministic set of bracketing, classification, and objective comparisons. A run completed 24,077 assertions over 2,006 parameter pairs and three additional high-abundance asymptotic cases. Floating-point tests do not replace the analytic proof and may require care near a saturated detection probability.

## Relationship to prior work

Acharya-Patel et al. (2024) systematically compared eDNA qPCR assay chemistries and found that field-matrix composition and PCR inhibition materially affect detection; they used dilution series and a binomial-Poisson approach for low-copy analytical assessment. Uchii et al. (2019) compared resistance to multiple inhibitors and found that no reagent consistently dominated for all matrices. Brys et al. (2023) compared multiple-marker and multiplex detection, including interference issues. None of those three inspected full-text papers stated or mathematically implied the present all-positive-parameter joint success optimum or the exact twofold-dose ratio boundary. Their experimental designs do not assume this particular exponential inhibition law, so the present theorem is a *benchmark*, not a reanalysis of their measurements. A semantically related indexed result on allocating a shared dose among independent Hill inhibition targets concerns distinct response functions and a fixed allocation budget, not optimization of two independently Poisson-detected targets under one common sample-input coordinate. A matched-title search is not proof of historical novelty, and generic log-concavity optimization may give alternative proofs of uniqueness.

## Limitations

Joint detection is more demanding than the common alternative objective of detecting *either* marker, whose optimum can differ. Amplifiability \(e^{-bx}\), independent successful counts, an entirely inhibition-resistant second target, fixed parameters and arbitrarily large input are structural idealizations. In real laboratory workflows an extraction's total volume is finite, co-extracted inhibitors differ by matrix, competition between assays and target-count dependence may occur, and template quantity is often controlled by dilution rather than unconstrained volume. No finite-sample inference, calibration, field efficacy, or experimentally verified mechanistic status is asserted. Priority against all older assay-design and pharmacodynamic optimization literature is not independently established.

## References

1. Acharya-Patel, N., Groenwold, E. T., Allison, M. J., and Helbing, C. C. (2024). “Systematic evaluation of the influence of Taq enzyme choice and amplification conditions on targeted environmental DNA assay performance and detection in field samples.” *Environmental DNA*. First published 18 June 2024. https://doi.org/10.1002/edn3.578.
2. Uchii, K., Doi, H., Okahashi, T., et al. (2019). “Comparison of inhibition resistance among PCR reagents for detection and quantification of environmental DNA.” *Environmental DNA*. First published 15 October 2019. https://doi.org/10.1002/edn3.37.
3. Brys, R., Halfmaerten, D., Everts, T., et al. (2023). “Combining multiple markers significantly increases the sensitivity and precision of eDNA-based single-species analyses.” *Environmental DNA*. First published 24 April 2023. https://doi.org/10.1002/edn3.420.
