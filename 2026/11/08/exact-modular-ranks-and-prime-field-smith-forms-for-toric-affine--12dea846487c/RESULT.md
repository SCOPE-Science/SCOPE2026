# Exact modular ranks and prime-field Smith forms for toric affine line tomography

## Finding

Let \(q=p^f\ge3\) be a prime power and write \(T=\mathbb F_q^\times\). The integer point-line incidence matrix \(B_q\), whose rows are indexed by \((a,b)\in T^2\), columns by \((x,y)\in T^2\), and entries by
\[
B_q[(a,b),(x,y)]={\bf1}_{\{y=ax+b\}},
\]
records all nonzero-slope, nonzero-intercept line sums of signals supported on the nonzero-coordinate points.

**Exact arithmetic classification.** For every such field, \(B_q\) is invertible over \(\mathbb Q\). Its singular-value multiset is
\[
\{q-2\}^{1}\ \cup\ \{\sqrt q\}^{(q-2)(q-3)}\ \cup\ \{1\}^{3(q-2)}.
\]
Superscripts in this display denote multiplicities; coincident values are combined. Consequently,
\[
|\det B_q|=(q-2)q^{(q-2)(q-3)/2},\qquad\kappa_2(B_q)=q-2.
\]
The absolute-value identities for Jacobi sums underlying this complex spectrum are classical; the arithmetic rank and Smith conclusions below are the focal claims.

Over the defining characteristic \(p\), the exact rank is
\[
\operatorname{rank}_{\mathbb F_p}(B_q)=
\begin{cases}
\bigl(p(p+1)/2\bigr)^f-2,&p\text{ odd},\\
\bigl(p(p+1)/2\bigr)^f-3,&p=2.
\end{cases}
\]
In particular, while this square transform always recovers complex or rational signals, its modular kernel grows rapidly with extension degree.

For every prime \(p\ge5\), put \(e=(p-2)(p-3)/2\). The entire Smith diagonal over \(\mathbb Z\), in divisibility order, is
\[
\underbrace{1,\ldots,1}_{(p-1)^2-e},\quad
\underbrace{p,\ldots,p}_{e-1},\quad p(p-2).
\]
For \(p=3\) the four Smith factors are all \(1\). Thus the complete obstruction to integral inversion in prime fields is determined, including all characteristics distinct from \(p\) that divide \(p-2\).

## Assumptions and scope

All points and line parameters belong to the same finite field \(\mathbb F_q\), with nonzero coordinates, slopes, and intercepts as specified. Each line-point incidence is counted once. The matrix entries lie in \(\mathbb Z\); all complex singular values use the unnormalized operator on \(\ell^2(T^2)\) with counting measure. The modular rank means rank of the reduction of this integer matrix over \(\mathbb F_p\), equivalently over \(\mathbb F_q\). The Smith result is asserted for prime fields, not for arbitrary extension fields. The excluded order \(q=2\) has no point-line incidences and a singular one-by-one matrix.

## Proof

**Step 1: Jacobi-sum diagonalization.** Reindex the rows by the bijection
\[
(r,s)=(-a/b,\,1/b)\in T^2.
\]
The incidence condition becomes \(rx+sy=1\). For multiplicative characters \(\chi,\psi:T\to\mathbb C^\times\), let \(F_{\chi,\psi}(x,y)=\chi(x)\psi(y)\). Substitution \(u=rx,\ v=sy\) yields
\[
B_q F_{\chi,\psi}(r,s)=J(\chi,\psi)\chi(r)^{-1}\psi(s)^{-1},\qquad
J(\chi,\psi)=\sum_{u\in\mathbb F_q\setminus\{0,1\}}\chi(u)\psi(1-u).
\]
Both character families are orthogonal bases with squared norm \((q-1)^2\). The transformed matrix therefore consists of an inversion permutation followed by diagonal Jacobi multipliers, so its singular values are their absolute values.

With both characters trivial the multiplier is \(q-2\). With exactly one trivial it is \(-1\). With both nontrivial and product trivial it has modulus one (indeed \(J(\chi,\chi^{-1})=-\chi(-1)\)); otherwise its modulus is \(\sqrt q\) by the classical Gauss--Jacobi identity. Counting the four cases gives the stated singular spectrum. All multipliers are nonzero because \(q>2\), establishing rational invertibility and the determinant and condition-number formulas.

**Step 2: Exact rank in defining characteristic.** Work over \(\mathbb F_q\). Since the order \(q-1\) of \(T\) is invertible in characteristic \(p\), the monomials \(u\mapsto u^i\), with \(0\le i\le q-2\), still form a basis of functions on \(T\). Therefore the rank equals the number of nonzero finite-field Jacobi multipliers. When one exponent is zero and the other positive the sum is \(-1\). When both are zero it is \(q-2\), nonzero exactly when \(p\ne2\).

For \(1\le i,j\le q-2\), binomial expansion and the finite-field power sum give
\[
J(i,j)=-(-1)^{q-1-i}{j\choose q-1-i}
\quad\text{if }q-1-i\le j,
\qquad J(i,j)=0\quad\text{otherwise},
\]
with coefficients interpreted modulo \(p\). Lucas's theorem makes this binomial coefficient nonzero precisely when each base-\(p\) digit of \(q-1-i\) does not exceed the corresponding digit of \(j\). The number of ordered digit pairs \((k,j)\) satisfying \(0\le k\le j\le p-1\) is \(p(p+1)/2\), so across \(f\) positions there are \(C^f\) with \(C=p(p+1)/2\). To force \(1\le i,j\le q-2\), exclude \(k=0\) (\(q\) possibilities) and \(j=q-1\) (\(q\) possibilities), restoring their one double-counted overlap. This leaves \(C^f-2q+1\). Adding the \(2(q-2)\) one-trivial cases, and one both-trivial case when \(p\) is odd, yields exactly \(C^f-3+\mathbf1_{p\ne2}\), proving the rank formula over all prime powers.

