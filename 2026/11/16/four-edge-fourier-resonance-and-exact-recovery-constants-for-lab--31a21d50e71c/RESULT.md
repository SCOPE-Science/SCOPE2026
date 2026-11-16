# Four-edge Fourier resonance and exact recovery constants for labelled unicyclic graphs

## Finding
Let \(\mathcal U_n\) be the family of connected simple graphs with vertex set \([n]\) and exactly \(n\) edges, for \(n\ge3\). Identify an edge set with its binary incidence vector in \(G_n=\mathbb F_2^{\binom n2}\), and define the unnormalized Walsh transform
\[
 W_n(S)=\sum_{H\in\mathcal U_n}(-1)^{|E(H)\cap S|},\qquad S\subseteq E(K_n).
\]
Let \(T_n f=\mathbf1_{\mathcal U_n}*f\) on the group algebra, with counting-measure convolution.

**Exact finite classification.** The operators \(T_3,T_4,T_7\) are invertible. At five vertices, \(\mathcal U_5\) contains \(222\) graphs, and precisely \(212\) of the \(1024\) Walsh multipliers vanish. Their zero-frequency weight distribution is \(10\) at weight \(1\), \(192\) at weight \(5\), and \(10\) at weight \(9\). Consequently \(\operatorname{rank}T_5=812\).

At six vertices, \(\mathcal U_6\) contains \(3660\) graphs. Precisely \(1200\) of the \(32768\) multipliers vanish, distributed by frequency Hamming weight as
\[
 (\text{weight},\text{zero count})=(4,420),(7,180),(8,180),(11,420).
\]
In particular, **no nonzero Fourier character of weight at most three vanishes**. A four-edge frequency \(S\) is a zero **if and only if** the four negative edges induce, together with isolated vertices on the six-vertex set, either a five-vertex path \(P_5\sqcup K_1\) (\(360\) labelled frequencies) or a triangle disjoint from an edge and an isolated vertex \(K_3\sqcup K_2\sqcup K_1\) (\(60\) frequencies). Thus
\[
 \boxed{\operatorname{rank}T_6=31568.}
\]
The smallest nonzero multiplier modulus equals \(4\) at both five and six vertices. The inverse convolution norm restricted to the recoverable Hilbert range is therefore exactly \(1/4\) in both cases.

Writing \(R_n=\operatorname{ran}T_n\), the **minimum endpoint projection norms among all real or complex linear projections** onto \(R_n\) are
\[
 \boxed{\lambda_1(R_5)=\lambda_\infty(R_5)=\frac{1013}{128},\qquad
 \lambda_1(R_6)=\lambda_\infty(R_6)=\frac{9077}{512}.}
\]

**Infinite parity consequence.** For all \(n\ge3\) with \(n\equiv3\pmod4\), \(|\mathcal U_n|\) is odd, so every Walsh multiplier is odd and \(T_n\) is invertible. The additional invertible rank \(n=4\) follows from the exact finite count. No converse is asserted beyond the checked ranks.

## Assumptions and scope
Graphs are undirected, simple and labelled. A unicyclic graph has exactly one undirected simple cycle, length at least three. Frequencies are arbitrary binary edge subsets, not merely vertex-switching signings. Unnormalized Fourier coefficients are integer signed sums; no probability normalization is inserted. The \(\ell^1\), \(\ell^2\), and \(\ell^\infty\) norms are counting-measure norms on the full binary edge group. Finite classifications concern \(3\le n\le7\) as stated, and the parity conclusion holds for an infinite congruence class.

## Proof
**1. Counting by the unique cycle.** Fix a cycle of length \(k\) on \(k\) chosen vertices. The remaining edges form a forest with exactly one prescribed cycle vertex in each component. The all-minors matrix-tree determinant of \(nI-J\) on the \(n-k\) nonroot vertices equals \(k n^{n-k-1}\) for \(k<n\), and the empty-forest count at \(k=n\) is \(1\). Multiplying by \(\binom nk(k-1)!/2\) possible cycles gives the classical exact count
\[
 U_n:=|\mathcal U_n|=\frac{(n-1)!}{2}\sum_{j=0}^{n-3}\frac{n^j}{j!}.
\]
At \(n=3,4,5,6,7\), these values are \(1,15,222,3660,68295\).

**2. Infinite parity.** Each summand \((n-1)!n^j/(2j!)\) is an integer. For odd \(n\ge5\), the final term \(j=n-3\) has two-adic valuation \(v_2((n-1)(n-2)/2)=v_2(n-1)-1\). Every earlier summand includes the additional even factor \(n-3\), so when \(n\equiv3\pmod4\) only the final summand is odd. Thus \(U_n\) is odd for all such \(n\). As \(W_n(S)\equiv U_n\pmod2\) for every sign pattern, no frequency vanishes. The case \(n=3\) follows directly.

**3. Exact signed cycle-and-forest formula.** For arbitrary signs \(\sigma_e=(-1)^{\mathbf1_{e\in S}}\), form the signed **net** Laplacian
\[
 (L_\sigma)_{uv}=\begin{cases}-\sigma_{uv},&u\ne v,\\ \sum_{w\ne u}\sigma_{uw},&u=v.\end{cases}
\]
For each undirected simple cycle \(C\), the principal minor indexed by \([n]\setminus V(C)\) is the weighted sum of forests rooted at the cycle vertices. Hence
\[
 W_n(S)=\sum_{C\text{ a simple cycle in }K_n}\left(\prod_{e\in C}\sigma_e\right)
 \det L_\sigma[[n]\setminus V(C)].\tag{1}
\]
The empty determinant is \(1\). This is an identity of integral polynomials in the edge weights, not a probabilistic approximation.

