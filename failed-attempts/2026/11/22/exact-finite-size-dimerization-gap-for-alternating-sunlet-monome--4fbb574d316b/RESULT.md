# Exact finite-size dimerization gap for alternating sunlet monomer–dimer zeros

## Finding

An exact all-length zero-band theorem holds for an alternating weighted sunlet. Let \(m\ge2\) be an integer and \(a,b>0\). Attach one pendant vertex to each vertex of the cycle \(C_{2m}\). Assign weight one to each cycle edge and weights \(a,b,a,b,\ldots\) to successive pendant edges. For every matching \(M\), its weight is \(\prod_{e\in M}w_e\). Define
\[
Z_{m,a,b}(z)=\sum_{M\text{ matching}}\Bigl(\prod_{e\in M}w_e\Bigr)z^{|M|},\qquad
\mu_{m,a,b}(x)=x^{4m}Z_{m,a,b}(-x^{-2}).
\]
All \(4m\) zeros of \(\mu_{m,a,b}\) are nonzero, real and simple. For
\[
c_k=\cos\frac{(2k+1)\pi}{2m},\qquad B_k=a+b+2+2c_k,\qquad 0\le k<m,
\]
the complete root list is \(\pm\sqrt{y_{k,-}}\) and \(\pm\sqrt{y_{k,+}}\), with
\[
y_{k,\pm}=\frac{B_k\pm\sqrt{B_k^2-4ab}}{2}>0.
\]
The positive roots form two groups of exactly \(m\) each, separated by the open interval \((\sqrt{\min(a,b)},\sqrt{\max(a,b)})\) when \(a\ne b\). Let \(g_m\) be the distance between the largest positive root of the lower group and the smallest positive root of the upper group. Then the **exact** finite-size law is
\[
\boxed{g_m(a,b)^2=(\sqrt a-\sqrt b)^2+4\sin^2\!\frac{\pi}{4m}.}
\]
In particular, at equal weights \(g_m(a,a)=2\sin(\pi/(4m))\), whereas at fixed unequal weights \(g_m\to|\sqrt a-\sqrt b|\). For a sequence of positive weights with \(m(\sqrt a-\sqrt b)\to\kappa\in\mathbb R\),
\[
\boxed{m g_m\longrightarrow\sqrt{\kappa^2+\pi^2/4}.}
\]
This gives a finite-size crossover without asserting a thermodynamic phase transition.

## Assumptions and scope

The cycle has \(2m\ge4\) distinct vertices; every vertex carries exactly one private leaf. Cycle dimer weights are one and pendant dimer weights alternate \(a,b\), each strictly positive. The variable \(z\) is the ordinary dimer activity and \(x\) is the standard reciprocal-square-root matching-root variable. A statement about a gap in \(x\) does **not** assert an equal-width gap in \(z\): their relation is \(z=-1/x^2\). No other geometry, edge weights, or boundary conditions are covered.

## Proof

**Step 1: weighted matchings as a magnetic determinant.** Put a Hermitian hopping \(\sqrt{w_e}\) on each edge of the sunlet. Assign total oriented cycle phase \(\pi/2\), for instance by placing phase \(i\) on the closing core edge and conjugate phase on its reverse. Call the resulting weighted adjacency matrix \(H\). In the permutation expansion of \(\det(xI-H)\), every transposition contributes \(-w_e\) and enumerates a matching; the only additional permutation cycles traverse the unique core cycle. Their two oriented contributions sum to a factor proportional to \(2\cos(\pi/2)=0\). Consequently
\[
\det(xI-H)=\mu_{m,a,b}(x).
\]
This is a special case of the established complex-gain/Sachs relation, and is used here as a tool rather than claimed as new.

**Step 2: eliminate leaves and compute the transfer trace.** For \(x\ne0\), Schur-complement elimination of the pendant vertices changes the core diagonal at site \(j\) to \(d_j(x)=x-t_j/x\), where \(t_j=a\) for even \(j\) and \(t_j=b\) for odd \(j\). The core cycle has flux \(\pi/2\). Write
\[
T_t(x)=\begin{pmatrix}x-t/x&-1\\1&0\end{pmatrix},\qquad \det T_t(x)=1.
\]
The cyclic determinant with total flux \(\pi/2\) equals the transfer trace, because the usual phase term \(-2\cos(\pi/2)\) vanishes. Hence
\[
\mu_{m,a,b}(x)=x^{2m}\operatorname{tr}\bigl[(T_b(x)T_a(x))^m\bigr].
\]
The pair-transfer trace is
\[
\Delta(x)=\operatorname{tr}(T_bT_a)=x^2-(a+b+2)+ab/x^2.
\]
The determinant-one Chebyshev trace identity yields the polynomial identity
\[
\boxed{\mu_{m,a,b}(x)=2x^{2m}T_m\!\left(\frac{x^2-(a+b+2)+ab/x^2}{2}\right)}.
\]
Although written using \(x^{-2}\), the right side extends polynomially over \(x=0\). Indeed \(\mu_{m,a,b}(0)=(-1)^{2m}(ab)^m>0\), since the unique perfect matching uses every pendant edge.

