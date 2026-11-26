# Exact determinant fibers and character spectrum of finite-field Hankel matrices

## Finding

For every prime power \(q\), every integer \(n\ge1\), and every \(t\in\mathbb F_q\), let
\[
N_{n,q}(t)=\#\{(a_0,\ldots,a_{2n-2})\in\mathbb F_q^{2n-1}:\det(a_{i+j})_{0\le i,j<n}=t\}.
\]
Put \(\varepsilon_n=(-1)^{n(n-1)/2}\in\mathbb F_q^\times\). Then \(N_{n,q}(0)=q^{2n-2}\). If \(t\ne0\), the complete answer is
\[
\boxed{N_{n,q}(t)=q^{2n-2}+\sum_{\substack{r\mid\gcd(n,q-1)\\r>1}}q^{n+n/r-2}\sum_{\substack{\chi:\mathbb F_q^\times\to\mathbb C^\times\\\operatorname{ord}(\chi)=r}}\chi(\varepsilon_nt^{-1}).}
\]
Equivalently, choose a generator \(g\) of \(\mathbb F_q^\times\) and the unique \(j\in\{0,\ldots,q-2\}\) with \(g^j=\varepsilon_nt^{-1}\). The inner sum is the integer Ramanujan sum
\[
c_r(j)=\sum_{d\mid\gcd(r,j)}d\,\mu(r/d).
\]
The determinant is uniformly distributed over nonzero field elements **if and only if** \(\gcd(n,q-1)=1\). In the nonuniform case every fiber is still explicitly determined by this integer formula.

A stronger Fourier formulation is available. For a multiplicative character \(\chi\) of exact order \(r\mid(q-1)\),
\[
\boxed{\sum_{\substack{a\in\mathbb F_q^{2n-1}\\\det H_n(a)\ne0}}\chi(\det H_n(a))=
\begin{cases}(q-1)\chi(\varepsilon_n)q^{n+n/r-2},&r\mid n,\\0,&r\nmid n.\end{cases}}
\]
The trivial character has order \(1\), so its value is precisely the known nonsingular count \(q^{2n-2}(q-1)\).

## Assumptions and scope

\(\mathbb F_q\) is the field with \(q=p^e\) elements, including even characteristic and nonprime field sizes. Matrices are **all** square Hankel matrices of order \(n\) with independently chosen anti-diagonal entries; no symmetry-class quotient or restriction on the first entries is imposed. The character order \(r\) is an ordinary positive divisor of \(q-1\), and every character is evaluated only at nonzero elements. If \(q=2\), the sums indexed by \(r>1\) are empty. The polynomial \(\mu\) in the Ramanujan formula denotes the number-theoretic Möbius function, not a character. The claim is exact for every \(q\), \(n\), and \(t\) in this domain.

## Proof

**1. Relate a Hankel determinant to a resultant, with an exact multiplicity.** Write \(u(X)=X^n+u_{n-1}X^{n-1}+\cdots+u_0\) and let \(v\) have degree smaller than \(n\). Expand at infinity:
\[
\frac{v(X)}{u(X)}=\sum_{k\ge1}a_kX^{-k},\qquad H_n(u,v)=(a_{i+j+1})_{0\le i,j<n}.
\]
If \(\gcd(u,v)=1\), this Hankel matrix is invertible. Conversely, every invertible Hankel matrix, specified by \(a_1,\ldots,a_{2n-1}\), has exactly \(q\) preimages \((u,v)\) of this form: arbitrarily choose \(a_{2n}\), solve the nonsingular Hankel system
\[
(a_{i+j+1})_{0\le i,j<n}(u_0,\ldots,u_{n-1})^{\mathsf T}=-(a_{n+1},\ldots,a_{2n})^{\mathsf T},
\]
and recover the coefficients of \(v\) from the first \(n\) coefficients of the Laurent expansion. This is the explicit Hermite-pair construction of García-Armas, Ghorpade, and Ram, Theorem 3.5 [1]. The choice of \(a_{2n}\) is recoverable from \((u,v)\), so the multiplicity is exactly \(q\).

