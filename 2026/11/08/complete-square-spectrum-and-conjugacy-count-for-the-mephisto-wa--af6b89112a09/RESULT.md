# Complete square spectrum and conjugacy count for the Mephisto Waltz word

## Finding

Let \(w\) be the one-sided binary fixed point starting in \(0\) of the substitution \(\varphi(0)=001\), \(\varphi(1)=110\). A *square of period* \(p\) is a factor \(uu\), where \(|u|=p\); a cube is \(uuu\). Positions are indexed from zero, and \(w[i,j)\) denotes the symbols in positions \(i,\ldots,j-1\). For every integer \(p\ge1\), a square of period \(p\) occurs if and only if \(p=3^k\) for some integer \(k\ge0\).

More precisely, put \(L=3^k\) and write the prospective start uniquely as \(i=qL+r\), with integers \(q\ge0\) and \(0\le r<L\). Then
\[
 w[i,i+2L)=uu\quad(|u|=L)
 \quad\Longleftrightarrow\quad
 \begin{cases}
 w(q)=w(q+1),&r=0,\\
 w(q)=w(q+1)=w(q+2),&1\le r<L.
 \end{cases}
\]
A cube of period \(L\) starts precisely when \(r=0\) and \(w(q)=w(q+1)=w(q+2)\). There is no fourth power of any integral period.

For each \(L=3^k\), the natural densities among all nonnegative starting positions of squares and cubes of period \(L\) are, respectively,
\[
 \delta_{\mathrm{sq}}(L)=\frac{L+2}{6L},\qquad
 \delta_{\mathrm{cu}}(L)=\frac{1}{6L}.
\]
At every such period exactly \(2L\) *distinct* length-\(2L\) square factors occur, and each has least period \(L\). At all other lengths there are no square factors. Equivalently, the ordinary-square factor complexity is exactly \(2\cdot3^k\) at factor length \(2\cdot3^k\), and zero at other lengths. The set of square factors is precisely the two families of cyclic conjugates of \(\varphi^k(0)\varphi^k(0)\) and \(\varphi^k(1)\varphi^k(1)\), with \(3^k\) distinct factors in each family.

## Assumptions and scope

Only the explicitly defined infinite, one-sided binary fixed point is considered. Period means an *integer* block length, and a square of period \(p\) need not initially be assumed primitive. The factor-count statement concerns distinct finite words, not their number of occurrences; the density statement counts starting indices, including overlapping occurrences, in the one-sided infinite word. Existence of a natural density is part of the conclusion. The source date identifies motivating literature and is not a claim that any result above appeared in that literature.

## Proof

**1. Differences and short runs.** Writing \(a=w(n)\), the defining substitution gives
\[
 w(3n)=w(3n+1)=a,\qquad w(3n+2)=1-a.
\]
Set \(d(n)=w(n)\mathbin{\oplus}w(n+1)\), where \(\oplus\) is binary exclusive-or. The three residue recurrences are
\[
 d(3n)=0,\qquad d(3n+1)=1,\qquad d(3n+2)=1-d(n).
\]
Consequently no four consecutive symbols of \(w\) are all equal, since every interval of three successive adjacent comparisons contains one index congruent to \(1\pmod3\), where the difference is \(1\). Every equal-letter triple, if present, starts at an index \(3n+2\), and at that index the triple occurs if and only if \(d(n)=1\).

**2. Only triadic periods can support squares.** A square of period \(p\) at \(i\) means \(w(j)=w(j+p)\) for all \(j\in[i,i+p)\). Therefore \(d(j)=d(j+p)\) for all \(j\in[i,i+p-1)\). If \(p\ge4\) and \(p\equiv1\pmod3\), this latter interval contains an index \(j\equiv0\pmod3\); the recurrence gives \(d(j)=0\) but \(d(j+p)=1\), impossible. If \(p\ge5\) and \(p\equiv2\pmod3\), choose \(j\equiv1\pmod3\) to get \(d(j)=1\) but \(d(j+p)=0\). The remaining nonmultiple \(p=2\) is impossible by examining the three starting residues: at \(i=3n\), the first and third symbols differ; at \(i=3n+1\), the first/third equality and second/fourth equality require simultaneously \(w(n+1)=w(n)\) and \(w(n+1)=1-w(n)\); at \(i=3n+2\), the second/fourth symbols differ.

