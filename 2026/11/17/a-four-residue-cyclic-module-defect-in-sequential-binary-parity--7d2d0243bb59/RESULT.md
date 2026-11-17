# A four-residue cyclic-module defect in sequential binary parity dynamics on wheels

## Finding

Let \(W_{n+1}=K_1\vee C_n\) have hub \(h\) and cyclically ordered rim vertices \(v_1,\ldots,v_n\), where \(n\ge4\). Over \(\mathbb F_2\), let \(F_n\) update the hub once and then \(v_1,\ldots,v_n\) once each; a vertex's new bit is the XOR of its current bit and the current bits of all its graph neighbors. Define

\[
P_n(z)=z^{n+1}+1+\sum_{j=3}^{n-2}z^j+\epsilon_n(z^n+z),\qquad
\epsilon_n=\begin{cases}1&n\equiv0,3\pmod4,\\0&n\equiv1,2\pmod4.\end{cases}
\]

(The sum is empty when \(n=4\).) The characteristic polynomial of \(F_n\) is exactly \(P_n\). Its \(\mathbb F_2[z]\)-module, with \(z\) acting as \(F_n\), is

\[
\mathbb F_2[z]/(P_n) \quad\text{when }4\nmid n,
\qquad
\mathbb F_2[z]/(z+1)\oplus\mathbb F_2[z]/(z+1)
\oplus\mathbb F_2[z]/\bigl(P_n/(z+1)^2\bigr)\quad\text{when }4\mid n.
\]

In particular, the sweep is cyclic as a linear operator except precisely at rim lengths divisible by four. Every configuration is immediately periodic. Set \(R_n=P_n\) and \(b_n=0\) when \(4\nmid n\); set \(R_n=P_n/(z+1)^2\) and \(b_n=2\) otherwise. For each integer \(d\ge1\), the exact number of configurations fixed after \(d\) sweeps is

\[
Q_n(d)=2^{\,b_n+\deg\gcd_{\mathbb F_2[z]}(R_n,z^d+1)}.
\]

Consequently, the number of configurations with **primitive** period \(d\) is \(\sum_{e\mid d}\mu(d/e)Q_n(e)\), and the number of distinct primitive \(d\)-cycles is that quantity divided by \(d\). These formulas are valid for *every* \(n\ge4\) and *every* \(d\ge1\), without a finite-period cutoff. The polynomials \(P_n\) are reciprocal. For example, the five-rim wheel has one fixed configuration and seven nine-cycles, whereas the eight-rim wheel has eight fixed configurations, eight three-cycles, twenty-four five-cycles, and twenty-four fifteen-cycles.

## Assumptions and scope

All arithmetic is in \(\mathbb F_2\). The wheel has \(n+1\) vertices, with \(n\) on the rim, and no loops; in particular the hub is distinct from the rim. The update includes the current bit of the vertex itself (self-inclusive parity), and is sequential rather than synchronous. The specific ordered sweep is hub, then rim vertices in cycle order; the theorem does not claim the same spectra for every permutation of the vertices. An orbit's least period counts *complete sweeps*, not individual vertex updates. No probability model is needed for the counting theorem.

## Proof

**1. The characteristic determinant.** Each single-vertex update is an involutory linear shear, so the sweep \(F_n\) is invertible. Let \(A=L+U\) be the symmetric zero-diagonal adjacency matrix for the order \((h,v_1,\ldots,v_n)\), with \(L\) strictly lower triangular and \(U\) strictly upper triangular. The equations of one sequential sweep are \((I+L)y=(I+U)x\). Therefore

\[
\det(zI-F_n)=\det\bigl((z+1)I+zL+U\bigr).
\]

To compute this determinant, write the hub coordinate as \(H\), the first rim coordinate as \(X\), and \(D=x_2+x_1\). In the kernel of the matrix on the right, set \(D_j=x_{j+1}+x_j\) for \(1\le j\le n-1\). The interior rim equations give \(D_j=zD_{j-1}+zH\), hence

\[
D_j=z^{j-1}D+G_jH,\qquad G_j=\sum_{r=1}^{j-1}z^r.
\]

Define \(H_D=\sum_{j=1}^{n-1}z^{j-1}\), \(H_H=\sum_{j=1}^{n-1}G_j\), \(W_D=\sum_{1\le j<n,\,n-j\text{ odd}}z^{j-1}\), and \(W_H=\sum_{1\le j<n,\,n-j\text{ odd}}G_j\). Eliminating interior coordinates by monic unit-pivot operations reduces the determinant exactly to that of the following \(3\times3\) matrix (columns \(H,X,D\)):

\[
B_n(z)=\begin{pmatrix}
z+H_H&z+1&1+H_D\\
z+zG_{n-1}+H_H&z+1&z^{n-1}+H_D\\
z+1+W_H&n\bmod2&W_D
\end{pmatrix}.
\]

Here \(n\bmod2\) is interpreted in \(\mathbb F_2\). To evaluate its determinant for arbitrary \(n\), abbreviate \(a=z+1\), \(Z=z^n\), and \(\kappa=\lfloor n/2\rfloor\bmod2\). In the rational-function field (the final identities are polynomial identities),

\[
H_D=\frac{Z+z}{za},\quad
H_H=\frac{z}{a}(H_D+\mathbf1_{2\mid n}),\quad
G_{n-1}=\frac{Z+z^2}{za},
\]
\[
W_D=\begin{cases}(Z+1)/(z^2+1)&2\mid n,\\(Z+z)/(z^2+1)&2\nmid n,\end{cases}
\qquad W_H=\frac{z}{a}(W_D+\kappa).
\]

Substituting into the displayed three-by-three determinant and reducing the four possible residues of \(n\bmod4\) gives

