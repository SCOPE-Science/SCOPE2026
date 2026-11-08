# Rational 1-limited domination census of Möbius ladders

## Finding

Let \(M_n\), for an integer \(n\ge2\), be the simple cubic graph on \(\mathbb Z/(2n)\mathbb Z\) with cycle edges \(\{i,i+1\}\) and antipodal edges \(\{i,i+n\}\), all indices understood modulo \(2n\). A set \(S\subseteq V(M_n)\) is *1-limited dominating* if every vertex outside \(S\) has at least one neighbor in \(S\), and every vertex in \(S\) has at most one neighbor outside \(S\). Define \(P_n(z)=\sum_{S}z^{|S|}\), summing over all such sets of **labelled** vertices.

For every \(n\ge2\),
\[
\gamma_1^{\mathrm L}(M_n)=\begin{cases}n,&n\equiv0\pmod4,\\n+1,&n\not\equiv0\pmod4,\end{cases}
\qquad
\#\{S:|S|=\gamma_1^{\mathrm L}(M_n)\}=\begin{cases}4,&n\equiv0\pmod4,\\2n,&n\equiv2\pmod4,\\3n,&n\ \text{odd}.\end{cases}
\]
The stronger statement determines the *entire* limited-domination polynomial sequence. Write
\[
4+z^2t+\sum_{n\ge2}P_n(z)t^n=\frac{N(t,z)}{D(t,z)},
\]
where \(D(t,z)=\sum_{j=0}^{8}d_j(z)t^j\), \(N(t,z)=\sum_{j=0}^{7}u_j(z)t^j\), and the coefficients are given exactly below.

| \(j\) | \(d_j(z)\) | \(u_j(z)\) |
|---:|---|---|
| 0 | \(1\) | \(4\) |
| 1 | \(-2z-z^2\) | \(-8z-3z^2\) |
| 2 | \(z^2+2z^3\) | \(4z^2+10z^3\) |
| 3 | \(-2z^4-2z^5\) | \(-6z^4-6z^5\) |
| 4 | \(-z^4+2z^5+z^6\) | \(2z^5+2z^6\) |
| 5 | \(2z^5-z^6-z^8\) | \(-z^6-4z^7-3z^8\) |
| 6 | \(-z^6\) | \(-4z^7+2z^8\) |
| 7 | \(z^{10}\) | \(2z^8+z^{10}\) |
| 8 | \(z^{10}\) | \(0\) |

The initial terms \(4\) and \(z^2t\) are formal transfer traces for widths zero and one; they are not graph polynomials of a Möbius ladder. For all actual graphs the range is \(n\ge2\).

## Assumptions and scope

Graphs are finite and simple, the antipodal edge is counted once per pair, and vertices are distinguished by their integer labels. For \(n=2\) the graph is \(K_4\), with four minimum 3-vertex sets. The parameter \(\gamma_1^{\mathrm L}\) uses the restriction on *selected* vertices; it is not the distinct notion of \([1,2]\)-domination, which restricts the number of selected neighbors of *unselected* vertices.

## Proof

**1. A general bound.** Given any 1-limited dominating \(S\), let \(T=V\setminus S\) and \(c\) be the number of edges crossing \((S,T)\). Domination requires \(c\ge|T|\), and limitedness requires \(c\le|S|\). As \(|S|+|T|=2n\), we obtain \(|S|\ge n\). For any \(n\ge2\), the set of the \(n+1\) consecutive vertices \(S=\{0,1,\ldots,n\}\) is 1-limited dominating: each selected interior vertex has its two cycle neighbors selected, the selected endpoints \(0,n\) have one cycle neighbor and their antipodal neighbor selected, and each outside vertex has its antipodal neighbor selected. Hence \(\gamma_1^{\mathrm L}(M_n)\le n+1\).

**2. Exact local transfer.** View the graph as \(n\) two-vertex columns. Column \(i\) contains vertices \(i,i+n\), and is labelled by \(x_i\in\{0,1,2,3\}\), whose two binary digits state selected membership. Consecutive columns are joined by the two parallel same-row edges, except that closing the strip joins rows with a swap. Let \(\sigma\) interchange the two binary digits, so \(\sigma(0)=0,\sigma(1)=2,\sigma(2)=1,\sigma(3)=3\). Extend columns by \(x_{-1}=\sigma(x_{n-1})\) and \(x_n=\sigma(x_0)\).

For \(a,b,c\in\{0,1,2,3\}\), call \((a,b,c)\) admissible when, for each row \(r\in\{0,1\}\),
\[
\operatorname{bit}_r(a)+\operatorname{bit}_{1-r}(b)+\operatorname{bit}_r(c)
\ \ge\ 1+\operatorname{bit}_r(b).
\]
This is precisely the limited-domination condition at that vertex: an outside vertex has at least one selected neighbor, and a selected cubic vertex has at least two selected neighbors.

