# A seven-period invertibility criterion for maximal-independent-set convolution on paths

## Finding
For every integer \(n\ge1\), let \(P_n\) be the labelled path on vertices \(1,\ldots,n\). Let \(\mathcal M_n\subseteq\mathbb F_2^n\) consist of the vertex-incidence vectors of *inclusion-maximal independent sets* of \(P_n\), and let \(f_n=\mathbf1_{\mathcal M_n}\). On \(\mathbb F_2^n\), consider unnormalized counting convolution
\[
(T_n g)(x)=\sum_{y\in\mathbb F_2^n} f_n(y)g(x-y).
\]
Then the following is an exact all-length classification:
\[
\boxed{T_n\text{ is invertible}\iff n\bmod7\notin\{2,3,5\}.}
\]
In every exceptional length an explicitly specified Walsh character lies in the kernel. In every nonexceptional length *all* Walsh multipliers are odd integers, and hence nonzero.

## Assumptions and scope
The ambient field is \(\mathbb C\) (the same assertion holds over \(\mathbb R\)); the group is the binary additive vertex cube, and the graph is the **open path**, not the cycle. An independent set is *maximal* by inclusion, not necessarily maximum by cardinality. The unnormalized Walsh multiplier at a frequency \(S\subseteq[n]\) is
\[
W_n(S)=\sum_{I\in\mathcal M_n}(-1)^{|I\cap S|}.
\]
Fourier diagonalization makes \(T_n\) invertible exactly when \(W_n(S)\ne0\) for all \(S\). The case \(n=1\) is included: the only maximal independent set is \(\{1\}\), and both Fourier multipliers are units.

## Proof
**1. Unsigned path count and the seven-period parity obstruction.** Write \(M_n=|\mathcal M_n|\), with \(M_0=1\). An independent dominating set of a path either contains vertex 1, in which case it reduces to a maximal independent set on vertices 3 through \(n\), or contains vertex 2, in which case it reduces to one on vertices 4 through \(n\). Thus
\[
M_0=M_1=1,\quad M_2=M_3=2,\qquad M_n=M_{n-2}+M_{n-3}\quad(n\ge4).
\]
Reducing the recurrence modulo two, the three consecutive initial residues \((M_0,M_1,M_2)=(1,1,0)\) recur at indices 7, 8, 9, since \((M_7,M_8,M_9)=(7,9,12)\). Determinism of the recurrence implies periodicity with period seven. Consequently
\[
M_n\equiv0\pmod2\iff n\bmod7\in\{2,3,5\}.
\]
Since \(W_n(S)\) is the sum of \(M_n\) signs, \(W_n(S)\equiv M_n\pmod2\). It follows immediately that \(T_n\) is invertible when \(n\bmod7\notin\{2,3,5\}\).

**2. Signed recurrence.** Fix a frequency \(S\) and put \(s_j=-1\) if \(j\in S\), and \(s_j=1\) otherwise. Successive vertices selected in an inclusion-maximal independent set have separation two or three, the first selected vertex is 1 or 2, and the last selected vertex is \(n-1\) or \(n\). Let \(F_j\) be the signed sum of partial selected-position sequences ending at position \(j\) and satisfying the first-vertex and intervertex-gap requirements. Then
\[
F_1=s_1,\quad F_2=s_2,\quad F_3=s_1s_3,
\qquad F_j=s_j(F_{j-2}+F_{j-3})\quad(j\ge4),
\]
and for \(n\ge2\),
\[
W_n(S)=F_{n-1}+F_n.
\]
The formula for \(n=2\) uses only \(F_1,F_2\); the signed recurrence beginning at \(j=4\) applies whenever a seven-vertex extension is used below.

