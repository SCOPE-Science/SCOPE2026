# Effective-rank fourth-moment gap in the complex cubic Hermite sector
## Finding
For every integer \(n\ge 1\) and every \(L^2\)-normalized \(q\in\mathcal H_{2,1}(\mathbb C^n)\), let
\[
X=\sqrt2\,\operatorname{Re}q=I_3(f)
\]
be the corresponding normalized real third-chaos variable on \(\mathbb R^{2n}\). Let \(F\) be the first flattening of the symmetric cubic kernel \(f\), let \(G=F^*F\), and define its effective rank by
\[
r_{\mathrm{eff}}(q)=\frac{(\operatorname{tr}G)^2}{\operatorname{tr}(G^2)}.
\]
Then
\[
\mathbb E|q|^4\ge 2+\frac{24}{r_{\mathrm{eff}}(q)}\ge 2+\frac{12}{n}.
\]
Consequently, a sequence in the complex cubic Hermite sector whose normalized fourth moments approach the complex-Gaussian value \(2\) must have flattening effective rank tending to infinity; in finite coordinate models its ambient complex dimension must therefore tend to infinity.

## Assumptions and scope
The complex Gaussian convention is the standard one in which each complex coordinate has density \(\pi^{-1}e^{-|z|^2}\). The space \(\mathcal H_{2,1}(\mathbb C^n)\) is the complex Hermite component of bidegree \((2,1)\). The normalization is \(\|q\|_2=1\). After realification, \(X=\sqrt2\,\operatorname{Re}q\) belongs to the third real Wiener chaos over \(\mathbb R^{2n}\). The claimed bounds do not assert optimality of either constant, nor do they characterize equality.

## Proof
Write \(X=I_3(f)\), with \(f\) a real symmetric cubic kernel on \(\mathbb R^{2n}\). For the first flattening \(F\), set \(G=F^*F\), and put
\[
s=\|G\|_{\mathrm{HS}}^2=\operatorname{tr}(G^2).
\]
The cubic moment calculation in Heilman--Jones--Malavolta gives, with \(h=\|\operatorname{sym}_4(FF^*)\|_{\mathrm{HS}}^2\ge0\),
\[
\kappa_4(X)=1296\left(s+\frac32h\right).
\]
For \(m=\mathbb E|q|^4\), circular symmetry gives
\[
\kappa_4(X)=\frac32(m-2).
\]
Hence
\[
m-2=864\left(s+\frac32h\right)\ge864s.
\]

Because \(X\) is normalized, the same third-chaos normalization gives
\[
1=\mathbb E X^2=3!\,\|f\|^2.
\]
Moreover,
\[
\operatorname{tr}G=\|F\|_{\mathrm{HS}}^2=\|f\|^2=\frac16.
\]
Thus \(G\ne0\), the effective rank is well defined, and
\[
s=\operatorname{tr}(G^2)
=\frac{(\operatorname{tr}G)^2}{r_{\mathrm{eff}}(q)}
=\frac1{36r_{\mathrm{eff}}(q)}.
\]
Substitution yields
\[
m-2\ge\frac{24}{r_{\mathrm{eff}}(q)}.
\]

Finally, \(G\) is positive semidefinite on \(\mathbb R^{2n}\). If its nonzero eigenvalues are \(\lambda_1,\ldots,\lambda_r\), Cauchy--Schwarz gives
\[
r_{\mathrm{eff}}(q)
=\frac{(\sum_j\lambda_j)^2}{\sum_j\lambda_j^2}
\le r=\operatorname{rank}G\le2n.
\]
Therefore \(24/r_{\mathrm{eff}}(q)\ge12/n\), completing the proof.

## Verification
The proof is symbolic. The nonstandard identity used is the exact fourth-cumulant contraction formula in the focal source, together with its normalization of \(X=\sqrt2\,\operatorname{Re}q\). The remaining steps are the Hilbert--Schmidt trace identities for the flattening and Cauchy--Schwarz for the eigenvalues of the positive semidefinite matrix \(G\). No numerical experiment, finite enumeration, or asymptotic approximation is used.

The dimension factor is \(2n\), not \(n\), because the real third-chaos representation of a function of \(n\) standard complex Gaussian coordinates lives on \(2n\) real Gaussian coordinates.

## Relationship to prior work
Heilman, Jones, and Malavolta derive the exact identity
\[
\kappa_4(X)=1296\left(s+\frac32h\right)
\]
and use only its nonnegativity to obtain \(\mathbb E|q|^4\ge2\); they also obtain a dimension-free upper bound. Their statement and proof do not record the effective-rank lower gap above.

Chen and Liu prove the complex fourth-moment theorem for fixed complex Wiener--Itô chaoses: convergence of the fourth moment to the Gaussian value characterizes Gaussian convergence under the relevant normalization. That asymptotic theorem does not give an explicit finite-coordinate lower gap or a flattening-effective-rank obstruction. The present estimate quantifies a structural requirement behind such convergence in the \((2,1)\) sector.

## Limitations
No matching lower construction is supplied, so neither \(24/r_{\mathrm{eff}}(q)\) nor \(12/n\) is claimed sharp. The result concerns the specific complex Hermite sector \(\mathcal H_{2,1}\) and the real first-flattening effective rank of \(\sqrt2\,\operatorname{Re}q\). It does not improve the dimension-free numerical bounds for the complex Grothendieck constant. General Wiener-chaos contraction theory is extensive, so an equivalent effective-rank formulation under different tensor-contraction terminology remains a residual originality risk.

## References
1. S. Heilman, C. Jones, and G. Malavolta, *Sharper Bounds for the Complex Grothendieck Constant*, arXiv:2609.25462v1, first public 21 September 2026.
2. Y. Chen and Y. Liu, *On the fourth moment theorem for the complex multiple Wiener-Itô integrals*, arXiv:1408.1817v1, 2014.
