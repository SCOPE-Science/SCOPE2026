# Hilbert–Schmidt composition classes for every Hadamard lacunarity ratio

## Finding
Let \(\Lambda=\{N_j:j\ge0\}\) be an increasing sequence of positive integers with \(N_{j+1}\ge qN_j\), for some **arbitrary** \(q>1\). Suppose the positive coefficient weights \(\beta_n\) satisfy
\[
0<\beta_n\le1,\qquad c:=\inf_{n\notin\Lambda}\beta_n>0,
\qquad\liminf_{n\to\infty}\beta_n^{1/n}\ge1.
\]
For each analytic disk self-map \(\varphi\), write \(C_\varphi f=f\circ\varphi\) on \(H^2(\beta)\), where \(\|f\|_\beta^2=\sum_{n\ge0}\beta_n|\widehat f(n)|^2\). Let \(\operatorname{HS}(\beta)\) be the set of symbols inducing Hilbert–Schmidt composition operators on this space. Then
\[
\boxed{\operatorname{HS}(\beta)=\operatorname{HS}(\mathbf1)
\quad\Longleftrightarrow\quad\inf_j N_j\beta_{N_j}>0.}
\]
This sharp characterization holds for all Hadamard ratios \(q>1\), including dyadic exceptional sets and ratios at most two. In particular, for \(N_j=2^j\) and \(\beta_{2^j}=2^{-j}\), with all other weights equal to one, the Hilbert–Schmidt composition classes coincide even though the two coefficient Hilbert spaces are different.

The new ingredient is a compact-compression principle: for every nonconstant analytic disk self-map \(\varphi(z)=\sum_{m\ge0}a_mz^m\), choose any integer \(\ell\ge1\) with \(a_\ell\ne0\). Compress multiplication by \(\varphi\) from the lacunary monomials to their \(\ell\)-shifted monomials. Under natural basis identifications the resulting infinite matrix is \(a_\ell I+K\), where \(K\) is Hilbert–Schmidt. This replaces the additive-free lacunarity assumption used in the earlier \(q>2\) argument.

## Assumptions and scope
The coefficient weights are positive, normalized above by one, bounded below away from zero off \(\Lambda\), and satisfy the disk-analyticity root condition written above. There is no monotonicity requirement. The sequence of exponents begins with some positive integer and satisfies a fixed multiplicative gap \(q>1\). All composition symbols map the open unit disk holomorphically into itself; constants are included. Equalities are equalities of *sets* of Hilbert–Schmidt symbols. The proof does not assert a symbol-uniform comparison of Hilbert–Schmidt norms for \(1<q\le2\).

For a symbol \(\varphi\), the exact Hilbert–Schmidt criterion is
\[
\|C_\varphi\|_{\mathcal S_2(H^2(\beta))}^2
=\sum_{n\ge0}\frac{\|\varphi^n\|_\beta^2}{\beta_n}.
\]
Whenever the series converges, composition is the resulting Hilbert–Schmidt extension of its polynomial action: evaluation at every point of the open disk is continuous on \(H^2(\beta)\) by the root condition. The unweighted criterion is the same expression with all weights one. The first public paper motivating this question is dated October 29, 2026, with primary MSC2020 47B33.

## Proof
### 1. Lacunary shifted multiplier lemma
Write \(P\) for orthogonal projection of classical \(H^2\) onto the closed span of \(\{z^{N_j}\}\), and \(Q=I-P\). Let \(\varphi\in H^\infty\), and fix \(\ell\ge1\). On the lacunary coefficient space \(\ell^2\), consider the matrix
\[
B_{ji}=a_{N_j+\ell-N_i},\qquad a_t=0\text{ for }t<0.
\]
Its diagonal is \(a_\ell\). We show \(B-a_\ell I\) is Hilbert–Schmidt. For \(j<i\), the difference \(N_i-N_j\ge(q-1)N_j\), so \(N_j+\ell-N_i<0\) once \(j\) is sufficiently large. Therefore, only finitely many entries below the diagonal are nonzero.

