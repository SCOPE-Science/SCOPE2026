# A five-residue joint rank-defect law for one-sided annihilating matrix projections

## Finding

Fix a prime power \(q\ge2\). For each integer \(n\ge1\), sample uniformly from the ordered pairs \((E,F)\in M_n(\mathbb F_q)^2\) satisfying \(E^2=E\), \(F^2=F\), and \(EF=0\), without imposing \(FE=0\). Let \(r=\operatorname{rank}E\), \(s=\operatorname{rank}F\), and \(\delta=\min(r,s)-\operatorname{rank}(FE)\). Write \(n=5m+h\), where \(0\le h\le4\), and put \(I_n=r-2m\) and \(J_n=s-2m\).

Define the convergent Euler products and theta sums
\[
 \Phi_a(q)=\prod_{k=1}^a(1-q^{-k}),\qquad
 \Phi_\infty(q)=\prod_{k=1}^{\infty}(1-q^{-k}),
\]
\[
 Q(x,y)=2x^2+xy+2y^2,\quad
 \Theta_{q,h}=\sum_{i,j\in\mathbb Z}q^{-Q(i-2h/5,j-2h/5)}.
\]
Set \(\nu_{q,d}(k)=q^{-k(k+d)}\Phi_\infty(q)/(\Phi_k(q)\Phi_{k+d}(q))\) for nonnegative integers \(d,k\). Then, **along every fixed residue class \(n\equiv h\pmod5\)**, the *joint* law of \((I_n,J_n,\delta)\) converges in total variation on \(\mathbb Z^2\times\mathbb Z_{\ge0}\) to
\[
 \boxed{\mu_{q,h}(i,j,k)=
 \frac{q^{-Q(i-2h/5,j-2h/5)}}{\Theta_{q,h}}
 \frac{q^{-k(k+|i-j|)}\Phi_\infty(q)}
 {\Phi_k(q)\Phi_{k+|i-j|}(q)}.}
\]
In particular the two factor ranks fluctuate on a *bounded*, coupled, five-residue discrete-Gaussian scale around \(2n/5\), while the opposite product has a nontrivial rectangular-matrix rank defect depending on their rank imbalance. The limiting law is not a product law for the three coordinates.

A sharp rarity law isolates when one-sided annihilation becomes two-sided. Let
\[ \Xi_{q,a}=\sum_{i,j\in\mathbb Z}
 q^{-2[(i-a/3)^2+(j-a/3)^2+(i-a/3)(j-a/3)]},
 \quad a\in\{0,1,2\}. \]
Then, with \(a=n\bmod3\) and \(h=n\bmod5\),
\[
 \boxed{\Pr(FE=0\mid EF=0)
 \sim q^{-2n^2/15}\frac{\Xi_{q,a}}{\Theta_{q,h}}.}
\]
In particular the reverse zero product is exponentially rare with the sharp quadratic exponent \(2/15\) and a positive **fifteen-residue prefactor**. This is a large-deviation statement and does not follow merely by taking a fixed defect in the joint weak limit.

There is an asymptotic equivalence with a different one-sided annihilation model. Let \(Z_n^{\mathrm{proj}}\) count the above pairs, and let \(Z_n^{\mathrm{mix}}\) count ordered pairs \((P,N)\) with \(P^2=P\), \(N^2=0\), \(PN=0\) in the same matrix algebra. Then
\[
 \boxed{Z_n^{\mathrm{proj}}\sim Z_n^{\mathrm{mix}}
 \sim \frac{q^{4n^2/5}\Theta_{q,h}}{\Phi_\infty(q)^2}
 \quad(n\equiv h\pmod5).}
\]
Moreover the joint two-rank distribution of \((P,N)\), centered by \(2m\) in both coordinates, has the same \(\Theta_{q,h}\)-normalized lattice limit as \((I_n,J_n)\), in total variation. These asymptotic conclusions, not the separately known finite enumeration formulas for the two models nor the classical rectangular-matrix rank-defect distribution, are the asserted contribution.

