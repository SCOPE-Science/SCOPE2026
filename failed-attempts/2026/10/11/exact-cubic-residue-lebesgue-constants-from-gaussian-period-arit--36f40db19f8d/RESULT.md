# Exact cubic-residue Lebesgue constants from Gaussian period arithmetic
## Finding
Let \(p\equiv1\pmod 3\) be prime, and let
\[
H=(\mathbb F_p^\times)^3\subset \mathbb Z_p^\times
\]
be the nonzero cubic residues. Let \(P_H\) be the Fourier projection on \(\mathbb Z_p\) whose multiplier is the indicator \(1_H\). There are unique integers \(L\) and \(M\ge0\) satisfying
\[
4p=L^2+27M^2,\qquad L\equiv1\pmod3.
\]
Define
\[
\theta_p=\frac13\arccos\!\left(\frac{L}{2\sqrt p}\right).
\]
Then
\[
\Lambda_3(p):=\|P_H\|_{\ell^1\to\ell^1}
=\|P_H\|_{\ell^\infty\to\ell^\infty}
=\|1_H\|_{A(\mathbb Z_p)}
\]
has the exact formula
\[
\Lambda_3(p)=
\begin{cases}
\displaystyle \frac{4(p-1)}{9p}\left(1+\sqrt p\cos\theta_p\right),&L\ge-2,\\[2mm]
\displaystyle \frac{2(p-1)}{9p}\left(1-2\sqrt p\cos(\theta_p+2\pi/3)\right),&L\le-5.
\end{cases}
\]
The two alternatives are exhaustive because \(L\equiv1\pmod3\).

Equivalently, if \(\eta_0,\eta_1,\eta_2\) are the three cubic Gaussian periods, then
\[
\Lambda_3(p)=\frac{p-1}{3p}
\left(1+|\eta_0|+|\eta_1|+|\eta_2|\right).
\]
For \(L\ge-2\), exactly one period is positive; for \(L\le-5\), exactly one period is negative. This gives an arithmetic phase split for a canonical cyclotomic Fourier projection.

## Assumptions and scope
The group \(\mathbb Z_p\) is equipped with normalized counting measure. The Fourier transform is
\[
\widehat f(r)=\frac1p\sum_{x\in\mathbb Z_p}f(x)e^{2\pi i rx/p}.
\]
The set \(H\) contains only the nonzero cubic residues. Since \(p\equiv1\pmod3\), necessarily \(p\equiv1\pmod6\), so \(-1\in H\) and the cubic Gaussian periods are real.

The claim concerns only the endpoint operator norms \(\ell^1\to\ell^1\) and \(\ell^\infty\to\ell^\infty\), and the equal Fourier-algebra norm. It does not assert an interior \(\ell^q\) operator norm formula, a distribution theorem for the arithmetic parameter \(L\), or an extremal comparison with arbitrary subsets of the same cardinality.

## Proof
Write \(k=(p-1)/3\). Fourier inversion shows that \(P_H\) is normalized convolution with
\[
K(x)=\sum_{h\in H}e^{2\pi i hx/p}.
\]
Hence both endpoint operator norms equal the normalized total variation of the kernel:
\[
\|P_H\|_{\ell^1\to\ell^1}
=\|P_H\|_{\ell^\infty\to\ell^\infty}
=\frac1p\sum_{x\in\mathbb Z_p}|K(x)|.
\]
The same quantity is \(\|1_H\|_{A(\mathbb Z_p)}\) under the stated Fourier normalization.

For \(x=0\), one has \(K(0)=k\). For \(x\ne0\), multiplication by \(x\) moves \(H\) to one of the three multiplicative cosets of \(H\). Thus \(K(x)\) is one of the three cubic Gaussian periods \(\eta_0,\eta_1,\eta_2\), and each period occurs exactly \(k\) times. Therefore
\[
\Lambda_3(p)=\frac{k}{p}
\left(1+|\eta_0|+|\eta_1|+|\eta_2|\right).
\]

