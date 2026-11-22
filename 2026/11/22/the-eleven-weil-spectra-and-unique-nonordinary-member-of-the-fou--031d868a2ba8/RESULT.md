# The eleven Weil spectra and unique nonordinary member of the four-nodal Kawakita sextics over \(\mathbb F_7\)

## Finding

Let \(C_{a,b}\) denote the normalization of the sextic in the next section. Exactly 29 of the 49 marked coefficient pairs give geometrically integral four-nodal sextics; their normalized genus-six curves have precisely eleven distinct Weil numerators, occurring with the following frequencies.

| \(t\) | \(s\) | Marked pairs | Parameters | \(\#C(\mathbb F_7)\) |
|---:|---:|---:|---|---:|
| -6 | 18 | 2 | (0,3), (3,0) | 26 |
| -4 | 13 | 6 | (0,1), (1,0), (2,6), (4,6), (6,2), (6,4) | 20 |
| -4 | 14 | 1 | (5,5) | 20 |
| -4 | 18 | 1 | (4,4) | 20 |
| -2 | -2 | 4 | (0,6), (4,5), (5,4), (6,0) | 14 |
| -2 | 2 | 4 | (0,5), (1,6), (5,0), (6,1) | 14 |
| -2 | 6 | 2 | (2,3), (3,2) | 14 |
| 0 | -3 | 2 | (1,5), (5,1) | 8 |
| 0 | 1 | 4 | (0,2), (2,0), (2,5), (5,2) | 8 |
| 0 | 9 | 2 | (3,4), (4,3) | 8 |
| 0 | 10 | 1 | (1,1) | 8 |

With the notation of the table, \(L_{C_{a,b}}(T)=(1-tT+sT^2-7tT^3+49T^4)^3\). The unique nonordinary marked parameter is \((a,b)=(5,5)\), with Jacobian \(7\)-rank \(3\), whereas the other 28 have \(7\)-rank \(6\). Exactly \((0,3)\) and \((3,0)\) attain the sharp marked-family maximum of 26 rational points.

## Assumptions and scope

Work over \(k=\mathbb F_7\), with \((a,b)\in k^2\) an **ordered, coefficient-marked** pair. Define

\[
S_{a,b}:X^6+Y^6+Z^6+a(X^4Y^2+X^2Z^4+Y^4Z^2)+b(X^2Y^4+X^4Z^2+Y^2Z^4)-3(a+b+1)X^2Y^2Z^2=0.
\]

The term *four-nodal* means the entire geometric singular locus consists of the four ordinary double points \([\pm1:\pm1:1]\), with independently varying signs. If the condition holds, let \(C_{a,b}\) be its unique smooth projective normalization. No claim is made about projective or abstract isomorphism classes within a Weil type.

## Proof

**Exact geometric singularity classification.** In each of the charts \(Z=1\), \(Y=1\), \(X=1\), form the ideal of the three partial derivatives of the sextic. Compute the reduced Gröbner basis over \(k\). The complete enumeration of 49 pairs gives the three canonical reduced bases

\[
(X^2-1,Y^2-1),\quad(X^2-1,Z^2-1),\quad(Y^2-1,Z^2-1)
\]

simultaneously for exactly the 29 ordered pairs listed in the table. These ideals describe every geometric singular point in each affine chart, not just the rational ones. For each admissible pair \(a+b+3\ne0\); the affine binary quadratic Hessian of the local equation at the four points has nonzero determinant proportional to \(3(a+b+3)^2\), proving each is an ordinary node. Conversely an equation with exactly those four ordinary nodes has precisely these Jacobian ideals because the nodes are reduced, so the 49-pair test is exhaustive. Geometric reducibility would force at least five singular intersection points by Bézout for a degree-six curve split into positive-degree components (every such intersection must be an ordinary node of multiplicity one); hence the curves are geometrically integral. Their genus is \((6-1)(6-2)/2-4=6\).

**Weil numerator.** Kawakita's established quotient decomposition identifies the \(k\)-isogeny class of \(\operatorname{Jac}(C_{a,b})\) as three copies of the Jacobian of the smooth genus-two hyperelliptic curve

\[
D_{a,b}:\quad v^2=-(u^3+bu^2+au+1)((a+b+2)u^3-(a+2b+3)u^2+(b+3)u-1).
\]

The cited decomposition first gives \(\operatorname{Jac}(D_{a,b})\times\operatorname{Jac}(D_{b,a})^2\); the established equal Frobenius counts of both quotients over all finite extensions give the stated cubed polynomial. For every admissible pair, the defining polynomial of \(D_{a,b}\) is squarefree of degree five or six. Exact enumeration of its points over \(\mathbb F_7\) and \(\mathbb F_{49}\) gives \(n_1,n_2\). Define \(t=8-n_1\) and \(s=(n_2-50+t^2)/2\). The genus-two polynomial is \(1-tT+sT^2-7tT^3+49T^4\), yielding the eleven rows above.

**Rank and extremum.** The genus-two \(7\)-rank is the degree of this numerator reduced modulo \(7\), equal to two unless \(7\mid s\), and one when \(7\mid s\) but \(7\nmid t\). The only row with \(7\mid s\) is \((t,s)=(-4,14)\), represented solely by \((a,b)=(5,5)\). Since \(p\)-rank is preserved by isogeny and is additive under products, this produces the stated genus-six ranks. The point count is \(8-3t\), whose maximum and parameters follow from the same complete table.

## Verification

Run `python verify.py` with Python 3.10+ and SymPy 1.12+. The program exhausts 49 parameter pairs and the three projective Jacobian charts; validates exactly 29 reduced singular schemes; verifies smooth genus-two factors; counts all required points of \(D_{a,b}\) over \(\mathbb F_7\) and \(\mathbb F_{49}=\mathbb F_7[i]/(i^2+1)\); and reproduces all eleven rows and rank strata. Independently, it directly enumerates the 57 rational projective-plane points and checks for all 29 parameters that \(\#C_{a,b}(\mathbb F_7)=\#S_{a,b}(\mathbb F_7)+4=3\#D_{a,b}(\mathbb F_7)-16\); the extra four account for the two rational branches at each split node in place of one rational singular point. No approximate numerical computation is used.

## Relationship to prior work

Kawakita introduced this family and proved its Jacobian quotient decomposition and point-count formula in *Certain sextics with many rational points* (2017). Iezzi–Kawakita–Timpanella's June 2023 preprint revisited the family to construct extremal large-field examples. Neither inspected paper gives the complete 49-parameter geometric-singularity census, the eleven \(\mathbb F_7\)-Weil strata, or the unique nonordinary member. The quotient decomposition, genus-two point-count method, and general motivation are credited rather than presented as new.

## Limitations

The classification is specific to \(\mathbb F_7\) and the coefficient-marked two-parameter subfamily. The eleven distinct Weil polynomials classify Jacobian isogeny types, **not** abstract isomorphism classes of curves; two different marked parameter pairs may define isomorphic curves. The result does not determine Cartier \(a\)-numbers or generalized characteristic-seven parameter-locus geometry. An equivalent previously unindexed finite census could affect priority; no independent mathematical audit has been performed.

## References

- M. Q. Kawakita, *Certain sextics with many rational points*, Advances in Mathematics of Communications 11 (2017), 289–292, doi:10.3934/amc.2017020. Accessible full text: https://manypoints.org/upload/322473513.pdf
- A. Iezzi, M. Q. Kawakita and M. Timpanella, *New sextics of genus 6 and 10 attaining the Serre bound*, arXiv:2306.01928v1 (first posted 2023-06-02), https://arxiv.org/abs/2306.01928
