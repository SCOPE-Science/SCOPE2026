# Exact coprime-run laws for the three quadratic cyclotomic sequences

## Finding
For the complete family of monic degree-two cyclotomic polynomials
\[\Phi_3(X)=X^2+X+1,\qquad \Phi_4(X)=X^2+1,\qquad \Phi_6(X)=X^2-X+1,\]
let \(R_m(n)\) be the length of the longest initial block of pairwise coprime integers in \(\Phi_m(n),\Phi_m(n+1),\ldots\), for \(n\ge1\). Then \(R_3\) and \(R_6\) have least positive period \(399\), and their frequencies in every full period are
\[
\begin{array}{c|rrrr}r&2&3&4&5\\\hline
\#\{n:R_m(n)=r\}&57&152&118&72\end{array}.
\]
For \(m=4\), the least positive period is \(10\), with frequencies \(2,5,3\) at \(r=1,2,3\), respectively. No longer coprime blocks exist for any of these three sequences. In particular, the maximal-run-start densities are \(24/133\) for \(m=3,6\) and \(3/10\) for \(m=4\).

More precisely, for every integer \(n\ge1\), the five values \(\Phi_3(n),\ldots,\Phi_3(n+4)\) are pairwise coprime exactly when
\[
n\equiv2\pmod3,\qquad n\bmod7\in\{3,4,5,6\},\qquad n\not\equiv7\pmod{19}.
\]
For \(\Phi_6\), replace \(n\) by \(n-1\) in this criterion. The three values \(\Phi_4(n),\Phi_4(n+1),\Phi_4(n+2)\) are pairwise coprime exactly when \(n\) is even and \(n\bmod5\in\{0,3,4\}\).

The complete edge-count distributions of the common-divisor graphs on these maximal possible windows, with one edge for every unordered pair having gcd greater than one, are also exact. For \(m=3,6\) the counts for \(0,1,2,3\) edges are \(72,202,119,6\) per period \(399\); for \(m=4\) the counts for \(0,1,2\) edges are \(3,5,2\) per period \(10\). Every nontrivial pair gcd on these windows is a single prime: \(3,7,19\) for \(m=3,6\), or \(2,5\) for \(m=4\).

## Assumptions and scope
The index \(m\) is exactly one of \(3,4,6\), the only indices with cyclotomic polynomial degree two. The starting index \(n\) is any positive integer, and all gcds are positive. A block of length \(k\) is pairwise coprime if the gcd of every two distinct entries equals one. Its run length \(R_m(n)\) is the greatest such \(k\). Frequencies are counts of starting indices in any consecutive full period; their ratios to the period are natural densities, with no probabilistic assumptions.

## Proof
**1. Exact local gcds.** For \(P_3(X)=X^2+X+1\) and \(P_4(X)=X^2+1\), direct polynomial elimination gives
\[
\operatorname{Res}_X(P_3(X),P_3(X+h))=h^2(h^2+3),\qquad
\operatorname{Res}_X(P_4(X),P_4(X+h))=h^2(h^2+4).
\]
Any common prime divisor of two integer values divides the corresponding resultant. For \(P_3\), all values are odd. On a five-value window, separations \(h=1,2,3,4\) therefore allow only the following nontrivial gcds:
\[
\begin{array}{c|c|c}
 h&\text{gcd}&\text{condition on the lower index }x\\\hline
 1&1&\text{always}\\
 2&7&x\equiv2\pmod7\\
 3&3&x\equiv1\pmod3\\
 4&19&x\equiv7\pmod{19}
\end{array}.
\]
Here a row with gcd greater than one means precisely that gcd when the displayed congruence holds, and gcd one otherwise. The root pairs for \(P_3\) modulo \(7\) are \(2,4\), modulo \(3\) are both \(1\) at distance \(3\), and modulo \(19\) are \(7,11\). The resultants have prime valuations exactly one at \(7\) and \(19\); when \(x\equiv1\pmod3\), \(P_3(x)\equiv3\pmod9\), forcing gcd exactly \(3\).

For \(P_4\), within a three-value window, consecutive values have gcd \(5\) exactly when the lower index is \(2\pmod5\), and values at separation two have gcd \(2\) exactly when the lower index is odd; other gcds equal one. Indeed the corresponding resultants are \(5\) and \(32\), the roots modulo \(5\) are \(2,3\), and for odd \(x\), \(P_4(x)\equiv2\pmod8\). Finally \(\Phi_6(x)=\Phi_3(x-1)\), giving its complete table by translation.

