# Complete maximizers of exact-two adjacent-swap spheres over nonbinary alphabets

## Finding

Let \(\Sigma\) be an alphabet of size \(q\ge2\), and let \(w=w_1\cdots w_n\in\Sigma^n\), \(n\ge2\). For \(1\le i<n\), write \(\tau_i\) for exchange of positions \(i,i+1\), including the identity operation if their symbols agree. The **exact-two-operation sphere** is
\[
T_2(w)=\{\tau_j\tau_i(w):1\le i,j<n\}.
\]
Put \(b_i=\mathbf1_{\{w_i\ne w_{i+1}\}}\), \(r=\sum_{i=1}^{n-1}b_i\), and
\[
\begin{aligned}
 a&=\sum_{i=1}^{n-2}b_ib_{i+1},\\
 h&=\sum_{i=1}^{n-2}\mathbf1_{\{b_i\ne b_{i+1}\}},\\
 p&=\sum_{i=1}^{n-2}\mathbf1_{\{w_i=w_{i+2}\ne w_{i+1}\}}.
\end{aligned}
\]
Define \(s=r\) if some \(b_i=0\); otherwise let \(s\) be the cardinality of the union of the pairs \(\{i,i+1\}\) for all indices \(i\) counted in \(p\). Empty sums and unions are zero. A support-partition lemma, valid for **every** \(q\ge2\) and \(n\ge2\), gives
\[
\boxed{|T_2(w)|=1+\binom r2+a+h-2p+s.}\tag{1}
\]

For every \(q\ge3\) and \(n\ge2\),
\[
\boxed{\max_{w\in\Sigma^n}|T_2(w)|=\binom n2.}\tag{2}
\]
For \(n\ge3\), the complete list of equality cases is: (A) all adjacent letters differ, and no factor is of the form \(abab\) with \(a\ne b\); or (B) precisely one adjacent pair is equal, and no factor is of the form \(aba\) with \(a\ne b\). These two classes are disjoint. At \(n=2\), every word is optimal, with the same two-class description.

Let \(A_n(q)\) and \(B_n(q)\) denote the labeled numbers of words of types (A) and (B). They are determined for \(q\ge3\) by
\[
\begin{gathered}
A_2(q)=q(q-1),\quad A_3(q)=q(q-1)^2,\quad A_4(q)=q^2(q-1)(q-2),\\
A_n(q)=(q-2)\bigl(A_{n-1}(q)+A_{n-2}(q)\bigr)\quad(n\ge5),\\
B_n(q)=q\sum_{j=1}^{n-1}f_j(q)f_{n-j}(q),\qquad
f_1(q)=1,\quad f_k(q)=(q-1)(q-2)^{k-2}\quad(k\ge2).
\end{gathered}\tag{3}
\]
Thus the **exact number of maximizers** is \(A_n(q)+B_n(q)\). In particular, for \(q=3\) and \(n\ge3\), this is \(6F_n+12(n-2)\), with \(F_1=F_2=1\) the ordinary Fibonacci numbers.

## Assumptions and scope

An operation may swap equal letters and leave the word unchanged; it still uses one operation. The two swaps are sequential, may overlap, and may use the same position. Equation (1) describes the sphere after **exactly two operations** and is not a claim about a disjoint-swap channel or about swaps restricted to nontrivial exchanges. The alphabet has distinct labeled letters. No restrictions on source word composition are imposed.

## Proof

**1. Exhaustive structural partition of two-swap outputs.** Fix \(w\). Every ordered pair of swap indices belongs to one of the following classes; outputs are classified by their changed positions relative to \(w\), so the stated classes are disjoint.