Index a \(16\times16\) matrix \(T(z)\) by ordered pairs \((a,b)\). Put
\[
T(z)_{(a,b),(b',c)}=\begin{cases}z^{\operatorname{wt}(b)},&b'=b\ \text{and }(a,b,c)\text{ admissible},\\0,&\text{otherwise},\end{cases}
\]
where \(\operatorname{wt}(b)\) is the number of ones in the two digits of \(b\). Let \(J\) be the permutation matrix sending \((a,b)\) to \((\sigma(a),\sigma(b))\). Exactly \(26\) entries of \(T\) are nonzero. For every \(n\ge2\), expansion over closed twisted walks gives a weight-preserving bijection, hence
\[
P_n(z)=\operatorname{tr}(T(z)^nJ).
\]
The analogous traces for \(n=0,1\) are \(4,z^2\), respectively. Consequently, as formal power series in \(t\),
\[
F(t,z):=\sum_{n\ge0}\operatorname{tr}(T(z)^nJ)t^n
=\operatorname{tr}((I-tT(z))^{-1}J).
\]

**3. Finite exact algebraic identity.** Applying Newton identities to \(T\) gives \(\det(I-tT)=D(t,z)\), with the nine coefficients in the table. The adjugate identity shows \(D(t,z)F(t,z)=\operatorname{tr}(\operatorname{adj}(I-tT)J)\), a polynomial of degree at most \(15\) in \(t\). Computing its sixteen coefficients by convolution of the characteristic coefficients with the twisted traces gives exactly \(N(t,z)\) in the table; all coefficients of degrees eight through fifteen vanish. This proves the displayed rational identity *for every* \(n\), not merely for sampled values. The included standard-library Python checker constructs the \(16\)-state transition system afresh, computes both traces to degree \(16\) by exact integer path enumeration, verifies all Newton divisions and the full characteristic and adjugate coefficient identities.

**4. Extraction of the first two coefficient diagonals.** Substitute \(t\mapsto t/z\) in \(F(t,z)\). Every real limited-dominating set has \(|S|\ge n\), so coefficients of \(z^0,z^1\) now count sets of sizes \(n,n+1\). Direct collection of the constant and linear terms from the displayed polynomials gives
\[
[z^0]F(t/z,z)=\frac{4}{1-t^4},\qquad
[z^1]F(t/z,z)=\frac{t(1+4t+7t^2-2t^4)}{(1-t^2)^2}.
\]
The first series has coefficient four precisely for positive \(n\) divisible by four, and zero otherwise. For \(n\ge2\), the coefficient of \(t^n\) in the second series is \(2n\) for even \(n\) and \(3n\) for odd \(n\). The earlier lower and upper bounds then give the minimum sizes and all the stated counts. The four weight-\(n\) solutions for \(n\equiv0\pmod4\) are concretely supplied by the four cyclic shifts of the pattern \(1100\) around the \(2n\)-cycle; the coefficient extraction proves that no others exist. This completes the proof.

## Verification

Run `python3 verify.py` with Python 3.10 or newer. The checker derives all \(16\) characteristic coefficients using integer Newton identities, verifies the exact rational numerator, checks the two low-diagonal generating functions, independently enumerates every vertex subset for \(2\le n\le9\), and checks further transfer values for \(10\le n\le16\). It prints `VERIFY_OK` only after every assertion succeeds. In the recorded execution, all assertions passed. The unrestricted theorem rests on the proved transfer bijection and finite exact polynomial identities, not on extrapolating the finite examples.

## Relationship to prior work

Božović, Radić, Kovijanić-Vukićević, and Tepeh introduced limited domination in 2026 and proved general inequalities and its equivalence to \((1,2)\)-domination in cubic graphs. Radić and Tepeh established its hardness on planar cubic graphs and exact Goldberg-snark values. Radić, Radić, and Tepeh subsequently characterized the structure of low-excess cubic limited dominating sets and obtained exact results for further snark families, using the already known characterization of the half-order equality case. These results are prior work and are not claimed anew. The current theorem adds a specific nonplanar, vertex-transitive cubic family with an exact four-residue minimum law, labelled minimum-set counts, and its full generating polynomial; these are not implied by their scalar general bounds or equality characterization without the new family-specific analysis. An unrelated literature on \([1,2]\)-domination in generalized Petersen graphs uses a different predicate, and must not be confused with the present one.

## Limitations

The formula treats the standard Möbius ladders with \(n\ge2\) antipodal pairs, not arbitrary cubic circulants, prisms, or generalized Petersen graphs. Polynomial transfer computations establish exact symbolic identities but are not an independent peer review. The mathematical literature comparison supports originality provisionally, not guaranteed global historical priority. No claim about efficient domination, graph coloring, or the distinct \([1,2]\)-domination parameter is made.

## References

1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, A. Tepeh, *On k-limited domination in graphs*, arXiv:2606.22422 (first submitted 2026-06-21), https://arxiv.org/abs/2606.22422.
2. G. Radić, A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796 (first submitted 2026-10-01), https://arxiv.org/abs/2610.01796.
3. G. Radić, G. Radić, A. Tepeh, *Structural aspects of 1-limited domination in cubic graphs*, arXiv:2610.26259 (first submitted 2026-10-19), https://arxiv.org/abs/2610.26259.
4. L. Chen, Y. Ma, Y. Shi, Y. Zhao, *On the [1,2]-domination number of generalized Petersen graphs*, Applied Mathematics and Computation 327 (2018), 1–7, DOI:10.1016/j.amc.2018.01.013 (a distinct domination parameter).
