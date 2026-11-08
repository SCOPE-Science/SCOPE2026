# Local Dold and realization dichotomy for first-kind Pell–Lucas families

## Finding

For each integer \(P\ge 2\), define \(U_0=0\), \(U_1=1\), and \(U_{n+2}=PU_{n+1}+U_n\). Every \(U_n\) for \(n\ge1\) is positive. For a prime \(p\), let \(B^{(p)}_n=p^{\nu_p(U_n)}\) for \(n\ge1\), and let \(\Delta=P^2+4\).

**Theorem.** The following statements hold for every integer \(P\ge2\) and every prime \(p\):

1. The local sequence \(B^{(p)}\) satisfies the Dold congruences if and only if \(p\) is odd and the quadratic character \(\left(\frac{\Delta}{p}\right)=1\). Its Möbius transforms are nonnegative, so this condition is also necessary and sufficient for dynamic realizability.
2. For odd \(p\), let \(r_p=\min\{n\ge1:p\mid U_n\}\). The least positive integer multiplying \(B^{(p)}\) into a Dold sequence is \(r_p/\gcd(r_p,p-1)\). At \(p=2\), it is \(3\) for odd \(P\) and \(2\) for even \(P\).
3. Every \(B^{(p)}\) is almost realizable. The sets of good Dold and realizability primes coincide and have relative prime density \(1/2\); both almost-good sets consist of all primes.

Here the quadratic character is zero at a ramified prime dividing \(\Delta\), hence these primes are bad. For example the ordinary Pell sequence \(P=2\) has good primes exactly the odd primes with \(\left(\frac{2}{p}\right)=1\), or \(p\equiv1,7\pmod8\). Its local sequence at \(p=2\) has repair factor \(2\).

## Assumptions and scope

For an integer sequence \(b=(b_n)_{n\ge1}\) define its Möbius transform
\[
\mathcal L_n(b)=\sum_{d\mid n}\mu(n/d)b_d.
\]
It is **Dold** when \(n\mid\mathcal L_n(b)\) for all \(n\ge1\), and **realizable** when additionally \(\mathcal L_n(b)\ge0\) for all \(n\). It is almost Dold (respectively, almost realizable) when some positive integer multiple is Dold (respectively, realizable). The minimum such integer multiplier is \(\operatorname{Fail}(b)\). Thus all quantifiers in the theorem range over every \(n\ge1\); the prime-density conclusion uses relative natural density within the primes.

## Proof

**Rank and valuation lemma.** Set \(\Delta=P^2+4\). Every odd prime \(p\) has a finite rank \(r=r_p\ge2\). If \(p\nmid\Delta\), then \(p\nmid r\), and
\[
\nu_p(U_n)=\begin{cases}e+\nu_p(n/r),&r\mid n,\\0,&r\nmid n,\end{cases}
\qquad e=\nu_p(U_r)\ge1.
\]
If \(p\mid\Delta\), then \(p\ge5\), \(r=p\), \(e=1\), and the same formula holds. These are instances of the general valuation theorem for Lucas sequences [2, Theorem 1.5], and also follow by the Lucas multiplication identity plus odd-prime lifting. For completeness, \(\gcd(U_m,U_n)=U_{\gcd(m,n)}\) gives the divisibility-by-rank criterion. If the characteristic roots are distinct modulo \(p\), the ratio of roots has multiplicative order \(r\) in \(\mathbb F_p\) or its quadratic extension. This order divides \(p-1\) when \(\Delta\) is a square and divides \(p+1\) when it is a nonsquare. In the double-root case, \(U_n\equiv n(P/2)^{n-1}\pmod p\), giving \(r=p\). General Lucas lifting gives the displayed valuation; for the ramified case the binomial formula for \(U_p\) starts with \(p(P/2)^{p-1}\) and all other terms are divisible by \(p^2\), because \(p\ge5\), proving \(e=1\).

**The odd-prime Möbius transform.** From the lemma,
\[
B^{(p)}_n=1+(p^{e+\nu_p(n/r)}-1){\bf1}_{r\mid n}.
\]
For every \(n>1\), convolution with \(\mu\) therefore vanishes unless \(n=r p^j\), and the only nonzero values (apart from \(\mathcal L_1=1\)) are
\[
\mathcal L_r=p^e-1,\qquad
\mathcal L_{r p^j}=p^{e+j-1}(p-1)\quad(j\ge1).
\]
Indeed, when \(n=rm\), the transform is the divisor convolution of \(d\mapsto p^{e+\nu_p(d)}-1\) with \(\mu\) at \(m\), which vanishes off prime powers and has the displayed positive values. If \(p\nmid\Delta\), the rank is coprime to \(p\), so the denominators of \(\mathcal L_n/n\) have least common multiple exactly \(r/\gcd(r,p-1)\) (the \(r p^j\) terms attain the needed denominator). If \(p\mid\Delta\), then \(r=p,e=1\) and the same formula gives \(\operatorname{Fail}=p\), already forced by \(\mathcal L_p=p-1\). All transforms are nonnegative.

