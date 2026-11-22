# An explicit planar Fourier eigenfunction with nonpositive area below \(183/100\)

## Finding

For the unitary Fourier transform on \(\mathbb R^2\),
\[
\widehat f(\xi)=\int_{\mathbb R^2} f(x)e^{-2\pi i x\cdot\xi}\,dx,
\]
consider the definite-set quantity
\[
\mathcal M_+(2)=\inf\bigl\{|\{x\in\mathbb R^2:f(x)\le0\}|:\ 0\ne f\in L^1(\mathbb R^2;\mathbb R),\ \widehat f=f,\ f(0)=0\bigr\}.
\]
(The Fourier transform of an admissible function is automatically integrable.) The following explicit real radial Schwartz witness establishes the strictly improved upper bound
\[
\boxed{\mathcal M_+(2)<\frac{183}{100}=1.83<2.}
\]
Let \(L_j=L_j^{(0)}\) denote the ordinary Laguerre polynomial, set \(z=2\pi|x|^2\), and define
\[
\boxed{f(x)=e^{-\pi|x|^2}\left[22(L_2(z)-1)+20(L_4(z)-1)-4(L_6(z)-1)+(L_8(z)-1)\right].}
\]
Its nonpositive set is exactly a closed Euclidean disk of area \(\rho/2\), where \(\rho\) is the unique positive zero of the explicit integer polynomial
\[
\begin{aligned}
Q(z)={}&z^7-64z^6+1344z^5-10752z^4+50400z^3\\
&-376320z^2+2217600z-4354560.
\end{aligned}
\]
In fact, \(73/20<\rho<183/50\), giving the exact rational enclosure
\[
\boxed{\frac{73}{40}<|\{f\le0\}|=\frac\rho2<\frac{183}{100}.}
\]
The improvement is a strict upper bound for the **unrestricted** two-dimensional definite-set problem, not a claim of its optimal value.

## Assumptions and scope

Lebesgue area is used in \(\mathbb R^2\); the Fourier convention and Laguerre normalization are as stated. The witness is a real-valued radial Schwartz function, with no additional normalization apart from vanishing at the origin. The nonpositive set includes zeros; its boundary and the isolated origin have area zero. Degree eight in \(z\) means degree sixteen in the spatial coordinates. No assertion is made that the witness minimizes the nonpositive area among polynomials of any prescribed degree or among arbitrary Fourier eigenfunctions.

## Proof

**1. Fourier eigenfunction and vanishing.** The standard Laguerre generating function is, for \(|t|<1\),
\[
\sum_{j=0}^{\infty}t^j L_j(z)=(1-t)^{-1}\exp\!\left(-\frac{zt}{1-t}\right).
\]
Consequently
\[
\sum_{j=0}^{\infty}t^j e^{-\pi|x|^2}L_j(2\pi|x|^2)
=\frac1{1-t}\exp\!\left(-\pi|x|^2\frac{1+t}{1-t}\right).
\]
The two-dimensional Fourier transform of the right side is
\[
\frac1{1+t}\exp\!\left(-\pi|\xi|^2\frac{1-t}{1+t}\right),
\]
which is the same generating function with \(t\) replaced by \(-t\). Coefficient comparison proves
\[
\widehat{\bigl(e^{-\pi|\cdot|^2}L_j(2\pi|\cdot|^2)\bigr)}
=(-1)^j e^{-\pi|\cdot|^2}L_j(2\pi|\cdot|^2).
\]
All the chosen indices \(0,2,4,6,8\) are even, so \(\widehat f=f\). Since \(L_j(0)=1\), we also have \(f(0)=0\). Its highest coefficient is positive, hence \(f\ne0\), and it is real, integrable and Schwartz.

**2. The exact sign polynomial.** The elementary expansion
\[
L_j(z)=\sum_{k=0}^j\frac{(-1)^k}{k!}\binom jk z^k
\]
gives, without approximation,
\[
22(L_2(z)-1)+20(L_4(z)-1)-4(L_6(z)-1)+(L_8(z)-1)
=\frac{zQ(z)}{40320}.
\]
Thus the sign of \(f(x)\) at \(z>0\) equals that of \(Q(z)\).

