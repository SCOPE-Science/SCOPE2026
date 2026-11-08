# Zero-error rigidity and divisor-sum census for finite-group translate families

## Finding
Let \(G\) be any finite abelian group, written additively, and let \(A\subseteq G\). Define the concept family \(\mathcal T(A)=\{A+g:g\in G\}\) on the universe \(G\), counting each distinct translate once. Then
\[
\operatorname{VCdim}\mathcal T(A)\le 1
\iff
A\in\{\varnothing,G\}\ \text{or}\ A\text{ is a coset of a proper subgroup or its complement}.
\]
If \(h_2(G)\) is the number of subgroups of index two, the exact number of subsets with this property is
\[
N_1(G)=2+2\sum_{H<G}[G:H]-2h_2(G).
\]
For a cyclic group of order \(n\ge1\), write \(\sigma(n)=\sum_{d\mid n}d\). Then
\[
N_1(\mathbb Z/n\mathbb Z)=2\sigma(n)-2\mathbf1_{2\mid n}.
\]
Among binary words of length \(n\) considered with cyclic shifts, the number with least period exactly \(n\) and shift-VC dimension at most one is
\[
P_1(n)=2n-2\mathbf1_{n=2}.
\]
In particular, if \(n\ge3\), the only primitive cyclic binary words in this class have exactly one one or exactly one zero.

There is also a quantitative refinement. With \(H_A=\{d\in G:A+d=A\}\) and \(B=G\setminus A\), the exact number of shattered unordered pairs is
\[
s_2(A)=\frac{|G|}{2}\,\left|\left((A-A)\cap(B-B)\right)\setminus H_A\right|.
\]
Thus the rigidity theorem identifies exactly when this natural second shattering coefficient vanishes.

## Assumptions and scope
Groups are finite and abelian, including the one-element group; the concept family contains only translates of a *single* subset, not arbitrary cosets of every subgroup. Shattering means that all Boolean traces on a support are realized. The empty set and the entire group have VC dimension zero. Every other subset has VC dimension at least one. The notation \(H<G\) means a proper subgroup, and distinct subsets, not translation orbits, are counted. The primitive-word convention uses least *positive cyclic period*.

## Proof
**1. Pair criterion.** Let \(B=G\setminus A\), and fix distinct query points \(x,y\), with difference \(d=y-x\ne0\). As the translating parameter varies, the trace \(\{x,y\}\) occurs exactly when \(d\in A-A\); the empty trace occurs exactly when \(d\in B-B\). The one-point traces are both present precisely when \(A+d\ne A\): each follows from the nonempty half of the symmetric difference, and both halves have equal size because translation preserves cardinality. Therefore the pair is shattered if and only if
\[
d\notin H_A,\qquad d\in(A-A)\cap(B-B).
\]
For each admissible difference there are \(|G|\) ordered pairs, while every unordered pair contributes exactly two directed differences, including when \(d=-d\). The formula for \(s_2(A)\) follows.

**2. Reduction by stabilizers.** Assume \(A\) is nonempty and proper and its translate VC dimension is at most one. Its stabilizer \(H_A\) is a subgroup. Since \(A\) is a union of \(H_A\)-cosets, it descends to a subset \(S\) of \(Q=G/H_A\). The stabilizer of \(S\) in \(Q\) is trivial, and shattering by translates of \(A\) on query points in different fibers is equivalent to shattering by translates of \(S\) on \(Q\). A pair in the same fiber cannot be shattered. It therefore suffices to show that one of \(S\) and \(T=Q\setminus S\) has size one.

Because \(S\) has trivial stabilizer, for every nonzero \(d\in Q\) both mixed traces occur. Hence absence of shattered pairs implies
\[
(S-S)\cap(T-T)=\{0\}.
\]
Write \(a=|S|\), \(b=|T|\), and \(N=|Q|=a+b\). If \(a<b\), then \(b>N/2\), so \(T\cap(T+d)\ne\varnothing\) for every \(d\in Q\), by the pigeonhole principle. Hence \(S-S=\{0\}\), forcing \(a=1\). The case \(b<a\) is symmetric. In the balanced case \(a=b\), inclusion-exclusion gives for every \(d\)
\[
|S\cap(S+d)|-|T\cap(T+d)|=2a-N=0.
\]
If \(a\ge2\), a nonzero difference of two points of \(S\) makes both intersections positive, a contradiction. Thus in every case \(S\) or \(T\) is a singleton. Pulling back along the quotient map proves that \(A\) is one \(H_A\)-coset or the complement of one.

