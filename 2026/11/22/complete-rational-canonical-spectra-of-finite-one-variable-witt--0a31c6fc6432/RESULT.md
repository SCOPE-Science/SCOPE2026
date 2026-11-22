# Complete rational-canonical spectra of finite one-variable Witt derivations
## Finding
Let \(p\ge3\) be prime, \(q=p^e\) with \(e\ge1\), and let \(A=\mathbb F_q[x]/(x^p)\). Every \(\mathbb F_q\)-derivation is \(D_f=f(x)\partial_x\), where \(f=\sum_{i=0}^{p-1}f_i x^i\). We classify the rational canonical form of **the linear operator \(D_f:A\to A\)**, not the adjoint action of \(D_f\) on the Witt Lie algebra. Exactly the following forms occur, with the indicated numbers of coefficient vectors \(f\).

**Nonzero separable characteristic polynomial.** For every \(\lambda\in\mathbb F_q^\times\), the operators with characteristic polynomial \(T^p-\lambda T\) are semisimple and have characteristic and minimal polynomial both \(T^p-\lambda T\). Their number is
\[
N(\lambda)=q^{p-2}\bigl(q-1+(p-1)\mathbf 1_{\lambda\in(\mathbb F_q^\times)^{p-1}}\bigr).
\]
Set \(d\) equal to the multiplicative order of the class of \(\lambda\) in \(\mathbb F_q^\times/(\mathbb F_q^\times)^{p-1}\), a cyclic group of order \(p-1\). Then \(T^{p-1}-\lambda\) is a product of exactly \((p-1)/d\) distinct monic irreducible polynomials, each of degree \(d\). For each divisor \(d\mid(p-1)\), the total number of derivations with this nonzero arithmetic splitting type is
\[
M_d=\frac{q-1}{p-1}\varphi(d)q^{p-2}
\begin{cases}q+p-2,&d=1,\\q-1,&d>1.\end{cases}
\]
The zero eigenvalue is simple in every such operator.

**Nilpotent characteristic polynomial.** Exactly \(q^{p-1}\) derivations are nilpotent. Among them, the \((q-1)q^{p-2}\) derivations with \(f_0\ne0\) and \(D_f^p=0\) each have one Jordan block of length \(p\). For every integer \(k\) with \(2\le k\le p-1\), exactly \((q-1)q^{p-k-1}\) derivations have \(f_0=\cdots=f_{k-1}=0\) and \(f_k\ne0\). Write \(s=k-1\), \(p-1=as+b\), \(0\le b<s\). Their nilpotent Jordan type is one block of size \(1\), together with \(b\) blocks of size \(a+1\) and \(s-b\) blocks of size \(a\). Finally the zero derivation is unique, of type \((1^p)\). The stated strata are disjoint and exhaustive. In particular, **every nonnilpotent derivation is semisimple**, while the nilpotent Jordan spectrum is controlled exactly by the first nonzero coefficient.

## Assumptions and scope
Here the rational canonical type is for the natural \(p\)-dimensional representation of \(\operatorname{Der}_{\mathbb F_q}(A)\) on \(A\); the underlying algebraic Lie bracket has no role in the definition of this linear type. The finite field may be a proper extension of its prime field. The multiplicities count all distinct coefficient tuples \((f_0,\ldots,f_{p-1})\), not similarity classes under algebra automorphisms. The formula uses Euler's totient \(\varphi(d)\). Its hypotheses are the full range \(p\ge3\), \(e\ge1\), and all \(f\in A\).

## Proof
**1. Restricted power.** The classical restricted Witt derivation identity (Evans–Fuchs) gives, for all \(f\in A\),
\[
D_f^p=\lambda(f)D_f,\qquad \lambda(f)=-\partial_x^{p-1}(f^{p-1})=[x^{p-1}]f^{p-1}.
\]
The last equality holds because \((p-1)!=-1\) in characteristic \(p\), and higher terms vanish modulo \(x^p\). The first identity is a published input, not asserted as a new theorem.