For \(i<j\), put \(t=N_j-N_i\). Because \(N_i\le N_j/q\),
\[
(1-q^{-1})N_j\le t<N_j,
\qquad t<N_j\le\frac{q}{q-1}t.
\]
The multiplicative gap condition implies that at most
\[
L_q=2+\left\lceil\frac{\log(q/(q-1))}{\log q}\right\rceil
\]
different indices \(j\) can satisfy the latter restriction for a fixed positive \(t\). For each fixed \(j\) and \(t\) there is at most one \(i\). Hence
\[
\sum_{i<j}|B_{ji}|^2\le L_q\sum_{t\ge1}|a_{t+\ell}|^2<\infty,
\]
since every bounded analytic function belongs to \(H^2\). Together with the finite lower-triangular part this proves \(B=a_\ell I+K\), \(K\in\mathcal S_2\). The same proof works for every \(q>1\), whether or not two lacunary exponents can add to a third.

The gaps \(N_{j+1}-N_j\) tend to infinity. Consequently there exists \(J\) such that every shifted exponent \(N_j+\ell\), \(j\ge J\), lies outside \(\Lambda\). Let \(R_J\) denote orthogonal projection in \(H^2\) onto the span of the shifted monomials \(\{z^{N_j+\ell}:j\ge J\}\), and \(P_{\ge J}\) the projection onto the original lacunary monomials indexed by \(j\ge J\). Because the compression \(K\) is compact, choose \(J\) larger, if needed, such that its tail-to-tail norm is smaller than \(|a_\ell|/2\). Then
\[
\|R_J(\varphi P_{\ge J}f)\|_2
\ge\tfrac12|a_\ell|\,\|P_{\ge J}f\|_2
\qquad(f\in H^2).
\]
This is a lower bound for the entire tail subspace, not only the individual lacunary monomials.

### 2. The inclusion from the weighted class into the classical class
Suppose that \(C_\varphi\) is Hilbert–Schmidt on \(H^2(\beta)\). Since \(\beta_n\le1\), the criterion in the preceding section and the off-lacunary lower bound yield
\[
\sum_{n\ge0}\|Q\varphi^n\|_2^2
\le c^{-1}\sum_{n\ge0}\|\varphi^n\|_\beta^2
\le c^{-1}\|C_\varphi\|_{\mathcal S_2(H^2(\beta))}^2<\infty.
\]
If \(\varphi\) is constant, both composition operators have rank one, by boundedness of point evaluations. Otherwise some nonconstant Taylor coefficient \(a_\ell\ne0\), \(\ell\ge1\). Apply the compression lemma to \(f=\varphi^n\). Because \(\varphi^{n+1}=\varphi\varphi^n\), because \(R_J\le Q\) as projections, and because multiplication by a disk self-map is a contraction on classical \(H^2\),
\[
\frac{|a_\ell|}{2}\|P_{\ge J}\varphi^n\|_2
\le\|Q\varphi^{n+1}\|_2
+\|Q\varphi^n\|_2
+\|P_{<J}\varphi^n\|_2.
\]
Here the last term arises by subtracting the low lacunary modes from \(P\varphi^n\). The first two sequences on the right are square summable in \(n\). For each fixed Taylor degree \(m\), choose \(0<r<1\) and put \(\eta=\max_{|z|=r}|\varphi(z)|<1\), using the strict maximum-modulus principle. Cauchy's estimate gives
\[
|\widehat{\varphi^n}(m)|\le r^{-m}\eta^n.
\]
Consequently, the sequence of norms of the finitely many low lacunary modes \(P_{<J}\varphi^n\) is also square summable. Squaring and summing the displayed compression inequality proves
\[
\sum_{n\ge0}\|P\varphi^n\|_2^2<\infty.
\]
Adding the already summable \(Q\)-part yields \(\sum_n\|\varphi^n\|_2^2<\infty\), which is exactly \(\varphi\in\operatorname{HS}(\mathbf1)\). Thus **for every \(q>1\)**,
\[
\operatorname{HS}(\beta)\subseteq\operatorname{HS}(\mathbf1).
\]
This inclusion does not require a positive lower bound for \(N_j\beta_{N_j}\).

