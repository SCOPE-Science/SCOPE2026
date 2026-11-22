# Thirteen Weil-polynomial classes and four Prym Frobenius types for cyclic quartics over \(\mathbb F_7\)

## Finding
Consider all coefficient-marked smooth plane quartics
\[
 C_{a,b}:\quad Y^4=X^3Z+aXZ^3+bZ^4,
 \qquad a,b\in\mathbb F_7,\quad b^2\ne4a^3.
\]
There are exactly \(42\) such pairs. Their genus-three Weil numerators have the form
\[
L_{C_{a,b}}(T)=(1-tT+7T^2)(1+uT^2+49T^4),
\]
with precisely \(13\) distinct pairs \((t,u)\), hence precisely \(13\) rational Jacobian isogeny types among these coefficient-marked models. The connected Prym surfaces for the double cover \(C_{a,b}\to E_{a,b}\) have exactly four \(\mathbb F_7\)-isogeny types, indexed by \(u=-14,0,7,14\), with coefficient-marked multiplicities \(2,12,16,12\), respectively.

Here is the **complete Weil spectrum**, where each row gives \((t,u)\) and the number of coefficient pairs. The complete coefficient-to-polynomial correspondence is in `SPECTRUM.json`.

| \(t\) | \(u\) | Number of smooth pairs |
|---:|---:|---:|
| -5 | 7 | 1 |
| -4 | -14 | 1 |
| -4 | 14 | 3 |
| -3 | 7 | 3 |
| -2 | 0 | 6 |
| -1 | 7 | 4 |
| 0 | 14 | 6 |
| 1 | 7 | 4 |
| 2 | 0 | 6 |
| 3 | 7 | 3 |
| 4 | -14 | 1 |
| 4 | 14 | 3 |
| 5 | 7 | 1 |

In particular, the six smooth curves with \(b=0\) all have the numerator \((1+7T^2)^3\); the other \(36\) smooth marked models realize the other twelve rational Weil types.

## Assumptions and scope
We work over \(\mathbb F_7\), with the **literal** displayed polynomial equation, without quotienting the coefficient pairs by coordinate changes. A smooth plane quartic has genus three. Its Weil numerator means the degree-six polynomial in
\[
Z(C,T)=\frac{L_C(T)}{(1-T)(1-7T)}.
\]
The involution \(Y\mapsto-Y\) has elliptic quotient \(E_{a,b}: z^2=x^3+ax+b\). The Prym denotes the connected kernel of the norm homomorphism from the Jacobian of the quartic to its elliptic quotient; it is an abelian surface over \(\mathbb F_7\). Statements about arithmetic isogeny are over \(\mathbb F_7\); no statement about geometric isomorphism or absolute simplicity is implied.

## Proof
**1. Domain and quotient.** The discriminant of \(x^3+ax+b\) is \(-4a^3-27b^2\equiv b^2-4a^3\pmod7\), so the stated condition is exactly smoothness of the branch cubic. The projective equation is nonsingular whenever the branch cubic is squarefree, including its unique point at infinity \([1:0:0]\); near infinity a local coordinate gives the tame Kummer ramification of degree four. This gives a smooth genus-three plane quartic. There are exactly seven excluded marked pairs: for every \(a\ne0\), the equation \(b^2=4a^3\) has two solutions if \(a\) is a square and none otherwise, and \((a,b)=(0,0)\) contributes one, giving \(3\cdot2+1=7\). The quotient under \(Y\mapsto-Y\) is the smooth genus-one curve \(z^2=x^3+ax+b\). The degree-two norm/pullback construction yields a base-field isogeny \(\operatorname{Jac}(C_{a,b})\sim_{\mathbb F_7}E_{a,b}\times P_{a,b}\), with \(\dim P_{a,b}=2\).

