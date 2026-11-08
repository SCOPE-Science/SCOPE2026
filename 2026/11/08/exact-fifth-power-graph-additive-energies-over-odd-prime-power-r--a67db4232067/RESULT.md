# Exact fifth-power graph additive energies over odd prime-power residue rings

## Finding

For each odd prime \(p\ne5\) and integer \(k\ge0\), set \(q=p^k\) and let
\[
C_q=\{(x,x^5):x\in\mathbb Z/q\mathbb Z\},\qquad
E_p(k)=\#\{(x,y,z,w)\in(\mathbb Z/q\mathbb Z)^4:\
x+y=z+w,\ x^5+y^5=z^5+w^5\}.
\]
At \(k=0\), the residue ring has one element and \(E_p(0)=1\). Let \(\chi_p\) be the quadratic character on \(\mathbb F_p\), and define
\[
\epsilon_p=\chi_p(-1),\qquad
D_p=3(p-1)(2+\epsilon_p),\qquad
S_p=4p^2-6p+2-6(p-1)(1+\epsilon_p).
\]
Then the **exact ordered additive energy** for every \(k\ge1\) is
\[
\boxed{E_p(k)=p^{2k-2}\left[S_p+D_p\bigl(1+(k-1)(p-1)\bigr)\right]
+\begin{cases}
p^{3k-3},&1\le k\le5,\\
p^{12}E_p(k-5),&k\ge6.
\end{cases}}
\]
For every odd integer \(q\ge1\) not divisible by five, the graph energy is multiplicative:
\[
\boxed{E(C_q)=\prod_{p^k\parallel q}E_p(k).}
\]
The product over the empty set is one. The recurrence is equivalent to a completely explicit rational generating function for the normalized local densities \(R_p(k)=E_p(k)/p^{3k}\), with \(R_p(0)=1\):
\[
\boxed{
\sum_{k\ge0}R_p(k)Z^k=
\frac{1+p^{-2}\left[(S_p+D_p)\frac{Z/p}{1-Z/p}
+D_p(p-1)\frac{(Z/p)^2}{(1-Z/p)^2}\right]
+p^{-3}(Z+Z^2+Z^3+Z^4)}{1-p^{-3}Z^5}.}
\]
For instance, \(E_3(6)=19\,427\,121\) and \(E_7(2)=14\,161\). The latter is distinct from the energy \(9\,169\) of the fifth-power graph over the field with \(49\) elements: the two rings of cardinality \(49\) have different additive collision laws.

## Assumptions and scope

All counted quadruples are ordered and all equations are modulo \(p^k\), with no distinctness restriction on entries. The domain is every odd prime other than five, including the exceptional prime three. The local formulas do **not** claim validity for powers of two or five. The finite-field case \(k=1\) is an already known specialization. For \(q\) with several coprime factors, use the Chinese remainder theorem coordinatewise.

## Proof

**1. Collision polynomial.** For a fixed first-coordinate sum, write
\[
s=x+y=z+w,\qquad d=x-y,\qquad e=z-w.
\]
Because two is a unit, \((s,d,e)\) uniquely parametrizes ordered quadruples satisfying \(x+y=z+w\). The invertible substitution \(a=d-e\), \(b=d+e\) gives the exact polynomial identity
\[
x^5+y^5-z^5-w^5
=\frac5{32}\,s a b(a^2+b^2+4s^2).
\]
For \(p\ne2,5\), the scalar is a unit. Thus \(E_p(k)\) is exactly the number of triples \((s,a,b)\bmod p^k\) satisfying \(F(s,a,b)\equiv0\pmod{p^k}\), where
\[
F(s,a,b)=s a b Q(s,a,b),\qquad Q(s,a,b)=a^2+b^2+4s^2.
\]