### 3. Sufficiency of the sharp weight bound
Assume \(b:=\inf_jN_j\beta_{N_j}>0\). Given \(\varphi\in\operatorname{HS}(\mathbf1)\), write \(u_n=\|\varphi^n\|_2^2\). Since \(|\varphi|\le1\) almost everywhere on the circle, \((u_n)\) is nonincreasing. Applying \(\beta_m\le1\) in the numerator of the weighted trace criterion gives
\[
\|C_\varphi\|_{\mathcal S_2(H^2(\beta))}^2
\le c^{-1}\sum_{n\notin\Lambda}u_n
+b^{-1}\sum_jN_ju_{N_j}.
\]
Each block between two consecutive lacunary exponents satisfies
\[
N_ju_{N_j}\le\frac{q}{q-1}
\sum_{n=N_{j-1}+1}^{N_j}u_n
\quad(j\ge1),
\]
and the initial term is bounded by the initial finite sum of \(u_n\). Hence
\[
\sum_jN_ju_{N_j}\le\frac{q}{q-1}\sum_{n\ge0}u_n.
\]
The last expression is finite, proving \(\operatorname{HS}(\mathbf1)\subseteq\operatorname{HS}(\beta)\).

### 4. Necessity of the sharp weight bound
Suppose instead \(\inf_jN_j\beta_{N_j}=0\). Extract a rapidly increasing subsequence \(M_k\in\Lambda\) such that
\[
M_{k+1}\ge2M_k,
\qquad (M_k\beta_{M_k})^{-1}\ge4^k.
\]
Such a subsequence exists under the weaker assumption \(q>1\), by skipping sufficiently many lacunary terms; enlarge its initial terms if needed. By Paley's classical lacunary projection theorem, the projection \(P\) satisfies
\[
\|Ph\|_2\le C_\Lambda\|h\|_{H^1}
\quad\text{for analytic }h\in H^1.
\]
Take pairwise disjoint measurable boundary arcs \(E_k\) of normalized measure \(\varepsilon/(2^kM_k)\), set \(E=\bigcup E_k\), and prescribe a boundary modulus \(\rho\) with \(\rho^2=1-1/M_k\) on \(E_k\) and \(\rho^2=1/4\) elsewhere. For sufficiently small positive \(\varepsilon\), the function \(\log\rho\) is integrable and the outer function \(\varphi\) with boundary modulus \(\rho\) is a holomorphic disk self-map. Geometric series give
\[
\sum_{n\ge0}\|\varphi^n\|_2^2
=\int_{\partial\mathbb D}\frac{1}{1-\rho^2}\,dm
\le\frac43+\varepsilon\sum_{k\ge1}2^{-k}<\infty.
\]
For \(n=M_k\), let \(F_k=\int_E\rho^{2M_k}\,dm\). The estimate \((1-1/M_k)^{M_k}\ge1/4\) gives \(F_k\ge m(E_k)/4\). Cauchy–Schwarz on \(E\), together with the exponentially small integral over its complement, gives
\[
C_\Lambda^2\|\varphi^{M_k}\|_{H^1}^2
\le2C_\Lambda^2m(E)F_k+2C_\Lambda^2 4^{-M_k}.
\]
Choose \(\varepsilon\) so that the first term is at most \(F_k/4\). Since \(M_k\) grows at least geometrically, the second term is at most \(F_k/4\) for all sufficiently large \(k\). Paley's estimate consequently yields
\[
\|Q\varphi^{M_k}\|_2^2
\ge F_k-C_\Lambda^2\|\varphi^{M_k}\|_{H^1}^2
\ge\frac{m(E_k)}8.
\]
Off \(\Lambda\), the weights are at least \(c\). Thus the weighted trace series diverges:
\[
\sum_n\frac{\|\varphi^n\|_\beta^2}{\beta_n}
\ge\sum_{k\text{ large}}\frac{c\,m(E_k)}{8\beta_{M_k}}
=\frac{c\varepsilon}{8}\sum_{k\text{ large}}\frac{2^{-k}}{M_k\beta_{M_k}}
\ge\frac{c\varepsilon}{8}\sum_{k\text{ large}}2^k=\infty.
\]
Therefore \(\varphi\in\operatorname{HS}(\mathbf1)\setminus\operatorname{HS}(\beta)\). This proves necessity and the complete stated equivalence.

