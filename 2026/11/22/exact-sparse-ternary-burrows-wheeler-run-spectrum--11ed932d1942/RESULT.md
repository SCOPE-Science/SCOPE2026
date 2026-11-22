# Exact sparse-ternary Burrows–Wheeler run spectrum

## Finding
Let \(n\ge 3\) and let \(\mathcal N_n\) denote necklaces over the ordered alphabet \(0<1<2\) with composition \((n-3,1,2)\): exactly one symbol \(1\), exactly two symbols \(2\), and all remaining symbols \(0\). For a necklace \(w\), sort all its cyclic rotations lexicographically, take the last column \(B(w)\), and count its maximal **linear**, not circular, equal-symbol runs \(r(w)\). Set \(C_j(n)=|\{w\in\mathcal N_n:r(w)=j\}|\). Then the complete ordinary generating functions \(F_j(z)=\sum_{n\ge3}C_j(n)z^n\) are

\[
\begin{aligned}
F_2(z)&=z^3,\\
F_3(z)&=\frac{z^4(1-z)^2(2z^3+3z^2+4z+2)}{D(z)},\\
F_4(z)&=\frac{z^4(1-z)(3z^2+2z+1)}{D(z)},\\
F_5(z)&=\frac{z^5(1-z)(2z^3+3z^2+4z+2)}{D(z)},\\
F_6(z)&=\frac{z^6(z^3+z^2+3z+1)}{D(z)},
\end{aligned}
\qquad D(z)=(1-z)(1-z^2)(1-z^3).
\]

Every other \(F_j\) vanishes. In particular, at every length \(n\ge6\) all four values \(3,4,5,6\) occur, and \(C_6(n)/\binom{n-1}{2}\to1\). This is a genuine ternary effect: both odd and even nontrivial run counts occur, unlike the previously enumerated binary three-marker family.

## Assumptions and scope
The transform is sentinel-free, built from **all** \(n\) cyclic rotations, with the order \(0<1<2\). Necklaces are modulo rotation, not reversal or symbol relabeling. The unique occurrence of \(1\) makes every such necklace primitive and gives the unique canonical representative
\[
w(a,b,c)=1\,0^a2\,0^b2\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\quad a+b+c=n-3.
\]
Consequently \(|\mathcal N_n|=\binom{n-1}{2}\). All generating functions are formal power series over \(\mathbb Q\), including zero gaps.

## Proof
**Rotation-order lemma.** Denote gaps \(a,b,c\) by labels \(A,B,C\) respectively. Every rotation beginning in a zero gap has a unique leading-zero length \(t\ge1\). A larger leading-zero length sorts before a smaller one. At equal \(t\), the gap labels that satisfy \(g_i\ge t\) occur in the order \(C,A,B\) if \(b>c\), and \(C,B,A\) otherwise. Indeed, the next nonzero symbol following gap \(C\) is \(1\) whereas the symbols following \(A,B\) are \(2\); in the \(A,B\) tie, the next distinguishing run lengths are \(b,c\), and at equality the following \(1\) for \(B\) sorts before the following \(2\) for \(A\). The three rotations starting with nonzero symbols come last, in the same order \(C,A,B\) or \(C,B,A\), where \(C\) denotes the rotation beginning with the unique \(1\). These comparisons are strict because the word is primitive.

For a zero-start rotation at level \(t\) in gap \(i\), its preceding symbol is \(1\) if \(i=A\) and \(t=g_A\), is \(2\) if \(i=B,C\) and \(t=g_i\), and is \(0\) otherwise. For the final marker-starting rows \(C,A,B\), the predecessors are respectively \(0\) when \(c>0\) and \(2\) when \(c=0\); \(0\) when \(a>0\) and \(1\) when \(a=0\); and \(0\) when \(b>0\) and \(2\) when \(b=0\). This reconstructs the entire BWT last column from the three gap lengths.

**Finite symbolic classification.** Identify \(A,B,C\) with the bit masks \(1,2,4\). Scan levels \(t\) from \(\max(a,b,c)\) down to \(1\) and record the active mask \(M_t=\{i:g_i\ge t\}\). After compressing repeated masks, this is a strictly increasing chain of nonempty subsets of \(\{A,B,C\}\); the empty chain represents \(a=b=c=0\). There are exactly \(26\) such chains (including the empty chain). For an active mask \(M\) following the strictly smaller mask \(P\), the first level contributes its symbol block in the order just proved, with predecessor \(p(A)=1\), \(p(B)=p(C)=2\) for newly active indices \(M\setminus P\), and \(0\) for the other indices. If the mask occupies \(s\) successive levels, the extra \(s-1\) levels contain only zeros. Therefore the contribution of a one-level visit to a mask of cardinality \(k\) is the weight \(z^k\); the contribution of a visit of at least two levels is \(z^{2k}/(1-z^k)\). For the latter visit, a *single* terminal zero represents all further zeros without changing the run count. Append the three marker-starting predecessors as above, and weight every case by \(z^3\) for the nonzero markers.

