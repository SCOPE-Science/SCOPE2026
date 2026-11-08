# Uniform nonzero associative-commutator fibers in the group algebra of \(S_3\)

## Finding
Let \(K=\mathbb F_q\) be any finite field (\(q\) an arbitrary prime power), \(G=S_3\), and \(A=K[G]\). Put \(Z=Z(A)\) and \(W=\operatorname{span}_K\{ab-ba:a,b\in A\}\). The alternating bilinear commutator induces an isomorphism
\[
\Lambda^2_K(A/Z)\;\xrightarrow{\sim}\;W,\qquad \bar a\wedge\bar b\longmapsto ab-ba.
\]
In particular, every \(w\in W\) is a single associative commutator. The exact ordered-pair fiber size is
\[
\#\{(a,b)\in A^2:ab-ba=w\}=\begin{cases}
q^{10}+q^9-q^7,&w=0,\\
q^9-q^7,&0\ne w\in W,\\
0,&w\notin W.
\end{cases}
\]
Thus all \(q^3-1\) nonzero attainable outputs have identical fibers, even when the group algebra is not semisimple (characteristics \(2\) and \(3\)). The commuting probability follows as the zero-fiber corollary \(q^{-2}+q^{-3}-q^{-5}\). The prime-field zero-fiber consequence is already implied by Gao--Tang--Chen (2012); it is not asserted to be a newly discovered commuting probability.

## Assumptions and scope
The group algebra has the six ordinary group elements as a \(K\)-basis, with multiplication inherited from \(S_3\), and \([a,b]=ab-ba\) denotes the *additive associative-algebra* commutator, not a multiplicative group commutator. The theorem concerns all finite fields, including nonprime fields and the modular cases; no assumption on splitting or semisimplicity is used. We count ordered pairs of arbitrary algebra elements, not invertible pairs. In any characteristic, \(Z\) has dimension three: it consists of coefficient functions constant on each conjugacy class, with basis the three conjugacy-class sums.

## Proof
Put \(s=(12)\), \(t=(23)\), \(u=(13)\), \(r=(123)\), \(r'=(132)\), and write the identity as \(e\). The conjugacy classes are \(\{e\}\), \(\{s,t,u\}\), and \(\{r,r'\}\). The three independent class sums \(e\), \(s+t+u\), and \(r+r'\) span the center, by direct conjugation of group-algebra coefficients. Hence \(A/Z\) has basis \(\bar s,\bar t,\bar r\): after subtracting multiples of the class sums, every class is represented by their linear combination, and independence follows by comparing the coefficients at \(e,u,r'\).

