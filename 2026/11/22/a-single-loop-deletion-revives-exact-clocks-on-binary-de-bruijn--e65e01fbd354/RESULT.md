# A single loop deletion revives exact clocks on binary de Bruijn parity networks

## Finding
For every word length \(m\ge1\), removing exactly the self-loop at the all-zero word of the binary de Bruijn digraph transforms outgoing-neighbor parity dynamics over a finite characteristic-two field from complete extinction into a system with a recurrent clock of exact length \(m+2\). With \(N=2^m\) vertices, exactly \(m+1\) state-space dimensions become recurrent. The complete transient and temporal-orbit populations are given below.

## Assumptions and scope
Fix \(m\in\mathbb N\) with \(m\ge1\) and \(q=2^h\), \(h\ge1\). Let \(V=\mathbb F_q^{\{0,1\}^m}\). The graph contains an arc from each word \(w=(w_1,\ldots,w_m)\) to \((w_2,\ldots,w_m,b)\) for each \(b\in\{0,1\}\), including the self-loop at \(0^m\). Define the synchronous map
\[ (Ax)(w)=\sum_{b\in\{0,1\}}x(w_2,\ldots,w_m,b). \]
Let \(e\) be the coordinate vector at \(0^m\) and \(B=A+ee^{\mathsf T}\), which deletes that self-loop because the field has characteristic two. Write \(N=2^m\), and let \(T(x)\) be the smallest nonnegative time at which \(B^{T(x)}x\) lies on a temporal cycle. The term 'primitive period' always refers to time, not the length of a graph walk.

## Proof
**1. Original extinction.** Repeated substitution shows, for each integer \(0\le t\le m\),
\[ (A^t x)(w)=\sum_{a_1,\ldots,a_t\in\{0,1\}}x(w_{t+1},\ldots,w_m,a_1,\ldots,a_t). \]
The images are precisely the functions of the last \(m-t\) word coordinates: the sum over disjoint extension sets is surjective onto all such functions. Consequently \(\operatorname{rank}A^t=2^{m-t}\). At \(t=m\) the output is the constant total sum, which is nonzero for suitable inputs. One more application multiplies by two, hence \(A^{m+1}=0\) and the nilpotency index is exactly \(m+1\).

**2. A canonical recurrent cyclic subspace.** Put \(v_j=A^j e\) for \(0\le j\le m\). The coordinate \(v_j(w)\) is one exactly when the last \(m-j\) symbols of \(w\) are zero. These strictly nested suffix indicator functions are linearly independent, so \(W=\operatorname{span}(v_0,\ldots,v_m)\) has dimension \(m+1\). Every \(v_j\) is one at \(0^m\), and therefore \(Bv_j=v_{j+1}+v_0\) for \(j<m\), whereas \(Bv_m=v_0\). In this basis, \(v_0\) is a cyclic vector for \(B|_W\), with the exact minimal/characteristic polynomial
\[ h_m(z)=1+z+\cdots+z^{m+1}=\frac{z^{m+2}+1}{z+1}. \]
Its constant term is one, so \(B|_W\) is invertible. Its order is exactly \(m+2\): the displayed identity proves an upper bound, while a smaller positive order \(d<m+2\) would require \(h_m\mid z^d+1\). If \(d\le m\), the degree is too small; at \(d=m+1\), the two distinct monic degree-\(m+1\) polynomials cannot divide one another. As \(B\) induces \(A\) on \(V/W\), that quotient is nilpotent. Hence \(W\) is the *entire* recurrent subspace of \(B\).

**3. Every power rank.** For \(0\le t\le m\), the image of \(A^t\) consists of functions depending only on the last \(m-t\) symbols. The explicit suffix indicators show
\[ W\cap\operatorname{im}A^t=\operatorname{span}(v_t,\ldots,v_m),\qquad\dim(W\cap\operatorname{im}A^t)=m-t+1. \]
The quotient map induced by \(B\) is induced by \(A\). Since the invertible \(W\) splits off the nilpotent quotient, we therefore have
\[ \operatorname{rank}B^t=(m+1)+2^{m-t}-(m-t+1)=2^{m-t}+t\quad(0\le t\le m). \]
All later ranks equal \(m+1\). For \(m\ge2\), the last strict decrease is between \(t=m-2\) and \(t=m-1\), since \(\operatorname{rank}B^{m-2}=m+2\) and \(\operatorname{rank}B^{m-1}=m+1\). Thus the maximal transient is exactly \(m-1\). For \(m=1\), all states are periodic immediately.

