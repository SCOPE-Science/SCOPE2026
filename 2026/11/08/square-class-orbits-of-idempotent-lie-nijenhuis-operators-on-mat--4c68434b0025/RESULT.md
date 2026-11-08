# Square-class orbits of idempotent Lie-Nijenhuis operators on \(\mathfrak{sl}_2(\mathbb F_q)\)

## Finding
Let \(q\) be any odd prime power, let \(k=\mathbb F_q\), and let \(\mathfrak g=\mathfrak{sl}_2(k)\). A \(k\)-linear operator \(P:\mathfrak g\to\mathfrak g\) is called an *idempotent Lie-Nijenhuis operator* if \(P^2=P\) and
\[
 [Pu,Pv]=P\bigl([Pu,v]+[u,Pv]-P[u,v]\bigr)
 \quad\text{for every }u,v\in\mathfrak g.
\]
The exact numbers of such operators of ranks \(0,1,2,3\), in that order, are
\[
\boxed{(1,\ q^2(q+1),\ q^2(q+1),\ 1).}
\]
Thus the total number is \(2+2q^2(q+1)\).

Under conjugation by \(\operatorname{Aut}_k(\mathfrak g)=\operatorname{PGL}_2(k)\), there are exactly *eight orbits*: one each for ranks zero and three, and three each for ranks one and two. In either nontrivial rank, the three orbit sizes are
\[
\boxed{q(q+1),\quad \frac{q(q^2-1)}2,\quad\frac{q(q^2-1)}2.}
\]
The orbits are distinguished by whether a canonical matrix-line discriminant is zero, a nonzero square, or a nonsquare. Over any field of characteristic different from two, the nontrivial fixed-rank parameter spaces are smooth geometrically irreducible varieties of dimension three: affine-plane bundles over \(\mathbb P^1\). Together with the isolated zero and identity operators, the reduced idempotent-Nijenhuis locus has four irreducible connected components.

## Assumptions and scope
All finite-field counting and square-class orbit statements require \(q\) odd; no claim is made in characteristic two. The geometry statement is over an arbitrary field with characteristic not two, and concerns the reduced variety. Operators are labeled linear endomorphisms, not matrices up to choice of basis; orbit equivalence refers to Lie automorphism conjugation. The trace-zero matrix basis is \(E=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\), \(H=\left(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\right)\), and \(F=\left(\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right)\).

## Proof
**(1) Nijenhuis projections are precisely Lie factorizations.** Write \(U=\operatorname{im}P\) and \(W=\ker P\), so \(\mathfrak g=U\oplus W\). On \(u,v\in U\), the Nijenhuis identity reduces to \((1-P)[u,v]=0\); on \(u,v\in W\), it reduces to \(P[u,v]=0\); on \(u\in U,v\in W\), both sides equal \(0\). Thus the identity holds exactly when \(U,W\) are Lie subalgebras. This uses neither algebraic closedness nor characteristic assumptions.

**(2) Every two-dimensional subalgebra is a unique rational Borel.** The centralizer of each nonzero element of \(\mathfrak{sl}_2(k)\) is one-dimensional when \(\operatorname{char}k\ne2\); hence a two-dimensional Lie subalgebra \(B\) is nonabelian. Its derived line is \(kZ=[B,B]\), so \([b,Z]\in kZ\) for all \(b\in B\). Write \(Z=[a,b]\) with \(a,b\in B\); cyclicity of matrix trace yields
\[
\operatorname{tr}(Z^2)=\operatorname{tr}([a,b]Z)=\operatorname{tr}(a[b,Z])=c\operatorname{tr}(a[a,b])=0
\]
for some scalar \(c\). Since \(\operatorname{tr}Z=0\), the identity \(\operatorname{tr}(Z^2)=-2\det Z\) implies \(\det Z=0\), so \(Z\) is a nonzero nilpotent matrix. Its kernel is a \(k\)-rational line in \(k^2\). Because \([B,Z]\subseteq kZ\), this kernel is \(B\)-stable. Therefore \(B\) is exactly the two-dimensional Lie subalgebra of matrices preserving that line. Conversely each rational line defines such a subalgebra. There are \(q+1\) such Borels, parameterized by \(\mathbb P^1(k)\).

**(3) Labeled rank enumeration and geometric structure.** A rank-one projection corresponds uniquely to its image line \(U\) and complementary kernel plane \(B\). Any line is a Lie subalgebra; the plane must be one of the Borels. For each \(B\), the number of lines \(U\not\subseteq B\) is \((q^2+q+1)-(q+1)=q^2\). Thus there are \(q^2(q+1)\) rank-one operators. Exchanging image and kernel, equivalently replacing \(P\) by \(1-P\), gives the same rank-two count. Only \(0\) and \(1\) occur in the extreme ranks.

For a fixed Borel \(B\), its complementary lines form the affine plane \(\mathbb P(\mathfrak g)\setminus\mathbb P(B)\). These assemble as a Zariski-locally trivial \(\mathbb A^2\)-bundle over the Borel variety \(\mathbb P^1\). This proves smoothness, geometric irreducibility, and dimension three for the rank-one stratum; rank two is isomorphic via \(P\mapsto1-P\). Ranks of idempotents are locally constant, so the reduced locus has exactly the four components claimed.

