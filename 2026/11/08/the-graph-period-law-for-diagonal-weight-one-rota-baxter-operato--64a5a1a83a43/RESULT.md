# The graph-period law for diagonal weight-one Rota–Baxter operators on evolution algebras

## Finding
Let \(K\) be an arbitrary field and let \(E\) be a finite-dimensional evolution algebra with natural basis \(e_1,\ldots,e_n\), \(e_ie_j=0\) for \(i\ne j\), and \(e_i^2=\sum_j a_{ij}e_j\). Suppose its structure digraph \(G\), containing \(i\to j\) precisely when \(a_{ij}\ne0\), is strongly connected and contains at least one directed edge. Write \(d\ge1\) for the gcd of the lengths of all directed cycles in \(G\), and \(\mu_m(K)=\{u\in K^\times:u^m=1\}\).

**Theorem.** The complete set of *diagonal* weight-one Rota–Baxter operators \(R(e_i)=r_ie_i\) is in explicit bijection with the disjoint union
\[
\{\mathrm{zero}\}\ \sqcup\ \{0\}\ \sqcup\ \big(\mu_{2^d-1}(K)\setminus\{1\}\big).
\]
The first parameter denotes \(R=0\). For the parameter \(0\), the operator is \(R=-\operatorname{id}\). For each \(u\in\mu_{2^d-1}(K)\setminus\{1\}\), fix a root vertex \(v_0\) and any directed path lengths \(h(v)\) from \(v_0\) to \(v\), and set
\[
R(e_v)=\frac{1}{u^{2^{h(v)}}-1}\,e_v.
\]
The result is independent of the chosen paths. Thus the number of such operators is \(1+|\mu_{2^d-1}(K)|\). In particular, over \(K=\mathbb F_q\),
\[
\boxed{\#\operatorname{DiagRB}_1(E)=1+\gcd(2^d-1,q-1).}
\]
Every nonzero diagonal weight-one operator is invertible. The answer depends on the digraph only through its period and **not at all** on its nonzero structure coefficients. Rescaling transfers the same count to any fixed nonzero Rota–Baxter weight.

## Assumptions and scope
The field may have any characteristic, including two. The natural basis is fixed: diagonal means diagonal **in that basis**. The graph must be strongly connected and contain a directed edge; for \(n=1\), this requires a nonzero loop coefficient. No associativity, perfection or nondegeneracy of the structure matrix is assumed. The theorem classifies *diagonal operators only*, not arbitrary off-diagonal Rota–Baxter operators.

A weight-one Rota–Baxter operator satisfies
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)+xy\bigr)\quad (x,y\in E).
\]
Since the identity is bilinear, checking all ordered basis pairs is sufficient.

## Proof
**Step 1: Edge equations and support.** When \(i\ne j\), both sides of the identity vanish for diagonal \(R\). For \(x=y=e_i\), comparison of the \(e_j\)-coefficient gives, for every edge \(i\to j\),
\[
r_i^2=(2r_i+1)r_j.\tag{1}
\]
If \(r_i=0\), equation (1) gives \(r_j=0\); if \(r_j=0\), it gives \(r_i=0\). As the underlying undirected graph is connected, either all \(r_i=0\) or all are nonzero. The first possibility is the zero operator. In the second, equation (1) also shows that \(2r_i+1\ne0\), without requiring that two be invertible in \(K\).

**Step 2: Squaring conjugacy.** For a nonzero solution define \(u_i=1+r_i^{-1}\). Then \(u_i\in K\setminus\{1\}\), and conversely \(r_i=(u_i-1)^{-1}\). Equation (1), divided by its nonzero terms, is exactly
\[
u_j=1+\frac{2r_i+1}{r_i^2}=\left(1+\frac1{r_i}\right)^2=u_i^2\quad\text{for every edge }i\to j.\tag{2}
\]
Thus a directed walk of length \(\ell\) sends its starting parameter \(u\) to \(u^{2^\ell}\). If \(u_{v_0}=0\), strong connectivity forces all \(u_i=0\), giving \(r_i=-1\) everywhere. Otherwise every \(u_i\) is nonzero.

**Step 3: Cycle-period necessity.** Fix a vertex \(v_0\). Along any positive-length closed directed walk at \(v_0\), of length \(L\), equation (2) yields \(u_{v_0}^{2^L-1}=1\). The gcd of lengths of positive closed walks at \(v_0\) equals \(d\): every closed walk decomposes into directed cycles; conversely, a cycle of length \(c\) at any vertex can be inserted between a path out from \(v_0\) and a path back, producing two closed walks whose lengths differ by \(c\). Hence
\[
\gcd_{L\text{ closed at }v_0}(2^L-1)=2^d-1,
\]
using the elementary identity \(\gcd(2^a-1,2^b-1)=2^{\gcd(a,b)}-1\). Bézout's identity applied in the multiplicative group yields \(u_{v_0}^{2^d-1}=1\), and \(u_{v_0}\ne1\) by definition.

