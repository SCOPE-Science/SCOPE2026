# The dyadic symbol-pair generation filtration of binary second-order Reed–Muller codes

## Finding
Fix an integer \(m\ge3\), put \(n=2^m\), and evaluate the binary code \(C=\operatorname{RM}(2,m)\) in numerical order \(0,1,\ldots,n-1\), with coordinate \(t\) corresponding to the binary digits \((x_0,\ldots,x_{m-1})\) of \(t=\sum_{i=0}^{m-1}2^i x_i\). Indices in the symbol-pair metric wrap cyclically. For an integer \(\alpha\ge0\), set
\[
H_\alpha=\operatorname{span}_{\mathbb F_2}\{c\in C:0<w_p(c)\le\alpha\},\qquad \gamma_m(\alpha)=\dim H_\alpha.
\]
For \(0\le j\le m-3\), let \(C_j\) be the subcode obtained by evaluating all Boolean polynomials of degree at most two in only \(x_j,\ldots,x_{m-1}\). Write \(T_j=2^{m-2}+2^{m-j-3}\). Then, as an equality of **subcodes** rather than only their dimensions,
\[
H_\alpha=\begin{cases}
\{0\},&0\le\alpha<T_{m-3},\\
C_j,&T_j\le\alpha<T_{j-1},\quad 1\le j\le m-3,\\
C_0,&\alpha\ge T_0,
\end{cases}
\]
where the middle line is empty when \(m=3\). Equivalently, the successive nonzero generation dimensions are
\[
7,\ 11,\ 16,\ 22,\ \ldots,\ 1+m+\binom m2,
\]
at thresholds \(2^{m-2}+1,\ 2^{m-2}+2,\ 2^{m-2}+4,\ldots,\ 3\cdot2^{m-3}\), with the finite sequence stopped at the term for \(m\). In particular the \(\alpha\)-pair-distance graph of \(C\) first becomes connected at \(\alpha=3\cdot 2^{m-3}\), and its last disconnected integer radius is \(3\cdot2^{m-3}-1\). At any \(\alpha\), its number of components is \(2^{k-\gamma_m(\alpha)}\), where \(k=1+m+\binom m2\).

## Assumptions and scope
The field is \(\mathbb F_2\); all dimensions are binary dimensions. The code is the full second-order Reed–Muller evaluation code, not its homogeneous subcode. The exact numerical ordering, including the convention that \(x_0\) is the least-significant bit, is essential because pair weight changes under arbitrary coordinate permutations. For \(c=(c_0,\ldots,c_{n-1})\), the cyclic pair weight is
\[
w_p(c)=\left|\{t\bmod n:(c_t,c_{t+1})\ne(0,0)\}\right|.
\]
A nonzero proper binary support has \(w_p(c)=w_H(c)+r(c)\), where \(r(c)\) is its number of maximal cyclic runs of ones. The all-one vector has pair weight \(n\), and is not used in the minimum-weight argument. The theorem holds for all integers \(\alpha\ge0\); when \(\alpha\ge n\), the graph is automatically complete.

## Proof
**1. Hamming gap and minimum supports.** For a Boolean polynomial \(f\) of degree at most two, let \(B_f(u,v)=f(u+v)+f(u)+f(v)+f(0)\). This is alternating bilinear of even rank \(r\). Write \(W_f=\sum_{x\in\mathbb F_2^m}(-1)^{f(x)}\). Orthogonality gives
\[
W_f^2=n\sum_{h\in\operatorname{rad}B_f}(-1)^{f(h)+f(0)}.
\]
The exponent is a linear functional on the radical. Hence either \(W_f=0\), or \(|W_f|=2^{m-r/2}\); in rank zero, \(f\) is affine. Thus each nonzero word has Hamming weight at least \(n/4\), and a weight strictly above \(n/4\) must be at least \(3n/8\). A word of weight exactly \(n/4\) has polar rank two, and the nonvanishing Walsh sum forces its restriction to the radical to be constant. In suitable affine coordinates its defining function is \(u v\), so its support is an affine codimension-two flat, the simultaneous solution of two independent affine linear constraints. This characterizes *all* minimum supports. The same conclusion also follows from the classical minimum-weight theorem for Reed–Muller codes.

Since every proper nonempty support has at least one cyclic run, the minimum pair weight is at least \(n/4+1\). We next construct words attaining this and all higher claimed thresholds.

**2. A run lower bound detects low-order bits.** Suppose \(c\) has minimum Hamming weight \(n/4\), so its support is an affine codimension-two flat. Let \(\ell\) be the smallest index of a variable on which its indicator depends essentially. It is constant on each aligned block of \(2^\ell\) consecutive numerical coordinates. In each adjacent pair of such blocks, only the bit \(x_\ell\) changes, with other bits fixed; at most one of the two blocks can be included, because the indicator changes under this flip (the vector of the two affine constraints evaluated at the unit vector \(e_\ell\) is nonzero). Therefore a cyclic run occupies at most two such blocks. There are \(2^{m-2}\) occupied coordinates, so, whenever \(\ell\le m-3\),
\[
r(c)\ge \frac{2^{m-2}}{2^{\ell+1}}=2^{m-\ell-3}.
\]
For \(j\ge1\) and \(w_p(c)\le T_j\), a nonzero \(c\) cannot have Hamming weight above \(n/4\): the next Hamming weight is at least \(3n/8\ge T_j\), and a proper support adds at least one to its pair weight. If its least essential bit were \(\ell<j\), the displayed run bound would give \(w_p(c)\ge n/4+2^{m-j-2}>T_j\). Therefore every generator of \(H_{T_j}\) belongs to \(C_j\). In particular \(H_{T_j}\subseteq C_j\) for each \(1\le j\le m-3\). The inclusion for \(j=0\) is automatic.

