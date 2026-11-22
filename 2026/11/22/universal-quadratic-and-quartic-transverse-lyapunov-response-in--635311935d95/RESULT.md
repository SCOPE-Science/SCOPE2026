# Universal quadratic and quartic transverse Lyapunov response in a cat-driven Möbius map

## Finding
For the exact deterministic Anosov-driven circle map below, the conditional Lyapunov exponent supported on its small attracting invariant graph is even and analytic in forcing, with the exact fourth-order expansion
\[
\boxed{\Lambda_\varepsilon(\mu)=\log\frac{1-\varepsilon}{1+\varepsilon}+\frac{\pi^2}{2}\mu^2+\frac{\pi^4(\varepsilon^2-\varepsilon+1)}{16\varepsilon}\mu^4+O_{\varepsilon}(\mu^6).}
\]
The first correction is universal over all fixed \(0<\varepsilon<1\) and all phases. The strictly positive fourth-order correction, though dependent on \(\varepsilon\), remains independent of the forcing phase. The exact coefficients refer to the original map time, not a return map or reparameterized clock.

## Assumptions and scope
Let \(A:\mathbb T^2\to\mathbb T^2\) be \(A(t,s)=(2t+s,t+s)\bmod1\), with normalized Haar probability \(m\). Fix \(\varepsilon\in(0,1)\), \(\alpha\in\mathbb R\), and zero frequency drift. Consider the real circle lift near zero
\[
 g_\varepsilon(x)=x-\frac1\pi\arctan\left(\frac{\varepsilon\sin(2\pi x)}{1+\varepsilon\cos(2\pi x)}\right),\quad
 F_\mu(\xi,x)=(A\xi,\,g_\varepsilon(x)+\mu\sin(2\pi t+\alpha))\bmod1.
\]
The parameter \(\mu\) is real and sufficiently close to zero, with admissible radius depending on the fixed \(\varepsilon\). The attracting graph \(h_\mu\) is the unique continuous solution within a sufficiently small fixed strip about zero of
\[
 h_\mu(A\xi)=g_\varepsilon(h_\mu(\xi))+\mu\sin(2\pi t+\alpha).
\]
The asserted fiber Lyapunov exponent is
\[
 \Lambda_\varepsilon(\mu)=\int_{\mathbb T^2}\log g_\varepsilon'(h_\mu(\xi))\,dm(\xi).
\]
Ergodicity of the cat automorphism identifies this integral with the almost-everywhere asymptotic fiber derivative exponent on the graph.

