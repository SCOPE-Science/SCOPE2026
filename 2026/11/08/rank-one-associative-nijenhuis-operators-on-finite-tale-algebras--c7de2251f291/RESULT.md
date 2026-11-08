# Rank-one associative Nijenhuis operators on finite étale algebras

## Finding
Let \(k=\mathbb F_q\) be any finite field, and let \(A=\prod_{i=1}^{r}\mathbb F_{q^{d_i}}\) be a nonzero finite étale commutative \(k\)-algebra (all \(d_i\ge1\)). Put \(s=\#\{i:d_i=1\}\). For each nonempty subset \(S\) of the factor indices, write \(e_S\) for the idempotent whose components are one on \(S\) and zero elsewhere; \(\varepsilon_i\) denotes projection onto the coordinate \(k\) when \(d_i=1\).

**Classification.** All nonzero \(k\)-linear associative Nijenhuis operators \(N:A\longrightarrow A\) of linear rank one are exactly the following two disjoint, uniquely parameterized families:

\[
N(a)=c\varepsilon_i(a)e_S,\quad c\in k^\times,\ i\in S,\ d_i=1;
\]
\[
N(a)=c(\varepsilon_i(a)-\varepsilon_j(a))e_S,\quad c\in k^\times,\ i\in S,\ j\notin S,\ d_i=d_j=1.
\]
In both displays \(S\ne\varnothing\) and \(c\ne0\). The second family requires two distinct split factors. Both families are valid in characteristic two, where the minus sign equals a plus sign; the roles of \(i\) and \(j\) remain distinguished by membership in \(S\).

**Exact counts.** The number of such operators is
\[
(q-1)s2^{r-1}+(q-1)s(s-1)2^{r-2},
\]
where the second term means zero when \(s<2\). Thus there are none if \(s=0\). For \(s\ge1\), the number of equivalence classes under conjugation by \(k\)-algebra automorphisms is
\[
(q-1)(2s-1)\prod_{d\ge2}(r_d+1),\qquad r_d=\#\{i:d_i=d\}.
\]
The product has finitely many nontrivial terms. For \(s=0\), the orbit count is zero. Every operator in the classification satisfies \(N^2=cN\) for its displayed nonzero scalar \(c\). In particular, no rank-one Nijenhuis operator on a finite étale algebra is nilpotent.

For the split algebra \(A=k^r\) with \(r\ge2\), the labeled count simplifies to \((q-1)r(r+1)2^{r-2}\), and the orbit count to \((q-1)(2r-1)\). For \(r=1\), these counts both equal \(q-1\).

## Assumptions and scope
An associative Nijenhuis operator is a \(k\)-linear map satisfying, for all \(x,y\in A\),
\[
N(x)N(y)=N\bigl(N(x)y+xN(y)-N(xy)\bigr).
\]
"Rank one" means rank exactly one over \(k\), excluding the zero map. Factor indices are labeled for the operator count. A conjugacy class is an orbit for \(N\mapsto gNg^{-1}\) with \(g\in\operatorname{Aut}_k(A)\); no identification by rescaling of operators is made. The coefficient field may have any prime-power order, including characteristic two.

## Proof
**1. Image normalization.** Write any nonzero rank-one linear map as \(N(x)=u\varphi(x)\) with nonzero \(u\in A\) and nonzero \(k\)-linear functional \(\varphi:A\to k\). Select \(x_0\) satisfying \(\varphi(x_0)=1\). Applying the Nijenhuis identity to \((x_0,x_0)\) shows that \(u^2=\alpha u\) for some \(\alpha\in k\). Since \(A\) is a product of fields and \(u\ne0\), \(\alpha\ne0\). Componentwise, every nonzero entry of \(u\) equals \(\alpha\). Hence \(u=\alpha e_S\) for a unique nonempty support \(S\). Absorb \(\alpha\) into the functional to normalize the map as \(N(x)=e_S\phi(x)\).

**2. Peirce reduction.** Write \(A=B\oplus C\) as algebras with \(B=e_SA\), \(C=(1-e_S)A\), and \(BC=0\). Write \(\phi=\psi+\eta\) for the restrictions to \(B\) and \(C\), extended by zero, and put \(p=\psi(e_S)=\phi(e_S)\). Direct substitution of \(x,y\in B\), \(x,y\in C\), and mixed \((x,y)\in B\times C\) into the Nijenhuis identity gives exactly
\[
\psi(x)\psi(y)=p\psi(xy)\quad(x,y\in B),\qquad
\eta(x)\eta(y)=-p\eta(xy)\quad(x,y\in C).
\]
The mixed equations are identities and impose no further restrictions.

If \(p=0\), setting \(x=y\) in these two equations forces \(\psi(x)^2=\eta(x)^2=0\) for every input; because \(k\) is a field, \(\phi=0\), a contradiction. Hence \(p\ne0\). Consequently \(\psi/p:B\to k\) is a unital nonzero \(k\)-algebra homomorphism. Either \(\eta=0\), or \(-\eta/p:C\to k\) is another unital \(k\)-algebra homomorphism: to see unitality, apply the multiplicativity equation to the identity element and some input on which the homomorphism is nonzero.

**3. Rational-factor obstruction.** Every unital \(k\)-algebra homomorphism from \(\prod_{i\in I}\mathbb F_{q^{d_i}}\) to \(k\) is evaluation at a unique degree-one factor. Indeed, its action on the orthogonal primitive idempotents chooses exactly one factor, and an injective unital map from a proper finite extension \(\mathbb F_{q^d}\) into \(k\) cannot exist. Thus \(\psi=p\varepsilon_i\) for some split \(i\in S\), and \(\eta\) is either zero or \(-p\varepsilon_j\) for split \(j\notin S\). The claimed formulas follow with \(c=p\). Conversely, these two choices satisfy the displayed equations, hence the full Nijenhuis identity. The uniqueness of \(S\), \(p\), and the two character maps makes all parameters unique.

**4. Counting and orbit classes.** In the first family, choose \(i\) among the \(s\) split factors and include it in \(S\), leaving \(r-1\) unrestricted factor memberships. This contributes \((q-1)s2^{r-1}\). In the second family choose ordered distinct split indices \(i,j\), include \(i\), exclude \(j\), and freely choose the remaining \(r-2\) memberships, contributing \((q-1)s(s-1)2^{r-2}\) for \(s\ge2\).

An automorphism of \(A\) permutes factors of each equal extension degree and may apply an internal Frobenius automorphism to each nonsplit factor. These internal actions fix all displayed maps. For each fixed \(c\), orbits in the first family are distinguished by the number \(1,\ldots,s\) of split factors in \(S\) and by the \(r_d+1\) choices of how many degree-\(d\) factors belong to \(S\), for every \(d>1\). In the second family, the number of split factors in \(S\) ranges from \(1\) through \(s-1\), with the same nonsplit choices. Conversely, within each such invariant pattern, permutations of equal-degree factors act transitively. This gives exactly \((q-1)(2s-1)\prod_{d>1}(r_d+1)\) classes. Finally \(N^2(x)=e_S\phi(e_S)\phi(x)=cN(x)\). As \(c\ne0\), \(N\) is not nilpotent.

## Verification
The standalone standard-library programs `verify.py` and `verify_orbits.py` are included. Run them with `python3 verify.py` and `python3 verify_orbits.py`. The first program independently enumerates all rank-one \(k\)-linear maps on selected products of \(k\) and its quadratic extension for \(q=2,3\), tests the Nijenhuis identity on every ordered pair of algebra basis vectors, and checks exact set equality against the two families. The second enumerates canonical parameters and the action of equal-degree factor permutations, checking the claimed orbit formula in a range of split and nonsplit examples, including repeated nonsplit degrees. Both require no third-party dependencies and finish with `VERIFY_OK` when all assertions hold. The infinite family is proved above; the computations are finite corroboration, not an extrapolation.

## Relationship to prior work
Gao, Kang, Lü, and Yu classify Nijenhuis operators on two-dimensional complex pre-Lie and three-dimensional complex associative algebras; in particular, the three-factor split complex case lies among their low-dimensional subjects. The present claim is the rank-one, finite-field, arbitrary-dimensional and finite-étale classification and enumeration, not a re-claim of low-dimensional cases. Iovanov and Sistko classify maximal subalgebras of finite-dimensional associative algebras; related diagonal and coordinate kernels can be understood through their subalgebra viewpoint, but their work does not supply the operator-compatible image classification or these labeled and automorphism-orbit counts. Sistko studies automorphism orbits of subalgebras over algebraically closed fields; the operators and finite-field orbit statistics considered here differ. The standard characterization of characters of finite products of fields is background, not claimed as new.

## Limitations
Only nonzero rank-one \(k\)-linear operators on finite étale **commutative** algebras are classified. Higher-rank Nijenhuis operators, local algebras with nilpotents, inseparable algebras, general coefficient rings, and conjugation by merely additive bijections are not addressed. The count depends on the chosen finite field and product decomposition, but not on internal choices of bases. Primary literature may contain a more general algebraic-operator theorem from which the classification follows; absence of an identified match is not a proof of publication priority. The review is not independent validation.

## References
1. X. Gao, C. Kang, J. Lü and S. Yu, *Nijenhuis operators on low dimensional pre-Lie algebras and solutions of CYBE*, arXiv:2308.12121, first submitted 2023-08-23, https://arxiv.org/abs/2308.12121 .
2. M. C. Iovanov and A. Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras*, arXiv:1705.00762, first submitted 2017-05-02, https://arxiv.org/abs/1705.00762 .
3. A. H. Sistko, *Automorphism Groups of Finite-Dimensional Algebras Acting on Subalgebra Varieties*, arXiv:1809.09760, first submitted 2018-09-25, https://arxiv.org/abs/1809.09760 .
