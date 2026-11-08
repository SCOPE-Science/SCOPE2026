# Complete palindrome-pair length spectrum of the period-doubling word

## Finding
Let \(\mathbf p=1011101010111011\cdots\) be the infinite fixed point beginning with \(1\) of the substitution \(\delta(1)=10\), \(\delta(0)=11\). Call a finite word a *palindrome pair* when it is the concatenation of two palindromes, either of which may be empty. Then, for **every integer \(n\geq1\)**,
\[
\boxed{\text{Every length-}n\text{ factor of }\mathbf p\text{ is a palindrome pair}\quad\Longleftrightarrow\quad n\in\{2^j,3\cdot2^j,5\cdot2^j:j\geq0\}.}
\]
In particular, at each length \(7\cdot2^j\), all factors are *palindromic periodicities* in the sense of Fici--Shallit--Simpson, but at least one is **not** itself a palindrome pair. This separates two distinct palindrome-based notions at infinitely many sharp dyadic lengths.

## Assumptions and scope
Words are finite, linear, labeled binary strings; factors are contiguous factors at any nonnegative starting position of the one-sided infinite fixed point. A word \(w\) is a palindrome when \(w=w^R\), and a palindrome pair when \(w=uv\) for possibly empty palindromes \(u,v\). A palindromic periodicity is a word that is a prefix of \((uv)^\omega\) for a palindrome pair \(uv\) whose length does not exceed the given word's length. Every palindrome pair is a palindromic periodicity, but the converse can fail. No statement about arbitrary binary infinite words is claimed.

## Proof
**1. Circular symmetry criterion.** A nonempty finite word \(w\) is a palindrome pair if and only if its reversal \(w^R\) is a cyclic rotation (conjugate) of \(w\). In the forward direction, \((uv)^R=vu\) for palindromic \(u,v\). In the reverse direction, equality of a circular word with a reflection gives two opposite cut points along the reflection axis; the two intervening linear arcs, cut at the corresponding letter/gap boundaries, are palindromes. This standard criterion also follows from the symmetric-word lemma in Fici--Shallit--Simpson (2024, Section 2). In particular, conjugacy and injective letter relabeling preserve the palindrome-pair property.

**2. Palindrome-preserving substitution.** For every \(j\geq1\) there is a palindrome \(U_j\) of length \(2^j-1\) and a letter permutation \(\pi_j\) with
\[\delta^j(a)=U_j\pi_j(a)\qquad (a\in\{0,1\}).\]
For \(j=1\), take \(U_1=1\) and \(\pi_1(a)=1-a\). Since \(\delta^{j+1}(a)=\delta^j(1)\delta^j(1-a)\), induction gives \(U_{j+1}=U_j\pi_j(1)U_j\), a palindrome, and \(\pi_{j+1}(a)=\pi_j(1-a)\), still a permutation. For any word \(v\), reversing \(\delta^j(v)\) yields a cyclic rotation of \(\delta^j(v^R)\): each substituted block has the common palindromic prefix \(U_j\). Hence \(\delta^j\) sends palindrome pairs to palindrome pairs by Step 1.

Because \(\mathbf p=\delta^j(\mathbf p)\), an arbitrary length-\(m2^j\) factor begins \(r\) characters after an aligned block boundary, where \(0\le r<2^j\). It is the rotation by \(r\) characters of \(\delta^j(v)\) for the corresponding length-\(m\) factor \(v\) of \(\mathbf p\): the only wraparound prefix replacement uses at most \(2^j-1\) characters, which agree in all \(\delta^j(a)\). Therefore, whenever all length-\(m\) binary words are palindrome pairs, so are all length-\(m2^j\) factors of \(\mathbf p\). Every binary word of lengths \(1,3,5\) has a palindrome-pair split (a complete finite verification follows by checking respectively \(2,8,32\) possibilities). This proves sufficiency for all three displayed length families.