**3. Exact Sturm root count.** Form the usual Sturm sequence \(S_0=Q\), \(S_1=Q'\), \(S_{j+1}=-\operatorname{rem}(S_{j-1},S_j)\), terminating at a nonzero constant. Multiplication of an individual member by a positive rational number does not affect sign variations. Using positive rescalings to primitive rational-coefficient polynomials, the eight sign strings, in order of increasing Sturm index, are:

| Evaluation | Signs | Variations |
|---|---|---:|
| \(z=0\) | `-++-+---` | 4 |
| \(z=73/20\) | `-+--+---` | 4 |
| \(z=183/50\) | `++--+---` | 3 |
| \(z\to+\infty\) | `+++--++-` | 3 |

These are **exact rational calculations**, reproduced from polynomial Euclidean division in the included pure-Python checker. No polynomial in this sequence vanishes at any evaluation point. Sturm's theorem shows that \(Q\) has exactly one positive real zero \(\rho\), lying strictly between \(73/20\) and \(183/50\). As independent endpoint checks, \(Q(0)=-4354560<0\) and
\[
Q(183/50)=\frac{85807489517127}{781250000000}>0.
\]
Since the leading coefficient of \(Q\) is positive and it has exactly one positive zero, \(Q(z)<0\) on \(0<z<\rho\) and \(Q(z)>0\) for \(z>\rho\). The nonpositive set is therefore
\[
\{x:2\pi|x|^2\le\rho\},
\]
whose area is \(\pi\rho/(2\pi)=\rho/2\). The rational enclosure and strict inequality follow. \(\square\)

## Verification

`CHECK.py` is a standalone exact checker using only the Python standard library. It independently expands every Laguerre polynomial with rational coefficients, checks the exact identity \(P(z)=zQ(z)/40320\), constructs the full rational Sturm sequence by Euclidean division, normalizes by positive factors only, and verifies all four variation counts and the exact positive endpoint evaluation. Run `python CHECK.py` from the extracted package directory. Expected final line: `CHECK_OK Laguerre_identity=exact Sturm_signs=4,4,3,3 positive_root_count=1 area_upper=183/100`. The all-function eigenvalue property and the use of Sturm's theorem are established analytically above, not inferred from finite sampling.

## Relationship to prior work

Roni Edwin, *Fourier inequalities and sign uncertainty II* (arXiv:2611.08224v1, 2026-11-05), formulates the definite-set minimization as Problem 1.6 and proves a general lower bound; it does not specify this planar degree-sixteen witness or the stated upper bound. The previously published *A sharp planar negative-set inequality in the fourth Hermite Fourier band* (published-finding corpus, 2026-11-16) proves that every real planar \(+1\)-eigenfunction of Gaussian polynomial total degree at most four, vanishing at zero, has nonpositive area at least \(2\). The present higher-degree witness shows why that finite-band lower bound cannot be extrapolated to the unrestricted problem. The earlier *Sharp negative-set length in the first three positive-Fourier Hermite modes* concerns **one-dimensional length**, not two-dimensional area.

Giraud and Peschanski (2005) develop the classical Gaussian–Laguerre Fourier eigenbasis and Sturm root-testing machinery for positivity of a function and its transform. These methods are prior art, not a newly invented technique. Their inspected two-dimensional discussion does not report the exact degree-sixteen polynomial and negative-area bound here. An equivalent older sign-radius witness or differently parametrized polynomial could have escaped the literature searches; absence of a database hit is not a proof of absolute novelty.

## Limitations

This is a single explicit nonoptimal upper-bound witness, not a universal lower bound and not an exact evaluation of \(\mathcal M_+(2)\). Its disk geometry is specific to this radial polynomial; no claim is made about general nonradial minimizers. The root enclosure is exact; its decimal estimate is optional and not used in proof. No independent mathematical audit has been conducted. Literature precedence is assessed relative to the named accessible primary material and search results and may be incomplete.

## References

1. Roni Edwin, *Fourier inequalities and sign uncertainty II*, arXiv:2611.08224v1, first submitted 2026-11-05, https://arxiv.org/html/2611.08224v1.
2. *A sharp planar negative-set inequality in the fourth Hermite Fourier band*, published-finding corpus, 2026-11-16, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-sharp-planar-negative-set-inequality-in-the-fourth-hermite-fou--7fbca0facafa.
3. *Sharp negative-set length in the first three positive-Fourier Hermite modes*, published-finding corpus, 2026-11-16, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-negative-set-length-in-the-first-three-positive-fourier-he--0c4edba5f7b1.
4. B. G. Giraud and R. Peschanski, *On positive functions with positive Fourier transforms*, arXiv:math-ph/0504015, first submitted 2005-04-05, https://arxiv.org/abs/math-ph/0504015.
