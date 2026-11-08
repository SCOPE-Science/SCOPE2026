# Joint rank fibers for commuting square-zero matrices in a maximal Jordan stratum

## Finding
Let \(q\) be any prime power, \(r\geq1\), and fix \(A\in M_{2r}(\mathbb F_q)\) with \(A^2=0\) and \(\operatorname{rank}A=r\). For integers \(s,b\), define the ordered-partner multiplicity
\[
H_{r,q}(s,b)=\#\{B\in M_{2r}(\mathbb F_q): B^2=0,\ AB=BA,\ \operatorname{rank}(AB)=s,\ \operatorname{rank}B=b\}.
\]
Write \(h=r-2s\), \(t=b-2s\), the Gaussian binomial coefficient \({a\brack c}_q\), and \(|\mathrm{GL}_0(\mathbb F_q)|=1\). The **complete joint rank distribution** is
\[
\boxed{ H_{r,q}(s,b)={r\brack s}_q {r-s\brack s}_q\, |\mathrm{GL}_s(\mathbb F_q)|\,q^{2s(r-s)}\, {h\brack t}_q\prod_{j=0}^{t-1}(q^h-q^j) }
\]
when \(0\leq s\leq\lfloor r/2\rfloor\) and \(0\leq t\leq h\); outside those ranges the multiplicity is zero. Empty products equal one. Thus all possible \(\operatorname{rank}(AB)\) and \(\operatorname{rank}B\) strata, including the annihilating locus, have explicit multiplicities. The answer is independent of the choice of \(A\) of Jordan type \((2^r)\).

There are exactly \({2r\brack r}_q|\mathrm{GL}_r(\mathbb F_q)|\) choices of such \(A\). Multiplying the displayed formula by this factor counts **ordered pairs** of square-zero matrices with the first factor of maximal rank and the specified joint ranks. In particular \(\sum_bH_{r,q}(0,b)=q^{r^2}\), and at \(r=2\) there are exactly \(q^2(q^2-1)\) partners with \(\operatorname{rank}(AB)=1\). For odd characteristic, \((A+B)^2=2AB\), so these positive-product-rank strata are precisely the commuting square-zero pairs whose sum has nilpotency index three (at least one such pair). In characteristic two, every such sum is square-zero.

## Assumptions and scope
The ground field is the full finite field \(\mathbb F_q\), for any prime-power \(q\) (including characteristic two); \(r\) is a positive integer. Only square-zero \(A\) of rank exactly \(r\) in dimension \(2r\) are fixed, and \(B\) ranges over *all* matrices with \(B^2=0\) commuting with \(A\). No rank condition on \(B\) beyond the displayed variable \(b\) is imposed. Gaussian coefficients are zero outside their normal integer ranges. The claim concerns labeled matrices, not simultaneous similarity orbits.

## Proof
Choose a basis in which
\[
A=\begin{pmatrix}0&I_r\\0&0\end{pmatrix}.
\]
Its centralizer consists precisely of
\[
B=\begin{pmatrix}X&Y\\0&X\end{pmatrix},\qquad X,Y\in M_r(\mathbb F_q).
\]
Direct multiplication gives \(AB=BA=\bigl(\begin{smallmatrix}0&X\\0&0\end{smallmatrix}\bigr)\) and
\(B^2=0\iff X^2=0\text{ and }XY+YX=0\). Hence \(\operatorname{rank}(AB)=\operatorname{rank}X=s\). This forces \(2s\leq r\).

Count the possible rank-\(s\) square-zero \(X\). Choose its image \(U\) of dimension \(s\), then its kernel \(K\) of dimension \(r-s\) containing \(U\), and finally the induced isomorphism \(\mathbb F_q^r/K\longrightarrow U\). These choices yield
\[
{r\brack s}_q{r-s\brack s}_q|\mathrm{GL}_s(\mathbb F_q)|.
\]
Write \(h=r-2s\), and split \(\mathbb F_q^r=U\oplus H\oplus T\) with \(\dim U=\dim T=s\), \(\dim H=h\), so that \(X\) maps \(T\) isomorphically onto \(U\) and vanishes on \(U\oplus H\). With respect to this ordered splitting, solving \(XY+YX=0\) gives **all** and only the matrices
\[
Y=\begin{pmatrix}D&P&Q\\0&E&R\\0&0&-D\end{pmatrix},
\]
where \(D\in M_s\), \(P\in M_{s\times h}\), \(Q\in M_s\), \(E\in M_h\), and \(R\in M_{h\times s}\), without further constraints. The four free blocks other than \(E\) contribute \(q^{2s^2+2sh}=q^{2s(r-s)}\) choices. The sign \(-D\) is valid also in characteristic two.

