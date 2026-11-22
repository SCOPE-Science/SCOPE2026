# No nontrivial multivariate extension of the variable-power FGM product ansatz

## Finding

For every integer \(n\geq 3\) and every real \(a\), consider the exact multivariate variable-power expression

\[
G_{n,a}(u_1,\ldots,u_n)=\left(\prod_{i=1}^{n}u_i\right)^{1+a\prod_{i=1}^{n}(1-u_i)}
\]

on the strictly positive cube \((0,1]^n\). It extends to an \(n\)-copula on \([0,1]^n\) **if and only if \(a=0\)**. More precisely, when \(a\neq0\), its continuous \(n\)-fold mixed derivative is strictly negative on a nonempty open subset of \((0,1)^n\); hence no modification of its values on the boundary can rescue \(n\)-increasingness. When \(a=0\), the expression is the independence copula.

This exactly resolves the parameter-range question for the specific higher-dimensional formula proposed in the concluding section of Chesneau (2024). It does *not* rule out differently constructed multivariate variable-power copulas.

## Assumptions and scope

The dimension \(n\) is any fixed integer at least three; \(a\in\mathbb R\) is constant and independent of the coordinates. The exponent and bases have exactly the product forms displayed above; no power rescaling, additive correction, or alternative exponent is included. Inside the positive cube all expressions and mixed derivatives are smooth for every real \(a\). A copula is an \(n\)-increasing distribution function with uniform one-dimensional margins. Its \(n\)-fold mixed partial derivative, where continuous, must be nonnegative: otherwise the signed volume of a sufficiently small axis-parallel box is negative.

Each proper marginal of the displayed candidate, evaluated by setting at least one coordinate to one, equals the corresponding independence product because the exponent's product correction vanishes. Thus boundary margins alone are not enough to test the proposed purely higher-order dependence.

## Proof

Write \(P=\prod_i u_i\), \(Q=\prod_i(1-u_i)\), and \(L=\log P\). Then \(G_{n,a}=P\exp(aQL)\). Fix a nonempty subset \(S\subset\{1,\dots,n\}\) of \(m\) variables with \(1\le m\le n-1\). Differentiating once in each variable of \(S\) and *then* setting those coordinates to one gives the face identity

\[
\left.\partial_S G_{n,a}\right|_{u_i=1\;(i\in S)}
=P_{S^c}\bigl[1+a(-1)^mQ_{S^c}\log P_{S^c}\bigr],
\quad P_{S^c}=\prod_{j\notin S}u_j,\quad
Q_{S^c}=\prod_{j\notin S}(1-u_j).
\tag{1}
\]

Indeed, expand \(\exp(aQL)=1+aQL+O(Q^2)\) near the face. Every differentiated coordinate divides \(Q\) as a separate factor \((1-u_i)\). After one derivative in each such coordinate, every term of order at least \(Q^2\) still vanishes on the face. The linear term contributes only when all \(m\) derivatives hit their respective factors in \(Q\), yielding \((-1)^m aP_{S^c}Q_{S^c}\log P_{S^c}\). The zeroth-order term contributes \(P_{S^c}\). This argument is legitimate locally at any face point whose undifferentiated coordinates are strictly positive; the exponential has a convergent Taylor series there.

Let \(b_1=a(-1)^{n-1}\) and \(b_2=a(-1)^{n-2}=-b_1\). For \(a\ne0\), precisely one of these coefficients is positive.

**Case 1: \(b_1>0\).** Choose \(S=\{2,\ldots,n\}\) in (1), with remaining coordinate \(z\in(0,1)\). Differentiating the face identity in \(z\) gives the continuous boundary limit of the complete mixed derivative,

\[
\lim_{u_2,\ldots,u_n\uparrow1}\partial_1\cdots\partial_nG_{n,a}(z,u_2,\ldots,u_n)
=1+b_1\big[(1-2z)\log z+1-z\big].
\tag{2}
\]

The bracket tends to \(-\infty\) as \(z\downarrow0\), so (2) is negative for a positive \(z\). By continuity the mixed derivative is negative at interior points near that face point.

