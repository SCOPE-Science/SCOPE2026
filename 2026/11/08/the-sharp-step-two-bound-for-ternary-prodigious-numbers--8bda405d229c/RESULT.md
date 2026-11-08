# The sharp step-two bound for ternary prodigious numbers

## Finding

Let \(p_3(n)\) be the product of the nonzero digits in the ordinary base-\(3\) expansion of a positive integer \(n\). Call \(n\) **ternary prodigious** when \(p_3(n)\mid n\).

**Theorem.** For every positive integer \(a\) and every positive integer \(L\), if \(p_3(a+2j)\mid(a+2j)\) for all integers \(0\le j<L\), then \(L\le13\). The bound is attained by
\[
108,110,112,114,116,118,120,122,124,126,128,130,132.
\]
Indeed, infinitely many starts attain the same sharp bound: for every integer \(K\ge5\), the \(13\) integers \(108+4\cdot3^K+2j\), where \(0\le j<13\), are ternary prodigious.

## Assumptions and scope

All terms and starting values are positive integers. The common difference is fixed at \(2\), the radix is exactly \(3\), and zero digits do not enter the digit product. If \(t(n)\) is the number of ternary digits equal to \(2\), then \(p_3(n)=2^{t(n)}\). We use leading zeroes only to name low-digit residue patterns; these do not alter \(p_3\).

## Proof

**Odd starting values.** If \(n\) is odd and ternary prodigious, then \(p_3(n)\), which is a power of \(2\), must equal \(1\). Consequently every ternary digit is \(0\) or \(1\). In particular \(n\pmod9\) belongs to \(\{0,1,3,4\}\). Among these four residues, the only pair of the form \((r,r+2)\pmod9\) is \((1,3)\); the next residue is \(5\), outside the set. Thus no three positive odd terms in a difference-\(2\) progression can all be ternary prodigious.

**Even starting values.** Every positive integer \(n\equiv2\pmod4\) has exactly one factor of \(2\). If at least two of its lowest three ternary digits equal \(2\), then \(4\mid p_3(n)\), so \(n\) is not ternary prodigious. The possible three-digit suffix residues modulo \(27\) with at least two \(2\)'s are precisely
\[
\{8,17,20,23,24,25,26\}.
\]
The Chinese remainder theorem, applied to \(n\equiv2\pmod4\) and each of these seven suffix residues modulo \(27\), gives exactly the following **forbidden even residue classes** modulo \(108\):
\[
F=\{26,50,62,74,78,98,106\}.
\]
Every positive representative of a class in \(F\) fails the prodigious divisibility test.

A difference-\(2\) progression of even integers cycles through all \(54\) even residues modulo \(108\). In the cyclic index \(j\) for the residues \(2j\pmod{108}\), the forbidden positions are
\[
13,25,31,37,39,49,53\pmod{54}.
\]
The successive cyclic differences between these positions are
\[
12,6,6,2,10,4,14.
\]
Hence no gap contains more than \(13\) consecutive nonforbidden even residues. Every block of \(14\) consecutive even terms with difference \(2\) therefore meets a forbidden class, whatever its starting residue. Such a block cannot consist entirely of ternary prodigious numbers. Combined with the odd case, this proves the universal upper bound \(L\le13\).

**Sharpness and infinitely many attaining progressions.** The nonzero ternary digit products of \(108+2j\) for \(j=0,1,\ldots,12\) are, respectively,
\[
1,2,1,2,4,1,1,2,2,2,4,2,4.
\]
Each divides its corresponding integer, proving that the displayed thirteen-term progression is valid. Every term is less than \(3^5=243\), and all thirteen products divide \(4\). For any integer \(K\ge5\), adding \(4\cdot3^K\) prepends the ternary digits \(11\) at positions \(K+1,K\) without carrying, leaving the nonzero digit product unchanged. The increment is divisible by \(4\), so every original divisibility remains valid. Distinct \(K\) give distinct starts, proving infinitely many sharp examples.

## Verification

The self-contained script `check_prodigious.py` recomputes the seven forbidden classes, checks all \(54\) even starting residues modulo \(108\) for the \(14\)-term obstruction, checks all \(9\) odd starting residues modulo \(9\), computes the thirteen witness products, and tests \(46\) members of the infinite witness family. It also performs a separate bounded scan through \(200000\). Exact output is recorded in `check_output.json`. The proof of the infinite upper bound uses only the fully specified residue cycle and does not rely on the bounded scan or the finite tests of large starts.

## Relationship to prior work

Gohn, Harrington, Lebiere, Samamah, Shappell, and Wong (2022) study base-\(b\) prodigious arithmetic progressions. Their Theorem 3 treats differences \(d\mid b\) with \(d<b/2\); their Theorem 5 treats even bases and difference \(b/2\). Neither includes base \(b=3\) and difference \(d=2\). Their consecutive-integer result gives maximum length \(5\) for base \(3\) and difference \(1\), so the sharp difference-\(2\) length \(13\) is an arithmetic contrast not implied by their formulas. Sanna (2018) studies the global counting function of integers divisible by nonzero digit products, rather than uniform lengths of fixed-step progressions. OEIS A055471 concerns the *decimal* digit product and does not tabulate this ternary progression maximum. No equivalent claim was identified in the inspected literature or targeted statement searches; this is not an assertion of exhaustive novelty.

## Limitations

This result concerns base \(3\), positive terms, step \(2\), and the **product of nonzero digits**, not the digit sum or the product including zeroes. It does not classify all attaining starting values and makes no general statement about other bases or differences. The proof and checks have not undergone independent scientific audit; equivalent unindexed prior work may exist.

## References

1. M. Gohn, J. Harrington, S. Lebiere, H. Samamah, K. Shappell, and T. W. H. Wong, *Arithmetic Progressions of b-Prodigious Numbers*, Journal of Integer Sequences **25** (2022), Article 22.8.7, published 25 October 2022. https://cs.uwaterloo.ca/journals/JIS/VOL25/Wong/wong42.pdf
2. C. Sanna, *On numbers divisible by the product of their nonzero base b digits*, arXiv:1809.05463 (14 September 2018). https://arxiv.org/abs/1809.05463
3. OEIS A055471, *Divisible by the product of its nonzero digits* (decimal case). https://oeis.org/A055471
