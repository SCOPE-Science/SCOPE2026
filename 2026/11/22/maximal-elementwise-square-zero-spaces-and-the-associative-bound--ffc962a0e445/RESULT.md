# Maximal elementwise square-zero spaces and the associative boundary of the three-generator exterior algebra

## Finding

Let \(k\) be any field of characteristic different from \(2\), let \(V\) be a three-dimensional \(k\)-vector space, and put \(E=\bigwedge_k V\), with augmentation ideal \(J=\bigwedge^1V\oplus\bigwedge^2V\oplus\bigwedge^3V\). A linear subspace \(W\subset E\) is **elementwise square-zero** when \(w^2=0\) for every \(w\in W\). This does *not* mean that all products between distinct elements of \(W\) vanish. Maximal means maximal by inclusion among elementwise square-zero linear subspaces.

**Theorem.** Every maximal such space has dimension \(4\) and contains \(\bigwedge^3 V\). Write \(U=(W+J^2)/J^2\subset J/J^2\cong V\), and \(r=\dim U\). Every \(r\in\{0,1,2,3\}\) occurs, and the maximal spaces are classified by a choice of \(r\)-plane \(U\subset V\) and an alternating form \(\beta\in\bigwedge^2U^*\otimes\bigwedge^3V\). This gives the following *distinct embedded-space* census, over every odd prime power \(q\):

\[
\begin{array}{c|c|c|c}
r&\#W&\dim W^2&\text{closed under multiplication?}\\\hline
0&1&0&\text{yes}\\
1&q^2+q+1&0&\text{yes}\\
2&q(q^2+q+1)&1&\text{yes}\\
3&q^3&3&\text{no}.
\end{array}
\]

Here \(W^2\) means the linear span of all products \(uv\) for \(u,v\in W\). In particular there are exactly
\[
2(q^3+q^2+q+1)
\]
maximal elementwise square-zero linear spaces, of which exactly
\[
1+(q+1)(q^2+q+1)
\]
are associative (nonunital) subalgebras of \(E\). The four \(r\)-strata are exactly the four orbits under the full algebra automorphism group \(\operatorname{Aut}_k(E)\).

Join two *distinct* maximal spaces when their intersection has dimension \(3\). This is the point–hyperplane incidence graph of \(\mathrm{PG}(3,q)\): the two parts have \(q^3+q^2+q+1\) vertices each, and every vertex has degree \(q^2+q+1\). More precisely, different spaces with \(r\) of the same parity intersect in dimension \(2\); spaces with opposite parity intersect in dimension \(3\) when adjacent and in dimension \(1\) otherwise. In addition, each nonzero \(x\in J\) with \(x^2=0\) and \(x\notin\bigwedge^3V\) belongs to exactly \(2(q+1)\) maximal spaces, whereas every element of \(\bigwedge^3V\) belongs to all of them.

## Assumptions and scope

The exterior algebra is ordinary, associative and unital; all subspaces \(W\) under consideration lie in its augmentation ideal and need not be graded, ideals, or closed under multiplication. All structural assertions, including the orbit classification, hold over **any** field of characteristic different from two. Counts and the projective incidence statement require \(k=\mathbb F_q\) with odd prime-power \(q\). The characteristic-two case is excluded because squaring and polarization differ fundamentally. An associative space is a nonunital subalgebra; no assertion is made that the displayed list contains all maximal square-zero subalgebras when maximality is taken only among subalgebras.

## Proof

**1. Intrinsic square-zero equation.** Every \(x\in E\) has a unique expression \(x=a_0+a+b+c\), where \(a_0\in k\), \(a\in V\), \(b\in\bigwedge^2V\), and \(c\in\bigwedge^3V\). If \(x^2=0\), its scalar part forces \(a_0=0\). For \(x\in J\), the exterior multiplication rules and \(\dim V=3\) give
\[
x^2=2a\wedge b.\]
The pairing \(V\times\bigwedge^2V\to\bigwedge^3V\), \((a,b)\mapsto a\wedge b\), is perfect. Thus the quadratic form \(Q(a,b)=a\wedge b\) on the six-dimensional vector space \(V\oplus\bigwedge^2V\) is split, nonsingular, and of Witt index \(3\). Its polar form is \(B((a,b),(a',b'))=a\wedge b'+a'\wedge b\). The remaining degree-three summand is the whole radical of the square-zero condition, so every maximal \(W\) contains \(\bigwedge^3V\). Its quotient \(L=W/\bigwedge^3V\) is a maximal totally \(Q\)-singular linear subspace.

