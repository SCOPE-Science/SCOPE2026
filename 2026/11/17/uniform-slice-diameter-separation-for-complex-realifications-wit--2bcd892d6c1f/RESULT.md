# Uniform slice-diameter separation for complex realifications with the alternative Daugavet property

## Finding

For every nonzero complex Banach space \(X\) with the alternative Daugavet property (ADP) on its **underlying real space** \(X_{\mathbb R}\), every nonempty slice \(S\) of the real unit ball obeys
\[
\operatorname{diam}(S)\ \ge\ 2-\sqrt2.
\]
Consequently, the natural slice-diameter index
\[
\delta_{\mathrm{slice}}(X_{\mathbb R}):=\inf_{S\ \mathrm{real\ slice\ of}\ B_X}\operatorname{diam}(S)
\]
is at least \(2-\sqrt2\). In particular there are no denting points of \(B_X\), and \(X_{\mathbb R}\) does not have the Radon–Nikodým property.

## Assumptions and scope

A real slice means \(S=S(B_X,f,\alpha)=\{v\in B_X:f(v)>1-\alpha\}\), with a real-linear functional \(f\in S_{(X_{\mathbb R})^*}\) and \(\alpha>0\). Every such slice is nonempty. The norm is the original complex Banach norm, regarded as a real norm. ADP is tested against **real-linear rank-one** maps: \(\max_{\sigma\in\{-1,1\}}\|I+\sigma T\|=1+\|T\|\). The quantifier is every nonzero complex Banach space and every real slice, without separability, dimension or reflexivity assumptions.

## Proof

Fix a real slice \(S\). Since \(\sup_{v\in B_X}f(v)=1\), there exists a vector \(x\in S\cap S_X\): choose a unit vector on which \(f\) exceeds \(1-\alpha\). Regard \(z=ix\) as a unit vector of \(X_{\mathbb R}\). The standard real-ADP slice criterion (Martín–Oikhberg, Proposition 2.1(iii)) gives
\[
\sup_{y\in S}\max_{\sigma\in\{-1,1\}}\|z+\sigma y\|=2.
\]
For every \(y\in S\), and for both choices of sign, the triangle inequality and complex homogeneity give
\[
\|ix\pm y\|\le\|ix\pm x\|+\|y-x\|
=\sqrt2+\|y-x\|\le\sqrt2+\operatorname{diam}(S).
\]
Taking the maximum over signs and supremum over \(y\in S\) proves \(2\le\sqrt2+\operatorname{diam}(S)\), hence the stated bound. The estimate is uniform because the identity \(\|ix\pm x\|=\sqrt2\|x\|\) holds in every complex normed space.

A denting point is contained in slices of arbitrarily small diameter, contradicting the bound. A nonzero Banach space with the Radon–Nikodým property has a dentable unit ball, so such a realification cannot have that property. The latter qualitative consequence was known independently through the link between ADP and numerical index on RNP spaces (Martín–Oikhberg, Remark 2.4), and it is not the new contribution.

## Verification

The proof is a direct norm argument with no numerical certificates or finite-model extrapolation. The only non-elementary input is the established equivalence between ADP and its real slice criterion; its quantifiers and scalar signs have been checked against the cited primary source. The sharpness of the numerical coefficient among all eligible spaces is not established.

## Relationship to prior work

Huang–Xu (arXiv:2611.06532v1, first public 2026-11-04, primary MSC 46B04) construct a separable complex Banach space with real ADP but without the complex Daugavet property. Their construction motivates quantitative geometry of this newly separated class; their paper does not state the above slice-diameter estimate. Martín–Oikhberg (2004), Proposition 2.1, supplies the exact ADP characterization used here, and Remark 2.4 together with the zero numerical radius of complex multiplication already gives a qualitative no-RNP obstruction. Thus the qualitative conclusion is not a novelty claim. Langemets–Lõo–Martín–Perreau–Rueda Zoca (2025) prove a stronger *super*-ADP property excludes the RNP, but that result does not give the displayed bound for ordinary real ADP with a complex structure. Searches under slice-diameter index, realification, alternative Daugavet property, complex structures, and rotation obstructions did not identify a directly covering bound; absence from searches is not proof of priority.

## Limitations

The constant \(2-\sqrt2\) is a proved universal **lower bound**, not claimed to be optimal. No bound on diameters of convex combinations of slices or on general weakly open sets follows. The argument does not establish the complex Daugavet property and does not classify spaces with real ADP. Known qualitative consequences (no RNP or denting points) are explicitly separated from the candidate quantitative novelty. Publication priority is subject to earlier equivalent geometric lemmas and expert review.

## References

1. J. Huang and R. Xu, *Real alternative Daugavet property without Daugavet property in a separable complex Banach space*, arXiv:2611.06532v1 (2026), https://arxiv.org/abs/2611.06532.
2. M. Martín and T. Oikhberg, *An alternative Daugavet property*, J. Math. Anal. Appl. 294 (2004), 158–180, Proposition 2.1 and Remark 2.4, https://doi.org/10.1016/S0022-247X(04)00123-4.
3. J. Langemets, M. Lõo, M. Martín, Y. Perreau, and A. Rueda Zoca, *The super alternative Daugavet property for Banach spaces*, arXiv:2504.07631v1 (2025), https://arxiv.org/abs/2504.07631.