**2. The even Prym factor.** For every odd positive integer \(n\), the finite multiplicative group \(\mathbb F_{7^n}^{\times}\) has order congruent to two modulo four. Its squaring and fourth-power homomorphisms have the same kernel and the same image. Thus for each \(c\in\mathbb F_{7^n}\), the equations \(y^2=c\) and \(y^4=c\) have the same number of solutions. Both curves have one rational point at infinity, and therefore
\[
\#C_{a,b}(\mathbb F_{7^n})=\#E_{a,b}(\mathbb F_{7^n})
\qquad\text{for every odd }n\ge1.
\]
Writing \(L_C=L_E L_P\) and using Newton identities, the trace power sums of the four reciprocal roots of \(L_P\) vanish for every odd positive \(n\). In particular the first and third power sums vanish, so the first and third elementary symmetric functions vanish. The abelian-surface functional equation gives the fourth coefficient \(49\) and, via the reciprocal symmetry, the degree-one coefficient also determines the degree-three coefficient. Consequently \(L_P(T)=1+uT^2+49T^4\), for an integer \(u\). The elliptic polynomial is \(1-tT+7T^2\), with \(t=8-\#E(\mathbb F_7)=8-\#C(\mathbb F_7)\).

**3. Exact extraction of \(u\).** For a Weil numerator \(L_C(T)=\prod_{j=1}^6(1-\alpha_jT)\), the sum of squares \(\sum_j\alpha_j^2\) equals \(t^2-14-2u\). Since \(\#C(\mathbb F_{49})=50-\sum_j\alpha_j^2\), the exact formula is
\[
 u=\frac{\#C(\mathbb F_{49})-64+t^2}{2}.
\]
Thus **two exact point counts** determine the entire genus-three Weil numerator and the Prym isogeny type. This equality uses the structural evenness proved above, rather than an unsupported guess from two measurements.

**4. Exhaustive finite-field certificate.** For each of the \(42\) smooth marked pairs, compute both counts by the explicit finite sums
\[
N_k=1+\sum_{x\in\mathbb F_{7^k}}\#\{y\in\mathbb F_{7^k}:y^4=x^3+ax+b\},\qquad k\in\{1,2\}.
\]
All arithmetic is done exactly with \(\mathbb F_{49}=\mathbb F_7[i]/(i^2+1)\), where \(-1\) is nonsquare in \(\mathbb F_7\). At \(k=2\), for each nonzero right-hand side \(v\), the number of fourth roots is four exactly when \(v^{12}=1\), otherwise zero, and at \(v=0\) it is one. The standalone verifier in `verify.py` computes the count by *both* this subgroup criterion and an independently constructed frequency table of all fourth powers, and asserts their agreement for every pair. Direct application of the formulas for \(t\) and \(u\) yields the thirteen-row table, with sum of multiplicities \(42\), as well as the complete individually labelled parameter table in `SPECTRUM.json`. These finite counts are exhaustive, not random examples. Their correctness is replayable using the bundled standard-library program, which supplies its own field arithmetic without external packages.

**5. Isogeny consequences.** The displayed \((t,u)\) pairs give different Weil polynomials, hence different \(\mathbb F_7\)-isogeny classes by the finite-field isogeny classification. The four distinct \(u\) values likewise give four distinct rational Prym isogeny classes. The proof does not deduce geometric non-isomorphism from distinct marked parameters.

## Verification
Run `python3 verify.py` beside `SPECTRUM.json` with Python 3 and its standard library only. The program enumerates all seven base-field coordinates and all \(49\) quadratic-extension coordinates for each smooth marked pair; it independently recomputes fourth-power counts using exponentiation, reconstructs each full degree-six numerator by polynomial multiplication, checks the exact thirteen-type histogram and every individual parameter row, and confirms the four Prym counts. A third extension check over \(\mathbb F_{343}=\mathbb F_7[w]/(w^3+w+1)\) verifies both the odd-degree cover equality and the cubic trace prediction for every pair. It prints `VERIFY_CYCLIC4_F7_OK` on success. The general parity argument in Step 2, rather than the degree-three experiment, proves the infinite odd-degree identity.

## Relationship to prior work
Goodson [1] studies genus-three generalized Legendre cyclic quartics, including this four-branch geometry under a fractional-linear coordinate change. Its general character-sum formulas provide an independent route to individual extension-field point counts, including the split residue field of order \(49\), but do not tabulate the thirteen \(\mathbb F_7\) Weil types or the four arithmetic Prym types. Li–Mantovan–Pries–Tang [2] study the Newton polygons of the same special cyclic-cover family, including the inert-prime regime, but Newton slopes do not determine the \(\mathbb F_7\) Frobenius polynomials. A previously published parameter-level classification [4] gives this family’s Deuring-polynomial superspecial criterion and its geometric Prym properties; that work **explicitly excludes any zeta or rational Frobenius-sign assertions**. The present result concerns rational Frobenius and isogeny classes, not those prior geometric stratifications. Cavalieri–Pries [3] give nonordinary mass computations with hypotheses that do not supply this characteristic-seven Weil census. Classical zeta-function factorization and the finite-field isogeny theorem are used without novelty claims.

## Limitations
The census applies to the displayed two-coefficient equations over \(\mathbb F_7\) and counts marked equations, not all genus-three cyclic quartics, all twists, all unmarked isomorphism classes, or genus-three moduli. It does not imply that the Prym surfaces are geometrically nonisogenous; in fact their geometric superspeciality is part of prior literature. The qualitative even-Prym splitting follows from familiar Kummer and Frobenius principles; the new assessed content is the **complete characteristic-seven arithmetic type spectrum**. An equivalent pre-existing small-field table, possibly written using another genus-three Legendre or Jacobi parameter, is a residual literature-priority risk. The result is verified by a finite exhaustive certificate for \(\mathbb F_7\); it does not assert a closed-form census for every characteristic congruent to three modulo four.

## References
[1] Heidi Goodson, *Hypergeometric Properties of Genus 3 Generalized Legendre Curves*, arXiv:1705.02404, first public May 5, 2017, especially Section 5. https://arxiv.org/abs/1705.02404

[2] Wanlin Li, Elena Mantovan, Rachel Pries, Yunqing Tang, *Newton Polygons Arising from Special Families of Cyclic Covers of the Projective Line*, arXiv:1805.06914, first public May 17, 2018, Sections 5–6. https://arxiv.org/abs/1805.06914

[3] Renzo Cavalieri, Rachel Pries, *Mass Formula for Non-Ordinary Curves in One Dimensional Families*, arXiv:2308.14891, first public August 28, 2023, Section 6. https://arxiv.org/abs/2308.14891

[4] *The reduced superspecial divisor of the cyclic-quartic genus-three pencil at inert primes*, published computation, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-reduced-superspecial-divisor-of-the-cyclic-quartic-genus-thr--8c80d021706e
