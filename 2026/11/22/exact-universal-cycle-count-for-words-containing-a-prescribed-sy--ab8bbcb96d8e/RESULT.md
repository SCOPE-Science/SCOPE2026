# Exact universal-cycle count for words containing a prescribed symbol

## Finding

Let \(q\ge 2\) and \(n\ge 2\) be integers. Fix a labeled alphabet \(\Sigma\) of size \(q\) and one distinguished symbol \(0\in\Sigma\). A *required-symbol universal cycle* is a circular word over \(\Sigma\), of length \(q^n-(q-1)^n\), whose cyclic length-\(n\) windows are precisely the words of \(\Sigma^n\) that contain \(0\), each appearing exactly once. Identify two such cycles if and only if one is a rotation of the other; do not identify letter permutations or reversals.

The exact number of required-symbol universal cycles is

\[
\boxed{U_{q,n}=q^{q^{n-1}-(q-1)^{n-1}-n+1}\bigl((q-1)!\bigr)^{q^{n-1}-(q-1)^{n-1}}.}
\]

More strongly, the directed combinatorial Laplacian \(L_{q,n}\) of their length-\((n-1)\) overlap graph has characteristic determinant

\[
\boxed{\det(xI+L_{q,n})=x(x+1)^{(q-1)^{n-1}-1}(x+q)^{q^{n-1}-(q-1)^{n-1}}.}
\]

Consequently the graph has exactly \(q^{q^{n-1}-(q-1)^{n-1}-n+1}\) directed spanning in-arborescences rooted at any specified vertex. The binary specialization equals the classical number of binary de Bruijn cycles of order \(n\), although the two classes of cyclic words have different lengths.

## Assumptions and scope

The alphabet is labeled; \(q\) and \(n\) are arbitrary integers with \(q,n\ge2\). Factors are contiguous and cyclic, including wraparound. The exact-one requirement is imposed on all length-\(n\) factors containing \(0\); factors without \(0\) must be absent from the universal cycle. Distinctness is only modulo cyclic shifts of the complete word. All spanning-tree weights and factorials count directed edges individually.

Set \(m=n-1\), \(N=q^m\), \(s=(q-1)^m\), \(k=N-s\), and \(b=q-1\). Every length-\(m\) word is a vertex. The allowed directed edge from \(v_1\ldots v_m\) to \(v_2\ldots v_ma\) exists precisely when \(0\) occurs in \(v_1\ldots v_ma\). Thus a vertex containing \(0\) has in-degree and out-degree \(q\); a vertex avoiding \(0\) has both degrees one.

## Proof

**1. Eulerian correspondence.** Every vertex has balanced degree. Each vertex can reach \(0^m\) by appending zeros, since every appended length-\((m+1)\) window then contains zero. Conversely, the path from \(0^m\) obtained by appending the successive letters of any target length-\(m\) word uses only windows with at least one zero, since an initial zero survives until the last step. Therefore the graph is strongly connected. Its directed Euler tours correspond exactly to required-symbol universal cycles. The edge labeled \(0^n\) occurs exactly once, so fixing it as the first edge gives one representative of each cyclic rotation class.

**2. Laplacian decomposition.** Let \(B\) be the adjacency matrix of the complete \(q\)-ary de Bruijn shift on length-\(m\) words. Let \(T\) be the set of zero-free length-\(m\) words, of size \(s\), and let \(B_T\) be the adjacency matrix of the complete \(b\)-ary shift on \(T\). Let \(\iota\) inject vectors indexed by \(T\) into vectors indexed by all length-\(m\) words, and set \(C=bI_s-B_T\). Removing the edges whose complete length-\((m+1)\) labels avoid zero subtracts exactly \(\iota C\iota^{\mathsf T}\) from the full \(q\)-ary graph Laplacian. Thus

\[
L_{q,n}=qI_N-B-\iota C\iota^{\mathsf T}.
\]

In the de Bruijn adjacency matrix, there is exactly one length-\(m\) shift walk from any vertex to any other, hence \(B^m=J_N\), the all-ones matrix. Also \(B\mathbf1=q\mathbf1\), so its characteristic polynomial is \(t^{N-1}(t-q)\). Similarly \(B_T^m=J_s\) and \(\det(tI_s-B_T)=t^{s-1}(t-b)\). These statements include \(b=1\).

**3. Exact determinant factorization.** Work over the rational function field in \(x\), so all intermediate inverses exist. Put \(a=x+q\) and \(H=aI_N-B\). The matrix determinant lemma gives

\[
\det(xI_N+L_{q,n})=\det H\;\det\!\left(I_s-C\iota^{\mathsf T}H^{-1}\iota\right).
\]

For integers \(0\le j<m\), the \(T\times T\) block of \(B^j\) equals \(B_T^j\): a length-\(j\) path with both endpoint words zero-free necessarily appends only nonzero letters, and hence all intermediate words are zero-free. Using \(B^m=J_N\), the geometric inverse expansion yields

