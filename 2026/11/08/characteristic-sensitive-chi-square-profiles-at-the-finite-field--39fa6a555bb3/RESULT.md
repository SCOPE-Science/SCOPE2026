# Characteristic-sensitive chi-square profiles at the finite-field Wishart mixing cutoff

## Finding

Let \(q\) be a fixed prime power, \(n\ge1\), and let \(U_n\) be uniform measure on the additive group \(\operatorname{Sym}_n(\mathbb F_q)\). With independent uniform columns \(v_1,v_2,\ldots\in\mathbb F_q^n\), put
\[
S_{n,t}=\sum_{j=1}^{t}v_jv_j^{\mathsf T},\qquad P_{n,t}=\mathcal L(S_{n,t}),\qquad t\in\mathbb Z_{\ge0}.
\]
Define the Gaussian coefficient and an odd-index product by
\[
B_q(n,r)=\prod_{j=0}^{r-1}\frac{q^{n-j}-1}{q^{r-j}-1},\quad B_q(n,0)=1,\qquad
H_q(r)=\prod_{j=1}^{r}(1-q^{-(2j-1)}),\quad H_q(0)=1.
\]
The chi-square divergence \(\chi^2(P_{n,t}\Vert U_n)=\sum_X(P_{n,t}(X)-U_n(X))^2/U_n(X)\) is, for every \(t\ge0\) in odd characteristic,
\[
\boxed{\chi^2(P_{n,t}\Vert U_n)
=\sum_{r=1}^{n}B_q(n,r)\,q^{r(r+1)/2-tr}\,H_q(\lceil r/2\rceil).}
\tag{1}
\]
In characteristic two, for every \(t\ge1\), the different, exact formula is
\[
\boxed{\chi^2(P_{n,t}\Vert U_n)
=\sum_{r=1}^{\lfloor n/2\rfloor}B_q(n,2r)\,q^{r(2r+1)-2rt}\,H_q(r).}
\tag{2}
\]
At \(t=0\), in either characteristic, the law is a point mass and \(\chi^2(P_{n,0}\Vert U_n)=q^{n(n+1)/2}-1\). Formula (2) must not be used at \(t=0\): the omitted zero-eigenvalue characters contribute to the initial point mass, though their powers vanish for all positive times.

For any fixed integer \(s\), and integer times \(t=n+s\ge0\), the limits as \(n\to\infty\) are the strictly positive, absolutely convergent series
\[
\boxed{F_q^{\mathrm{odd}}(s)=\sum_{r=1}^{\infty}
\frac{q^{-sr-r(r-1)/2}H_q(\lceil r/2\rceil)}{\prod_{j=1}^{r}(1-q^{-j})}},
\tag{3}
\]
\[
\boxed{F_q^{\mathrm{even}}(s)=\sum_{r=1}^{\infty}
\frac{q^{-2rs-2r^2+r}H_q(r)}{\prod_{j=1}^{2r}(1-q^{-j})}}.
\tag{4}
\]
In other words, \(\lim_{n\to\infty}\chi^2(P_{n,n+s}\Vert U_n)=F_q^{\mathrm{odd}}(s)\) or \(F_q^{\mathrm{even}}(s)\), according to the characteristic. The two profiles have different Fourier rank sectors: arbitrary positive ranks in odd characteristic, and even polar ranks in characteristic two.

Moreover, for every sequence of integers \(a_n\to\infty\), with \(0\le a_n\le n\), there is a total-variation cutoff at time \(n\), in the precise sense
\[
\boxed{\lVert P_{n,n+a_n}-U_n\rVert_{\mathrm{TV}}\longrightarrow0,
\qquad \lVert P_{n,n-a_n}-U_n\rVert_{\mathrm{TV}}\longrightarrow1.}
\tag{5}
\]
This is a cutoff with a bounded time window. No limit for total variation at a *fixed* offset \(s\) is asserted; the explicit offset profiles are for chi-square divergence.

## Assumptions and scope

