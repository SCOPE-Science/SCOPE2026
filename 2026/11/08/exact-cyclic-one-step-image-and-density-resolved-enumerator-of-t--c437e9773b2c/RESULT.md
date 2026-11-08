# Exact cyclic one-step image and density-resolved enumerator of traffic Rule 184

## Finding
For every integer \(n\ge1\), consider the binary cyclic ring \(\{0,1\}^{n}\), with positions labeled modulo \(n\). Let \(F\) be elementary cellular automaton Rule 184 and let \(G\) be its reflected traffic rule, Rule 226, defined by
\[
 F(x)_i=x_{i-1}(1-x_i)+x_i x_{i+1},\qquad
 G(x)_i=x_{i+1}(1-x_i)+x_i x_{i-1}.
\]
The two displayed summands never overlap, so these are binary operations. A word \(y\) belongs to the one-step image of \(F\) **if and only if** the cyclic length-four pattern `1100` does not occur in \(y\). In that case, \(G(y)\) is an explicit one-step predecessor:
\[
 F(\{0,1\}^n)=\{y:\text{cyclic `1100' is absent from }y\},
 \qquad F(G(y))=y\quad\text{for every }y\in F(\{0,1\}^n).
\]
In particular, \(F\circ G\circ F=F\) for all ring lengths, including \(n<4\).

Let \(a_{n,k}\) be the number of **indexed**, distinct reachable words of length \(n\) having exactly \(k\) ones. The complete density-resolved generating function is
\[
 \boxed{\sum_{n\ge1}\sum_{k=0}^{n}a_{n,k}z^nu^k
 =\frac{(1+u)z-4u^2z^4}{1-(1+u)z+u^2z^4}}.
\]
Equivalently, for every integer \(n\ge1\) and \(0\le k\le n\),
\[
 \boxed{a_{n,k}=\sum_{s=0}^{\min(\lfloor n/4\rfloor,\lfloor k/2\rfloor)}
 (-1)^s\frac{n}{n-3s}\binom{n-3s}{s}\binom{n-4s}{k-2s}},
\]
where binomial coefficients outside their natural ranges are zero. The total number \(a_n=\sum_k a_{n,k}\) has values
\[
 (a_1,\ldots,a_{12})=(2,4,8,12,22,40,72,132,242,444,816,1500).
\]
If \(\lambda=1.839286755214\ldots\) is the positive root of \(\lambda^3-\lambda^2-\lambda-1=0\), then \(a_n\sim\lambda^n\). The exact one-step output growth rate is therefore \(\log_2\lambda=0.879146421606\ldots\) bits per ring site.

## Assumptions and scope
All words are binary, rings have positive integer length, and coordinates are labeled rather than identified under cyclic rotations. Length-four cyclic factors at lengths below four are defined by repeated modulo-\(n\) indices. The map is a **single simultaneous update**, not a long-time attractor map; the image counts distinct output configurations, not preimage multiplicities. The formal variables \(z\) and \(u\) mark length and number of ones, respectively.

## Proof
**1. Necessary excluded pattern.** In the pair-state de Bruijn graph, an input triple \(abc\) is an edge from \(ab\) to \(bc\), labeled \(F(a,b,c)\). With pair states in order `00,01,10,11`, its two labeled adjacency matrices are
\[
 M_0=\begin{pmatrix}1&1&0&0\\0&0&1&0\\0&0&0&0\\0&0&1&0\end{pmatrix},\qquad
 M_1=\begin{pmatrix}0&0&0&0\\0&0&0&1\\1&1&0&0\\0&0&0&1\end{pmatrix}.
\]
Direct multiplication gives \(M_1M_1M_0M_0=0\). Hence no output word, even on an arbitrarily short cyclic ring with repeated coordinates, can exhibit four consecutive output symbols `1100`.

**2. Constructive sufficiency and exact section.** To compute \((F\circ G)(y)_i\), only the five source bits \((a,b,c,d,e)=(y_{i-2},y_{i-1},y_i,y_{i+1},y_{i+2})\) are needed. Substituting the two displayed local rules and checking the \(32\) possible five-bit patterns shows that \((F\circ G)(y)_i\ne c\) holds exactly for

`01100`, `11000`, `11001`, `11100`.

Every pattern on this list contains `1100` in one of its two length-four windows. Consequently, if cyclic `1100` is absent from \(y\), no coordinate of \(F(G(y))\) differs from \(y\), and \(F(G(y))=y\). Combining with Step 1 establishes both the complete one-step image characterization and the section identity \(FGF=F\). This argument uses only local identities and therefore covers \(n=1,2,3\) without an exception.

**3. Exact density-enumeration transfer matrix.** Index an eight-state graph by the triples `000,001,010,011,100,101,110,111`. A transition from `abc` to `bcd` has weight \(u^d\), except when `abcd=1100`, in which case it is absent. The resulting matrix, with the indicated state ordering, is
\[
 T(u)=\begin{pmatrix}
 1&u&0&0&0&0&0&0\\
 0&0&1&u&0&0&0&0\\
 0&0&0&0&1&u&0&0\\
 0&0&0&0&0&0&1&u\\
 1&u&0&0&0&0&0&0\\
 0&0&1&u&0&0&0&0\\
 0&0&0&0&0&u&0&0\\
 0&0&0&0&0&0&1&u
 \end{pmatrix}.
\]
Every length-\(n\) closed walk, even for \(n<3\), is uniquely an indexed cyclic binary word with no `1100`; its weight is \(u\) to its number of ones. Thus \(\sum_k a_{n,k}u^k=\operatorname{tr}(T(u)^n)\). A finite exact determinant calculation (reproducible in `verify.py`, using only integer polynomial operations) yields
\[
 D(z,u):=\det(I-zT(u))=1-(1+u)z+u^2z^4.
\]
The formal trace identity therefore gives
\[
 \sum_{n\ge1}\operatorname{tr}(T(u)^n)z^n
 =-z\frac{\partial}{\partial z}\log D(z,u)
 =\frac{(1+u)z-4u^2z^4}{D(z,u)}.
\]
Expanding \(-\log D=\sum_{m\ge1}((1+u)z-u^2z^4)^m/m\) and extracting the coefficient of \(z^nu^k\) after multiplying by \(z\partial_z\) gives precisely the finite binomial formula in the Finding. Each step is a formal-power-series identity, with no analytic convergence assumption.

**4. Entropy.** Setting \(u=1\) yields \(D(z,1)=(1-z)(1-z-z^2-z^3)\), so \(a_n=1+\lambda^n+\lambda_2^n+\lambda_3^n\), where \(\lambda_2,\lambda_3\) are the remaining roots of the tribonacci polynomial. Their moduli are smaller than \(\lambda\), proving \(a_n\sim\lambda^n\). This concludes the theorem.

## Verification
Run `python3 verify.py` using Python's standard library. It checks the exact four five-bit defects in Step 2, verifies the polynomial determinant in Step 3 by a separate coefficient-dictionary permutation expansion, verifies the zero product \(M_1^2M_0^2\), exhaustively compares all source images with cyclic `1100` avoiders for each \(1\le n\le16\), checks the explicit predecessor on each reachable output, and independently checks every coefficient in the displayed binomial formula across those lengths. All checks completed with `VERIFY_OK`. The finite tests are not substituted for Steps 1–4.

## Relationship to prior work
Fukś's 1997 treatment of Rule 184 established traffic-density dynamics and preimage enumeration for specific blocks, but does not report the full one-step cyclic output language or the length/weight output generating function. Schüle and Stoop (2011/2012), Section 6, explicitly observe that **any Rule-184 output containing `1100` is impossible**; Step 1 here is thus *already known*, while the reverse inclusion, explicit Rule-226 section, and exact weight-resolved cyclic image enumerator are the additional claims. Bilotta, Pergola, and Pinzani (2011) study enumerations for certain **linear** pattern-avoiding words; OEIS A008937 records the linear count for avoiding `1100`. Neither linear enumeration nor forbiddenness alone determines the cyclic, exact-weight Rule-184 image theorem.

Rodríguez Zamora and Chapa Vergara (2004) explicitly study Rule 184 using de Bruijn diagrams, making their work a close priority risk. Their abstract is accessible, but the ten-page original could not be inspected in full; accordingly this document does **not** claim their full text lacks the result. The stated comparisons support a qualified best-knowledge novelty assessment rather than independent priority certification.

## Limitations
Only the one-step image on indexed binary periodic rings is classified. The formulas do not count all inverse fibers, transient dynamics, attractors, or other traffic rules; they also do not directly count rotation classes (binary necklaces). The `1100` impossibility was documented previously, and a closely relevant 2004 de Bruijn study remains incompletely accessible; historical priority is not fully settled. Independent mathematical review has not been performed.

## References
1. H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, arXiv:comp-gas/9703001, first posted 1997-03-07, https://arxiv.org/abs/comp-gas/9703001.
2. N. Boccara and H. Fukś, *Cellular automaton rules conserving the number of active sites*, arXiv:adap-org/9712003, first posted 1997-12-12, https://arxiv.org/abs/adap-org/9712003.
3. M. Schüle and R. Stoop, *A Full Computation-relevant Topological Dynamics Classification of Elementary Cellular Automata*, arXiv:1107.2080, first posted 2011-07-11, especially Section 6, https://arxiv.org/abs/1107.2080.
4. R. Rodríguez Zamora and S. V. Chapa Vergara, *Using de Bruijn Diagrams to Analyze 1d Cellular Automata Traffic Models*, ACRI 2004, pp. 306–315, DOI:10.1007/978-3-540-30479-1_32, https://doi.org/10.1007/978-3-540-30479-1_32 (abstract inspected; full text unavailable).
5. S. Bilotta, E. Pergola and R. Pinzani, *Pattern \(1^j0^i\) Avoiding Binary Words*, arXiv:1108.3621, first posted 2011-08-18, https://arxiv.org/abs/1108.3621.
6. OEIS A008937, a classical linear `1100`-avoiding-word count, https://oeis.org/A008937.