The presence of a mask containing \(B\) but not \(C\) is equivalent to \(b>c\), so the entire block ordering is determined by the chain. All possible strictly increasing chains with their binary one-level/multiple-level choices are disjoint and exhaustive. There are exactly \(111\) such cases, each representing an infinite disjoint family of gap triples. Summing their rational weights times \(u^{r}\), where \(r\) is the run count of the represented finite block sequence, gives \(\sum_{j=2}^6F_j(z)u^j\). The complete case generator and exact symbolic summation are included in `proof_mask_gf.py`.

With \(D=(1-z)(1-z^2)(1-z^3)\), exact polynomial arithmetic on these \(111\) cases gives the respective numerator polynomials
\[
\begin{aligned}
D F_2&=z^3D,\\
D F_3&=z^4(1-z)^2(2z^3+3z^2+4z+2),\\
D F_4&=z^4(1-z)(3z^2+2z+1),\\
D F_5&=z^5(1-z)(2z^3+3z^2+4z+2),\\
D F_6&=z^6(z^3+z^2+3z+1).
\end{aligned}
\]
The symbolic program asserts each identity individually. Their sum is \(z^3/(1-z)^3\), agreeing with the independent count \(\binom{n-1}{2}\) of gap triples. The nonnegative rational-coefficient expansions show that for every \(n\ge6\) each of \(F_3,F_4,F_5,F_6\) has strictly positive coefficient; alternatively `check_direct.py` confirms the small onsets and the displayed denominators provide the all-length extension. Because the numerators for \(F_3,F_4,F_5\) cancel at least one factor \(1-z\) from \(D\), their coefficients grow at most linearly, while \(\binom{n-1}{2}\) grows quadratically. Hence the proportion of six-run necklaces tends to one.

## Verification
Run `python3 proof_mask_gf.py` with SymPy installed. It independently lists all mask chains and their one-/multiple-level visits, computes the formal rational generating functions, and asserts every numerator, the absence of other run counts, and the total-composition identity. Run `python3 check_direct.py` using only the Python standard library. It enumerates every gap triple and sorts all cyclic rotations directly, comparing the resulting run-count distribution to the closed formulas at **every length from \(3\) through \(54\)**. The finite direct checks corroborate, but do not replace, the all-length symbolic proof.

The first distributions are \(n=3:(C_2)=1\); \(n=4:(C_3,C_4)=(2,1)\); \(n=5:(C_3,C_4,C_5)=(2,2,2)\); \(n=6:(C_3,C_4,C_5,C_6)=(1,4,4,1)\). At length \(n=7\), the respective counts are \((3,3,5,4)\), summing to \(15\).

## Relationship to prior work
The original Burrows–Wheeler transform (1994) defines the ordered-rotation operation. Simpson and Puglisi (2008) characterize a *special* three-letter pattern whose last column has three consecutive single-symbol blocks in a prescribed descending order; they do not enumerate all run counts at the present fixed sparse composition. An existing binary three-identical-marker theorem gives only even run numbers \(2,4,6\) and accounts for binary rotation orbits, in contrast to this exact ternary mixed-marker spectrum of \(2,3,4,5,6\). The ternary sparse statement does not follow from the binary census by alphabet relabeling, and the special three-run characterization does not imply frequencies for the four-, five- and six-run classes.

## Limitations
The theorem is restricted to the fixed ternary content \((n-3,1,2)\) and linear runs of a sentinel-free circular BWT; it does not classify general ternary contents or cyclic runs of the BWT output. An earlier unindexed equivalent sparse-color BWT enumeration is a remaining historical-priority risk. Computational verification through length \(54\) is finite; all-length validity relies on the rotation-order lemma and exact rational mask summation. No independent mathematical audit is claimed.

## References
1. M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, Digital Systems Research Center technical report 124, first public report 10 May 1994. https://www.cl.cam.ac.uk/teaching/2002/DSAlgs/SRC-124.pdf
2. J. Simpson and S. J. Puglisi, *Words with Simple Burrows-Wheeler Transforms*, Electronic Journal of Combinatorics 15(1), R83, 20 June 2008. https://www.kurims.kyoto-u.ac.jp/EMIS/journals/EJC/Volume_15/PDF/v15i1r83.pdf
3. *Exact Burrows–Wheeler run spectrum of cyclic binary words with three markers*, previously released binary composition census. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-burrows-wheeler-run-spectrum-of-cyclic-binary-words-with-t--17765181f4c4
4. M. Crochemore, J. Désarménien and D. Perrin, *A note on the Burrows-Wheeler transformation*, preprint 17 February 2005. https://arxiv.org/abs/cs/0502073
