# Sharp sixth-power norm and Euclidean distance of the five-atom real zero-mean hyperplane

## Finding
Let \(H_5=\{x\in\mathbb R^5:\sum_{i=1}^5x_i=0\}\), and for nonzero \(x\in H_5\) put \(S=\sum_i x_i^2\) and \(T=\sum_i x_i^6\). Then the complete sharp interval is
\[
\boxed{\frac{11}{180}\le\frac{T}{S^3}\le\frac{41}{80}.}
\]
Minimum equality holds exactly for permutations and nonzero real multiples of \((2,2,2,-3,-3)\). Maximum equality holds exactly for permutations and nonzero real multiples of \((4,-1,-1,-1,-1)\). Every value between the endpoints is attained. For the inherited real \(\ell_6\) norm, the exact multiplicative Banach--Mazur distance is
\[
\boxed{d_{\mathrm{BM}}((H_5,\|\cdot\|_6),\ell_2^4)^6=\frac{369}{44}.}
\]
The optimal Euclidean comparator is the ambient \(\ell_2\) norm restricted to \(H_5\). Under the uniform five-atom probability law, the same finding gives the sharp normalized sixth-to-second moment interval \([55/36,205/16]\).

## Assumptions and scope
All vectors and linear isomorphisms are real, the ambient measure has five equal atoms, and \(H_5\) is four-dimensional. The inherited norms use unnormalized sums, \(\|x\|_p=(\sum_i|x_i|^p)^{1/p}\). Define \(d_{\mathrm{BM}}(X,Y)=\inf_T\|T\|\|T^{-1}\|\) over invertible real linear maps. The inequalities exclude only the zero vector, and the stated equality cases are exhaustive up to the stated permutations and scaling.

## Proof
**1. Order-cone reduction.** Permute coordinates so that \(x_1\le\cdots\le x_5\) and let \(u_j=x_{j+1}-x_j\ge0\) for \(1\le j\le4\). Put \(v=(0,u_1,u_1+u_2,u_1+u_2+u_3,u_1+u_2+u_3+u_4)\) and \(x_i=v_i-\frac15\sum_jv_j\). This parametrizes every ordered zero-mean vector exactly. Define \(P_+=41S^3-80T\) and \(P_-=180T-11S^3\).

**2. Upper inequality and equality.** Exact expansion of \(P_+\) in the four nonnegative gap variables has 76 nonzero monomials and **every coefficient is strictly positive**. The exact rational coefficient list, including zero coefficients of the pure \(u_1^6\) and \(u_4^6\) monomials, is in `CERTIFICATE.tsv`; `verify.py` regenerates and checks it independently. In particular, coefficients of \(u_2^6\) and \(u_3^6\) are \(312/5>0\), so \(P_+=0\) requires \(u_2=u_3=0\). On this face, an exact factorization gives
\[
P_+=\frac{24}{5}u_1^2u_4^2(12u_1^2+11u_1u_4+12u_4^2).
\]
Thus a nonzero equality vector has only \(u_1>0\) or only \(u_4>0\), giving the single-outlier orbit. The witness \((4,-1,-1,-1,-1)\) has \(T/S^3=41/80\).

**3. Lower inequality and equality.** The expansion of \(P_-\) has four negative coefficients, and the following exact four-square certificate removes all of them:
\[
\begin{aligned}
Q={}&\frac{48}{5}u_1u_2u_3^2(u_3-u_2)^2
+\frac{72}{5}u_1u_2u_3u_4(u_3-u_2)^2\\
&+\frac{32}{5}u_2^2u_3^2(u_3-u_2)^2
+\frac{48}{5}u_2^2u_3u_4(u_3-u_2)^2.
\end{aligned}
\]
The remainder \(R=P_--Q\) has 68 nonzero monomials, **all with strictly positive rational coefficients**; their complete exponent/coefficient list is in `CERTIFICATE.tsv`, with exact regeneration and verification in `verify.py`. Hence \(P_-\ge Q\ge0\) throughout the nonnegative orthant. The coefficients of \(u_1^6\) and \(u_4^6\) in \(R\) equal \(208/5\), forcing \(u_1=u_4=0\) at equality. The exact remaining face is
\[
P_-\big|_{u_1=u_4=0}=\frac85 u_2^2u_3^2(9u_2^2-8u_2u_3+9u_3^2).
\]
The last quadratic equals \(5(u_2^2+u_3^2)+4(u_2-u_3)^2>0\) unless both gaps vanish. Consequently, for nonzero equality exactly one of \(u_2,u_3\) is positive, giving permutations/scalings of \((2,2,2,-3,-3)\). This vector has \(T/S^3=11/180\).

