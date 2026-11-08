# Transient exact tightness of heat-kernel graph Gabor frames on irregular clique joins

## Finding
For every integer \(k\ge1\), let \(G_k=(2K_{5k})\vee(4K_{2k})\), where juxtaposition denotes disjoint union of the specified number of complete graphs and \(\vee\) joins every vertex on the left to every vertex on the right. This is a connected simple graph on \(18k\) vertices with two vertex orbits and distinct degrees \(13k-1\) and \(12k-1\). Construct the heat-kernel graph Gabor system with the combinatorial Laplacian, the entire orthonormal graph Fourier basis, and unweighted atoms as below. At \(t=0\) this frame is tight. **At exactly one additional finite time \(t_k>0\), it is tight, although the graph is not regular or vertex-transitive.** It is not tight at any other finite positive time.

Define the two functions
\[
\begin{aligned}
\gamma_{A,k}(t)&=\frac1{18k}+\frac1{10k}e^{-16kt}+\left(1-\frac1{5k}\right)e^{-26kt}+\frac2{45k}e^{-36kt},\\
\gamma_{B,k}(t)&=\frac1{18k}+\frac3{8k}e^{-20kt}+\left(1-\frac1{2k}\right)e^{-24kt}+\frac5{72k}e^{-36kt}.
\end{aligned}
\]
The entire frame-operator spectrum is \(\gamma_{A,k}(t)\) with multiplicity \(10k\) and \(\gamma_{B,k}(t)\) with multiplicity \(8k\); when equal they constitute one eigenvalue of multiplicity \(18k\). Its optimal squared frame bounds are their minimum and maximum.

The unique positive tightness time is characterized by \(t_k=-\log(x_k)/(2k)\), where \(x_k\in(0,1)\) is the unique root there of
\[
P_k(x)=4-15x^2-(40k-20)x^4+(40k-8)x^5-x^{10}.
\]
For \(0<t<t_k\), \(\gamma_{A,k}(t)<\gamma_{B,k}(t)\); for \(t>t_k\), the strict inequality reverses. In particular \(t_1=0.34663861547152\ldots\). As \(k\to\infty\),
\[
x_k\sim(10k)^{-1/4},\qquad t_k\sim\frac{\log(10k)}{8k}.
\]

## Assumptions and scope
Take the graph on \(18k\) labelled vertices, with group \(A\) consisting of two disjoint \(5k\)-cliques (size \(10k\)), group \(B\) of four disjoint \(2k\)-cliques (size \(8k\)), and all edges joining group \(A\) to group \(B\). There are no other edges. Let \(L=D-A_G\) be its unnormalized combinatorial Laplacian (\(A_G\) denotes graph adjacency). Let \(H_t=e^{-tL}\), and choose any orthonormal eigenbasis \(\phi_1,\ldots,\phi_{18k}\) of \(L\) in the counting-measure Hilbert space \(\mathbb C^{18k}\).

For each vertex \(i\), graph frequency \(j\), and real \(t\ge0\), define the graph Gabor atom by
\[
\psi_{ij}(t)(v)=H_t(v,i)\phi_j(v).
\]
No factor of \(\sqrt{18k}\), normalization of individual atoms, graph normalized Laplacian, or additional spectral weights is inserted. The frame operator is \(S_k(t)f=\sum_{i,j}\langle f,\psi_{ij}(t)\rangle\psi_{ij}(t)\). Its optimal frame bounds \(0<A\le B\) are determined by \(A\|f\|^2\le\sum_{i,j}|\langle f,\psi_{ij}(t)\rangle|^2\le B\|f\|^2\) for all \(f\in\mathbb C^{18k}\).

## Proof
**1. Frame operator.** Orthonormal completeness of the eigenbasis gives
\[
\sum_j|\langle f,\psi_{ij}(t)\rangle|^2
 =\sum_v|f(v)|^2|H_t(v,i)|^2.
\]
Summing over \(i\) and using symmetry and the semigroup identity gives
\[
S_k(t)=\operatorname{diag}\bigl(H_{2t}(v,v)\bigr)_{v\in V(G_k)}.
\]
This is positive definite for finite \(t\), since the diagonal of \(H_{2t}\) is positive. Permutations within cliques and among equal-sized cliques act transitively within each of the two groups \(A,B\). Hence there are at most two diagonal values.