**2. Unit-coefficient strata.** Suppose \(f_0\ne0\). For \(1\le j\le p-1\), \(D_f(x^j)=j f_0x^{j-1}\) plus higher-degree terms. It follows that
\[
x^{p-1},\ D_fx^{p-1},\ \ldots,\ D_f^{p-1}x^{p-1}
\]
is a basis of \(A\): its leading-term coefficient matrix is triangular, with nonzero diagonal entries \((p-1)!/(p-1-j)!\,f_0^j\). Thus \(D_f\) is cyclic. Its minimal polynomial divides \(T^p-\lambda(f)T\) by Step 1 and has degree \(p\), so its characteristic and minimal polynomials equal \(T^p-\lambda(f)T\).

For fixed \(f_0\in\mathbb F_q^\times\) and \(f_1,\ldots,f_{p-2}\in\mathbb F_q\), the coefficient of \(f_{p-1}\) in \([x^{p-1}]f^{p-1}\) is \((p-1)f_0^{p-2}=-f_0^{p-2}\), nonzero. No higher power of \(f_{p-1}\) can contribute because its degree already equals \(p-1\). Hence as \(f_{p-1}\) varies, \(\lambda(f)\) runs through \(\mathbb F_q\) exactly once. For **each** prescribed \(\lambda\), exactly \((q-1)q^{p-2}\) derivations have \(f_0\ne0\), including \(\lambda=0\).

**3. Zero-constant coefficient but nonzero linear coefficient.** Suppose \(f_0=0\) and \(f_1\ne0\). Relative to \(1,x,\ldots,x^{p-1}\), the matrix of \(D_f\) is triangular with diagonal \(0,f_1,2f_1,\ldots,(p-1)f_1\). These are \(p\) distinct elements of \(\mathbb F_q\), so \(D_f\) is semisimple with characteristic and minimal polynomial \(T^p-f_1^{p-1}T\). For a prescribed \(\lambda\ne0\), the equation \(f_1^{p-1}=\lambda\) has \(p-1\) roots if \(\lambda\in(\mathbb F_q^\times)^{p-1}\), and none otherwise. The remaining \(p-2\) coefficients of \(f\) are arbitrary. Summing with Step 2 gives \(N(\lambda)\), and \(\lambda=0\) gets no contribution here.

**4. Arithmetic splitting type.** For \(\lambda\ne0\), the derivative of \(T^p-\lambda T\) is \(-\lambda\ne0\), so it is squarefree. Choose a root \(\alpha\) of \(T^{p-1}=\lambda\). Frobenius acts on the \(p-1\) roots \(\alpha\zeta\), \(\zeta\in\mathbb F_p^\times\), by
\[
(\alpha\zeta)^q=\alpha\zeta\lambda^{(q-1)/(p-1)}.
\]
The multiplier is a \((p-1)\)-st root of unity in \(\mathbb F_q\), with multiplicative order \(d\). Thus all Frobenius orbits have length \(d\); this establishes the factor-degree statement. For each \(d\mid p-1\), exactly \(\frac{q-1}{p-1}\varphi(d)\) values of \(\lambda\) have order \(d\). Multiplying by the value of \(N(\lambda)\) proves \(M_d\).

**5. Positive valuation.** Suppose \(f_0=f_1=0\), \(f\ne0\), and \(k=v_x(f)\in\{2,\ldots,p-1\}\). Write \(s=k-1\). The polynomial \(D_f^h(x^j)\) has first possible term of degree \(j+hs\) with leading coefficient
\[
f_k^h\prod_{i=0}^{h-1}(j+is).
\]
If \(j+hs<p\), all the integers \(j+is\) are between \(1\) and \(p-1\) and the coefficient is nonzero. If \(j+hs\ge p\), the image vanishes modulo \(x^p\). Images of distinct eligible monomials have distinct leading degrees. Consequently, for all \(h\ge1\),
\[
\operatorname{rank}(D_f^h)=\max\{p-1-hs,0\}.
\]
These power ranks describe precisely the direct sum of the one-dimensional constant kernel with the \(s\) truncated shift chains on the positive-degree basis: among \(p-1=as+b\) positive-degree positions, \(b\) chains have length \(a+1\) and \(s-b\) length \(a\). The number of coefficient tuples with valuation \(k\) is \((q-1)q^{p-k-1}\). The zero tuple gives the remaining zero operator.

