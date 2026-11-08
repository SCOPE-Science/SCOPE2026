# Sharp factor-completion thresholds for Brik's infinite binary word

## Finding

Let \(B_1=101\) and, for each \(i\ge1\), obtain \(B_{i+1}\) by adjoining to \(B_i\) its suffix after removing the first \(i\) letters. Let \(b\) be the infinite binary word having all \(B_i\) as prefixes. Write \(t(w)\) for the least *one-based starting position* of a contiguous factor \(w\) in \(b\). Define
\[
r_1=1,\qquad r_2=5,\qquad r_{n+1}=2^{r_n-2}+r_n\quad(n\ge2).
\]

**Theorem.** For every integer \(n\ge3\), the set of length-\(n\) factors consists of the binary strings avoiding \(00\), and
\[
\max_{\substack{|w|=n,\;00\not\subseteq w\\ w\ne 1^n}}t(w)=r_{n-1},
\qquad t(1^n)=r_n.
\]
The first maximum is attained by \(1^{n-1}0\). Thus \(1^n\) is the **unique last new length-\(n\) factor** and the longest wait before all length-\(n\) factors are present in a finite prefix is exact:
\[
U(n)=r_n+n-1\quad (n\ge2),\qquad U(1)=2.
\]
In particular \(U(2)=6\), \(U(3)=15\), \(U(4)=2064\), and \(U(5)=2^{2059}+2065\). The result is a sharp factor-completion cutoff, rather than merely a recurrence for the appearance of a single long run.

## Assumptions and scope

Words and positions are one-based. Formally \(B_{i+1}=B_i B_i[i+1\ldots |B_i|]\), where the second interval is a suffix of \(B_i\), and the prefix limit \(b\) exists. A finite binary word is *legal* when it avoids \(00\) as a contiguous factor. We adopt the established facts from Shallit [1]: \(|B_i|=2^{i-1}+i+1\), every \(B_i\) ends in \(01\), the legal words are exactly the factors of \(b\), and \(t(1^n)=r_n\) with the recurrence above. The following quantitative prefixing lemma and penultimate-first-occurrence theorem are proved here.

## Proof

**1. Quantitative boundary-prefixing lemma.** Define \(f(p)=2^{p-2}+p=|B_{p-1}|\) for \(p\ge2\). Suppose a word \(v\) of length \(k\) occurs at position \(p\) of \(b\) and \(p\ge k+2\). As
\[
|B_{p-1}|-p+1=2^{p-2}+1\ge k,
\]
the occurrence is already wholly within \(B_{p-1}\). Hence the appended suffix in \(B_p\) begins with \(v\); since \(B_{p-1}\) ends in \(01\), the words \(1v\) and \(01v\) occur, respectively, starting at positions \(f(p)\) and \(f(p)-1\) of \(b\). These new starts are at least their respective word lengths plus two when \(p\ge k+2\) and \(k\ge2\). This is the inductive *safe-occurrence* property.

**2. Small explicit safe bases.** For \(n=3\), the legal words and safe occurrence starts are

| word | 010 | 011 | 101 | 110 | 111 |
|---|---:|---:|---:|---:|---:|
| safe start | 7 | 9 | 6 | 5 | 13 |

All starts are at least \(n+2=5\). Their earliest occurrences, however, need not themselves be safe: the first occurrences of \(010,011,101,110\) start at positions \(2,4,1,5\), respectively. The non-all-ones first-occurrence bound at \(n=3\) is therefore checked directly; the stronger *safe-occurrence* induction begins at \(n=4\). At \(n=4\), the legal words and safe starts are

| word | 0101 | 0110 | 0111 | 1010 | 1011 | 1101 | 1110 | 1111 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| safe start | 7 | 9 | 12 | 6 | 8 | 10 | 13 | 2061 |

Here all starts are at least \(6\), every non-all-ones word starts at most \(r_3=13\), and the all-ones word starts at \(r_4=2061\). Every length-three legal word has a safe start at most \(r_3=13\). All these facts can be checked directly in \(B_{13}\), whose length is \(4110\).

**3. Upper bound on non-all-ones first occurrences.** Inductively assume for some \(n\ge4\): (i) every legal length-\(n\) word has a safe start no later than \(r_n\); (ii) a length-\(n\) word other than \(1^n\) has a safe start no later than \(r_{n-1}\); and (iii) every legal length-\(n-1\) word has a safe start no later than \(r_{n-1}\). The bases in step 2 establish these conditions when \(n=4\).

