# Sharp four-adic envelope and first peak of reduced Abelian complexity in the Thue–Morse word

## Finding
For the zero-indexed Thue–Morse word \(t(k)=s_2(k)\bmod2\), let \(R(n)\) be the reduced Abelian complexity of its contiguous length-\(n\) factors (defined below). For every integer \(m\ge2\),
\[
\max_{1\le n\le4^m} R(n)=\left\lceil\frac{3(m+2)}2\right\rceil.
\]
The **least** positive integer \(n\) attaining that maximum is
\[
n_m=\frac{2\cdot4^m+4}{3}+\begin{cases}0,&m\text{ even},\\2,&m\text{ odd}.\end{cases}
\]
Moreover \(R(4^j)=4\) for every integer \(j\ge1\); the extremal oscillation has sharp asymptotic limits
\[
\limsup_{n\to\infty}\frac{R(n)}{\log_4 n}=\frac32,\qquad
\liminf_{n\to\infty}\frac{R(n)}{\log_4 n}=0.
\]

## Assumptions and scope
For a nonempty finite binary word, **run reduction** replaces each maximal consecutive block of equal letters by its single letter. The Parikh vector of the reduced word records its counts of zeros and ones, ignoring order. The number of such vectors among all length-\(n\) factors of the infinite Thue–Morse word is \(R(n)\). The initial symbol is \(t(0)=0\). The theorem concerns all positive lengths within every **four-adic prefix of the length domain**, not only those lengths which are themselves substitution powers. No limiting measure over factor starting positions is involved. The first formula excludes \(m=1\), for which the maximum is \(4\), first reached at length \(4\).

## Proof
Write \(a_n\) and \(b_n\) for the minimum and maximum numbers of *alternations* (adjacent unequal pairs) among all length-\(n\) factors, and \(w_n=b_n-a_n\). Thue–Morse factors are invariant under bitwise complement. By sliding length-\(n\) windows, alternation counts change by at most one, so every integer from \(a_n\) to \(b_n\) occurs; by complement closure, both initial bits occur for each such count. A factor with \(r\) alternations reduces to an alternating word of length \(r+1\). If \(r\) is even, the two initial-bit choices have distinct Parikh vectors; if \(r\) is odd, they have the same Parikh vector. Thus
\[
 R(n)=\sum_{r=a_n}^{b_n}\bigl(1+\mathbf1_{\{r\text{ even}\}}\bigr)
 \le\left\lceil\frac{3(w_n+1)}2\right\rceil.\tag{1}
\]
If \(w_n\) is odd, equality holds in (1) regardless of \(a_n\). If \(w_n\) is even, equality holds exactly when \(a_n\) is even.

The published Thue–Morse alternation-extrema identities [1, Lemmas 2–3] are, for positive integers \(r\),
\[
\begin{aligned}
a_{2r}&=2r-1-b_{r+1},&b_{2r}&=2r-1-a_r,\\
a_{2r+1}&=2r-b_{r+1},&b_{2r+1}&=2r-a_{r+1},\\
a_{4r}&=2r-1+a_{r+1},&b_{4r}&=2r+b_{r+1},\\
a_{4r+2}&=2r+a_{r+1},&b_{4r+2}&=2r+1+b_{r+1}.
\end{aligned}\tag{2}
\]
The first even identity is used for \(r\ge2\), with the length-two case checked directly. Twice applying (2) also gives
\[
a_{4r+1}=2r+a_{r+1},\qquad a_{4r+3}=2r+1+a_{r+1},\qquad b_{4r+3}=2r+1+b_{r+2}.\tag{3}
\]
Consequently, for \(r\ge1\),
\[
\begin{aligned}
w_{4r}&=w_{r+1}+1,&w_{4r+2}&=w_{r+1}+1,\\
w_{4r+1}&=w_{r+1},&w_{4r+3}&=w_{r+1}+(b_{r+2}-b_{r+1}).
\end{aligned}\tag{4}
\]
Because any factor can be extended to the right by one letter, and adding one letter adds at most one alternation, \(0\le b_{r+2}-b_{r+1}\le1\). The small initial widths are \(w_1=0\), \(w_2=1\), \(w_3=1\), \(w_4=2\).

Let \(q_m=(2\cdot4^m+4)/3\), an integer for every \(m\ge1\), so \(q_1=4\) and \(q_{m+1}=4(q_m-1)\). We prove by induction on \(m\ge1\):
\[
\max_{1\le n\le4^m}w_n=m+1,\qquad
q_m\text{ is the least length with }w_n=m+1.\tag{5}
\]
Both assertions hold at \(m=1\). Assume (5) at rank \(m\). For each \(n\le4^{m+1}\), formula (4), apart from the directly checked first few lengths, reduces \(w_n\) to \(w_s\) with \(s\le4^m+1\), and increases its value by at most one. At the sole extra index \(s=4^m+1\), repeated odd-index reduction \(w_{2r+1}=w_{r+1}\), together with \(w_2=1\), gives \(w_{4^m+1}=1\). Hence \(w_n\le m+2\). The particular index \(n=q_{m+1}=4(q_m-1)\) satisfies \(w_n=w_{q_m}+1=m+2\). For any \(n<q_{m+1}\), the reduced index in (4) is strictly less than \(q_m\), and its width is at most \(m\) by the first-attainment induction hypothesis; therefore \(w_n\le m+1\). This proves (5).