**6. Exhaustiveness.** The cases \(f_0\ne0\), \(f_0=0,f_1\ne0\), \(v_x(f)\ge2\), and \(f=0\) partition \(A\). The nilpotent number is
\[
(q-1)q^{p-2}+\sum_{k=2}^{p-1}(q-1)q^{p-k-1}+1=q^{p-1}.
\]
The nonnilpotent number is \((q-1)q^{p-1}\), yielding the required \(q^p\) total. Since the polynomial in Step 4 is squarefree, there are no other nonsemisimple, nonnilpotent types.

## Verification
The accompanying standalone `verify_witt.py` uses the Python 3 standard library and writes `verify_full_output.json` beside itself. It constructs each derivation directly on the monomial basis, checks the restricted-power equation and the cyclic-basis rank when \(f_0\ne0\), checks all claimed nilpotent power ranks when \(v_x(f)\ge2\), and compares exhaustive characteristic-polynomial fibers against the formulas. The exact exhaustive configurations \((p,q)=(3,3),(3,9),(5,5)\) cover respectively \(27\), \(729\), and \(3125\) derivations; a further \(900\) seeded checks use \((p,q)=(7,7)\). Every reported check passed. The extension-field check uses the irreducible polynomial \(u^2+1\) over \(\mathbb F_3\). Finite tests do not establish the theorem in unbounded characteristic or extension degree; Steps 1–6 do.

## Relationship to prior work
Evans and Fuchs establish the scalar restricted-power relation of Step 1, including the differential formula for its scalar. Premet studies regular derivations, automorphism group orbits and invariant structures of the same truncated polynomial Lie algebra; its results anticipate some regular strata but do not state this complete finite-field natural-operator rational-canonical census with multiplicities and Frobenius splitting degrees. Yao and Chang study geometric nilpotent commuting varieties and centralizers rather than the characteristic polynomials and Jordan multiplicities of individual operators on \(A\). A published finite Witt Lie-centralizer census concerns the kernels of \(\operatorname{ad}D_f\), which differ from the present kernels of powers of \(D_f:A\to A\). Likewise published finite nilpotent commuting-tuple counts concern several pairwise commuting derivations. The new claim here is **only** the exact joint natural-representation type/count classification in Steps 2–6; the classical restricted-power identity and known regularity facts are cited as inputs.

## Limitations
This result applies to the one-variable truncated polynomial algebra at the characteristic-bound length \(p\), and only to \(p\ge3\). It does not classify operator similarity under algebra automorphisms, adjoint Jordan forms, multivariable Witt algebras, derivations of \(\mathbb F_q[x]/(x^N)\) with \(N\ne p\), or geometric scheme structures of type loci. Published literature may contain an equivalent arithmetic Jordan census not located by the searches; independent scientific priority validation is not yet available.

## References
1. T. J. Evans and D. Fuchs, *On the Restricted Lie Algebra Structure for the Witt Lie Algebra in Finite Characteristic*, arXiv:math/0111271, first publicly submitted 2001-11-27. https://arxiv.org/abs/math/0111271
2. A. Premet, *Regular Derivations of Truncated Polynomial Rings*, arXiv:1405.2426, first publicly submitted 2014-05-10; primary MSC 17B50. https://arxiv.org/abs/1405.2426
3. Y.-F. Yao and H. Chang, *Nilpotent Commuting Varieties of the Witt Algebra*, arXiv:1301.5667, first publicly submitted 2013-01-23; MSC 17B05, 17B08, 17B50. https://arxiv.org/abs/1301.5667
