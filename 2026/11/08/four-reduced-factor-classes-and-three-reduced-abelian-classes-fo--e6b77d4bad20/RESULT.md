# Four reduced factor classes and three reduced Abelian classes for every Sturmian word

## Finding

For every aperiodic binary Sturmian word \(\mathbf{s}\), let \(\operatorname{red}(w)\) collapse each maximal constant-letter run of a nonempty factor \(w\) to one letter. Denote by \(p^{\rm red}_{\mathbf{s}}(n)\) the number of distinct collapsed length-\(n\) factors, and by \(p^{\rm ab,red}_{\mathbf{s}}(n)\) the number of their Parikh vectors. Then

\[
 p^{\rm red}_{\mathbf{s}}(n)=\begin{cases}2&n=1,\\3&n=2,\\4&n\ge3,\end{cases}
 \qquad
 p^{\rm ab,red}_{\mathbf{s}}(n)=\begin{cases}2&n=1,2,\\3&n\ge3.\end{cases}
\]

More precisely, the theorem determines the sizes of all four fibers among the \(n+1\) **distinct** length-\(n\) Sturmian factors, and the occurrence frequencies of those fibers, for every irrational slope and every \(n\ge3\). These refinements depend only on three rotation breakpoints.

## Assumptions and scope

Use the lower mechanical coding of irrational slope \(0<\alpha<1\):
\[
 w_i(x)=\lfloor x+(i+1)\alpha\rfloor-\lfloor x+i\alpha\rfloor\quad(0\le i<n),\qquad 0\le x<1.
\]
Its length-\(n\) language equals that of every Sturmian word with slope \(\alpha\), regardless of intercept. Exchanging the two letters replaces \(\alpha\) with \(1-\alpha\). Hence for the explicit formula take \(\beta=\min(\alpha,1-\alpha)\), so that \(0<\beta<1/2\), and restore the letter exchange afterward if necessary.

For \(n\ge3\), define \(t_j=1-\{j\beta\}\) for \(1\le j\le n\); put \(t_0=0\) and sort the \(n+1\) distinct points into \(0=q_0<q_1<\cdots<q_n<1\). Sort the three marked points \(t_1,t_{n-1},t_n\) into \(u_1<u_2<u_3\), and let their ranks in the ordered list \(q_0,\ldots,q_n\) be \(r_1<r_2<r_3\) (zero-based, so each rank is at least one).

**Exact fiber formula.** In increasing mechanical-intercept order, the four reduced factor classes have numbers of distinct ordinary factors
\[
 (r_1,\ r_2-r_1,\ r_3-r_2,\ n+1-r_3).
\]
Their frequencies among occurrences of length-\(n\) factors in any Sturmian word with slope \(\beta\) are respectively
\[
 (u_1,\ u_2-u_1,\ u_3-u_2,\ 1-u_3).
\]
When \(\alpha>1/2\), the same counts and frequencies apply after exchanging \(0\) and \(1\). All four counts and frequencies are strictly positive.

To recover the reduced Abelian class sizes, set \(\phi=\{(n-1)\beta\}\), \(\theta=\{n\beta\}\), and order the events \(T=t_n\), \(P=t_{n-1}\), and \(A=t_1\) from left to right. Only the four orders \(TPA,TAP,PAT,APT\) can occur. For \(TPA\) or \(TAP\), merge the **second and fourth** reduced classes; for \(PAT\) or \(APT\), merge the **first and third**. The other two classes remain singleton classes under the reduced Abelian equivalence. Add the relevant pairs of multiplicities or frequencies to obtain every reduced Abelian fiber.

## Proof

**1. Rotation intervals.** Irrationality ensures that \(0,t_1,\ldots,t_n\) are pairwise distinct. For fixed \(n\), the length-\(n\) mechanical factor is constant on each half-open interval \([q_i,q_{i+1})\), taking \(q_{n+1}=1\). By the standard Sturmian rotation/factor correspondence these \(n+1\) intervals represent the \(n+1\) different factors, one per interval. The orbit of every initial intercept under irrational rotation is dense and uniformly distributed, giving frequency equal to the length of each union of intervals.

**2. Three-breakpoint formula.** Since \(0<\beta<1/2\), two consecutive letters \(1\) are impossible. Write \(K_j(x)=\lfloor x+j\beta\rfloor\), \(s=w_0(x)=K_1(x)\), and let \(a(x)\) be the number of adjacent changes in the length-\(n\) factor. Every occurrence of \(1\) contributes two changes, except for a \(1\) at either endpoint. Thus
\[
 a(x)=2K_n(x)-s(x)-[K_n(x)-K_{n-1}(x)]
      =K_n(x)+K_{n-1}(x)-s(x).
\]
Set \(B=\lfloor n\beta\rfloor+\lfloor(n-1)\beta\rfloor\). Since \(x\in[0,1)\), this becomes the exact identity
\[
 s(x)=\mathbf1_{x\ge t_1},\qquad
 a(x)=B+\mathbf1_{x\ge t_n}+\mathbf1_{x\ge t_{n-1}}-\mathbf1_{x\ge t_1}.
\]
For \(n\ge3\), these three thresholds are distinct. Crossing \(t_n\) or \(t_{n-1}\) increases \(a\) by one without changing \(s\); crossing \(t_1\) decreases \(a\) by one and changes \(s\) from zero to one. Therefore the four successive intervals delimited by \(u_1,u_2,u_3\) have four different pairs \((s,a)\): within either fixed value of \(s\), the \(a\)-values increase strictly, while pairs with different \(s\) differ. Since a reduced binary word is exactly determined by its initial letter and number \(a+1\) of runs, the four intervals are exactly the four reduced classes. Counting their component Sturmian-factor intervals proves the rank formula; irrational equidistribution proves the frequency formula.