To check the determinant relation rather than merely invertibility, use their Barnett factorization [1, Proposition 3.4]:
\[
B_n(u,v)=B_n(u,1)H_n(u,v)B_n(u,1),
\]
where \(B_n\) is the Bezoutian of \((u(X)v(Y)-v(X)u(Y))/(X-Y)\). The matrix \(B_n(u,1)\) is anti-triangular with anti-diagonal entries \(1\), hence its determinant has square \(1\) in every field. On the dense locus where \(u\) has distinct roots \(\alpha_1,\ldots,\alpha_n\), Vandermonde evaluation of the Bezoutian gives
\[
V^{\mathsf T}B_n(u,v)V=\operatorname{diag}(u'(\alpha_i)v(\alpha_i)),\qquad
\det B_n(u,v)=(-1)^{n(n-1)/2}\prod_i v(\alpha_i).
\]
The last product is the monic resultant \(\operatorname{Res}(u,v)\). Polynomial identity then extends to inseparable \(u\), with no restriction on characteristic. Therefore
\[
\det H_n(u,v)=\varepsilon_n\operatorname{Res}(u,v).
\]
The sign and factor \(q\) are essential to the stated fiber formula.

**2. Evaluate the resultant-character series.** Fix a multiplicative character \(\chi\) of exact order \(r\). Define
\[
S_n(\chi)=\sum_{\substack{u\text{ monic},\ \deg u=n\\\deg v<n,\ \gcd(u,v)=1}}\chi(\operatorname{Res}(u,v)),\qquad S_0(\chi)=1.
\]
For any monic irreducible \(P\) of degree \(d\), \(\operatorname{Res}(P^e,v)\) is the \(e\)-th power of the norm from \(\mathbb F_{q^d}\) of the residue of \(v\) modulo \(P\). This norm surjects onto \(\mathbb F_q^\times\). Consequently the sum of \(\chi(\operatorname{Res}(P^e,v))\) over units \(v\bmod P^e\) vanishes unless \(r\mid e\); if \(r\mid e\) it is \(q^{ed}-q^{(e-1)d}\). Chinese remaindering makes these local sums multiplicative in the monic \(u\). Thus, as an identity of formal power series,
\[
\begin{aligned}
\sum_{n\ge0}S_n(\chi)z^n
&=\prod_{P\text{ monic irreducible}}\left(1+\sum_{j\ge1}(q^{rj\deg P}-q^{(rj-1)\deg P})z^{rj\deg P}\right)\\
&=\prod_P\frac{1-q^{(r-1)\deg P}z^{r\deg P}}{1-q^{r\deg P}z^{r\deg P}}\\
&=\frac{1-q^rz^r}{1-q^{r+1}z^r}.
\end{aligned}
\]
Here the last equality is the elementary Euler identity \(\prod_{P}(1-w^{\deg P})=1-qw\), counting all monic polynomials over \(\mathbb F_q\). Extracting coefficients for \(n\ge1\) gives
\[
S_n(\chi)=\begin{cases}(q-1)q^{n+n/r-1},&r\mid n,\\0,&r\nmid n.\end{cases}
\]

**3. Transfer and invert the characters.** The signed resultant identity and exact \(q\)-to-one map in Step 1 show that the Hankel character sum equals \(q^{-1}\chi(\varepsilon_n)S_n(\chi)\), proving the displayed Fourier formula. For the trivial character, \(S_n=(q-1)q^{2n-1}\), so the number of nonsingular matrices is \((q-1)q^{2n-2}\). Subtract this from the total \(q^{2n-1}\) to obtain \(N_{n,q}(0)=q^{2n-2}\). Fourier inversion on the cyclic group \(\mathbb F_q^\times\) gives
\[
N_{n,q}(t)=\frac1{q-1}\sum_{\chi}\chi(t^{-1})\sum_{\det H\ne0}\chi(\det H),\qquad t\ne0,
\]
which is precisely the asserted formula. Character sums of exact order \(r\) are the Ramanujan sum \(c_r(j)\).

**4. Prove the criterion for uniformity.** If \(\gcd(n,q-1)=1\), every nontrivial character has order \(r\nmid n\), hence every nontrivial Fourier coefficient vanishes and the nonzero fibers all equal \(q^{2n-2}\). Conversely if \(\gcd(n,q-1)>1\), the cyclic multiplicative group has a nontrivial character of some order \(r\mid n\), and its nonzero coefficient is \((q-1)\chi(\varepsilon_n)q^{n+n/r-2}\ne0\). By Fourier orthogonality, the fibers cannot be uniform. This proves necessity and sufficiency.

## Verification

The independent standard-library script `verify_hankel.py` constructs the Hankel determinants by finite-field Gaussian elimination and calculates the predicted fibers from multiplicative-group discrete logs and integer Ramanujan sums. It checks prime fields and the extension fields \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_9\), including cases with nontrivial multiplicative character orders. The completed execution checked \(27\) combinations of \((q,n)\), \(127102\) matrices, and \(136\) determinant fibers. It returned `VERIFY_OK fields=8 cases=27 enumerated_matrices=127102 predicted_fibers=136`. To rerun: `python verify_hankel.py`. This finite verification is corroborative and cannot establish the universally quantified formulas without the proof above.

