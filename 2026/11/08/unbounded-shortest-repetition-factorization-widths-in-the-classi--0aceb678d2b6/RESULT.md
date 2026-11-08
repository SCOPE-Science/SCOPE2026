# Unbounded shortest repetition-factorization widths in the classical period-doubling word

## Finding

Consider the classical period-doubling word \(p=(p(n))_{n\ge0}\) defined by
\[
p(n)=\nu_2(n+1)\bmod 2,
\]
where \(\nu_2(z)\) is the exponent of \(2\) dividing the positive integer \(z\). Equivalently, \(p\) is the fixed point beginning with \(0\) of \(0\mapsto01\), \(1\mapsto00\).

A *repetition* is a nonempty finite word possessing a period \(d\ge1\) no greater than half its length. For a repetition-factorizable word \(u\), let \(\operatorname{sw}(u)\) be the minimum number of consecutive repetition factors whose concatenation is \(u\). For every integer \(r\ge1\), put
\[
W_r=p[2:2^{r+1}),
\]
using zero-based, start-inclusive/end-exclusive interval notation. Then \(W_r\) is repetition-factorizable and
\[
\boxed{\lfloor r\log_3 2\rfloor+1\le \operatorname{sw}(W_r)\le r.}
\]
In particular, shortest repetition-factorization width is unbounded among factors of this classical binary automatic word.

The structural ingredient is stronger: if \(p[a:a+\ell)\) is a repetition and \(d\le\ell/2\) is any one of its repetition periods, then \(d\) is a power of two, \(a\ge2d\), and \(\ell\le4d-1\). Consequently every such repetition ends strictly before position \(3a\).

## Assumptions and scope

All indices \(a\) are nonnegative integers. The valuation is evaluated only at positive integers. A period \(d\) of a length-\(\ell\) factor at \(a\) requires \(p(n)=p(n+d)\) for every integer \(a\le n<a+\ell-d\). To count as a repetition, \(1\le d\le\ell/2\). Arbitrarily many different periods may be allowed; the theorem treats *every* period satisfying this inequality. The empty word is excluded. The bounds apply to the stated family of finite factors, not to all length-\(2^{r+1}-2\) factors nor to all binary automatic words.

## Proof

**Lemma 1 (the only possible repetition periods are dyadic).** Write a positive candidate period as \(d=2^k u\), with \(k\ge0\) and \(u\ge1\) odd, and put \(h=2^k\). At each position \(n=hq-1\), where \(q\ge1\), the equality comparison for shift \(d\) is
\[
p(hq-1)=\big(k+\nu_2(q)\big)\bmod2,\qquad
p(h(q+u)-1)=\big(k+\nu_2(q+u)\big)\bmod2.
\]
If \(q\equiv2\pmod4\), then \(\nu_2(q)=1\) while \(q+u\) is odd, so the two letters differ for *every* odd \(u\). These mismatch positions form a progression with step \(4h\). Therefore, when \(u\ge5\), every interval of \(d=uh\ge5h\) consecutive comparison positions contains a mismatch, and no length-\(2d\) factor can have period \(d\).

When \(u=3\), positions with \(q\equiv3\pmod4\) are also mismatches: \(q\) is odd while \(q+3\equiv2\pmod4\). Every three consecutive integers \(q\) contain a residue congruent to \(2\) or \(3\) modulo \(4\). Every interval of \(3h=d\) consecutive comparison positions contains three consecutive positions of the form \(hq-1\); hence it contains a mismatch. Thus \(u=3\) is impossible as well. Therefore, any repetition period has \(u=1\), so it is \(d=h=2^k\).

**Lemma 2 (location and maximal length).** Fix a dyadic period \(h=2^k\). At \(n=hq-1\), differences occur whenever \(q\equiv1\pmod4\) or \(q\equiv2\pmod4\): in the former case \(q+1\equiv2\pmod4\), and in the latter case \(q\equiv2\pmod4\) but \(q+1\) is odd. These mismatch locations have successive gaps at most \(3h\). Therefore a comparison interval free of mismatches has length strictly less than \(3h\). A length-\(\ell\) factor with period \(h\) needs \(\ell-h\) consecutive matching comparisons. Hence \(\ell-h<3h\), or \(\ell\le4h-1\).

Further, if \(0\le a<2h\), the first \(h\) comparison positions \(a,a+1,\ldots,a+h-1\) contain \(h-1\) when \(a<h\), or \(2h-1\) when \(h\le a<2h\). Both are mandatory mismatches (corresponding to \(q=1\) and \(q=2\)). A length-\(\ell\ge2h\) factor would need these comparisons to match. Thus \(a\ge2h\). Its endpoint satisfies
\[
a+\ell\le a+4h-1\le3a-1<3a.
\]
This proves both structural claims.

