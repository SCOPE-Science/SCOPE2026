# The frozen-state zeta and occupation density of three-row Life without Death

## Finding

Consider Life without Death (outer-totalistic rule `B3/S012345678`) on the labelled Moore-neighborhood torus \(\mathbb Z_3\times\mathbb Z_n\), \(n\ge3\), with synchronous updates. Let \(Z_n(u)\) be the sum of \(u^k\) over all fixed configurations with exactly \(k\) occupied cells. Put \(m_c=\binom3c\) for \(0\le c\le3\), and define a \(16\times16\) polynomial matrix indexed by pairs \((a,b)\in\{0,1,2,3\}^2\):

\[
T(u)_{(a,b),(b',c)}=
\begin{cases}
\binom3c\,u^c,&b=b'\text{ and }\bigl(b=3\text{ or }a+b+c\ne3\bigr),\\
0,&\text{otherwise}.
\end{cases}
\]

The **complete occupation-resolved fixed-state census**, for every \(n\ge3\), is

\[
\boxed{Z_n(u)=\operatorname{tr}\bigl(T(u)^n\bigr).}
\]

In particular, with \(D(z)=\det(I-zT(1))\),

\[
\begin{aligned}
D(z)={}&1-5z-15z^2-26z^3+162z^4+528z^5+261z^6\\
&-1188z^7-4131z^8-3888z^9-1458z^{10}+2187z^{11},
\end{aligned}
\]

and the exact generating function is

\[
\boxed{\sum_{n\ge1}\operatorname{tr}(T(1)^n)z^n=-z\frac{D'(z)}{D(z)}.}
\]

The formal terms for circumferences one and two are transfer-graph traces only; the physical torus theorem starts at three. The counts for \(n=3,4,5,6,7\) are respectively \(428,2447,16635,117892,811242\).

The transfer graph is primitive. Its Perron eigenvalue \(\lambda\) satisfies the exact certified bracket

\[
\frac{43617827115317}{6245655706778}\le\lambda\le
\frac{29011117680146}{4154114605937},
\quad\lambda=6.983706621545\ldots .
\]

Consequently \(Z_n(1)\sim\lambda^n\) and the fixed-state entropy per lattice site is \(\frac13\log\lambda=0.6478599368\ldots\). The fraction of all \(2^{3n}\) configurations already fixed is asymptotic to \((\lambda/8)^n\), which tends exponentially to zero.

There is also an exact expression for the typical occupied fraction in the uniform distribution on fixed configurations. Write \(\mathcal D(z,u)=\det(I-zT(u))\), \(z_*=1/\lambda\), and let the partial derivatives be evaluated at \((z_*,1)\). Then

\[
\boxed{
\lim_{n\to\infty}\frac{Z_n'(1)}{3nZ_n(1)}=
\frac{\partial_u\mathcal D(z_*,1)}{3z_*\partial_z\mathcal D(z_*,1)}
=0.5822864541778059\ldots .}
\]

## Assumptions and scope

The vertices of the torus are \((r,i)\) with \(r\in\mathbb Z_3\) and \(i\in\mathbb Z_n\). Every site has eight **distinct** Moore neighbors because \(n\ge3\). An occupied site stays occupied unconditionally; a vacant site becomes occupied if and only if exactly three of its neighbors are occupied. A fixed configuration is one unchanged by a complete synchronous update. Column positions and row positions are labelled; no translation, rotation, or reflection quotient is taken. The variable \(u\) marks the total number of occupied sites, not the number of columns containing occupied sites.

## Proof

Write \(c_i\in\{0,1,2,3\}\) for the population of the \(i\)-th vertical column. For a vacant cell in column \(i\), its two vertical neighbors comprise the other two cells of that column, while its six diagonal/horizontal neighbors comprise all cells in columns \(i-1\) and \(i+1\). Since the cell itself is vacant, the occupied-neighbor count is exactly

\[
c_{i-1}+c_i+c_{i+1}.
\]

If \(c_i=3\), the column has no vacant cell and imposes no birth constraint. Otherwise, every vacant cell in that column has the same neighbor count and the column is fixed precisely if \(c_{i-1}+c_i+c_{i+1}\ne3\). Thus the fixed-state condition is equivalent to the stated local constraint for all cyclic triples of column populations.

For a prescribed population \(c_i=c\), there are exactly \(\binom3c\) choices of its labelled binary column, each contributing \(u^c\). A closed length-\(n\) walk of the pair-state graph is the cyclic sequence of all population pairs \((c_{i-1},c_i)\), with each transition contributing the independent weight of the appended column. The closed-walk product is therefore exactly the multiplicity and occupation weight of that binary configuration. The correspondence is one-to-one for each indexed sequence. Hence \(Z_n(u)=\operatorname{tr}(T(u)^n)\).

Exact rational-integer characteristic-polynomial expansion gives

\[
\begin{aligned}
\det(XI-T(1))=X^5(&X^{11}-5X^{10}-15X^9-26X^8+162X^7\\
&+528X^6+261X^5-1188X^4-4131X^3\\
&-3888X^2-1458X+2187).
\end{aligned}
\]

The determinant formula above follows by reversing coefficients. The formal trace identity is the standard finite-matrix identity \(-z\,\partial_z\log\det(I-zT)=\sum_{n\ge1}\operatorname{tr}(T^n)z^n\), verified as a formal power series over the integers.

All sixteen pair-states communicate: any state other than \((0,0)\) reaches \((3,3)\) by appending two full columns; \((0,0)\) reaches it by appending populations \(1,3,3\). Conversely \((3,3)\) reaches every state \((a,b)\ne(0,0)\) by appending \(a,b\), and reaches \((0,0)\) by appending \(1,0,0\). (Each displayed path obeys the local constraint.) The state \((3,3)\) has a self-loop. Hence the nonnegative matrix \(T(1)\) is primitive, with a simple strictly dominant positive eigenvalue. The exact rational bounds on that eigenvalue follow from the Collatz–Wielandt inequalities applied to the explicit positive sixteen-entry integer vector in `check_symbolic.py`; that script verifies each inequality in rational arithmetic.

Primitivity persists for positive \(u\), so \(\lambda(u)\), the dominant eigenvalue of \(T(u)\), is analytic near \(u=1\). We have \(Z_n(u)=\lambda(u)^n+o(\lambda(u)^n)\) locally uniformly with differentiable error. Thus the mean occupied fraction tends to \(\lambda'(1)/(3\lambda(1))\). Implicit differentiation of \(\mathcal D(1/\lambda(u),u)=0\) yields the displayed exact partial-derivative formula. The decimal occupation density is a numerical evaluation of this algebraic expression, not a separate approximation-based proof.

## Verification

`check_symbolic.py` independently constructs the weighted sixteen-state graph, checks its strong connectivity and loop, computes the exact characteristic polynomial and zeta denominator, verifies a rational Perron bracket, evaluates the occupation fraction, and enumerates the complete occupied-cell histograms through circumference seven by transfer. Run it with `python3 check_symbolic.py` after installing SymPy (`python3 -m pip install sympy`). Its recorded output is `output_symbolic.txt`.

`check_direct.cpp` computes the original eight-neighbor update at every vacant site for every binary configuration on the \(3\times n\) tori for \(3\le n\le7\). It does not invoke a transfer matrix or column-weight reduction. Compile and run with `g++ -O3 -std=c++17 check_direct.cpp -o check_direct && ./check_direct`; `output_direct.txt` gives the recorded counts and occupancy histograms. The two independent methods agree for each of these five circumferences. These finite experiments are checks, not substitutes for the all-circumference transfer proof.

## Relationship to prior work

Toffoli and Margolus introduced the rule as Inkspot in *Cellular Automata Machines* (1987), pp. 6–7, as identified in the original 1998 Gravner–Griffeath survey. Griffeath and Moore (1996) proved computational-complexity properties using growing ladders. Gravner and Griffeath (1998), section 4, analyzed planar growth, fixation from particular seeds, and sensitivity to seeds. Eppstein (2009) described faster ladders. These primary discussions address infinite-plane evolution and constructions rather than the exact density-resolved fixed-state population on all periodic three-row tori.

Published work on Conway Life, HighLife, three-color cyclic rules, and majority automata on strips treats different updates. In particular, every fixed configuration of Conway Life is fixed under Life without Death, but Conway Life's fixed-state census does not determine the strictly larger Life-without-Death census. The algebraic finite-state counting method itself is standard; the claimed result is its exact application and the resulting new polynomial, entropy and occupation law for this specific model.

## Limitations

The theorem concerns fixed points and their uniform counting measure only; it does not determine the probability that a random starting configuration eventually reaches any particular fixed point, fixation times beyond the elementary \(3n\) upper bound, or growth on the infinite plane. The full text of the 1987 book's original relevant pages could not be inspected in the literature comparison; unindexed earlier enumerations therefore remain a historical-priority risk. Numerical occupation and entropy figures are approximations to exact algebraic quantities. No independent external mathematical audit has been performed.

## References

1. T. Toffoli and N. Margolus, *Cellular Automata Machines: A New Environment for Modeling*, MIT Press, public edition dated 1987-04-22, pp. 6–7. https://doi.org/10.7551/mitpress/1763.001.0001 .
2. D. Griffeath and C. Moore, “Life Without Death is P-complete,” *Complex Systems* **10** (1996), 437–447. https://wpmedia.wolfram.com/sites/13/2018/02/10-6-3.pdf .
3. J. Gravner and D. Griffeath, “Cellular Automaton Growth on \(\mathbb Z^2\): Theorems, Examples, and Problems,” definitive preprint April 1998, section 4; *Advances in Applied Mathematics* **21** (1998), 241–304. https://www.math.ucdavis.edu/~gravner/papers/cagrowth.pdf .
4. D. Eppstein, “Faster ladders in Life without Death,” 2009-06-07. https://11011110.github.io/blog/2009/06/07/faster-ladders-in.html .
