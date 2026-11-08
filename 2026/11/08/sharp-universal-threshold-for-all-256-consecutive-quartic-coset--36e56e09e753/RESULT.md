# Sharp universal threshold for all 256 consecutive quartic-coset quadruples

## Finding

For each prime \(p\equiv1\pmod4\), choose a primitive root \(g\) modulo \(p\). For \(y\not\equiv0\pmod p\), write \(c_p(y)\in\{0,1,2,3\}\) for the unique residue class of the discrete logarithm of \(y\) to base \(g\) modulo four; thus \(c_p(g^a)=a\bmod4\). Let
\[
\mathcal W_4(p)=\{(c_p(n),c_p(n+1),c_p(n+2),c_p(n+3)):1\le n\le p-4\}.
\]
Then
\[
\boxed{\mathcal W_4(p)=\{0,1,2,3\}^4\quad\text{for every prime }p\equiv1\pmod4,\ p\ge3373.}
\]
The threshold is sharp: the preceding eligible prime \(p=3361\) realizes exactly \(255\) words. Using the least positive primitive root \(g=22\) modulo \(3361\), the sole missing word is \((3,0,0,3)\); with an alternative primitive root it may be relabeled as \((1,0,0,1)\). In contrast, \((0,0,0,0)\) already occurs at \(p=3361\). The final prime without four consecutive quartic residues is \(p=2689\). In the complete finite range there are exactly \(144\) primes missing at least one word.

For every \(\boldsymbol a\in\{0,1,2,3\}^4\), its occurrence count \(N_p(\boldsymbol a)\) obeys the explicit uniform bound
\[
\boxed{256N_p(\boldsymbol a)\ge p-513\sqrt p-256.}
\]
Here \(n\) ranges over ordinary representatives \(1,\ldots,p-4\); the four entries are all nonzero and consecutive without wrapping through zero.

## Assumptions and scope

The prime \(p\) must satisfy \(p\equiv1\pmod4\), so the multiplicative group has exactly four quartic-power cosets. A primitive root choice permutes the nonzero coset labels by multiplication by either \(1\) or \(3\) modulo four. Consequently the property of realizing **all** \(256\) words and the number of missing words are independent of this choice, while the name of a particular nonzero missing word may change. No statement is made about least starting positions or primes in other congruence classes.

## Proof

Fix a multiplicative character \(\chi\) of exact order four with \(\chi(g)=i\). Let \(U=\mathbb F_p\setminus\{0,-1,-2,-3\}\). For any prescribed word \(\boldsymbol a=(a_0,a_1,a_2,a_3)\), the quartic-character orthogonality identity gives
\[
256N_p(\boldsymbol a)=\sum_{\boldsymbol e\in\{0,1,2,3\}^4}i^{-\boldsymbol a\cdot\boldsymbol e}\sum_{n\in U}\chi\!\left(\prod_{j=0}^3(n+j)^{e_j}\right).
\]
The zero exponent vector contributes \(p-4\). For a nonzero exponent vector with support \(r\) (the number of nonzero coordinates), the polynomial has exactly \(r\) distinct roots and is not a fourth power. The standard multiplicative-character Weil bound applied to the complete field sum gives magnitude at most \((r-1)\sqrt p\) for \(r\ge2\). For \(r=1\) the complete sum vanishes exactly by translating a nontrivial character. Removing the four excluded field elements changes the sum by at most \(4-r\), because at the other \(r\) excluded roots the character already vanishes.

There are \(\binom4r3^r\) nonzero exponent vectors of support \(r\). Triangle inequality therefore yields
\[
\begin{aligned}
256N_p(\boldsymbol a)&\ge(p-4)-12\cdot3-54(\sqrt p+2)\\
&\qquad{}-108(2\sqrt p+1)-81(3\sqrt p)\\
&=p-513\sqrt p-256.
\end{aligned}
\]
At \(p=263681\), the exact integer comparison \((p-256)^2-513^2p=65536>0\) holds and \(p-256>0\). This difference is increasing for all larger \(p\), so every word occurs for every prime \(p\ge263681\) in the required congruence class.