* Identical swap indices return \(w\), contributing one output. Swapping at an equal-letter edge also may leave \(w\) unchanged.
* Two distinct, nonoverlapping **active** original edges \(i,j\) with \(|i-j|\ge2\) change the four positions \(i,i+1,j,j+1\). This support uniquely specifies the two edges, so there are exactly \(\binom r2-a\) outputs.
* Two overlapping indices \(i,i+1\) act on one triple. If all three letters are distinct, the two orders give two different cyclic permutations, each changing all three coordinates. Such triples number \(a-p\), hence contribute \(2(a-p)\) outputs. If the triple has exactly two distinct letters in adjacent equal positions (types \(aab\) or \(abb\)), one order gives a word differing only at its nonadjacent endpoints; this is a new, uniquely supported output. These triples number \(h\). If it is \(aba\), neither order contributes a new three-position or endpoint-only output: both are single-effective-swap outputs. Constant triples contribute none.
* A word differing by exactly one **effective adjacent swap** at edge \(i\) occurs in two operations precisely as follows. If the original word has any inactive edge, perform that swap first and then swap edge \(i\); hence all \(r\) active edges contribute. If every original edge is active, an effective swap can be followed or preceded by a trivial swap only when it creates a repeated adjacent pair; this occurs precisely when edge \(i\) meets a factor \(aba\), so the number is the defined union size \(s\). Each distinct active edge produces a distinct one-swap output.

The singleton, disjoint-two-swap, three-position, endpoint-only, and one-swap classes therefore total
\[
1+(\binom r2-a)+2(a-p)+h+s,
\]
which is (1). In particular no cancellation of distinct output words is assumed without a support argument.

**2. General-alphabet extremizers.** Write \(m=n-1\). If every edge is active, then \(r=m\), \(a=m-1\), \(h=0\), and \(s\le2p\). Equation (1) gives
\[
|T_2(w)|=\binom{m+1}{2}-2p+s\le\binom n2.
\]
The union of \(p\) successive edge-pairs has size \(2p\) exactly when no two such pairs overlap. Two factors \(aba\) starting at consecutive positions overlap precisely when their four-letter union is \(abab\). Thus equality holds exactly in case (A).

If at least one edge is inactive, let \(c_{00}\) count adjacent pairs of inactive edges. Since \(a+h+c_{00}=m-1\), equation (1) simplifies to
\[
|T_2(w)|=m+\binom{r+1}{2}-c_{00}-2p.
\]
Consequently
\[
\binom n2-|T_2(w)|=\frac{m(m-1)-r(r+1)}2+c_{00}+2p.
\]
If there is precisely one inactive edge, \(r=m-1\) and \(c_{00}=0\): equality is equivalent to \(p=0\), exactly case (B). If there are at least two inactive edges, \(r\le m-2\), and the first term is at least \(m-1>0\) for \(m\ge2\). At \(n=2\) directly \(|T_2|=1\). A three-letter alphabet permits words in (A) of arbitrary length, for instance each prefix of the period-three word `012012...`. This proves the sharp bound and all equality cases for \(q\ge3\).

**3. Count the nonbinary equality classes.** For (A), every adjacent pair is different; a forbidden length-four alternating factor is exactly a *pair of consecutive* palindromic length-three factors. For \(n=4\), choose the first three adjacent-different letters and exclude the unique forbidden fourth-letter continuation when the first and third agree, obtaining \(A_4=q^2(q-1)(q-2)\). In a valid word, appending a letter different from the last two contributes \(q-2\) choices. Appending the letter two positions earlier produces a final palindromic triple, and is legal only if the previous final triple was not palindromic. The number of valid words of length \(n-1\) ending with a nonpalindromic triple is \((q-2)A_{n-2}\). This yields the recurrence for \(n\ge5\).

For class (B), split a word across its sole equal adjacent pair, at the boundary after position \(j\). Fix the common letter. Each side must avoid both adjacent equality and a palindromic length-three factor; the number of such side-words of length \(k\) with one specified endpoint letter is \(f_1=1\), and \(f_k=(q-1)(q-2)^{k-2}\) for \(k\ge2\). No forbidden palindrome can cross the equal pair. Sum over \(j=1,\ldots,n-1\) and the \(q\) common letters. This proves (3). At \(q=3\), \(A_n=6F_n\) for \(n\ge3\), and \(B_n=12(n-2)\) by the finite convolution, as asserted.

