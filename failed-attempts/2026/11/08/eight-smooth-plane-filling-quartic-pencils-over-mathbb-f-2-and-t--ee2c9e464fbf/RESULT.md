# Eight smooth plane-filling quartic pencils over \(\mathbb F_2\) and their triple base points

## Finding
Let \(k=\mathbb F_2\), and let \(W\subset k[X,Y,Z]_4\) be the vector space of homogeneous quartics vanishing at every point of \(\mathbb P^2(k)\). Call a projective linear subspace \(\mathbb P(U)\subset\mathbb P(W)\) *entirely smooth over \(k\)* if every member indexed by \(\mathbb P(U)(k)\) is geometrically smooth; this does **not** mean all members indexed by the algebraic closure are smooth.

There are exactly \(24\) geometrically smooth nonzero forms in \(W\), and exactly \(8\) two-dimensional vector subspaces \(U\subset W\) with all three nonzero members geometrically smooth. These eight pencils are pairwise disjoint as sets of nonzero equations and partition all \(24\) smooth filling quartics. No vector subspace of dimension at least \(3\) has all nonzero members smooth. The natural \(\mathrm{PGL}_3(k)\)-action is transitive on the eight pencils, with pencil stabilizer of order \(21\); the pencils correspond canonically to the eight cyclic subgroups of order \(7\) in \(\mathrm{GL}_3(k)\).

The base scheme of **each** pencil is a degree-\(16\) complete intersection consisting of the seven reduced \(k\)-points of the plane and one closed point of degree \(3\), whose three geometric points each have curvilinear scheme length \(3\). In particular the base scheme is not reduced, although all three rational pencil members are smooth.

## Assumptions and scope
Forms are actual degree-four elements of \(k[X,Y,Z]\); since \(k^\times=\{1\}\), scalar-equivalence introduces no quotient ambiguity. All geometric smoothness statements are over an algebraic closure. A pencil is a two-dimensional **vector** subspace and contains precisely three nonzero \(k\)-forms. The base scheme is the ideal-theoretic intersection of two independent generators, not just the intersection of their rational point sets. Counts are restricted to \(k=\mathbb F_2\) and degree \(4\); the result does not classify quartics over extension fields or assert that every geometrically parametrized member of these pencils is smooth.

## Proof
**The finite classification.** The homogeneous quartic monomial basis \(X^iY^jZ^{4-i-j}\) in lexicographic \((i,j)\)-loop order \(0\le i\le4\), \(0\le j\le4-i\) has \(15\) elements. Evaluation on the seven nonzero binary coordinate triples gives seven independent linear conditions, so \(\dim_k W=8\) and \(W\) has \(255\) nonzero forms. The exhaustive verifier constructs all \(255\) from these conditions. It first checks gradients at all seven rational points; exactly \(24\) forms survive. For each survivor it computes the Jacobian ideal on each affine chart, using a Gröbner basis over \(k\), and obtains the unit ideal in all three charts. Thus those \(24\) and only those \(24\) are geometrically smooth.

For any distinct nonzero forms \(F,G\in W\), the pencil they span is entirely smooth over \(k\) precisely when all \(F,G,F+G\) belong to this set of \(24\). Enumerating all pairs gives exactly the following eight unordered triples of binary coefficient masks (bit \(m\) refers to the \(m\)-th monomial in the fixed basis, starting at zero):

\[
\begin{gathered}
(6438,10988,13258),\quad(6636,10086,16010),\\
(6922,11948,13734),\quad(7110,9004,14570),\\
(7530,11884,13062),\quad(7596,9190,15946),\\
(8006,10794,13676),\quad(8070,10154,14380).
\end{gathered}
\]

Each mask occurs in exactly one triple. Consequently the triples partition the \(24\) forms. If a larger vector subspace had all nonzero members smooth, it would contain at least two different projective lines through one form, contradicting its unique occurrence in the list. Hence dimension \(2\) is maximal.

**Projective symmetry and Singer groups.** The verifier enumerates all \(168\) matrices in \(\mathrm{GL}_3(k)=\mathrm{PGL}_3(k)\) and substitutes the corresponding coordinate transformations into every representative. The orbit of the first pencil has eight members and equals the complete list; its stabilizer has order \(21\). A separate matrix-algebra verifier gives a conceptual cross-check. By the standard Tallini--Homma--Kim representation, the space \(W\) is \(M_3(k)/kI\) via \(A\mapsto F_A\), with \(F_A\) smooth exactly when \(\det A=\det(A+I)=1\). Precisely \(48\) matrices satisfy both conditions; each has order \(7\). They lie in exactly eight distinct Singer subgroups \(H\cong C_7\), each with six nonidentity matrices. Modulo the pair \(\{A,A+I\}\), the six elements of a Singer group give three nonzero elements of the two-dimensional space \(k[H]/kI\), hence a smooth pencil. The independent verifier checks all cross-group pairs and finds no additional smooth pencils. This identifies the eight pencils with the eight Singer subgroups, compatibly with conjugation.

