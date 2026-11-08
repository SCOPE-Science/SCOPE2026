# Arithmetic resonance of long-time unitary chord gaps on Paley graphs

## Finding
For every odd prime power \(q\equiv1\pmod4\), let \(A_q\) be the adjacency Hamiltonian of the Paley graph \(P_q\). Let \(\lambda_0<\lambda_1<\lambda_2\) be its **three distinct** real eigenvalues (multiplicities are ignored), and define the long-time minimum *chord* separation
\[
\mathcal G(q)=\lim_{T\to\infty}\frac1T\int_0^T
\min_{i<j}\bigl|e^{-it\lambda_i}-e^{-it\lambda_j}\bigr|\,dt.
\]
The limit exists. If \(q\) is not a perfect square, it has the same exact value for **every such order**:
\[
\mathcal G(q)=C_3:=\frac{12}{\pi}-\frac{18\sqrt3}{\pi^2}=0.660836751077666\ldots.
\]
If \(q=r^2\), where \(r\) is an odd prime power, put \(k=(r-1)/2\). Then
\[
\mathcal G(q)=R_k:=\frac2\pi\int_0^\pi
\min\left\{\left|\sin\frac t2\right|,
\left|\sin\frac{kt}{2}\right|,
\left|\sin\frac{(k+1)t}{2}\right|\right\}\,dt.
\]
In particular, the first two explicit resonances on opposite sides of the universal value are
\[
\mathcal G(9)=\frac3\pi=0.954929658551372\ldots>C_3,
\]
\[
\mathcal G(49)=\frac{101-15\sqrt5-28\cos(\pi/7)-28\cos(2\pi/7)}{12\pi}
=0.657154409560447\ldots<C_3.
\]
Thus the **same natural graph family**, with three distinct adjacency energies at every size, has a universal non-square-order value and commensurability-induced deviations of both signs. This is a claim about a time-averaged spectral *chord*, not about graph quantum-walk mixing or algorithmic QAOA success.

## Assumptions and scope
A Paley graph \(P_q\) has vertex set \(\mathbb F_q\), where \(q\) is an odd prime power congruent to \(1\) modulo \(4\); distinct vertices are joined when their difference is a nonzero square. Its adjacency matrix is a real symmetric Hamiltonian. The minimum is taken over **distinct spectral values**, not repeated eigenvalues; otherwise degeneracies would make the quantity trivially zero. Time averaging is continuous, from zero to infinity, with ordinary Euclidean distance between the complex unitary eigenvalues. No finite-window or discrete-time statement is asserted. Scaling \(A_q\) by any positive constant leaves \(\mathcal G(q)\) unchanged by time reparametrization.

## Proof
**1. Paley spectrum and arithmetic condition.** For the quadratic character \(\chi\) on \(\mathbb F_q\), the additive-character diagonalization of the Paley adjacency matrix yields the eigenvalues
\[
\lambda_2=(q-1)/2,\qquad \lambda_{0,1}=(-1\mp\sqrt q)/2.
\]
Indeed the adjacency multiplier at a nontrivial additive character is \(({-1}+\chi(a)G)/2\), where the quadratic Gauss sum has \(G^2=q\) for \(q\equiv1\pmod4\). This also follows from the strongly regular parameters \((q,(q-1)/2,(q-5)/4,(q-1)/4)\): on the orthogonal complement of constants, the adjacency operator satisfies \(A^2+A-(q-1)I/4=0\).

Subtracting \(\lambda_0\) from the remaining energies gives the two frequencies \(\sqrt q\) and \((q+\sqrt q)/2\). They are rationally independent if and only if \(\sqrt q\notin\mathbb Q\): for \(a,b\in\mathbb Z\),
\[
 a\sqrt q+b(q+\sqrt q)/2=0
\quad\Longleftrightarrow\quad bq+(2a+b)\sqrt q=0.
\]
When \(q\) is nonsquare, both coefficients must vanish. When \(q=r^2\), the adjacent spectral gaps are \(r\) and \(r(r-1)/2\); dividing by the common \(r\) yields \(\{0,1,k+1\}\), with \(k=(r-1)/2\).

**2. An independent-phase chord lemma.** Let \(H\) have \(n\ge2\) distinct real eigenvalues with \(n-1\) rationally independent differences from one reference eigenvalue. By the continuous Kronecker–Weyl theorem, the relative eigenphase orbit is equidistributed on the \((n-1)\)-torus. The average of the continuous minimum-chord function therefore equals its average over \(n\) independent uniformly distributed points on the circle, after fixing the first point at angle zero.

For \(n\) circular uniform points, the \(n\) ordered clockwise normalized gaps \((G_1,\ldots,G_n)\) have Dirichlet\((1,\ldots,1)\) distribution. If \(M=\min_jG_j\), translation of the simplex gives the exact survival law
\[
\Pr(M>s)=(1-ns)^{n-1},\qquad 0\le s\le1/n.
\]
The minimum chord between any two points is \(2\sin(\pi M)\): the closest pair is consecutive in circular order. Integration by parts yields
\[
\mathbb E[2\sin(\pi M)]=2\pi\int_0^{1/n}\cos(\pi s)(1-ns)^{n-1}\,ds.
\]
For \(n=3\), elementary integration produces \(C_3=12/\pi-18\sqrt3/\pi^2\). Applying the first step proves the nonsquare Paley law.

