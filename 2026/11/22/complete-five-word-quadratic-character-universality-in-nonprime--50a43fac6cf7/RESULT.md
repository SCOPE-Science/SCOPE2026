# Complete five-word quadratic-character universality in nonprime finite fields

## Finding
Let \(q=p^e\), where \(p\ge5\) is prime and \(e\ge2\). Let \(\chi_q\) be the quadratic character of \(\mathbb F_q\), with \(\chi_q(0)=0\). For \(\boldsymbol\varepsilon\in\{-1,1\}^5\), define the number of realizations
\[
N_q(\boldsymbol\varepsilon)=\#\{x\in\mathbb F_q:\chi_q(x+j)=\varepsilon_j\ \text{for every }0\le j\le4\}.
\]
Then **every one of the thirty-two words occurs** if and only if
\[
q\notin\{25,49,121,125,169\}.
\]
Equivalently, every such nonprime field of order at least \(289\) realizes every word, and this uniform threshold is sharp because the preceding eligible field order \(169\) lacks one word. The first successful eligible field has order \(289\).

The classification also determines the missing words at every exceptional field. Encode a word by its five-bit integer \(b=\sum_{j=0}^4 2^j\mathbf1_{\{\varepsilon_j=1\}}\); the low bit corresponds to \(j=0\). The complete sets of absent codes are:

| \(q\) | Absent five-bit codes |
|---:|---|
| \(25\) | \(0,1,2,4,7,8,11,13,14,15,16,19,21,22,23,25,26,27,28,29,30,31\) |
| \(49\) | \(0,2,8,11,13,15,17,22,23,26,27,29,30\) |
| \(121\) | \(0,27\) |
| \(125\) | \(0,5,7,9,10,14,18,19,20,25,28,31\) |
| \(169\) | \(4\) |

There are no missing words in any other nonprime field of characteristic at least five.

## Assumptions and scope
The five consecutive field elements are \(x,x+1,x+2,x+3,x+4\), where the integers act through the prime subfield. The characteristic is at least five, so the five shifts are distinct. Zero entries are disallowed by the definition of a word. The case of a prime field \(e=1\), and characteristics two and three, are not covered. The result is a complete existence and nonexistence classification, not an exact formula for all positive multiplicities \(N_q(\boldsymbol\varepsilon)\).

## Proof
**1. Uniform bound for large fields.** Fix a word \(\boldsymbol\varepsilon\). Put \(E=\{0,-1,-2,-3,-4\}\) in \(\mathbb F_q\). For \(x\notin E\), the indicator of the desired word equals
\[
\frac1{32}\prod_{j=0}^{4}(1+\varepsilon_j\chi_q(x+j)).
\]
At each of the five excluded points exactly one character is zero, and each of the other four factors belongs to \(\{0,2\}\). Thus the entire excluded-point correction to the unnormalized sum lies between zero and \(80\).

Expand the product over all \(x\in\mathbb F_q\). The empty subset contributes \(q\), and the five singleton sums vanish. Each of the ten distinct quadratic character sums of the form
\[
\sum_{x\in\mathbb F_q}\chi_q((x+i)(x+j)),\qquad i\ne j,
\]
is \(-1\). Since its coefficient is \(\pm1\), the total pair contribution is at least \(-10\). For a subset of \(d\ge3\) shifts, the product polynomial is squarefree of degree \(d\) and is not a square. The classical Weil bound yields
\[
\left|\sum_{x\in\mathbb F_q}\chi_q\!\left(\prod_{j\in J}(x+j)\right)\right|\le(d-1)\sqrt q.
\]
Summing the absolute values for subsets of sizes three, four and five gives
\[
\binom53\cdot2+\binom54\cdot3+\binom55\cdot4=39.
\]
Consequently, uniformly in the sign word,
\[
32N_q(\boldsymbol\varepsilon)\ge q-39\sqrt q-90.
\]
The right side is strictly positive for every \(q\ge1697\): it is increasing for \(\sqrt q\ge\sqrt{1697}\), and at the endpoint its positivity follows by squaring the positive inequality \(1607>39\sqrt{1697}\), since \(1607^2-39^2\cdot1697=1312>0\). Thus every word occurs in each eligible field of order at least \(1697\).

