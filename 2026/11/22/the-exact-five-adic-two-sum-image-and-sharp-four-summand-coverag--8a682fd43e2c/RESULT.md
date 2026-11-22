# The exact five-adic two-sum image and sharp four-summand coverage of Motzkin-zero indices

## Finding

For each integer \(n\ge0\), the Motzkin number is
\[
M_n=\sum_{j=0}^{\lfloor n/2\rfloor}\binom n{2j}\frac1{j+1}\binom{2j}{j}.
\]
Let \(Z=\{n\ge0:5\mid M_n\}\), and let \(\mathcal Z\) be its closure in the five-adic integers \(\mathbb Z_5\). The theorem determines the complete twofold sumset \(\mathcal Z+\mathcal Z\), its residue projections at *every* depth, and the least positive integer \(h\) for which \(h\mathcal Z=\mathbb Z_5\).

Write \(v_5\) for the five-adic valuation and put
\[
X=\{0\}\cup\{x\in5\mathbb Z_5\setminus\{0\}:\ 
5^{-v_5(x)}x\equiv2\pmod5\ \text{if }v_5(x)\text{ is odd},\
5^{-v_5(x)}x\equiv4\pmod5\ \text{if }v_5(x)\text{ is even}\}.
\]
Define \(P=X+X\) and \(D=X-X\). Then
\[
\boxed{\mathcal Z=(-1+X)\sqcup(-2-X),}
\]
\[
\boxed{P=(10+25\mathbb Z_5)\sqcup(20+25\mathbb Z_5)
\sqcup(75+125\mathbb Z_5)\sqcup(100+125\mathbb Z_5)\sqcup25P,}
\]
\[
\boxed{D=25\mathbb Z_5\sqcup(10+25\mathbb Z_5)
\sqcup(15+25\mathbb Z_5),}
\]
and the **complete two-sum image** is the disjoint union
\[
\boxed{\mathcal Z+\mathcal Z=(-2+P)\sqcup(-3+D)\sqcup(-4-P).}
\]
The three components lie respectively in residue classes \(3,2,1\pmod5\). For every \(k\ge2\), the exact count of attainable residue classes is
\[
\boxed{\#\{a+b\pmod{5^k}:a,b\in Z\}=8\cdot5^{k-2}+1,}
\]
while for \(k=1\) it is \(3\). The exact normalized Haar measure is
\[
\boxed{\mu_5(\mathcal Z+\mathcal Z)=\frac8{25};}
\]
for comparison, \(\mu_5(\mathcal Z)=1/10\).

**Sharp additive order.** Four summands suffice to attain every residue modulo every power of five:
\[
\boxed{4\mathcal Z=\mathbb Z_5,\qquad3\mathcal Z\ne\mathbb Z_5.}
\]
Equivalently, for each integer \(k\ge1\) and each residue \(t\pmod{5^k}\), there exist **nonnegative integer indices** \(n_1,n_2,n_3,n_4\), all satisfying \(5\mid M_{n_i}\), whose sum is \(t\pmod{5^k}\). No three such indices cover all residues even modulo five. This is a congruence-additive statement, not an assertion of exact nonmodular integer representations.

## Assumptions and scope

The prime is exactly five. \(Z\) consists of indices of *values* divisible by five, not the values themselves. In \(hX\) or \(h\mathcal Z\), summands may repeat, and all sums and differences are in the additive group \(\mathbb Z_5\). \(\pi_k\) denotes reduction modulo \(5^k\). Compactness implies \(\pi_k(\mathcal Z)=\pi_k(Z)\), so the projections characterize actual finite congruence representation, not merely a limit phenomenon. For \(v_5(x)=\infty\), only the separately included point \(x=0\) is meant.

The sole non-elementary number-theory input is Deutsch and Sagan's published characterization of indices at which Motzkin numbers vanish modulo five (their Theorem 5.4). All claims about sumsets, measures and additive order below follow from explicit arithmetic of that index set.

## Proof

**1. From the published index criterion to a closed digital set.** Deutsch--Sagan, Theorem 5.4, gives precisely the four index families
\[
\begin{aligned}
n&=(5i+1)5^{2j}-2,&n&=(5i+2)5^{2j-1}-1,\\
n&=(5i+3)5^{2j-1}-2,&n&=(5i+4)5^{2j}-1,
\end{aligned}
\qquad i\ge0,\ j\ge1.
\]
In the second and fourth families \(n+1\) has respectively odd valuation with leading digit two and positive even valuation with leading digit four, so \(n=-1+x\) with \(x\in X\setminus\{0\}\). In the first and third, \(-(n+2)\) has respectively positive even valuation with leading digit four and odd valuation with leading digit two, so \(n=-2-x\) with \(x\in X\setminus\{0\}\). Conversely every finite congruence cylinder of either branch occurs among the listed nonnegative indices by choosing \(i\) in the required congruence class. Taking closure adds the two limit points \(-1\) and \(-2\), and no others; hence \(\mathcal Z=(-1+X)\sqcup(-2-X)\). The branches are disjoint because their elements are \(4\) and \(3\pmod5\).

The first nonzero base-five digits give the exact recursive partition
\[
X=A\sqcup B\sqcup C,\qquad
A=10+25\mathbb Z_5,\quad B=100+125\mathbb Z_5,\quad C=25X.
\tag{1}
\]
Indeed \(A\) contains valuation-one elements with first nonzero digit two, \(B\) contains valuation-two elements with first nonzero digit four, and division by \(25\) maps all remaining nonzero elements bijectively back to the same digit rule. The point zero also lies in \(C\). Every component of (1) is compact.

**2. Exact pairwise sums and differences.** As \(C\subseteq125\mathbb Z_5\), the identities
\[
A+A=20+25\mathbb Z_5,\quad A+(B\cup C)=10+25\mathbb Z_5,
\]
\[
B+B=75+125\mathbb Z_5,\quad B+C=100+125\mathbb Z_5,
\quad C+C=25P
\]
are exact; here a full coset plus any nonempty subset of the corresponding subgroup remains the full coset. These five disjoint sets cover all pairs of components in (1), proving the displayed recursion for \(P\).

For differences, \(A-A=25\mathbb Z_5\), \(A-(B\cup C)=10+25\mathbb Z_5\), and \((B\cup C)-A=15+25\mathbb Z_5\). All other differences are in \(25\mathbb Z_5\). This proves the full three-coset formula for \(D\). Expanding \(\mathcal Z+\mathcal Z\) into pairs of its two branches gives exactly \(-2+P\), \(-3+D\) and \(-4-P\), disjoint modulo five.

**3. Exact images at every finite depth.** Put \(p_k=\#\pi_k(P)\), \(d_k=\#\pi_k(D)\). The recursions give \(p_1=1\), \(p_2=3\), and for \(k\ge3\),
\[
p_k=2\cdot5^{k-2}+2\cdot5^{k-3}+p_{k-2}.
\]
Induction, including both parity classes, yields \(p_k=(5^{k-1}+1)/2\) for every \(k\ge1\). Likewise \(d_1=1\) and \(d_k=3\cdot5^{k-2}\) for \(k\ge2\). Since the three translated pieces of the twofold sum are disjoint modulo five,
\[
\#\pi_k(\mathcal Z+\mathcal Z)=2p_k+d_k
=8\cdot5^{k-2}+1\quad(k\ge2),
\]
and its value at depth one is three. Taking the limit of the fraction of represented classes gives \(\mu_5(\mathcal Z+\mathcal Z)=8/25\). From (1), \(\mu_5(X)=(1/25+1/125)/(1-1/25)=1/20\), hence \(\mu_5(\mathcal Z)=1/10\).

The first two images give useful boundary checks. The support modulo five is \(\{1,2,3\}\); modulo twenty-five it is exactly
\[
\{1,7,8,11,12,18,21,22,23\}.
\]
These are support statements, not fiber-multiplicity statements.

**4. The sharp four-summand covering.** We prove a stronger signed-sum lemma: for every choice of four signs \(\varepsilon_i\in\{+1,-1\}\),
\[
\varepsilon_1X+\varepsilon_2X+\varepsilon_3X+\varepsilon_4X=5\mathbb Z_5. \tag{2}
\]
The inclusion from left to right is immediate. If there are \(r\) plus signs and \(4-r\) minus signs, select \(u\) positive and \(v\) negative slots, place an element of \(A\) in the selected slots and zero in the rest. The integer \(\delta=u-v\) ranges over every integer from \(-(4-r)\) through \(r\): five consecutive residues modulo five. For a given \(t\in5\mathbb Z_5\) with \(v_5(t)=1\), choose \(\delta\ne0\pmod5\) such that \(10\delta\equiv t\pmod{25}\). At least one selected slot is a full coset \(A=10+25\mathbb Z_5\); varying that slot realizes \(t\) exactly while the others remain fixed.

For \(v_5(t)=2\), use the same argument with \(B=100+125\mathbb Z_5\): choose \(\delta\) so that \(100\delta\equiv t\pmod{125}\), and vary one chosen \(B\) term to realize \(t\) exactly. If \(3\le v_5(t)<\infty\), write \(t=25t'\) with \(t'\in5\mathbb Z_5\), use induction on \(v_5(t)\) to represent \(t'\) as the signed four-sum of points of \(X\), then multiply each point by \(25\); the products remain in \(C=25X\subseteq X\). If \(t=0\), choose four zeros. This proves (2), including every sign choice and every valuation boundary.

For a specified \(t\in\mathbb Z_5\), select \(r\in\{0,1,2,3,4\}\) so that \(t\equiv-8+r\pmod5\). Choose \(r\) terms from \(-1+X\) and \(4-r\) from \(-2-X\). Their constant sum is \(-8+r\), and by (2) the adjustable signed-four-\(X\) part is exactly \(5\mathbb Z_5\). Thus every \(t\) belongs to \(4\mathcal Z\). Conversely \(3\mathcal Z\) reduces modulo five to the four classes \(0,1,2,4\), missing \(3\). The least additive covering order is therefore exactly four.

Finally, for every \(k\), membership in \(4\mathcal Z\) gives a congruence representation by four actual indices in \(Z\), because every point of \(\mathcal Z\) is congruent modulo \(5^k\) to at least one index of \(Z\). This establishes the finite prime-power claim without asserting exact integer equality.

## Verification

The accompanying standalone `verify_motzkin_sumsets.py` uses only Python's standard library. It checks the published zero-index rule against 1,601 independently generated integer Motzkin values, directly enumerates all two-sum supports modulo \(5^k\) for \(1\le k\le6\), compares the algebraic recursion and derived support counts, checks fourfold coverage at each tested depth, and exhausts the 125-residue digit-lifting certificate for every sign pattern. Execute `python3 verify_motzkin_sumsets.py`; the expected terminator is `VERIFY_OK checks=2570258`. Bounded checks corroborate the statements but do not prove the infinite theorem; that proof is in the preceding section.

## Relationship to prior work

Deutsch and Sagan (first public arXiv version July 19, 2004) give the exact modulo-five Motzkin **zero-index criterion**, used above as the stated premise. Burns determines the density \(1/10\) of those indices; this is acknowledged as prior work, not claimed new. Later modular-automaton papers classify residues and patterns of **Motzkin values**, including adjacent-pair frequencies. Those statements do not provide the prime-power **additive image of the indices** or prove that four zero indices suffice to attain every prime-power target, while three never do. The new mathematical contribution here is the full twofold sumset, its self-similar exceptional components, exact prime-power cardinalities, and the signed four-summand lifting theorem. A sufficiently general earlier automatic-set addition theorem could implicitly specialize to the present set; historical-priority uncertainty remains, and no assertion of independent external validation is made.

## Limitations

This result is specific to the indices at which ordinary Motzkin numbers vanish modulo five. It does not classify the number of ordered representations of each sum residue, does not establish exact nonmodular integer additive bases, and does not address indices of zeros modulo higher powers of five. The finite checker does not replace the published Motzkin congruence antecedent or the infinite arithmetic proof. The strongest priority uncertainty concerns unindexed consequences of general automatic-set addition results; the searches described in the review are evidence of comparison, not proof of uniqueness.

## References

1. E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326, initial public posting 2004-07-19; *Journal of Number Theory* 117 (2006), 191–215, Theorem 5.4. https://arxiv.org/abs/math/0407326 and https://users.math.msu.edu/users/bsagan/papers/old/ccm.pdf.
2. R. Burns, *Asymptotic density of Motzkin numbers modulo small primes*, arXiv:1611.04910 (2016). https://arxiv.org/abs/1611.04910.
3. R. Burns, *Structure and asymptotics for Motzkin numbers modulo small primes using automata*, arXiv:1612.08146 (2016). https://arxiv.org/abs/1612.08146.
4. N. Kohen, *Uniform recurrence in the Motzkin numbers and related sequences mod p*, arXiv:2403.00149 (2024). https://arxiv.org/abs/2403.00149.
5. OEIS A338220, *Indices of Motzkin numbers divisible by five*. https://oeis.org/A338220.
