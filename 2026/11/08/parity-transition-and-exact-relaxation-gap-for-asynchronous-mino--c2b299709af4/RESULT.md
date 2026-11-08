# Parity transition and exact relaxation gap for asynchronous minority on cocktail-party graphs

## Finding

For every integer \(m\ge2\), let \(G_m=K_{2m}-M_m\), where \(M_m\) is a fixed perfect matching. Thus the vertices are labelled pairs \(\{v_i^0,v_i^1\}\), with all edges except each pair's internal edge. At each discrete time step, a vertex is selected independently and uniformly from the \(2m\) vertices; its bit is replaced by the strict minority bit in its **closed neighborhood**, including the selected vertex itself. The closed neighborhood has \(2m-1\) vertices and hence no tie. Every other bit is retained.

Write \(R_m\) for the number of recurrent configurations and \(K_m\) for the number of closed irreducible communicating classes of this finite Markov chain. Then
\[
(R_m,K_m)=
\begin{cases}
\left(\binom m{m/2},\binom m{m/2}\right),&m\text{ even},\\[2mm]
\left((m+3)\binom m{(m-1)/2},1\right),&m\text{ odd}.
\end{cases}
\]
Every trajectory reaches the recurrent configurations almost surely; they are precisely the **maximum-cut** configurations of \(G_m\). For even \(m\), all of these configurations are absorbing. For odd \(m\), there is a single nonabsorbing class with uniform stationary distribution and an exact discrete-time spectral gap
\[
\boxed{\gamma_m=\frac{d+1-\sqrt{(d+1)^2-2}}{2m},\quad d=\frac{m+1}{2},\qquad m\ge3\text{ odd}.}
\]
In particular \(\lim_{m\to\infty,\ m\text{ odd}}m^2\gamma_m=1\). The odd-class transition graph is obtained by replacing every edge of the middle-level inclusion graph between subsets of sizes \((m-1)/2\) and \((m+1)/2\) with **two internally vertex-disjoint paths of length two**. The gap and the parity transition concern this specified asynchronous minority rule, not synchronous majority/minority or XOR updates.

## Assumptions and scope

Bits are labelled and distinguishable; there is no quotient by graph automorphisms or by binary complementation. The chain has a self-loop when the selected bit already equals its closed-neighborhood minority. A recurrent communicating class means a closed strongly connected component of the full transition digraph, and a configuration is recurrent if it lies in such a class. The spectral gap is \(1-\lambda_2(P)\), with eigenvalues in decreasing order for the unique odd-\(m\) recurrent transition matrix \(P\). The numerical results and proofs start at \(m=2\); no generalization to weighted sites, positive-temperature Glauber dynamics or other update conventions is asserted.

## Proof

**1. Update and cut formulas.** Let \(S\) be the total number of bit-one vertices and let \(k\) count pairs whose two bits disagree. If the mate of a selected vertex has bit \(b\), the selected vertex's closed neighborhood contains exactly \(S-b\) ones out of \(2m-1\) sites. Therefore its new bit is one exactly when \(S-b\le m-1\). This has three regimes: when \(S<m\), all selected sites become one; when \(S>m\), all selected sites become zero; and when \(S=m\), a selected site copies its mate. The number of edges joining opposite bits, the cut \(c\), is
\[
c=S(2m-S)-k=m^2-(S-m)^2-k.
\]
Here \(S\equiv k\pmod 2\), because a homogeneous pair contributes zero or two ones, while a mixed pair contributes one. Each bit flip selected by the minority rule weakly increases \(c\): it changes only edges incident to the selected vertex and it is the strictly better anti-coordination response when a flip is made.

**2. The maximum-cut locus.** If \(m\) is even, equality \(c=m^2\) requires \(S=m,k=0\). These are exactly the configurations with \(m/2\) homogeneous one-pairs and \(m/2\) homogeneous zero-pairs; there are \(\binom m{m/2}\) and the update rule fixes each. If \(m\) is odd, parity excludes \(S=m,k=0\). The optimal cut is \(m^2-1\), achieved precisely by either \(S=m,k=1\), or \(S=m-1,k=0\), or \(S=m+1,k=0\). Put \(r=(m-1)/2\). The two homogeneous types each contribute \(\binom mr\) configurations, and the mixed type contributes \(2m\binom{m-1}r\). Since \(\binom mr=2\binom{m-1}r\) for \(m=2r+1\), the total is \((m+3)\binom mr\). These maxima are closed under the update rule, because no update decreases the cut.

**3. Universal reachability of the maxima.** From any state with \(S<m\), selecting a zero vertex increases \(S\) by one. Repeating reaches \(S=m\), through a finite sequence of allowed transitions; analogously selecting ones when \(S>m\) reaches \(S=m\). If \(S=m\) and \(k\) exceeds the parity-minimal value (zero for even \(m\), one for odd \(m\)), choose a mixed pair and select its zero endpoint. This creates a homogeneous one-pair, changes \((S,k)\) to \((m+1,k-1)\), and is an allowed update. Choose the one endpoint of a *different* remaining mixed pair; under \(S=m+1\), that endpoint becomes zero, giving \((m,k-2)\). The two-step path strictly increases the cut by two. Iterate to a maximum. Consequently every initial state has a finite positive-probability path to the closed maximum-cut set. In a finite Markov chain, this excludes recurrent classes outside that set and implies almost-sure eventual entrance.

