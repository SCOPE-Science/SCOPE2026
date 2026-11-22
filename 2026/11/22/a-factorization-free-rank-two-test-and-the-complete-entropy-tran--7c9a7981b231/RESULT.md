# A factorization-free rank-two test and the complete entropy–transitivity census of binary two-channel cellular automata

## Finding

Let \(p\) be prime and let \(R=\mathbb F_p[z,z^{-1}]\). For a nonzero matrix \(A\in M_2(R)\), let \(L\) and \(U\) be the smallest and largest exponents of \(z\) occurring in any nonzero entry. On \((\mathbb F_p^2)^{\mathbb Z}\) consider the linear cellular automaton whose Laurent matrix is \(A\). It is **strongly transitive** if and only if

1. \(\det A\ne0\),
2. \(\det A\) is not a Laurent unit (a nonzero monomial), and
3. \(\det(A-cz^jI)\ne0\) as a Laurent polynomial for every \(c\in\mathbb F_p^\times\) and every integer \(L\le j\le U\).

These are finitely many determinant identities, requiring no factorization of the characteristic polynomial. The zero matrix is not strongly transitive.

For the complete nearest-neighbor two-channel binary family
\[
 (F_{B,C}x)_i=Bx_i+Cx_{i+1},\qquad B,C\in M_2(\mathbb F_2),\quad i\in\mathbb Z,
\]
there are precisely \(256\) ordered local rules. They split jointly by dynamical topological entropy and strong transitivity as follows:

| Temporal topological entropy | Not strongly transitive | Strongly transitive | Total |
| --- | ---: | ---: | ---: |
| \(0\) | 40 | 0 | 40 |
| \(\log 2\) | 102 | 18 | 120 |
| \(2\log 2\) | 42 | 54 | 96 |
| Total | 184 | 72 | 256 |

Under simultaneous onsite linear changes of basis \((B,C)\mapsto(PBP^{-1},PCP^{-1})\), \(P\in\mathrm{GL}_2(\mathbb F_2)\), the same family has exactly \(56\) basis-change orbits. The respective numbers of orbits in the five nonempty cells of the table are \(12,17,3,10,14\) in row-major order. Their orbit-size distribution is \(4\) of size \(1\), \(6\) of size \(2\), \(12\) of size \(3\), and \(34\) of size \(6\). This is a classification under onsite linear relabeling, **not** a claim of complete topological conjugacy classification.

## Assumptions and scope

Strong transitivity means that for every nonempty open set \(V\) of the bilateral full shift, \(\bigcup_{n\ge0}F^n(V)\) equals the entire full shift. All spatial sites are indexed by \(\mathbb Z\); all matrices are over the indicated finite field; addition is field addition. Entropy refers to the **time evolution** \(F\), not the spatial entropy of a one-step image shift. The support bounds \(L,U\) are taken over all four entries together, disregarding zero coefficients. If a different convention represents spatial shift by \(z^{-1}\), replace \(z\) by \(z^{-1}\); the criterion and entropy values are unchanged.

For the binary census, matrices \(B,C\) are individually arbitrary, including singular and zero matrices. Each ordered pair is counted once; no quotient by spatial translations or reversal is taken. The basis-change orbit count applies only to the simultaneous action of the six onsite invertible binary matrices.

## Proof

**1. A finite root test in rank two.** Set \(K=\mathbb F_p(z)\), \(\tau=\operatorname{tr}A\), and \(\Delta=\det A\). Then \(\chi_A(t)=t^2-\tau t+\Delta\). The published strong-transitivity characterization for linear group cellular automata [2, Theorem 6] states that strong transitivity is equivalent to \(\Delta\ne0\) and the absence of a monic irreducible factor of \(\chi_A\) in \(K[t]\) whose constant term is a unit of \(R\).