If \(3\mid p\), write \(p=3h\). Among \(p\) consecutive indices in the square comparison are exactly \(h\) consecutive multiples of \(3\). Restricting the comparison \(w(j)=w(j+3h)\) to those indices \(j=3a\) gives \(h\) consecutive equalities \(w(a)=w(a+h)\). Thus \(w\) also contains a square of period \(h\). Dividing repeatedly, a possible \(p\) must be a power of \(3\).

**3. Exact starts.** Let \(A_a=\varphi^k(a)\), for \(a\in\{0,1\}\); both blocks have length \(L\), and \(A_1\) is the positionwise binary complement of \(A_0\). At multiples of \(L\), the word is tiled by blocks \(A_{w(0)},A_{w(1)},\ldots\). At start \(i=qL+r\), a square compares the final \(L-r\) symbols of one block with those of the next; because \(L-r>0\), equality forces \(w(q)=w(q+1)\). If \(r>0\), comparison of the first \(r\) symbols of the next two blocks also forces \(w(q+1)=w(q+2)\). Conversely, these exact conditions make every one of the \(L\) comparisons equal. For a cube at \(r=0\), three blocks must agree; for \(r>0\), four successive parent letters would have to agree, which is impossible by step 1. A fourth power likewise would require at least four consecutive equal parent letters. The parent triple \(000\) occurs beginning at \(q=8\), while \(111\) occurs beginning at \(q=5\), so squares of every period \(3^k\) and cubes of every such period really occur.