**2. Exact heat diagonal.** The orthogonal Laplacian eigenspaces consist of: constants (eigenvalue \(0\)); differences of constants among the two \(A\)-cliques (eigenvalue \(8k\), dimension \(1\)); internal \(A\)-clique zero-sum vectors (eigenvalue \(13k\), dimension \(10k-2\)); differences of constants among the four \(B\)-cliques (eigenvalue \(10k\), dimension \(3\)); internal \(B\)-clique zero-sum vectors (eigenvalue \(12k\), dimension \(8k-4\)); and one group-constant vector orthogonal to the all-ones vector (eigenvalue \(18k\), dimension \(1\)). These dimensions total \(18k\).

At a vertex in group \(A\), the diagonal spectral-projector weights in eigenvalue order \(0,8k,13k,18k\) are respectively
\[
\frac1{18k},\quad\frac1{10k},\quad1-\frac1{5k},\quad\frac2{45k}.
\]
At a vertex in \(B\), the weights at \(0,10k,12k,18k\) are
\[
\frac1{18k},\quad\frac3{8k},\quad1-\frac1{2k},\quad\frac5{72k}.
\]
One way to check these weights is to split each group into its all-ones line, the orthogonal space of component-constant vectors, and the within-component zero-sum space. In particular, the group-difference eigenspace at eigenvalue \(18k\) contributes \(8k/(10k\,18k)=2/(45k)\) on group \(A\) and \(10k/(8k\,18k)=5/(72k)\) on group \(B\). Each displayed set of weights sums to one. Spectral expansion of \(H_{2t}\) gives the formulas for \(\gamma_{A,k}\) and \(\gamma_{B,k}\) and their multiplicities.

**3. Exactly one positive tightness time.** Set \(x=e^{-2kt}\). Direct subtraction and factorization yield
\[
\gamma_{A,k}(t)-\gamma_{B,k}(t)=\frac{x^8}{40k}P_k(x),\qquad
P_k(x)=(1-x)Q_k(x),
\]
where
\[
Q_k(x)=x^9+x^8+x^7+x^6+x^5+(9-40k)x^4-11x^3-11x^2+4x+4.
\]
The finite boundary \(t=0\) corresponds to \(x=1\), and the open range \(0<t<\infty\) corresponds bijectively to \(0<x<1\). Put \(y=x/(1-x)>0\), so \(x=y/(1+y)\). Then
\[
\begin{aligned}
(1+y)^9 Q_k\left(\frac{y}{1+y}\right)={}&4+40y+165y^2+360y^3\\
&+40(11-k)y^4+40(7-5k)y^5\\
&+(50-400k)y^6-40(1+10k)y^7\\
&-20(1+10k)y^8-40ky^9.
\end{aligned}
\]
For every integer \(k\ge1\), the ordered nonzero coefficients in this last polynomial have **exactly one sign change**. The constant coefficient is positive and the leading coefficient is negative; hence there is at least one positive root. By Descartes' rule of signs, there is exactly one positive root counting multiplicity. Thus \(Q_k\) has exactly one root \(x_k\) in \((0,1)\), and it is simple. The signs are determined by \(Q_k(0)=4>0\) and \(Q_k(1)=-40k<0\). Consequently the signs of \(\gamma_{A,k}-\gamma_{B,k}\) reverse at \(t_k=-\log(x_k)/(2k)\), giving the claimed complete tightness and sharp-bound classification.

**4. Asymptotic.** Reorganize the root equation as
\[
4=40k x_k^4(1-x_k)+15x_k^2-20x_k^4+8x_k^5+x_k^{10}.
\]
For any fixed \(\varepsilon\in(0,1)\), \(P_k(\varepsilon)\to-\infty\) as \(k\to\infty\), while \(P_k(0)=4\); uniqueness forces \(x_k\to0\). The displayed identity then implies \(40k x_k^4\to4\), which gives the stated asymptotics after taking logarithms.

