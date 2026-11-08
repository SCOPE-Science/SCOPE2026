# A six-characteristic rational-point law for seventh-index Fermat surfaces

## Finding
Let \(q=p^r\) be any prime power with \(7\mid q-1\), put \(d=(q-1)/7\), and let \(X_{q}\subset\mathbb P^3_{\mathbb F_q}\) be the smooth Fermat surface
\[X_q:\quad X_0^d+X_1^d+X_2^d+X_3^d=0.\]
For every such \(q\), its number of rational points is precisely
\[
\#X_q(\mathbb F_q)=
\begin{cases}
6d+24d^2+43d^3,&p=2,\\
4d^2,&p=3,\\
12d^3,&p=29,\\
12d^2,&p=43,\\
12d^3,&p=71,\\
4d^3,&p=547,\\
0,&\text{all other characteristics}.
\end{cases}
\]
In particular, rational solubility occurs **if and only if** the characteristic belongs to \(\{2,3,29,43,71,547\}\), independently of the extension degree once \(7\mid q-1\). Smoothness follows from \(p\nmid d\). The allowable degree-one case \(q=8\), \(d=1\), is included.

## Assumptions and scope
The field is exactly \(\mathbb F_q\); the four coefficients of the diagonal equation are all \(1\). The surface is considered as a projective subscheme of \(\mathbb P^3\). The claim does not concern twists or arbitrary diagonal coefficients, and the restriction \(7\mid q-1\) is essential. Although \(q\) may be a prime power, the occurrence of solutions depends only on the prime characteristic.

## Proof
**Step 1: seventh-root reduction.** Since \(\mathbb F_q^\times\) is cyclic and \(d=(q-1)/7\), the power map \(u\mapsto u^d\) maps onto the seven seventh roots of unity \(\mu_7\subset\mathbb F_q^\times\), with exactly \(d\) preimages per root. Let \(N_s(p)\) be the number of ordered \(s\)-tuples from \(\mu_7\) summing to zero, for \(1\le s\le4\). The number of affine solutions other than the zero quadruple is
\[\sum_{s=1}^4\binom4s N_s(p)d^s.\]
The scalar action of \(\mathbb F_q^\times\) on each nonzero affine tuple is free, so
\[\#X_q(\mathbb F_q)=\frac1{7d}\sum_{s=1}^4\binom4s N_s(p)d^s.\]

**Step 2: exhaustive finite cyclotomic obstruction.** Let \(\zeta\) be a primitive seventh root of unity in characteristic zero and \(\Phi_7(T)=1+T+\cdots+T^6\). For every multiset \(I\) of size \(1\) through \(4\), with entries in \(\{0,\ldots,6\}\), put \(a_I=\sum_{i\in I}\zeta^i\). No \(a_I\) is zero in characteristic zero, since a nonnegative integral polynomial of degree at most six with at most four monomials cannot be divisible by \(\Phi_7\). There are exactly \(329\) multisets. Computing each absolute norm \(|N_{\mathbb Q(\zeta)/\mathbb Q}(a_I)|\) as the determinant of multiplication by \(a_I\) in the integral basis \(1,\zeta,\ldots,\zeta^5\) gives this **complete certificate**, written as \(\text{norm}:\text{multiplicity}\):
\[1:91,\quad 8:28,\quad29:42,\quad43:42,\quad64:28,\quad71:42,\quad547:42,\quad729:7,\quad4096:7.\]
Any vanishing sum of at most four seventh roots in characteristic \(p\) therefore forces \(p\in\{2,3,29,43,71,547\}\). The certificate can be reproduced by `python verify.py`; it uses exact integer Bareiss determinants, not floating-point approximations.

**Step 3: complete exceptional cases.** For each exceptional prime, evaluate the \(7^s\) ordered exponent tuples in the cyclotomic residue field. For \(p=2\) take \(\Phi_7\)'s irreducible factor \(T^3+T+1\); for \(p=3\), use \(\Phi_7\) itself (irreducible of degree six). For \(p=29,43,71,547\), a primitive seventh root in the prime field is respectively \(7,4,20,9\). These give

| \(p\) | \(N_1(p)\) | \(N_2(p)\) | \(N_3(p)\) | \(N_4(p)\) |
|---|---:|---:|---:|---:|
| 2 | 0 | 7 | 42 | 301 |
| 3 | 0 | 0 | 7 | 0 |
| 29 | 0 | 0 | 0 | 84 |
| 43 | 0 | 0 | 21 | 0 |
| 71 | 0 | 0 | 0 | 84 |
| 547 | 0 | 0 | 0 | 28 |

These computations are independent of the selected primitive root: any two primitive seventh roots differ by an exponent automorphism, which permutes the complete set of ordered exponent tuples. Every other characteristic has \(N_s(p)=0\) for all \(s\le4\). Substitution into Step 1 proves the displayed formulas.

## Verification
Run `python verify.py` using Python 3 with no third-party dependencies. It checks the entire multiset norm certificate (all \(329\) cases), all \(6\) exceptional ordered-tuple distributions (up to \(7^4\) possibilities per characteristic), and independently enumerates projective surface points over \(\mathbb F_{29},\mathbb F_{43},\mathbb F_{71}\), obtaining respectively \(768,432,12000\). The general prime-power assertion follows from the proof; these small direct enumerations are corroborations rather than an extrapolation. Output on successful verification: `VERIFY_SEVENTH_ROOT_OK`.

## Relationship to prior work
Borges, Cook and Coutinho (2018, arXiv:1804.04442) investigate plane sections of Fermat surfaces with \(q=2d+1\), not the seventh-index degree \(d=(q-1)/7\) nor the present point-count law. Voloch and Zieve (2013, arXiv:1310.1772) analyze exponent \(q-1\) on curves and surfaces over extension fields, rather than this exponent. Oliveira (2021, arXiv:2110.07452) characterizes equality in Weil's upper/lower bounds for certain diagonal affine equations with nonzero right-hand side; it does not imply these exact zero and exceptional point counts for the homogeneous projective family. Aubry and Voloch (2026, arXiv:2605.09166) explicitly use norms of short fifth-root sums and exhibit seventh-root phenomena for a **different mixed-monomial surface** in Section 5, without determining this diagonal seventh-index family's sharp exceptional-prime set or point counts. The cyclotomic-norm method itself is not new; the exhaustive seventh-index classification is the specific contribution.

## Limitations
This does not classify non-rational geometric points, all rational lines, twists, or other indices. The norm and residue-field tables are exact finite certificates and are reproducible; no external or independent mathematical audit is claimed. Historical-priority uncertainty remains for potentially differently formulated cyclotomic tables or classical diagonal-equation calculations.

## References
1. H. Borges, G. Cook, M. Coutinho, *Plane sections of Fermat surfaces over finite fields*, arXiv:1804.04442, first public 2018-04-12.
2. J. F. Voloch, M. E. Zieve, *Rational points on some Fermat curves and surfaces over finite fields*, arXiv:1310.1772, first public 2013-10-07.
3. J. A. Oliveira, *On maximal and minimal hypersurfaces of Fermat type*, arXiv:2110.07452, first public 2021-10-14.
4. Y. Aubry, J. F. Voloch, *Rational points on smooth surfaces in \(\mathbb P^3\) over finite fields*, arXiv:2605.09166, first public 2026-05-09, Sections 4–5.
