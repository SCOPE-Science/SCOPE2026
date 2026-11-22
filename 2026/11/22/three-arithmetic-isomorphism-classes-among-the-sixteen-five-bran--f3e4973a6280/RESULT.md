# Three arithmetic isomorphism classes among the sixteen five-branch Humbert twists over \(\mathbb F_5\)

## Finding
Let \(k=\mathbb F_5\) and \(B=\mathbb F_5\subset\mathbb P^1(k)\). For every ordered four-tuple \(\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3,\epsilon_4)\in\{1,2\}^4\), let \(C_\epsilon\) be the smooth projective normalization of the multiquadratic function-field extension
\[
k(x)\left(\sqrt{\epsilon_a(x-a)/x}:a=1,2,3,4\right)/k(x).
\]
Every \(C_\epsilon\) is a geometrically integral genus-five classical Humbert curve. Among these sixteen explicitly specified, coefficient-marked covers, there are **exactly three abstract \(k\)-isomorphism classes**, with multiplicities \(1,10,5\), respectively. If \(m\in\{0,2,4\}\) indexes these classes, then
\[
L(C_\epsilon,T)=(1+2T+5T^2)^{5-m}(1-2T+5T^2)^m,
\qquad\#C_\epsilon(k)=16-4m.
\]
Thus the three point counts are \(16,8,0\), with the zero-point class represented by \(\epsilon=(2,2,2,2)\). Every one of the sixteen curves has \(56\) points over \(\mathbb F_{25}\), and its Jacobian is ordinary.

