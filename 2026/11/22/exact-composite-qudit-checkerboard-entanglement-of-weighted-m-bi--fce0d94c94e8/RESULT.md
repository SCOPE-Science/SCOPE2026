# Exact composite-qudit checkerboard entanglement of weighted Möbius ladders

## Finding
For every odd integer \(n\ge3\), every integer rung weight \(w\), and every local Hilbert-space dimension \(d\ge2\), the weighted \(2n\)-site Möbius-ladder graph state has an exactly flat Schmidt spectrum across the even/odd vertex bipartition. Its entire nonzero spectrum is determined by a pair of integers computable from a second-order recurrence, rather than by an \(n\)-dimensional matrix reduction.

Define \(a_0=0\), \(a_1=1\), and \(a_{j+1}=-w a_j-a_{j-1}\) for \(j\ge1\). Define \(L_0=2\), \(L_1=-w\), and \(L_{j+1}=-wL_j-L_{j-1}\) for \(j\ge1\). Set
\[
 g_{n,w}=\gcd(|a_n|,|a_{n-1}+1|),\qquad \delta_{n,w}=|2-L_n|,
\]
and set \(h_{n,w}=\delta_{n,w}/g_{n,w}\) when \(g_{n,w}>0\), while \(h_{n,w}=0\) when \(g_{n,w}=0\). The latter case necessarily has \(\delta_{n,w}=0\). The integral Smith normal form of the bipartite cross-adjacency matrix is
\[
 \operatorname{diag}(\underbrace{1,\ldots,1}_{n-2},g_{n,w},h_{n,w}),
\]
where zero factors are permitted and the nonzero Smith factors appear in divisibility order. Consequently the reduced state has precisely
\[
 R_{n,d,w}=\frac{d^n}{\gcd(d,g_{n,w})\gcd(d,h_{n,w})}
\]
nonzero eigenvalues, each equal to \(R_{n,d,w}^{-1}\), and the bipartite von Neumann entropy in bits is \(\log_2 R_{n,d,w}\). Here \(\gcd(d,0)=d\).

The rung-weight phase examples are exact for **every odd** \(n\ge3\):

| Rung weight | Last two integral Smith factors |
|---|---|
| \(w=-2\) | \((n,0)\) |
| \(w=-1\), \(3\mid n\) | \((2,2)\) |
| \(w=-1\), \(3\nmid n\) | \((1,1)\) |
| \(w=0\) | \((1,2)\) |
| \(w=1\), \(3\mid n\) | \((0,0)\) |
| \(w=1\), \(3\nmid n\) | \((1,3)\) |
| \(w=2\) | \((1,4)\) |

In particular, at uniform weight \(w=1\), the entropy is \((n-2)\log_2 d\) when \(3\mid n\), and \(n\log_2 d-\log_2\gcd(d,3)\) otherwise. This distinguishes a two-unit loss of base-\(d\) entanglement at divisible-by-three lengths from a one-unit ternary loss at other lengths.

## Assumptions and scope
Let \(V=\mathbb Z/(2n)\), with \(n\ge3\) odd. Join each vertex \(v\) to \(v\pm1\) with unit edge weight, and to \(v+n\) with integer weight \(w\). Since \(n\) is odd, each edge crosses the balanced cut \(E=\{0,2,\ldots,2n-2\}\), \(O=\{1,3,\ldots,2n-1\}\). A negative or zero rung weight is allowed: it is a phase weight, and zero removes that phase coupling.

Let \(\omega=\exp(2\pi i/d)\). The graph state is obtained from \(d\)-level \(|+\rangle\) product states by multiplying every computational-basis amplitude by the phase \(\omega^{\sum_{\{u,v\}} w_{uv}x_ux_v}\), the sum being over **unordered** graph edges once. Equivalently, for the above bipartition and its integer cross-adjacency matrix \(B\),
\[
 |\Psi_{n,d,w}\rangle=d^{-n}\sum_{x,y\in(\mathbb Z/d\mathbb Z)^n}\omega^{x^{\mathsf T}By}|x\rangle_E|y\rangle_O.
\]
The normalization is \(d^{-n}\) because there are \(2n\) qudits. All statements concern this pure state, one specified bipartition, and integer phase weights reduced modulo \(d\). No primeness condition on \(d\) is assumed.

