# Ptolemy constants certify exact Euclidean distortion for two max-norm planes
## Finding
For \(2^{-1/2}\le \lambda\le 1\), let \(A_\lambda=(\mathbb R^2,N^{(1)}_\lambda)\) with \(N^{(1)}_\lambda(x)=\max\{\|x\|_2,\lambda\|x\|_1\}\). For \(1\le \lambda\le \sqrt2\), let \(B_\lambda=(\mathbb R^2,N^{(\infty)}_\lambda)\) with \(N^{(\infty)}_\lambda(x)=\max\{\|x\|_2,\lambda\|x\|_\infty\}\). Then \(d_{\mathrm{BM}}(A_\lambda,\ell_2^2)^2=C_{\mathrm{Pt}}(A_\lambda)=2\lambda^2\) and \(d_{\mathrm{BM}}(B_\lambda,\ell_2^2)^2=C_{\mathrm{Pt}}(B_\lambda)=\lambda^2\). Thus the obvious Euclidean identity-map distortions are globally optimal over all linear isomorphisms in both parameter ranges.

Here \(C_{{\mathrm{{Pt}}}}\) denotes the Ptolemy constant and \(d_{{\mathrm{{BM}}}}\) the multiplicative Banach--Mazur distance. The conclusion is affine, not merely coordinatewise: no nontrivial linear change of variables improves the displayed Euclidean distortion.

## Assumptions and scope
The spaces are real two-dimensional normed spaces. In the first family the parameter range is exactly \(2^{{-1/2}}\le\lambda\le1\); in the second it is exactly \(1\le\lambda\le\sqrt2\). The endpoint cases are included. The source literature proves the exact Ptolemy values for these same norm families: \(C_{{\mathrm{{Pt}}}}(A_\lambda)=2\lambda^2\) and \(C_{{\mathrm{{Pt}}}}(B_\lambda)=\lambda^2\).

## Proof
First note a general inequality. Let \(X=(V,N)\) be a finite-dimensional real normed space and let \(T:V\to\ell_2^n\) be an isomorphism. Put \(|x|_T=\|Tx\|_2\). Then
\[
\frac{1}{\|T\|}\,|x|_T\le N(x)\le \|T^{{-1}}\|\,|x|_T.
\]
For two equivalent norms satisfying \(a|x|\le N(x)\le b|x|\), the elementary norm-comparison estimate for the Ptolemy constant gives \(C_{{\mathrm{{Pt}}}}(N)\le(b/a)^2 C_{{\mathrm{{Pt}}}}(|\cdot|)\). Since a Euclidean norm has Ptolemy constant \(1\), every \(T\) therefore satisfies
\[
C_{{\mathrm{{Pt}}}}(X)\le \bigl(\|T\|\,\|T^{{-1}}\|\bigr)^2.
\]
Taking the infimum over \(T\) yields
\[
C_{{\mathrm{{Pt}}}}(X)\le d_{{\mathrm{{BM}}}}(X,\ell_2^n)^2. \tag{1}
\]

For \(A_\lambda\), the inequalities \(\|x\|_1\le\sqrt2\,\|x\|_2\) and \(N_\lambda^{{(1)}}(x)\ge\|x\|_2\) give
\[
\|x\|_2\le N_\lambda^{{(1)}}(x)\le\sqrt2\,\lambda\,\|x\|_2,
\]
because \(\sqrt2\lambda\ge1\) on the stated range. Hence the identity map gives
\[
d_{{\mathrm{{BM}}}}(A_\lambda,\ell_2^2)\le\sqrt2\,\lambda.
\]
Zuo's Example 2.6 proves \(C_{{\mathrm{{Pt}}}}(A_\lambda)=2\lambda^2\). Combining this with (1) forces equality throughout:
\[
\sqrt2\,\lambda=\sqrt{{C_{{\mathrm{{Pt}}}}(A_\lambda)}}\le d_{{\mathrm{{BM}}}}(A_\lambda,\ell_2^2)\le\sqrt2\,\lambda.
\]

For \(B_\lambda\), \(\|x\|_\infty\le\|x\|_2\) gives
\[
\|x\|_2\le N_\lambda^{{(\infty)}}(x)\le\lambda\,\|x\|_2.
\]
Thus \(d_{{\mathrm{{BM}}}}(B_\lambda,\ell_2^2)\le\lambda\). Zuo's Example 2.7 proves \(C_{{\mathrm{{Pt}}}}(B_\lambda)=\lambda^2\), and (1) again gives the matching lower bound. Therefore \(d_{{\mathrm{{BM}}}}(B_\lambda,\ell_2^2)=\lambda\).

## Verification
The argument was checked at all four parameter endpoints. For \(A_{{2^{{-1/2}}}}\), the max norm reduces to the Euclidean norm and both invariants equal \(1\); for \(A_1\), it reduces to \(\ell_1^2\) and both squared distance and Ptolemy constant equal \(2\). For \(B_1\), the max norm is Euclidean; for \(B_{{\sqrt2}}\), both quantities equal \(2\). The proof uses no finite enumeration or numerical approximation. Its only imported scientific input is the exact Ptolemy formulas for the two source families; the Banach--Mazur lower bound is proved directly from norm equivalence and applies to every linear isomorphism.

## Relationship to prior work
Zuo (2012) introduced the two max-norm examples in the course of computing Ptolemy constants of absolute normalized norms and proved the exact values used above. The paper does not state Banach--Mazur distances. Llorens-Fuster, Mazcuñán-Navarro and Reich (2010) developed Ptolemy-constant bounds under renorming; this supplies the same general comparison mechanism but does not, in the inspected material, identify these two max-norm families with exact Euclidean Banach--Mazur distances. Zuo (2018) generalized several Ptolemy computations for comparable absolute normalized norms; its full text likewise contains no Banach--Mazur terminology. The new point is that the exact Ptolemy values meet the universal lower bound \(C_{{\mathrm{{Pt}}}}(X)\le d_{{\mathrm{{BM}}}}(X,\ell_2^2)^2\), certifying that the elementary coordinate comparison is already affine-optimal.

## Limitations
The claim concerns only the two displayed parameterized planes and their distance to \(\ell_2^2\). It does not classify all absolute normalized norms for which \(C_{{\mathrm{{Pt}}}}=d_{{\mathrm{{BM}}}}^2\), nor does it assert uniqueness of an optimizing linear isomorphism. A targeted literature search found no prior statement of these exact Banach--Mazur formulas, but unindexed literature could still contain an equivalent formulation. One plausible 2010 source was available only through an abstract and section snippets in this review; an a lawful full-text copy was not available during the literature check and was not used as evidence for a noncoverage claim.

## References
1. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2012, 107 (2012), DOI 10.1186/1029-242X-2012-107. Published 17 May 2012; primary classification 46B20.
2. E. Llorens-Fuster, E. M. Mazcuñán-Navarro, and S. Reich, “The Ptolemy and Zbăganu constants of normed spaces,” *Nonlinear Analysis* 72 (2010), 3984–3993, DOI 10.1016/j.na.2010.01.030.
3. Z.-F. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” *Mathematical Inequalities & Applications* 21 (2018), 945–956, DOI 10.7153/mia-2018-21-64.
