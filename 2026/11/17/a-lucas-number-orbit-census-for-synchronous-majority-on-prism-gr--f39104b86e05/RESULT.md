# A Lucas-number orbit census for synchronous majority on prism graphs

## Finding

Let \(G_n=C_n\square K_2\) be the undirected prism graph with two labelled \(n\)-cycles joined by corresponding rungs, for every integer \(n\ge3\). Under synchronous binary open-neighborhood majority, each vertex simultaneously adopts the majority opinion of its three graph neighbors. Denote the update by \(F_n\).

Let \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\) denote the Lucas numbers. Let \(H_n=\#\{x:F_n(x)=x\}\) and \(P_n=\#\{x:F_n^2(x)=x\}\). Then, for every \(n\ge3\),

\[
\begin{array}{c|c|c}
n\bmod 6&H_n&P_n\\\hline
0&L_n+4&L_{2n}+8L_n+18\\
1&L_n+3&L_{2n}+1\\
2&L_n+1&L_{2n}+2L_n+3\\
3&L_n&L_{2n}+4\\
4&L_n+1&L_{2n}+2L_n+3\\
5&L_n+3&L_{2n}+1
\end{array}
\]

The exact number of distinct primitive temporal two-cycles is \((P_n-H_n)/2\). Moreover, as \(n\to\infty\), their number is

\[
\frac{P_n-H_n}{2}\sim \frac12\left(\frac{3+\sqrt5}{2}\right)^n.
\]

These are counts of **already periodic** labelled configurations and their orbits, not attraction-basin sizes.

## Assumptions and scope

The graph is simple, undirected, and has labelled vertices \((i,\ell)\), with \(i\in\mathbb Z/n\mathbb Z\) and \(\ell\in\{0,1\}\). The three neighbors of \((i,\ell)\) are \((i-1,\ell)\), \((i+1,\ell)\), and \((i,1-\ell)\). For \(n\ge3\), these are distinct; the update never encounters ties. There are \(2^{2n}\) possible initial configurations. A primitive two-cycle comprises two different configurations exchanged by \(F_n\).

All enumerations distinguish each labelled vertex. Neither configurations up to spatial rotation nor basins of attraction are counted. Known general theorems imply that eventual periods in finite symmetric majority dynamics divide two; the new statement concerns exact all-size orbit counts.

## Proof

**1. Space-time transfer.** Write the two bits in column \(i\) at successive times as \(x_i=(x_i^{(0)},x_i^{(1)})\) and \(y_i=(y_i^{(0)},y_i^{(1)})\). Put \(M(a,b,c)=1\) if \(a+b+c\ge2\) and \(0\) otherwise. The condition \(F_n(x)=y\), \(F_n(y)=x\) is equivalent to, for each \(i\bmod n\) and each layer \(\ell\),

\[
\begin{aligned}
y_i^{(\ell)}&=M(x_{i-1}^{(\ell)},x_{i+1}^{(\ell)},x_i^{(1-\ell)}),\\
x_i^{(\ell)}&=M(y_{i-1}^{(\ell)},y_{i+1}^{(\ell)},y_i^{(1-\ell)}).
\end{aligned}
\]

Encode a column pair as the four-bit letter \(s_i=(x_i^{(0)},x_i^{(1)},y_i^{(0)},y_i^{(1)})\in\{0,1\}^4\). Construct the directed graph \(T\) on 256 ordered pairs of letters: there is an edge \((a,b)\to(b,c)\) precisely when all four equations at the central column \(b\) hold for the triple \((a,b,c)\). This is an unambiguous finite specification of a \(256\times256\) integer adjacency matrix, without any numerical approximation. Its closed walks of length \(n\) correspond bijectively to pairs \((x,y)\) satisfying both updates, hence to \(x\in\operatorname{Fix}(F_n^2)\), because the first update determines \(y\) uniquely. Thus

\[
P_n=\operatorname{tr}(T^n).
\]

For the fixed points, use two-bit letters \(x_i\) alone and the two majority equations. The corresponding directed graph \(S\) on 16 ordered pairs of letters satisfies \(H_n=\operatorname{tr}(S^n)\).

**2. Exact finite algebra.** Only directed strongly connected components containing cycles contribute to a positive-power matrix trace. The cyclic components of \(T\) have sizes \(16,8,8,2,1,1\). The monic characteristic polynomials of their internal adjacency matrices are as follows, with the listed repetitions:

\[
\begin{aligned}
A(z)&=(z-1)^2(z+1)^2(z^2-3z+1)(z^2+z+1)\\
&\quad\cdot(z^4-z^3+2z^2+z+1)(z^4+z^3+2z^2-z+1),\\
B(z)&=(z^2-z-1)(z^2-z+1)(z^2+z-1)(z^2+z+1),\\
C(z)&=z^2-1,\qquad D(z)=z-1.
\end{aligned}
\]

Specifically, they are \(A,B,B,C,D,D\). The cyclic components of \(S\) have sizes \(4,1,1\), with polynomials \((z^2-z-1)(z^2-z+1),D,D\). These exact integer polynomial identities are established by the standalone `verify_transfer.py` checker, which constructs every edge, computes cyclic strongly connected components, and verifies the characteristic coefficients using power traces and Newton identities. The checker is finite, deterministic, and needs only the Python standard library. As the matrices are explicitly defined finite objects, these identities establish the ensuing formulas for **all** cycle lengths \(n\), not just checked examples.

**3. Evaluate the spectral power sums.** Let \(\phi=(1+\sqrt5)/2\). The roots of \(z^2-3z+1\) are \(\phi^2,\phi^{-2}\); the roots of the two quartic factors, taken together, are \(\phi^{\pm1}e^{\pm i\pi/3}\) and \(\phi^{\pm1}e^{\pm 2i\pi/3}\). The roots of \(B\) are \(\pm\phi,\pm\phi^{-1}\), together with primitive third and sixth roots of unity. All these root descriptions follow by direct multiplication of the displayed exact polynomials. Using the identity \(L_j=\phi^j+(1-\phi)^j\), evaluation of traces gives

\[
H_n=L_n+2+2\cos(n\pi/3)
\]

and, setting \(c_n=\cos(2\pi n/3)\),

\[
P_n=\begin{cases}
L_{2n}+2+2c_n,&n\text{ odd},\\
L_{2n}+(4+4c_n)L_n+8+10c_n,&n\text{ even}.
\end{cases}
\]

The six residue classes modulo six produce precisely the table in the finding. Fixed configurations contribute one state to \(P_n\); each primitive two-cycle contributes two. Therefore their exact orbit number is \((P_n-H_n)/2\).

**4. Growth.** The dominant root \(\phi^2=(3+\sqrt5)/2\) of \(z^2-3z+1\) occurs once, while every other root of all cyclic component polynomials has modulus at most \(\phi\). Consequently \(P_n=\phi^{2n}+O(\phi^n)\) and \(H_n=O(\phi^n)\), proving the displayed asymptotic.

## Verification

`verify_transfer.py` exhaustively builds the 256-vertex and 16-vertex directed transfer graphs. It verifies their edge counts (400 and 20), cyclic component sizes, every characteristic polynomial shown above, and evaluates the trace formulas for \(3\le n\le32\). Exact integer matrix multiplications and Newton identities are used throughout.

`verify_vertices.py` is a separate implementation using bitwise rotations on the two actual graph layers rather than transfer states. It exhaustively checks all \(2^{2n}\) initial configurations for every \(3\le n\le10\), counting both fixed points and points fixed by two updates. Output files `verify_transfer.txt` and `verify_vertices.txt` give captured runs. The combinatorial proof, not bounded exhaustive enumeration, establishes the infinite-family statement.

Some examples of \((n,H_n,P_n,\text{primitive two-cycles})\) are \((3,4,22,9)\), \((4,8,64,28)\), \((6,22,484,231)\), \((8,48,2304,1128)\), and \((12,326,106276,52975)\).

## Relationship to prior work

The classical theorem of Goles and Olivos supplies eventual period at most two for finite symmetric threshold dynamics but no prism-specific orbit count. Agur, Fraenkel and Klein give exact fixed-point formulas for the distinct one-dimensional cyclic self-inclusive majority rule; their paper highlights a single two-cycle on an even ring, whereas the prism open-neighborhood majority studied here has exponentially many two-cycles. The difference in graph and in the local neighborhood is essential.

Jen's 1988 work gives a general transfer-matrix framework for cylindrical cellular automata, but the accessible abstract and bibliographic record do not provide the evaluated Lucas-number orbit census for this three-input, two-layer coupled majority rule. Benjamini and collaborators' 2014 arXiv preprint investigates convergence and unanimity on infinite and random graphs; Kaaser and collaborators' 2015 arXiv preprint investigates convergence time. Neither supplies this all-size prism count in the inspected text.

## Limitations

This result does not enumerate attraction basins or maximum transient lengths. It uses strict majority of the **three graph neighbors** and does not apply unchanged to closed-neighborhood majority, ties, Möbius ladders, or path ladders. Existing generic matrix methods are not claimed as new. The 1988 Jen article was not available in complete text for comparison; an unlocated equivalent enumeration remains a historical-priority risk. Independent mathematical validation has not been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: https://doi.org/10.1016/0012-365X(80)90121-1.
2. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302. Accessible primary text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf.
3. E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics 118 (1988), 569–590. DOI: https://doi.org/10.1007/BF01221109.
4. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, May 11, 2014. https://arxiv.org/abs/1405.2486.
5. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, August 14, 2015. https://arxiv.org/abs/1508.03519.