**2. Finite maximal lengths.** Every six consecutive integers contain two distinct numbers congruent to \(1\pmod3\), whose \(P_3\)-values are both divisible by \(3\), so no six-value block is pairwise coprime. Every four consecutive indices contain two odd numbers, whose \(P_4\)-values are even, so no four-value block is pairwise coprime. Any adjacent two \(P_3\)-values are coprime; each sequence also has starting indices realizing its stated longest blocks, by the congruence criteria below. The same assertions for \(\Phi_6\) follow by translation.

**3. Congruences and exact run frequencies.** On the five-value \(P_3\) window, the possible gcd edges are \((i,i+2)\) for \(i=0,1,2\) (modulus \(7\)), \((i,i+3)\) for \(i=0,1\) (modulus \(3\)), and \((0,4)\) (modulus \(19\)). Avoiding these edges gives precisely the three claimed residue restrictions. They leave \(1\cdot4\cdot18=72\) of the \(3\cdot7\cdot19=399\) residues by the Chinese remainder theorem. The numbers of starts permitting at least \(2,3,4,5,6\) terms per period are respectively \(399,342,190,72,0\): length at least three excludes one residue modulo \(7\), and length at least four excludes two residues modulo \(7\) and one modulo \(3\). Taking successive differences gives \(57,152,118,72\).

For \(P_4\), a three-term window is pairwise coprime exactly when \(n\equiv0\pmod2\) and \(n\bmod5\in\{0,3,4\}\), yielding \(3\) starts per \(10\). A two-term window requires only \(n\not\equiv2\pmod5\), yielding \(8\) starts per \(10\). Hence the counts for exact run lengths \(1,2,3\) are \(2,5,3\).

**4. Graph distributions.** The three independent local contributions to the number of edges for \(P_3\) have generating polynomials \(1+2z\), \(4+3z\), and \(18+z\), from residues modulo \(3,7,19\), respectively. Their product equals \(72+202z+119z^2+6z^3\). For \(P_4\) the corresponding product is \((1+z)(3+2z)=3+5z+2z^2\). Chinese remaindering justifies multiplication of residue counts.

**5. Least periods.** The successful maximal-length starts for \(P_3\) form a nonempty Cartesian product of proper nonempty residue subsets modulo \(3,7,19\). Any translation preserving this set must preserve each local projection. Since each local modulus is prime, no nonzero additive translation stabilizes a proper nonempty subset. Therefore every period is divisible by \(3\), \(7\), and \(19\), and the least period of the maximal-run indicator is \(399\). As \(R_3\) itself has this period, its least period is also \(399\). Exactly the same argument for the nonempty proper residue subsets modulo \(2,5\) proves period \(10\) for \(R_4\), and translation proves the \(\Phi_6\) result.

## Verification
A standalone standard-library Python program `verify.py` independently enumerates the relevant pairwise gcds for every starting index in the full periods and compares the exact edge tables, run-frequency histograms, edge-number histograms and all proper-divisor periods against the formulas. It also checks further large indices. Execute `python verify.py`. This is finite corroboration only; the proof above establishes the assertions for every positive integer.

## Relationship to prior work
Deshouillers and Naik (first posted June 26, 2025) proved arbitrarily long pairwise-coprime consecutive blocks when a smooth function has second derivative tending to zero and unbounded first derivative. The three present integer quadratic polynomials have second derivative identically two, so their theorem is inapplicable; the present conclusion is instead a sharp uniform upper bound with a full periodic spectrum. Sanna and Szikszai (2017) studied the complementary Pillai-type property of blocks in which **no** value is coprime to all the others, using polynomial resultant techniques. Their statements do not imply the present exact pairwise-coprime run spectrum, although those techniques are relevant background. General resultant-gcd literature supports the local algebraic mechanism; the exact complete cyclotomic classification is a separate finite-CRT conclusion.

## Limitations
Only the degree-two cyclotomic polynomials are classified. The proof uses explicit small-resultant information particular to this complete finite family and is not an asymptotic theorem for arbitrary quadratic polynomials or higher-degree cyclotomic polynomials. The exact counts are reproducible, but neither a historical-priority guarantee nor any independent external audit is asserted. The finite checker does not replace the symbolic proof.

## References
1. J.-M. Deshouillers and S. Naik, *On coprimality of consecutive elements in certain sequences*, arXiv:2506.20948, first posted June 26, 2025, https://arxiv.org/abs/2506.20948.
2. C. Sanna and M. Szikszai, *A coprimality condition on consecutive values of polynomials*, arXiv:1704.01738, first posted April 6, 2017; *Bull. Lond. Math. Soc.* 49 (2017), 908–915, https://arxiv.org/abs/1704.01738.
3. A. Bodin and C. Drouin, *Around the GCD of the Values of Two Polynomials*, *Amer. Math. Monthly* 132 (2025), 754–765, DOI:10.1080/00029890.2025.2525048; general resultant context, not evidence of the present exact profile.
