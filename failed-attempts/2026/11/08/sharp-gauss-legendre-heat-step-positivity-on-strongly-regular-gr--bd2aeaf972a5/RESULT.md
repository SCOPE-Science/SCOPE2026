# Sharp Gauss–Legendre heat-step positivity on strongly regular graphs

## Finding

Let \(G\) be any finite connected, simple, noncomplete strongly regular graph with parameters \((v,k,\lambda,\mu)\), where \(0<k<v-1\) and \(\mu>0\). Thus each vertex has \(k\) neighbors, adjacent vertices have \(\lambda\) common neighbors, and nonadjacent vertices have \(\mu\) common neighbors. Write \(A\) for its symmetric adjacency matrix, \(L=kI-A\), and \(J\) for the all-ones matrix. Consider the semidiscrete heat equation \(u'(t)=-Lu(t)\).

The two-stage, fourth-order Gauss–Legendre Runge–Kutta method has the one-step matrix
\[
T_h=\left(I+\frac h2 L+\frac{h^2}{12}L^2\right)^{-1}
\left(I-\frac h2 L+\frac{h^2}{12}L^2\right),\qquad h\ge0.
\]
Define
\[
s=2k-\lambda+\mu,\quad p=\mu v,\quad
\Delta=v-2k+\lambda-\mu=v-s,
\]
\[
D(h)=144+72sh+12(s^2+p)h^2+6psh^3+p^2h^4.
\]
Then \(D(h)>0\) for all \(h\ge0\), and, for distinct vertices, the matrix entries depend only on whether the vertices are adjacent:
\[
\boxed{\quad
(T_h)_{ij}=\begin{cases}
\dfrac{12h(12+6\mu h-\mu\Delta h^2)}{D(h)},&i\sim j,\\[2mm]
\dfrac{12\mu h^2(6+sh)}{D(h)},&i\not\sim j.
\end{cases}\quad}
\]
Every diagonal entry is strictly positive for every \(h\ge0\), every nonedge entry is strictly positive for \(h>0\), and \(T_h\mathbf1=\mathbf1\). The **exact full-graph positivity frontier** is therefore
\[
\boxed{\quad T_h\ge0\text{ entrywise for all }h\ge0
\quad\Longleftrightarrow\quad\Delta\le0.\quad}
\]
When \(\Delta>0\), the entire set of positivity-preserving steps is the sharp closed interval
\[
\boxed{\quad T_h\ge0\text{ entrywise}
\quad\Longleftrightarrow\quad0\le h\le h_*(G),\qquad
h_*(G)=\frac{3+\sqrt{9+12\Delta/\mu}}{\Delta}.\quad}
\]
At \(h=h_*(G)\), all edge entries vanish; for every \(h>h_*(G)\) every edge entry is negative. All eigenvalues of \(T_h\) remain strictly positive and at most one for all finite \(h\ge0\), so spectral stability does not prevent the sign failure.

**Examples and structural consequences.** The Paley graphs of prime-power order \(q\equiv1\pmod4\) have \(\Delta=0\), hence are unconditionally positivity-preserving for arbitrarily large orders. The Petersen graph has \((v,k,\lambda,\mu)=(10,3,0,1)\), \(\Delta=3\), and \(h_*=1+\sqrt5\). At \(h=4\), its adjacent, nonadjacent, and diagonal entries are respectively \(-36/4123\), \(408/4123\), and \(1783/4123\). For the triangular graph \(T(m)\), the line graph of the complete graph on \(m\ge4\) vertices, \(\Delta=(m^2-7m+4)/2\): unconditional positivity holds precisely for \(4\le m\le6\); every \(m\ge7\) has a finite frontier, with \(h_*(T(7))=(3+\sqrt{15})/2\).

## Assumptions and scope

The graph is an actual finite connected noncomplete strongly regular graph, not an arbitrary feasible-looking parameter tuple. In particular \(A\) is symmetric, \(0<k<v-1\), \(\mu>0\), and the graph has diameter two. The timestep \(h\) is dimensionless relative to the unweighted unit edge rate of the Laplacian \(L=kI-A\). A common positive edge rate \(c\) replaces \(h\) by \(ch\). Componentwise positivity is required for every nonnegative input vector, exactly equivalent to entrywise nonnegativity of the end-step matrix. No claim is made about the internal Runge–Kutta stages.

## Proof

**1. Three-eigenvalue reduction.** Strong regularity gives the identity
\[
A^2=(k-\mu)I+(\lambda-\mu)A+\mu J,
\qquad A\mathbf1=k\mathbf1.
\]
On the orthogonal complement of \(\mathbf1\), the two (necessarily distinct) adjacency eigenvalues \(r>t\) satisfy \(x^2-(\lambda-\mu)x-(k-\mu)=0\). Connectivity makes \(k\) the simple largest adjacency eigenvalue. Therefore the two strictly positive nonzero Laplacian eigenvalues are \(a=k-r\) and \(b=k-t\), with
\[
a+b=2k-\lambda+\mu=s,
\qquad ab=(k-r)(k-t)=\mu v=p.
\]
The second equality follows directly by combining the quadratic eigenvalue relation with the standard double count \(k(k-\lambda-1)=\mu(v-k-1)\). Consequently
\[
(12+6ah+a^2h^2)(12+6bh+b^2h^2)=D(h),
\]
which is strictly positive.

**2. Exact end-step coefficients.** Let \(g(z)=(12+6z+z^2)/(12-6z+z^2)\). Then \(T_h=g(-hL)\). Its spectral expansion can be written as
\[
T_h=P_0+g(-ah)P_a+g(-bh)P_b,
\]
where \(P_0=J/v\) and the other spectral projectors are
\[
P_a=\frac{A-tI-(k-t)J/v}{r-t},\qquad
P_b=\frac{rI-A+(k-r)J/v}{r-t}.
\]
Substituting \(g(-x)=1-12x/(x^2+6x+12)\), putting terms over the product denominator \(D(h)\), and using \(a+b=s\), \(ab=\mu v\), yields the two displayed off-diagonal expressions. Equivalently, this calculation reduces modulo \(A^2=(k-\mu)I+(\lambda-\mu)A+\mu J\) to the \(I,A,J\) basis; thus there are only two types of off-diagonal entries. This is an identity of rational functions and holds for every eligible graph, not just tested examples.

**3. Diagonal positivity and exact threshold.** Since
\[
g(-x)=\frac{x^2-6x+12}{x^2+6x+12}
=\frac{(x-3)^2+3}{x^2+6x+12}\in(0,1)
\quad(x>0),
\]
and \(g(0)=1\), the spectral theorem makes \(T_h\) positive definite for all finite \(h\ge0\). In particular \((T_h)_{ii}>0\). Also \(T_h\mathbf1=g(0)\mathbf1=\mathbf1\). Because \(s>0\), \(\mu>0\), and \(D(h)>0\), all nonedge entries are positive for \(h>0\). The edge entry has the sign of the single quadratic \(12+6\mu h-\mu\Delta h^2\). If \(\Delta\le0\), that expression is positive for every finite \(h\ge0\). If \(\Delta>0\), it is initially positive and has exactly one positive zero, namely \(h_*=(3+\sqrt{9+12\Delta/\mu})/\Delta\), and becomes negative thereafter. At \(h=0\), \(T_0=I\). This proves all endpoints, both directions, and the full classification.

**4. Example families.** The Paley parameters \((q,(q-1)/2,(q-5)/4,(q-1)/4)\) give \(\Delta=0\). The Petersen parameters give \(\Delta=3\), and substituting \(h=4\) in the exact formulas produces the three stated rational entries. The triangular graph has \((v,k,\lambda,\mu)=(m(m-1)/2,2(m-2),m-2,4)\); direct substitution gives \(\Delta=(m^2-7m+4)/2\), negative at \(m=4,5,6\) and positive for every integer \(m\ge7\). Substituting \(m=7\) into the threshold gives the stated radical.

## Verification

The complete symbolic argument above is independent of finite enumeration. A standalone, dependency-free exact rational verifier is included as `verify_srg.py`. It reconstructs actual simple graphs and their strongly regular parameters for the five-cycle, Petersen graph, \(K_{4,4}\), Paley graph on 13 vertices, and triangular graphs \(T(6)\) and \(T(7)\). For each it checks the asserted closed formulas against the original matrix rational identity at five rational timesteps, for 30 exact matrix identities in all. It additionally checks row sums, symmetry, diagonal and off-diagonal signs, and the exact Petersen witness. Its deterministic console output is recorded as `verification.txt`. These tests are corroboration of the algebra, not an exhaustive check over all strongly regular graphs or all real timesteps.

## Relationship to prior work

The fourth-order Gauss–Legendre method and its \([2/2]\) Padé stability rational function are classical. Zappavigna, Colaneri, Kirkland and Shorten (2012) establish obstructions to positivity of high-order rational approximations for broad Metzler and Hurwitz matrix classes; they do not provide this fixed conservative, undirected, three-eigenvalue graph classification. Blanes, Iserles and Macnamara (first publicly posted February 16, 2021) develop a positivity-preserving graph-Laplacian integrator framework; their methods and general order-barrier discussion do not evaluate the present \([2/2]\) end-step entry signs for all strongly regular graphs. Standard strongly regular graph adjacency relations and spectral parameters are prior knowledge and not claimed new.

Related published results establish an eight-state sharp small-step obstruction for the same \([2/2]\) map on directed pure-birth Markov generators, and a reversible-chain resolvent criterion for the different \([1/1]\) Padé/Crank–Nicolson method. Neither entails the displayed \(\Delta\)-threshold for undirected strongly regular graphs. A previous exact periodic-cycle classification for the same integrator already covers the five-cycle example; that special case and its boundary are **not new here**. The claimed contribution is the arbitrary-strongly-regular-graph parameter classification and the new families and thresholds it implies, not the method, graph spectral identities, or five-cycle example.

## Limitations

The classification is restricted to unweighted, undirected, connected, noncomplete strongly regular graphs (and uniform positive rescalings of their Laplacians). It does not extend without proof to arbitrary regular graphs, weighted edges, nonreversible Markov generators, stage positivity, floating-point calculations, or nonlinear dynamics. Spectral stability here follows directly from symmetry; it is not a new stability theorem. The full text of all historical specialist numerical-positivity work has not been exhaustively inspected; overlapping prior results under three-eigenvalue association-scheme or rational Markov-kernel terminology remain a publication-priority risk. No independent review has been performed.

## References

1. S. Blanes, A. Iserles, S. Macnamara, “Positivity-preserving methods for ordinary differential equations” (preprint originally entitled “Positivity-preserving methods for population models”), first arXiv posting February 16, 2021, arXiv:2102.08242. https://arxiv.org/abs/2102.08242
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442. https://doi.org/10.1016/j.laa.2011.12.021 ; lawful full manuscript https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf
3. Z. Horváth, “Positivity of Runge–Kutta and diagonally split Runge–Kutta methods,” *Applied Numerical Mathematics* 28 (1998), 309–326. https://doi.org/10.1016/S0168-9274(98)00050-6
4. A. E. Brouwer, W. H. Haemers, *Spectra of Graphs*, Springer (2012). https://mathworld.wolfram.com/StronglyRegularGraph.html (standard parameters and adjacency identity).
5. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
6. “A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains,” published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a