## Proof
**1. An integral circulant model.** Number even vertices as \(e_i=2i\) and odd vertices as \(o_j=2j+1\), with indices in \(\mathbb Z/n\mathbb Z\). The two cycle neighbors of \(e_i\) are \(o_i\) and \(o_{i-1}\), and its antipode \(e_i+n\) is \(o_{i+(n-1)/2}\). If \(S\) denotes a cyclic one-step shift on the index module, the cross-adjacency is, up to choosing the direction of \(S\), \(B=I+S^{-1}+wS^{(n-1)/2}\). Multiplication by the invertible integer shift \(S\) gives \(SB=I+S+wS^{(n+1)/2}\).

Put \(T=S^{(n+1)/2}\). As \(n\) is odd, \(\gcd((n+1)/2,n)=1\), so \(T\) is again an \(n\)-cycle, and \(T^2=S^{n+1}=S\). Therefore \(SB=I+T^2+wT\). Integer shift multiplication and reordering of the cyclic index preserve integral Smith factors, so those of \(B\) equal those of \(f_w(T)=T^2+wT+I\).

**2. Reduce every size to a rank-two lattice.** Let \(f_w(t)=t^2+wt+1\). The cokernel of the integer circulant \(f_w(T)\) has the module presentation
\[
 \mathbb Z[t]/(t^n-1,f_w(t)).
\]
The monic quadratic relation makes \(Q_w=\mathbb Z[t]/(f_w(t))\) a free \(\mathbb Z\)-module of rank two, with basis \((1,t)\). Multiplication by \(t\) has the integer matrix
\[
 C_w=\begin{pmatrix}0&-1\\1&-w\end{pmatrix},\qquad\det C_w=1.
\]
Adding the relation \(t^n=1\) therefore produces precisely \(\operatorname{coker}(C_w^n-I_2)\). Isomorphic finitely generated integer modules have the same nontrivial invariant factors and free rank. Thus the original \(n\)-by-\(n\) Smith form has \(n-2\) unit entries followed by the two Smith entries of \(C_w^n-I_2\), including any zeros.

**3. Evaluate the two factors without diagonalization.** Induction on \(j\) gives
\[
 C_w^j=\begin{pmatrix}-a_{j-1}&-a_j\\a_j&a_{j+1}\end{pmatrix},\qquad j\ge1.
\]
The gcd of the four entries in \(C_w^n-I_2\) is precisely \(g_{n,w}\): the two off-diagonal entries are \(\pm a_n\), the upper-left entry is \(-a_{n-1}-1\), and the lower-right entry is \(-w a_n-a_{n-1}-1\). The trace of \(C_w^n\) obeys the recurrence defining \(L_n\); because \(\det C_w^n=1\),
\[
 \det(C_w^n-I_2)=2-\operatorname{tr}(C_w^n)=2-L_n.
\]
If \(g_{n,w}>0\), the Smith entries of this \(2\)-by-\(2\) integer matrix are \(g_{n,w}\) and \(|2-L_n|/g_{n,w}\), with a zero second entry when the determinant vanishes. If \(g_{n,w}=0\), all entries vanish and both Smith entries are zero. This proves the integer classification for every parameter, including singular cases.

**4. Compute the exact Schmidt spectrum over any cyclic local dimension.** Trace out the odd sites. Orthogonality of characters of \((\mathbb Z/d\mathbb Z)^n\) shows that the even reduced density matrix obeys
\[
 (\rho_E)_{x,x'}=d^{-n}\mathbf1_{\{B^{\mathsf T}(x-x')=0\pmod d\}}.
\]
This is a direct sum of equal all-ones blocks indexed by the cosets of \(\ker B^{\mathsf T}\). If \(K=|\ker B^{\mathsf T}|\), the number of blocks is \(d^n/K\); each contributes one eigenvalue \(K/d^n\) and otherwise zero. Since the Smith factors are \((1,\ldots,1,g_{n,w},h_{n,w})\), the image cardinality is \(d^{n-2}(d/\gcd(d,g_{n,w}))(d/\gcd(d,h_{n,w}))\). This is \(R_{n,d,w}\), proving the flat spectrum and entropy formula for all composite as well as prime \(d\).