**Step 3: exact roots and simplicity.** The \(m\) distinct roots of \(T_m\) are \(c_k=\cos((2k+1)\pi/(2m))\), for \(0\le k<m\). Solving \(\Delta(x)/2=c_k\), then setting \(y=x^2\), gives
\[
y^2-B_k y+ab=0,\quad B_k=a+b+2+2c_k>a+b\ge2\sqrt{ab}.
\]
Both \(y\)-roots are strictly positive and distinct. Different \(c_k\) cannot share a positive \(y\), because \(c=(y+ab/y-(a+b+2))/2\) is single-valued. This yields \(4m\) distinct real nonzero roots, exhausting the degree.

**Step 4: the exact gap.** The smallest value of \(B_k\) is \(B_*=a+b+2-2\cos(\pi/(2m))\). For every \(k\), the lower root \(y_{k,-}<\min(a,b)\) and the upper root \(y_{k,+}>\max(a,b)\), since the quadratic is negative at \(y=a\) and \(y=b\). The functions \(y_-\) and \(y_+\) decrease and increase, respectively, with \(B\). Thus the two positive roots bordering the internal gap are \(\sqrt{y_-(B_*)}\) and \(\sqrt{y_+(B_*)}\). Using their sum and product,
\[
\bigl(\sqrt{y_+(B_*)}-\sqrt{y_-(B_*)}\bigr)^2
=B_*-2\sqrt{ab}=(\sqrt a-\sqrt b)^2+4\sin^2\frac{\pi}{4m}.
\]
The fixed-contrast limit and the critical \(m^{-1}\) crossover follow immediately.

**Step 5: limiting bands.** The \(c_k\) form the Chebyshev midpoint grid, equidistributed under the arcsine law on \([-1,1]\). The lower and upper positive-root maps are continuous and monotone. Each supplies exactly \(m\) of the \(4m\) roots; the negative-root counterparts have the same counts. For \(B\in[a+b,a+b+4]\), define \(Y_\pm(B)=(B\pm\sqrt{B^2-4ab})/2\). The limiting support consists of the four signed images of the intervals
\[
[\sqrt{Y_-(a+b+4)},\sqrt{\min(a,b)}]\quad\text{and}\quad
[\sqrt{\max(a,b)},\sqrt{Y_+(a+b+4)}].
\]
The two positive intervals touch only when \(a=b\), exactly as their negative counterparts do.

## Verification

The attached standalone script `verify.py` independently enumerates weighted matchings by deletion/contraction on the vertex masks and compares the entire exact polynomial with the Chebyshev transfer expression. It checks \(m=2,3,4\), including rational and unequal weights; verifies the exact magnetic characteristic identity for \(m=2,3\); and numerically cross-checks the gap identity and its finite-size behavior. The analytic proof, rather than finite enumeration, establishes the all-length assertions.

## Relationship to prior work

Heilmann and Lieb established real-rootedness for general nonnegative-weight monomer–dimer systems, and Wagner's 2008 work develops broader weighted matching zero-free theorems. The complex-gain determinant identity used in Step 1 is already supplied by the general cycle-contribution formula of Samanta and Kannan (2023), especially their Corollary 4.1. Earlier work on pendant-weighted molecular graphs and spectra, notably Mandal (2008), studies related band gaps for weighted pendant graphs; its full article was not accessible for direct comparison and the possibility of a stronger equivalent result remains a priority risk. Other literature on alternating-cycle spectra provides related transfer tools. The claim assessed here is specifically the **evaluated finite-size matching-root gap**, its exact quadrature formula and critical crossover for alternating pendant activities, not general real-rootedness, complex-gain representation, or generic spectral theory.

## Limitations

The result concerns a one-dimensional periodic decorated graph and a fixed pattern of strictly positive edge weights. It is a zero-location theorem for the finite monomer–dimer partition polynomial, not a phase-transition statement. The matching-root coordinate is a nonlinear reparametrization of physical dimer activity. Prior literature could contain an equivalent explicit special case that was not located; independent historical-priority review has not been performed.

## References

- O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190–232.
- D. G. Wagner, *Weighted enumeration of spanning subgraphs with degree constraints*, arXiv:0803.1659 (first public version 2008-03-11), https://arxiv.org/abs/0803.1659.
- A. Samanta and M. R. Kannan, *Bounds and extremal graphs for the energy of complex unit gain graphs*, arXiv:2312.17152 (first public version 2023-12-28), https://arxiv.org/abs/2312.17152.
- B. Mandal, *Eigenspectral Analysis of Pendant Vertex- and Pendant Edge-Weighted Graphs of Linear Chains, Cycles, and Stars*, Bulletin of the Chemical Society of Japan 81 (2008), 956–965, https://doi.org/10.1246/bcsj.81.956.
- S. Alikhani et al., *Graphs Whose Certain Polynomials Have Few Distinct Roots*, International Scholarly Research Notices (2013), https://doi.org/10.1155/2013/195818.