**(4) Complete automorphism-orbit count.** For odd characteristic, \(\operatorname{Aut}_k(\mathfrak g)=\operatorname{PGL}_2(k)\) acts transitively on rational Borels. Fix \(B=\langle E,H\rangle\). Every complementary line has exactly one generator
\[
X(a,b)=F+aH+bE=\begin{pmatrix}a&b\\1&-a\end{pmatrix},\qquad a,b\in k.
\]
The stabilizer of \(B\) consists of projective upper-triangular matrices, represented by \(G(t,u)=\left(\begin{smallmatrix}t&u\\0&1\end{smallmatrix}\right)\) with \(t\ne0\). Conjugate \(X(a,b)\) by \(G(t,u)\), and normalize the lower-left entry back to one. The resulting parameters satisfy
\[
a'=ta+u,\qquad b'=t^2b-2tau-u^2,\qquad (a')^2+b'=t^2(a^2+b).
\]
Choosing \(u=-ta\) sends every pair to \((0,t^2(a^2+b))\). Thus the Borel stabilizer has precisely three orbits in the affine plane: \(a^2+b=0\), nonzero square, and nonsquare. For each fixed \(a\), these fibers have respectively \(1\), \((q-1)/2\), and \((q-1)/2\) values of \(b\), hence stabilizer-orbit sizes \(q\), \(q(q-1)/2\), and \(q(q-1)/2\). Multiplication by the \(q+1\) possible Borels gives the stated \(\operatorname{PGL}_2\) orbit sizes. The rank-two orbits follow via \(1-P\). The two constant operators are fixed points. This proves the theorem.

## Verification
Run \(`python3 verify.py`\) using the standalone script supplied with this result. It enumerates all reduced-row-echelon subspaces and directly checks bracket closure, complementary decompositions, and the original Nijenhuis identity for every recovered operator for \(q=3,5\). It independently enumerates all \(3^9\) endomorphism matrices over \(\mathbb F_3\), filtering first on idempotence then directly on the Nijenhuis equations, yielding rank profile \((1,36,36,1)\). For \(q=5\) the direct complement enumeration yields \((1,150,150,1)\). In both fields the program directly computes all upper-triangular conjugation orbits and confirms their discriminant classes and orbit sizes. See \(`verification_output.txt`\) for exact replay output. These finite tests are corroboration, not a proof for arbitrary odd prime powers.

## Relationship to prior work
Liu–Sheng–Zhou–Bai, *Nijenhuis operators on n-Lie algebras*, arXiv:1601.02356v1 (first publicly posted 2016-01-11), gives the operator setting and constructions but no cited finite-field count or this square-class orbit stratification. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators*, arXiv:2410.10536v1 (2024), analyzes real and complex Lie algebras with three distinct operator eigenvalues, and remarks on equivalence of full Nijenhuis eigenbases for real/complex \(\mathfrak{sl}_2\). The projections here have repeated eigenvalues (multiplicities one and two) and are considered over finite fields; the 2024 equivalence assertion therefore does not give the three rational square-class orbits, their sizes or labeled counts. Bin Shu, arXiv:1404.1149v1, studies homogeneous Borel subalgebras of restricted modular Lie algebras (not the present operator variety). Gubarev–Kozlov, *Rota–Baxter operators on Cur(sl₂(C))*, International Electronic Journal of Algebra 33 (2023), Proposition 2.5, explicitly classifies weight-one Rota–Baxter operators on complex \(\mathfrak{sl}_2\) and gives two complex splitting-operator types. The operator \(R=-P\) is a splitting Rota–Baxter operator of weight one, so this complex classification is acknowledged as stronger prior work for algebraically closed characteristic-zero conjugacy; the new claim is its exact rational descent over every odd finite field, where the nonzero discriminant class splits into square and nonsquare orbits, and the all-odd-field counts and geometry. The classical Borel classification, and that the line discriminant is a quadratic-form invariant, are not claimed as new. The precise operator census, rational orbit splitting, and associated family of parameter varieties are the only novelty claims.

## Limitations
Only idempotent operators are classified, not arbitrary Nijenhuis operators or nonsemisimple operators. Characteristic two and non-split forms of the Lie algebra are excluded. The four components concern the reduced algebraic set; no scheme-theoretic multiplicity statement is asserted. The classification's historical originality has not been independently certified and could be subsumed by an unidentified broader account of two-subalgebra factorizations of \(\mathfrak{sl}_2\).

## References
1. J. Liu, Y. Sheng, Y. Zhou, C. Bai, *Nijenhuis operators on n-Lie algebras*, arXiv:1601.02356v1, first public 2016-01-11, https://arxiv.org/abs/1601.02356.
2. E. S. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators*, arXiv:2410.10536v1, first public 2024-10-14, https://arxiv.org/abs/2410.10536.
3. V. Gubarev, R. Kozlov, *Rota–Baxter operators on Cur(sl₂(C))*, International Electronic Journal of Algebra 33 (2023), 247–269, Proposition 2.5, DOI 10.24330/ieja.1218727, https://ieja.net/files/papers/volume-33/15-IEJA-3522.pdf.
4. B. Shu, *Generic property and conjugacy classes of homogeneous Borel subalgebras of restricted Lie algebras*, arXiv:1404.1149v1, first public 2014-04-04, https://arxiv.org/abs/1404.1149.