## Verification
The independently executable exact-arithmetic script `check_lacunary.py` checks the shifted-monomial matrix coefficients for finite Hadamard sets with ratios \(7/5\), \(3/2\), \(2\), and \(3\); tests the off-diagonal squared-sum estimate against a geometric majorant for a finite polynomial multiplier; and checks dyadic example weights and explicit monomial composition norms. The actual execution returned `LACUNARY_FINITE_CHECK_OK 472`. The result for infinitely many exponents follows from the analytic counting and compactness arguments above, **not** from these finite checks. The main source's theorems and proofs were checked against the precise hypothesis \(q>2\); no bound uniform over symbols has been asserted for \(q\le2\).

## Relationship to prior work
Cruz-Zamorano, Dellepiane, and Seco (2026), Theorem 1.3(b), prove the same equivalence **assuming \(q>2\)**. Their Proposition 4.5 uses \(P[(Pf)^2]=0\), which requires that no sum of two exceptional exponents is exceptional; this can fail for dyadic sets. Their Proposition 4.6 proves the upper inclusion by lacunary block estimates and constructs a counterexample when the sharp weight bound fails; those ingredients adapt to any \(q>1\) by selecting a sparser subsequence. The new argument is the shifted-multiplier compact-compression lemma and its use to obtain the missing inclusion at arbitrary \(q>1\). The earlier Lefèvre–Li–Queffélec–Rodríguez-Piazza study concerns boundedness of *all* composition operators and does not imply this Hilbert–Schmidt classification. The Paley projection theorem and outer-function construction are classical ingredients.

## Limitations
This statement concerns Hilbert–Schmidt membership, not arbitrary Schatten exponents, compactness alone, or unrestricted coefficient weights. The extra root condition ensures that the coefficient space is a space of analytic functions on the full disk. The proof gives equality of symbol classes for \(1<q\le2\), not a uniform norm-equivalence constant in that range. Source searches and comparison of accessible mathematical records do not certify worldwide publication priority. An equivalent result expressed as a lacunary Fourier-multiplier or sequence-space statement could exist outside the examined literature. Independent mathematical verification has not been performed.

## References
1. Francisco J. Cruz-Zamorano, Eugenio Dellepiane, and Daniel Seco, *Compact and Hilbert–Schmidt composition operators on weighted Hardy spaces*, arXiv:2610.40148v1, first publicly posted 2026-10-29. https://arxiv.org/html/2610.40148v1. Especially Theorem 1.3 and Propositions 4.5–4.6.
2. Pascal Lefèvre, Daniel Li, Hervé Queffélec, and Luis Rodríguez-Piazza, *Characterization of weighted Hardy spaces on which all composition operators are bounded*, arXiv:2312.03482, first posted 2023-12-06. https://arxiv.org/abs/2312.03482.
3. R. E. A. C. Paley, classical lacunary-coefficient inequality for analytic \(H^1\) functions, as stated and referenced in Section 4 of arXiv:2610.40148v1.
