# An explicit genus-four Artin–Schreier curve realizes the sharp closed-point threshold \(\rho(4,4)=4\)

## Finding
Let \(\mathbb F_4=\mathbb F_2(\omega)\), where \(\omega^2+\omega+1=0\). Write \(B_r(X)\) for the number of closed points of degree \(r\) of a smooth, projective, geometrically integral curve \(X/\mathbb F_4\). Define \(\rho(4,4)\) as the least integer \(n\) such that every such curve of genus four has \(B_r(X)>0\) for each integer \(r\ge n\).

**Theorem.** The exact universal threshold is
\[\boxed{\rho(4,4)=4}.\]
Every genus-four curve over \(\mathbb F_4\) has a closed point of every degree at least four. The smooth projective curve \(C\) with affine equation
\[y^2+y=x^9+\omega\]
has genus four but no closed point of degree three: \(B_3(C)=0\). It has zeta numerator
\[P_C(T)=(1-2T)^4(1+2T+4T^2)^2,\]
and \(B_1(C)=1\), \(B_2(C)=4\), \(B_3(C)=0\), and \(B_4(C)=54\). These are exact closed-point counts, not numerical approximations.

## Assumptions and scope
The ground field has characteristic two and exactly four elements. The expression \(y^2+y=x^9+\omega\) denotes the smooth projective model of the displayed affine curve. The genus is the geometric genus. Closed-point degrees are measured over \(\mathbb F_4\), not over \(\mathbb F_2\). The theorem quantifies over **all** smooth, projective, geometrically integral genus-four curves over \(\mathbb F_4\). The index \(r\) is an arbitrary positive integer; no bound on \(r\) is assumed.

## Proof

### The explicit missing-degree-three example
Since the polynomial \(x^9+\omega\) has a unique pole of odd order nine at infinity, the standard Artin–Schreier genus formula gives \(g(C)=(9-1)/2=4\). The affine equation is smooth because its partial derivative with respect to \(y\) equals one; its Artin–Schreier function has pole order not divisible by two, so the quadratic function-field extension is geometrically integral. There is exactly one point above infinity, and it is rational over \(\mathbb F_4\).

For each \(x\in\mathbb F_{64}\), \(x^9\in\mathbb F_8\): if \(x\ne0\), then \(x^{63}=1\), so \((x^9)^8=x^{72}=x^9\); the assertion also holds at zero. The absolute trace \(\operatorname{Tr}_{\mathbb F_{64}/\mathbb F_2}(x^9)\) vanishes because \(x^9\) lies in \(\mathbb F_8\), and the degree of \(\mathbb F_{64}/\mathbb F_8\) is two. In contrast, \(\omega\in\mathbb F_4\) has absolute trace one from \(\mathbb F_{64}\), because
\[\operatorname{Tr}_{\mathbb F_{64}/\mathbb F_2}(\omega)
=3\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}(\omega)=1\]
in characteristic two. Therefore every value \(x^9+\omega\) has absolute trace one. The image of the Artin–Schreier map \(y\mapsto y^2+y\) on \(\mathbb F_{64}\) consists precisely of the trace-zero elements. The affine curve has no \(\mathbb F_{64}\)-rational points, while its single rational point at infinity survives. Hence
\[N_3(C)=\#C(\mathbb F_{64})=1.\]
The identical trace argument over \(\mathbb F_4\) shows \(N_1(C)=1\): indeed every ninth power in \(\mathbb F_4\) belongs to \(\mathbb F_2\), and \(\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}(\omega)=1\). The relation \(N_3=B_1+3B_3\), combined with \(N_1=B_1\), gives \(B_3(C)=0\). Thus no universal threshold \(n\le3\) is possible.

