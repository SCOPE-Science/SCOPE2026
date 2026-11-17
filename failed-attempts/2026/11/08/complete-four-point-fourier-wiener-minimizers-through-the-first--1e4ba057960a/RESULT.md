# Complete four-point Fourier Wiener minimizers through the first descent obstruction

## Finding

For each integer \(8\le N\le17\), let \(G=\mathbb Z/N\mathbb Z\). For every four-element subset \(C\subset G\), define its unnormalized character sum and its nontrivial-frequency Wiener sum by
\[
S_C(k)=\sum_{c\in C}e^{-2\pi i kc/N},\qquad
D_N(C)=\sum_{k=1}^{N-1}|S_C(k)|.
\]
The full set of global minimizers of \(D_N\) is exactly **one invertible-affine orbit** for each such \(N\), as follows:

| \(N\) | Representative \(C_N\) | Number of minimizing four-sets | Number of all affine orbits |
|---:|---|---:|---:|
| 8 | \(\{0,2,4,6\}\) | 2 | 6 |
| 9 | \(\{0,1,2,3\}\) | 27 | 4 |
| 10 | \(\{0,1,5,6\}\) | 10 | 9 |
| 11 | \(\{0,1,2,3\}\) | 55 | 4 |
| 12 | \(\{0,3,6,9\}\) | 3 | 21 |
| 13 | \(\{0,1,2,3\}\) | 78 | 7 |
| 14 | \(\{0,1,7,8\}\) | 21 | 17 |
| 15 | \(\{0,1,2,3\}\) | 60 | 18 |
| 16 | \(\{0,4,8,12\}\) | 4 | 25 |
| 17 | \(\{0,1,2,3\}\) | 136 | 11 |

Here “one invertible-affine orbit” means precisely every set \(t+u C_N\) with \(t\in G\) and \(\gcd(u,N)=1\), without other minimizers. Their exact objective values are
\[
\min_{|C|=4}D_N(C)=
\begin{cases}
N-4,&4\mid N,\\[2pt]
4\bigl(\csc(\pi/N)-1\bigr),&N\equiv2\pmod4,\\[2pt]
\displaystyle\sum_{k=1}^{N-1}\left|\frac{\sin(4\pi k/N)}{\sin(\pi k/N)}\right|,&N\in\{9,11,13,15,17\}.
\end{cases}
\]
The range is the complete sequence of four-element problems from the smallest admissible cyclic order through order \(17\), the first order exhibiting a published strict nonglobal single-exchange local minimum. The cases \(4\mid N\) are included for completeness and already follow from the known subgroup-coset theorem; the other seven orders provide the new finite classification.

By the established bipartite reduction, this also gives the exact Fourier edge complexity of every complete bipartite graph \(K_{4,n}\) for \(4\le n\le13\). Writing \(N=n+4\) and \(D\) for the value above, it is
\[
\operatorname{FR}_{\min}(K_{4,n})=
\frac{8n+2(n-4)D+2D^2}{(n+4)\sqrt{8n}},
\]
and exactly the partite labelings whose four-vertex part is one of the stated affine images attain it.

## Assumptions and scope

All arithmetic in a set \(C\) or in its affine action is modulo \(N\). The four elements of \(C\) are distinct. The Fourier transform is unnormalized in \(S_C\); the sum \(D_N\) excludes the zero frequency, where \(S_C(0)=4\). The graph ratio uses the unitary two-dimensional Fourier convention of Ferguson et al. The statement is a finite-range exact classification, not an assertion for all cyclic orders or all subset sizes.

## Proof

