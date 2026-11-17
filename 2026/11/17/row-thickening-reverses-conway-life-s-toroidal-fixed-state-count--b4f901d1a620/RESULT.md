# Row thickening reverses Conway Life's toroidal fixed-state count at every triple circumference

## Finding

For each integer \(h\ge 3\) and \(n\ge 3\), let \(F_h(n)\) be the number of labelled binary configurations fixed after one synchronous B3/S23 update on the Moore-neighborhood torus \(\mathbb Z_h\times\mathbb Z_n\). In particular all eight neighbors of a cell are distinct for \(h\in\{3,4\}\) and \(n\ge 3\).

**Theorem.** For every positive integer \(n\) divisible by three,
\[
F_4(n)<F_3(n).
\]
Thus enlarging the periodic torus from three rows to four strictly *reduces* its number of fixed configurations, even though the number of possible binary configurations increases.

More precisely, a uniquely specified primitive nonnegative integer matrix \(B\) of order \(127\), defined below without lookup tables, satisfies
\[
F_4(n)=\operatorname{tr}(B^n)\quad(n\ge 3),
\qquad F_4(n)\sim \lambda^n,
\]
where \(\lambda=\rho(B)\), and the rigorous bounds
\[
2.55371542<\lambda<2.55371544
\]
hold. The height-three transfer has a separate component with characteristic polynomial \(x^{24}(x^3-27)\), hence
\[
F_3(n)\ge 3^{n+1}\quad\text{whenever }3\mid n.
\]
The contribution \(3^{n+1}\) is exact for that component; it is not asserted to be the entire height-three count.

Selected exact values \(F_4(3),F_4(4),\ldots,F_4(12)\) are
\[
39,\ 53,\ 313,\ 651,\ 983,\ 3133,\ 5907,\ 16649,\ 43057,\ 99107.
\]
The \(4\times4\) value \(53\) was already documented in a 2018 finite-square-torus census and is not claimed as new.

## Assumptions and scope

Coordinates are modulo the corresponding height and circumference. A site in state \(1\) survives precisely when it has two or three living Moore neighbors; a site in state \(0\) becomes living precisely when it has three. Configurations are labelled; translations and rotations are **not** quotiented out. The comparison is only asserted when \(n\) is divisible by three, and the count concerns one-step fixed configurations, not longer-period oscillators, transients, or finite planar islands.

## Proof

**Column transfer.** A column of height \(h\) is an integer in \(\{0,\ldots,2^h-1\}\); let \(b_r(a)\in\{0,1\}\) be its row-\(r\) bit, read modulo \(h\). For three consecutive columns \((a,b,c)\), define
\[
\begin{aligned}
s_r(a,b,c)={}&b_{r-1}(b)+b_{r+1}(b)\\
 &+\sum_{j=-1}^{1}\bigl(b_{r+j}(a)+b_{r+j}(c)\bigr).
\end{aligned}
\]
Put \(L_h(a,b,c)=1\) precisely if, for all rows \(r\),
\[
b_r(b)=\mathbf1_{\{s_r=3\}}+\mathbf1_{\{s_r=2\}}b_r(b),
\]
and put \(L_h(a,b,c)=0\) otherwise. This sum is disjoint, so its right side is a bit. Define the \(2^{2h}\)-square \(0\)-\(1\) matrix
\[
(T_h)_{(a,b),(b',c)}=\mathbf1_{\{b=b'\}}L_h(a,b,c).
\]
Every closed walk of length \(n\) in \(T_h\) corresponds bijectively to a cyclic word of \(n\) columns whose every middle column satisfies Life's rule. In particular, for all \(n\ge3\),
\[
F_h(n)=\operatorname{tr}(T_h^n).
\]
This identity is exact for all circumferences, rather than an extrapolation from finite enumeration.

**The height-four spectrum.** The exact transfer \(T_4\) has \(256\) vertices and \(499\) directed edges. Its directed graph has \(130\) strongly connected components, exactly one of which contains any directed cycle. That component has \(127\) vertices and \(309\) edges. Let \(B\) be its induced adjacency matrix, ordered by ascending integer indices \(16a+b\) of the pair-column states. This explicit definition uniquely determines every entry of \(B\), and components outside it make zero contribution to any positive trace. Therefore \(F_4(n)=\operatorname{tr}(B^n)\).

The component is strongly connected and contains the empty-state self-loop. Thus \(B\) is primitive. The Perron--Frobenius theorem yields a simple dominant positive eigenvalue \(\lambda\) and \(\operatorname{tr}(B^n)=\lambda^n+o(\lambda^n)\).