**4. Exhaustive six-vertex signed calculation.** A standalone C++17 proof checker (`verify.cpp`) evaluates all edge masks of sizes \(n\) on \(3\le n\le7\), retaining exactly the connected masks. Independently it generates each unicyclic mask from its unique simple cycle and a forest whose parent pointers all reach that cycle; the two sorted sets agree. At \(n=5,6\), it computes all integer Walsh coefficients by a butterfly transform and checks **every** coefficient against two independent formulas: the direct signed sum over generated graphs and equation (1) with exact integer determinants. All \(1024\) and \(32768\) frequencies are checked, respectively. In particular it checks every frequency of weight at most four at \(n=6\), recording that the \(420\) zeros of weight four are precisely the negative-edge graphs with sorted degrees \((0,1,1,2,2,2)\). A four-edge six-vertex graph has this degree pattern exactly when it is a five-vertex path plus an isolate, or a triangle and a disjoint edge plus an isolate. Their counts are \(6\cdot5!/2=360\) and \(\binom63\binom32=60\).

**5. Rank and sharp endpoint constants.** On the full finite abelian group, convolution is diagonal under the Walsh transform, so rank equals the number of nonzero multipliers and the positive-spectrum inverse norm is the reciprocal of the least positive absolute multiplier. Let \(\Omega_n=\{S:W_n(S)\ne0\}\). Its canonical projection has kernel
\[
 P_n(x)=2^{-\binom n2}\sum_{S\in\Omega_n}(-1)^{S\cdot x}.
\]
The checker takes a second exact Walsh transform of the binary support indicator and finds the numerator sums \(8104\) at \(n=5\) and \(580928\) at \(n=6\). Dividing by group orders \(1024\) and \(32768\) gives the displayed rational constants. For any projection onto this translation-invariant range, averaging its conjugates over all translations produces the unique translation-invariant projection with no greater endpoint norm. Thus the displayed canonical projection norms are minima over **all** projections, without assuming translation invariance at the outset.

## Verification
Compile and run `verify.cpp` using `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. The program executes exhaustive exact-integer checks and exits with `UNICYCLIC_WALSH_CERTIFICATE_PASS` only when all assertions succeed. `SPECTRA.txt` records the expected complete absolute-multiplier histograms and zero-weight profiles, including the complete frequency census for orders five and six. The signed-Laplacian formula is independently evaluated at every such frequency rather than inferred from the butterfly output. Integer Parseval consistency may additionally be checked directly from the frequency histograms.

## Relationship to prior work
Classical rooted-forest enumeration gives the unsigned numbers \(U_n\), and these counts are not new. The 2005 paper by van der Hofstad and Spencer studies counts of connected graphs by cyclomatic complexity, not individual edge-character Walsh cancellation. Goodall (2008) provides general finite-group Fourier and graph-polynomial techniques but not this signed unicyclic frequency census. Mallik's signed net-Laplacian matrix-tree theorem and his signless-Laplacian subgraph sums (2022/2023) are relevant determinant identities; the latter count odd-unicyclic components with different weights and allow disconnected components, and do not give the connected fixed-edge Fourier cancellation distribution above.

A prior public mathematical record, *Exact centered Walsh stability for uniform labelled unicyclic graphs* (2026; identifier `191cfc31fb25`), completely determines the **centered degree-one sampling Gram matrix** for the same unicyclic family. In particular, it already implies the vanishing single-edge Walsh coefficient at five vertices, so that fact is not claimed as independent novelty. Its first-band Gram theorem does not determine the full high-degree signed Fourier zero set, the six-vertex weight-four isomorphism types, convolution ranks, or unrestricted endpoint projections stated here. Neither the elementary parity argument nor general Fourier diagonalization alone is claimed as a new technique.

## Limitations
The exact zero set and endpoint constants are computed only at the stated small orders; there is no asserted complete spectral classification for arbitrary \(n\). Odd cardinality proves a sufficient infinite invertibility condition, not an if-and-only-if theorem for all ranks. The finite certificate is an exhaustive integer computation whose correctness is reproducible from source, not an externally certified formal proof. Historical-priority checks are bounded and do not rule out an unindexed equivalent exact signed enumeration. No independent mathematical audit has been performed.

## References
- R. van der Hofstad and J. Spencer, *Counting Connected Graphs Asymptotically*, arXiv:math/0502579v1 (first posted 2005-02-28), https://arxiv.org/abs/math/0502579.
- A. Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848v1 (first posted 2008-06-30), https://arxiv.org/abs/0806.4848.
- S. Mallik, *Matrix tree theorem for the net Laplacian matrix of a signed graph*, arXiv:2210.03711v1 (first posted 2022-10-07), https://arxiv.org/abs/2210.03711.
- *Exact centered Walsh stability for uniform labelled unicyclic graphs*, public mathematical finding record (2026), identifier `191cfc31fb25`.
