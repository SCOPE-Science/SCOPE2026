# A sharp degree-four place minimum for genus-five hyperelliptic curves over the ternary field

## Finding
For a smooth genus-five hyperelliptic curve \(C/\mathbb F_3\) with a rational Weierstrass point, the natural closed-point invariant \(B_4(C)\) satisfies \(B_4(C)\ge4\). The bound is attained by the smooth curve
\[y^2=x^{11}+x^7+x^5+2x^3+2x.\]
Its point counts are \(N_2=18\) and \(N_4=34\), so \(B_4=(N_4-N_2)/4=4\). Thus the minimum is exactly four on this arithmetic moduli stratum.

## Assumptions and scope
The base field is \(\mathbb F_3\). All curves are smooth, projective, geometrically connected, genus five, hyperelliptic, and possess at least one \(\mathbb F_3\)-rational Weierstrass point. For a positive integer \(n\), write \(N_n=\#C(\mathbb F_{3^n})\) and \(B_n\) for the number of degree-\(n\) closed points. Then \(N_4=N_1+2B_2+4B_4\) and \(N_2=N_1+2B_2\).

## Proof
In odd characteristic, translate a rational Weierstrass point to infinity in the hyperelliptic degree-two map. Every curve under consideration then admits an affine presentation \(y^2=f(x)\), where \(f\in\mathbb F_3[x]\) is squarefree of degree \(11\). The leading coefficient can be made \(1\): if it is \(2\), substitute \(x\mapsto-x\), since the degree is odd. Thus every curve is represented among the \(3^{11}\) monic polynomials
\[f(x)=x^{11}+\sum_{j=0}^{10}c_j x^j,\qquad c_j\in\mathbb F_3.\]
For each such polynomial the number of points over \(\mathbb F_{3^n}\), for \(n=2,4\), is exactly
\[N_n=3^n+1+\sum_{x\in\mathbb F_{3^n}}\chi_n(f(x)),\]
where \(\chi_n\) is the quadratic character extended by \(\chi_n(0)=0\). The appended independent finite-field arithmetic program enumerates all \(177147\) coefficient vectors, calculates \((N_2,N_4)\), then filters those with \((N_4-N_2)/4<4\). There are **exactly 21**: three have \(B_4=0\) and eighteen have \(B_4=2\); none has \(B_4=1\) or \(3\). The program then calculates \(\gcd(f,f')\) over \(\mathbb F_3\) for each of those 21 and finds positive gcd degree in every case. Therefore no smooth curve in this family can have fewer than four degree-four closed points.

For the displayed witness, the exact computations give \(\gcd(f,f')=1\), \(N_2=18\), and \(N_4=34\). Squarefreeness makes its smooth completion genus five. Its four degree-four closed points prove sharpness. All field operations and the 21 smoothness exclusions are exact, not probabilistic samples.

## Verification
Run `python verify_degree4.py` with Python 3, NumPy and SymPy. It asserts irreducibility of the defining polynomials \(u^2+1\) and \(u^4+u^3+u^2+1\) over \(\mathbb F_3\), defines the fields with explicit quotient multiplication, verifies the quadratic character, examines every monic degree-eleven polynomial, checks singularity of all 21 low-\(B_4\) candidates, and verifies the squarefree witness. The program prints `VERIFY_OK` only on completion. The exhaustive enumeration is finite and proves only the stated genus-five rational-Weierstrass case; it does not imply a bound for arbitrary genera.

## Relationship to prior work
Kudo and Harashita (2022) enumerate genus-five hyperelliptic and trigonal curves in characteristic three for extremal numbers of rational points over \(\mathbb F_9\). Their established finite-field enumeration motivates the arithmetic family, but maximizing \(N_2\) does not determine the present minimum of \(B_4=(N_4-N_2)/4\), which depends on \(\mathbb F_{81}\) and on exclusion of all smooth low-degree-four models. Aubry, Herbaut, and Monaldi (2023) study closed points and universal eventual degree thresholds; the present result is an exact lower envelope for a defined genus-five hyperelliptic stratum rather than a global existence threshold.

## Limitations
The result says nothing about genus-five curves without an \(\mathbb F_3\)-rational Weierstrass point, including nonhyperelliptic curves, and it does not classify all equality cases up to isomorphism. The proof is a complete finite calculation, not a symbolic classification of arbitrary higher genus. Historical priority outside the sources inspected remains uncertain; independent audit has not occurred.

## References
1. M. Kudo and S. Harashita, *Genus-five hyperelliptic or trigonal curves with many rational points in characteristic three*, arXiv:2204.06805 (first public April 2022).
2. Y. Aubry, C. Herbaut, and J. Monaldi, *Closed points on curves over finite fields*, arXiv:2310.11218 (2023).