| Number \(m\) of positive-trace elliptic factors | Marked covers | \(k\)-isomorphism classes | \(\#C(k)\) | \(\#C(\mathbb F_{25})\) |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 16 | 56 |
| 2 | 10 | 1 | 8 | 56 |
| 4 | 5 | 1 | 0 | 56 |

## Assumptions and scope
All fields, equations, maps and isomorphisms are in characteristic five. The symbol \(2\) denotes a fixed nonsquare in \(\mathbb F_5\); \(\epsilon_a\in\{1,2\}\) represents one of the two square classes of \(k^\times\). The point \(\infty\) is *not* a branch point, so \(B\) is the entire set of five finite rational points. The sixteen presentations retain a marked target coordinate and four Kummer generators. The three counted isomorphism classes are **abstract curves**, not only marked Galois covers. No claim is made that the sixteen models exhaust all forms of the geometric Humbert curve, all branch configurations over other fields, or every genus-five curve over \(\mathbb F_5\).

## Proof
**1. Connected smooth genus-five covers.** Write \(r_a=(x-a)/x\). The four square classes \([\epsilon_a r_a]\) are independent in \(k(x)^\times/k(x)^{\times2}\): the valuation at \(x=a\) detects the coefficient of the \(a\)-th generator. Thus the compositum is a geometrically connected \((\mathbb Z/2)^4\)-cover of degree sixteen. The only branch points are \(0,1,2,3,4\), each with inertia order two, and no branch occurs at infinity. Tame Riemann–Hurwitz gives
\[
2g-2=16(-2)+5\cdot16(1-1/2)=8,
\]
so \(g=5\). The smooth projective normalization is therefore a classical Humbert cover (equivalently, the degree-eight intersection of three diagonal quadrics in \(\mathbb P^4\)).

**2. Exactly five elliptic character quotients.** For each \(j\in B\), define
\[
f_j(x)=\prod_{b\in B\setminus\{j\}}(x-b)=(x-j)^4-1.
\]
Let \(\chi:k^\times\to\{\pm1\}\) be the quadratic character, with \(\chi(1)=1\), \(\chi(2)=-1\), and put
\[
d_0=\prod_{a=1}^4\epsilon_a,\qquad
d_j=\prod_{\substack{a=1\\a\ne j}}^4\epsilon_a\quad(1\le j\le4),\qquad \eta_j=\chi(d_j).
\]
The index-two character corresponding to the product of the four radicals (for \(j=0\)), respectively the product of all but the \(j\)-th radical (for \(j\ne0\)), has exactly four branch points \(B\setminus\{j\}\). Multiplying its defining function by an explicit square, namely a power of \(x\), identifies the quotient with
\[
E_{\epsilon,j}:y^2=d_j f_j(x).
\]
Each is genus one and possesses a rational point (a rational root). All the other ten nontrivial characters yield genus-zero double covers (two branch points). Consequently the five genus-one character cohomology spaces exhaust the ten-dimensional first cohomology of \(C_\epsilon\); decomposition under the odd-prime-to-characteristic group action gives an isogeny over \(k\) of \(\operatorname{Jac}(C_\epsilon)\) with \(\prod_{j=0}^4 E_{\epsilon,j}\), equivalently the equality of their degree-ten Weil numerators. This use of the known Humbert–Edge Jacobian decomposition is not claimed as a discovery.

**3. Elliptic Frobenius traces.** For every \(j\), the polynomial \(f_j\) has four distinct roots in \(k\), while at the remaining finite input \(x=j\) it has value \(-1=4\), a square. The monic quartic model has two rational points over infinity. Thus \(E_{1,j}\) has \(4+2+2=8\) rational points and Frobenius trace \(-2\). Multiplying by a nonsquare yields four rational root points, no point above \(x=j\) and no rational infinity points, giving trace \(+2\). Therefore the trace on \(E_{\epsilon,j}\) is \(-2\eta_j\), and
\[
L(C_\epsilon,T)=\prod_{j=0}^4(1+2\eta_jT+5T^2).
\]
Each elliptic trace is prime to five; all five factors and hence the genus-five Jacobian are ordinary.

**4. Parity and point counts.** Let \(s_a=\chi(\epsilon_a)\), and \(p=\prod_{a=1}^4s_a\). Directly from the displayed constants,
\[
(\eta_0,\eta_1,\eta_2,\eta_3,\eta_4)
=(p,p s_1,p s_2,p s_3,p s_4),\qquad\prod_{j=0}^4\eta_j=+1.
\]
This map is bijective from the sixteen four-bit choices onto the sixteen even-parity sign vectors on five elements (its inverse is \(s_j=\eta_0\eta_j\)). Hence exactly \(\binom50=1\), \(\binom52=10\), and \(\binom54=5\) choices have \(m=0,2,4\) negative signs. The trace formula gives
\[
\#C_\epsilon(k)=5+1-\sum_{j=0}^4(-2\eta_j)=16-4m.
\]
For any elliptic trace \(t=\pm2\), its quadratic-extension trace is \(t^2-2\cdot5=-6\); hence \(\#C_\epsilon(\mathbb F_{25})=25+1-5(-6)=56\) independently of the twist.

**5. Curves of equal \(m\) are isomorphic.** The group of affine substitutions \(x\mapsto ux+v\), with \(u\in k^\times\), \(v\in k\), is the order-twenty subgroup of \(\operatorname{PGL}_2(k)\) preserving \(B\). It permutes the five branch points sharply two-transitively. Since
\[
f_j(ux+v)=u^4 f_{(j-v)/u}(x),
\]
and \(u^4\) is a square, these coordinate changes permute the five signed elliptic characters \(\eta_j\) without a new nonsquare factor. More explicitly, for each original radical \((x-a)/x\), the substituted rational function \((ux+v-a)/(ux+v)\) is a quotient of two factors \((x-b)/x\) with \(b\in B\); Kummer theory therefore supplies the required isomorphism of the complete sixteenfold covers, not just the elliptic quotients. The affine group is transitive on singleton complements and on unordered two-element subsets of \(B\), and thus on even sign subsets of sizes \(0,2,4\). All presentations with fixed \(m\) are consequently \(k\)-isomorphic. Different \(m\) have different rational-point counts, so cannot be \(k\)-isomorphic. This proves exactly three abstract isomorphism classes with the claimed frequencies.

## Verification
The included standalone `verifier.py` performs exhaustive exact arithmetic, without external dependencies. It constructs \(\mathbb F_{25}=\mathbb F_5[z]/(z^2-2)\), independently counts points in every fibre over \(\mathbb P^1(\mathbb F_5)\) and \(\mathbb P^1(\mathbb F_{25})\), and verifies all sixteen individual point counts and all five elliptic quotients. It enumerates the twenty affine transformations and their complete orbits on the sixteen even-parity character signatures. To reproduce, run `python3 verifier.py`; the program prints `HUMBERT_F5_FIVE_BRANCH_TWISTS_VERIFIED`. The infinite statements are proved by the Kummer, cohomology and group-action arguments above; the finite exhaustive computation is an independent consistency check, not a substitute for that proof.

## Relationship to prior work
Laterveer's 2022 study supplies the genus-five Humbert moduli setting, including the presentation as three diagonal quadrics and the five involutions. Auffarth–Lucchini Arteche–Rojas (2019/2020) establish the general Jacobian decomposition of Humbert–Edge curves: this paper's elliptic decomposition is **already known**. Hidalgo–Reyes-Carocca (2016) relate their geometric isomorphisms to projective transformations of the five-point branch set. The present result instead resolves a specific finite-field arithmetic question: complete isomorphism classes, twist frequencies, exact Weil numerators, and zero-point/sixteen-point dichotomy within the sixteen covers with full affine rational branch locus over \(\mathbb F_5\). Similar results for six-branch genus-seventeen curves do not imply these genus-five counts or the three abstract isomorphism classes. No claim of exhaustive global literature priority is made.

## Limitations
The classification is limited to the sixteen specified constant square-class twists of the genus-five cover over this branch set, not to all twists under the full automorphism group or arbitrary Humbert curves. The proof gives no new general decomposition theorem. Full automorphism groups, polarization-level isomorphisms of Jacobians, and extension fields beyond the provided zeta formulas are not separately classified. Literature retrieval cannot rule out an unindexed equivalent computation. Independent mathematical audit has not been performed.

## References
- R. Laterveer, *On the tautological ring of Humbert curves*, published online 14 November 2022, DOI: https://doi.org/10.1007/s00229-022-01445-4 ; open preprint https://arxiv.org/abs/2211.15291.
- R. Auffarth, G. Lucchini Arteche, A. M. Rojas, *A decomposition of the Jacobian of a Humbert–Edge curve*, https://arxiv.org/abs/1905.12690, Theorem 2.1.
- R. A. Hidalgo, S. Reyes-Carocca, *Fields of moduli of classical Humbert curves*, https://arxiv.org/abs/1609.04895.