**2. Exhaustive classification of the remaining fields.** Every nonprime prime power \(q=p^e<1697\) with \(p\ge5\), \(e\ge2\), belongs to the fifteen-element list
\[
25,49,121,125,169,289,343,361,529,625,841,961,1331,1369,1681.
\]
The attached self-contained `verify.py` performs complete exact arithmetic in each corresponding finite field, and its output certifies the table above and positivity of all thirty-two pattern counts at the ten remaining orders. The code enumerates the entire field and its nonzero squares, rejects every start touching zero, and accumulates the thirty-two counts. It does not sample starts or use probabilistic primality tests. Each finite field is presented using an irreducible polynomial, and membership in the computed square set is independently checked against Euler's criterion throughout the field. For quadratic extensions a second verification uses the norm to the prime subfield.

For degree two the polynomial is \(T^2-c\), with \(c\) a least positive quadratic nonresidue modulo \(p\), and hence irreducible. For degree three it is \(T^3+AT+B\), where the program chooses the first monic trinomial with no root in \(\mathbb F_p\); absence of a root is exactly irreducibility for a cubic. The only degree-four case in the finite range is \(q=625\), represented by \(T^4+2\) over \(\mathbb F_5\). This is irreducible: a reducible quartic has a root in \(\mathbb F_{25}\); such a root would be a fourth root of \(3\). But \(3\) has multiplicative order four in \(\mathbb F_{25}^{\times}\), while any fourth power in that group of order twenty-four has order dividing six.

Therefore the finite enumeration is exhaustive and takes place in the stated finite fields. Combining it with the analytic bound proves the complete classification and its sharp threshold.

## Verification
Run `python3 verify.py` with a standard Python 3 installation. The program lists all fifteen field sizes below the analytic cutoff, prints the absent pattern codes, and terminates with `PASS` after checking them against the exact table. It independently confirms for every nonzero element that its computed square-set membership equals Euler's criterion; in every quadratic extension it also checks the quadratic character of the field norm. The finite loop counts \(q-5\) valid starting points at every size. The uniform large-field conclusion is the analytic argument above, not an extrapolation from enumeration.

## Relationship to prior work
Cohen's 2024 study of consecutive squares and nonsquares over general finite fields evaluates homogeneous triples and special quadruples in characteristic five. Wang and Fang's 2023 work considers counts of all-square or all-nonsquare progressions over prime fields, including length five. Buchaev and Tsfasman's 2026 preprint gives formulas for arbitrary length-four and length-five words over **prime** fields. None of these stated results supplies the complete exceptional-field list for all mixed five-letter patterns in **nonprime** fields. A published six-letter universality result for prime fields concerns a different domain; its prime-only cutoff does not resolve extension fields. Standard character expansions and the Weil inequality are acknowledged as prior tools, not claimed as discoveries.

## Limitations
The result is a sharp existence classification and finite exceptional-word census, not a formula for every positive multiplicity or a new general bound for arbitrary word lengths. Its finite component relies on the provided exhaustive arithmetic program; independent replication is advisable. General curve-trace formulas in the more recent length-five literature may make some instances indirectly computable, and an unindexed explicit extension-field census would affect priority. No independent mathematical audit has been carried out.

## References
1. Stephen D. Cohen, *Triples and quadruples of consecutive squares or non-squares in a finite field*, arXiv:2402.10737, first submitted 2024-02-16, https://arxiv.org/abs/2402.10737.
2. Xiao Wang and Hao Fang, *The Distribution Properties of Consecutive Quadratic Residue Sequences*, Journal of Mathematics (2023), article 5253261, https://doi.org/10.1155/2023/5253261.
3. Abdulkadyr Buchaev and Michael Tsfasman, *Quadratic residue patterns of length 4 and 5*, arXiv:2607.17418, first submitted 2026-07-19, https://arxiv.org/abs/2607.17418 (abstract accessible; full text not inspected).
4. *Sharp six-block quadratic-character universality from prime 461*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-six-block-quadratic-character-universality-from-prime-461--a2fa4afbd655 (scientific statement and proof read).
5. Classical Weil bound for nontrivial quadratic character sums of squarefree polynomials over finite fields; see the background and cited references in [1] and [2].
