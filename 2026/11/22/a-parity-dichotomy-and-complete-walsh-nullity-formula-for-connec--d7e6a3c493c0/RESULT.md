# A parity dichotomy and complete Walsh nullity formula for connected sets of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite simple graph, where \(r\ge2\) and every part size \(n_i\ge1\). Set \(N=\sum_{i=1}^r n_i\). Let \(f_G:\mathbb F_2^N\to\{0,1\}\) indicate the **nonempty** vertex subsets that induce a connected subgraph. Convolution is unnormalized XOR convolution, \((T_Gu)(x)=\sum_y f_G(y)u(x+y)\). For a frequency subset \(S\subseteq V(G)\), put \(k_i=|S\cap V_i|\) and \(K=\sum_i k_i\). The complete Walsh multiplier formula is

\[
\widehat f_G(S)=
\begin{cases}
2^N-1-\displaystyle\sum_{i=1}^r(2^{n_i}-1-n_i),&S=\varnothing,\\[3pt]
N+r-1-2K-\displaystyle\sum_{i:k_i=0}2^{n_i},&S\ne\varnothing.
\end{cases}
\]

In particular, **the convolution operator is invertible precisely when \(N+r\) is even**. In this case its smallest absolute Fourier multiplier is exactly one, so the sharp \(\ell^2\) singular-value condition number is

\[
\kappa_2(T_G)=2^N-1-\sum_{i=1}^r(2^{n_i}-1-n_i).
\]

The formula below gives the exact full nullity for **every** multipartite shape. For each proper subset \(Z\subsetneq[r]\), let

\[
K_Z=\frac{N+r-1-\sum_{i\in Z}2^{n_i}}2.
\]

With the convention that a polynomial coefficient \([z^a]\) is zero when \(a\) is negative or not an integer, the nullity and rank are

\[
\nu_G=\sum_{Z\subsetneq[r]}[z^{K_Z}]\prod_{i\notin Z}\bigl((1+z)^{n_i}-1\bigr),
\qquad \operatorname{rank}(T_G)=2^N-\nu_G.
\]

For fixed \(r\) and \(\min_i n_i\ge cN\) with fixed \(c>0\), along sizes for which \(N+r\) is odd,

\[
\frac{\nu_G}{2^N}=\sqrt{\frac2{\pi N}}\bigl(1+O_r(N^{-1})\bigr)+O_r(2^{-cN}).
\]

For the opposite parity the nullity is identically zero, giving a sharp oscillation between complete recovery and a Gaussian-scale fraction of lost frequencies.

## Assumptions and scope
All parts are labelled and nonempty. The graph is simple, complete across different parts and edgeless within each part. Singleton induced subgraphs are considered connected; the empty induced subgraph is not counted. Frequencies run over every subset of the \(N\) vertex coordinates. All character values are \(\pm1\), and no probability normalization is applied to the Fourier transform or convolution. Rank, kernel and conditioning refer to \(T_G\) acting on complex-valued functions on the Boolean group, with the counting-measure \(\ell^2\) norm.

## Proof
**1. Connected-set decomposition.** A nonempty vertex set is connected if and only if it is a singleton or meets at least two multipartite parts. Thus the excluded subsets are the empty set and the subsets of size at least two contained in exactly one part. For \(h_i\), the indicator of size-at-least-two subsets supported in part \(V_i\), the disjoint decomposition is

\[
f_G=\mathbf1-\delta_0-\sum_{i=1}^r h_i.
\]

**2. Multipliers.** For a nonzero frequency \(S\), the constant function has Walsh transform zero, the delta mass at the empty set has transform one, and

\[
\widehat h_i(S)=\sum_{A\subseteq V_i}(-1)^{|A\cap S|}-1-\sum_{v\in V_i}(-1)^{\mathbf1_{v\in S}}
=2^{n_i}\mathbf1_{k_i=0}-1-n_i+2k_i.
\]

Substituting this into the decomposition gives the stated nonzero-frequency formula. At \(S=\varnothing\), direct cardinality counting gives the other branch. The characters of \(\mathbb F_2^N\) diagonalize \(T_G\), so each multiplier is an eigenvalue and singular-value magnitude.

