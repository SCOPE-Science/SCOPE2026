# Quadratic palindrome cutoff and exact maximal-occurrence densities in generalized Mephisto words

## Finding
For every integer \(b\ge3\), consider the binary infinite fixed point \(w_b\) of the uniform substitution
\[
\mu_b(0)=0^{b-1}1,\qquad \mu_b(1)=1^{b-1}0.
\]
The base-three member is the Mephisto Waltz word. The maximum length of an ordinary (reversal) palindrome in \(w_b\) is exactly \(b^2-1\). The only palindromes of this length are
\[
P_a=(a^{b-1}\bar a)^{b-1}a^{b-1}\qquad(a\in\{0,1\}),
\]
where \(\bar a=1-a\). Their complete zero-based occurrence sets are
\[
\operatorname{Occ}_{w_b}(P_a)=\{b^2t+b(b-1): t\ge0,\ w_b(t)=1-a,\ w_b(t+1)=a\}.
\]
Each has natural starting-position density \(1/[b^2(b+1)]\), so the total density of longest-palindrome starts is \(2/[b^2(b+1)]\).

## Assumptions and scope
The integer parameter \(b\) ranges over all \(b\ge3\). Factors and start positions are zero-indexed. A palindrome is a finite contiguous binary factor fixed by reversal (not by reverse complement). Density means the limit of the number of starting indices below \(N\), divided by \(N\), as \(N\to\infty\). The case \(b=2\) is excluded: its fixed point is the Thue--Morse word, which has unbounded palindrome lengths. No claim is made about all shorter palindromes or the exact prefix palindromic-length function.

## Proof
**1. The transition word.** Define \(d(n)=w_b(n)\oplus w_b(n+1)\), with \(\oplus\) the binary exclusive-or. The fixed-point equations give, for all \(q\ge0\),
\[
d(bq+r)=\begin{cases}
0&0\le r\le b-3,\\
1&r=b-2,\\
1\oplus d(q)&r=b-1.
\end{cases}
\tag{1}
\]
Thus a \(1\) in \(d\) is possible only at residue \(b-2\) or \(b-1\) modulo \(b\), with \(d(bq+b-2)=1\) mandatory; and \(d(bq+b-1)=1\) exactly when \(d(q)=0\). Consequently \(d\) has no \(b\) consecutive zeros. Its consecutive runs of ones have length at most two, since each block contains the separator \(0^{b-2}\) with \(b-2\ge1\). In particular, \(d\) has no three consecutive ones.

If \(w_b[i..i+L-1]\) is a palindrome, the transition factor \(d[i..i+L-2]\) is itself a palindrome. For any transition palindrome \(d[i..i+N-1]\), reflection of an index \(j\) acts as \(j\mapsto C-j\), where \(C=2i+N-1\). A mandatory one at residue \(b-2\) must reflect to a one, possible only at residue \(b-2\) or \(b-1\). Since \(N\ge b^2-2\) in every use below, such a mandatory one lies inside the interval. Therefore necessarily
\[
C\equiv b-4\quad\text{or}\quad C\equiv b-3\pmod b.\tag{2}
\]
If \(C\equiv b-4\), reflection sends the optional residue \(b-1\) to the forced-zero residue \(b-3\); hence **every optional position in the interval is zero**, and equation (1) forces the corresponding consecutive parent values of \(d\) to be one. If \(C\equiv b-3\), reflection sends each optional position to a mandatory-one position; hence **all optional positions are one**, forcing the corresponding consecutive parent values of \(d\) to be zero.

**2. Sharp upper bound.** Suppose a transition palindrome has length \(N=b^2\) or \(N=b^2-1\). Every interval of \(b^2\) consecutive positions contains \(b\) optional positions. An interval of \(b^2-1\) contains \(b\) optional positions unless its starting residue \(r=i\bmod b\) is zero, in which case it contains \(b-1\). For \(N=b^2-1\) and \(r=0\), however, \(C\equiv b-2\pmod b\), incompatible with (2). Thus every feasible case contains \(b\) consecutive optional positions. Equation (2) would require \(b\) consecutive parent ones or \(b\) consecutive parent zeros in \(d\). Both are impossible: \(b\ge3\), and the preceding paragraph established maximum one-run length two and zero-run length at most \(b-1\). Hence \(d\) has no palindromic factors of lengths \(b^2-1\) or \(b^2\).

If a palindrome of \(w_b\) had length at least \(b^2\), its central factor of the same parity would have length \(b^2\) or \(b^2+1\); its transition factor would then be a forbidden palindrome of length \(b^2-1\) or \(b^2\). Therefore all palindromes of \(w_b\) have length at most \(b^2-1\).

**3. All equality cases.** Suppose a palindrome of \(w_b\) has length \(L=b^2-1\), and put \(N=L-1=b^2-2\), \(r=i\bmod b\). Now \(C\equiv 2r-3\pmod b\). The two alternatives (2) require respectively \(2r\equiv-1\pmod b\) or \(2r\equiv0\pmod b\). Every interval of length \(b^2-2\) starting at residue \(r\ge2\) has \(b\) optional positions, so the run obstruction excludes all such \(r\). The only remaining possibilities are \(r=0\), and the exceptional \(b=3,r=1\) arising from \(2r\equiv-1\pmod3\). In that exceptional case, the transition palindrome would have odd length seven with central position at residue one, which is mandatory one by (1). The exclusive-or of its seven transitions is consequently one (all symmetric pairs cancel). Its endpoint letters differ, contradicting palindromicity of the original eight-letter factor. Thus \(r=0\) necessarily.