**4. Natural densities and exact finite-scale counts.** Define \(D(N)=\#\{0\le j<N:d(j)=1\}\). The recurrences from step 1 give
\[
 D(3N)=2N-D(N),\qquad D(3N+1)=2N-D(N),\qquad D(3N+2)=2N-D(N)+1.
\]
Writing \(E(N)=D(N)-N/2\), we have \(E(3N)=-E(N)\), \(E(3N+1)=-E(N)-1/2\), and \(E(3N+2)=-E(N)\). Induction on the ternary length yields \(|E(N)|=O(\log(N+2))\); thus \(d(j)=1\) with density \(1/2\). Adjacent equal parent pairs therefore have starting density \(1/2\). Equal parent triples are exactly at \(q=3n+2\) with \(d(n)=1\), so their starting density is \(1/6\). The residue classes modulo the fixed \(L\) in step 3 each contribute their parent density divided by \(L\), hence
\[
 \delta_{\mathrm{sq}}(L)=\frac{1/2+(L-1)/6}{L}
 =\frac{L+2}{6L},\qquad
 \delta_{\mathrm{cu}}(L)=\frac{1/6}{L}.
\]
For an optional exact finite count, let \(t\ge1\), \(Q_t=\#\{0\le q<3^t:w(q)=w(q+1)\}\), and \(T_t=\#\{0\le q<3^t:w(q)=w(q+1)=w(q+2)\}\). The same recurrences give
\[
 Q_t=\frac{3^t+(-1)^t}{2},\qquad
 T_t=\frac{3^{t-1}-(-1)^{t-1}}{2}.
\]
Among the first \(L\cdot3^t\) possible starting positions, there are exactly \(Q_t+(L-1)T_t\) squares of period \(L\) and exactly \(T_t\) cubes of period \(L\). Factors are always evaluated in the infinite word, even if they extend beyond this range of starts.

**5. Distinct square words.** Every square with period \(L\) arises from a pair of neighboring blocks equal to \(A_a\), possibly shifted through the next equal block; it is therefore a cyclic conjugate of \(A_aA_a\). Conversely, the occurrences of both equal-letter parent triples \(000\) and \(111\) ensure that every one of the \(L\) cyclic shifts of \(A_aA_a\) appears as a square for each letter \(a\). If \(A_a\) were a proper power, its length \(L=3^k\) being odd would force it to contain at least three copies of a shorter root. The occurrence of \(A_aA_aA_a\) would then contain a fourth power, contradicting step 3. Thus \(A_a\) is primitive and has \(L\) distinct cyclic conjugates. The conjugates from \(a=0\) and \(a=1\) cannot overlap: their symbol counts are complementary, and the odd length \(L\) prevents equality of their one-counts. Hence there are exactly \(2L\) distinct length-\(2L\) squares. To see that this is the *least* period, suppose a conjugate square \(AA\), where \(|A|=L\), had another period \(h<L\). For every \(0\le j<L\), its period condition gives \(A_j=A_{(j+h)\bmod L}\), because \(j+h<2L\). Thus \(A\) is invariant under cyclic shift by \(h\), hence under shift \(\gcd(h,L)\), and so is a proper power, a contradiction. This proves least period \(L\) for every conjugate square.

## Verification

The supplied standalone `check_squares.py` generates the substitution word directly and compares, for every candidate period from \(1\) through \(600\), the actual square and cube windows against the closed-form tests. It independently checks absence of fourth powers, all distinct square counts for periods \(1,3,9,27,81,243\), and the exact finite-scale count formulas. Its successful output is `VERIFY_OK periods=1..600 word_length= 19683 square_checks= 11449800 cube_checks= 11269500 fourth_checks= 11089200 distinct_counts= 6 finite_window_counts= 48`. This is finite diagnostic evidence; steps 1–5, not the computation, prove the infinite statements. To reproduce: `python3 check_squares.py` with an ordinary Python 3 interpreter.

## Relationship to prior work

Meleshko, Ochem, Shallit and Shan (first posted 20 July 2022), *Pseudoperiodic Words and a Question of Shevelev*, analyze the very same substitution word in their pseudoperiodicity treatment; their tested relation is not the equality of consecutive blocks. Shallit and Xu (2023) investigate repetition factorizations of automatic words, which neither specify all square starts nor count the distinct squares of this word. Kishi, Guo, Urbina and Bannai (2026), *On Occurrence-Preserving Morphisms*, prove a general morphism occurrence-preservation theorem and explicitly discuss this substitution, but do not present the above complete square spectrum, arithmetic occurrence criteria or the \(2L\) factor enumeration. Khodier's 2026 thesis treats the same word's known critical exponent and factor complexity; neither invariant implies the exact starting sets and densities. The classical fact that the word avoids fourth powers is also prior knowledge, not claimed as independently new here. The contribution assessed here is the *combined exact all-period/all-position square classification, asymptotic starting densities and full distinct-square spectrum*.

## Limitations

The classification concerns ordinary integral squares and cubes, not Abelian repetitions, complement repetitions, arbitrary fractional powers or two-sided variants. The result does not solve general square occurrence problems for other substitutions. Search and full-text comparison substantially reduce but cannot eliminate the possibility of an unindexed equivalent formula; 2003 textbook discussion was identified bibliographically but not compared in full from a verified lawful version. Independent mathematical validation has not been performed.

## References

1. J. Meleshko, P. Ochem, J. Shallit and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171v1, first publicly posted 2022-07-20. https://arxiv.org/abs/2207.10171
2. J. Shallit and X. Xu, *Repetition factorization of automatic sequences*, arXiv:2311.14961v1 (2023). https://arxiv.org/abs/2311.14961
3. K. Kishi, P. Guo, C. Urbina and H. Bannai, *On Occurrence-Preserving Morphisms*, CPM 2026; arXiv:2605.18034. https://arxiv.org/abs/2605.18034
4. M. Khodier, *New Methods for Analyzing the Properties of Automatic Sequences*, University of Waterloo MSc thesis (2026). https://uwspace.uwaterloo.ca/items/41caf0b3-0bdd-4dbf-a630-cf4decabc1af
5. J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), discussion of the Mephisto Waltz sequence, p. 25.