## Assumptions and scope

Throughout, \(q\) is a **fixed** prime power and \(n\to\infty\) through one specified residue class modulo five. Matrix pairs are ordered and labeled, not modulo simultaneous similarity. The multiplication order is material: the condition is \(EF=0\), but \(FE\) may be nonzero. Rank is ordinary vector-space rank; the defect \(\delta\) is always nonnegative. The square-zero condition in the comparison ensemble concerns the *second* matrix, not the first. The limiting distributions concern exact integer-valued centered ranks, not rescaled continuous Gaussians. The asserted asymptotic equivalents are not uniform as \(q\to\infty\).

## Proof

**1. Block parametrization and exact finite weights.** For a rank-\(r\) idempotent \(E\), write \(V=U\oplus W\), with \(U=\operatorname{im}E\), \(W=\ker E\), of dimensions \(r\) and \(n-r\). There are \({n\brack r}_q q^{r(n-r)}\) such projections. Relative to the decomposition, \(EF=0\) forces
\[
 F=\begin{pmatrix}0&0\\ C&D\end{pmatrix}.
\]
The equation \(F^2=F\) is equivalent to \(D^2=D\), \(DC=C\). Hence \(s=\operatorname{rank}F=\operatorname{rank}D\), with \(0\le s\le n-r\); for each rank-\(s\) projection \(D\) on \(W\), the map \(C:U\to\operatorname{im}D\) is arbitrary. Its matrix in any bases is uniformly distributed over \(M_{s\times r}(\mathbb F_q)\), and \(\operatorname{rank}(FE)=\operatorname{rank}C\). Therefore, using the Gaussian coefficient \({a\brack b}_q\), the number of pairs with specified \(r,s\) is
\[
 L_n(r,s)={n\brack r}_q{n-r\brack s}_q
 q^{r(n-r)+s(n-r-s)+rs}
 =q^{D_n(r,s)}\frac{\Phi_n}{\Phi_r\Phi_s\Phi_{n-r-s}},
\]
where \(D_n(r,s)=2n(r+s)-2r^2-2s^2-rs\). Invalid rank ranges have weight zero. The number of \(s\times r\) matrices of rank \(t\) equals \({r\brack t}_q\prod_{a=0}^{t-1}(q^s-q^a)\). Thus, conditional on \((r,s)\),
\[
 \Pr(\operatorname{rank}(FE)=t\mid r,s)
 =q^{-(r-t)(s-t)}
 \frac{\Phi_r\Phi_s}{\Phi_t\Phi_{r-t}\Phi_{s-t}}.
\]
These exact finite counts are included only as the established inputs needed to prove the limiting assertions.

**2. Five-residue lattice saddle.** Put \(n=5m+h\), \(r=2m+i\), \(s=2m+j\). Direct completion of squares gives the exact identity
\[
 D_n(r,s)=\frac{4n^2}{5}-Q(i-2h/5,j-2h/5).
\]
The quadratic form has eigenvalues \(3/2\) and \(5/2\). In particular \(Q(x,y)\ge(3/2)(x^2+y^2)\), and its lattice theta series is finite and positive. On every fixed lattice point \((i,j)\), the admissibility conditions hold for all sufficiently large \(m\), while \(r,s,n-r-s\to\infty\). Consequently
\[
 \frac{L_n(2m+i,2m+j)}{q^{4n^2/5}}
 \longrightarrow \frac{q^{-Q(i-2h/5,j-2h/5)}}{\Phi_\infty^2}.
\]
For every nonnegative integer \(a\), \(0<\Phi_\infty\le\Phi_a\le1\); hence the normalized weights are bounded above by \(\Phi_\infty^{-3}q^{-Q}\), a summable function of \((i,j)\) independent of \(n\). Dominated convergence proves
\[
 \lim_{\substack{n\to\infty\\n\equiv h\ (5)}}
 q^{-4n^2/5} Z_n^{\mathrm{proj}}=
 \Theta_{q,h}/\Phi_\infty^2.
\]
It also proves convergence in total variation of the centered rank pair to the normalized theta weights: pointwise convergence of probability masses to a mass-one distribution on a countable space implies convergence in \(\ell^1\).