**2. Finite-field strata.** Put \(\epsilon=\chi_p(-1)\) and \(\beta=1+\epsilon\), so \(\beta\) is either zero or two. The union of the three coordinate planes over \(\mathbb F_p\) contains \(3p^2-3p+1\) points. The nondegenerate ternary quadratic form \(Q\) has exactly \(p^2\) zeros. On any coordinate plane, its zero set has \(1+\beta(p-1)\) points, because the remaining binary equation is a nonzero-square rescaling of \(u^2+v^2=0\). The intersections of these three plane sections meet pairwise only at the origin, so the intersection of \(Q=0\) with the union of coordinate planes has \(1+3\beta(p-1)\) points. Therefore the number of zeros of \(F\) in \(\mathbb F_p^3\) is
\[
Z_p=4p^2-3p-3\beta(p-1).
\]
For completeness, \(\#\{(u,v):u^2+v^2=t\}=p-\epsilon\) for any nonzero \(t\), obtained by a quadratic-character sum (or counting solutions of \((v-u)(v+u)=t\) after a suitable square-class change). This, together with the \(t=0\) count \(1+\beta(p-1)\), yields \(\#\{Q=0\}=p^2\).

Away from the origin, no point lies on three components of the divisor \(F=0\): on an intersection of two coordinate planes, \(Q\) evaluates to a nonzero square multiple of the remaining nonzero coordinate. Intersections of two coordinate planes give \(3(p-1)\) nonzero points. Intersections of a coordinate plane with \(Q=0\) contribute \(3\beta(p-1)\) additional nonzero points, all distinct. Hence exactly
\[
D_p=3(p-1)(1+\beta)=3(p-1)(2+\epsilon)
\]
nonzero zeros are *double crossings*. All other nonzero zeros are smooth points of exactly one component. They number
\[
S_p=Z_p-1-D_p=4p^2-6p+2-6\beta(p-1).
\]
At primitive zeros of \(Q\), its gradient \((8s,2a,2b)\) is nonzero. At intersections \(Q=0\) with a coordinate plane, the gradients of the two components are independent modulo \(p\), since the other two coordinates are nonzero. The two coordinate planes at an axis intersection likewise have independent gradients. Thus all \(D_p\) crossings are transverse, including at \(p=3\).

**3. Exact local lifting.** A smooth zero class modulo \(p\) has precisely \(p^{2(k-1)}\) zero lifts modulo \(p^k\), by the multivariate simple-root lifting criterion. Near any of the \(D_p\) transverse crossing classes, two component functions and a third free coordinate form integral analytic local coordinates, with unit Jacobian, and the remaining factors are units. Therefore the zero condition is locally \(uv\equiv0\pmod{p^k}\), where both \(u\) and \(v\) are divisible by \(p\). For each crossing class the exact number of zero lifts is
\[
p^{2k-2}\left[1+(k-1)(p-1)\right].
\]
Indeed for \(k\ge2\), writing \(u=pU\), \(v=pV\) makes \(U,V\) uniform modulo \(p^{k-1}\). For independent uniform \(U,V\in\mathbb Z_p\),
\[
\Pr(\nu_p(UV)\ge m)=p^{-m}\left(m+1-\frac mp\right)\quad(m\ge0),
\]
which follows by summing the geometric valuation laws; take \(m=k-2\) and multiply by \(p^{3(k-1)}\). At \(k=1\) the displayed lift count is one, as required.

**4. The singular origin.** As \(F\) is homogeneous of degree five, all \(p^{3(k-1)}\) lifts of the origin vanish modulo \(p^k\) when \(1\le k\le5\). For \(k\ge6\), write \((s,a,b)=p(s',a',b')\). Then \(F(p(s',a',b'))=p^5F(s',a',b')\), and lifting the remaining three variables from modulus \(p^{k-5}\) to modulus \(p^{k-1}\) gives exactly \(p^{12}E_p(k-5)\) solutions from the origin class. Adding the smooth, transverse, and origin contributions proves the stated recurrence for every \(k\ge1\).

**5. Local series and global moduli.** Divide the recurrence by \(p^{3k}\) and sum formally over \(k\ge1\). Its smooth-and-crossing terms contribute the two elementary geometric sums in the displayed rational function, while the origin contributes \(p^{-3}(Z+\cdots+Z^4)+p^{-3}Z^5\sum_{k\ge0}R_p(k)Z^k\). Rearrangement yields the rational generating function. Finally CRT gives a bijection of each ordered collision set for coprime moduli with the product of the corresponding collision sets, proving multiplicativity.

## Verification

Run `python3 verify_quintic_prime_power_energy.py` using Python's standard library. It directly enumerates pair-sum multiplicities, then sums their squares, for seventeen prime-power instances including \(p=3\), \(k=6\); nine composite moduli; and independently enumerates the finite-field smooth/crossing/origin strata for seven primes. The expected successful output is

```text
VERIFY_OK strata_primes=7 local_cases=17 composite_cases=9 max_local_modulus=729 crossed_singular_k6=PASS
```

The finite checks are not an infinite proof. The result for all exponents is proved by the local lifting and homogeneity arguments above.

## Relationship to prior work

Browning's study of equal sums of polynomial values addresses integer solutions and asymptotic bounds; it does not give the exact prime-power modular energy. Bories' work provides general Newton-polyhedron and Igusa-local-zeta methods, but does not evaluate the polynomial \(s a b(a^2+b^2+4s^2)\) or give the displayed coefficients and recurrence. A published complete two-sum spectrum for the fifth-power graph over **finite fields** determines the \(k=1\) case and is acknowledged as prior mathematics; a field of size \(p^k\) is not the ring \(\mathbb Z/p^k\mathbb Z\) for \(k>1\). The new result is the explicit all-exponent prime-power and coprime-composite evaluation, not a reproof of the finite-field case or of general rationality of local zeta functions.

## Limitations

The theorem excludes moduli divisible by two or five. It determines the ordered additive energy (equivalently the constant-input fourth Fourier moment, with an appropriate normalization), but does not classify the complete target-by-target two-sum multiplicities or optimal weighted Fourier-extension constants. The five-step recurrence need not be minimal among all algebraic recurrences for these numbers. General local-zeta methods may allow the same formula to be derived without the present explicit stratification; no absolute historical-priority or independent-certification claim is made.

## References

1. B. Bories, *Igusa's p-adic local zeta function associated to a polynomial mapping and a polynomial integration measure*, arXiv:1012.5087v1 (first public 2010-12-22), particularly the Introduction and Theorem 4.3. https://arxiv.org/abs/1012.5087.
2. T. D. Browning, *The polynomial sieve and equal sums of like polynomials*, arXiv:1306.6767v1 (first public 2013-06-28), Section 1 and Theorems 1.2–1.3. https://arxiv.org/abs/1306.6767.
3. *Complete two-sum spectrum of the finite-field fifth-power graph*, published result (2026), full `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-two-sum-spectrum-of-the-finite-field-fifth-power-graph--f9410cde2e91.