If \(\chi_A\) itself is irreducible, this obstruction exists exactly when \(\Delta\) is a unit. If it is reducible, each irreducible factor is linear. A monic linear factor with a unit constant term has the form \(t-cz^j\) for some \(c\in\mathbb F_p^\times\) and integer \(j\). It divides \(\chi_A\) exactly when \(\chi_A(cz^j)=\det(cz^jI-A)=0\). It remains to bound \(j\) without polynomial factorization.

Write \(A=z^L H\), where \(H\in M_2(\mathbb F_p[z])\), each entry of \(H\) has degree at most \(r=U-L\), and at least one entry has a nonzero constant term. If \(cz^j\) is an eigenvalue of \(A\), then \(cz^{j-L}\) is an eigenvalue of \(H\). This belongs to \(K\) and is integral over \(\mathbb F_p[z]\), being a root of the monic characteristic polynomial of \(H\). The polynomial ring is integrally closed, so \(cz^{j-L}\in\mathbb F_p[z]\); hence \(j\ge L\). If \(s=j-L>r\), then in the equation \((cz^s)^2-\operatorname{tr}(H)cz^s+\det H=0\), the first term has degree \(2s\), strictly larger than the degrees (at most \(r+s\) and \(2r\)) of the other terms. This is impossible. Thus \(j\le U\). The three displayed tests are therefore necessary and sufficient. This deduction is a rank-two specialization of the published spectral criterion, not a replacement for its general proof.

**2. The nearest-neighbor entropy test.** Work over \(\mathbb F_2\), and write \(A=B+zC\), \(\tau=\tau_0+\tau_1z\), \(\Delta=d_0+d_1z+d_2z^2\). The published one-dimensional group-cellular-automaton entropy formula [1, Theorem 4] is the width, including exponent zero, of the Laurent supports of the characteristic-polynomial coefficients, times \(\log2\). Here all exponents lie between zero and two. Thus the entropy is \(e\log2\), where \(e=2\) if \(d_2=1\); otherwise \(e=1\) if \(d_1=1\) or \(\tau_1=1\); otherwise \(e=0\).

By part 1, strong transitivity is equivalent to \(\Delta\notin\{0,1,z,z^2\}\) together with the two nonzero polynomial tests
\[
 1+\tau+\Delta\ne0,\qquad z^2+z\tau+\Delta\ne0.
\]
These are exact polynomial identities, not evaluations at a numerical value of \(z\).

**3. Full exact enumeration.** Write
\[
 B=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
 C=\begin{pmatrix}e&f\\g&h\end{pmatrix},\qquad a,b,c,d,e,f,g,h\in\mathbb F_2.
\]
Then
\[
 \tau_0=a+d,\quad\tau_1=e+h,\quad
 d_0=ad+bc,\quad d_1=ah+de+bg+cf,\quad d_2=eh+fg.
\]
All additions in these five identities are over \(\mathbb F_2\). Holding \(\tau_0,\tau_1\) fixed leaves six independent binary variables, so each of the four rows below sums to \(64\). Exhausting these six variables yields this complete determinant-distribution table (column heading denotes \(\Delta\)):