\[
\iota^{\mathsf T}H^{-1}\iota
=\sum_{j=0}^{m-1}\frac{B_T^j}{a^{j+1}}+\frac{J_s}{a^m(a-q)}.
\]

The analogous expansion for the smaller alphabet is

\[
(aI_s-B_T)^{-1}
=\sum_{j=0}^{m-1}\frac{B_T^j}{a^{j+1}}+\frac{J_s}{a^m(a-b)}.
\]

The two expressions differ by a scalar multiple of \(J_s\). Since \(CJ_s=0\), multiplication on the left by \(C\) annihilates that difference. Therefore

\[
I_s-C\iota^{\mathsf T}H^{-1}\iota
=I_s-C(aI_s-B_T)^{-1}
=(a-b)(aI_s-B_T)^{-1}.
\]

Consequently

\[
\det\!\left(I_s-C\iota^{\mathsf T}H^{-1}\iota\right)
=\frac{(x+1)^s}{(x+1)(x+q)^{s-1}}.
\]

Now \(\det H=x(x+q)^{N-1}\). Multiplication establishes the claimed characteristic determinant exactly as a polynomial identity, without extrapolating from finite cases.

**4. Arborescences and cycle count.** The coefficient of \(x\) in \(\det(xI+L_{q,n})\) is \(q^k\). By the directed matrix-tree theorem, this coefficient is the sum of all \(N\) rooted spanning in-arborescence counts. Since the graph is Eulerian, all principal Laplacian cofactors agree; each count is therefore \(q^k/N=q^{k-m}\). The directed BEST theorem counts tours beginning with the fixed edge labeled \(0^n\) as

\[
q^{k-m}\prod_{v}\bigl(d^+(v)-1\bigr)!=q^{k-m}\bigl((q-1)!\bigr)^k,
\]

because exactly \(k\) vertices have out-degree \(q\) and the remaining \(s\) have out-degree one. This gives the displayed formula. Each cyclic word has exactly one window \(0^n\), and therefore exactly one rotation beginning with that window; no further division by its length is valid or required.

## Verification

Run `python3 verify.py` using Python's standard library. The independent checker builds adjacency matrices from the permitted words, computes integer Laplacian determinants with fraction-free elimination, verifies the closed characteristic determinant at several integer arguments, and checks every rooted cofactor for the stated formula at the displayed sample parameters. It independently counts fixed-edge Euler tours by exact graph traversal in six small instances.

The replay produced `VERIFY_OK`, including exact cyclic counts \(1,2,16\) for the binary cases \(n=2,3,4\), \(2,864\) for the ternary cases \(n=2,3\), and \(6\) for the quaternary case \(n=2\). Further exact determinant tests cover \(q=2,3,4\) and several larger \(n\), including \(q=2,n=7\). These finite checks do not substitute for the general determinant proof above.

## Relationship to prior work

Leitner and Godbole's 2008 preprint on restricted universal cycles proves existence for password classes, which include a single prescribed required symbol; it does not count rotation classes or calculate the Laplacian spectrum. Blanca and Godbole's 2010 preprint (Theorem 11) proves existence for all words containing any prescribed set of required symbols; the singleton case is exactly the present underlying family, so **existence is prior work, not a new claim**. Their proof does not supply this exact enumeration. Sawada and Gabrić (2025) develop uniform random generation of several universal-cycle families using arborescences; their studied families and algorithms do not state this all-parameter count for one required letter.

The contribution here is the exact full-family enumeration and the simple three-eigenvalue characteristic determinant, not the general Euler-tour method or the existence of required-symbol universal cycles. Other enumerated constrained de Bruijn families impose different window conditions such as bounded nonzero weight, exact symbol multiplicity, or local avoidance; those statements do not imply the count for the entire one-required-symbol family. A hidden or unindexed equivalent spectral calculation remains possible.

## Limitations

Only a single required alphabet symbol is treated; the proof does not enumerate simultaneous requirements involving two or more distinct symbols. Words with no zero are entirely forbidden from the universal cycle. The theorem counts rotation classes with a fixed labeled alphabet, not reversal classes or equivalence under alphabet permutations. No claim is made about efficient direct ranking or uniform sampling. Originality is assessed against inspected accessible sources and indexed research; exhaustive global novelty cannot be guaranteed. No independent mathematical audit has been performed.

## References

1. A. Leitner and A. P. Godbole, *Universal Cycles of Restricted Classes of Words*, arXiv:0808.1309, publicly posted 2008-08-08. https://arxiv.org/abs/0808.1309
2. A. Blanca and A. P. Godbole, *On Universal Cycles for New Classes of Combinatorial Structures*, arXiv:1008.2251 (2010-08-13), Theorem 11. https://arxiv.org/abs/1008.2251
3. J. Sawada and D. Gabrić, *Random Generation of Universal Cycles and de Bruijn Sequences*, arXiv:2510.16545 (2025-10-18). https://arxiv.org/abs/2510.16545
4. The directed matrix-tree theorem and the de Bruijn–van Aardenne-Ehrenfest–Smith–Tutte (BEST) Euler-tour theorem, classical counting identities applied with labeled directed edges.
