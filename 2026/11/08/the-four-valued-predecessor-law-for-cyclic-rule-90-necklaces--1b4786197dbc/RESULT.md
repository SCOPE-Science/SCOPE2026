# The four-valued predecessor law for cyclic Rule 90 necklaces

## Finding
For each integer \(n\ge1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the binary cellular automaton
\[
(F_n(x))_i=x_{i-1}\oplus x_{i+1},\qquad i\in\mathbb Z/n\mathbb Z,
\]
with both neighbor subscripts taken modulo \(n\). Write \([x]\) for the necklace (cyclic rotation orbit) of \(x\), identifying neither reversal nor complementation. Define \(b_n([y])\) as the number of distinct input necklaces \([x]\) with \([F_n(x)]=[y]\).

**Theorem (complete inverse-degree classification).** Write \(p\) for the least positive period of \(y\), \(t=n/p\), and \(u=(y_0,\ldots,y_{p-1})\) for its primitive block. All congruences in the following cases are modulo two.

1. If \(n\) is odd, \(b_n([y])=2\) when the total number of ones of \(y\) is even, and \(b_n([y])=0\) otherwise.
2. If \(n\) is even and \(p\) is odd, put \(e=\sum_{i=0}^{p-1}u_i\pmod2\). If \(e=0\), then \(b_n([y])=3\). If \(e=1\), then \(b_n([y])=1\) exactly when \(4\mid t\), and \(b_n([y])=0\) otherwise.
3. If \(n\) and \(p\) are even, let \(a=\sum_{0\le i<p,\ i\text{ even}}u_i\pmod2\) and \(c=\sum_{0\le i<p,\ i\text{ odd}}u_i\pmod2\). If \(a=c=0\), then \(b_n([y])=4\). Otherwise \(b_n([y])=2\) exactly when \(2\mid t\), and \(b_n([y])=0\) when \(t\) is odd.

These mutually exclusive cases classify every output necklace, whether or not it is attainable. The bound \(0\le b_n([y])\le4\) is sharp, and all five values occur simultaneously at length \(n=8\): outputs `00000001`, `11111111`, `00010001`, `00000000`, and `00000101` have respectively \(0,1,2,3,4\) input necklaces.

## Assumptions and scope
The words are indexed binary words of the *same* fixed positive length. Only spatial rotations are factored out; a word and its reversal or bitwise complement are not automatically identified. The map is one *synchronous* update, not an asynchronous update or a time-iterated map. The definition is literal even for lengths \(n=1\) and \(n=2\), when the left and right neighbors coincide. The primitive block \(u\) need not have even weight and its parity statistics are invariant under changes of representative in the relevant cases (for even \(p\), a one-step rotation interchanges \(a\) and \(c\), preserving the predicate \(a=c=0\)).

## Proof
**1. Labeled fibers.** The rule is linear over \(\mathbb F_2\). A vector lies in its kernel exactly when \(x_{i-1}=x_{i+1}\) for every \(i\), so kernel vectors have period dividing two. For odd \(n\), the kernel consists of the two constant vectors, hence has dimension one. The image is therefore exactly the even-weight subspace: all outputs have even total parity, and this codimension-one condition is sufficient by rank-nullity. For even \(n\), the kernel consists of the four vectors constant separately on even and odd sites, hence has dimension two. Every output has zero sum on the even sites and zero sum on the odd sites, and these independent conditions are sufficient because their subspace has codimension two. Consequently every attainable *labeled* word has two predecessors if \(n\) is odd, or four if \(n\) is even; unattainable words have none. These statements hold at \(n=1,2\) directly.

**2. Passing to rotation orbits.** Denote the one-step rotation by \(\sigma\). The stabilizer of \(y\) in the cyclic rotation group is \(H=\langle\sigma^p\rangle\), of order \(t=n/p\). Since \(F_n\) commutes with \(\sigma\), two elements of the labeled fiber \(F_n^{-1}(y)\) represent the same input necklace precisely when related by an element of \(H\). Thus \(b_n([y])\) is the number of \(H\)-orbits on this fiber.

For a rotation by \(s\) positions, let \(d=\gcd(n,s)\), setting \(d=n\) at \(s=0\). A fixed input is repetition of a length-\(d\) block, and its image is repetition of the Rule 90 image of that block on the length-\(d\) ring. Its fixed-input contribution is therefore
\[
c(d,y)=\begin{cases}2,&d\text{ odd and the length-}d\text{ block of }y\text{ has even weight},\\4,&d\text{ even and both parity classes of that block have even weight},\\0,&\text{otherwise}.\end{cases}
\]
For each divisor \(j\mid t\), exactly \(\varphi(t/j)\) elements of \(H\) have \(d=pj\). Burnside's lemma gives the exact identity
\[
 b_n([y])=\frac1t\sum_{j\mid t}\varphi(t/j)c(pj,y).
\tag{1}
\]
This identity uses no aperiodicity assumption on the input.

**3. Evaluating the divisors.** If \(n\) is odd, then \(p,t,j\) are odd. Every length-\(pj\) block of \(y=u^t\) has parity equal to that of \(u\); it is even precisely when the entire output has even weight. Every summand in (1) is then \(2\varphi(t/j)\), and \(\sum_{j\mid t}\varphi(t/j)=t\) gives the first case.

Suppose \(n\) is even and \(p\) is even. A length-\(pj\) block consists of \(j\) copies of \(u\), with even-site and odd-site parities \(ja\) and \(jc\). If \(a=c=0\), every summand contributes four, giving \(b_n=4\). Otherwise only even \(j\) contribute, and then the full output is attainable only if \(t\) is even. For even \(t\), the elementary divisor identity
\[
\sum_{\substack{j\mid t\\2\mid j}}\varphi(t/j)=t/2
\]
gives \(b_n=2\). For odd \(t\), the sum is zero.

Finally let \(n\) be even and \(p\) odd; thus \(t\) is even. Write \(e\) for the parity of \(u\). If \(j\) is odd, the length-\(pj\) block has odd length and parity \(e\), giving a contribution of two precisely when \(e=0\). If \(j\) is even, the alternating parity classes each contain \(j/2\) copies of the symbols of \(u\), so both parity sums equal \((j/2)e\). If \(e=0\), the even divisors contribute four and the odd divisors contribute two. The two totient sums equal \(t/2\), hence \(b_n=(4(t/2)+2(t/2))/t=3\). If \(e=1\), only divisors \(j\) divisible by four contribute. There are none when \(4\nmid t\), while when \(4\mid t\),
\[
\sum_{\substack{j\mid t\\4\mid j}}\varphi(t/j)=t/4,
\]
so the degree is one. This proves every case and the bound. Direct inspection of the five stated length-eight representatives proves that every value is attained. \(\square\)

## Verification
Run `python3 verify.py` in the extracted package. The checker independently constructs Rule 90 outputs from indexed cells, canonicalizes input and output words by all cyclic rotations, and compares actual inverse-necklace counts with the theorem for every necklace of every length from \(1\) through \(16\). This comprises \(8{,}923\) output necklaces, with the five length-eight witnesses checked separately. An extracted copy was executed and returned `VERIFY_OK lengths=1..16 necklaces=8923 witnesses=5`. These finite tests do **not** constitute the proof for all lengths; the proof is the stabilizer and parity argument above.

## Relationship to prior work
Wolfram introduced the elementary Rule 90 setting in 1983. Martin, Odlyzko, and Wolfram (1984) derive algebraic state-transition descriptions for additive cellular automata, including Rule 90, at the level of *indexed configurations*. Powley and Stepney (2009) state the two-versus-four predecessor multiplicities of those indexed configurations and analyze full transition-graph automorphisms. Frati, Petak, and Cheney (2024) study the *necklace quotient* across all elementary rules and visualize Rule 90 examples, including their length-six quotient network. The theorem here refines that framework with an all-length, individual-output formula for exact incoming degrees on the necklace quotient. Malcolm Black's adjacent-XOR (binary Ducci) necklace map acts by a one-neighbor difference, whose square agrees with Rule 90 up to a rotation; the existing one-step predecessor and branching descriptions are closely related, but do not explicitly state this primitive-period and parity classification for the square map.

## Limitations
The result concerns one-step inverse branching for Rule 90, not the full dynamic cycle structure, lengths of transient basins, or multi-step inverse counts. No assertion is made about nonbinary alphabets, other elementary rules, or equivalence under reflection/complementation. The full labeled state-transition algebra and the adjacent-XOR necklace framework predate this classification; potential undiscovered prior formulations under Ducci or linear-cellular-automaton terminology remain a historical-priority risk. No independent mathematical audit has been performed.

## References
1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644, first published July 1, 1983. https://doi.org/10.1103/RevModPhys.55.601
2. O. Martin, A. M. Odlyzko, and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. https://doi.org/10.1007/BF01223745
3. E. Powley and S. Stepney, *Automorphisms of Transition Graphs for Linear Cellular Automata*, Journal of Cellular Automata **4** (2009), 293–310. https://www-users.york.ac.uk/~ss44/bib/ss/nonstd/jca09.pdf
4. L. Frati, C. Petak, and N. Cheney, *Networks of Binary Necklaces Induced by Elementary Cellular Automata Rules*, arXiv:2409.04780 (September 7, 2024). https://arxiv.org/abs/2409.04780
5. M. Black, *Binary Necklaces*, section “Adjacent XOR” (web exposition; publication date not established). https://malcolmblack.org/binary-necklaces.html