**2. Classification of all maximal singular spaces.** Let \(U\subset V\) be the projection of \(L\), with \(r=\dim U\), and put
\[
U^\perp=\{b\in\bigwedge^2 V:u\wedge b=0\text{ for all }u\in U\}.\]
Since \(L\) is totally singular, \(L\cap\bigwedge^2V\subseteq U^\perp\). Conversely, adjoining the missing elements of \(U^\perp\) preserves total singularity. Hence maximality forces \(L\cap\bigwedge^2V=U^\perp\), whose dimension is \(3-r\). We obtain \(\dim L=3\), hence \(\dim W=4\). Modulo \(U^\perp\), lifts \(u+b(u)\in L\) of \(u\in U\) define a bilinear form
\[
\beta(u,v)=u\wedge b(v)\in\bigwedge^3V.\]
The condition \(Q|_L=0\) says exactly that \(\beta\) is alternating. Conversely every pair \((U,\beta)\) defines a unique maximal totally singular \(L\) by this construction. Thus there are \({3\brack r}_q q^{\binom r2}\) spaces in each stratum. Evaluating the four Gaussian coefficients yields the displayed table and total.

**3. Associative closure and product ranks.** For any \(x=a+b+c\) and \(y=a'+b'+c'\) in the same elementwise square-zero space, polarization gives \(a\wedge b'+a'\wedge b=0\). Therefore
\[
xy=a\wedge a'\in\bigwedge^2 V,\qquad W^2=\bigwedge^2U.
\]
The inclusion \(W^2\subseteq W\) is equivalent to \(\bigwedge^2U\subseteq U^\perp\), or equivalently \(\bigwedge^3U=0\), because \(a\wedge a'\wedge a''=0\) for all \(a,a',a''\in U\) is the defining condition. This holds exactly for \(r\leq2\). Hence the closure, dimension, and count claims follow. When \(r=2\), the product is nonzero and anti-commutative, so these are associative noncommutative subalgebras in odd characteristic; \(r=0,1\) have identically zero products.

**4. Four algebra-automorphism orbits.** The radical \(J\) and its square \(J^2\) are characteristic, so \(r=\dim((W+J^2)/J^2)\) is invariant under algebra automorphisms. Linear changes of generators act transitively on the \(r\)-planes \(U\). For fixed \(U\), conjugation by \(1+a\), with \(a\in V\), maps any \(v\in V\) to \(v+2a\wedge v\), and changes \(\beta(u,v)\) by \(-2a\wedge u\wedge v\). As \(a\) varies, these changes fill \(\bigwedge^2U^*\otimes\bigwedge^3V\) for every \(r\leq3\) (trivial for \(r\leq1\), surjective by dimension and the nondegenerate volume pairing for \(r=2,3\)). Thus every stratum is one orbit and no two strata merge.

**5. The complete intersection geometry.** The two parity families \(r=0,2\) and \(r=1,3\) each have \(q^3+q^2+q+1\) spaces. Fix a volume form to identify \(\bigwedge^2V^*\) with \(V\). Identify the odd family with the points of \(\mathrm{PG}(V\oplus k)\): an \(r=1\) space with tangent line \(ka\) corresponds to the point \([a:0]\) at infinity; an \(r=3\) space with alternating form \(\gamma\) corresponds to \([a:1]\), where \(\gamma(u,v)=\operatorname{vol}(a,u,v)\). Identify the even family with projective hyperplanes: the \(r=0\) space gives the hyperplane at infinity; an \(r=2\) space \((U,\beta)\) gives the unique hyperplane whose points at infinity are \([a:0]\) with \(a\in U\), and whose affine equation is \(\operatorname{vol}(a,u_1,u_2)=\beta(u_1,u_2)\) for a chosen basis \(u_1,u_2\) of \(U\). This equation is independent of basis up to a common nonzero scalar.

The intersection of an \(r=2\) space with an \(r=1\) space has dimension \(3\) including the degree-three line precisely when the latter's tangent line lies in \(U\). The intersection with an \(r=3\) space has dimension \(3\) precisely when the latter's alternating form restricts to \(\beta\) on \(U\). The \(r=0\) space has a three-dimensional intersection precisely with the \(r=1\) spaces. These are exactly the point-in-hyperplane conditions in \(\mathrm{PG}(3,q)\). Directly from the \((U,\beta)\) description, distinct members of a single parity family meet in dimension \(2\), while nonincident opposite-parity members meet in dimension \(1\). Each projective point belongs to \(q^2+q+1\) projective hyperplanes, establishing the degree and all intersection claims.

**6. Element containment multiplicities.** There are \(q^6+q^4-q^3\) square-zero elements in \(J\): the number of solutions to \(a\wedge b=0\) is \(q^3+(q^3-1)q^2\), followed by an independent factor \(q\) for \(c\). Nonzero isotropic vectors in the split six-space lie in a single orbit of its full orthogonal isometry group. Hence they belong to the same number \(h\) of maximal totally singular three-spaces. Double-counting their incidences gives
\[
h=\frac{2(q^3+q^2+q+1)(q^4-q)}{q^6+q^4-q^3-q}=2(q+1).\]
The central line \(\bigwedge^3V\) is contained in every maximal space, proving the final assertion. The orthogonal isometry here is used only for incidence uniformity, not asserted to be an automorphism of the exterior algebra.

## Verification

The standalone standard-library checker `artifacts/check.py` constructs every predicted maximal space using finite-field linear algebra over \(\mathbb F_3\) and \(\mathbb F_5\), and independently checks square-zero equations, closure, product dimensions, and every pairwise intersection. It obtains respectively \(80\) and \(312\) spaces, with adjacency degrees \(13\) and \(31\). A separate **exhaustive** enumeration of all \({6\brack3}_3=33880\) three-dimensional subspaces of \(\mathbb F_3^6\) finds precisely the same \(80\) totally singular subspaces. In the two tested fields the numbers of unordered pairs with intersection dimensions \(3,2,1\) are respectively \((520,1560,1080)\) and \((4836,24180,19500)\). The recorded output is `artifacts/check_output.txt` and is reproduced by running `python3 artifacts/check.py` from the package root. The proof, not the finite tests, establishes the statements for all odd finite fields and all other characteristic-not-two fields.

## Relationship to prior work

The orthogonal geometry of the split six-dimensional quadratic form, including the two families of maximal generators and their classical Klein-quadric incidence, is standard prior mathematics and is **not claimed** as a new theorem. The contribution is the precise identification of *elementwise square-zero spaces in the full ungraded exterior algebra* with this geometry, together with the complete four-stratum **multiplication-closure**, embedded-space and automorphism-orbit census and its element-containment multiplicities.

Ghorpade–Patil–Pillai characterize **decomposable subspaces inside a single exterior power** (arXiv:0710.5161, especially Sections 1–2). Their object is not the inhomogeneous linear locus \(\{x\in\bigwedge V:x^2=0\}\), and their classification alone does not give the displayed multiplication-closure boundary. Domokos–Zubor (arXiv:1403.2916, Sections 2 and 7) define a *square-zero subspace* to mean a space \(D\) with \(D^2=0\), i.e. **all** pairwise products vanish; their work concerns commutative subalgebras. In contrast, the \(r=2\) spaces here are closed but have one-dimensional nonzero product, and \(r=3\) spaces have square-zero individual elements but are not subalgebras. Bavula (arXiv:math/0703352, Sections 1–2) provides the known exterior-automorphism framework used in the orbit step, not the classification here.

Related published calculations on retraction images and on homomorphisms into the three-generator exterior algebra concern images of **algebra maps** and individual labeled maps, respectively. They imply the alternating bilinear constraints for generator images but do not state the full maximal elementwise square-zero space incidence graph, the closure criterion, or the four-stratum classification. The separate rank-three finite-field census is not claimed to be an unrelated algebraic phenomenon. Broad theorems on orthogonal generators or quadratic-algebra representation schemes may contain equivalent results, and priority has not been independently established.

## Limitations

The new classification is for exactly three exterior generators and characteristic different from two; it is not extended to the higher-rank Grassmann algebras, characteristic two, or all maximal **subalgebras** with every element square-zero. The abstract Klein-quadric generator counts are pre-existing; only their particular exterior-algebra realization and the finer multiplicative boundary are evaluated here. The originality comparison is bounded and is not a proof of unique historical priority. There is no independent mathematical audit.

## References

1. S. R. Ghorpade, A. R. Patil and H. K. Pillai, *Decomposable Subspaces, Linear Sections of Grassmann Varieties, and Higher Weights of Grassmann Codes*, arXiv:0710.5161v1, first posted 2007-10-26, https://arxiv.org/abs/0710.5161.
2. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916v1, first posted 2014-03-12, https://arxiv.org/abs/1403.2916.
3. V. V. Bavula, *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra*, arXiv:math/0703352v1, first posted 2007-03-12, https://arxiv.org/abs/math/0703352.
4. V. A. Bovdi and H.-H. Leung, *Maximal commutative subalgebras of a Grassmann algebra*, arXiv:1803.03457v1, first posted 2018-03-09, https://arxiv.org/abs/1803.03457.