For group elements \(g,h\), the elements \(gh\) and \(hg\) are conjugate, so their difference has coefficient sum zero separately in each conjugacy class. Let \(W_0\) be the subspace of all such coefficient vectors. It is three-dimensional, with two degrees of freedom on \(\{s,t,u\}\) and one on \(\{r,r'\}\). We have \(W\subseteq W_0\). Direct multiplication gives
\[
[s,t]=r-r',\qquad [s,r]=t-u,\qquad [t,r]=u-s.
\]
The three displayed vectors are linearly independent over **every** field (also in characteristics two and three) and span \(W_0\), so \(W=W_0\). Since elements of \(Z\) commute with everything, the bracket descends to an alternating bilinear map on \(A/Z\), hence to a linear map \(\Lambda^2_K(A/Z)\to W\). On the basis \(\bar s\wedge\bar t\), \(\bar s\wedge\bar r\), \(\bar t\wedge\bar r\), its images are exactly the three independent displayed commutators. Thus it is an isomorphism, with both spaces three-dimensional.

Every alternating two-vector in dimension three is decomposable: a nonzero two-vector has a two-dimensional support and can be expressed as \(v\wedge w\); zero is \(0\wedge v\). Therefore every element of \(W\) is a *single* bracket. Moreover, every choice of two cosets in \(A/Z\) has exactly \(|Z|^2=q^6\) lifts to an ordered pair in \(A^2\), all with the same commutator.

To count ordered pairs \((v,w)\in K^3\times K^3\) with a prescribed wedge, first consider the zero wedge. If \(v=0\), there are \(q^3\) choices for \(w\). If \(v\ne0\), there are \(q^3-1\) choices of \(v\), and \(w\) must lie on the line \(Kv\), giving \(q\) choices. Hence the zero-wedge fiber has \(q^3+(q^3-1)q=q^4+q^3-q\) pairs.

For a prescribed nonzero wedge \(\eta\), all representing pairs \((v,w)\) are ordered bases of the unique support plane of \(\eta\) with fixed determinant. The group \(\operatorname{SL}_2(K)\) acts freely and transitively on these bases, so the fiber size is \(|\operatorname{SL}_2(K)|=q(q^2-1)\), independent of \(\eta\). Multiplying both counts by \(q^6\) gives exactly \(q^{10}+q^9-q^7\) at zero and \(q^9-q^7\) at every nonzero output in \(W\). Since the exterior-square map is surjective onto \(W\), nothing outside \(W\) occurs. As a consistency check, the two fiber levels sum to \(q^{12}\) across the \(q^3\) attainable values. Dividing the zero count by \(|A|^2=q^{12}\) gives the stated commuting probability.

## Verification
The complete finite-field verifier in `verify.cpp` represents the six elements of \(S_3\) by permutations, implements group-algebra multiplication directly, and independently computes the bracket from the quotient exterior-square coordinates. It enumerates all \(q^{12}\) ordered pairs for each of \(q=2,3,4\); the order-four field uses polynomial arithmetic modulo \(X^2+X+1\). It checks direct multiplication against the wedge formula for **every pair**, and then compares the fiber size of **every** algebra element against the theorem. Reproduce with `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. Expected terminal marker: `VERIFY_OK`. Finite checks support, but do not replace, the field-independent proof above.

## Relationship to prior work
Gao, Tang, and Chen (2012) classified the commuting-graph components of \(\mathbb Z_p[S_3]\), including exceptional primes \(2\) and \(3\). Their graph results directly imply the number of zero commutators and several centralizer statistics over prime fields; these are not presented as new. The graph describes which pairs commute but does not record which **nonzero** additive commutator each noncommuting pair produces, nor the fiber size of each such output. Shumyatsky and Vannacci (2023), the motivating work on finite-ring commuting and product-zero probabilities, prove structural bounds rather than individual nonzero commutator-fiber formulas. Gardella and Thiel (2023) study ideal generation by commutators and sums of their products; this does not provide the exact ordered-pair law here. Related public work counts fibers for finite Kronecker path algebras, which are not group algebras of \(S_3\) and whose results do not imply this computation. The present result refines the **nonzero-value distribution** for a particular, structurally natural group algebra, uniformly over all finite fields. Publication priority has not been independently certified.

## Limitations
The theorem covers the six-dimensional group algebra of \(S_3\), not arbitrary finite groups or general coefficient rings. Over nonfields, the exterior-square and fiber arguments need modification. Previous commuting-graph results cover the zero-fiber consequence in prime-field cases; the contribution must not be taken to rediscover those counts. Further unlocated literature could contain an equivalent formula or a broader theorem. No independent mathematical audit has been performed.

## References
1. Y. Gao, G. Tang, J. Chen, *On Commuting Graph of Group Ring* \(\mathbb Z_nS_3\), Communications in Mathematical Research **28** (2012), 313–323. Full-text transcription: https://www.fx361.com/page/2012/1227/20156581.shtml ; publisher record: https://www.global-sci.com/cmr/article/view/8744 .
2. P. Shumyatsky, M. Vannacci, *Commuting and product-zero probability in finite rings*, first public preprint **2023-07-24**; https://arxiv.org/abs/2307.12633 .
3. E. Gardella, H. Thiel, *Rings and C*-algebras generated by commutators*, first public preprint **2023-01-14**; https://arxiv.org/abs/2301.05958 .
4. *Commutator fibers and commuting probabilities of finite Kronecker path algebras*, publicly indexed research summary, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d .