**Step 4: Sufficiency and uniqueness.** Conversely, choose \(u\in\mu_{2^d-1}(K)\setminus\{1\}\) and a base vertex \(v_0\). For each vertex \(v\), select a directed path of length \(h(v)\). Any two such lengths differ by a multiple of \(d\), because appending the same directed return path from \(v\) to \(v_0\) produces two closed walks. Since \(u^{2^d}=u\), the value \(u^{2^{h(v)}}\) is independent of the path. Moreover it is never \(1\): the multiplicative order of \(u\) divides the **odd** integer \(2^d-1\), so taking a power of two preserves its order. The prescribed coefficients \(r_v=(u^{2^{h(v)}}-1)^{-1}\) therefore exist and satisfy equation (2) along each edge, hence equation (1) and the Rota–Baxter identity. Each solution is uniquely determined by the base parameter. Together with the zero and \(-\operatorname{id}\) cases, this proves the classification.

**Step 5: Finite-field formula.** The cyclic group \(\mathbb F_q^\times\) has order \(q-1\), so \(|\mu_m(\mathbb F_q)|=\gcd(m,q-1)\). The displayed formula follows. If \(\lambda\ne0\), then \(R\) has weight \(\lambda\) if and only if \(R/\lambda\) has weight one.

**A perfect non-monomial example.** Over \(\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\), take the four-dimensional evolution algebra with structure matrix
\[
\begin{pmatrix}
0&0&1&1\\0&0&1&\omega\\1&1&0&0\\1&\omega&0&0
\end{pmatrix}.
\]
The two off-diagonal \(2\times2\) blocks are invertible, hence the algebra is perfect; its graph is strongly connected, non-monomial and has period \(d=2\). Since \(\gcd(3,3)=3\), there are exactly four diagonal weight-one operators: zero, negative identity, and two operators with alternating diagonal coefficient pairs \((\omega,\omega,\omega^2,\omega^2)\) and \((\omega^2,\omega^2,\omega,\omega)\). This example displays arithmetic resonance on a perfect non-monomial graph. Conversely, over \(\mathbb F_8\), the directed three-cycle has period \(3\) and admits \(8\) diagonal weight-one operators; adding a single reverse edge to create a two-cycle changes the period to \(1\) and collapses the count to \(2\). Thus branching and interactions between distinct cycle lengths have a genuine global effect.

## Verification
The attached `verify.py` exhaustively tests every strongly connected labeled directed graph with at most three vertices and at least one edge, using all diagonal assignments over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8\). The checker implements the defining edge equations with exact prime-field and binary-extension-field arithmetic, independently calculates the graph period, and compares actual counts to the formula. It checks 894 graph/field configurations and 156,329 diagonal assignments, including the explicitly weighted four-dimensional perfect example. The logged result is `VERIFY_OK configurations=894 tested_directed_edges=5118 maps=156329 dense_perfect_example=4`. These finite tests corroborate but do not replace the all-dimensional proof.

## Relationship to prior work
Ladra and Murodov (2019) derive general Rota–Baxter coefficient equations and classify low-dimensional complex evolution-algebra examples; their explicit two-cycle example is consistent with the present period-two specialization. Qaralleh, Mukhamedov and Khakimov (January 2026), Section 5, study weight-one operators on **nilpotent maximal-nilindex** evolution algebras in characteristic zero and identify the rational recurrence \(f(x)=x^2/(2x+1)\). That recurrence is a key prior ingredient. However, their source has an acyclic triangular graph and does not determine the weight-one diagonal solution count on an arbitrary **strongly connected, possibly non-monomial** graph over every finite field. A previously obtained exact scheme classification for a single directed cycle already gives the same root-of-unity count in the cyclic monomial case (and scheme-theoretic multiplicities); a two-dimensional cycle classification likewise covers that special case. The present claim is specifically the extension to **arbitrary strongly connected graphs**, including graphs with multiple interacting cycle lengths, arbitrary nonzero edge coefficients and non-monomial perfect examples. Its new mechanism is the gcd of **all** graph cycle lengths, which can cause a one-edge collapse in the number of operators. It does not reclaim the previously established cycle formula or its scheme structure. No assertion about off-diagonal classification or independence from previous ingredients is made.

## Limitations
Only diagonal operators in the given natural basis are counted. Strong connectivity is essential for the one-parameter classification; general digraphs can have multiple components and asymmetric restrictions. The result does not classify all weight-one Rota–Baxter operators, does not classify operators up to change of natural basis, and does not establish historical priority beyond the sources inspected. A fully comprehensive historical bibliography could still reveal an implicit earlier equivalent theorem.

## References
1. I. Qaralleh, F. Mukhamedov, O. Khakimov, *Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669, first posted January 13, 2026, especially Section 5. https://arxiv.org/abs/2601.08669
2. M. Ladra and S. N. Murodov, *On chains and Rota-Baxter operators of evolution algebras*, arXiv:1906.09098, first posted June 19, 2019, especially Section 3. https://arxiv.org/abs/1906.09098
3. I. Qaralleh, F. Mukhamedov, O. Khakimov, *Local Rota--Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex*, arXiv:2606.22623, first posted June 21, 2026. https://arxiv.org/abs/2606.22623
