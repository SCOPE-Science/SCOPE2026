# Parallel-line two-gate entropy loss in odd-order affine-plane graph states

## Finding

**Theorem (complete zero-, one-, and two-gate omission law).** Let \(\mathcal A\) be **any** finite affine plane of odd order \(q\ge3\), not necessarily Desarguesian. Its point set \(\mathcal P\) has \(q^2\) members and its line set \(\mathcal L\) has \(q(q+1)\) members. Prepare a pure qubit graph state with one qubit at each point and line, starting in \(\lvert+\rangle\) states and applying a controlled-\(Z\) gate for each point–line incidence. Write \(F\) for a set of **at most two distinct** incidence gates omitted during preparation. Across the bipartition of **all point qubits versus all line qubits**, the von Neumann and every positive-order Rényi entropy, in bits, equal

\[
S(F)=\begin{cases}
q^2-1,& F=\{(p_1,\ell_1),(p_2,\ell_2)\},\ \ell_1\ne\ell_2,\ \ell_1\parallel\ell_2,\\
q^2,&\text{otherwise.}
\end{cases}
\]

The exceptional case automatically has distinct point endpoints because parallel lines are disjoint. Thus an initially **maximally point–line entangled** graph state is immune to every single omitted gate, but two omitted gates lower its entanglement by exactly one bit **if and only if** their line endpoints are parallel. The reduced state has exactly \(2^{S(F)}\) equal nonzero eigenvalues, each \(2^{-S(F)}\).

For two incidences sampled uniformly without replacement from the \(q^2(q+1)\) available gates, the exact probability of one-bit entropy loss is

\[
\Pr\{S(F)=q^2-1\}=\frac{q(q-1)}{q^2(q+1)-1}=\frac1q+O(q^{-2}).
\]

This classification is a *two-gate* theorem, not a claim about arbitrary multi-gate faults or imperfect operations.

## Assumptions and scope

A finite affine plane of order \(q\) has \(q^2\) points, \(q+1\) parallel classes of \(q\) pairwise disjoint lines, and \(q\) points on each line. Every pair of distinct points lies on one common line; lines from different parallel classes meet at one point. Only these axioms and oddness of \(q\) are used. The incidence matrix \(B\in\mathbb F_2^{q^2\times q(q+1)}\) has \(B_{p\ell}=1\) exactly when \(p\in\ell\). Omitting incidence \((p,\ell)\) toggles this entry from one to zero in characteristic two. Gates are otherwise ideal and applied once. The bipartition is fixed throughout.

## Proof

**1. Exact graph-state entropy rule.** By the graph-state stabilizer bipartition rule of Hein–Eisert–Briegel [1], the reduced spectrum of an ideal graph state is flat and its entropy in bits is the rank over \(\mathbb F_2\) of the between-register adjacency matrix. Therefore \(S(F)=\operatorname{rank}_{\mathbb F_2}(B+E_F)\), where \(E_F=\sum_{(p,\ell)\in F}e_pe_\ell^{\mathsf T}\).

**2. The unperturbed incidence matrix has full row rank.** Each point lies on \(q+1\) lines and each distinct point pair determines one line, so in characteristic two

\[
BB^{\mathsf T}=I+J.
\]

Here \(J\) is the all-ones matrix of order \(q^2\). Since \(q^2\) is odd, the kernel of \(I+J\) is exactly the span of the all-ones vector \(\mathbf1\). Moreover \(B^{\mathsf T}\mathbf1=\mathbf1\), because every line contains odd \(q\) points. If \(B^{\mathsf T}x=0\), then \((I+J)x=0\), hence \(x=c\mathbf1\), forcing \(c=0\). Thus \(B^{\mathsf T}\) is injective and \(\operatorname{rank}B=q^2\).

**3. All binary row-codewords with support at most two.** The sum of the incidence columns of any one parallel class is \(\mathbf1\), since its lines partition the point set. Consequently every word \(c=B^{\mathsf T}x\), whose coordinates are labeled by lines, has the **same parity sum in every parallel class**, namely \(\sum_p x_p\pmod2\). A nonzero word with one nonzero coordinate violates this property. A word with exactly two nonzero coordinates satisfies it only if those two lines are **distinct and parallel**. Conversely, if \(\ell_1\) and \(\ell_2\) are distinct parallel lines, let \(x\) be the binary indicator of their union. Both selected lines meet this union in odd \(q\) points; every other line meets it in zero or two points. Therefore

\[
B^{\mathsf T}x=e_{\ell_1}+e_{\ell_2}.
\]

Injectivity from Step 2 shows that this \(x\) is the **unique** point vector mapped to this two-line codeword.