**The complete base scheme.** It suffices by projective transitivity to examine the first pencil. Take
\[
\begin{aligned}
F={}&X^3Z+X^2Y^2+XY^3+XZ^3+Y^2Z^2+YZ^3,\\
G={}&X^3Y+X^2Y^2+X^2Z^2+XY^2Z+XYZ^2+XZ^3+Y^3Z+Y^2Z^2.
\end{aligned}
\]
They have masks \(6438\) and \(10988\); their sum is the third member. On the chart \(Z=1\), direct reduction over \(k\) yields the *ideal equality*
\[
(F(X,Y,1),G(X,Y,1))=
(X^2+X,Y^2+Y)\ \cap\
(X+Y^8+Y^5,(Y^3+Y+1)^3).
\]
To verify equality rather than only equality of zero sets, a lexicographic Gröbner basis of the left side has leading monomials \(X^2,XY^2,Y^{11}\); its quotient therefore has dimension \(11+2=13\). Both original generators reduce to zero modulo each ideal on the right. The two right-hand ideals are comaximal: the first is the ideal of four affine \(k\)-points, and the second is supported on the irreducible cubic \(Y^3+Y+1\), with no binary roots. Their quotient lengths are \(4\) and \(9\), totaling \(13\), proving ideal equality.

At each of the three roots \(t\) of \(t^3+t+1\), the residual component has \(X=t^8+t^5\), and its geometric local algebra is \(\overline k[\varepsilon]/(\varepsilon^3)\). Thus the residual component has one degree-three closed support point, whose three geometric branches have length three each. On \(Z=0\), the restrictions at \(X=1\) have gcd \(Y(Y+1)\), while \([0:1:0]\) is also common. They are exactly the other three rational base points. At each of the seven rational base points the gradients of \(F\) and \(G\) are nonzero and distinct, so the intersections are transverse and reduced. The total scheme length is \(4+9+3=16\), agreeing with Bézout for quartics without common components. The transitive projective action transfers this complete scheme description to every pencil.

## Verification
Run \(\texttt{python3 verify_pencils.py}\) using Python and SymPy. It enumerates all \(255\) filling quartics, checks rational and geometric smoothness on all charts, identifies the eight triples, tests their symmetry orbits, and verifies the base-ideal Gröbner certificate and affine length. It finishes with \(\texttt{SMOOTH_FILLING_QUARTIC_PENCILS_PASS 255 24 8 168 21 7 13 9}\).

Run \(\texttt{python3 verify_matrix_pencils.py}\) using only the Python standard library. Independently enumerate all \(512\) matrices over \(k\), all \(168\) invertibles, the \(48\) irreducible-characteristic-polynomial matrices, and all eight Singer subgroups. This verifies both the partition into pencils and the absence of additional pencils by matrix-addition checks. It finishes with \(\texttt{MATRIX_FIELD_CHECK_PASS 512 168 48 24 8 8}\). The first verifier also recomputes geometric smoothness directly, rather than relying only on the published criterion.

## Relationship to prior work
Homma and Kim (arXiv:0903.1918, 2009) give the matrix representation of smooth minimum-degree plane-filling curves, the irreducible-characteristic-polynomial smoothness criterion, and individual automorphism groups. These results account for the known background classification of individual curves; we do **not** claim a new minimum-degree theorem or a new smoothness criterion. Asgarli and Ghioca (arXiv:2203.07169, first posted March 14, 2022) motivate the distinct problem of linear systems with every rational member smooth, including their small-field questions. Their results concern general existence and conics/quadric surfaces, not the complete constrained family of binary plane-filling quartic pencils or its nonreduced base scheme. Asgarli, Ghioca, and Reichstein (arXiv:2207.00918, Theorem 2) establish the existence of a projective **two-dimensional** smooth linear system of degree-four plane curves over \(\mathbb F_2\) in the **full** space of quartic forms; their construction is not restricted to equations vanishing at all seven rational points. Accordingly, the present maximality at projective dimension one concerns only the *plane-filling* subspace \(W\) and is neither a contradiction of nor an improvement to that unrestricted existence theorem. The present claim is the joint classification of smooth *pencils* inside this extremal filling linear system and their intersection schemes, not a classification of the individual quartics alone.

## Limitations
All enumerations are mathematically exhaustive over the specified finite spaces, but there is no statement for larger ground fields, degrees, or positive-dimensional linear systems with singular algebraically parameterized fibers. The base scheme is nonreduced at three geometric points; it must not be described as \(16\) distinct points. The relationship to the older matrix parametrization is explicit, so there remains a historical-priority risk that this exact pencil/base-scheme refinement was previously derived in a source not identified by the targeted searches. The scientific review is not an independent mathematical audit.

## References
- S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, version 1 posted March 14, 2022, Sections 1–3. https://arxiv.org/abs/2203.07169
- M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups: Supplements to a work of Tallini*, arXiv:0903.1918, version 1 posted March 11, 2009, especially Proposition 2.1, Lemma 3.1, Theorem 3.2, Theorem 5.4. https://arxiv.org/abs/0903.1918
- S. Asgarli, D. Ghioca and Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918, version 1 posted July 2, 2022, Theorem 2 and Section 3. https://arxiv.org/abs/2207.00918
- S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072, version 1 posted July 6, 2023, Introduction. https://arxiv.org/abs/2307.03072