**3. An exact seven-vertex zero-preserving block.** Set
\[
V_j=(F_j,F_{j-1},F_{j-2})^\mathsf T,\qquad
A_s=\begin{pmatrix}0&s&s\\1&0&0\\0&1&0\end{pmatrix},
\quad V_j=A_{s_j}V_{j-1}\ (j\ge4).
\]
Append the signs \((+,+,+,+,+,-,+)\) to any existing frequency of length \(n\ge3\). The resulting seven-step product, in chronological application order, is
\[
B=A_{+}A_{-}A_{+}A_{+}A_{+}A_{+}A_{+}
=\begin{pmatrix}3&4&2\\-2&-3&-2\\2&2&1\end{pmatrix}.
\]
The row vector \(e=(1,1,0)\) satisfies the **integer identity** \(eB=e\). Thus
\[
W_{n+7}(S')=eV_{n+7}=eBV_n=eV_n=W_n(S).
\]
Here \(S'\cap[n]=S\) and \(S'\cap\{n+1,\ldots,n+7\}=\{n+6\}\). This is a constructive identity for the *actual signed Walsh coefficient*, not merely for its parity.

**4. Initial zero frequencies and completion.** Direct substitution into the signed recurrence gives
\[
W_2(\{1\})=W_3(\{1\})=W_5(\{1\})=W_9(\{4\})=0.
\]
For every larger exceptional length, take the base representative \(n_0=3\) if \(n\equiv3\), \(n_0=5\) if \(n\equiv5\), and \(n_0=9\) if \(n\equiv2\), and append the zero-preserving seven-block repeatedly until length \(n\). The lone remaining exceptional case is \(n=2\), already treated. Every exceptional residue class therefore has an explicit Walsh zero at every permitted length. Combined with step 1, this proves the stated equivalence.

## Verification
The standalone standard-library program `verify.py` independently enumerates every maximal independent set on paths with \(1\le n\le16\), performs an exact Walsh–Hadamard transform, verifies invertibility against the seven-residue classification, and checks the prescribed zero frequencies. It also multiplies the seven transfer matrices over the integers and checks the zero-frequency recursion for all exceptional lengths through 500. Run `python3 verify.py`; its intended final output is `PASS: 16 exhaustive Walsh spectra, seven-step transfer, 499 lengths`. These finite checks corroborate the theorem; the proof for every length is in the recurrence and integer matrix identity above.

## Relationship to prior work
Bisdorff and Marichal develop Perrin/Padovan enumeration and orbit formulas for maximal independent sets on cycles; their 2007 preprint is related through the permitted gaps of size two and three, but does not give vertexwise binary character sums for maximal independent sets on paths. Nagy's 2015 work reviews maximal independent set counting (the \(k=1\) case of independent domination) and develops extremal counting results for \(k\ge2\); those counts likewise do not establish the present convolution-invertibility criterion. General Fourier interpolation on independent-set supports concerns a different restriction matrix, not convolution by the maximal-independent-set indicator. The ordinary Padovan count, including its parity recurrence, is classical and is not claimed as new. The seven-step *signed cancellation construction* together with the exact if-and-only-if criterion is the asserted contribution.

## Limitations
This does **not** determine the nullity, complete spectrum, or sharp condition number when \(n\equiv2,3,5\pmod7\), nor does it make assertions about cycles or arbitrary graphs. The positive direction uses only parity and does not calculate the smallest nonzero multiplier. The originality assessment is bounded by accessible published material; a previously unindexed equivalent specialization of signed independence-domination polynomials cannot be excluded by search alone.

## References
1. R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647, first submitted 23 January 2007. https://arxiv.org/abs/math/0701647
2. Z. L. Nagy, *On the number of k-dominating independent sets*, arXiv:1504.03224, first submitted 13 April 2015. https://arxiv.org/abs/1504.03224
3. D. R. Wood, *On the number of maximal independent sets in a graph*, arXiv:1104.1243, first submitted 7 April 2011. https://arxiv.org/abs/1104.1243
4. The On-Line Encyclopedia of Integer Sequences, A000931 (Padovan sequence), https://oeis.org/A000931 (unsigned numerical context only).
