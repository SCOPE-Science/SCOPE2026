# The exact inverse-degree spectrum of cyclic Rule 150 necklaces

## Finding

Let \(n\geq1\). On indexed binary circular words \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\), define synchronous Rule 150 by
\[
F_n(x)_i=x_{i-1}\oplus x_i\oplus x_{i+1}.
\]
Let \([x]\) denote the necklace of \(x\), i.e. its orbit under cyclic rotation, with neither reversal nor complementation identified. For an output necklace \([y]\), let \(\delta_n([y])\) be the number of distinct input necklaces \([x]\) for which \([F_n(x)]=[y]\). This is a *one-step* inverse degree, not a count of labeled inputs or of temporal ancestors.

If \(3\nmid n\), every output necklace has inverse degree exactly \(1\). Suppose \(3\mid n\). For any indexed representative \(y\), define the three parity sums
\[
s_a(y)=\bigoplus_{\substack{0\le i<n\\ i\equiv a\ (\mathrm{mod}\ 3)}}y_i,
\qquad a\in\{0,1,2\}.
\]
Let \(p\mid n\) be the least cyclic period of \(y\), and let \(u=(y_0,\ldots,y_{p-1})\) be its primitive length-\(p\) block. Then the complete classification is
\[
\boxed{
\delta_n([y])=
\begin{cases}
0,&s_0(y),s_1(y),s_2(y)\text{ are not all equal},\\
4,&s_0(y)=s_1(y)=s_2(y),\ 3\mid p,\ s_0(u)=s_1(u)=s_2(u),\\
2,&\text{otherwise}.
\end{cases}}
\]
The three parity sums of \(u\) in the second case are taken over the \(p\)-cell primitive block. The criterion is independent of the choice of rotation representative: rotations permute the three residue classes.

Consequently the complete possible positive inverse-degree spectrum is \(\{1\}\) if \(3\nmid n\), and \(\{2,4\}\) among reachable outputs if \(3\mid n\), with degree \(4\) occurring as soon as \(n\ge6\) is a multiple of three. Neither degrees \(1\) nor \(3\) occur on a nonempty fiber when \(3\mid n\). For \(n=3^k\), \(k\ge1\), the only reachable degree-\(2\) necklaces are the two constant outputs; all other reachable necklaces have degree \(4\).

There is also an exact census. Write \(\mu\) for the Möbius function and \(\varphi\) for Euler's totient. For \(3\mid n\) and each \(d\mid n\), put
\[
H_n(d)=
\begin{cases}
2^d,&3\nmid d\text{ or }2\mid(n/d),\\
2^{d-2},&3\mid d\text{ and }n/d\text{ is odd}.
\end{cases}
\]
The number \(J(n)\) of output necklaces with at least one predecessor and the number \(B_4(n)\) with exactly four predecessor necklaces are
\[
\boxed{
J(n)=\frac1n\sum_{d\mid n}\varphi(n/d)H_n(d),\qquad
B_4(n)=\sum_{\substack{p\mid n\\3\mid p}}\frac1p\sum_{d\mid p}\mu(p/d)H_p(d).
}
\]
The numbers of degree-\(2\) and degree-\(0\) necklaces are respectively \(J(n)-B_4(n)\) and
\(\frac1n\sum_{d\mid n}\varphi(n/d)2^d-J(n)\). For \(3\nmid n\), all necklaces have degree \(1\), and their number is \(\frac1n\sum_{d\mid n}\varphi(n/d)2^d\).

Among *reachable* output necklaces for lengths divisible by three, the proportion of degree-\(4\) necklaces tends to one as \(n\to\infty\). In fact the number of degree-\(2\) necklaces is at most \(n2^{n/2}\), while \(J(n)\ge 2^{n-2}/n\).

## Assumptions and scope

All arithmetic is over \(\mathbb F_2\), all indices in a ring of size \(n\) are modulo \(n\), and all rotations are allowed. At \(n=1,2\) the repeated-neighbor convention is used literally: the two neighbors may refer to the same cell. The output's least period is measured in indexed cells, and any length-\(p\) primitive block is regarded as an indexed word on a separate ring of length \(p\). The global map is the standard simultaneous *elementary* Rule 150, not the different staggered/Floquet reversible automaton also called Rule 150 in parts of the physics literature. The statement concerns a single update and necklace quotient, not reflection equivalence.