\[
\det B_n(z)=zZ+1+\frac{Z+z^4}{z(z+1)}+\epsilon_n(Z+z).
\]

Because \((Z+z^4)/(z(z+1))=\sum_{j=3}^{n-2}z^j\) on substituting \(Z=z^n\), the claimed polynomial \(P_n\) follows, including the small boundary \(n=4\).

**2. Cyclicity and its unique obstruction.** For an eigenvalue \(\lambda\ne1\) over an algebraic closure of \(\mathbb F_2\), subtracting the first two rows of \(B_n(\lambda)\) yields a row with zero \(X\)-entry and with \((H,D)\)-entries \((\lambda G_{n-1},1+\lambda^{n-1})\). These two entries cannot both vanish. If \(\lambda=0\), the second is one. If \(\lambda\ne0,1\) and \(\lambda^{n-1}=1\), the first equals \(\lambda\), as follows directly from the geometric sum. Meanwhile the first row's \(X\)-entry is \(\lambda+1\ne0\). Thus \(\operatorname{rank}B_n(\lambda)\ge2\), giving geometric multiplicity at most one at all eigenvalues other than one.

At \(\lambda=1\), direct evaluation of the finite sums in \(B_n\), for residues \(n\equiv0,1,2,3\pmod4\), gives ranks \(0,3,2,3\), respectively. For \(n\equiv0\pmod4\), every entry of \(B_n(z)\) is divisible by \(z+1\). Its quotient by \(z+1\), evaluated at one, equals

\[
\begin{pmatrix}1&1&1\\0&1&0\\0&0&0\end{pmatrix}
\ \text{if }n\equiv4\pmod8,
\qquad
\begin{pmatrix}1&1&1\\0&1&0\\1&0&0\end{pmatrix}
\ \text{if }n\equiv0\pmod8.
\]

Finally, expanding \(P_n(1+u)\) to the first nonzero term gives order of vanishing \(3\) for \(n\equiv0,2\pmod8\) and \(5\) for \(n\equiv4,6\pmod8\). It follows from the elementary-divisor classification that for \(4\nmid n\) every eigenvalue has one Jordan chain, so the operator has a single cyclic module \(\mathbb F_2[z]/(P_n)\). For \(4\mid n\), the eigenvalue one has three chains, of lengths \((1,1,1)\) if \(8\mid n\) and \((3,1,1)\) if \(n\equiv4\pmod8\), while all other eigenvalues still have only one chain. This proves precisely the two extra linear factors \(z+1\) in the stated module decomposition.

**3. Orbit counts.** On a cyclic module \(\mathbb F_2[z]/(R)\), the kernel of multiplication by \(z^d+1\) has binary dimension \(\deg\gcd(R,z^d+1)\). Each additional trivial \(\mathbb F_2[z]/(z+1)\) summand contributes one dimension for every \(d\ge1\). Since all shears are invertible, every state belongs to a cycle; the fixed-power formula and Möbius inversion finish the proof. For reciprocity, reflection of the rim reverses the rim scan, while conjugation by the invertible hub update cyclically moves the hub scan between first and last. Hence the sweep is linearly conjugate to its inverse; its determinant is one and its characteristic polynomial is reciprocal.

## Verification

The accompanying dependency-free program `checks/verify.py` constructs the sweep independently from the graph adjacency and computes the characteristic determinant independently by Euclidean elimination over \(\mathbb F_2[z]\). It compares the proposed polynomials at every rim length from 4 through 25 (22 exact tests). It separately derives full matrix minimal polynomials and ranks of fixed-power kernels through rim length 80 (77 lengths, 1,078 fixed-power comparisons). It also enumerates all \(4,064\) binary states for rim lengths 4 through 10, comparing entire cycle decompositions with the polynomial-gcd formula. The accompanying captured output is `checks/verification_output.txt`.

The algebra in the proof establishes the unbounded theorem; finite tests are checks, not substitutes for its all-size assertions.

## Relationship to prior work

Macauley and Mortveit's 2008 preprint *Cycle Equivalence of Graph Dynamical Systems* studies the equivalence of update orders of graph dynamical systems, and explicitly discusses invertible parity local maps. Its general equivalence bounds, including the vertex-join orientation bound, do not evaluate this ordered wheel's characteristic polynomial or its invariant-factor census. Macauley, McCammond and Mortveit also treat Rule 150 in the full text of their dynamics-groups article, but explicitly restrict the studied asynchronous automata to circular graphs. Their group classification does not give the spectrum of the hub-coupled graph. The published binary-ring sequential Rule 150 classification concerns a cycle without a hub; it cannot directly supply the wheel's exceptional noncyclic invariant factors. Synchronous neighbor-XOR on wheels likewise uses a different global map, which can be noninvertible, unlike this sweep.

## Limitations

This theorem concerns a fixed hub-first rim-contiguous scan, not all possible orders and not synchronous excitation. The formula is an exact effective census, but does not reduce all possible primitive periods to a single simple arithmetic progression as \(n\) varies. The literature comparison was bounded by discoverability and availability; an inaccessible individual published classification or a more general spectral theorem might have historical priority. Independent mathematical auditing has not been performed.

## References

1. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412, first public version 2008-02-29; published in *Nonlinearity* **22** (2009), 421–436. https://arxiv.org/abs/0802.4412 ; accessible full text https://www.math.clemson.edu/~macaule/papers/CycleEquivalence_Nonlinearity.pdf
2. *Scan-order phase diagram and exact Rule 150 cycle census on binary rings*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-scan-order-phase-diagram-and-exact-rule-150-cycle-census-on-bina--a8edc73752da
3. M. Macauley, J. McCammond and H. S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238, first public version 2008-08-08, sections 2 and 5, especially Theorem 5.4. https://arxiv.org/html/0808.1238v2