**3. Necessary four-family restriction.** Let \(C(n)\) denote the number of distinct length-\(n\) factors of \(\mathbf p\). The recurrence
\[C(1)=2,\quad C(2)=3,\quad C(2m)=2C(m),\quad C(2m-1)=C(m-1)+C(m)\qquad(m\geq2)\]
is also recorded with proof at OEIS A275202. It follows directly from \(\mathbf p[2i]=1\), \(\mathbf p[2i+1]=1-\mathbf p[i]\): parity-aligned factors correspond bijectively to shorter factors; their classes are disjoint since \(\mathbf p\) has no \(00\) and an aligned variable block of length at least two has a zero in its complement. Induction on the recurrence gives, when \(n=q+r\), \(q=2^k\) and \(0\le r<q\), \(k\ge1\),
\[
C(q+r)=\begin{cases}3q/2+2r,&0\le r\le q/2,\\ 2q+r,&q/2\le r<q.\end{cases}
\]
Fici--Shallit--Simpson (2024, Theorem 14; 2025, Theorem 13) give the *published exact count* \(F(n)\) of length-\(n\) factors that are palindromic periodicities:
\[
F(q+r)=\begin{cases}
3q/2,&0\le r<q/4,\\
2q,&q/4\le r<q/2,\\
3q-r,&q/2\le r<3q/4,\\
7q/2-r,&3q/4\le r<q.
\end{cases}
\]
Since palindrome pairs are palindromic periodicities, the desired universal property requires \(C(n)=F(n)\). Subtracting on the four respective intervals gives \(2r\), \(2r-q/2\), \(2r-q\), and \(2r-3q/2\). These are nonnegative and vanish only at the permitted integral breakpoints \(r\in\{0,q/4,q/2,3q/4\}\). Therefore any universal palindrome-pair length must belong to one of the four families \(2^j,3\cdot2^j,5\cdot2^j,7\cdot2^j\), with the cases \(n=1,2,3\) also checked directly. The use of \(F(n)\) here is explicitly a use of the published theorem, not a new reconstruction of its automaton certificate.

**4. Exclusion of the fourth family.** The length-seven word \(b=0111010\) occurs in \(\mathbf p\) starting at index \(1\). Its reversal \(0101110\) is not among its seven cyclic rotations, so \(b\) is not a palindrome pair. More generally, for any binary word \(v\) containing a \(1\), \(\delta(v)\) can be a palindrome pair only if \(v\) is. Indeed, \(\delta(v)^R\) is a one-symbol rotation of \(\delta(v^R)\). If \(\delta(v)\) is conjugate to its reversal, then \(\delta(v)\) is conjugate to \(\delta(v^R)\). Such a conjugacy cannot have odd offset: every even-position symbol in either doubled word is \(1\), but the odd-position symbols include a \(0\) because \(v\) contains a \(1\). The offset is therefore even and descends to a conjugacy between \(v\) and \(v^R\), proving the assertion by Step 1. All iterates \(\delta^j(b)\) contain a \(1\), occur in \(\mathbf p\), have length \(7\cdot2^j\), and are not palindrome pairs. This excludes the fourth family, completing the equivalence.

## Verification
The accompanying standalone `verify_period_doubling.py` enumerates all binary words through length \(13\) to check the circular-symmetry criterion; tests every length-\(1,3,5\) binary word under substitutions through order \(6\); tests the morphic obstruction through order \(8\); and independently compares every period-doubling factor through length \(192\) against the exact complexity recurrence and claimed length spectrum. For the finite factor sets, the program also compares stabilized factor sets extracted from prefixes of lengths \(8192\) and \(16384\). These are finite sanity checks, not a substitute for the all-length argument or the published palindromic-periodicity enumeration theorem. Run with `python3 verify_period_doubling.py`.

## Relationship to prior work
Borchert and Rampersad (2015) introduced property PP in the present setting, proved it for Sturmian words, and analyzed the Thue--Morse word. Their palindromic-prefix construction provides infinitely many PP lengths for some other infinite words, but does not identify this period-doubling spectrum. Fici, Shallit and Simpson (2024; CPM 2025) establish the exact enumerator for the *broader* class of palindromic periodicities in the period-doubling word; the present classification requires a new positive palindrome-pair lifting argument and a negative obstruction for the entire \(7\cdot2^j\) family. The ordinary period-doubling subword-complexity recurrence is established background, not a novelty claim. The result is therefore a precise distinction between factorwise palindrome-pair and factorwise palindromic-periodicity behavior.

## Limitations
The necessity argument invokes the published exact enumerator for palindromic periodicities; the provided verifier does not rederive its infinite-state-to-finite-state computation. This establishes the claimed statement conditional on the cited theorem as a previously proved mathematical result, not on finite extrapolation. The proof concerns exactly the specified binary period-doubling fixed point and ordinary contiguous factors, not nonbinary substitutions or arbitrary automatic words. Historical-priority checks cannot guarantee absence of an unindexed equivalent result. No independent audit is claimed.

## References
1. A. Borchert and N. Rampersad, *Words with many palindrome pair factors*, arXiv:1509.05396v1 (first public September 17, 2015), Electronic J. Combinatorics 22 (2015), #P4.23. https://arxiv.org/pdf/1509.05396
2. G. Fici, J. Shallit and J. Simpson, *Some Remarks on Palindromic Periodicities*, arXiv:2407.10564v2 (2024), Section 5.1, Theorem 14. https://arxiv.org/pdf/2407.10564
3. G. Fici, J. Shallit and J. Simpson, *On Palindromic Periodicities*, CPM 2025, LIPIcs 331, article 11, Theorem 13, DOI 10.4230/LIPIcs.CPM.2025.11. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2025.11
4. OEIS A275202, *Subword complexity of the period doubling sequence*, with the parity recurrence and proof, https://oeis.org/A275202 (accessed November 4, 2026 UTC).