## Verification

`verify.py` constructs each exact-two swap output set by literal transpositions and compares its cardinality against the local support lemma. It checks the optimizer characterization and counting recurrence for every word with \(q=3\), lengths \(2\) through \(9\); \(q=4\), lengths \(2\) through \(7\); and \(q=5\), lengths \(2\) through \(6\). Binary words through length \(12\) additionally check the universal local formula, not a claimed binary optimizer classification. The full finite audit covers 79,073 words; the captured stdout is in `verification_output.txt`. Run `python3 verify.py`. Exhaustive finite checks do not establish the arbitrary-length statements: sections 1–3 give their proofs.

## Relationship to prior work

The **closest previously recorded result** is an exact formula for radius-two successive adjacent-swap output balls. It provides an exact formula for **at most two** successive adjacent swaps and gives maxima and equality cases for that larger ball. It is important not to mistake the current exact-two channel for that earlier at-most-two channel. The earlier theorem's nonbinary equality class requires all consecutive three letters to be distinct, whereas the exact-two maximizers here also allow isolated \(aba\) triples and one equal adjacent pair, and their population is the distinct Fibonacci-type recurrence plus convolution (3). The earlier full ball formula and the new two-operation support analysis are closely related; the new contribution claimed here is specifically the **complete different equality characterization and its labeled all-length enumeration**, not novelty for the at-most-two ball or for the already known binary radius-two maximum.

Kovačević, Kiah and Goyal [1] address pairwise **disjoint** adjacent transpositions and code bounds. Ataba and Zabokritskiy [2] explicitly develop the successive-transposition model and block-concatenation locality; neither inspected primary paper gives this exact-two optimizer census. Multipermutation Kendall-distance code bounds [3] concern a related packing problem. Public records on one length-three cyclic permutation burst [4] and constrained median swap graphs [5] have different output operators and constraints. No checked publication or own prior claim gives the two exact-two extremal classes and their nonbinary labeled count; an implicit prior derivation from a broader ball enumerator is a substantial priority risk and is not excluded by negative search results.

## Limitations

The main theorem and complete optimizer count concern alphabets of size \(q\ge3\), for exactly two ordered adjacent swaps including trivial equal-letter exchanges. The all-center formula (1) is used as a structural lemma, but no separate originality claim is made for all-center radius-two ball results or binary extremal values. Higher-radius coding capacity and nonuniform swap probabilities are not addressed. The finite verifier supports the identities at tested lengths only; the all-length conclusions follow from the support partition and counting arguments.

## References

[1] M. Kovačević, H. M. Kiah, K. Goyal, *Bounds on Codes Correcting Adjacent Transpositions*, arXiv:2509.06692, first submitted 2025-09-08. https://arxiv.org/abs/2509.06692

[2] A. Ataba, A. L. Zabokritskiy, *Concatenation Locality under Successive Adjacent Transpositions*, arXiv:2611.02192, first submitted 2026-11-01. https://arxiv.org/abs/2611.02192

[3] S. Buzaglo, E. Yaakobi, T. Etzion, J. Bruck, *Error-Correcting Codes for Multipermutations*, ISIT 2013. https://authors.library.caltech.edu/records/ft4vp-ka042

[4] *Exact sphere spectrum for nonbinary length-three cyclic permutation bursts*, published scientific record. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-sphere-spectrum-for-nonbinary-length-three-cyclic-permutat--31d5888bce8c

[5] *Median swap graphs for binary words with bounded monochromatic runs*, published scientific record. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-median-swap-graphs-for-binary-words-with-bounded-monochromatic-r--b743472fbcd0