**3. Exact commensurate family.** For square order, translation and positive rescaling of the spectrum reduce the three unitary phases to \(1,e^{-it},e^{-i(k+1)t}\). Their three pairwise chord lengths are \(2|\sin(t/2)|\), \(2|\sin(kt/2)|\), and \(2|\sin((k+1)t/2)|\). This function has period \(2\pi\), is symmetric under \(t\mapsto2\pi-t\), and gives the asserted formula for \(R_k\).

For \(q=9\), \(k=1\). On \(0\le t\le\pi\), the minimum of the two distinct functions \(\sin(t/2)\) and \(\sin t\) changes at \(t=2\pi/3\). Direct integration gives
\[
R_1=\frac2\pi\left(\int_0^{2\pi/3}\sin(t/2)\,dt+
\int_{2\pi/3}^{\pi}\sin t\,dt\right)=\frac3\pi.
\]
For \(q=49\), \(k=3\). The active minimum of \(|\sin(t/2)|,|\sin(3t/2)|,|\sin(2t)|\) is, in order,
\[
\begin{array}{c|cccccc}
t&[0,2\pi/5]&[2\pi/5,\pi/2]&[\pi/2,4\pi/7]&[4\pi/7,2\pi/3]&[2\pi/3,6\pi/7]&[6\pi/7,\pi]\\
\hline
\text{minimum}&\sin(t/2)&\sin(2t)&-\sin(2t)&\sin(3t/2)&-\sin(3t/2)&-\sin(2t)
\end{array}
\]
The table follows by using \(\sin^2u-\sin^2v=\sin(u+v)\sin(u-v)\) on every interval separated by zeros of the pairwise differences; all possible internal comparison zeros are at \(\pi/2\), \(2\pi/5\), \(4\pi/5\), \(2\pi/3\), and \(2j\pi/7\) for \(j=1,2,3\). Integration of the six displayed pieces gives the stated radical–trigonometric expression for \(R_3\). Exact rational enclosures for \(\pi\), \(\sqrt3\), \(\sqrt5\), \(\cos(\pi/7)\), and \(\cos(2\pi/7)\), derived from alternating series and integer square roots, prove strictly \(R_3<C_3<R_1\). The enclosure script uses rational arithmetic without third-party packages.

## Verification
Run `python3 verify.py` from the package directory. It computes rigorous rational intervals for all three constants using Machin's arctangent identity with alternating-series remainders, rational Taylor enclosures of cosine, and integer-square-root brackets. It certifies \(\mathcal G(49)<C_3<\mathcal G(9)\). Independent direct-period midpoint quadrature checks the two commensurate formulas. Separately, explicit finite-field enumeration for \(q=5,9,49\) checks the Paley degree and adjacent/nonadjacent common-neighbor counts. The finite enumerations and numerical quadratures are diagnostic checks only; the proof for every allowed prime power uses the spectral formula, Kronecker–Weyl equidistribution and analytic integrations.

## Relationship to prior work
Gulati and SAPV's 2026 work [1] proposes a long-time averaged unitary eigenvalue-separation heuristic for QAOA mixers and analyzes complete graphs, hypercubes, cycles and balanced two-dimensional tori. This finding explicitly treats a Paley-graph family and its square/nonsquare arithmetic resonance, using a specified **distinct-eigenvalue Euclidean chord** observable. It does not claim the general concept of the heuristic is new. Podestá and Videla [2,3], and standard conference-graph theory [4], supply Paley and generalized Paley spectral information, but spectral formulas alone do not state the long-time minimum-chord classification or the opposite-sign \(q=9\) and \(q=49\) resonances. The Dirichlet minimum circular-spacing law is classical and is used, not claimed as a new probability result [5]. A source-level coverage risk remains for uninspected portions of [1]; the available abstract lists other graph classes but not Paley graphs.

## Limitations
The metric discards eigenvalue multiplicities, and its infinite-time average may be very different from the finite-time QAOA-parameter behavior. The result does not imply anything about mixing probabilities, quantum speedups, entanglement, or the success of an optimization algorithm. It does not classify the order or extrema of \(R_k\) for all \(k\), nor show uniform convergence rates in averaging time. The primary 2026 manuscript's full text was not obtainable during this review, leaving a concrete publication-priority risk; abstract-only inspection cannot establish whole-document noncoverage. Independent validation has not been performed.

## References
1. J. S. Gulati and Tharrmashastha SAPV, *Quantum-Walk Inspired Spectral Metrics for Evaluating QAOA Mixers*, arXiv:2610.40459 (first public 2026-10-29), https://arxiv.org/abs/2610.40459 .
2. R. A. Podestá and D. E. Videla, *Spectral properties of generalized Paley graphs*, arXiv:2310.15378 (first public 2023-10-23), https://arxiv.org/abs/2310.15378 .
3. R. A. Podestá and D. E. Videla, *The nature of the spectrum of generalized Paley graphs and weak Waring numbers over finite fields*, arXiv:2604.06513 (first public 2026-04-07), https://arxiv.org/abs/2604.06513 .
4. A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, Springer (2012), Chapter on strongly regular graphs; standard Paley spectrum also summarized at https://en.wikipedia.org/wiki/Paley_graph .
5. *Smallest gap among random points on a circle*, Geometric Probability, chapter 17 (viewed 2026-11-05), https://vamshij.com/books/geometric_probability/read/17/ .