**Case 2: \(b_2>0\).** Choose \(S=\{3,\ldots,n\}\) in (1), retaining \(x=u_1\), \(y=u_2\). Put \(f(t)=t(1-t)\). The boundary limit of the complete mixed derivative equals

\[
1+b_2D(x,y),\qquad
D(x,y)=f'(x)f'(y)\log(xy)
+(1-2x)(1-y)+(1-x)(1-2y).
\tag{3}
\]

This follows by differentiating \(xy[1+b_2(1-x)(1-y)\log(xy)]\) once in each remaining variable. At the fixed \(y=1/4\),

\[
D(x,1/4)=\frac{1-2x}{2}\log(x/4)
+\frac34(1-2x)+\frac12(1-x)
\longrightarrow-\infty\quad(x\downarrow0).
\tag{4}
\]

Consequently (3) is negative for sufficiently small positive \(x\), and continuity again gives interior points with negative mixed density.

In either sign of \(a\), \(G_{n,a}\) violates the necessary \(n\)-increasing condition. When \(a=0\), \(G_{n,0}=P\) has constant density one and uniform margins, so is a copula. This proves the claimed equivalence. \(\square\)

## Verification

The attached standalone `CHECK.py` verifies identity (1) by exact symbolic differentiation for dimensions 3 through 6 and every subset of each dimension, independently differentiates (2)--(4), and constructs explicit strictly negative *face-density* sign witnesses using only the rigorous inequality \(\log 2>1/2\). Those finite computations support the algebra but are not substituted for the unrestricted-dimensional proof above. Run `python CHECK.py` with SymPy installed. The proof's asymptotics establish both sign cases for every nonzero real parameter, not only the checker examples.

## Relationship to prior work

Chesneau, *Investigation of a variable-power FGM-type copula* (2024), Proposition 1, proves the bivariate formula \((xy)^{1+a(1-x)(1-y)}\) is a copula for \(0\le a\le1\). On printed page 33, the author explicitly proposes the displayed \(n\)-variable product-power expression and leaves its admissible parameter range for future study. The present theorem answers that specific question for \(n\ge3\) with the singleton parameter set \(\{0\}\); it does not make any new claim about the complete bivariate parameter range.

The classical \(n\)-way FGM perturbation \(P(1+\theta Q)\), by contrast, has density \(1+\theta\prod_i(1-2u_i)\) and is a nontrivial copula when \(|\theta|\le1\). Therefore the obstruction comes from the **variable exponent**, not from the idea of retaining independence on every proper marginal face. The 2024 bivariate variable-power constructions of Chesneau and the 2025 bivariate concordance compendium of Nadarajah--Nawa do not state this higher-dimensional no-go result in the material inspected. The ratio-type constructions of El Ktaibi--Bentoumi--Mesfioui use a distinct rational structure.

## Limitations

The theorem treats this one exact ansatz and real scalar parameters, not all power-based, asymmetric, or dimension-dependent copula designs. It does not certify historical uniqueness: unpublished or unindexed calculations might already contain a related face-derivative obstruction. The mathematical proof has not been independently certified; the result should not be read as a classification of other multivariate constructions.

## References

1. C. Chesneau (2024), *Investigation of a variable-power FGM-type copula*, Stochastic Models in Probability and Statistics **1**(1), 17--36, DOI: https://doi.org/10.22067/smps.2024.45178 . Publisher full text: https://smps.um.ac.ir/article_45178_cc0e5acb5224d3537fb81f97ee594c95.pdf (particularly pages 20 and 33).
2. C. Chesneau (2024), *Solutions to two open problems on bivariate variable-power copulas*, Bull. Comput. Appl. Math. **12**(1), 93--118. Abstract: https://sites.google.com/usb.ve/bullcompama/table-of-contents/abstract-92 .
3. S. Nadarajah and V. Nawa (2025), *A compendium of expressions for dependence measures of bivariate copulas*, AIMS Mathematics **10**(9), 22336--22381, https://doi.org/10.3934/math.2025995 .
4. F. El Ktaibi, R. Bentoumi and M. Mesfioui (2024), *On the ratio-type family of copulas*, Mathematics **12**, 1743, https://doi.org/10.3390/math12111743 .