**Affine reduction.** If \(C'=t+uC\) with \(\gcd(u,N)=1\), then
\[
S_{C'}(k)=e^{-2\pi i kt/N}S_C(uk).
\]
Multiplication by \(u\) permutes nonzero frequencies, so \(D_N(C')=D_N(C)\). Consequently it suffices to inspect one representative from each affine orbit. In `CHECK.py`, `orbit` explicitly constructs these classes and proves their disjointness and completeness by deleting each entire orbit from the set of all \(\binom N4\) four-subsets. The ten exact orbit counts and winner orbit sizes are given in the table.

**Certified Fourier comparisons.** Put \(Q=10^{13}\). For every \(r\in\mathbb Z/N\mathbb Z\), the checker constructs rational bounds \(l_r\le Q\cos(2\pi r/N)\le u_r\), using the identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\), alternating-series rational brackets for the arctangents, and a degree-36 cosine Taylor polynomial. For an argument of absolute value at most \(\pi<22/7\), the Taylor remainder has absolute value at most \((22/7)^{38}/38!\); the uncertainty in the rational enclosure of \(\pi\) is added using the one-Lipschitz property of cosine. All floor and ceiling operations on the resulting rational numbers use exact integer arithmetic.

For a four-set \(C\), the identity
\[
|S_C(k)|^2=4+2\sum_{\{a,b\}\subset C,\ a<b}\cos(2\pi k(b-a)/N)
\]
gives certified integer lower and upper bounds \(A_k\le Q|S_C(k)|^2\le B_k\). Hence
\[
\frac{\lfloor\sqrt{Q\max(0,A_k)}\rfloor}{Q}
\le |S_C(k)| <
\frac{\lfloor\sqrt{QB_k}\rfloor+1}{Q}.
\]
The integer square root is exact. Summing these inequalities supplies an enclosed interval for \(D_N(C)\) for every orbit representative. For each \(N\) from \(8\) to \(17\), the checker verifies the **strict** inequality that the upper endpoint for the stated winning orbit is below the lower endpoint of every other affine orbit. It exhausts all \(8{,}512\) four-subsets, partitioned into \(122\) affine orbits, and therefore proves both minimum and uniqueness of the minimizing orbit. No floating-point comparison enters the certificate.

**Exact objective formulas.** For \(4\mid N\), the winning set is a coset of the subgroup of order four, so only \(N/4\) Fourier coefficients are nonzero and equal in magnitude to four. Removing the zero frequency yields \(N-4\). For \(N\equiv2\pmod4\), put \(M=N/2\); the winning character sum factors as \((1+e^{-2\pi ik/N})(1+(-1)^k)\), and summing its even-frequency magnitudes gives \(4\bigl(\csc(\pi/N)-1\bigr)\). At odd orders, the geometric-series identity for four consecutive characters gives the stated sine quotient. The graph formula follows from the monotone bipartite identity in Ferguson et al., equation (3), with \(m=4\) and \(n=N-4\).

## Verification

Run `python3 CHECK.py` from the directory containing this file. Only the Python standard library is used. Expected final line:

`CHECK_OK orders=8..17 sets=8512 affine_orbits=122 strict_minimum_all_orders=1`

The certificate constructs all four-subsets and affine classes afresh, computes mathematically rigorous rational enclosures for trigonometric values, and tests strict interval separation of all competitor classes. Its count includes the three already-known subgroup cases. No numeric approximations, finite samples outside the certified range, or partial searches are used to prove the stated finite theorem.

## Relationship to prior work

Ferguson, Gupta, Iosevich, Iosevich, Kelly, Smith, and Yang (2026) reduced optimal complete-bipartite graph labelings to exactly this four-subset Fourier Wiener objective and, in their Question 9.1, explicitly asked for the four-element classification. Their Proposition 9.2 constructs a strict nonglobal single-exchange minimum for order \(17\) and explicitly does **not** assert that their four-term progression is globally minimizing. The present certificate supplies the global answer at that order and at every smaller admissible four-set order. Their subgroup-coset equality theorem already covers orders \(8,12,16\); these are not presented as newly discovered cases. Their two- and three-element classifications do not imply the seven remaining four-element cases.

General finite-prime Littlewood estimates, such as those of Green and Konyagin (2006/2009), address different asymptotic questions rather than the complete exact finite minimizer orbits here. An existing published computation of the Fourier projection norm of four consecutive characters determines the value for a **candidate progression**, not the global minimum among all four-point sets or its uniqueness. The latter distinction is precisely what the exhaustive certificate resolves.

## Limitations

No assertion is made for \(N\ge18\), for other cardinalities, or for robustness under perturbed Fourier data. The result is computer-assisted but exact: the scientific proof depends on the executable exhaustive finite certificate and rational inequalities; a finite experiment without that interval certificate would not prove the classification. Generalization to arbitrary orders remains open. Independently auditing the result has not been performed.

## References

1. S. Ferguson, V. Gupta, A. Iosevich, J. Iosevich, C. Kelly, G. Smith, and S. Yang, *Edge complexity of complete bipartite and complete multipartite graphs*, first submitted October 26, 2026, arXiv:2610.36276, https://arxiv.org/abs/2610.36276. In particular equation (3), Question 9.1, Proposition 9.2, and Appendix A.
2. B. Green and S. Konyagin, *On the Littlewood Problem Modulo a Prime*, arXiv:math/0601565 (2006), Canadian Journal of Mathematics 61 (2009), 141–164, https://arxiv.org/abs/math/0601565.
3. *Exact four-frequency Fourier projection norm on every cyclic group*, published published-finding corpus mathematical record (2026), record ID `2026/10/11/SCOPE-exact-four-frequency-fourier-projection-norm-on-every-cyclic-gro--6fefdbed98ba`. Its candidate-norm scope does not assert four-point global minimization.