**3. Rectangular rank defect.** If \(r\le s\) and \(\Delta=s-r\), substitute \(t=r-k\) in Step 1. With \(r\to\infty\) and \(\Delta\ge0\) fixed, its probability tends to \(\nu_{q,\Delta}(k)\), with the same conclusion for \(s\le r\) by transposition. Each \(\nu_{q,\Delta}\) is a probability distribution: the finite rank probabilities sum to one, and their tails obey the uniform bound \(C_q\sum_{k\ge K}q^{-k^2}\), since every Euler factor lies between \(\Phi_\infty\) and one. Thus no probability mass escapes to infinity. For fixed \((i,j,k)\), Step 2 and this conditional convergence give the stated joint pointwise limit; summing over the lattice gives one. Applying the same countable-space \(\ell^1\) argument proves **joint total-variation convergence**. The conditional law explicitly depends on \(|i-j|\), so it does not reduce to three independent coordinates.

**4. Sharp two-sided rarity.** The additional equation \(FE=0\) is equivalent to \(C=0\) in Step 1, so for any feasible \(r,s\) its population is precisely \(U_n(r,s)=L_n(r,s)q^{-rs}\). It has exponent
\[
 D_n(r,s)-rs=2n(r+s)-2(r^2+s^2+rs).
\]
Writing \(n=3m+a\), \(r=m+i\), \(s=m+j\), another exact completed square gives
\[
 D_n(r,s)-rs=\frac{2n^2}{3}-2\left[(i-a/3)^2+(j-a/3)^2+(i-a/3)(j-a/3)\right].
\]
The quadratic form is positive definite, and on any fixed lattice point all three ranks \(r,s,n-r-s\) grow, so the Euler quotient again tends to \(\Phi_\infty^{-2}\). The same domination argument as Step 2 proves
\[
 \#\{(E,F):E^2=E,F^2=F,EF=FE=0\}
 \sim q^{2n^2/3}\Xi_{q,a}/\Phi_\infty^2.
\]
Dividing by the denominator from Step 2 yields the sharp quadratic-exponent probability and the combined modulus-fifteen prefactor. No pointwise weak-limit argument is used for this rare event.

**5. Comparison with square-zero factors.** A rank-\(s\) square-zero matrix \(N\) is equivalent to a flag \(\operatorname{im}N\subset\ker N\) with dimensions \(s,n-s\), together with an isomorphism \(V/\ker N\to\operatorname{im}N\). There are \({n\brack s}_q{n-s\brack s}_q|\mathrm{GL}_s(q)|\) such matrices, possible only if \(2s\le n\). For each, the rank-\(r\) idempotents \(P\) with \(PN=0\) are the projections whose kernel contains \(\operatorname{im}N\); there are \({n-s\brack r}_q q^{r(n-r)}\). Write their product as \(M_n(r,s)\). Simplifying the Gaussian products yields the **same** quadratic exponent \(D_n(r,s)\) and, on common rank support, the exact ratio
\[
 \boxed{\frac{L_n(r,s)}{M_n(r,s)}=
 \frac{\Phi_{n-2s}(q)}{\Phi_{n-s}(q)}.}
\]
For any fixed \(i,j\), we have \(s=2m+j\) and \(n-2s=m+h-2j\to\infty\), so the ratio tends to one, while the square-zero feasibility condition is eventually satisfied. The mixed weights have the same pointwise normalized limit as Step 2. Their Euler quotients are uniformly bounded by an appropriate constant depending only on \(q\), and the shared positive-definite quadratic controls the tails. Dominated convergence gives both the same asymptotic total and the same centered two-rank law in total variation. Equivalently, the two exact counting formulas yield asymptotically indistinguishable total mass despite their distinct finite-dimensional constraints. This completes the proof. \(\square\)

## Verification

