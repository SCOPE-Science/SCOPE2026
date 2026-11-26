# Two-to-one binomial reconstruction and linear ambiguity in the Cantor word

## Finding

Let \(\mathbf c\) be the one-sided binary Cantor word, the fixed point beginning in \(1\) of the morphism \(\sigma(1)=101\), \(\sigma(0)=000\). Two binary words are *\(2\)-binomially equivalent* when every scattered subsequence of length at most two occurs with the same multiplicity in both words. Let \(\mathcal F_n\) denote the set of **distinct** contiguous factors of \(\mathbf c\) of length \(n\).

**Theorem.** For each integer \(k\ge3\), put \(n=3^k\). Every \(2\)-binomial equivalence class in \(\mathcal F_n\) contains at most **two** distinct words; this bound is attained. More strongly, at least
\[
  2\cdot3^{k-3}+1=\frac{2n}{27}+1
\]
**different equivalence classes contain exactly two distinct words**, with explicit representatives given in the proof. Hence ambiguity is simultaneously bounded per observation and present in a number of observations growing linearly with \(n\).

The theorem asserts a lower bound on the number of double classes, **not** a complete classification of all classes or an exact formula for the entire \(2\)-binomial complexity.

## Assumptions and scope

The binary alphabet is \(\{0,1\}\). Factors are non-circular contiguous substrings of the infinite word, and words are counted as *distinct strings*, independently of how many times they occur. Position indices in finite strings begin at zero. A scattered subsequence \(v\) of \(w\) is selected from strictly increasing index positions. The symbol \(0^a\) means \(a\) consecutive zeros for an integer \(a\ge0\). Define \(C_k=\sigma^k(1)\); then \(|C_k|=n\), \(|C_k|_1=2^k\), and \(C_k\) is a palindrome.

For a length-\(n\) binary word \(w\), let \(t(w)\) count its ones and let \(s(w)\) be the sum of their zero-based positions. The pair \((t(w),s(w))\) is its second-binomial signature. Indeed, if the ones occupy positions \(p_1<\cdots<p_t\), the multiplicity of scattered \(01\) equals \(\sum_jp_j-\binom t2\). All other subsequence counts of lengths zero, one, or two follow from \(n\), \(t\), and this multiplicity: those of \(00\) and \(11\) are binomial coefficients, and the multiplicities of \(01\) and \(10\) sum to \(t(n-t)\). Therefore two length-\(n\) words are \(2\)-binomially equivalent **exactly when** their signatures agree.

## Proof

**Step 1: exhaustive two-family description of factors.** The morphism supplies a tiling of \(\mathbf c\) by length-\(n\) blocks, each equal to \(C_k\) or \(0^n\), with block-type sequence again \(\mathbf c\). There is no occurrence of \(11\) in \(\mathbf c\): this holds in \(1\) and is preserved by \(\sigma\). Thus two neighboring blocks can be of types \((1,0)\), \((0,1)\), or \((0,0)\), never \((1,1)\). A length-\(n\) factor beginning at offset \(r\) into a block, with \(0\le r<n\), must therefore belong to one of the families
\[
  A_r=0^{n-r}\,\mathrm{pref}_r(C_k),\qquad
  B_r=\mathrm{suff}_{n-r}(C_k)\,0^r,
  \quad 0\le r\le n.
\]
The all-zero factor is \(A_0=B_n\). Every \(A_r\) and \(B_r\) actually occurs, because the adjacent block types \(01\) and \(10\) both occur in \(\mathbf c\). Hence
\[
 \mathcal F_n=\{A_r:0\le r\le n\}\cup\{B_r:0\le r\le n\}.
\]
The boundary representations at \(r=n\) merely describe the same aligned factor as an offset-zero representation; no new factors are introduced.

**Step 2: signature injectivity within each family.** Write \(t_r=|\mathrm{pref}_r(C_k)|_1\) and \(P_r\) for the sum of one-positions within that prefix. The signature of \(A_r\) is
\[
  (t_r,\,P_r+(n-r)t_r).
\]
The integer \(t_r\) is nondecreasing. Whenever \(t_r=t_{r+1}>0\), the displayed second coordinate decreases by exactly \(t_r\). The value \(t_r=0\) occurs only at \(r=0\), since \(C_k\) starts in \(1\). Thus the signatures of all \(A_r\) are pairwise distinct. Since \(C_k\) is a palindrome,
\[
 B_r=\operatorname{rev}(A_{n-r}),
\]
and reversal sends \((t,s)\) to \((t,(n-1)t-s)\). Consequently the signatures of all \(B_r\) are pairwise distinct as well. Each equivalence class can contain at most one factor from each family, proving the upper bound of two.

