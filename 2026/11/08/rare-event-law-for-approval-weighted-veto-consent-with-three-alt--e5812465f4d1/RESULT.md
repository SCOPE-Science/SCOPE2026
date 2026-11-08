# Rare-event law for approval-weighted veto consent with three alternatives

## Finding

For the Approval-Weighted Veto Core (AWVC) on three alternatives, suppose each of \(n\ge1\) voters independently draws one of the six strict rankings uniformly and approves exactly her top-ranked alternative. Let \(E_n\) be the event that AWVC is nonempty. Under these explicit approval and preference assumptions:

1. The resulting consent set has at most one member on every profile. Its nonemptiness probability is given by the exact finite multinomial formula below.
2. The probability is exponentially small, with an exact logarithmic rate:
   \[
   \lim_{n\to\infty}\frac1n\log\Pr(E_n)=-\frac16\log\frac{27}{16}.
   \]
3. On the subsequence \(6\mid n\), the exact leading prefactor is
   \[
   \Pr(E_n)\sim\frac{36\sqrt3}{(2\pi n)^{3/2}}\,\frac{14904}{121}\left(\frac{16}{27}\right)^{n/6}.
   \]

The same at-most-one conclusion holds with any finite number of alternatives at least two, provided each voter approves only her strict top choice. The probability and asymptotic formulas concern precisely three alternatives.

## Assumptions and scope

The candidate set is \(C=\{c,d,e\}\); each of the \(n\) rankings is independent and uniformly sampled from the six permutations. The sole approved alternative of a voter is her top-ranked one. This is consistent with the original cardinal-utility/threshold framework: assign utility \(2\), \(1\), \(0\) to a voter's first, second, third alternatives and set her approval threshold to \(3/2\).

For a nonempty set \(S\) of voters, write \(B_S(c)=\{x\in C:x\succ_i c\ \text{for all }i\in S\}\). Under AWVC a candidate with \(a>0\) approvers is blocked if a nonempty coalition consisting entirely of disapprovers has
\[
\frac{|S|}{a}>1-\frac{|B_S(c)|}{3}.
\]
A candidate with zero approvers is blocked by convention. All these inequalities are strict for blocking. \(\Pr(E_n)\) is over rankings alone, without a random choice of mechanisms or a random downstream selected outcome.

For a fixed candidate \(c\), define \(a\) as its number of first-place voters, \(b\) as its number of last-place voters, \(r\) as the number ranking \(d\succ c\succ e\), and \(s\) as the number ranking \(e\succ c\succ d\). Thus \(a+b+r+s=n\); the last-place voters may prefer \(d\) or \(e\) first. In this four-type categorization the probabilities are \((1/3,1/3,1/6,1/6)\).

Then \(c\) survives precisely when
\[
 a>0,\qquad 2a\ge n,\qquad 3b\le a,\qquad 3(b+r)\le2a,\qquad3(b+s)\le2a.
\]
Consequently its exact nonemptiness probability is
\[
\Pr(E_n)=\frac{3}{6^n}
\sum_{\substack{a,b,r,s\in\mathbb Z_{\ge0}\\a+b+r+s=n\\a>0,\ 2a\ge n\\3b\le a,\ 3(b+r)\le2a,\ 3(b+s)\le2a}}
\frac{n!\,2^{a+b}}{a!\,b!\,r!\,s!}.
\]
This sum is valid for all positive integers \(n\), including parity boundaries. For example, at \(n=6\) it gives \(103/243\), and at \(n=12\) it gives \(24023/157464\).

## Proof

**Coalition reduction.** The disapprovers of \(c\) fall into the last-place group of size \(b\) (all prefer both other alternatives), the group of size \(r\) (only \(d\) above \(c\)), and the group of size \(s\) (only \(e\) above \(c\)). A coalition with no unanimously preferred alternative can block only if its size exceeds \(a\), so no such block exists exactly when \(n-a\le a\). A coalition unanimously preferring both alternatives can block exactly when \(b>a/3\). A coalition unanimously preferring \(d\), respectively \(e\), can block if \(b+r>2a/3\), respectively \(b+s>2a/3\). The same implications hold when an ostensible one-alternative coalition also prefers both alternatives: that only makes blocking easier, and the last-place test already detects it. These four tests exhaust the possible intersections \(B_S(c)\), yielding the displayed necessary and sufficient inequalities.

**Uniqueness.** The full disapprover coalition blocks any candidate with fewer than half of the first-place votes: its size is greater than the candidate's number of approvers, and the right-hand side of the AWVC inequality is at most one. If two different candidates each have at least half, their counts must both be \(n/2\) and all voters rank one of those two first. For either candidate, all its disapprovers rank the other candidate above it. The full disapprover coalition then has relative size one and at least one unanimously preferred alternative, hence strictly blocks it. Thus two candidates cannot simultaneously survive, regardless of the number of alternatives. By symmetry, \(\Pr(E_n)=3\Pr(c\text{ survives})\). Applying the multinomial distribution gives the finite formula.

