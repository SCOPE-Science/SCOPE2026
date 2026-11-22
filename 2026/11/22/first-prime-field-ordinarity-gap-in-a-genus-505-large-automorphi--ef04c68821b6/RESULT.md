# First prime-field ordinarity gap in a genus-505 large-automorphism pencil

## Finding

Let \(k=\mathbb F_{23}\), and let \(\mathcal X_\lambda\) denote the smooth projective normalization of the plane curve
\[
(x+y)^{24}-2\big((xy)^{23}+xy\big)-\lambda(x-y)^{24}=0,
\quad \lambda\in k\setminus\{1,-1\}.
\]
Its Sylow-\(23\) quotient is the genus-\(21\) hyperelliptic curve
\[
F_\lambda:\quad w^2=v^{44}+2\lambda v^{22}+1.
\]
For all 21 admissible rational parameters, the exact geometric Jacobian \(23\)-ranks are as follows.

| Rank of \(F_\lambda\) | Parameters \(\lambda\in\mathbb F_{23}\) | Count | Rank of \(\mathcal X_\lambda\) |
|---:|---|---:|---:|
| 10 | \(0\) | 1 | 252 |
| 17 | \(9,14\) | 2 | 413 |
| 19 | \(4,6,7,10,11,12,13,16,17,19\) | 10 | 459 |
| 20 | \(2,3,5,8,15,18,20,21\) | 8 | 482 |

In particular **none of the 21 prime-field members is ordinary**, even though the family has geometrically ordinary members. Among primes \(5,7,11,13,17,19,23\), the counts of smooth prime-field ordinary members are respectively \(2,2,2,8,8,10,0\); thus \(23\) is the first prime \(p\ge5\) with the gap.

Over \(\mathbb F_{529}=\mathbb F_{23}(\omega)\), with \(\omega^2=-1\), all 527 smooth marked parameters have quotient ranks distributed as
\[
10:1,\quad17:2,\quad19:24,\quad20:10,\quad21:490.
\]
Thus 490 members of this same pencil become ordinary upon allowing quadratic-field parameters; an explicit ordinary parameter is \(\lambda=3\omega\). These counts concern **marked coefficients**, not distinct geometric isomorphism classes.

## Assumptions and scope

All curves are smooth projective normalizations. The plane equation is the natural \(\mathrm{PGL}_2(23)\)-invariant pencil constructed by Borges–Korchmáros–Speziali; it has a geometrically irreducible smooth projective normalization of genus \(505\) for \(\lambda\ne\pm1\). The smoothness condition for the quotient polynomial follows independently from its derivative: a multiple root exists exactly at \(\lambda^2=1\). The rank is the *geometric* \(23\)-rank of the Jacobian, unaffected by extension of the constant field. No claim is made about the number of abstract isomorphism classes.

## Proof

**1. Quotient and rank comparison.** Proposition 8.13 of Borges–Korchmáros–Speziali (2022) identifies the quotient \(F_\lambda\), gives its genus \(p-2\) for \(p=q\) prime, and proves
\[
\gamma(\mathcal X_\lambda)=p\,\gamma(F_\lambda)+(p-1).
\]
Their Proposition 8.5 yields \(g(\mathcal X_\lambda)=p^2-p-1\). At \(p=23\), these become \(g(F)=21\), \(g(\mathcal X)=505\), and \(\gamma(\mathcal X)=23\gamma(F)+22\). These structural relations are prior work, not newly asserted discoveries.

**2. Explicit Cartier diagonal.** In characteristic \(p=23\) the hyperelliptic Cartier–Manin matrix, in the differential basis \(v^{i-1}dv/w\) for \(1\le i\le21\), has entries
\[
M_{ij}=[v^{23i-j}]\big(v^{44}+2\lambda v^{22}+1\big)^{11}.
\]
The right-hand polynomial has exponents divisible by 22, and \(23i-j\equiv i-j\pmod {22}\), with \(|i-j|<22\). Hence \(M\) is diagonal and
\[
M_{ii}=[z^i](1+2\lambda z+z^2)^{11}=(-1)^i P_i(\lambda),
\quad 1\le i\le21,
\]
where \(P_i\) is the classical Legendre polynomial. This special form follows from the general Cartier–Manin formulas of Novoselov (2017), Theorem 9, and is **credited prior work**. The polynomial identity follows by reducing the generating series \((1-2tz+z^2)^{-1/2}\) modulo 23 through degree 21. Since the matrix and all its Frobenius twists are diagonal, its stable rank is the number of nonzero entries:
\[
\gamma(F_\lambda)=\#\{i\in\{1,\ldots,21\}:P_i(\lambda)\ne0\}.
\]