**3. Exact Abelian merging.** The reduced word is alternating, with \(r=a+1\) letters. Its Parikh vector is \((\lceil r/2\rceil,\lfloor r/2\rfloor)\) if it begins in \(0\), with entries swapped if it begins in \(1\). Thus two reduced classes with different starting letters merge exactly when they have the same even \(r\).

Let \(m=\lfloor(n-1)\beta\rfloor\) and \(\phi=\{(n-1)\beta\}\). If \(\phi+\beta<1\), then \(\theta=\phi+\beta\), \(B=2m\), and \(t_n\) precedes both other thresholds. The possible event orders are \(TPA\) and \(TAP\). Their four successive \((s,a)\) pairs are, respectively,
\[
 \begin{array}{c|cccc}
 TPA&(0,B)&(0,B+1)&(0,B+2)&(1,B+1)\\
 TAP&(0,B)&(0,B+1)&(1,B)&(1,B+1)
 \end{array}.
\]
Since \(B\) is even, exactly classes two and four have the same reduced Parikh vector (their common run count \(B+2\) is even).

If \(\phi+\beta>1\), then \(\theta=\phi+\beta-1\), \(B=2m+1\), and \(t_n\) follows both others. The possible orders and their successive pairs are
\[
 \begin{array}{c|cccc}
 PAT&(0,B)&(0,B+1)&(1,B)&(1,B+1)\\
 APT&(0,B)&(1,B-1)&(1,B)&(1,B+1)
 \end{array}.
\]
Now \(B\) is odd, and precisely classes one and three merge (common even run count \(B+1\)). The other pairs have different Parikh vectors. Equality \(\phi+\beta=1\) is impossible by irrationality. This proves the three reduced Abelian classes and their merger profile.

**4. Small lengths and complementary slopes.** At length one the factors are \(0,1\). At length two the three factors for \(\beta<1/2\) are \(00,01,10\); their reductions are all distinct and their reduced Parikh vectors have two types. For \(\alpha>1/2\), complement every factor to obtain the same complexity counts and fiber multiplicities. All statements follow for every irrational slope and every Sturmian intercept.

## Verification

Run `python3 verify_sturmian.py` using Python 3 without external dependencies. It independently enumerates factors by mechanical-intercept cells for ten irrational slopes and all \(1\le n\le300\) (3,000 parameter pairs), including rank multiplicities and the complete Abelian merger rule. It also computes direct length-\(n\) factors from 12,000-symbol mechanical prefixes for four irrational slopes and \(1\le n\le100\), checking ordinary complexity and the two reduced complexity counts. These finite tests passed. The proof above, not the finite checks, establishes the arbitrary-length theorem.

## Relationship to prior work

Campbell, Currie and Rampersad (2025) introduced precisely these reduced factor and reduced Abelian equivalences and evaluated them for Thue–Morse and paperfolding words; their results do not provide the Sturmian value or the four-fiber classification. Carey and Clampitt (2018) established the rotation-interval correspondence and fixed-partition height-profile varieties for Sturmian factors. That interval correspondence is used here, but run reduction has a variable, input-dependent partition, and neither their fixed-partition varieties nor their results state the three-breakpoint run-collapse/Abelian-merger theorem. Launer, Puzynina and Voloshinova (2026) study group complexities defined by permutations of the original letters, a different, length-preserving equivalence that does not encode the run-collapse operation. The exact reduction-class multiplicities and frequencies are the additional claimed contribution, not the classical Sturmian interval description itself.

## Limitations

The result is restricted to aperiodic binary Sturmian languages and the specific run-collapsing reduction. It does not classify finite balanced words, other low-complexity morphic shifts, or higher-alphabet reductions. The computer checks are finite corroboration only; published-record searches and source comparisons cannot exclude every unindexed equivalent theorem. No external mathematical audit has been performed.

## References

1. J. M. Campbell, J. Currie, N. Rampersad, *Reduced complexities for sequences over finite alphabets*, arXiv:2509.16034 (first posted 2025-09-19), https://arxiv.org/abs/2509.16034.
2. N. Carey and D. Clampitt, *Partitioned Factors in Christoffel and Sturmian Words*, arXiv:1804.08724 (2018), https://arxiv.org/html/1804.08724v2.
3. M. Launer, S. Puzynina, E. Voloshinova, *On possible values of the group complexity function of infinite words*, arXiv:2607.07620 (2026), https://arxiv.org/abs/2607.07620.