**3. The first layer.** Divide the numerical cycle into eight aligned blocks of size \(2^{m-3}\). For each of the eight choices of two cyclically consecutive blocks, take their union. The indicator is a minimum-weight codeword: in the top three bits, any two distinct points constitute an affine line, and the remaining lower bits are unrestricted. Each indicator has exactly one cyclic run and hence pair weight \(T_{m-3}=n/4+1\). The eight adjacent-edge incidence vectors on a cycle of length eight span the binary even-weight subspace of \(\mathbb F_2^8\), of dimension seven. This is exactly the evaluation of \(\operatorname{RM}(2,3)\), since the degree-at-most-two polynomials on three bits have dimension seven and even total parity. Consequently \(H_{T_{m-3}}=C_{m-3}\).

**4. Each lower bit creates one sharp layer.** Induct downward on \(j\), taking \(0\le j\le m-4\) and assuming \(C_{j+1}\subseteq H_{T_{j+1}}\). For each \(i\in\{j+2,\ldots,m-1\}\) and \(b\in\mathbb F_2\), consider
\[
f_{i,b}(x)=(x_j+x_{j+1})(x_i+b).
\]
Divide the numerical cycle into blocks of \(2^{j+2}\) positions. Within each block where \(x_i+b=1\), the indicator follows the four-block pattern \(0110\), each digit denoting one block of size \(2^j\); the other larger blocks contain only zeros. There are exactly \(2^{m-j-3}\) selected larger blocks, each contributing one run of length \(2^{j+1}\). Thus every such word has Hamming weight \(n/4\) and pair weight \(T_j\).

Also consider the degree-two function
\[
g_j(x)=1+x_j+x_{j+1}+x_{j+2}+x_jx_{j+1}+x_jx_{j+2}+x_{j+1}x_{j+2}.
\]
It is the indicator that the triple \((x_j,x_{j+1},x_{j+2})\) is either \((0,0,0)\) or \((1,1,1)\). In each period of eight size-\(2^j\) blocks, the first and last blocks are occupied; they join across successive period boundaries. Thus it too has weight \(n/4\), exactly \(2^{m-j-3}\) cyclic runs, and pair weight \(T_j\).

Modulo \(C_{j+1}\), the words \(f_{i,b}\) span the independent classes of \(x_j\) and \(x_jx_i\) for every \(i\ge j+2\): varying \(b\) separates the affine and bilinear terms. The word \(g_j\) has a nonzero \(x_jx_{j+1}\) coefficient and supplies the one missing class. These are exactly the \(m-j\) basis classes of \(C_j/C_{j+1}\), since the new monomials are \(x_j\) and \(x_jx_i\), \(i>j\). Since \(T_{j+1}<T_j\), the induction yields \(C_j\subseteq H_{T_j}\). Combined with Step 2, equality holds at every \(T_j\).

**5. No intermediate jumps.** Below \(n/4+1\), there are no nonzero generators. Between successive thresholds, the Hamming gap and the run lower bound in Step 2 force every generator into the already attained \(C_j\), so the span cannot increase. Above \(T_0=3n/8\) the span is already \(C_0=C\). This proves the entire subcode filtration. Its dimensions follow from the monomial basis, and the graph component formula is the elementary Cayley-graph coset statement. \(\square\)

## Verification
Run `python3 check.py` using the embedded standalone Python file. It constructs the actual evaluation vectors in numerical order and computes cyclic pair weights directly. It exhaustively enumerates all \(2^7-1\), \(2^{11}-1\), and \(2^{16}-1\) nonzero codewords at \(m=3,4,5\), respectively, verifying the full generation profile at every integer radius (67,709 words total). It also constructs the displayed inductive generators and checks pair weights and ranks for all \(3\le m\le8\). The finite tests are corroboration; the all-length theorem follows from the proof above, not from finite enumeration.

## Relationship to prior work
Singh and Singh (2026) define the symbol-pair generation profile and identify Cayley-graph connected components with cosets of the low-pair-weight span; their general formulas do not specialize to a full dyadic filtration for second-order Reed–Muller codes. Li (2019), following Sloane and Berlekamp (1970), establishes the ordinary Hamming weight spectrum of second-order Reed–Muller codes, including the gap needed in Step 1, but Hamming weight does not determine cyclic pair weights under a specified coordinate order. The present proof identifies the exact generating **subcodes**, all jumps, and the sharp connectedness threshold under numerical evaluation order.

## Limitations
The result does not cover arbitrary coordinate permutations, other Reed–Muller orders, nonbinary fields, or noncyclic (nonwrapping) pair metrics. It relies on the classical rank-two structure of binary quadratic forms, but independently derives the run obstruction and spanning construction. The independent mathematical audit and definitive priority determination remain unperformed.

## References
1. A. Singh and A. K. Singh, *Data Protection in Function-Correcting Symbol-Pair Codes: Redundancy Bounds and Protection Profiles*, arXiv:2609.10989, first publicly available 2026-09-10. https://arxiv.org/abs/2609.10989
2. S. Li, *On the weight distribution of second order Reed-Muller codes and their relatives*, arXiv:1903.08058, 2019. https://arxiv.org/abs/1903.08058
3. N. J. A. Sloane and E. R. Berlekamp, *Weight enumerator for second-order Reed–Muller codes*, IEEE Transactions on Information Theory 16 (1970), 745–751. https://doi.org/10.1109/TIT.1970.1054553
4. Y. Cassuto and M. Blaum, *Codes for symbol-pair read channels*, IEEE Transactions on Information Theory 57 (2011), 8011–8020. https://doi.org/10.1109/TIT.2011.2164891