## Proof
**1. Local analytic attracting graph.** Direct differentiation gives
\[
 g_\varepsilon'(x)=\frac{1-\varepsilon^2}{1+2\varepsilon\cos(2\pi x)+\varepsilon^2},\qquad q=g_\varepsilon'(0)=\frac{1-\varepsilon}{1+\varepsilon}\in(0,1).
\]
Because \(g_\varepsilon\) is real analytic and odd near zero, choose a closed strip \([-\delta,\delta]\) on which \(|g_\varepsilon'|\le\theta<1\), then choose \(|\mu|<(1-\theta)\delta\). Graph transform on continuous functions, \(H\mapsto g_\varepsilon(H\circ A^{-1})+\mu\sin(2\pi e_1\cdot A^{-1}\xi+\alpha)\), contracts the strip and yields the unique graph. The analytic implicit-function theorem on \(C^0(\mathbb T^2)\) gives real-analytic parameter dependence: the derivative of the graph equation at zero is \(I-q\,C_{A^{-1}}\), with inverse given by a norm-convergent Neumann series. Oddness of \(g_\varepsilon\) yields \(h_{-\mu}=-h_\mu\); write \(h_\mu=\mu u+\mu^3v+O_\varepsilon(\mu^5)\) in the uniform norm.

**2. Perturbation and Fourier dissociation.** Put \(S(\xi)=\sin(2\pi t+\alpha)\) and \(a_3=4\pi^2\varepsilon(1-\varepsilon)/(3(1+\varepsilon)^3)\). The graph equation implies
\[
 u(A\xi)=q u(\xi)+S(\xi),\qquad v(A\xi)=q v(\xi)+a_3u(\xi)^3,
\]
so \(u(\xi)=\sum_{j\ge1}q^{j-1}S(A^{-j}\xi)\), \(v(\xi)=a_3\sum_{j\ge1}q^{j-1}u(A^{-j}\xi)^3\).

The Fourier frequencies of \(S(A^{-j}\xi)\) are \(\pm k_j\), where \(k_j=A^{-Tj}e_1=(F_{2j-1},-F_{2j})\) for Fibonacci numbers \(F_1=F_2=1\). There is no nontrivial zero sum of at most four such signed frequencies. To see this, write \(b_j=F_{2j}\), so \(b_{j+1}=3b_j-b_{j-1}\) and \(b_{j+1}>2b_j\) for all \(j\ge1\). In a shortest signed relation with at most four terms, the largest index can occur only once (twice would outweigh the at most two smaller terms), and must equal the sum of three lower-index terms in the second coordinate; at most two smaller terms cannot reach it. If at most one summand has the immediately preceding index, their sum is too small. If two do, the leftover is \(b_{N-1}-b_{N-2}\), strictly between two adjacent possible values for \(N\ge3\), and three would be too large. The exceptional \(N=2\) scalar identity \(3b_1=b_2\) fails in the first coordinate since \(3k_1\ne k_2\). Hence no four-wave resonance. Consequently all mixed sine moments of total degree at most four agree with independent uniform phases, including the repeated-index terms.

Orthogonality and the fourth-order moment identity give
\[
 U_2:=\int u^2dm=\frac1{2(1-q^2)},\quad
 U_4:=\int u^4dm=\frac3{4(1-q^2)^2}-\frac3{8(1-q^4)}.
\]
Splitting \(u(\xi)\) into its last \(j\) forcing kicks plus \(q^j u(A^{-j}\xi)\), and applying the same four-wave dissociation, gives \(\int u(\xi)u(A^{-j}\xi)^3dm=q^jU_4\). Therefore
\[
 \int uv\,dm=\frac{a_3q}{1-q^2}U_4.
\]
All series are absolutely and uniformly convergent for fixed \(q<1\); term-by-term integration is legitimate.

**3. The exact coefficients.** Taylor expansion of the logarithmic derivative reads
\[
 \log g_\varepsilon'(x)=\log q+\ell_2x^2+\ell_4x^4+O_\varepsilon(x^6),
\quad \ell_2=\frac{4\pi^2\varepsilon}{(1+\varepsilon)^2},\quad
 \ell_4=-\frac{4\pi^4\varepsilon(\varepsilon^2-4\varepsilon+1)}{3(1+\varepsilon)^4}.
\]
Substitution of \(h_\mu=\mu u+\mu^3v+O(\mu^5)\) yields
\[
 \Lambda_\varepsilon(\mu)=\log q+\ell_2U_2\mu^2+
 (2\ell_2\int uv\,dm+\ell_4U_4)\mu^4+O_\varepsilon(\mu^6).
\]
Simplifying the rational expressions in \(\varepsilon\) gives \(\ell_2U_2=\pi^2/2\) and \(2\ell_2\int uv\,dm+\ell_4U_4=\pi^4(\varepsilon^2-\varepsilon+1)/(16\varepsilon)\). This proves the expansion, its phase-independence and strict positivity.

## Verification
The standalone `verify.py` reproduces the exact symbolic derivatives and rational-function simplifications, checks the first fourteen Fibonacci frequency vectors and verifies that all zero signed four-wave sums within that finite check are trivial pair cancellations. These finite checks support, but do not replace, the infinite dissociation and graph-transform arguments proved above. Run `python verify.py` with Python 3 and SymPy installed.

## Relationship to prior work
Chigarev, Kazakov and Pikovsky introduced precisely this invertible cat-driven Möbius family and computed Lyapunov exponents numerically while studying attractor–repeller collisions. Their displayed derivative formula agrees with the one used here, but their analysis does not give this parameter-uniform weak-forcing expansion. A subsequent analysis of the same family gives sharp spatial regularity thresholds for the first graph response; the present calculation instead integrates nonlinear graph response and uses the absence of short Fourier resonances to obtain second- and fourth-order transverse Lyapunov coefficients. Dorsch and Schulz-Baldes examine a distinct stochastic Möbius matrix-product setting, not this deterministic cat skew-product with its fixed zero-drift attracting graph.

## Limitations
The result is local in \(\mu\) for each fixed \(0<\varepsilon<1\); the remainder constant and admissible forcing interval need not remain uniform as \(\varepsilon\to0\) or \(\varepsilon\to1\). No claim is made for the other invariant circle graph, all invariant measures, global basins, nonlinear collision thresholds, or forcing terms other than the displayed one. The fourth-order formula is a statement about the exponent, not the fourth derivative of the graph in its base coordinate. The completeness of the mathematical literature comparison remains subject to incompletely accessible related work.

## References
1. V. Chigarev, A. Kazakov, A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172v1, first submitted 2023-05-29, https://arxiv.org/html/2305.18172v1 (original map, derivative and Lyapunov discussion, Sections II–III and Appendix A).
2. F. Dorsch, H. Schulz-Baldes, *Random Möbius dynamics on the unit disc and perturbation theory for Lyapunov exponents*, Discrete and Continuous Dynamical Systems–B 27 (2022), 945–976, DOI:10.3934/dcdsb.2021076 (distinct i.i.d. random matrix-product framework).
3. *Sharp smoothness staircase and gradient susceptibility of a cat-driven Möbius response* (2026), public mathematical summary indexed in the published-finding corpus research collection (first-order spatial regularity, distinct claim).
