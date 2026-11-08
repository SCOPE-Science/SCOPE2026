# Idempotent derivation rank spectra of model filiform Lie algebras over finite fields

## Finding
For an integer \(n\ge3\) and a finite field \(k=\mathbb F_q\), consider the \((n+1)\)-dimensional Lie algebra \(L_n(k)\) with basis \(e,v_1,\ldots,v_n\) and brackets
\[
[e,v_i]=v_{i+1}\quad(1\le i<n),\qquad[e,v_n]=[v_i,v_j]=0.
\]
The bracket is alternating and is extended by bilinearity and skew-symmetry, including in characteristic two. Let \(\mathcal P_n(q)\) be the set of \(k\)-linear derivations \(D\colon L_n(k)\to L_n(k)\) satisfying \(D^2=D\). Distinct derivations are counted as distinct linear maps, not modulo automorphisms. Define the rank enumerator
\[
R_{n,q}(z)=\sum_{D\in\mathcal P_n(q)}z^{\operatorname{rank}_k D}.
\]
If \(q\) is odd, then
\[
\boxed{R_{n,q}(z)=1+q^n z^n.}
\]
If \(q\) is even and \(n=2m\ge4\), then
\[
\boxed{R_{n,q}(z)=1+2q^{2m}z^{m+1}+q^{2m}z^{2m}.}
\]
If \(q\) is even and \(n=2m+1\ge3\), then
\[
\boxed{R_{n,q}(z)=1+q^{2m+1}z^{m+1}+q^{2m}z^{m+2}+q^{2m+1}z^{2m+1}.}
\]
Terms with identical exponents are to be combined; in particular for \(n=3\) the last two nonzero-rank contributions coincide. These formulas determine every attainable rank and its multiplicity, for all permitted \(n\) and \(q\).

In even characteristic a further structural distinction occurs. The idempotent derivation defined by \(D(e)=e\) and \(D(v_i)=(i-1)v_i\), where the integer \(i-1\) is mapped into \(k\), has nonabelian image: \(e,D(v_2)=v_2\) are in the image but \([e,v_2]=v_3\) is not. Thus the abelian-image assertion for idempotent derivations in characteristic zero does not extend to characteristic two, even for these nilpotent Lie algebras.

## Assumptions and scope
The fields are arbitrary finite fields, not only prime fields. The dimension assumption \(n\ge3\) matters: it makes the nilpotent shift below have rank at least two and excludes the three-dimensional Heisenberg exception. The counted maps are ordinary Lie derivations, not Lie algebra endomorphisms, almost-inner derivations, or matrices modulo conjugacy. The base field is held fixed when asymptotic statements in \(n\) are made.

## Proof
Write \(V=\operatorname{span}_k\{v_1,\ldots,v_n\}\) and let \(N\colon V\to V\) satisfy \(Nv_i=v_{i+1}\) for \(i<n\), and \(Nv_n=0\). Every \(k\)-linear operator \(D\) on \(L_n\) has a unique block description
\[
D(e)=ae+u,\qquad D(v)=f(v)e+Bv\quad(v\in V),
\]
where \(a\in k\), \(u\in V\), \(f\in V^*\), and \(B\in\operatorname{End}_k(V)\). Since \([V,V]=0\), the derivation identity implies
\[
f(v)Nw-f(w)Nv=0\quad\text{for all }v,w\in V.
\]
If \(f\ne0\), choose \(v\) with \(f(v)\ne0\). Then the displayed equality would force \(\operatorname{im}N\) to have dimension at most one. But \(\operatorname{rank}N=n-1\ge2\), hence \(f=0\). The remaining derivation equations reduce exactly to
\[
BN-NB=aN.
\]
Define \(H(v_i)=(i-1)v_i\) (integers are reduced in \(k\)). Then \([H,N]=N\). Because \(N\) is one regular nilpotent Jordan block, its centralizer in \(\operatorname{End}_k(V)\) consists exactly of polynomials \(p(N)\) with \(\deg p<n\): a commuting operator is uniquely determined by its value on the cyclic vector \(v_1\). Consequently every derivation has the unique form
\[
D(e)=ae+u,\qquad D|_V=B=aH+p(N),
\]
with \(a\in k\), \(u\in V\), \(p\in k[t]/(t^n)\).

The condition \(D^2=D\) is equivalent to
\[
a^2=a,\qquad B^2=B,\qquad (aI+B-I)u=0.
\]
Thus \(a=0\) or \(a=1\). If \(a=0\), the element \(B=p(N)\) is an idempotent in the local algebra \(k[t]/(t^n)\). Its only idempotents are \(0\) and \(1\): an idempotent with zero constant term is nilpotent, hence zero, and the complementary assertion handles constant term one. For \(B=0\), the vector condition gives \(u=0\), yielding the unique zero derivation. For \(B=I\), any of the \(q^n\) vectors \(u\) works, and the resulting derivation has rank \(n\).

Now suppose \(a=1\). Write
\[
B=H+cI+\sum_{i=1}^{n-1}b_iN^i.
\]
Every idempotent matrix is diagonalizable, with eigenvalues only zero or one. Since \(B\) is triangular in the natural basis, its diagonal values \(c,c+1,c+2,\ldots,c+n-1\) must all belong to \(\{0,1\}\). When \(\operatorname{char}k\ne2\), the first three values are pairwise distinct, a contradiction. Therefore \(a=1\) is possible only in characteristic two.