### Existence of every degree at least four for every genus-four curve
Let \(X/\mathbb F_4\) be any smooth projective geometrically integral genus-four curve. Put \(N_r=\#X(\mathbb F_{4^r})\). The Weil bounds give, for all \(r\ge1\),
\[4^r+1-8\cdot2^r\le N_r\le4^r+1+8\cdot2^r.\]
Fix \(r\ge4\) and put \(U=2^r\ge16\). Each proper positive divisor \(d\mid r\) is at most \(r/2\), and there are at most \(r/2\) such divisors. Consequently,
\[\sum_{\substack{d\mid r\\d<r}}N_d
\le\frac r2(U+1+8\sqrt U)
\le\frac{49r}{32}U.\]
The last inequality uses \(1\le U/16\) and \(8\sqrt U\le2U\) for \(U\ge16\). But
\[N_r\ge U^2+1-8U.\]
For every integer \(r\ge4\), one has \(2^r-8>49r/32\): at \(r=4\) this reads \(8>49/8\), and its left-minus-right difference increases strictly with \(r\). Therefore
\[N_r>\sum_{\substack{d\mid r\\d<r}}N_d.\]
Every rational point over \(\mathbb F_{4^r}\) belongs to a unique closed point whose degree divides \(r\), so \(N_r=\sum_{d\mid r}dB_d\). In particular, since \(dB_d\le N_d\) for each \(d\), the strict inequality implies
\[rB_r=N_r-\sum_{\substack{d\mid r\\d<r}}dB_d>0.\]
Thus \(B_r>0\) for all \(r\ge4\) on every genus-four curve. Combined with the explicit missing degree three above, this proves \(\rho(4,4)=4\).

### Forced zeta numerator and the first four closed-point counts
For \(C\), \(N_3=1\) attains equality in the genus-four Weil lower bound \(4^3+1-8\cdot4^{3/2}=1\). Let \(\alpha_1,\ldots,\alpha_8\) be its Frobenius eigenvalues, each of complex modulus two. Since \(N_3=65-\sum_i\alpha_i^3=1\), one has \(\sum_i\alpha_i^3=64\). Equality in the triangle inequality forces \(\alpha_i^3=8\) for all \(i\). The eigenvalues are therefore among \(2,2\zeta,2\zeta^2\), where \(\zeta\) is a primitive cubic root of unity. Conjugate roots have the same multiplicity. If the multiplicities are \(m_0,m,m\), then \(m_0+2m=8\), and \(N_1=1\) implies \(2(m_0-m)=4\). Thus \(m_0=4\) and \(m=2\), which yields
\[P_C(T)=\prod_{i=1}^{8}(1-\alpha_iT)=(1-2T)^4(1+2T+4T^2)^2.\]
Taking power sums gives \((N_1,N_2,N_3,N_4)=(1,9,1,225)\). Applying \(N_r=\sum_{d\mid r}dB_d\) gives \((B_1,B_2,B_3,B_4)=(1,4,0,54)\), as claimed.

## Verification
The standalone program `verify_fields.py` implements the three fields \(\mathbb F_4\), \(\mathbb F_{16}\), and \(\mathbb F_{64}\) independently as polynomial quotients of \(\mathbb F_2[t]\), enumerates affine solutions of the equation, and confirms the point counts \((1,9,1)\) after adding the point at infinity. It also checks the \(x^9\)-trace identity for all 64 field elements. The separately implemented `verify_closed_points.py` reconstructs the Weil polynomial, the four small closed-point counts, and sample instances of the strict universal inequality. Run `python3 verify_fields.py` and `python3 verify_closed_points.py` in the directory containing the two files. Both ran successfully. The algebraic induction and Weil bounds in the proof—not these finite tests—certify all \(r\ge4\).

## Relationship to prior work
Aubry, Herbaut, and Monaldi initiated the study of the exact universal closed-point threshold \(\rho(q,g)\), obtaining sharp genus-at-most-three results and general bounds. Their preprint first appeared in October 2023. A September 2024 survey of diophantine stability records admissible genus-four parameter cases without asserting that this characteristic-two genus-four example has been constructed. A public candidate-polynomial table lists the exact reciprocal Weil polynomial \((t-2)^4(t^2+2t+4)^2\) for the extension \(\mathbb F_{64}/\mathbb F_4\) with one rational point, but explicitly describes the genus-four entries outside the smallest base field as *candidate* Weil polynomials. Thus the polynomial is **not newly proposed here**. The contribution established here is its explicit realization by a smooth genus-four curve, together with the exact universal threshold. Older unindexed realizations or equivalent descriptions remain a historical-priority risk.

## Limitations
The theorem concerns the particular pair of field size and genus, \(q=4\) and \(g=4\); it provides no complete classification of genus-four curves, no uniqueness or isomorphism classification of the witness, and no formula for \(\rho(q,g)\) at other parameters. It does not establish that the displayed equation or its zeta-polynomial candidate were previously unknown; an older equivalent explicit example could eliminate the claimed novelty. All assertions here are mathematical deductions reviewed within the present work; independent mathematical audit and publication-priority certification have not been performed.

## References
1. Yves Aubry, Fabien Herbaut, and Julien Monaldi, *Closed points on curves over finite fields*, arXiv:2310.11218, first public 2023-10-17. https://arxiv.org/abs/2310.11218
2. Francesc Bars et al., *Diophantine stability for curves over finite fields*, arXiv:2409.07086, first public 2024-09-11. https://arxiv.org/abs/2409.07086
3. Joan-Carles Lario, *Curves over finite fields with Diophantine Stability*, public genus-four candidate tables. https://web.mat.upc.edu/joan.carles.lario/DS_2024.html