| \(\tau\) | \(0\) | \(1\) | \(z\) | \(1+z\) | \(z^2\) | \(1+z^2\) | \(z+z^2\) | \(1+z+z^2\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(0\) | 10 | 10 | 6 | 6 | 10 | 10 | 6 | 6 |
| \(1\) | 18 | 2 | 6 | 6 | 6 | 6 | 18 | 2 |
| \(z\) | 18 | 6 | 6 | 18 | 2 | 6 | 6 | 2 |
| \(1+z\) | 18 | 6 | 18 | 6 | 6 | 2 | 6 | 2 |

There are \(64\) matrices with \(\Delta=0\), \(84\) with \(\Delta\) a nonzero monomial, \(18\) with a remaining nonunit determinant but \(\chi_A(1)=0\), and \(18\) with a remaining nonunit determinant but \(\chi_A(z)=0\). These four exclusion categories are disjoint: the two possible root identities simultaneously would force \(\tau=1+z\) and \(\Delta=z\), already a monomial. Exactly \(256-64-84-18-18=72\) remain. Sorting the table by the above entropy and root tests yields the five nonempty joint cells stated in the Finding.

**4. Onsite basis-change orbits.** The six matrices of \(\mathrm{GL}_2(\mathbb F_2)\) act on pairs \((B,C)\) by simultaneous conjugation. The identity fixes all \(16^2=256\) pairs. Each nonidentity matrix has a four-element centralizer in the full matrix algebra \(M_2(\mathbb F_2)\), hence fixes \(4^2=16\) pairs. Burnside's formula gives \((256+5\cdot16)/6=56\) orbits. Every element of each orbit has the same characteristic polynomial and strong-transitivity status. Exact traversal of the six-element action partitions these orbits by the five joint cells, and gives the sizes and counts stated above. A fully reproducible independent second coefficient enumerator is supplied alongside the orbit enumerator.

## Verification

The two standalone Python 3 standard-library scripts `check_polynomial.py` and `check_coefficients.py` both exhaust all \(2^8=256\) ordered rules by different representations: bit-polynomial multiplication versus direct five-coefficient formulas. Both assert the complete joint entropy/strong-transitivity table. The first also exhausts and checks all simultaneous basis-change orbits; the second asserts each of the \(32\) entries of the displayed characteristic-polynomial multiplicity table and each disjoint exclusion population. Both complete without third-party packages. To reproduce, run `python3 check_polynomial.py` and `python3 check_coefficients.py` from the directory containing these files.

The rank-two theorem is an infinite-lattice statement proved algebraically in part 1 using the cited characterization. The exhaustive programs certify only the finite, precisely \(256\)-case census; they do not establish the infinite-lattice characterization by simulation.

## Relationship to prior work

The strong-transitivity spectral characterization and its group-theoretic assumptions are in [2]; the group entropy formula, including the degree-width normalization, is in [1]. The factorization-free rank-two reduction is an explicit specialization of [2]. Earlier work [3] establishes qualitative strong-transitivity stability under translations and iterations for additive cellular automata. Kari's multiple-state-variable work [4] studies determinants and injectivity/surjectivity, but is not used to assert a classification of joint entropy and strong transitivity. None of the full texts inspected for [1]–[3] tabulates this natural complete binary two-channel nearest-neighbor family or its simultaneous basis-change orbit distribution. The originality claimed here is restricted to that **evaluated joint census and orbit refinement**, rather than to the general published algebraic criteria.

## Limitations

This is an exact binary two-channel local-rule classification, not an enumeration of all cellular automata on four symbols, not a classification of all dynamical conjugacies, and not a claim of a factorization-free decision test in arbitrary matrix rank. The first criterion is valid for any prime field and any finite Laurent stencil, but its proof uses the published strong-transitivity characterization. Searches of indexed literature cannot rule out unindexed earlier numerical tables or theses. There has been no independent mathematical audit.

## References

[1] N. Castronuovo, A. Dennunzio, J. Kari, L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746, first public 2026-11-12, https://arxiv.org/abs/2611.16746 .

[2] N. Castronuovo, A. Dennunzio, L. Margara, *Strong Transitivity of Group Cellular Automata: Characterization and Decidability*, arXiv:2611.22365, first public 2026-11-17, https://arxiv.org/abs/2611.22365 .

[3] A. Dennunzio, E. Formenti, D. Grinberg, L. Margara, *Additive Cellular Automata Over Finite Abelian Groups: Topological and Measure Theoretic Properties*, MFCS 2019, DOI 10.4230/LIPIcs.MFCS.2019.68, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2019.68 .

[4] J. Kari, *Linear Cellular Automata with Multiple State Variables*, STACS 2000, DOI 10.1007/3-540-46541-3_9 .