The rank of \(B\) is exactly \(2s+\operatorname{rank}E\). Indeed, \(B(u,v)=0\) requires \(Xv=0\) and \(Xu+Yv=0\). For \(v\in K=U\oplus H\), the second equation is solvable in \(u\) exactly when the \(H\)-component \(Ev_H\) vanishes; when solvable, \(u\) has \(\dim K=r-s\) free coordinates. If \(\operatorname{rank}E=t\), this yields
\[
\dim\ker B=(r-s)+(s+h-t)=2r-2s-t,
\]
so \(\operatorname{rank}B=2s+t\). The number of rank-\(t\) matrices \(E\in M_h(\mathbb F_q)\) is \({h\brack t}_q\prod_{j=0}^{t-1}(q^h-q^j)\). Multiplication of the independent counts proves the formula and shows there are no omitted cases.

Finally, the number of maximal-rank square-zero matrices \(A\in M_{2r}\) is obtained by choosing \(U=\operatorname{im}A=\ker A\) in \({2r\brack r}_q\) ways and an isomorphism from the quotient onto \(U\) in \(|\mathrm{GL}_r|\) ways. When \(s=0\), \(X=0\) and \(Y\) is arbitrary, giving \(q^{r^2}\) partners. For \(r=2,s=1\), the formula simplifies to \(q^2(q^2-1)\). The sum-index statement follows from \((A+B)^2=AB+BA=2AB\) and \((A+B)^3=0\) because \(A^2=B^2=0\), \(AB=BA\).

## Verification
The finite-field checks are reproducible using `check.cpp`, `full_enum.cpp`, and `formula.py`, with reference outputs `check_output.txt`, `full_output.txt`, and `formula_output.txt`. Compile the C++ programs with a C++17 compiler (for example, `c++ -O2 -std=c++17 check.cpp -o check` and `c++ -O2 -std=c++17 full_enum.cpp -o full_enum`), run them, and run `python3 formula.py`. They require no third-party packages.

`check.cpp` uses literal finite-field arithmetic (including an explicit quadratic extension for \(\mathbb F_4\)), multiplies each tested matrix \(B\) and verifies its commutator, square, and two ranks. It exhausts the relevant centralizer for the cases \((q,r)=(2,1),(2,2),(3,2),(4,2),(5,2),(2,3)\). `full_enum.cpp` separately inspects every one of the \(2^{16}\) binary \(4\times4\) matrices \(B\), without assuming a centralizer description, for one rank-two \(A\). `formula.py` computes the full integer formula and its support for these cases and tests larger integer parameter ranges. The observed reference outputs agree with the claimed formula. These finite computations are corroboration, not proof for all \(q,r\).

## Relationship to prior work
Kokol Bukovšek, Košir, Novak, and Oblak (2007) analyze **possible products** of commuting nilpotent transformations and establish a sharp rank restriction for products of square-zero matrices; the inequality \(\operatorname{rank}(AB)\leq r/2\) is consistent with that work. Their analysis does not give the present full finite-field multiplicities stratified jointly by both \(\operatorname{rank}(AB)\) and \(\operatorname{rank}B\). Britnell and Wildon (2010 preprint; 2011 journal) characterize commuting nilpotent similarity types but do not count these labeled refined fibers. Fulman and Guralnick (2016) give broad unrefined finite-field commuting-pair enumeration: the nilpotent-partner totals do not state the joint product-rank fibers. The full rank-stratified enumeration here is a refinement, not a new existence criterion.

## Limitations
No formula is claimed here for non-maximal-rank square-zero first factors, for arbitrary non-square-zero nilpotents, or for simultaneous similarity-orbit multiplicities. Historical priority has not received independent verification: a more general unlocated Hall-polynomial or commuting-module enumeration could imply this formula. Independent mathematical validation has not been performed.

## References
1. D. Kokol Bukovšek, T. Košir, N. Novak, P. Oblak, *Products of commuting nilpotent operators*, Electronic Journal of Linear Algebra 16 (2007), 237–247. DOI: `10.13001/1081-3810.1199`.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:`1001.0811`, first submitted 2010-01-06; Journal of the London Mathematical Society 83 (2011), 470–492.
3. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:`1611.05499` (2016).
4. N. Novak, *Sums of commuting square-zero transformations*, Linear Algebra and its Applications (2009), DOI: `10.1016/j.laa.2009.06.010` (abstract consulted, complete text not reviewed).