**Step 3: Exact prime-field Smith form.** Set \(q=p\) prime and \(e=(p-2)(p-3)/2\). For \(p\ge5\), the determinant has \(p\)-valuation exactly \(e\). The rank formula gives \(\operatorname{rank}_{\mathbb F_p}B_p=(p-1)^2-e\), so precisely \(e\) Smith invariant factors are divisible by \(p\). Since their total \(p\)-valuation equals \(e\), each is divisible by \(p\) only to the first power.

Now let \(\ell\mid p-2\) be prime. Since \(\gcd(\ell,p-1)=1\), the full character basis of \(T\), over a finite extension of \(\mathbb F_\ell\), remains invertible. The Jacobi-sum diagonalization from Step 1 therefore applies modulo \(\ell\). Every nontrivial-pair Jacobi sum is a unit modulo \(\ell\): the product with its conjugate/inverse-character counterpart equals \(1\) or \(p\), and \(\ell\nmid p\). The one-trivial sums \(-1\) are units too. The sole vanishing diagonal multiplier is the both-trivial sum \(p-2\). Hence \(\operatorname{rank}_{\mathbb F_\ell}B_p=(p-1)^2-1\).

Consequently the full \(\ell\)-primary determinant factor \(\ell^{v_\ell(p-2)}\) sits in exactly one Smith invariant. There are no other determinant primes. The Smith divisibility chain combines that last factor with one of the \(p\)-invariants, giving exactly \((p-1)^2-e\) ones, \(e-1\) factors \(p\), and one factor \(p(p-2)\). For \(p=3\), the determinant has absolute value \(1\), proving the separate unit-Smith case.

**Step 4: Integral reconstruction identity.** Write \(H=B_q^{\mathsf T}B_q\). Its only possible eigenvalues are \(1\), \(q\), and \((q-2)^2\). Set
\[
s_1=1+q+(q-2)^2,\qquad
s_2=q+(q-2)^2+q(q-2)^2,\qquad
s_3=q(q-2)^2.
\]
Its spectral polynomial implies \(H^3-s_1H^2+s_2H-s_3I=0\) even when these spectral levels coincide. Consequently
\[
B_q^{-1}=\frac{(H^2-s_1H+s_2I)B_q^{\mathsf T}}{s_3}.
\]
This supplies a finite, exact rational backprojection formula without constructing characters.

## Verification

Run the standalone checker in the same directory:

```bash
python toric_radon_checker.py
```

It constructs the actual zero-one incidence matrix, checks defining-characteristic ranks using exact modular elimination, compares complete squared-singular-value multisets in seven fields, verifies the matrix polynomial identity for four fields with integer arithmetic, and computes exact Smith forms for the primes \(3,5,7\). Checked field orders are \(3,4,5,7,8,9,11\). The final expected marker is `TORIC_RADON_SMITH_AND_JACOBI_PASS 7_fields=checked`. The infinite-family claims are established by Steps 1--4, not by finite computations.

## Relationship to prior work

Finite-field line transforms and Jacobi sums are classical. Vandervelde gives the underlying complex Jacobi-sum magnitude classification; no novelty is asserted for those absolute-value identities. Chandler--Sin--Xiang determine Smith forms of **complete** point/flat incidence matrices of finite affine and projective spaces, not the square restricted incidence matrix on \(T^2\) with selected line parameters. Their general monomial-basis and Jacobi-sum methods motivate the comparison, but complete-matrix Smith data do not determine arbitrary square submatrices. Koh studies full finite-field X-ray/Radon operators through harmonic-analytic endpoint inequalities, not the specific defining-characteristic rank and prime-field invariant factors here. The claimed contribution is the exact arithmetic classification for the doubly restricted transform. Overlap with unpublished or differently formulated incidence-scheme results remains a priority risk.

## Limitations

The Smith diagonal is fully determined only in prime fields, whereas the defining-characteristic rank formula covers all prime powers. The result does not characterize Smith factors for composite prime powers, arbitrary deleted point sets, weighted lines, or numerical robustness of modular recovery. The complex Fourier spectrum uses established Jacobi-sum facts. No independent mathematical audit has been performed.

## References

- D. B. Chandler, P. Sin, Q. Xiang, *The invariant factors of the incidence matrices of points and subspaces in PG(n,q) and AG(n,q)*, arXiv:math/0312506v1 (first public 2003-12-30), https://arxiv.org/abs/math/0312506 .
- S. Vandervelde, *Jacobi Sum Matrices*, *American Mathematical Monthly* 119 (2012), 100--115, doi:10.4169/amer.math.monthly.119.02.100 .
- D. Koh, *Sharp endpoint estimates for the X-ray transform and the Radon transform in finite fields*, arXiv:1209.1215v1 (2012-09-06), https://arxiv.org/abs/1209.1215 .
- S. DeDeo and M. Velasquez, *The Radon Transform on \(\mathbb Z_n^k\)*, *SIAM Journal on Discrete Mathematics* 18 (2004), doi:10.1137/S0895480103430764 .
