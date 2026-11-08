# Exact automatic fair-length profile of Thue–Morse prefixes

## Finding

Let \(\mathbf t=t_0t_1\cdots\) be the binary Thue–Morse word with \(t_i\) equal to the binary digit sum of \(i\) modulo two, and let \(P_n=t_0\cdots t_{n-1}\) for \(n\ge1\). A nonempty binary word is *fair* if its scattered occurrences of \(01\) and \(10\) have the same multiplicity. The *fair length* \(\ell_F(w)\) is the least positive number of nonempty fair words whose concatenation is \(w\).

The exact profile is
\[
\ell_F(P_n)=
\begin{cases}
1,&n=1\text{ or } n=4k\ (k\ge1),\\
2,&n=2\text{ or }n=4k+1\ (k\ge1),\\
3,&n=4k+2\ (k\ge1),\\
2,&n=4k+3\ (k\ge0),\ t_k=0,\\
3,&n=4k+3\ (k\ge0),\ t_k=1.
\end{cases}
\]

Every prefix of fair length \(2\) has **exactly one** split into two nonempty fair pieces. At length \(4k+1\) it is after position \(4k\). At length \(4k+3\), where \(t_k=0\), it is after the first position. The fair-length sequence has natural densities \(1/4,3/8,3/8\) at the values \(1,2,3\), respectively, and is not ultimately periodic.

## Assumptions and scope

All occurrences here are scattered subsequences: \(\binom{w}{01}\) counts increasing index pairs bearing the letters \(0,1\). Only **nonempty** factors are allowed in a factorization. The positions are zero-based for \(t_i\); cuts are numbered by the length of the left piece. The theorem covers **every finite nonempty prefix** of the infinite Thue–Morse word, not all factors. It has no unproved asymptotic parameter.

## Proof

Put \(h(w)=|w|_0-|w|_1\) and
\[
D(w)=\binom{w}{01}-\binom{w}{10}.
\]
A word is fair precisely when \(D(w)=0\). Directly separating pairs internal to each piece from cross pairs yields, for any binary words \(u,v\),
\[
D(uv)=D(u)+D(v)+\frac{h(u)|v|-|u|h(v)}{2}.\tag{1}
\]
In particular, if both \(u,v\) are fair and \(n=|uv|\), \(j=|u|\), then
\[
2D(uv)=n h(u)-j h(uv).\tag{2}
\]

Write \(\mu(0)=0110\) and \(\mu(1)=1001\). The Thue–Morse recurrences imply that the length-four block beginning at index \(4k\) is \(\mu(t_k)\). Both blocks are balanced (their \(h\) is zero) and palindromic, hence fair (their \(D\) is zero). Identity (1) proves that every \(P_{4k}\) is balanced and fair.

Set \(\varepsilon_k=(-1)^{t_k}\). In the next block, the first, first two, and first three letters are respectively a singleton with \(h=\varepsilon_k\), a balanced word with \(D=\varepsilon_k\), and a word with \(h=-\varepsilon_k\) and \(D=2\varepsilon_k\). By (1),
\[
\begin{array}{c|c|c}
\text{length}&h(P_n)&D(P_n)\\\hline
4k&0&0\\
4k+1&\varepsilon_k&-2k\varepsilon_k\\
4k+2&0&\varepsilon_k\\
4k+3&-\varepsilon_k&2(k+1)\varepsilon_k.
\end{array}\tag{3}
\]
This proves that exactly the asserted \(4k\) prefixes and \(P_1\) are fair. The prefix \(P_{4k+1}\), for \(k\ge1\), is a fair length-four-block prefix followed by one fair singleton, so its fair length is \(2\). For \(n=4k+2\), a decomposition into two nonempty fair words would force by (2) and (3) that \(n h(u)=\pm2\). When \(k\ge1\), \(n\ge6\), so no integer \(h(u)\) is possible. Three factors suffice: \(P_{4k}\) and the two trailing singleton letters. The exceptional \(P_2=01\) is two fair singletons.