Conversely, the translates of a proper subgroup coset form a partition of \(G\); no pair admits all four traces. Translates of the complement have exactly the Boolean complements of those traces, so they too shatter no pair. Every nonempty proper example shatters a singleton, proving the exact classification.

**3. Counting all such subsets.** For each proper subgroup \(H\), its cosets give \([G:H]\) distinct subsets and their complements give another \([G:H]\). A nonempty subgroup coset uniquely determines its subgroup through its difference set, so distinct proper subgroups do not duplicate cosets; similarly for complements. A coset and a complement can coincide only if both occupy half of \(G\), and then they are two cosets of the same index-two subgroup. Consequently the sum double-counts exactly two subsets per index-two subgroup. Adding the empty and total subsets yields \(N_1(G)\).

For \(G=\mathbb Z/n\mathbb Z\) there is exactly one subgroup of each index \(d\mid n\), and one subgroup of index two if and only if \(2\mid n\). Therefore
\[
N_1(\mathbb Z/n\mathbb Z)=2+2\sum_{d\mid n,\,d\ge2}d-2\mathbf1_{2\mid n}
=2\sigma(n)-2\mathbf1_{2\mid n}.
\]

**4. Primitive cyclic words.** Every cyclic binary word of length \(n\) is the repetition of a unique primitive word of length \(d\mid n\). Pullback under reduction modulo \(d\) preserves translate VC dimension: points in one fiber cannot be separated, and all traces on points in distinct fibers correspond to traces downstairs. Therefore \(N_1(n)=\sum_{d\mid n}P_1(d)\). Möbius inversion and the identity \(\sigma=\mathbf1*\mathrm{id}\) give
\[
P_1(n)=2n-2\mathbf1_{n=2}.
\]
The explicit form of the primitive words also follows directly from the triviality of their stabilizer and Step 2.

## Verification
The included standalone Python program `verify_translation_vc1.py` checks every binary subset of cyclic groups through order thirteen against the coset/complement characterization and the divisor-sum count. For cyclic groups through order ten it additionally computes all Boolean traces on each two-point support directly and checks the exact pair-count formula. It independently checks the classification on elementary abelian groups of ranks two and three. Invoke `python3 verify_translation_vc1.py`; its final line is `ALL_LOW_VC_TRANSLATION_CHECKS_PASS masks=16382 n=1..13 direct_n=1..10`. These are finite confirmations; the unrestricted finite-group statement is established by the proof above.

## Relationship to prior work
Conant, Pillay and Terry (first public version February 12, 2018) established structural and regularity results for sets in finite groups with bounded translate VC dimension. The present statement concerns the special zero-error endpoint of VC dimension one, identifying *all* exact examples and enumerating them; their quantitative approximate regularity conclusions are not claimed as new. Johnson (2021) analyzed VC dimension of binary strings via finite substrings and one-sided windows and classified low-complexity strings in that setting. A complete cyclic-shift orbit of a word is a different concept family from all its finite substrings; that paper's one-sided classification is not presented as the cyclic theorem here. No complete subgroup-coset rigidity statement with the divisor-sum and primitive-word counts was located in the inspected sources. The absence of a database match does not establish priority.

## Limitations
This is a finite-group result for translate VC dimension at most one, not a classification at higher VC dimensions, nor a stability or regularity theorem for infinite groups. The subgroup classification is elementary and may be folklore under an unsearched equivalent formulation; its historical novelty is not independently certified. Only finite computational ranges were tested, with the universal claims resting on the stated proof.

## References
1. G. Conant, A. Pillay, C. Terry, *Structure and regularity for subsets of groups with finite VC-dimension*, arXiv:1802.04246, first public February 12, 2018; J. Eur. Math. Soc. 24 (2022), 583–621. https://arxiv.org/abs/1802.04246
2. H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first public January 16, 2021. https://arxiv.org/abs/2101.06490
3. O. Sisask, *Convolutions of sets with bounded VC-dimension are uniformly continuous*, arXiv:1802.02836, first public February 8, 2018. https://arxiv.org/abs/1802.02836