**4. Complete transient and period census.** Let \(r_t=2^{m-t}+t\) for \(0\le t\le m\), and \(r_t=m+1\) for \(t\ge m\). The nilpotent Fitting summand has a time-\(t\) kernel of dimension \(N-r_t\). Therefore, with \(E_t=|\{x:T(x)\le t\}|\),
\[ E_t=q^{N+(m+1)-r_t}, \]
so the exact first-entry shell at any \(t\ge1\) is \(E_t-E_{t-1}\) and at zero is \(E_0=q^{m+1}\). The half of all binary configurations which need the last update when \(m\ge2\) follows by comparing ranks \(r_{m-2}=m+2\) and \(r_{m-1}=m+1\); over \(\mathbb F_q\) that fraction is \(1-q^{-1}\).

For each positive divisor \(d\mid m+2\), the number of recurrent states fixed by \(B^d\) is \(q^{\deg\gcd(h_m(z),z^d-1)}\). For each \(r\mid m+2\), write
\[ H_r=\sum_{d\mid r}\mu(r/d)\,q^{\deg\gcd(h_m(z),z^d-1)}. \]
Then \(H_r\) is the number of recurrent states of exact period \(r\), \(H_r/r\) the number of primitive temporal orbits, and the number of arbitrary initial states with least eventual period \(r\) and first periodic-entry time \(t\ge1\) is
\[ H_r\big(q^{N-r_t}-q^{N-r_{t-1}}\big). \]
For \(t=0\) it is \(H_r\). These statements include all times and all finite fields of characteristic two.

## Verification
Run `python verify_linear.py` (uses SymPy for independent integer characteristic polynomials) and `python verify_states.py` (direct successor simulation, no rank calculations). The first confirms the exact power-rank formula at word lengths one through seven and independent characteristic polynomials at lengths one through four. The second exhaustively tests all \(4+16+256+65,536=65,812\) binary initial states through word length four, including every entry shell and the period-dividing \(m+2\) condition. An exhaustive finite check corroborates but does not replace the proof for arbitrary lengths. The scripts do not use external downloaded papers or preexisting outputs.

## Relationship to prior work
The classical de Bruijn graph overlap construction and its canonical loops are standard [1]. Delorme–Tillich [2] describe the tensor/spectral structure of **unedited** de Bruijn and Kautz adjacency, predominantly over the complex field. Their claims do not provide the finite-characteristic, one-loop-deleted \(m+2\) clock or the full first-entry/primitive-period census. The published Kautz XOR classification [3] concerns a **different**, loop-free directed word graph and has a different periodic core. The contribution here is the exact spectral and dynamical effect of **deleting the existing all-zero self-loop**, not a new definition of the de Bruijn graph nor the unmodified adjacency spectrum.

## Limitations
The statement concerns the binary directed de Bruijn graph, one deleted constant-word self-loop, synchronous outgoing-neighbor sums, and characteristic-two fields. It makes no claim for undirected symmetrizations, arbitrary arc deletions, or other characteristics. Historical exhaustive searches cannot rule out unpublished or differently indexed equivalent calculations. No independent external validation has been performed.

## References
[1] A. Alhakim and M. Akinwande, *De Bruijn Graph Homomorphisms and Recursive De Bruijn Sequences*, arXiv:0812.4012v1 (first posted 2008-12-21), https://arxiv.org/pdf/0812.4012; definitions and graph-cycle constructions.
[2] C. Delorme and J.-P. Tillich, *The Spectrum of de Bruijn and Kautz Graphs*, European Journal of Combinatorics **19** (1998), 307–319, https://core.ac.uk/download/pdf/82810454.pdf; the unmodified directed adjacency's tensor/spectral structure.
[3] Published published-finding corpus record, *Parity-dependent Jordan structure and transient-depth census for Kautz XOR dynamics*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-parity-dependent-jordan-structure-and-transient-depth-census-for--165ad680a86f (a distinct graph with a different loop structure).