For orientation: over \(\mathbb F_5\) and \(n=2\), the ordered fiber counts \((N(0),N(1),N(2),N(3),N(4))\) are \((25,30,20,20,30)\); the distinction is invisible to a total nonsingularity count.

## Relationship to prior work

García-Armas, Ghorpade, and Ram [1] prove the exact \(q\)-to-one correspondence of coprime polynomial pairs with nonsingular Hankel matrices and give the complete rank counts. Their Theorem 3.5 and Section 5 provide the indispensable map and the aggregate nonsingular count, but their inspected text does not state character spectra or separate prescribed nonzero determinants. Dwivedi and Grinberg [2] refine classical rank counts after fixing initial anti-diagonal entries (Theorem 1.5), a different parameter than fixing determinant values. Their historical discussion points back to Daykin's 1960 rank-count theorem [3]. This result instead performs multiplicative Fourier inversion on the determinant; the explicit character-order cutoff and the sharp uniformity criterion are additional assertions not implied by rank or initial-entry enumerations alone.

## Limitations

The classification applies to all *square* Hankel matrices with unrestricted defining coefficients; it does not enumerate determinant fibers for additional coefficient restrictions, matrices over general finite rings, or other structured matrix spaces. It is a self-contained mathematical derivation using established polynomial/Hankel correspondences, not an independent review of the published literature. Historical articles on persymmetric-matrix distributions may contain related formulations not accessible for complete comparison; originality therefore remains subject to specialist literature confirmation. A computational test on finitely many fields and orders cannot replace the proof.

## References

[1] M. García-Armas, S. R. Ghorpade, and S. Ram, *Relatively Prime Polynomials and Nonsingular Hankel Matrices over Finite Fields*, arXiv:1011.1760v1, first posted 2010-11-08, especially Proposition 3.4, Theorem 3.5, and Theorem 5.1. https://arxiv.org/html/1011.1760v1

[2] O. D. Dwivedi and D. Grinberg, *On the rank of Hankel matrices over finite fields*, arXiv:2109.05415v1, first posted 2021-09-12, especially Theorems 1.1 and 1.5. https://arxiv.org/html/2109.05415v1

[3] D. E. Daykin, *Distribution of Bordered Persymmetric Matrices in a Finite Field*, Journal für die reine und angewandte Mathematik **203** (1960), 47–54, DOI: 10.1515/crll.1960.203.47. Historical rank-count source as identified in [1] and [2]; full text not inspected.