Take a legal length-\(n+1\) word \(w\). If it begins in \(1\), write \(w=1v\) for a legal length-\(n\) word. Applying the boundary-prefixing lemma to a safe occurrence of \(v\) at \(p\le r_n\), we get a safe occurrence of \(w\) by \(f(p)\le f(r_n)=r_{n+1}\). If \(w\ne1^{n+1}\), then \(v\ne1^n\), and the improved bound \(p\le r_{n-1}\) yields a safe occurrence by \(r_n\). Otherwise \(w\) begins in \(0\). Legalness forces \(w=01v\), where \(v\) is legal and has length \(n-1\). The lemma applied to a safe occurrence of \(v\) at \(p\le r_{n-1}\) yields a safe occurrence by \(f(p)-1<r_n\). Thus every legal length-\(n+1\) factor has a safe start by \(r_{n+1}\), and every non-all-ones one by \(r_n\). Induction proves the claimed quantitative upper bounds for all \(n\ge4\). For length three, all non-all-ones first starts are at most 5, verified directly by their earliest occurrences, so the weaker first-occurrence (not safe-occurrence) bound holds there as well.

**4. Sharpness of the penultimate bound.** The first \(1^k\) begins at \(r_k\) and is followed immediately by \(0\), for every \(k\ge2\). At \(k=2\), the prefix is \(1010110\), so the first \(11\) is followed by zero. Suppose the first \(1^k\) is followed by \(0\). By the first-run proof in [1, Theorem 4], the first \(1^{k+1}\) is formed across the concatenation boundary in \(B_{r_k}\), starting at \(f(r_k)=r_{k+1}\), with its final \(k\) ones copied from the suffix beginning at the old first occurrence \(r_k\). That suffix contains at least \(k+1\) letters, and the letter following those \(k\) ones is therefore the copied \(0\). So the first \(1^{k+1}\) is also followed by zero. The induction follows. Consequently the factor \(1^k0\) first occurs exactly at \(r_k\): it cannot occur before the first \(1^k\), and it does occur there.

Putting \(k=n-1\) establishes \(t(1^{n-1}0)=r_{n-1}\) for \(n\ge3\). In conjunction with step 3, this proves the claimed equality for non-all-ones legal factors. Source [1, Theorem 4] gives the first all-ones occurrence at \(r_n\). Since \(r_n>r_{n-1}\), \(1^n\) uniquely arrives last. The shortest prefix containing every legal length-\(n\) factor must include its entire first occurrence, so its length is \(r_n+n-1\). For \(n=2\) the same completion formula follows by directly observing that \(11\) first occurs at position 5, and for \(n=1\) both symbols have appeared by position 2.

## Verification

The standalone `verify.py` uses only Python's standard library. It builds \(B_1,\ldots,B_{13}\) directly from the recurrence, checks all finite base starts, all one-run onset positions through length four, the boundary-prefixing identity at twelve finite stages, the complete construction of all safe length-five words by the induction, and the exact prefix-completion values for lengths two through four. It returns `BRIK_COMPLETION_VERIFY_OK base_3_4 lifted_5 2064`. This finite computation checks the bases and construction, **not** the infinitely quantified conclusion by exhaustive enumeration: the proof of the latter is steps 1–4.

## Relationship to prior work

Shallit [1] proves that the factors are exactly binary words avoiding \(00\) (Theorem 7) and determines the first occurrences of \(1^n\) (Theorem 4). Neither statement alone determines whether another factor first appears later, the next-to-last first occurrence, or the shortest prefix that contains the entire length-\(n\) factor language. The quantitative safe-occurrence lemma and two-level induction determine these missing bounds and their sharpness. The result does not imply an algorithmic lower bound for all factor-enumeration algorithms; its completion time is a property of this particular infinite word.

## Limitations

The first-occurrence statements apply to contiguous factors of the fixed binary sequence and use one-based positions. The penultimate-position assertion is stated for \(n\ge3\), while the completion formula also covers \(n=2\). The theorem does not classify the order of arrival of all the remaining legal factors or address other infinite words. The finite tests are not substitutes for the inductive infinite argument. Independent mathematical validation and exhaustive historical-priority confirmation have not been performed.

## References

[1] Jeffrey Shallit, *Brik's sequence: a strange recursion*, arXiv:2605.07542v1, first publicly submitted 8 May 2026. https://arxiv.org/abs/2605.07542 ; full text https://pdfs.assets.alphaxiv.org/2605.07542v1.pdf . In particular, Proposition 1 and Theorems 4 and 7.
