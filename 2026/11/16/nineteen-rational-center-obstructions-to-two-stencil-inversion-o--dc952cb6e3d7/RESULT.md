# Nineteen rational-center obstructions to two-stencil inversion on rectangular tori

## Finding

Two natural five-point lattice convolutions—a coordinate cross and a diagonal cross—have a complete simultaneous information-loss classification when their center gains are rational. Across **every** rectangular torus \(\mathbb Z_m\times\mathbb Z_n\), \(m,n\ge3\), only nineteen gain pairs can produce a nontrivial common kernel: fifteen integer pairs from rational cosine values and four further, intrinsically quadratic pairs. For each pair and each pair of torus lengths, the exact kernel dimension is given below. Outside these nineteen pairs, the joint unsampled two-output analysis map is injective for every such torus. All nineteen exceptional pairs occur for some torus.

The classification is a statement about the *common kernel* of two finite convolutions; it does not claim perfect reconstruction after downsampling, nor does it give uniform stability as torus sizes vary.

## Assumptions and scope

Let \(m,n\ge3\) be integers, \(G=\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\), and \(\alpha,\beta\in\mathbb Q\). For each complex-valued function \(f\colon G\to\mathbb C\), define (all subscripts are reduced modulo \(m,n\))

\[
\begin{aligned}
(A_\alpha f)_{j,k}&=\alpha f_{j,k}+f_{j+1,k}+f_{j-1,k}+f_{j,k+1}+f_{j,k-1},\\
(B_\beta f)_{j,k}&=\beta f_{j,k}+f_{j+1,k+1}+f_{j+1,k-1}+f_{j-1,k+1}+f_{j-1,k-1},\\
\mathcal T_{\alpha,\beta}f&=(A_\alpha f,B_\beta f).
\end{aligned}
\]

Thus \(\mathcal T_{\alpha,\beta}\colon\mathbb C^{mn}\to\mathbb C^{2mn}\) has two full-resolution output channels. Let \(R=\{-2,-1,0,1,2\}\) and

\[
\mathcal E_{\rm rat}=\{(-(u+v),-uv):u,v\in R,\ u\le v\},\qquad
\mathcal E_{\rm quad}=\{(1,1),(-1,1),(0,2),(0,3)\}.
\]

The sets are disjoint, \(|\mathcal E_{\rm rat}|=15\) and \(|\mathcal E_{\rm quad}|=4\). In explicit order the fifteen rational-family pairs \((\alpha,\beta)\) are

\[
\begin{gathered}
(4,-4),(3,-2),(2,0),(1,2),(0,4),\\
(2,-1),(1,0),(0,1),(-1,2),(0,0),\\
(-1,0),(-2,0),(-2,-1),(-3,-2),(-4,-4).
\end{gathered}
\]