**Exponential rate.** Under the uniform independent culture, the numbers \((a,b,n-a-b)\) of first, last and middle placements of a fixed candidate are multinomial with equal category probabilities. Put \(L=(3/2)^a(1/2)^b\). Directly, \(\mathbb E L=[((3/2)+(1/2)+1)/3]^n=1\). On survival, \(a\ge n/2\) and \(b\le a/3\), so
\[
 L\ge \exp\left\{\frac n2\left(\log\frac32-\frac13\log2\right)\right\}=
 \left(\frac{27}{16}\right)^{n/6}.
\]
Markov's inequality gives \(\Pr(E_n)\le3(16/27)^{n/6}\). For \(n=6m\), consider the nonempty type with \((a,b,r,s)=(3m,m,m,m)\); it obeys every survival inequality. Its probability is \(\exp[-n\log(27/16)/6+O(\log n)]\) by Stirling's formula. For a general \(n=6m+t\), \(0\le t<6\), add \(t\) top-\(c\) rankings to that type, keeping all disapprover counts unchanged. It still obeys the inequalities and has the same exponential rate. This proves the claimed full-sequence logarithmic limit.

**Exact prefactor.** Fix \(n=6m\) and introduce a tilted four-type distribution \(Q=(1/2,1/6,1/6,1/6)\). Write \(k_0=(3m,m,m,m)\), a mode of the associated multinomial distribution. Under the original four-type law \(P=(1/3,1/3,1/6,1/6)\), the probability of any count vector \((a,b,r,s)\) equals its \(Q\)-probability multiplied by \((2/3)^a2^b\). Parameterize all surviving count vectors by integers \(h\ge0\), \(j\ge-\lfloor h/3\rfloor\) and \(\ell=r-s\), with
\[
 a=3m+h,\quad b=m-j,\quad r+s=2m-h+j,\quad
 \ell\equiv j-h\pmod2,\quad
 |\ell|\le 2h+j+\lfloor h/3\rfloor.
\]
As usual, only vectors with nonnegative counts are included for finite \(m\). Relative to the original probability of the base type, each vector has the multiplier
\[
 \left(\frac23\right)^h2^{-j}\frac{Q(a,b,r,s)}{Q(k_0)}.
\]
For every fixed admissible triple \((h,j,\ell)\), the final ratio tends to one. It is at most one for every \(m\), because \(k_0\) is a global multinomial mode: whenever a count exceeds its mode coordinate and another falls below, transferring one count toward the mode strictly increases probability. The sum of the dominating multipliers over all admissible triples is finite, so dominated convergence applies.

For fixed \(h,j\), the number of allowed values of \(\ell\) is \(2h+j+\lfloor h/3\rfloor+\varepsilon_h\), where \(\varepsilon_h=1\) if \(h+\lfloor h/3\rfloor\) is even and zero otherwise. Writing \(h=3q+t\) with \(t\in\{0,1,2\}\) and summing the geometric series over \(j\) and \(q\) gives
\[
 \sum_{h\ge0}\sum_{j\ge-\lfloor h/3\rfloor}
 \left(\frac23\right)^h2^{-j}
 \left(2h+j+\lfloor h/3\rfloor+\varepsilon_h\right)
 =\frac43\left(\frac{19z}{(1-z)^2}+\frac{10}{1-z}\right)
 =\frac{14904}{121},\qquad z=\frac{16}{27}.
\]
Finally, Stirling's formula for the tilted base mode gives \(Q(k_0)\sim 12\sqrt3/(2\pi n)^{3/2}\), and its original probability is \(Q(k_0)(16/27)^{n/6}\). Multiplying by the convergent factor \(14904/121\) and then by three disjoint candidate choices proves the prefactor formula.

## Verification

Run `python3 check.py` in the same directory. The checker compares the literal strict coalition-blocking definition against the four-count characterization on all 5,004 anonymous six-ranking histograms with \(1\le n\le9\); it checks that at most one candidate survives. It also recomputes the finite formula, the \(n=12\) exact probability, and the rational prefactor sum. These finite computations are checks of the stated formulas, not substitutes for their proofs. The proof of the large-\(n\) rate and prefactor is the analytic argument above.

## Relationship to prior work

Dong, Kraiczy, Vasishta, Brill, Holliday and Boehmer (arXiv:2609.10759v1, first posted September 9, 2026) define AWVC through candidate-specific approval-weighted blocking and establish its general support and veto guarantees; their experimental study includes synthetic preference profiles. The present theorem studies its different, distributional question: exact and asymptotic *nonemptiness* under three-alternative impartial culture and top-choice approval, with the explicit polynomial prefactor. The older proportional-veto-core work of Ianovski and Kondratev (arXiv:2003.09153) concerns a different rule without the same joint approval-and-ranking input. Standard multinomial large-deviation and local-mass methods are used as proof tools, not asserted as new mathematics.

## Limitations

The probability formula is only for uniformly independent rankings, three alternatives, and single top-choice approvals; it is not a statement about general joint approval distributions, larger candidate sets, or the composition with the disapproval Smith set. The leading constant is asserted only along \(6\mid n\); for other residue classes the logarithmic rate remains valid, but no common leading prefactor is claimed. The analysis does not address strategic reporting. Related indexed literature and selected relevant portions of the primary paper were inspected, but complete coverage of every unpublished or unindexed source is not claimed. This result has not received an independent scientific audit.

## References

- C. Dong, S. Kraiczy, R. Vasishta, M. Brill, W. H. Holliday, N. Boehmer, *Where Should Society Draw the Line? A Social Choice Approach to Collective Consent*, arXiv:2609.10759v1 (September 9, 2026). https://arxiv.org/abs/2609.10759
- E. Ianovski and A. Y. Kondratev, *Computing the Proportional Veto Core*, arXiv:2003.09153 (March 20, 2020), AAAI 2021. https://arxiv.org/abs/2003.09153