The finite field may have composite prime-power order. All vectors are independent and uniformly distributed, without conditioning on nonzero entries, and the increments are \(v_jv_j^{\mathsf T}\) with no additional scalar multipliers. Time is discrete and nonnegative. Fourier transforms use an arbitrary fixed nontrivial additive character of \(\mathbb F_q\); its choice cannot affect squared Fourier magnitudes. The rank of \(S_{n,t}\) is at most \(t\). Define total variation by \(\|P-U\|_{\mathrm{TV}}=\frac12\sum_X|P(X)-U(X)|\). All asymptotics hold for fixed field order, not for an alphabet growing with \(n\).

## Proof

**1. Fourier reduction.** For the finite abelian additive group of symmetric matrices and integer \(t\ge1\), character orthogonality and Plancherel give the exact identity
\[
\chi^2(P_{n,t}\Vert U_n)=\sum_{\xi\ne0}|\widehat\mu_n(\xi)|^{2t},
\]
where \(\mu_n\) is the one-increment distribution. It remains to classify all nontrivial Fourier coefficients of the map \(v\mapsto vv^{\mathsf T}\), including their multiplicities.

**2. Odd characteristic.** Since \(2\) is invertible, the trace pairing identifies characters with symmetric matrices \(A\). The character at \(A\) evaluates the increment as \(\psi(v^{\mathsf T}Av)\). A congruence change diagonalizes \(A\) with \(r=\operatorname{rank}A\) nonzero diagonal entries. The quadratic Gauss identity then gives
\[
\widehat\mu_n(A)=q^{-r}G_{\psi}^{r}\eta(\det A_{\mathrm{nd}}),\qquad |G_{\psi}|=\sqrt q,
\]
where \(\eta\) is the quadratic character, and \(A_{\mathrm{nd}}\) denotes any nonsingular rank-\(r\) diagonal block after congruence. Consequently \(|\widehat\mu_n(A)|^2=q^{-r}\). The number of symmetric rank-\(r\) matrices is
\[
B_q(n,r)\,q^{r(r+1)/2}H_q(\lceil r/2\rceil).
\]
Indeed, choose their \(n-r\) dimensional kernel (\(B_q(n,r)\) choices), then a nonsingular symmetric bilinear form on the quotient. Its count is \(q^{r(r+1)/2}\prod_{1\le j\le r,\,j\ \mathrm{odd}}(1-q^{-j})\), the standard orthogonal-group orbit-stabilizer formula. Substitution into Plancherel proves (1).

**3. Characteristic two.** Here the trace pairing is inadequate: \(\operatorname{tr}(Avv^{\mathsf T})\) does not range over all characters of the symmetric-matrix additive group. Instead index its characters by coefficients \(b_{ij}\) of a homogeneous quadratic polynomial \(Q_b(v)=\sum_{i\le j}b_{ij}v_iv_j\), pairing these with upper-triangular entries of the symmetric matrix. Write \(B_b\) for the alternating polar form of \(Q_b\), of rank \(2r\), and \(R_b\) for its radical. A sum along \(R_b\) vanishes when \(Q_b|_{R_b}\ne0\). Otherwise the quotient is a nonsingular \(2r\)-variable quadratic form and the classical characteristic-two quadratic Gauss identity gives
\[
|\widehat\mu_n(b)|=q^{-r}.
\]
For a fixed alternating polar form of rank \(2r\), precisely \(q^{2r}\) quadratic refinements vanish on its radical: arbitrary diagonal Frobenius-linear terms restrict surjectively to Frobenius-linear maps on the \((n-2r)\)-dimensional radical. The count of rank-\(2r\) alternating polar forms is
\[
B_q(n,2r)\,q^{r(2r-1)}H_q(r).
\]
To see the factor, choose the radical and use \(|\mathrm{GL}_{2r}(q)|/|\mathrm{Sp}_{2r}(q)|=q^{r(2r-1)}H_q(r)\). Therefore exactly \(B_q(n,2r)q^{r(2r+1)}H_q(r)\) characters of nonzero polar rank \(2r\) have Fourier magnitude \(q^{-r}\). At polar rank zero, the only nonvanishing character is trivial: a nonzero Frobenius-linear quadratic has zero character sum. Substituting into Plancherel proves (2).