At \(q_1=4\), \(a_{q_1}=1\). By (2),
\[
a_{q_{m+1}}=2(q_m-1)-1+a_{q_m},\]
so \(a_{q_m}\equiv m\pmod2\). If \(m\ge2\) is even, \(w_{q_m}=m+1\) is odd and equality in (1) gives \(R(q_m)=3(m+2)/2\). No earlier index attains that bound, because (5) gives strictly smaller width earlier. If \(m\ge3\) is odd, \(w_{q_m}=m+1\) is even and \(a_{q_m}\) is odd: \(R(q_m)=(3(m+2)-1)/2\), one below the possible maximum. The next length \(q_m+1=4(q_{m-1}-1)+1\) has width \(w_{q_{m-1}}=m\), so it cannot reach the maximum. At \(q_m+2=4(q_{m-1}-1)+2\), (2) shows \(w_{q_m+2}=m+1\) and \(a_{q_m+2}\equiv a_{q_{m-1}}\equiv m-1\equiv0\pmod2\). Thus equality in (1) holds at exactly this first eligible length, giving \(R(q_m+2)=(3(m+2)+1)/2\). Combining both parity cases with the global width bound in (5) proves the sharp envelope and its least attaining length.

Finally, \(w_{4^j}=w_{4^{j-1}+1}+1=2\) for \(j\ge2\), by the same odd-index reduction; \(w_4=2\). Formula (3) shows the parity of \(a_{4^j+1}\) equals that of \(a_{4^{j-1}+1}\) when \(j\ge2\); the base \(a_5=2\) is even. Therefore \(a_{4^j}\) is odd by (2), and the three consecutive alternation levels yield exactly four Parikh classes: \(R(4^j)=4\) for every \(j\ge1\). The envelope bound between successive powers of four gives \(R(n)\le(3/2)\log_4 n+O(1)\), while the peaks at \(n_m\asymp4^m\) realize the matching limsup. The constant troughs at \(4^j\) force the liminf to zero, because \(R(n)\ge0\). This completes the proof.

## Verification
Run `python3 VERIFY.py`. The standalone program verifies the exact maxima and first maximizers independently from the alternating-extrema recursion through \(m=9\), checks the extrema by directly scanning length-\(n\) Thue–Morse windows for all \(1\le n\le512\), and independently builds the entire reduced Parikh-vector sets for every \(1\le n\le64\). Its captured deterministic output is `VERIFY_OUTPUT.txt`. The infinite claim rests on the induction above, not on those finite tests.

## Relationship to prior work
Campbell–Currie–Rampersad [1] introduced reduced Abelian complexity and proved the alternation-extrema recurrences underlying (2), but did not optimize this complexity over entire initial length intervals. A subsequent closed-form study [2] gives an exact value of reduced Abelian complexity at every length, together with a regularity statement and a base-four parity algorithm. That full pointwise evaluation is **stronger information about individual values** than the present theorem assumes; [2, Proposition 8.1] also exhibits the same length recurrence \(4,12,44,172,\ldots\) as an **unboundedness witness**, without proving these are the first width peaks or giving the optimal global reduced-Abelian maxima. The new claim instead determines the sharp global prefix maximum, the earliest peak at each four-adic scale, and the oscillatory logarithmic envelope. None of these optimized assertions was found stated in the inspected material; they are obtained by the separate first-attainment induction above. The theorem does not claim a new pointwise formula.

## Limitations
This is a self-review, not independent validation. Novelty is assessed against the cited full texts, a semantic mathematical-record search and accessible prior research claims; absence of a match does not prove publication priority. In particular, the strong existing all-length closed form [2] can in principle be optimized, and an unstated derivation in other literature is a residual priority risk. Verification experiments end at finite lengths and serve only as reproducibility checks.

## References
[1] John M. Campbell, James Currie, Narad Rampersad, *Reduced complexities for sequences over finite alphabets*, arXiv:2509.16034, first public posting 2025-09-19. https://arxiv.org/abs/2509.16034

[2] *A closed form for the reduced Abelian complexity of the Thue–Morse word, and the five open problems of Campbell, Currie and Rampersad*, first public 2026-09-07. https://ideosphere.ai/papers/redab-tm-v1.pdf
