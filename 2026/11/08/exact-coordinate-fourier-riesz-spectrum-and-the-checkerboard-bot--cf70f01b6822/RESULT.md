# Exact coordinate-Fourier Riesz spectrum and the checkerboard bottleneck on the finite-field Segre cone

## Finding
For any prime power \(q\ge2\), let \(C\) be the affine cone of decomposable tensors in \(V=(\mathbb F_q^2)^{\otimes3}\), **including zero**, with uniform probability measure. Restrict the constant character and the \(8(q-1)\) nontrivial one-coordinate additive characters to \(C\). The resulting \(1+8(q-1)\) functions are linearly independent and their normalized Gram operator has a complete explicit spectrum as follows.

Set \(D=q^3+2q^2-2\),
\[
 a=\frac{2(q^2-1)}{D},\quad
 \mu_0=\frac{12q^3-10q^2-17q+16}{D},\quad
 h=a\sqrt{8(q-1)},\quad
 L_\pm=\frac{1+\mu_0\pm\sqrt{(1-\mu_0)^2+4h^2}}2.
\]
Then the eigenvalues and multiplicities are

| Eigenvalue | Multiplicity |
| :--- | ---: |
| \(L_+\) | \(1\) |
| \(L_-\) | \(1\) |
| \(q(2q-1)^2/D\) | \(3\) |
| \(q(2q-1)/D\) | \(3\) |
| \(q/D\) | \(1\) |
| \(q^3/D\) | \(8(q-2)\) |

The last row is absent when \(q=2\). Coincident numerical levels, if any, are combined with their multiplicities. The **sharp lower Riesz bound**, uniquely attained, is
\[
\boxed{\lambda_{\min}=\frac q{q^3+2q^2-2}.}
\]
The corresponding coefficient vector is the checkerboard pattern \((-1)^{i+j+k}\), constant across nonzero character labels, with zero constant-character coefficient. The **sharp upper bound** is \(L_+\), attained on its uniquely determined constant/uniform character mixture. Therefore the optimal squared Riesz condition number is \(L_+D/q\), with the exact asymptotic \(\boxed{L_+D/q\sim12q^2}\) as \(q\to\infty\) through prime powers.

## Assumptions and scope
Let \(\psi:\mathbb F_q\to\mathbb C^\times\) be any nontrivial additive character. The eight coordinates of a tensor are indexed by \(e=(i,j,k)\in\{0,1\}^3\). Denote by \(x_e\) the corresponding tensor coordinate, and define
\[
\mathcal F=\{1\}\cup\{\psi(t x_e):e\in\{0,1\}^3,\ t\in\mathbb F_q^\times\}.
\]
The Gram matrix has entries \(G_{f,g}=|C|^{-1}\sum_{x\in C}f(x)\overline{g(x)}\). Coefficient vectors use the standard Euclidean norm. The Riesz bounds refer to the precise equal-weight character family above (not a full Fourier basis, a random sample, or the punctured projective Segre variety).

## Proof
**Character averages.** Every nonzero decomposable tensor has exactly \((q-1)^2\) preimages as an ordered nonzero triple, whence \(|C|=1+(q-1)(q+1)^3=qD\). For a trilinear frequency tensor \(\xi\), write its pencil of \(2\)-by-\(2\) slices as \(sA+tB\). If \(a_0\) and \(b_1\) are the numbers of directions \([s:t]\in\mathbb P^1(\mathbb F_q)\) having matrix ranks zero and one, the standard nontrivial additive-character orthogonality identity
\[
\sum_{u,v\in\mathbb F_q^2}\psi(u^{\mathsf T}Mv)=q^{4-\operatorname{rank}M}
\]
followed by removal of zero vectors and division by the scalar-triple multiplicity yields
\[
\sum_{x\in C}\psi(\langle\xi,x\rangle)
=q^2\bigl((q+1)a_0+b_1\bigr)-q(q+2).
\]
If \(\xi\) is a nonzero scalar multiple of a single coordinate frequency, its pencil rank profile is \((1,q)\), so the normalized average is
\[
 a=\frac{2q(q^2-1)}{|C|}=\frac{2(q^2-1)}D.
\]
If \(\xi\) is the sum of nonzero coordinate frequencies at two positions of Hamming distance two, it is a matrix of rank two with one shared factor, and has rank profile \((1,0)\); the average is \(b=(q^2-2)/D\). If the two coordinates have Hamming distance three, the pencil consists of two independent diagonal rank-one matrices and has profile \((0,2)\); its average is \(c=(q-2)/D\). Distance-one pairs, and two distinct labels at the same coordinate, again have average \(a\). All formulas remain valid in characteristic two. The constant has inner product \(a\) with every nonconstant character.