**4. Fixed-offset profiles.** For each fixed \(r\), the Gaussian coefficient satisfies
\[
B_q(n,r)q^{-r(n-r)}\longrightarrow \left(\prod_{j=1}^{r}(1-q^{-j})\right)^{-1}.
\]
The same expression is bounded uniformly in \(n,r\) by \(C_q=\prod_{j=1}^{\infty}(1-q^{-j})^{-1}<\infty\). At time \(t=n+s\), formulas (1) and (2) are thus dominated, respectively, by constant multiples of \(q^{-sr-r(r-1)/2}\) and \(q^{-2rs-2r^2+r}\). Both are summable even for negative fixed \(s\). Dominated convergence proves (3) and (4), with strict positivity from the first term.

**5. Sharp total-variation cutoff.** If \(t=n+a\), \(a\ge0\), Cauchy--Schwarz and Plancherel yield \(\|P_{n,t}-U_n\|_{\mathrm{TV}}\le\frac12\sqrt{\chi^2(P_{n,t}\Vert U_n)}\). The preceding uniform bounds imply that the right side tends to zero when \(a\to\infty\), uniformly in \(n\).

For the lower bound, \(\operatorname{rank}S_{n,t}\le t\); hence at \(t=n-a\) its nullity is at least \(a\) with certainty. For a uniform symmetric matrix \(M\), a fixed \(a\)-plane lies in its kernel with probability \(q^{-an+a(a-1)/2}\). There are \(B_q(n,a)\le C_q q^{a(n-a)}\) such planes. The union bound gives
\[
\Pr_{U_n}(\operatorname{nullity}M\ge a)\le C_q q^{-a(a+1)/2}.
\]
Using the nullity event as a total-variation test proves the second limit in (5). This argument holds in both characteristics. \(\square\)

## Verification

The companion standard-library scripts `check_odd.py` and `check_even.py` independently enumerate Fourier characters and their normalized quadratic Gauss sums, compare exact rank/multiplicity formulas, and check Plancherel against explicit convolution probabilities in small cases. The odd-characteristic checker covers \((n,q)=(1,3),(2,3),(2,5),(3,3)\), with direct convolution through four steps for \((2,3)\). The characteristic-two checker covers \((1,2),(2,2),(3,2),(4,2),(2,4)\) and direct convolution at \((2,2),(3,2),(2,4)\). Tests additionally evaluate finite-size convergence toward both offset-series profiles. Execute `python3 check_odd.py` and `python3 check_even.py` from their containing directory. The general theorems follow from the proof, not the finite checks.

## Relationship to prior work

The rank counts for uniform symmetric matrices are classical and appear in Fulman and Goldstein's 2012 preprint. Schmidt's 2014 and 2018 association-scheme studies give much more general eigenmatrix methods for symmetric and quadratic forms; they cover ingredients needed for one-step spectral analysis. Pak and Vu's geometric walks choose a field scalar independently of a generator, unlike the present increments. Even when the rank-one set is closed under scalars in characteristic two, their uniform-scalar version has one-step holding probability \(q^{-1}\), whereas this walk has holding probability \(q^{-n}\); the measures therefore differ for \(n>1\). The present statements focus on the specific unscaled Gram walk, its exact full chi-square divergence in both characteristics, and the distinct fixed-offset limits together with a two-sided sharp mixing window. Priority beyond this bounded comparison is not claimed.

## Limitations

The explicit infinite series are chi-square profiles, not proved total-variation profiles. Field size is fixed in the limits. Characteristic-two signed eigenvalues depend on quadratic isometry type, but only their magnitudes and multiplicities enter the chi-square formulas. Literature overlap remains possible via implicit specialization of known association-scheme eigenmatrices or general cutoff theory. No independent audit or outside mathematical validation has been performed.

## References

- J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, first posted 2012-11-02, arXiv:1211.0504. https://arxiv.org/abs/1211.0504
- K.-U. Schmidt, *Symmetric bilinear forms over finite fields with applications to coding theory*, first posted 2014-10-27, arXiv:1410.7184. https://arxiv.org/abs/1410.7184
- K.-U. Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, first posted 2018-03-12, arXiv:1803.04274. https://arxiv.org/abs/1803.04274
- I. Pak and V. H. Vu, *On mixing of certain random walks, cutoff phenomenon and sharp threshold of random matroid processes*, Discrete Applied Mathematics 110 (2001), 251–272, DOI:10.1016/S0166-218X(00)00201-8.