**Lemma 3 (explicit dyadic square factors).** For each integer \(j\ge1\), the block \(B_j=p[2^j:2^{j+1})\) has length \(2^j\) and period \(h=2^{j-1}\). Indeed, compare \(p(n)\) and \(p(n+h)\) for \(2h\le n<3h\). If \(h\nmid(n+1)\), adding \(h\) leaves \(\nu_2(n+1)\) unchanged. In this interval the only multiple of \(h\) among the integers \(n+1\) is \(3h\). At that exceptional point the valuations are \(\nu_2(3h)=j-1\) and \(\nu_2(4h)=j+1\), which have the same parity. Hence the two halves agree exactly and \(B_j\) is a square.

**The claimed bounds.** The intervals \([2^j,2^{j+1})\) for \(1\le j\le r\) partition \([2,2^{r+1})\). By Lemma 3, \(W_r=B_1B_2\cdots B_r\) is a concatenation of \(r\) repetitions, proving \(\operatorname{sw}(W_r)\le r\). Conversely, suppose any repetition factorization of \(W_r\) has \(s\) factors, with successive zero-based endpoints \(2=a_0<a_1<\cdots<a_s=2^{r+1}\). Lemma 2 applies to every factor and gives \(a_{i+1}<3a_i\). Induction yields \(2^{r+1}=a_s<2\cdot3^s\). Hence \(s>r\log_3 2\), and because \(s\) is an integer, \(s\ge\lfloor r\log_3 2\rfloor+1\). This holds for *every* factorization and completes the proof. \(\square\)

The word also has bounded monochromatic runs: every even index carries \(0\), while every index congruent to \(1\pmod4\) carries \(1\). Thus the maximum run of zeros has length at most \(3\) and adjacent ones never occur. The unbounded width is not a consequence of increasing constant-run lengths.

## Verification

Run \(`python3 verify.py`\) with Python 3. The standalone program computes the digit-valuation word directly and tests every potential repetition period through \(128\) at starting positions through \(2048\), including all maximal comparison runs required for the finite tests. It tests the explicit square blocks through scale \(13\), and computes shortest factorization widths independently by dynamic programming for \(W_r\) with \(1\le r\le10\). Expected terminal line: \(`VERIFY_OK squares_checked= 5518 max_start= 2048 max_period= 128 block_scales= 13`\). It is a finite diagnostic; the preceding lemmas prove the quantified infinite statement.

## Relationship to prior work

Shallit and Xu [1] define the same repetition-factorization invariant, construct bounded-width descriptions for several other classical automatic words and discuss unbounded shortest width as an open decision problem. Their sections on Fibonacci, Thue–Morse, paperfolding and Rudin–Shapiro sequences do not establish the present period-doubling statement. Goc and Shallit [2] prove that every positive integer is the *least period* of some finite factor of the period-doubling word. This does not imply the existence of a repetition at that period, since a factor may have length strictly less than twice its period; the present lemma specifically concerns periods of repetition factors. Currie [3] studies avoidable binary patterns and good words related to period-doubling, without giving these shortest repetition-factorization bounds. Bognini and Ammar [4] study kernel-word and gap-word factorizations of generalized period-doubling sequences, a different factorization notion. Bognini, Kaboré and Kientéga [5] study the same word under Ziv–Lempel and Crochemore factorization conventions, governed by earlier factor occurrences rather than repetition periods or the least number of repetition pieces. The theorem here concerns the classical sequence and the minimum number of exponent-at-least-two factors, with an explicit infinite witness family.

## Limitations

Only two-sided bounds for \(\operatorname{sw}(W_r)\) are proved; an exact formula for every \(r\), optimal factorizations of arbitrary factors and decidability of unbounded shortest width for arbitrary automatic sequences are not established. The finite checker does not prove statements for unbounded indices. Exhaustive literature discovery is not guaranteed: an equivalent result might be implicit in an unindexed paper or derivable from stronger prior structural classifications. No independent scientific audit has been performed.

## References

[1] J. Shallit and X. Xu, *Repetition factorization of automatic sequences*, arXiv:2311.14961, first posted 2023-11-25. https://arxiv.org/abs/2311.14961

[2] D. Goc and J. Shallit, *Least periods of k-automatic sequences*, arXiv:1207.5450, 2012. https://arxiv.org/abs/1207.5450

[3] J. D. Currie, *The analogue of overlap-freeness for the period-doubling sequence*, arXiv:2303.14539, 2023. https://arxiv.org/abs/2303.14539

[4] K. E. Bognini and H. Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881, 2025. https://arxiv.org/abs/2511.20881

[5] K. E. Bognini, I. Kaboré and B. Kientéga, *Ziv-Lempel and Crochemore factorizations of the generalized period-doubling word*, Advances and Applications in Discrete Mathematics 25(2), 143–159 (2020). https://doi.org/10.17654/DM025020143