**Gram reduction.** On each coordinate, the \(q-1\) nontrivial character labels split into their uniform sum and a \((q-2)\)-dimensional orthogonal contrast space. Every label contrast has eigenvalue \(1-a=q^3/D\). On the eight coordinate-uniform directions, the remaining block is
\[
H_{\rm cube}=(1+(q-2)a)I_8+(q-1)(aA_1+bA_2+cA_3),
\]
where \(A_r\) connects the vertices of the three-dimensional Hamming cube at distance \(r\). The Hamming characters indexed by a subset of \(\{1,2,3\}\) of cardinality \(d\) have eigenvalues \(3-2d\), \(((3-2d)^2-3)/2\), and \((-1)^d\) for \(A_1,A_2,A_3\), respectively. Substituting the exact averages gives the four levels
\[
\mu_0=\frac{12q^3-10q^2-17q+16}{D},\quad
\mu_1=\frac{q(2q-1)^2}{D},\quad
\mu_2=\frac{q(2q-1)}{D},\quad
\mu_3=\frac qD
\]
with multiplicities \(1,3,3,1\). The constant character couples only to the cube's uniform mode, with coupling \(h=a\sqrt{8(q-1)}\). The associated symmetric \(2\)-by-\(2\) matrix \(\left(\begin{smallmatrix}1&h\\h&\mu_0\end{smallmatrix}\right)\) gives \(L_\pm\). This proves the full spectrum and its multiplicities.

**The unique sharp least mode.** The displayed values give \(\mu_1>\mu_2>\mu_3>0\), and \(q^3/D>q/D\) for all \(q\ge2\). Also \(\mu_0>\mu_1\), because
\[
D(\mu_0-\mu_1)=2(q-1)(4q^2+q-8)>0.
\]
To compare \(L_-\) with \(\mu_3\), observe \(1-\mu_3>0\) and
\[
\det\left(\begin{pmatrix}1&h\\h&\mu_0\end{pmatrix}-\mu_3 I\right)
=\frac{6q(q-1)^2(q+1)(2q^2-q-2)}{D^2}>0.
\]
Sylvester's criterion gives \(L_->\mu_3\); hence the unique smallest eigenvalue is \(\mu_3=q/D\), and its coefficient vector is precisely the cube-parity character in the coordinate-uniform sector. Moreover \(\mu_0>\mu_1\) and \(\mu_0>q^3/D\); since \(h>0\), \(L_+>\max(1,\mu_0)\) and it is the unique largest eigenvalue. The positive least eigenvalue proves linear independence and exact equality modes. Finally \(\mu_0\to12\), \(h\to0\), and \(D/q\sim q^2\), so the squared condition number is asymptotic to \(12q^2\).

## Verification
The bundled `checks/verify.py` constructs the complete affine Segre cone from all nonzero tensor-product triples for \(q=2,3,4,5\), evaluates every listed restricted additive character directly on every point, builds the full complex Gram matrix, and checks every eigenvalue and multiplicity against the symbolic table. It also verifies the checkerboard eigenvector and positivity. The \(q=4\) test uses explicit \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\) arithmetic and field-trace characters. All checks passed. Finite computation is corroboration, not the proof of the all-prime-power statement.

## Relationship to prior work
Lavrauw and Sheekey's 2012 work classifies finite-field projective orbits for the same \(2\times2\times2\) Segre tensor variety, but not this restricted Fourier-character Gram spectrum. Byrne and François (2026) derive a general additive Cayley-graph eigenvalue formula for rank-one tensors, which supplies character averages in principle; its subject is the **full graph adjacency spectrum**, not the sharp Riesz frame formed by the constant and all one-coordinate Fourier characters, and it does not identify the cube-parity bottleneck or sharp \(12q^2\) squared conditioning law. Related exact coordinate-Fourier spectra on finite-field Plücker and ordinary rank-one matrix varieties address different underlying sampling spaces, with Johnson or rook geometry instead of the three-dimensional Hamming cube. Known character orthogonality, matrix-pencil ranks and cube spectra are acknowledged ingredients.

## Limitations
The theorem concerns a specific \(1+8(q-1)\)-column family and the full affine \(2\times2\times2\) Segre cone. It does not classify arbitrary coordinate subsets, optimal weights, or higher-format Segre cones. It is not an independent audit or a proof of historical uniqueness; an unlocated equivalent treatment of Segre-coordinate sampling is a priority risk. All-q correctness rests on the algebraic proof, not the four tested fields.

## References
1. M. Lavrauw and J. Sheekey, “Orbits of the stabiliser group of the Segre variety product of three projective lines,” arXiv:1207.3972, first posted 17 July 2012, https://arxiv.org/abs/1207.3972 .
2. E. Byrne and L. François, “The multilinear forms Cayley graph and the eigenvalue method for tensor codes,” arXiv:2607.03479, first posted 3 July 2026, https://arxiv.org/abs/2607.03479 .
3. M. Lavrauw and J. Sheekey, “Canonical forms of 2×3×3 tensors over the real field, algebraically closed fields, and finite fields,” arXiv:1411.5910 (2014), https://arxiv.org/abs/1411.5910 .