**Step 3: a linearly large, explicitly paired family.** Fix \(k\ge3\), and set \(T=2^k\), \(t=3T/4\), and \(n=3^k\). The decomposition
\[
 C_k=C_{k-1}0^{n/3}C_{k-1},\qquad
 C_{k-1}=C_{k-2}0^{n/9}C_{k-2}
\]
shows that the first \(t\) ones of \(C_k\) consist of all \(T/2\) ones in the first copy of \(C_{k-1}\), followed by the first \(T/4\) ones in the final copy's first \(C_{k-2}\). Their last position is \(7n/9-1\); the next one is at position \(8n/9\). Therefore all prefixes of lengths
\[
 \frac{7n}{9}\le r\le\frac{8n}{9}
\]
have exactly \(t\) ones. A palindromic length-\(L\) binary word with \(h\) ones has one-position sum \(h(L-1)/2\). Applying this separately to the two completed blocks above, the one-position sum of these first \(t\) ones is
\[
 P=\frac T2\frac{n/3-1}{2}
    +\frac T4\left(\frac{2n}{3}+\frac{n/9-1}{2}\right)
   =T\left(\frac{19n}{72}-\frac38\right).
\]
Hence \(2P/t=19n/27-1\). Consider each integer
\[
 \frac{22n}{27}\le r\le\frac{24n}{27},
 \qquad u=\frac{46n}{27}-r.
\]
Since \(n\) is divisible by \(27\), all endpoints and \(u\) are integers, and both \(r\) and \(u\) lie between \(7n/9\) and \(8n/9\). The signature of \(A_r\) has second coordinate \(P+t(n-r)\). As \(B_{n-u}=\operatorname{rev}(A_u)\), its second coordinate is
\[
 (n-1)t-[P+t(n-u)].
\]
These two quantities are equal precisely when \(r+u=n+1+2P/t=46n/27\), as required. Thus \(A_r\) and \(B_{n-u}\) are \(2\)-binomially equivalent.

They are nevertheless **different strings**. The last one in \(A_r\) is at position \(48n/27-r-1\), whereas the last one in \(B_{n-u}\) is at position \(u-1\). Their positions differ by the strictly positive integer \(2n/27\). Finally, the \(A_r\) signatures are distinct as \(r\) varies, by Step 2. There are exactly
\[
  \frac{24n}{27}-\frac{22n}{27}+1=\frac{2n}{27}+1
\]
values of \(r\). Each produces a *different* binomial equivalence class containing two *different* factors. By Step 2 none of these classes can have a third factor. This proves every assertion. \(\square\)

## Verification

The accompanying standalone `checker.py` reconstructs the Cantor blocks independently of the proof, enumerates the predicted two factor families, checks their presence in a longer finite prefix, evaluates \(2\)-binomial signatures, and verifies every explicitly paired class. It checks \(k=1,2,3,4,5,6,7\) (the asserted lower-bound family for \(k\ge3\)). In particular the observed numbers of distinct factors, distinct signatures, and size-two signature classes at \(k=3,4,5,6,7\) are respectively
\[
 (53,50,3),\ (161,154,7),\ (485,466,19),\ (1457,1402,55),\ (4373,4210,163).
\]
These are **finite observations**, not an assertion of a closed formula for all possible classes. The theorem for arbitrary \(k\) follows from the block decomposition, injectivity, and explicit algebra in the proof, not from the tests.

Reproduce with Python 3 by running `python checker.py` in a directory containing that file. No third-party packages, external datasets, or random seeds are required.

## Relationship to prior work

Rigo and Salimov introduced and studied binomial complexity, including binary \(2\)-binomial equivalence. Their 2015 article treats Sturmian words and fixed points of Parikh-constant morphisms. The morphism considered here is **not** Parikh-constant: the image of \(1\) has two ones while that of \(0\) has none. Their classification and boundedness statements do not give this Cantor-word reconstruction theorem.

The Cantor sequence itself has a literature on factor complexity and \(k\)-Abelian complexity. Chen, Lü and Wu show that its \(k\)-Abelian complexities are \(3\)-regular and describe endpoint-conditioned classes. Their \(k\)-Abelian equivalence counts **contiguous** short factors rather than **scattered** subsequences. Equality of \(2\)-Abelian signatures does not establish equality of \(2\)-binomial signatures. Their results therefore do not settle the particular two-to-one bound and explicit linear family here. The general ambient binary \(2\)-binomial class-size distribution, also studied subsequently, does not by itself determine class intersections with the Cantor factor language.

## Limitations

The lower bound on size-two classes may be strict; no exact all-scale count of such classes, nor of all \(2\)-binomial classes, is proved. No assertion is made for arbitrary lengths not equal to powers of three, for higher-order binomial equivalence, or for any other morphic word. The result is a direct mathematical proof subject to ordinary scholarly verification; no independent audit has been performed. A prior equivalent statement under different terminology cannot be ruled out absolutely.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079, 217–228, DOI 10.1007/978-3-642-40579-2_23. Public preprint listing: https://orbi.uliege.be/handle/2268/149313 .
2. M. Rigo and P. Salimov, *Another generalization of abelian equivalence: binomial complexity of infinite words* (extended version), *Theoretical Computer Science* 601 (2015), 47–57. Full author preprint: https://orbi.uliege.be/bitstream/2268/178703/1/binomial_TCS_final.pdf .
3. J. Chen, X. Lü and W. Wu, *On the k-Abelian complexity of the Cantor sequence*, arXiv:1703.04063 (first posted 12 March 2017). Full text: https://arxiv.org/html/1703.04063v1 . (This later work is used for comparison, not as the archival anchor.)
4. X.-T. Lü, J. Chen, Y. Guo and Z.-X. Wen, *On the permutation complexity of the Cantor-like sequences*, *Theoretical Computer Science* 616 (2016), 100–110, DOI 10.1016/j.tcs.2015.12.022 (context on the Cantor substitution; only publicly accessible excerpt was examined).