**4. Intermediate values.** The Euclidean unit sphere in the four-dimensional real space \(H_5\) is connected. The continuous moment ratio has attained endpoints, so its image is the entire closed interval between them.

**5. Optimal Euclidean distortion.** Any Euclidean comparator corresponds to a positive definite quadratic form \(Q_0\) on \(H_5\). If \(aQ_0(x)\le\|x\|_6^2\le bQ_0(x)\) holds for all \(x\), the same inequalities hold for every coordinate-permuted form, because \(\|\cdot\|_6\) is permutation invariant. Averaging over all \(120\) permutations therefore produces a quadratic form with no larger factor \(b/a\). Every permutation-invariant symmetric quadratic form on the real zero-sum hyperplane is a scalar multiple of \(S\) (diagonal coefficients and off-diagonal coefficients are each constant, and the all-ones form vanishes there). Thus the optimal distortion is \(((41/80)/(11/180))^{1/6}=(369/44)^{1/6}\).

## Verification
Run `python verify.py` with SymPy installed, using this directory as the working directory. The independent exact expansion recomputes 76 upper and 68 nonnegative lower-remainder terms, verifies both equality-face factorizations and exact witness ratios, and checks 624 additional rational zero-sum vectors. The complete nonzero coefficient certificate is `CERTIFICATE.tsv`. The finite rational samples are diagnostic; the universal proof is supplied by the exact polynomial identities, nonnegative term coefficients and symmetry averaging.

## Relationship to prior work
Riener's symmetric-polynomial half-degree principle (2010 preprint) reduces degree-six symmetric nonnegativity to at most three distinct coordinate levels but does not determine the sharp five-atom lower sixth-power constant or its equality orbit. The published *Sharp sixth-moment constant for finite subgroup-hole spectra* (published-finding corpus, 2026) proves the **upper** zero-sum sixth-moment inequality, more generally for complex vectors of arbitrary length; the upper bound here is explicitly credited as covered, though it receives an independent elementary gap certificate. The new contribution is the sharp **lower** inequality \(11/180\), its complete \(3:2\) minimizing orbit, and the resulting exact four-dimensional Euclidean distance \((369/44)^{1/6}\). The published real zero-sum \(\ell_4\) hyperplane result is for exponent four, while the real three-coordinate zero-sum \(\ell_p\) classification is only two-dimensional; neither implies this five-atom sixth-power minimum.

## Limitations
The classification is specific to five **real** equally weighted coordinates, exponent six, and a single zero-sum constraint. It does not establish the lower extremum for every dimension or exponent, nor weighted or complex analogues. Exact algebraic certificates and an optimal-symmetry argument are provided; no independent review of this finding has been performed. An unindexed equivalent for this special finite-dimensional inequality remains a bibliographic possibility.

## References
1. Cordian Riener, *On the degree and half degree principle for symmetric polynomials*, arXiv:1001.4464, first public 2010-01-25, Theorem 1.3. https://arxiv.org/abs/1001.4464
2. *Sharp sixth-moment constant for finite subgroup-hole spectra*, published-finding corpus published mathematical finding, 2026-10-11, especially the sharp local zero-sum sixth-moment lemma and equality classification.
3. *Exact Euclidean distortion of zero-sum real \(\ell_4\) hyperplanes*, published-finding corpus published mathematical finding, 2026-10-11, comparison of exponent and optimal-Euclidean argument.
4. *Exact Euclidean distortion of the real zero-sum \(\ell_p^3\) plane*, published-finding corpus published mathematical finding, 2026-10-11, comparison of dimension and exponent.