**3. Exact parity criterion.** Because every \(n_i\ge1\), each \(2^{n_i}\) is even. For nonzero \(S\), \(\widehat f_G(S)\equiv N+r-1\pmod2\). The same congruence holds for the value at the empty frequency. Thus if \(N+r\) is even, every multiplier is odd and nonzero. Conversely, if \(N+r\) is odd, then \(N-r\) is a positive odd integer, and the integer \(K=(N+r-1)/2\) lies between \(r\) and \(N\). One can choose a frequency meeting each part with total size \(K\) by distributing \(K-r\) additional selected vertices among capacities \(n_i-1\). Its multiplier, for which no part is empty, equals zero. This establishes both directions.

**4. Sharp invertible conditioning.** The zero-frequency value \(M=|\operatorname{supp}f_G|\) is the largest multiplier magnitude by the triangle inequality. When \(N=r\), the graph is complete and every nonzero frequency has multiplier \(-1\). Otherwise, even parity forces \(N-r\ge2\). A frequency meeting every part in a total of \((N+r-2)/2\) coordinates exists by the same capacity argument, and its multiplier is exactly \(1\). All multipliers are nonzero integers, so no smaller positive singular value exists. Therefore \(\kappa_2=M\).

**5. Exact nullity.** Partition the nonempty frequencies by the set \(Z\) of parts completely missed. Frequencies with this exact \(Z\) have generating polynomial \(\prod_{i\notin Z}((1+z)^{n_i}-1)\) by total selected size. Their multiplier vanishes exactly when that size equals \(K_Z\). Sum the corresponding coefficients over all proper \(Z\). The empty frequency is not included, and its multiplier is strictly positive. This is an exhaustive disjoint partition, proving the rank and nullity formulas.

**6. Asymptotics.** In the singular parity let \(K_0=(N+r-1)/2\). Among all frequencies of weight \(K_0\), those missing some part number at most \(\sum_i2^{N-n_i}\). The zeros with at least one missed part also number at most \(\sum_{\varnothing\ne Z\subsetneq[r]}2^{N-\sum_{i\in Z}n_i}\). Therefore

\[
\nu_G=\binom N{K_0}+O_r(2^{N-\min_i n_i}).
\]

For fixed \(r\), \(K_0\) is within a bounded distance of the center, so Stirling's formula yields \(2^{-N}\binom N{K_0}=\sqrt{2/(\pi N)}(1+O_r(N^{-1}))\). The stated growth condition completes the proof.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. The program directly constructs every connected-set indicator, computes its entire integer Walsh–Hadamard transform and independently evaluates the block-count formula. It also evaluates the proposed nullity via coefficient products and checks both parity and sharp conditioning. It passed all **751 exact assertions** across **136 multipartite part-size vectors** with \(2\le r\le6\), each individual part size at most six and total vertex count at most eleven. These tests are finite corroboration only; the all-size conclusions follow from the proof above.

For example, part sizes \((2,2)\) yield no zero multipliers and largest absolute multiplier \(13\), whereas part sizes \((2,3)\) yield exactly \(12\) zero multipliers in a Boolean group of size \(32\). With part sizes \((3,4)\), the exact nullity is \(34\) out of \(128\).

## Relationship to prior work
Tittmann, Averbouch and Makowsky [1] introduce the subgraph component polynomial and, in Theorem 18 and Corollary 19, enumerate induced connected subgraphs of graph joins and complete bipartite graphs by **total cardinality**. Liao and Hou [2] prove that the subgraph component polynomial identifies complete bipartite graphs, again within ordinary graph-polynomial enumeration. These are the natural counting foundations and are not claimed as new. The present result concerns the **vertex-frequency-resolved signed Walsh transform**, XOR-convolution rank, a necessary-and-sufficient invertibility parity criterion, sharp recovery conditioning, and the nullity asymptotics for arbitrary complete multipartite shapes. The univariate subgraph component polynomial does not itself record which vertex coordinates carry negative signs in a character.

## Limitations
The theorem is confined to binary XOR convolution and to complete multipartite graphs with at least two nonempty parts. It does not cover arbitrary graph joins, weighted connected-set measures, or Fourier analysis over other finite groups. Finite verification is not a substitute for proof. Priority beyond the inspected literature remains subject to the possibility of older multivariate weighted connected-set enumerators that imply this specialization.

## References
[1] P. Tittmann, I. Averbouch, J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, arXiv:0812.4147 (first publicly posted 2008-12-22), especially Theorem 18 and Corollary 19. https://arxiv.org/abs/0812.4147

[2] Y. Liao, Y. Hou, *Note on the subgraph component polynomial*, arXiv:1311.6856 (first publicly posted 2013-11-27), especially Theorem 4.5. https://arxiv.org/abs/1311.6856
