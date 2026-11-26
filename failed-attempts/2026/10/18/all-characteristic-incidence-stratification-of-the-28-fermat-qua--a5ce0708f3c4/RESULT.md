# All-characteristic incidence stratification of the 28 Fermat-quartic bitangents

## Finding
Let \(k\) be algebraically closed of odd prime characteristic \(p\), and let \(C\subset\mathbb P^2_k\) be the Fermat quartic \(x^4+y^4+z^4=0\). Write \(N_j\) for the number of geometric projective points lying on exactly \(j\) of the 28 distinct bitangent lines, considering points in the entire projective plane, whether or not on \(C\). Then every intersection is at most fourfold, and

\[
\begin{array}{c|ccc}
p&N_2&N_3&N_4\\\hline
3&0&0&63\\
5&240&16&15\\
17&144&48&15\\
\text{other odd primes}&288&0&15
\end{array}
\]

The 16 non-coordinate lines and 12 coordinate-pair lines have individual incidence profiles \((n_2,n_3,n_4)\), respectively:

\[
\begin{array}{c|cc}
p&\text{16-line family}&\text{12-line family}\\\hline
3&(0,0,9)&(0,0,9)\\
5&(12,3,3)&(24,0,1)\\
17&(12,3,3)&(8,8,1)\\
\text{other odd primes}&(18,0,3)&(24,0,1)
\end{array}
\]

Consequently \(3,5,17\) are exactly the odd characteristics at which this entire incidence pattern departs from characteristic zero; especially characteristic five creates exactly 16 triple concurrences.

## Assumptions and scope
The algebraic closure and the word geometric are essential: a bitangent line and its intersection points need not be rational over the prime field. The result concerns geometric concurrence of **distinct** bitangent lines, not their tangency-point rationality, intersections with the quartic, or exceptional curves of a double cover. The quartic is nonsingular in every odd characteristic because the three partial derivatives have no common projective zero.

## Proof
Choose a primitive eighth root \(\zeta\) with \(\zeta^4=-1\). All 28 bitangents are the distinct lines

\[
\{\zeta^{2i}x+\zeta^{2j}y+z=0:0\le i,j<4\}
\quad\text{and}\quad
\{u-\zeta^{2h+1}v=0:0\le h<4,\ \{u,v\}\in\{\{x,y\},\{x,z\},\{y,z\}\}\}.
\]

For the first family, with \(X=\alpha x\) and \(Y=\beta y\), the line restriction satisfies \(X^4+Y^4+(X+Y)^4=2(X^2+XY+Y^2)^2\). The remaining lines restrict the quartic to the fourth power of the third coordinate. Thus these are 28 distinct bitangents for every \(p\ne2\). They exhaust the bitangents because a smooth plane quartic in odd characteristic has 28 odd theta characteristics, hence 28 geometric bitangent lines, counted with their possible hyperflexes.

All line coefficients are defined over the cyclotomic integer ring \(\mathbb Z[\zeta]=\mathbb Z[t]/(t^4+1)\). For each of the \(\binom{28}{3}=3276\) three-line determinants \(d=a+b\zeta+c\zeta^2+e\zeta^3\), the algebraic norm to \(\mathbb Q\) equals

\[
\operatorname{Norm}(d)=(a^2-c^2+2be)^2+(2ac-b^2+e^2)^2.
\]

Direct exhaustive integer arithmetic in `verify_norms.py` yields **60 identically zero determinants**. Among the other 3216 determinants, the complete distribution of nonzero absolute norms is

\[
\begin{array}{c|rrrrrrrrrrrr}
\lvert\operatorname{Norm}(d)\rvert&1&2&4&8&9&16&17&32&36&64&256&400\\\hline
\#&384&64&864&384&192&560&192&96&192&192&64&32
\end{array}.
\]

Every such norm has prime factors drawn from \(\{2,3,5,17\}\). A determinant which is nonzero in the cyclotomic ring therefore remains nonzero after any specialization to a field of odd characteristic outside \(\{3,5,17\}\): otherwise the characteristic would divide the norm. Conversely, every identically vanishing determinant stays zero. Thus the complete triple-concurrence incidence relation is **identical in every other odd characteristic**, including arbitrary algebraically closed fields, not merely the sampled prime fields.

The finite exact checker `verify_fields.py` constructs the splitting field \(\mathbb F_{p^2}\) for \(p=3,5,7,17\), enumerates all 28 lines there, and groups the \(\binom{28}{2}=378\) pairwise intersections by normalized homogeneous coordinates. It exhaustively finds the tables above for the exceptional primes, and for the representative nonexceptional prime \(7\). The norm theorem transfers the characteristic-seven **triple-concurrence relation**, and hence all multiplicities and per-line profiles, to every other odd prime \(p\notin\{3,5,17\}\). The finite computation is exhaustive for these four finite fields, and the algebraic norm argument supplies the global step. Both checkers are standalone standard-library Python scripts embedded with this result. For every row, the identity \(\sum_j\binom{j}{2}N_j=378\) gives an independent incidence check.

## Verification
Run `python3 verify_norms.py` and `python3 verify_fields.py` with Python 3, no third-party modules. The first script exhaustively checks 3276 three-line determinants, their 12 norm values, and the exact exceptional-prime support; the second enumerates every geometric pairwise intersection over \(\mathbb F_{p^2}\) for four primes and checks the complete incidence distribution and the two line-profile types. The outputs `NORM_OK` and `FIELD_OK` mean precisely these finite certificates passed. No computation is used as a substitute for the norm-based all-characteristics implication.

## Relationship to prior work
Knecht and Reyes (2015, arXiv:1510.04621, §§2 and 4) explicitly give the characteristic-three Fermat quartic with 63 fourfold intersections and, in Theorem 4.5, the characteristic-17 Fermat quartic with the two bitangent intersection types that imply 15 fourfold and 48 triple intersections. Their results cover those particular finite-field instances and must not be claimed as new. Janasz, Pokora and Zieliński (2025, §3.2) give the complex Fermat-quartic bitangents and their 15 fourfold incidence points; this covers the generic complex configuration, not the arithmetic specialization analysis. Betten, Kaplan and Karaoglu's 2021 finite-field catalogue includes \(\mathbb F_9\) and \(\mathbb F_{17}\) quartic classifications and explicit bitangents, but is not an all-odd-characteristic incidence classification. The contribution here is the **uniform exceptional-characteristic theorem**, including the characteristic-five triple-locus count and a finite cyclotomic norm certificate proving no other odd prime can alter the incidence pattern.

## Limitations
This does not classify other smooth quartics, their bitangent arithmetic forms, or incidence schemes with nilpotent structure. The proof uses a finite exhaustive integer determinant calculation whose correctness is reproducible through the embedded code; it is not a hand table of all determinants. Although the closest relevant primary literature was inspected, a published all-characteristic specialization theorem outside the reviewed sources remains a residual overlap risk. Independent audit has not been performed.

## References
1. A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields* (first public 2015-10-15), arXiv:1510.04621, §§2,4, Theorems 4.1 and 4.5. https://arxiv.org/abs/1510.04621
2. M. Janasz, P. Pokora and M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, Fundamenta Mathematicae (published online 2025), DOI:10.4064/fm240105-13-12, especially §3.2.
3. A. Betten, N. Kaplan and F. Karaoglu, *Classification of Quartic Curves Over Small Finite Fields* (2021), https://www.math.colostate.edu/~betten/mathdata/quartic_curves.html.