Assume \(\operatorname{char}k=2\). The diagonal condition gives \(c\in\{0,1\}\), and \(H^2=H\). Set \(P=\sum_{i=1}^{n-1}b_iN^i\). Using \([H,N^i]=iN^i\), the equation \(B^2=B\) becomes
\[
\sum_{i=1}^{n-1}(i+1)b_iN^i+P^2=0.
\]
In characteristic two, \(P^2=\sum_{2i<n}b_i^2N^{2i}\). Hence every odd-indexed coefficient \(b_i\) is free, while every even-indexed coefficient obeys
\[
b_{2j}=b_j^2\qquad(2j<n).
\]
This gives precisely \(q^{\lfloor n/2\rfloor}\) choices of \(B\) for each fixed \(c\in\{0,1\}\). There are no extra equations: the displayed recursion is both necessary and sufficient for \(B^2=B\).

The triangular diagonal entries of an idempotent \(B\) give its rank, because its characteristic polynomial is \(t^{n-r}(t-1)^r\) and an idempotent is semisimple. For \(n=2m\), both choices of \(c\) give \(r=m\). For \(n=2m+1\), choice \(c=0\) gives \(r=m\), and \(c=1\) gives \(r=m+1\).

The remaining vector equation for \(a=1\) is \(Bu=0\). There are exactly \(q^{n-r}\) choices of \(u\) for a given \(B\) of rank \(r\). Moreover, in the block matrix of \(D\), the image of \(e\) has nonzero \(e\)-component, so \(\operatorname{rank}D=1+r\). For \(n=2m\), each of the two choices of \(c\) therefore contributes \(q^m q^m=q^{2m}\) distinct derivations of rank \(m+1\). For \(n=2m+1\), choice \(c=0\) contributes \(q^m q^{m+1}=q^{2m+1}\) derivations of rank \(m+1\), and choice \(c=1\) contributes \(q^m q^m=q^{2m}\) derivations of rank \(m+2\). Adding the \(a=0\) cases proves every displayed rank polynomial.

For the nonabelian-image assertion, use \(a=1\), \(B=H\), \(u=0\) in characteristic two. Then \(D^2=D\) by \(H^2=H\), and the derivation condition holds because \([H,N]=N\). Both \(e\) and \(v_2\) lie in \(\operatorname{im}D\), but their bracket is \(v_3\), on which \(D\) vanishes. This proves that \(\operatorname{im}D\) is not a Lie subalgebra.

## Verification
The complete derivation identities were independently encoded as a homogeneous linear system in the \((n+1)^2\) matrix entries. The standalone `verify.py` computes a nullspace basis over each test field, enumerates every linear combination of that basis, directly checks the matrix idempotency equation, and computes each rank by elimination. It does not assume the polynomial parameterization used in the proof. Tested field orders are \(2,3,4,5\), including the nonprime field of order four. Results:

```
CHECK n=3 q=2: {0: 1, 2: 8, 3: 12}
CHECK n=4 q=2: {0: 1, 3: 32, 4: 16}
CHECK n=5 q=2: {0: 1, 3: 32, 4: 16, 5: 32}
CHECK n=3 q=3: {0: 1, 3: 27}
CHECK n=4 q=3: {0: 1, 4: 81}
CHECK n=3 q=4: {0: 1, 2: 64, 3: 80}
CHECK n=3 q=5: {0: 1, 3: 125}
VERIFY_OK
```

To reproduce, run `python verify.py` with a standard Python 3 interpreter; no external packages are required. These finite computations test the formulas but do not replace the all-\(n\), all-\(q\) proof.

## Relationship to prior work
Avetisyan's 2016 and 2018 descriptions of derivations of almost Abelian Lie algebras already provide the general linear structure from which the derivation block form can be recovered. That structure is not new here. The contribution is the exact solution of the **additional nonlinear idempotency constraint**, refined by operator rank over all finite fields, and the sharp characteristic-two obstruction to a characteristic-zero image theorem.

Bai, Gao, and Li (2015) proved that images of idempotent derivations are abelian ideals for complex finite-dimensional Lie algebras; the proof explicitly uses the hypothesis \(\operatorname{char}k=0\) to divide by two. The characteristic-two example above is outside that theorem's hypotheses. Burde, Dekimpe, and Verbeke (2019) study **almost-inner** derivations, a different property. Previously published adjoint-rank computations for filiform Lie algebras concern \(\operatorname{ad}(x)\), not all idempotent derivations. No inspected source gave the stated finite-field rank-polynomial enumeration.

## Limitations
The result concerns one fixed standard filiform, almost Abelian family and ordinary derivations. It makes no claim about all filiform Lie algebras, arbitrary nilpotent Lie algebras, or other operator identities. The asymptotic probabilities, if used, require fixed field order. The formulas are proved exactly, but a broader uninspected enumeration in Lie-algebra grading or derivation literature could affect publication priority. Independent mathematical review has not been conducted.

## References
1. Z. Avetisyan, *Jordanable almost Abelian Lie algebras*, arXiv:1811.01252, first posted 2018-11-03. https://arxiv.org/abs/1811.01252
2. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365, first posted 2016-10-17; Section 5, Proposition 13. https://arxiv.org/html/1610.05365v2
3. R. Bai, Y. Gao and Z. Li, *Lie algebras with idempotent derivations*, Mathematica Aeterna 5 (2015), 159–162, Theorems 1–3. https://www.longdom.org/articles-pdfs/lie-algebras-with-idempotent-derivations.pdf
4. D. Burde, K. Dekimpe and B. Verbeke, *Almost inner derivations of Lie algebras II*, arXiv:1905.08145, first posted 2019-05-20, Section 3. https://arxiv.org/abs/1905.08145