## Proof

**1. Kernel and image.** The linear equation \(F_n(x)=0\) is the recurrence \(x_{i+1}=x_i\oplus x_{i-1}\). Its solutions are precisely the sequences \((a,b,a\oplus b,a,b,a\oplus b,\ldots)\). Thus \(\ker F_n=\{0\}\) when \(3\nmid n\), and, when \(3\mid n\), \(\ker F_n=K\) has four members. The nonzero members of \(K\) are cyclic shifts of one another, and rotation by one or two positions cyclically permutes them. If \(3\nmid n\), injectivity of this square linear map implies bijectivity, and its equivariant bijection of labeled states descends to a bijection of necklaces.

For \(3\mid n\), summing \(F_n(x)_i\) over any one residue class \(i\pmod3\) counts every input coordinate exactly once modulo two, so the three values \(s_a(F_n(x))\) are equal. The two resulting linear constraints are independent on \(\mathbb F_2^n\); their common solution space has dimension \(n-2\), exactly equal to \(\operatorname{rank}F_n\). Hence \(y\) is reachable if and only if \(s_0(y)=s_1(y)=s_2(y)\). Each reachable labeled \(y\) has precisely four labeled preimages, a coset \(x+K\).

**2. Passing from labeled preimages to necklaces.** Fix a reachable output representative \(y\) of least period \(p\). Since \(F_n\) commutes with the rotation \(R\), the distinct preimage necklaces over \([y]\) correspond exactly to orbits of the four-member labeled fiber \(F_n^{-1}(y)\) under \(\langle R^p\rangle\), the stabilizer of \(y\). There are no further identifications: any rotation mapping two members of the chosen fiber onto one another must fix \(y\), hence be a multiple of \(p\).

If \(3\nmid p\), the \(p\)-cell map \(F_p\) is invertible. There is therefore a unique \(p\)-periodic preimage \(x_0\) of the primitive block \(u\), repeated on the length-\(n\) ring. Its four lifts are \(x_0+K\); rotation by \(p\) fixes \(x_0\), fixes zero in \(K\), and permutes the three nonzero elements of \(K\) as a three-cycle. Consequently there are exactly two necklaces.

If \(3\mid p\), then \(R^p\) acts identically on \(K\). If \(u\) is in the image of \(F_p\), all four labeled lifts of its \(p\)-periodic preimages are fixed by \(R^p\), yielding four necklaces. If \(u\) is not in that image but \(y\) is reachable on the length-\(n\) ring, then for any preimage \(x\) the difference \(R^p x\oplus x\) is a nonzero element of \(K\), since otherwise \(x\) would be \(p\)-periodic and supply a preimage of \(u\). This difference is the same for all four preimages because \(R^p\) fixes \(K\). Thus \(R^p\) acts by a fixed nonzero translation on the four-member fiber, producing two two-cycles, hence exactly two necklaces. The reachability test for \(u\) is again equality of its three residue parities. This proves the pointwise classification.

**3. Census by stabilizers.** Suppose \(3\mid n\). An output of period dividing \(d\mid n\) is the repetition \(n/d\) times of an arbitrary length-\(d\) word \(v\). If \(3\nmid d\), the repetition count is divisible by three, so every residue parity of the length-\(n\) output is the same. If \(3\mid d\) and \(n/d\) is even, all three residue parities vanish. Otherwise reachability is equivalent to two independent parity constraints on \(v\). Hence the count of reachable outputs fixed by a rotation whose fixed words have period dividing \(d\) is exactly \(H_n(d)\). Burnside's lemma gives \(J(n)\).

For any \(p\) divisible by three, the number of *primitive* length-\(p\) words in the image of \(F_p\) equals \(G(p)=\sum_{d\mid p}\mu(p/d)H_p(d)\), by Möbius inversion on the least period. Each primitive necklace has \(p\) distinct representatives. The pointwise classification shows that a degree-\(4\) output on an \(n\)-ring has a unique least-period divisor \(p\mid n\) divisible by three, and its primitive block is counted by \(G(p)\). Conversely, repetition of every such primitive good block is reachable on the length-\(n\) ring, and has degree \(4\). Summing \(G(p)/p\) proves the stated formula for \(B_4(n)\); subtraction gives the remaining counts.

