# A squarefree multiplicative-energy Euler product over \(\mathbb F_q[T]\)

## Finding
For every fixed prime power \(q\), let \(\mathcal S_n(q)\) denote the monic squarefree polynomials of degree exactly \(n\) over \(\mathbb F_q[T]\). Their equal-degree multiplicative energy is
\[
E_{\mathrm{sf}}(q,n)=\#\{(f_1,f_2,f_3,f_4)\in\mathcal S_n(q)^4:f_1f_2=f_3f_4\}.
\]
Then as \(n\to\infty\) with \(q\) fixed,
\[
E_{\mathrm{sf}}(q,n)=(C_q+o_q(1))(n+1)q^{2n},
\qquad C_q=\prod_{P}(1-|P|^{-1})^4(1+4|P|^{-1}+|P|^{-2}),
\]
where \(P\) ranges over every monic irreducible polynomial and \(|P|=q^{\deg P}\). The infinite product converges absolutely to a positive number. Uniformly as prime powers \(q\to\infty\),
\[
C_q=1-9q^{-1}+O(q^{-2}).
\]
The local factor is equivalently \(1-9|P|^{-2}+16|P|^{-3}-9|P|^{-4}+|P|^{-6}\).

## Assumptions and scope
All polynomials are in \(\mathbb F_q[T]\) and monic. Squarefree means no square of a nonconstant irreducible divides the polynomial; the constant polynomial \(1\) is allowed only as an auxiliary degree-zero factor. The theorem is a fixed-field, large-degree asymptotic with \(q\) any prime power, not an error bound uniform jointly in \(q,n\). The notation \(o_q(1)\) indicates a real quantity tending to zero for each fixed \(q\).

## Proof
**1. Unique five-factor decomposition.** Fix an ordered quadruple of squarefree polynomials with \(f_1f_2=f_3f_4\). At each monic irreducible \(P\), the occurrence indicators in \((f_1,f_2,f_3,f_4)\) are binary and have equal sum on the first and last two positions. Precisely six patterns are possible: none; all four; or one of the four patterns pairing a position in \(\{1,2\}\) with one in \(\{3,4\}\). Consequently there exist **unique** monic, individually squarefree, *pairwise coprime* \(G,A,B,C,D\) with
\[
f_1=GAB,\quad f_2=GCD,\quad f_3=GAC,\quad f_4=GBD.
\]
Indeed \(G\) receives primes shared by all four; \(A,B,C,D\) receive the four respective cross patterns. Degree equality at \(n\) gives \(\deg A=\deg D=u\), \(\deg B=\deg C=v\), and \(\deg G=k\), with \(k+u+v=n\). Conversely each such five-tuple yields exactly one admissible ordered quadruple. There is no multiplicity or symmetry quotient in this bijection.

**2. Limiting coprimality probability.** Fix monic squarefree \(G\) of degree \(k\). Independently and uniformly select \(A,D\) among all monic polynomials of degree \(u\) and \(B,C\) among all monic polynomials of degree \(v\). Define \(R_G(u,v)\) as the probability that all four are individually squarefree, mutually coprime, and coprime to \(G\). For each irreducible \(P\), put \(z=|P|^{-1}\). For \(P\nmid G\), the local admissible configurations are: none divisible by \(P\), probability \((1-z)^4\); or exactly one divisible by \(P\) to exponent one, probability \(4(z-z^2)(1-z)^3\). Their sum is \((1-z)^4(1+4z)\). For \(P\mid G\), all four must be indivisible by \(P\), giving \((1-z)^4\).

For any finite list of primes, the exact uniform distribution of sufficiently high-degree monic polynomials in residue classes modulo the product of their squares, followed by the polynomial Chinese remainder theorem, makes the finite-prime event probabilities the products of these factors. Events at primes of degree greater than \(J\) that could invalidate the required conditions are either a square \(P^2\) dividing one of the four polynomials or \(P\) dividing two distinct polynomials. In each instance the probability is at most \(|P|^{-2}\); there are at most ten union-bound possibilities. The tail is bounded uniformly in \(u,v\) by
\[
10\sum_{\deg P>J}|P|^{-2}\le10\sum_{d>J}\frac{q^{-d}}d,
\]
since there are at most \(q^d/d\) monic irreducibles of degree \(d\). When \(G\) is fixed, choose \(J\ge\deg G\). This tail tends to zero. Thus, as \(\min(u,v)\to\infty\),
\[
R_G(u,v)\longrightarrow r_G:=\kappa_q\prod_{P\mid G}(1+4|P|^{-1})^{-1},
\qquad \kappa_q:=\prod_P(1-|P|^{-1})^4(1+4|P|^{-1}).
\]
Both products converge to strictly positive values because each local factor is \(1+O(|P|^{-2})\) and \(\sum_P|P|^{-2}<\infty\).