**5. Weight-specific boundaries.** These follow by substituting \(w=-2,-1,0,1,2\) into the same rank-two recurrence. For example, \(w=1\) gives \(C_w^3=I_2\) and \(I_2+C_w+C_w^2=0\); the resultant Smith entries are \((0,0)\) for \(3\mid n\), and \((1,3)\) otherwise. For \(w=-2\), \((C_w-I_2)^2=0\) with primitive rank-one \(C_w-I_2\), so \(C_w^n-I_2=n(C_w-I_2)\), giving \((n,0)\). At \(w=-1\), \(C_w^3=-I_2\), producing \((2,2)\) when odd \(n\) is divisible by three and a unimodular difference otherwise. The other entries follow from \(C_0^2=-I_2\) and the double root \(-1\) at \(w=2\).

## Verification
Two complete standalone Python files accompany this result: `verify_weighted.py` and `verify_weighted_schmidt.py`. The first builds the physical cross-cut matrix and computes its integer Smith normal form using SymPy, independently of the proof's quotient construction. It tests all eight odd lengths \(n=3,5,\ldots,17\), each with the thirteen weights \(-6\le w\le6\), for 104 exact cases. The second builds the full weighted physical adjacency, enumerates modular images for odd lengths three, five and seven and several composite and prime dimensions, and directly diagonalizes small reduced density matrices derived from the pure state. Both pass. These are finite cross-checks only: the all-length and all-dimension assertions follow from the exact integer-module proof, not extrapolation.

For a reproducible run with Python, NumPy and SymPy installed, use `python verify_weighted.py` and `python verify_weighted_schmidt.py` in the folder containing the scripts.

## Relationship to prior work
The graph-state formalism and the relationship between bipartite entanglement and cross-adjacency are established by Hein, Eisert and Briegel (2003). Looi, Yu, Gheorghiu and Griffiths (2007) extend graph-state and stabilizer constructions to arbitrary qudit dimension. Helwig (2013) investigates bipartite graph-state entanglement, especially absolute maximality. Telloni and Williams (2014) study Smith forms of circulant polynomial \(\lambda\)-matrices. These foundations are not claimed as new. Their inspected results do not give the present weighted Möbius-ladder integer Smith factors or the ensuing complete three-parameter composite-dimension Schmidt classification.

Related separately published findings on generalized-Petersen graph-state resonances concern a different graph family and a different cut. In particular, the generalized Petersen graph with an odd outer ring is not the bipartite odd-rung Möbius ladder considered here. Existing results on Möbius-ladder quantum transport analyze spectral time evolution, not this pure graph-state bipartite Schmidt spectrum. Such relationships do not constitute a proof of global historical uniqueness.

## Limitations
The theorem treats odd \(n\) only, when the parity cut is bipartite and every edge crosses it. Even \(n\), arbitrary cuts, noisy states, nonuniform individual rung weights, and physically dynamical Hamiltonians are not covered. Weighted edges are integer controlled-phase exponents, not arbitrary real-valued couplings. The result determines entanglement for this one balanced cut; it does not assert absolute maximal multipartite entanglement. Computational tests are finite checks, and an equivalent result in unindexed literature cannot be ruled out without independent historical review.

## References
1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first public 18 July 2003), https://arxiv.org/abs/quant-ph/0307130.
2. S. Y. Looi, L. Yu, V. Gheorghiu and R. B. Griffiths, *Quantum Error Correcting Codes Using Qudit Graph States*, arXiv:0712.1979 (first public 12 December 2007), https://arxiv.org/abs/0712.1979.
3. W. Helwig, *Absolutely Maximally Entangled Qudit Graph States*, arXiv:1306.2879 (first public 12 June 2013), https://arxiv.org/abs/1306.2879.
4. A. I. Telloni and G. Williams, *Smith forms of circulant polynomial matrices*, preprint dated 19 June 2014, https://repository.essex.ac.uk/9703/1/TelloniWilliams-SmithFormsCirculants.pdf.