Write \(i=bq\). For this residue, (2) has only the second alternative; the \(b-1\) optional transition positions within length \(b^2-2\) must all equal one. Equation (1) therefore says
\[
d(q)=d(q+1)=\cdots=d(q+b-2)=0,
\]
which is equivalent to \(w_b(q)=\cdots=w_b(q+b-1)=a\) for some \(a\in\{0,1\}\). Conversely, if those parent letters are equal, the substituted factor starting at \(bq\) and having length \(b^2-1\) is precisely \(P_a\), visibly a palindrome. Thus this condition characterizes every maximal occurrence, and exactly two distinct maximal palindromes exist once both parent run types are shown to occur.

Any run of \(b\) identical letters in \(w_b\) must start at the last position of a substitution block: an interval of \(b\) positions starting at any other phase contains the mandatory final-symbol flip of a block. A run of \(b\) copies of \(a\) consequently starts at \(q=bt+b-1\) precisely when \(w_b(t)=1-a\) and \(w_b(t+1)=a\). Substitution of \(i=bq\) gives the asserted occurrence formula. Both transition orientations occur already in \(\mu_b(0)\mu_b(0)\) (and, by primitivity, recur), so both \(P_0\) and \(P_1\) occur.

**4. Exact densities.** Equation (1) also shows that \(d\) is the fixed point beginning with zero of
\[
\eta_b(0)=0^{b-2}11,\qquad\eta_b(1)=0^{b-2}10.
\]
For \(b\ge3\), both images contain both letters, so this uniform substitution is primitive and the natural frequency \(D\) of ones in \(d\) exists. Counting ones under substitution yields \(bD=2(1-D)+D\), hence \(D=2/(b+1)\). The difference between the numbers of \(01\) and \(10\) transitions in every finite binary prefix is at most one (the signed sum telescopes). Therefore each oriented transition has natural frequency \(1/(b+1)\). The occurrence formula dilates transition starts by \(b^2\) and adds a fixed shift. Each maximal-palindrome type thus has density \(1/[b^2(b+1)]\). This completes the proof.

## Verification
The standalone `verify_palindrome.py` recomputes substitution prefixes for bases three through ten, checks every longest-palindrome start against the exact parent-run condition, verifies the two proposed distinct factors and checks absence of the next two possible palindrome lengths. It additionally checks the residue-count arithmetic in the proof for bases three through 250. The finite run returned `VERIFY_OK bases=3..10 palindrome_window_tests=2363532 modular_cases=1488`. The infinite theorem does **not** depend on these finite tests; it is proved by steps 1--4 above.

To reproduce: `python3 verify_palindrome.py` in a directory containing the two files. No network, third-party package or external data is required.

## Relationship to prior work
Frid--Laborde--Peltomäki (2020), arXiv:2009.02934, show that prefix palindromic-length differences are automatic when a fixed automatic word has finitely many palindromes. This applies after the bounded-palindrome theorem here is established, but it neither determines this family's cutoff nor identifies longest factors and their positions or densities. Dvořáková--Ochem--Opočenská (2023), arXiv:2311.13003, investigate a different optimization problem over infinite binary words with few distinct palindromes and give constructions based on other morphisms; their results do not state this exact family theorem. Bulgakova--Frid--Scanvic (2022), arXiv:2201.09556, compute the prefix palindromic length of the distinct Sierpinski word. The Mephisto Waltz sequence is documented as the base-three morphism \(0\mapsto001,1\mapsto110\) in OEIS A064990; this identification is not a prior classification of its maximal palindromes. The present theorem is a statement about ordinary contiguous palindromes, not scattered subsequences, pseudopalindromes, or prefix palindromic length.

## Limitations
The classification excludes base two, where there are arbitrarily long palindromes. It does not enumerate every shorter palindrome or compute the prefix palindromic-length function. The literature comparison is based on identified accessible sources and mathematical-record searches; an equivalent unindexed or inaccessible statement cannot be ruled out by unsuccessful retrieval. The argument is a mathematical proof with finite diagnostic tests, not independent external certification.

## References
- A. E. Frid, E. Laborde, J. Peltomäki, *On prefix palindromic length of automatic words*, earliest public arXiv version 2020-09-07, https://arxiv.org/abs/2009.02934.
- L. Dvořáková, P. Ochem, D. Opočenská, *Critical exponent of binary words with few distinct palindromes*, earliest public arXiv version 2023-11-21, https://arxiv.org/abs/2311.13003.
- D. V. Bulgakova, A. E. Frid, J. Scanvic, *Prefix palindromic length of the Sierpinski word*, earliest public arXiv version 2022-01-24, https://arxiv.org/abs/2201.09556.
- OEIS A064990, *Mephisto Waltz word*, https://oeis.org/A064990.