**3. Exact sum, Cesàro limit and dominated convergence.** For fixed degrees of the five factors, the four auxiliary monic polynomials have \(q^{2u+2v}=q^{2(n-k)}\) unconstrained possibilities. The unique decomposition therefore gives the *exact identity*
\[
\frac{E_{\mathrm{sf}}(q,n)}{q^{2n}}=
\sum_{\substack{G\ \mathrm{monic\ squarefree}\\ k=\deg G\le n}}q^{-2k}
\sum_{u+v=n-k}R_G(u,v).
\]
For each fixed \(G\), a proportion tending to one of the \(n-k+1\) nonnegative pairs \((u,v)\) have \(\min(u,v)\to\infty\). More precisely the at most \(2M\) boundary pairs with \(\min(u,v)<M\) contribute at most \(2M/(n-k+1)\), while in the interior the convergence in Step 2 is uniform once \(M\) is fixed large. Consequently
\[
\lim_{n\to\infty}\frac{1}{n+1}\sum_{u+v=n-k}R_G(u,v)=r_G.
\]
The summand on the left after weighting by \(q^{-2k}\) is bounded by \(q^{-2k}\). Furthermore
\[
\sum_{G\ \mathrm{monic\ squarefree}}q^{-2\deg G}
\le\sum_{k=0}^\infty q^kq^{-2k}=(1-q^{-1})^{-1}<\infty.
\]
Dominated convergence therefore yields
\[
\lim_{n\to\infty}\frac{E_{\mathrm{sf}}(q,n)}{(n+1)q^{2n}}
=\sum_{G\ \mathrm{monic\ squarefree}}q^{-2\deg G}r_G
=\kappa_q\prod_P\left(1+\frac{|P|^{-2}}{1+4|P|^{-1}}\right)
=C_q.
\]
The last equality follows by multiplying the two local factors; in particular the local factor equals \((1-z)^4(1+4z+z^2)\), not the product of an unrestricted coprimality factor with an ad hoc squarefree density.

**4. Positivity and large-field expansion.** Each Euler factor \((1-z)^4(1+4z+z^2)\) is positive for \(0<z<1\) and is \(1-9z^2+16z^3-9z^4+z^6\). Absolute convergence follows from \(\sum_P|P|^{-2}<\infty\). For degree-one primes there are exactly \(q\) factors, each with logarithm \(-9q^{-2}+O(q^{-3})\). The sum of absolute logarithms of degree-at-least-two factors is \(O(\sum_{d\ge2}q^{-d}/d)=O(q^{-2})\). Hence \(\log C_q=-9q^{-1}+O(q^{-2})\), and exponentiation proves the stated large-field expansion.

## Verification
The self-contained standard-library script `check_sqf_energy.py` enumerates both sides of the five-factor bijection for \(q=2\) and every \(1\le n\le6\); their common values are respectively \(6,6,28,128,528,2264\). It also independently checks the corresponding unrestricted monic counts \(6,32,160,768,3584,16384\) against the exact elementary formula \(q^{2n}[1+n(1-q^{-1})]\) for these cases. The script evaluates the corrected Euler product through degree \(25\) (approximately \(0.017710366303\) at \(q=2\), \(0.074573211040\) at \(q=3\)). Run `python3 check_sqf_energy.py` with Python 3 and no third-party packages. The computation prints `VERIFY_OK`; these finite checks do not prove the infinite asymptotic, which is proved in Steps 1–4.

## Relationship to prior work
Afifurrahman, *Statistics of divisor functions over function fields* (2026), investigates function-field restricted divisor counts and the unrestricted monic multiplicative-energy setting. The squarefree equal-degree restriction treated here has different local admissibility patterns and a new explicit Euler product. Florea, Lalín, Malik and Sahay, *The shifted convolution problem in function fields* (2025), study shifted divisor-function correlations rather than this zero-shift, squarefree multiplicative-energy enumeration. An elementary benchmark for unrestricted monic quadruples is \(E_{\mathrm{all}}(q,n)=q^{2n}[1+n(1-q^{-1})]\), obtained by reducing the common ratio of a product equality; it does not imply the restricted constant \(C_q\). No exhaustive claim concerning all unpublished tables or future literature is made.

## Limitations
The result provides the leading asymptotic for fixed \(q\), not a power-saving error estimate or a uniform joint \(q,n\) expansion. Independent verification has not been performed. Possible previously unindexed work on squarefree divisor correlations remains an originality risk; the mathematical argument is self-contained. Finite enumeration in the checker cannot independently certify a statement for unbounded degree.

## References
1. Muhammad Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (first posted 2026-10-08), https://arxiv.org/abs/2610.11240.
2. Alexandra Florea, Matilde Lalín, Amita Malik and Anurag Sahay, *The shifted convolution problem in function fields*, arXiv:2502.16067v1 (first posted 2025-02-22), https://arxiv.org/abs/2502.16067.