The classical cubic period equation, with the uniquely normalized integer \(L\), is
\[
F_{p,L}(X)=X^3+X^2-\frac{p-1}{3}X-\frac{p(L+3)-1}{27}.
\]
Putting \(X=Z-1/3\) depresses it to
\[
Z^3-\frac p3Z-\frac{pL}{27}=0.
\]
Thus its roots are
\[
\eta_j=-\frac13+\frac{2\sqrt p}{3}
\cos\!\left(\theta_p+\frac{2\pi j}{3}\right),
\qquad j=0,1,2,
\]
up to a permutation. Because \(0\le\theta_p\le\pi/3\), the largest root is
\[
\eta_{\max}=-\frac13+\frac{2\sqrt p}{3}\cos\theta_p,
\]
and the smallest root is
\[
\eta_{\min}=-\frac13+\frac{2\sqrt p}{3}
\cos(\theta_p+2\pi/3).
\]

The elementary symmetric functions of the three periods are
\[
\eta_0+\eta_1+\eta_2=-1,
\qquad
\eta_0\eta_1+\eta_0\eta_2+\eta_1\eta_2=-\frac{p-1}{3},
\]
and
\[
\eta_0\eta_1\eta_2=\frac{p(L+3)-1}{27}.
\]
If \(L\ge-2\), the product is positive. The negative second symmetric sum and the negative total sum force exactly one positive root and two negative roots. Hence
\[
|\eta_0|+|\eta_1|+|\eta_2|=1+2\eta_{\max}.
\]
Substitution gives the first branch.

If \(L\le-5\), the product is negative. The negative second symmetric sum rules out three negative roots, so exactly one root is negative. Consequently
\[
|\eta_0|+|\eta_1|+|\eta_2|=-1-2\eta_{\min},
\]
which gives the second branch. Since \(L\equiv1\pmod3\), no integer value lies between the two branches.

## Verification
The standalone script `verify.py` enumerates every prime \(p\equiv1\pmod3\) below \(1001\). For each prime it constructs the cubic-residue cosets directly, computes the three periods from roots of unity, reconstructs the unique pair \((L,M)\), checks all three elementary symmetric identities and the unordered trigonometric root formula, checks the sign branch, and compares the direct normalized kernel \(\ell^1\) norm with the displayed theorem.

A replay of the packaged script returned:

`VERIFY_OK primes=80 one_positive=43 one_negative=37 max_norm_err=4.690e-13 max_poly_res=4.087e-11 max_imag=3.120e-11`

These finite numerical checks corroborate the formulas but are not used as a proof for arbitrary primes.

## Relationship to prior work
Green and Konyagin define the normalized Fourier transform on \(\mathbb Z_p\), identify the corresponding Fourier-algebra norm as the \(\ell^1\)-norm of the transform, and study lower bounds for that norm in a half-density Littlewood problem. Their primary MSC is 42A99. Their inspected paper does not discuss cubic residues or Gaussian periods, and its extremal question concerns a minimum over half-density sets rather than the exact norm of a fixed index-three multiplicative subgroup.

Barcanescu develops Gaussian period polynomials. In the inspected cubic-period section, the nonzero field elements are partitioned into the cubic-residue coset and its two companion cosets; the paper gives the cubic period polynomial
\[
X^3+X^2-\frac{p-1}{3}X-\frac{p(L+3)-1}{27}
\]
with \(4p=L^2+27M^2\) and \(L\equiv1\pmod3\). That source supplies the period algebra, but it does not formulate the endpoint Fourier projection norm, the absolute-period sign split, or the resulting two-branch Lebesgue constant.

Published-index searches for the exact norm, its cubic-period aliases, and the formula fingerprints found no statement covering this quantitative projection theorem. The closest indexed cubic-residue item located concerned discrepancy rather than Fourier-algebra norms.

## Limitations
The originality conclusion is limited to the inspected sources and searches. Classical cyclotomy has a large literature, so an equivalent norm identity could exist under terminology such as a cyclotomic Lebesgue constant or an absolute Gaussian-period sum. The theorem itself does not require a novelty assumption: its proof is self-contained once the classical cubic period equation is supplied.

The formula depends on the normalized parameter \(L\), so it does not reduce to a function of \(p\) alone without solving the representation \(4p=L^2+27M^2\). No claim is made here about the distribution of the two branches as \(p\) varies.

## References
1. B. Green and S. Konyagin, *On the Littlewood Problem Modulo a Prime*, arXiv:math/0601565; Canadian Journal of Mathematics 61 (2009), 141–164, DOI 10.4153/CJM-2009-007-4.
2. S. Barcanescu, *The coefficients of the period polynomials*, arXiv:1402.3833, especially the section on cubic residues and Gaussian 3-periods.