An exact symbolic determinant calculation (reproduced by the supplied checker) gives a degree-\(127\) characteristic polynomial with a factor \(x^{46}\); the complete factorization is printed by the checker. With \(\mathbf 1\) the all-ones vector, set \(v=B^{400}\mathbf 1\) and \(w=Bv\). Strict positivity and the Collatz--Wielandt inequalities give
\[
\min_i\frac{w_i}{v_i}\le\lambda\le\max_i\frac{w_i}{v_i}.
\]
The checker evaluates these ratios as exact rationals and verifies that both lie strictly between \(255371542/10^8\) and \(255371544/10^8\), proving the stated numerical interval and in particular \(\lambda<13/5\).

**The height-three lower bound.** Construct \(T_3\) from the *same* local formula. Its directed graph has a cyclic strongly connected component on \(27\) vertices with adjacency matrix \(C\) and exactly computed characteristic polynomial
\[
\det(xI-C)=x^{24}(x^3-27).
\]
For every positive \(n\) divisible by three, the three nonzero eigenvalues contribute
\[
\operatorname{tr}(C^n)=3^{n+1}.
\]
All other contributions to \(\operatorname{tr}(T_3^n)\) count closed walks and are nonnegative, so \(F_3(n)\ge3^{n+1}\).

**Strict comparison.** Since \(B\) has \(127\) eigenvalues, all of modulus at most \(\lambda\),
\[
0\le F_4(n)=\operatorname{tr}(B^n)\le127\lambda^n<127(13/5)^n.
\]
The exact integer inequality \(127\cdot13^{27}<3\cdot15^{27}\) shows that \(127(13/5)^n<3^{n+1}\) for every \(n\ge27\), and therefore for every multiple of three in that range. The remaining positive multiples \(3,6,9,12,15,18,21,24\) have respective exactly computed values
\[
F_4(n)=39,\ 651,\ 5907,\ 99107,\ 1517719,\ 24500451,\ 391780043,\ 6355667155,
\]
all strictly smaller than \(3^{n+1}\). This proves \(F_4(n)<F_3(n)\) for every allowed circumference.

## Verification

The self-contained Python program `check_life4_transfer.py` constructs the transfer graphs directly from the B3/S23 rule, independently recomputes strongly connected components, exactly factors the characteristic polynomial, checks all quoted transfer traces and verifies the rational Perron bounds and the complete all-\(n\) comparison. It requires Python 3 and SymPy. The separate C++ program `check_life4_direct.cpp` uses direct eight-neighbor bit masks rather than column transfer and exhaustively checks all \(2^{4n}\) configurations for \(3\le n\le6\); the two programs agree on counts \(39,53,313,651\). Captured outputs and build instructions accompany these files. The finite exhaustive tests supplement, but do not replace, the transfer and spectral proof.

## Relationship to prior work

Conway's B3/S23 rule was introduced publicly by Gardner in 1970. Jen (1988) gave general cylindrical cellular-automaton trace methods. A May 2018 finite-square-torus census explicitly reports the already-known \(4\times4\) fixed-state count \(53\). In contrast, the theorem here simultaneously establishes the height-four all-circumference trace spectrum, the exact asymptotic, and the strict *every-multiple-of-three* row-thickening reversal. A preexisting height-three toroidal fixed-state analysis treats the other width; the height-three component used in this proof was recomputed independently from the local rule. Neither the general transfer method nor isolated finite-square counts by themselves provide the present height comparison.

## Limitations

This result does not classify higher-period states or transients; it does not assert fixed-state count decreases on circumferences not divisible by three. A plausible 1988 methodological source was available in abstract but not full text through the accessed lawful channels; the 2018 discussion was accessible through indexed excerpts rather than its complete thread. These limit claims of absolute historical priority. The new algebraic computations are fully reproducible, but no independent mathematical audit has been performed.

## References

1. M. Gardner, "Mathematical Games: The fantastic combinations of John Conway's new solitaire game 'life'," *Scientific American* **223**(4) (1970), 120--123, DOI: 10.1038/scientificamerican1070-120. The publisher dates its public item October 1, 1970.
2. E. Jen, "Cylindrical cellular automata," *Communications in Mathematical Physics* **118** (1988), 569--590, DOI: 10.1007/BF01221109. General transfer method; complete text not inspected.
3. F_rank, "Small Tori in B3/S23," ConwayLife.com discussion, May 10, 2018, https://conwaylife.com/forums/viewtopic.php?t=3383. Indexed discussion includes the \(4\times4\) count \(53\).
4. Stephen A. Silver, *Life Lexicon*, "Still life," https://playgameoflife.com/lexicon/still_life. Definition of standard still-life terminology, not an exact torus count.