**Splitting dichotomy.** If \(\left(\frac{\Delta}{p}\right)=1\), then \(r\mid p-1\), and the repair factor is \(1\). If the character is \(-1\), then \(r\mid p+1\). But \(r>2\): \(r=1\) is impossible because \(U_1=1\), and \(r=2\) would give \(p\mid P\), whence \(\Delta\equiv4\pmod p\), contrary to nonsplitting. Therefore \(r\nmid p-1\), because \(\gcd(p-1,p+1)=2\). If the character is zero, the ramified calculation gives repair factor \(p>1\). This proves the odd-prime criterion.

**The prime two.** For even \(P\), let \(a=\nu_2(P)\ge1\). The Lucas valuation law gives \(\nu_2(U_n)=0\) for odd \(n\) and \(a+\nu_2(n)-1\) for even \(n\). Hence \(\mathcal L_1=1\), \(\mathcal L_2=2^a-1\), and \(\mathcal L_{2^j}=2^{a+j-2}\) for \(j\ge2\), with all other transforms zero. The least repair is \(2\), and each transform is nonnegative.

For odd \(P\), the valuation law gives \(\nu_2(U_n)=0\) if \(3\nmid n\), \(1\) if \(n\equiv3\pmod6\), and \(\nu_2(n)+2\) if \(6\mid n\). This agrees with the classical Fibonacci two-part sequence. Its nonzero transforms are \(\mathcal L_1=1\), \(\mathcal L_3=1\), \(\mathcal L_6=6\), and \(\mathcal L_{3\cdot2^j}=2^{j+1}\) for \(j\ge2\). They are nonnegative and have least repair \(3\). In neither parity is the unscaled local sequence Dold at two.

Finally, \(\Delta=P^2+4\) is not a square for any positive \(P\): it lies strictly between \(P^2\) and \((P+1)^2\) for \(P\ge2\); the case \(P=1\) also gives nonsquare \(5\). The nontrivial quadratic character of \(\Delta\) therefore takes the values \(\pm1\) on half of the primes, up to finitely many ramified exceptions, by the prime number theorem in arithmetic progressions. This gives density \(1/2\) and completes the proof.

## Verification

Two finite, independently coded exact-integer verifiers accompany this result: `verify.py` and `independent_verify.py`. They construct the recurrence, compute valuations and Möbius transforms directly, test predicted minimal repair multipliers and nonnegativity, and compare the Legendre-symbol criterion. The calculations are checks of finite initial segments only; the theorem for every parameter and integer index rests on the proof and the cited general valuation theorem.

To reproduce: `python3 verify.py` followed by `python3 independent_verify.py`, using only Python's standard library.

## Relationship to prior work

Chuysurichay, Jaidee, Panraksa and Ward [1, Theorems 2.4, 3.1 and Section 4] determine the local Dold/realizability sets for the classical Fibonacci and companion Lucas sequences, and explicitly ask for corresponding results for general companion and first-kind Lucas sequences. The present theorem treats all first-kind recurrences with second coefficient one and \(P\ge2\), including the nonclassical Pell family. Their Fibonacci case corresponds to the excluded parameter \(P=1\), not the new claim.

Murru and Sanna [2, Theorem 1.5] supply the general prime-adic Lucas valuation formulas used as an ingredient. Their paper concerns valuation and regularity, not the Dold prime spectrum, repair factors or orbit-count positivity. General linear-recurrence Dold classifications [3,4] concern the original recurrence sequence rather than its prime-part transform; the transformation is nonlinear and does not inherit those results. The extension here is the full local Möbius-transform calculation, the uniform splitting characterization and the even/odd parameter dichotomy at two.

## Limitations

The result is restricted to the family \(U(P,-1)\) with integer \(P\ge2\). It does not classify all Lucas pairs \(U(P,Q)\), higher-order recurrences, nor the companion second-kind sequences. The general valuation lemma is a previously published input, not an original claim. Finite tests are corroboration rather than proof. Literature priority remains qualified by possible unindexed equivalent treatments of local prime parts.

## References

[1] S. Chuysurichay, S. Jaidee, C. Panraksa and T. Ward, *The local Dold congruence for Fibonacci and Lucas sequences*, arXiv:2609.24544v1 (21 September 2026), https://arxiv.org/html/2609.24544.

[2] N. Murru and C. Sanna, *On the k-regularity of the k-adic valuation of Lucas sequences*, arXiv:1603.09310v3, Theorem 1.5, https://arxiv.org/pdf/1603.09310; *Journal de Théorie des Nombres de Bordeaux* 30 (2018), 227–237.

[3] J. Byszewski, G. Graff and T. Ward, *Dold sequences, periodic points, and dynamics*, *Bull. Lond. Math. Soc.* 53 (2021), 1263–1298, https://doi.org/10.1112/blms.12531.

[4] G. T. Minton, *Linear recurrence sequences satisfying congruence conditions*, *Proc. Amer. Math. Soc.* 142 (2014), 2337–2352, https://doi.org/10.1090/S0002-9939-2014-12168-X.