**4. Rare exceptional degrees and prime-power corollary.** If a reachable output has least period \(n\) with \(3\mid n\), its primitive block is the entire output and hence is in the image, so its degree is four. Therefore degree-\(2\) outputs must be periodic with some proper divisor \(p\mid n\), hence \(p\le n/2\). Counting all such words coarsely gives at most \(\sum_{p\mid n,\ p<n}2^p\le n2^{n/2}\) degree-\(2\) necklaces. The labeled image has \(2^{n-2}\) states and its necklaces have size at most \(n\), so \(J(n)\ge2^{n-2}/n\); the stated limiting proportion follows. If \(n=3^k\), every divisor is a power of three. The only output of least period not divisible by three is a constant word, yielding exactly two degree-\(2\) necklaces. Every other reachable output has \(3\mid p\), with an odd repeat count \(n/p\), so its primitive block must be reachable on its own ring and its inverse degree is four.

## Verification

The standalone file `verify_rule150_necklaces.py` performs independent exhaustive construction of all labeled Rule 150 transitions, collapses both source and target states by rotation, compares each observed necklace inverse degree with the pointwise formula for every \(1\le n\le18\), and compares the resulting complete histograms with the Möbius–Burnside formulas. It also checks the closed census identities for all multiples of three through \(60\). Its successful terminal line is `VERIFY_OK exhaustive_lengths=1..18 formula_censuses=3,6,..,60`. The brute-force part tests every binary word for the stated finite lengths; those finite tests are not treated as a proof for unbounded \(n\).

Some exact output-degree histograms \((B_0,B_2,B_4)\) are \((2,2,0)\) at \(n=3\), \((8,5,1)\) at \(n=6\), \((44,2,14)\) at \(n=9\), \((256,16,80)\) at \(n=12\), and \((10928,47,3627)\) at \(n=18\). Values are indexed by *output necklaces*, not by labeled outputs.

## Relationship to prior work

The 1983 elementary-cellular-automaton source introduces the standard rules. Martin, Odlyzko and Wolfram (1984) provide a polynomial treatment of additive cyclic automata, including Rule 150, and their reachability criterion covers the labeled-image component used here. Krawczyk (2013) compares finite-state network symmetry classes and observes similarities of Rules 105 and 150; its equivalence classes are not the literal cyclic-rotation necklaces here. Frati, Petak and Cheney (2024) explicitly form necklace networks for all 256 elementary rules and study their finite connectivity and cycle statistics, but do not state the all-length inverse-degree classification or its primitive-period Möbius census.

The full distinction is that *labeled* reachable Rule 150 outputs have four preimages when the ring length is divisible by three, whereas in the necklace quotient some of these collapse into the same orbit, giving exactly two or four according to the output stabilizer and primitive-block parity. This is not implied by the earlier Rule 90 inverse-degree classification: Rule 90 has a different kernel and is never bijective on odd rings. The source comparison is limited to inspected materials and searchable records, not a proof of absolute publication priority.

## Limitations

This theorem addresses only the one-step *synchronous* binary Rule 150 map with cyclic boundary conditions and the cyclic rotation quotient. It does not classify higher-step predecessors, the temporal cycle-length distribution, or necklaces modulo reversal. Full historical priority is not guaranteed; alternative descriptions under Rule 105, polynomial cyclic codes, or older phase-space diagrams may exist. No independent mathematical audit has been performed.

## References

1. S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics **55** (1983), 601–644. Published July 1, 1983. https://doi.org/10.1103/RevModPhys.55.601
2. O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic properties of cellular automata*, Communications in Mathematical Physics **93** (1984), 219–258. https://doi.org/10.1007/BF01223745 ; author-hosted open text https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf
3. M. J. Krawczyk, *New aspects of symmetry of elementary cellular automata*, 2013. https://arxiv.org/abs/1304.5771
4. L. Frati, C. Petak, N. Cheney, *Networks of Binary Necklaces Induced by Elementary Cellular Automata Rules*, 2024. https://arxiv.org/abs/2409.04780