**3. Structural proof of the prime-field gap.** Compute the Legendre polynomials via the exact recurrence
\[
P_0=1,\quad P_1=t,\quad (n+1)P_{n+1}=(2n+1)tP_n-nP_{n-1}.
\]
In \(\mathbb F_{23}[t]\), direct coefficient arithmetic gives the divisibility
\[
Q(t):=t\sum_{j=0}^{10}t^{2j}=\frac{t^{23}-t}{t^2-1}
\;\bigm|\; P_2(t)P_5(t)P_7(t)P_9(t)P_{11}(t).
\]
The 21 simple roots of \(Q\) are precisely \(\mathbb F_{23}\setminus\{\pm1\}\); therefore every admissible parameter zeroes at least one Hasse diagonal entry. This proves the universal nonordinarity claim without treating a sampling experiment as a proof. For the finer rank counts, exact recurrence evaluation for each of these 21 parameters, independently checked by expanding \((1+2\lambda z+z^2)^{11}\), yields the four exhaustive groups displayed above.

**4. First-prime property.** The same recurrence, with exhaustive finite evaluation for each prime \(p\in\{5,7,11,13,17,19\}\), yields ordinary-parameter sets
\[
\begin{array}{c|c}
p&\{\lambda\in\mathbb F_p\setminus\{\pm1\}:\gamma(F_\lambda)=p-2\}\\\hline
5&\{2,3\}\\
7&\{2,5\}\\
11&\{5,6\}\\
13&\{2,4,5,6,7,8,9,11\}\\
17&\{5,6,7,8,9,10,11,12\}\\
19&\{2,4,6,7,8,11,12,13,15,17\}.
\end{array}
\]
These are all primes strictly between 3 and 23, proving minimality in that specified range.

**5. Quadratic extension.** Because \(-1\) is nonsquare in \(\mathbb F_{23}\), \(\mathbb F_{529}=\mathbb F_{23}(\omega)\) with \(\omega^2=-1\). Exhaustive enumeration of its 527 smooth coefficients gives the complete five-bin rank histogram. All values are checked by two independently implemented coefficient methods. More intrinsically, with \(H(t)=\prod_{i=1}^{21}P_i(t)\), the exact identity \(H(3\omega)=\omega\ne0\) certifies a quadratic-field ordinary member, independently of the enumeration.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. It computes the Legendre recurrence and the Cartier coefficient expansion independently, checks the symbolic divisibility certificate in \(\mathbb F_{23}[t]\), verifies every one of 21 rational and 527 quadratic-field smooth parameters, checks smaller-prime minimality, and evaluates \(H(3\omega)\). Successful output ends in `GENUS_505_PGL2_23_ARITHMETIC_GAP_VERIFIED`. The rank relation and genus of the original plane normalization are supplied by the cited Proposition 8.13 and Proposition 8.5, rather than rederived by the code.

## Relationship to prior work

Borges–Korchmáros–Speziali (2022), Section 8.2, give the invariant pencil, quotient, genus and Deuring–Shafarevich rank relation, and Remark 8.14 explicitly raises the problem of ordinary fibers. Novoselov (2017), especially Theorem 9, proves the Legendre polynomial Cartier–Manin formula for a broader hyperelliptic family; that general formula and the diagonal reduction are not claimed new. Neither inspected work provides the **first-prime rational nonordinarity obstruction**, the specific rank strata at \(23\), or the 490 ordinary quadratic-field marked parameters. A separate study of Klein-four quotients of the same plane pencil studies a different quotient and does not imply this arithmetic spectrum.

## Limitations

These results classify only prime-field and quadratic-field *marked parameters* in the specified pencil at characteristic 23. They do not classify abstract isomorphism classes or all extension fields, and they do not assert every geometric member is nonordinary (indeed, an explicit ordinary member is given). The polynomial reduction methodology is established prior art. Historical priority is based on inspected sources and bounded searches, not an exhaustive proof that an equivalent calculation was never published.

## References

- H. Borges, G. Korchmáros and P. Speziali, *Plane curves with a large linear automorphism group in characteristic \(p\)*, arXiv:2202.05765, version 1 publicly submitted 2022-02-11, especially Propositions 8.5, 8.13 and Remark 8.14, https://arxiv.org/html/2202.05765v1.
- S. A. Novoselov, *Hyperelliptic curves, Cartier–Manin matrices and Legendre polynomials*, Prikladnaya Diskretnaya Matematika 37 (2017), 20–31, DOI 10.17223/20710410/37/2, especially Theorem 9, https://www.mathnet.ru/eng/pdm593.
- L. Miller, *Curves with invertible Hasse-Witt-matrix*, Math. Ann. 197 (1972), 123–127, DOI 10.1007/BF01419588; scope discussed in the two references above, original full text not inspected here.