For \(n=4k+3\), first suppose \(t_k=0\). Then \(h(P_n)=-1\) and \(2D(P_n)=4k+4=n+1\). Every two-piece fair split would have to satisfy
\[
n h(u)+j=n+1,\quad 1\le j<n.
\]
As \(h(u)\) is integral, the only possible solution is \(h(u)=1\), \(j=1\). The first letter is indeed \(0\) and fair. By (1), its complementing suffix has \(D=0\): the cross term is exactly \((n+1)/2=D(P_n)\). Thus the unique split is after the first letter, proving fair length \(2\).

When \(t_k=1\), the same calculation uses \(h(P_n)=1\) and \(2D(P_n)=-(n+1)\). Equation (2) forces \(n h(u)-j=-(n+1)\). The only possible integer solution with \(1\le j<n\) is \(h(u)=-1\), \(j=1\), which is impossible because the first letter is \(0\), with \(h=1\). Hence at least three fair pieces are required. Three suffice: \(P_{4k}\), the first letter \(1\) of the final block, and the remaining \(00\), all fair. This also establishes the uniqueness statement in the \(t_k=0\) case.

For \(n=4k+1\) with \(k\ge1\), (2) and (3) yield \(n h(u)-j\varepsilon_k=-4k\varepsilon_k\). Since \(1\le j<n\), the only integer solution is \(h(u)=0\), \(j=4k\); this is the exhibited fair split. Therefore all length-two optimal decompositions are unique.

Finally, the pairs \(t_{2i},t_{2i+1}\) are complements, hence the symbols \(0,1\) each have asymptotic frequency \(1/2\). The four residue classes of \(n\pmod4\) have frequency \(1/4\). Formula (3) and the exact classification give respective frequencies \(1/4\), \(1/4+1/8=3/8\), and \(1/4+1/8=3/8\). The subsequence \(\ell_F(P_{4k+3})\) is an injective recoding of \(t_k\); since the classical Thue–Morse word is not ultimately periodic, neither is this fair-length profile. \(\square\)

## Verification

The self-contained script `verify_tm_fair_prefix.py` constructs the Thue–Morse prefix directly from binary digit parities and computes exact shortest fair factorizations of **all prefixes through length \(2048\)** using a dynamic program on all contiguous substrings. It also cross-checks direct ordered-pair counts against the incremental fair-word test and checks the complete difference table (3) through length \(2048\). It returns `TM_FAIR_PREFIX_VERIFY_OK 2048 independent_dynamic_program pair_count_crosscheck`. These finite computations check the implementation and sample consequences; the all-length classification rests on the foregoing proof.

## Relationship to prior work

Richomme, *On some 2-binomial coefficients of binary words* (2025 preprint; 2026 journal), introduces fair length in §6.3 and proves in Proposition 6.2 that **all factors** of the Thue–Morse word have fair length at most \(4\), with a factor requiring \(4\). Its proof also notes that all complete length-four substitution blocks are fair. Those results do not specify the fair lengths of individual prefixes, nor their Thue–Morse-dependent residue-four profile or unique two-factor cuts. The present calculation uses the established fairness notion and sharper prefix-boundary analysis. No assertion of priority beyond the inspected literature is made.

## Limitations

The theorem does **not** determine fair length for every factor starting at an arbitrary positive offset, even though the literature provides a general factor bound. Its asymptotic density and aperiodicity corollaries concern only the prefix-length profile. An independent mathematical review has not been performed. Publication priority beyond the inspected sources is not established.

## References

- G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159v1 (first publicly posted 2025-10-08), §§6.2–6.3, Proposition 6.2. https://arxiv.org/abs/2510.07159 ; freely available full text: https://pdfs.assets.alphaxiv.org/2510.07159v1.pdf
- J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003 (classical Thue–Morse background).