**4. Complete fault classification.** If the faulty matrix \(B+E_F\) loses row rank, some nonzero \(x\) satisfies \(B^{\mathsf T}x=E_F^{\mathsf T}x\). For \(|F|\le2\), the right side has line-support size at most two. By injectivity it cannot be zero, and by Step 3 it cannot be a singleton. Thus there must be two omitted gates on **distinct parallel lines**. This is necessary even if the two gates share a point or a line, since those arrangements never produce the required two distinct parallel-line coordinates.

Conversely, when the omitted gates belong to distinct parallel lines \(\ell_1,\ell_2\), the unique \(x=\mathbf1_{\ell_1\cup\ell_2}\) from Step 3 has coordinate one at the point endpoint of each omitted gate. Hence \(E_F^{\mathsf T}x=e_{\ell_1}+e_{\ell_2}=B^{\mathsf T}x\), giving a nonzero left kernel vector. Every possible nonzero left kernel vector must map to the same two-line codeword, so injectivity of \(B^{\mathsf T}\) makes this kernel exactly one-dimensional. Therefore the faulty rank is exactly \(q^2-1\), never lower. For every other fault set of size at most two, the rank remains \(q^2\).

**5. Exact random-fault probability.** There are \(M=q^2(q+1)\) distinct incidence gates. For each of \(q+1\) parallel classes, choose two of its \(q\) lines and then one of \(q\) incidences on each line. The number of unordered losing pairs is \((q+1)\binom q2q^2\). Dividing by \(\binom M2\) proves the displayed fraction, which tends to zero at order \(1/q\).

## Verification

The standalone `VERIFY.py` computes the incidence matrices and performs exact bitwise Gaussian elimination over \(\mathbb F_2\). It independently enumerates **every** one-gate fault and **every** unordered pair of distinct gate faults for prime orders \(q=3,5,7\), testing the actual rank against the geometrically predicted value. The exact two-fault counts are: \(108\) rank-losing pairs out of \(630\) at order three; \(1500\) out of \(11175\) at order five; and \(8232\) out of \(76636\) at order seven. In addition, it constructs the extension field \(\mathbb F_9\) explicitly and checks all \(810\) single faults plus \(5000\) reproducibly sampled pairs at order nine. The executed output is in `verification_output.txt`. Run `python3 VERIFY.py` using only the Python standard library. Finite verification is corroborative; the proof above covers **every** finite affine plane of odd order, whether or not coordinatizable.

## Relationship to prior work

Hein–Eisert–Briegel [1], especially Section III.B–C, establish the graph-state cut-rank formula and the general one-edge entanglement-change bound. These imply that the calculation can be expressed as a binary-rank problem, **not** which incidence-edge pairs cause rank loss. Severini [2] discusses maximal bipartite graph-state entanglement and matrix ranks, without this affine-plane two-fault placement classification in the inspected material. A published result on *even-order projective planes* [3] gives a different matching-omission theorem: its underlying projective incidence matrix is square, its base binary rank is generally deficient, and its entanglement increases when small matching gate sets are omitted. It does not directly imply the present full-row-rank odd-order **affine** criterion. The standard geometric facts about parallel classes and incidence codes are used, not claimed as new; the combined geometric two-fault iff, entropy formula and exact fault-count law are the assessed contribution. Searches of relevant records and primary literature have not established historical uniqueness.

## Limitations

The result does not address three or more omitted gates, noisy or partial controlled-phase gates, other partitions, or non-affine incidence graphs. The uniform random-fault probability concerns **exactly two** distinct gates sampled without replacement and is not a general reliability model. Although all odd-order affine planes are covered axiomatically, numerical checks cover only prime-field examples and a sampled prime-power example. Independent scientific validation and exhaustive historical priority verification have not been performed.

## References

1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, first publicly posted 18 July 2003, especially Section III.B–C, https://arxiv.org/abs/quant-ph/0307130 .
2. S. Severini, *Two-colorable graph states with maximal Schmidt measure*, arXiv:quant-ph/0511147, first publicly posted 15 November 2005, https://arxiv.org/abs/quant-ph/0511147 .
3. *Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes* (public research record, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-incidence-matching-fault-threshold-for-graph-state-entangl--0f1e8bff6768 .
4. D. Ghinelli, M. J. de Resmini, J. D. Key, *Minimum Words of Codes from Affine Planes*, Journal of Geometry (2009), DOI: 10.1007/s00022-008-2096-y. Its binary geometric-code setting is relevant, but its displayed abstract concerns characteristic-dividing-order cases, not the present odd-order binary failure law.