Define \(c_q(s)=\#\{a\in\{0,\ldots,q-1\}:2\cos(2\pi a/q)=s\}\) for each positive integer \(q\ge3\) and \(s\in R\). Its complete explicit form is

\[
\begin{array}{c|ccccc}
s&-2&-1&0&1&2\\ \hline
c_q(s)&\mathbf1_{2\mid q}&2\mathbf1_{3\mid q}&2\mathbf1_{4\mid q}&2\mathbf1_{6\mid q}&1.
\end{array}
\]

**Theorem (exact common-kernel classification).** For \((\alpha,\beta)\notin\mathcal E_{\rm rat}\cup\mathcal E_{\rm quad}\), the common kernel is zero for all \(m,n\ge3\). For \((\alpha,\beta)=(-(u+v),-uv)\in\mathcal E_{\rm rat}\), with \(u\le v\) in \(R\), the exact complex kernel dimension \(K\) is

\[
K=\begin{cases}
c_m(u)c_n(v),&u=v,\\
c_m(u)c_n(v)+c_m(v)c_n(u),&u<v.
\end{cases}
\]

For the four quadratic pairs the exact nullities are, respectively,

\[
\begin{array}{c|c|c}
(\alpha,\beta)&\text{required common divisor }q&K\\ \hline
(1,1)&5&8\mathbf1_{q\mid m}\mathbf1_{q\mid n}\\
(-1,1)&10&8\mathbf1_{q\mid m}\mathbf1_{q\mid n}\\
(0,2)&8&8\mathbf1_{q\mid m}\mathbf1_{q\mid n}\\
(0,3)&12&8\mathbf1_{q\mid m}\mathbf1_{q\mid n}.
\end{array}
\]

Always \(\operatorname{rank}_{\mathbb C}\mathcal T_{\alpha,\beta}=mn-K\). These are sharp formulas including all divisibility boundaries; no genericity assumption on \(\alpha,\beta\) beyond rationality is made.

## Proof

**1. Simultaneous Fourier diagonalization.** For \(0\le a<m\) and \(0\le b<n\), the character \(\chi_{a,b}(j,k)=\exp(2\pi i(aj/m+bk/n))\) is an eigenvector of each convolution. Write \(u_a=2\cos(2\pi a/m)\) and \(v_b=2\cos(2\pi b/n)\). Direct substitution yields

\[
A_\alpha\chi_{a,b}=(\alpha+u_a+v_b)\chi_{a,b},\qquad
B_\beta\chi_{a,b}=(\beta+u_av_b)\chi_{a,b}.
\]

Consequently \(\chi_{a,b}\) belongs to the joint kernel if and only if

\[
u_a+v_b=-\alpha,\qquad u_av_b=-\beta.\tag{1}
\]

All \(mn\) characters form a basis. Thus the complex nullity is precisely the number of pairs \((a,b)\) satisfying (1).

**2. Arithmetic rigidity for rational gains.** Each \(u_a=\zeta+\zeta^{-1}\) and \(v_b=\eta+\eta^{-1}\) is an algebraic integer. By (1) their sum and product are rational algebraic integers, hence integers: \(\alpha,\beta\in\mathbb Z\). Both scalars solve the same monic quadratic

\[
t^2+\alpha t-\beta=0.\tag{2}
\]

If this polynomial is reducible over \(\mathbb Q\), both scalars are rational algebraic integers, hence ordinary integers. Since \(u_a,v_b\in[-2,2]\), both lie in \(R\). Equation (1) gives exactly the fifteen pairs in \(\mathcal E_{\rm rat}\), which are distinct by their sum and product. The displayed \(c_q\) formula follows from the exact root orders: \(s=2,-2,-1,0,1\) respectively corresponds to roots of exact orders \(1,2,3,4,6\). Counting the independent positions in each coordinate proves the rational-family nullity formula, with the second term only when the roots differ.

Otherwise (2) is an irreducible quadratic, so \(u_a,v_b\) must be distinct Galois conjugates of degree exactly two over \(\mathbb Q\). For a root of unity \(\zeta\) of exact order \(q\), the standard real-cyclotomic degree is \([\mathbb Q(\zeta+\zeta^{-1}):\mathbb Q]=\varphi(q)/2\) for \(q\ge3\), and degree one for \(q=1,2\). The only positive integers with \(\varphi(q)=4\) are \(q=5,8,10,12\). Their minimal polynomials for twice the cosine are, in that order,

\[
t^2+t-1,\quad t^2-2,\quad t^2-t-1,\quad t^2-3.\tag{3}
\]

Comparing (2) and (3) gives exactly the four stated quadratic gain pairs with orders \(5,8,10,12\), respectively. In each case both coordinate scalar values have the *same exact primitive root order* \(q\), and each of the two conjugate scalar values occurs at exactly two character frequencies when \(q\mid m\) or \(q\mid n\), and never otherwise. Therefore there are \(2\cdot2\cdot2=8\) ordered frequency pairs precisely when the displayed order divides both \(m\) and \(n\), proving the four formulas.

**3. Exhaustiveness and realization.** Every joint kernel character is covered by either the rational or irreducible quadratic case. Conversely all fifteen rational gain pairs are realized by selecting coordinate lengths divisible by the required orders in \(\{1,2,3,4,6\}\), and all four quadratic pairs by taking \(m=n=q\) at the corresponding order \(q\). Completeness of the Fourier basis now gives the rank identity.

## Verification

The standalone file `verify_two_stencils.py` constructs the nineteen gain pairs and their predicted nullities. It checks all \(12^2=144\) grids with \(3\le m,n\le14\) using exact cyclotomic polynomial reductions over \(\mathbb Z\): for each Fourier character, it derives \(\alpha,\beta\) as algebraic elements and tests exact rationality before comparing the resulting complete gain-pair census. It also performs \(58^2\cdot19=63{,}916\) supplemental floating-point Fourier checks for \(3\le m,n\le60\). Run from the artifact directory using `python verify_two_stencils.py` (Python, NumPy, SymPy).

The exact tests certify only the stated finite grids. The unbounded theorem depends on the arithmetic degree argument above, not on finite enumeration or floating-point tolerances.

## Relationship to prior work

Classical cyclotomic real-subfield degrees and integer-valued algebraic-integer facts supply the arithmetic proof. Christie, Dykema and Klep (arXiv:2008.11268; public August 25, 2020) systematically classify vanishing root-of-unity sums, a more general arithmetic setting. The present theorem does **not** assert a new cyclotomic degree result; it classifies the *intersection of the Fourier zero sets for two specified unsampled two-dimensional stencils*, all rational center gains, and exact rectangular-torus multiplicities.

You and Yang (arXiv:2210.02024; first public October 5, 2022) analyze perfect reconstruction in **downsampled graph filter banks** through generalized samplers and synthesis conditions. Those results address a different measurement model and do not provide the nineteen-pair arithmetic table or joint-kernel counts above. General Fourier diagonalization of toroidal graph adjacency yields each single-filter symbol but not, by itself, the full rational-gain common-zero and multiplicity classification. Specialized earlier literature may have an equivalent formula; see limitations.

## Limitations

Only the exact pair of axial/diagonal five-point stencils, with common unit off-center weights and rational center gains, is treated. The output channels are **not downsampled**, so comparison with critically sampled filter banks requires care. The theorem establishes injectivity and ranks, not a uniform lower singular-value bound, noise robustness, optimal parameter choice, or uniqueness within a broader stencil class. The underlying cyclotomic facts are classical; the claim of originality is restricted to the explicit, complete joint-stencil classification. A historical-priority search cannot exclude every older source. No external or independent mathematical audit has been performed.

## References

1. L. Christie, K. J. Dykema and I. Klep, *Classifying minimal vanishing sums of roots of unity* (2020), arXiv:2008.11268, https://arxiv.org/abs/2008.11268.
2. J. You and L. Yang, *Perfect Reconstruction Two-Channel Filter Banks on Arbitrary Graphs* (2022), arXiv:2210.02024, https://arxiv.org/abs/2210.02024.
3. J. H. Conway and A. J. Jones, *Trigonometric Diophantine equations (On vanishing sums of roots of unity)* (1976), *Acta Arithmetica* 30, 229–240 (classical background).