For the remaining finite interval \(5\le p<263681\), the complete deterministic C++17 verifier `verify_quartic4.cpp` enumerates every prime \(p\equiv1\pmod4\) by an Eratosthenes sieve, constructs a primitive root using the distinct prime factors of \(p-1\), labels the \(p-1\) nonzero residues, and forms the exact 256-bit word-coverage bitmap by scanning \(1\le n\le p-4\). It evaluates all \(11{,}538\) eligible primes and finds exactly \(144\) with incomplete coverage. The largest such prime is \(3361\), and the next eligible prime \(3373\) has full coverage. The associated output `quartic4_output.txt` lists every exceptional prime, so this finite cutoff is fully replayable rather than an extrapolation from a sampled range.

Independently, `check_quartic4_independent.py` constructs each coset from the set of nonzero fourth powers and the least quadratic nonresidue, without using primitive roots or discrete logarithms. It checks all \(269\) eligible primes up to \(4000\), reproducing all \(144\) exceptions and the unique final missing word. This independent check is corroborative; the exhaustive finite verification for the entire required interval is supplied by the C++17 program. Combining the finite verification with the symbolic bound proves the statement for every eligible prime.

## Verification

Compile and execute with a standard C++17 compiler:

```sh
g++ -std=c++17 -O3 verify_quartic4.cpp -o verify_quartic4
./verify_quartic4
python3 check_quartic4_independent.py
```

Expected first output line:

```text
eligible_primes=11538 bad_primes=144 last_bad=3361 first_good_after_last=3373 last_zero_bad=2689 max_missing=255
```

The complete output, including the exceptional-prime list, is embedded in `quartic4_output.txt`. The verifier uses exact integers and independent deterministic primality testing. The separate Python implementation also confirms that the missing word at \(3361\) is not the all-zero word. Neither code requires an external table or third-party package.

## Relationship to prior work

The classical work of Graham (1964) concerns the unbounded first starting position of four **equal** power-residue labels across varying primes, not the existence of all mixed four-label words at each sufficiently large prime. Rabung and Jordan (1970) calculate least starting-position bounds for monochromatic runs in a single coset, rather than simultaneous coverage of all 256 ordered patterns. Su and Zhang (2020) establish formulas for special configurations involving \(a+a^{-1}\) and \(a-a^{-1}\) and do not determine adjacent four-term coset-word coverage. An earlier exact classification of **three** consecutive quartic-coset labels establishes a smaller word spectrum but does not imply the four-term threshold or explain the mixed last obstruction at \(3361\).

Emma Lehmer's *Patterns of power residues* (1983) is a potentially relevant broader source: the available review discusses smallest occurrences of all-residue patterns for prescribed shift sets, not the 256-word simultaneous prime threshold. The full paper was not accessible for a complete implication comparison. This is a genuine residual literature risk, not a claim of unique priority.

## Limitations

The result gives a sharp eventual threshold, a complete finite exceptional-prime list, and a universal count bound; it does not give closed formulas for individual word counts, least witnesses, or analogous classifications for longer words. The sharp part relies on a finite exhaustive calculation through \(263680\) which has been independently cross-checked over a substantial initial range but has not received external certification or independent scientific audit. The Weil bound is classical; the new claim is the exact four-word classification and the mixed terminal obstruction. Priority beyond inspected sources is not asserted.

## References

1. J. Su and J. Zhang, *On the Quartic Residues and Their New Distribution Properties*, Mathematics 8 (2020), article 1337, first published 2020-08-11. https://doi.org/10.3390/math8081337
2. R. L. Graham, *On Quadruples of Consecutive kth Power Residues*, Proc. Amer. Math. Soc. 15 (1964), 196–197. https://doi.org/10.2307/2034033
3. J. R. Rabung and J. H. Jordan, *Consecutive Power Residues or Nonresidues*, Math. Comp. 24 (1970), 737–740. https://doi.org/10.2307/2004850
4. E. T. Lehmer, *Patterns of power residues*, J. Number Theory 17 (1983), 37–46. https://doi.org/10.1016/0022-314X(83)90004-5
5. N. A. Carella, *Consecutive Quadratic Residues And Quadratic Nonresidue Modulo p*, arXiv:2011.11054v1 (2020-11-17), a quadratic-character comparison rather than the present quartic theorem.