## Verification
Execute `python verify.py` in the same directory (Python 3, SymPy, NumPy and SciPy). The script verifies the exact polynomial factorization and the transformed sign coefficients symbolically; checks the equality and strict ordering around the computed positive crossing for \(1\le k\le100\); verifies exact spectral projector weight sums for \(1\le k\le500\); and compares explicit formulas with the directly constructed \(18k\)-vertex and \(36\)-vertex graph Laplacian heat matrices for \(k=1,2\), including a direct eigenspectrum check. Its output was `GRAPH_HEAT_FRAME_VERIFY_PASS 1424 k1_t 0.34663861547152`. The sign-change proof and projector decomposition, not finite numerical sampling, cover every integer \(k\ge1\).

## Relationship to prior work
Buck and Okoudjou (first public February 24, 2024) define the heat-kernel graph Gabor system and identify its diagonal frame-operator eigenvalues with the squared heat-column norms. They prove tightness for all heat times on vertex-transitive and strongly regular graphs. The present construction **uses that framework**, but gives the stronger, different phenomenon of one *isolated positive heat time* with exact tightness on an **irregular** graph, and classifies this transition uniformly over an infinite graph family. Their general diagonal criterion does not state these graphs, this root classification or the single-crossing proof.

Ghandehari, Guillot and Hollingsworth prove a general sharp diagonal-bound criterion for a broad family of graph Gabor-type frames, which includes the mechanism of the heat-window frame bounds but does not assert the existence or uniqueness of an exceptional positive heat time on this graph family. Shuman, Ricaud and Vandergheynst formulate graph windowed Fourier frames and frame bounds; Perraudin et al. analyze graph heat-window concentration and design tight spectral filter banks. Their inspected constructions and results do not provide the isolated-temperature classification for this fixed, unmodified heat-kernel graph Gabor system. A separate family of *designed* tight graph filters must not be confused with automatic tightness of the single heat window at exactly \(t_k\). The standard general heat-spectral formula is acknowledged rather than claimed as new.

## Limitations
This theorem concerns only the specified unweighted graph family, counting-measure normalization, combinatorial Laplacian, complete graph Fourier basis, and unrescaled heat-kernel atoms. It does not assert that the example has minimum graph order, nor classify all graphs with transient exact tightness, nor establish robustness to graph-edge perturbations. Exact tightness at \(t=\infty\) is only a limiting statement and is not counted as a second finite positive time. The identified crossing is a mathematical exact equality; practical numerical implementation with finite precision yields approximate tightness. Historical priority remains conditional on a more comprehensive search for implicit consequences of earlier graph-heat centrality identities.

## References
1. Martin Buck and Kasso A. Okoudjou, *Tight Frames Generated By A Graph Short-Time Fourier Transform*, arXiv:2402.15902 (first public 2024-02-24), especially Theorems 3.1–3.2 and 4.2–4.3. https://arxiv.org/abs/2402.15902
2. David I. Shuman, Benjamin Ricaud, and Pierre Vandergheynst, *Vertex-Frequency Analysis on Graphs*, arXiv:1307.5708 (2013), Section 6. https://arxiv.org/abs/1307.5708
3. Nathanael Perraudin, Benjamin Ricaud, David I. Shuman, and Pierre Vandergheynst, *Global and Local Uncertainty Principles for Signals on Graphs*, APSIPA Transactions on Signal and Information Processing 7 (2018), DOI:10.1017/ATSIP.2018.2. https://doi.org/10.1017/ATSIP.2018.2
4. David I. Shuman, Christoph Wiesmeyr, Nicki Holighaus, and Pierre Vandergheynst, *Spectrum-Adapted Tight Graph Wavelet and Vertex-Frequency Frames*, arXiv:1311.0897 (2013). https://arxiv.org/abs/1311.0897
5. Mahya Ghandehari, Dominique Guillot, and Kris Hollingsworth, *Gabor-Type Frames for Signal Processing on Graphs*, arXiv:2009.06058 (first public 2020-09-13), especially Theorem 3.1 (general sharp frame-bound criterion). https://arxiv.org/abs/2009.06058