The standalone `verify_one_sided_theta.py` evaluates exact Gaussian-binomial formulas using integer arithmetic, directly enumerates every idempotent-matrix pair for the prime-field test cases \((n,q)=(1,2),(2,2),(3,2),(2,3),(3,3)\), and checks their two factor ranks and opposite product rank. It confirms the mixed-pair ratio for every admissible rank cell for \(1\le n\le34\) and the field-size parameters \(q=2,3,4,5\), without floating-point arithmetic, and checks complete rectangular rank enumerations. It additionally checks the bidirectional-zero rank cells and the fifteen-residue rarity formula, and compares finite totals with the five-residue theta normalization through \(n=50\). The completed output is embedded as `verification_output.txt`. Exhaustive finite tests establish only the listed finite instances; the proof supplies the general and asymptotic claims.

For illustration, over \(\mathbb F_2\) the ratio \(Z_n^{\mathrm{proj}}/Z_n^{\mathrm{mix}}\) is approximately \(1.09035\) at \(n=20\), \(1.02258\) at \(n=30\), and \(1.00141\) at \(n=50\). The ratio is **not** identically one at finite size.

## Relationship to prior work

Călugăreanu and Pop (2024), in a study with primary MSC2020 15B33, investigate products of nilpotent matrices that are idempotent, and explicitly note the distinct phenomenon of nilpotent products of idempotents. Their finite factorization results do not state a one-sided annihilation probability limit. The Gaussian count of finite-field idempotents, and the exact joint rank formula for two arbitrary finite-field idempotents and both ordered products, already give the finite-rank information from which Step 1 can be derived; **that exact enumeration is not claimed as new**. Likewise, the published component and rank-stratum formulas for one-sided idempotent–square-zero pairs already provide the finite mixed weights in Step 4, and Fulman and Goldstein's rectangular-matrix rank theory gives the standard defect law used in Step 3. The claimed contribution is the assembled *joint* five-residue total-variation law **under one-sided annihilation**, the sharp **fifteen-residue two-sided-annihilation rarity law**, and the explicit asymptotic equivalence of two algebraically different annihilating-pair ensembles, retaining the rank-dependent reverse-product defect kernel. The comparisons do not establish exhaustive historical priority; a more general conditional matrix-pair limit theorem may cover the joint law.

## Limitations

This does not claim new finite Gaussian enumeration, new rectangular-matrix nullity distributions, or new five-periodic maximal-component counts for the mixed square-zero model. It does not prove any independence of all three limit coordinates, nor supply a uniform-in-\(q\) error rate. It concerns fixed field size and the large-dimension limit, not finite-size equality of the two ensembles. Historical-priority risk persists for uncatalogued matrix-pair asymptotics.

## References

1. G. Călugăreanu and H. F. Pop, *Idempotents which are products of two nilpotents*, Special Matrices **12** (2024), article 20240004, first publicly published 2024-04-19; primary MSC2020 15B33. https://doi.org/10.1515/spma-2024-0004 . Full published article text inspected.
2. *Joint rank distribution for products of two finite-field idempotents* (2026-10-12), full public result: https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-joint-rank-distribution-for-products-of-two-finite-field-idempot--3c6fd019df5a/RESULT.md . The preexisting exact full joint finite-field distribution is explicitly credited.
3. *Complete three-rank census of idempotent matrix pairs with idempotent product* (2026-10-25), full public result: https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-complete-three-rank-census-of-idempotent-matrix-pairs-with-idemp--0caa4d1d1d52/RESULT.md . The finite counting baseline for idempotent-product pairs is credited.
4. *Five-periodic top-component counts for one-sided annihilating idempotent–square-zero matrix pairs* (2026-11-08), full public result: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-five-periodic-top-component-counts-for-one-sided-annihilating-id--5aa5dce3fcca/RESULT.md . The published finite mixed-model rank census and dimension calculation are credited.
5. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, Annals of Probability **43** (2015), 1274–1314. https://doi.org/10.1214/13-AOP889 . The classical rectangular-matrix defect limit and quantitative total-variation context are credited.