**4. Connectivity for odd \(m\).** A homogeneous optimal configuration with \(S=m-1\) has \(r\) one-pairs, represented by an \(r\)-subset \(A\) of the \(m\) pair labels. A homogeneous optimal configuration with \(S=m+1\) similarly has \(r+1\) one-pairs, represented by a set \(B\). The two configurations can communicate by two single-site flips through a mixed optimal configuration exactly when \(A\subset B\). Each inclusion \(A\subset B\) has **two** distinct mixed intermediates, obtained by choosing which of the two vertices of the differing pair is one. No other nontrivial recurrent transitions occur. Every transition can be reversed by selecting the same endpoint after the corresponding total-spin change. The inclusion graph of the two middle Boolean levels is connected (replace a label using a two-step inclusion path), so the doubled-edge subdivision is connected. It is therefore the unique closed irreducible class. Every nontrivial edge is traversed in either direction with probability \(1/(2m)\); the remaining probability is a self-loop, making the uniform distribution reversible and stationary.

**5. Exact gap.** Write \(d=r+1=(m+1)/2\), and denote the middle-level inclusion graph by \(H\). Each vertex of \(H\) has degree \(d\); after replacing each edge by two subdivided paths, an old vertex has degree \(2d\), each new vertex degree two. The unweighted Laplacian of the recurrent transition graph consequently has block form
\[
L=\begin{pmatrix}2dI&-B\\-B^{\mathsf T}&2I\end{pmatrix},
\]
where \(B\) records incidences of old vertices with all doubled subdivision vertices, and \(BB^{\mathsf T}=2(dI+A_H)\). Thus \(L\) has eigenvalues \(2\) on any kernel-only subdivision subspace, and every adjacency eigenvalue \(\lambda\) of \(H\) yields solutions of
\[
\mu=d+1\pm\sqrt{d^2+1+2\lambda}.
\]
The spectrum of \(H\), a classical middle-level graph result, is \(\pm(d-j)\) for \(j=0,1,\ldots,r\), with multiplicities \(\binom mj-\binom m{j-1}\) (put \(\binom m{-1}=0\)). The largest adjacency eigenvalue is \(d\), giving the unique Laplacian eigenvalue zero; its next largest eigenvalue is \(d-1\). Hence the smallest positive Laplacian eigenvalue is \(d+1-\sqrt{(d+1)^2-2}\), smaller than the kernel eigenvalue two. The recurrent transition matrix is \(P=I-L/(2m)\), proving the formula for \(\gamma_m\). Rationalizing the radical shows \(m^2\gamma_m\to1\) along odd integers.

## Verification

The standalone program `check_recurrent.py` builds all selected-vertex transitions from the literal closed neighborhoods, computes the strongly connected components, and identifies their closed classes for all \(m=2,3,4,5,6,7\). Across these six graph sizes it examines \(21{,}840\) labelled configurations, matching both the claimed recurrent populations and the independent maximum-cut census. Run `python3 check_recurrent.py`; its captured output is `recurrent_output.txt`.

An independent `check_spectrum.py` enumerates odd-\(m\) recurrent states and constructs their transition matrices from the local rule, verifies stochasticity and reversibility, constructs each middle-level inclusion matrix separately, checks its adjacency eigenvalues, and compares the numerical spectral gap against the exact formula for \(m=3,5,7\). Run `python3 check_spectrum.py` (requires NumPy); its captured output is `spectrum_output.txt`. These finite tests corroborate, but do not replace, the all-\(m\) proof above.

## Relationship to prior work

Regnault, Rouquier and Thierry's *Stochastic Minority on Graphs* supplies the fully asynchronous closed-neighborhood minority model and general cut-energy approach; its discussions of cliques, trees, paths, cycles, and bipartite structures do not state the cocktail-party recurrent-class parity transition or the present exact spectral gap. The complete graph is dynamically different from a complete graph with a perfect matching deleted.

The eigenvalues of the middle-level inclusion graph are established in the graph spectral literature (for example, Dalfó, Fiol and Mitjana's *On middle cube graphs*). Those eigenvalues are an **input**, not an independent novelty claim. The result here identifies a doubled-subdivision graph as the recurrent transition graph and combines the known spectrum with the actual stochastic update rates to obtain its exact mixing spectral gap.

Related published complete-multipartite parity-automaton and acyclic-orientation enumerations concern different operators (synchronous XOR and orientation signatures, respectively); their graph-family overlap does not imply this stochastic-minority classification. No absolute historical-priority assertion is made.

## Limitations

The gap is for the nonabsorbing recurrent class of odd-\(m\) graphs, not a global mixing-time bound from arbitrary starting states. For even \(m\) there are multiple absorbing classes, so no unique full-space stationary measure or corresponding irreducible spectral gap. No exact hitting-time distribution, tight total-variation mixing time, weighted update extension, or claim of independent verification is provided. Although the most relevant accessible primary texts and semantic-result comparisons were inspected, an unindexed older equivalent formulation cannot be ruled out.

## References

1. D. Regnault, J.-B. Rouquier, É. Thierry, *Stochastic Minority on Graphs*, LIP technical report (2008), HAL identifier `hal-00272271` (version 2, 15 April 2008); later arXiv `1011.5119` (2010). Full accessible text: https://ar5iv.labs.arxiv.org/html/1011.5119 .
2. C. Dalfó, M. A. Fiol, M. Mitjana, *On middle cube graphs*, Electronic Journal of Graph Theory and Applications **3** (2015), 133–145, DOI `10.5614/ejgta.2015.3.2.3`.
3. Standard middle-level inclusion-graph spectral decomposition, including the eigenvalue/multiplicity calculation given in reference 2.
