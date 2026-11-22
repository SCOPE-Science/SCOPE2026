# Exact sign and energy laws for parity-weighted short binary representations

## Finding

For a positive integer \(n\), a *short signed-binary representation* is a finite string of digits \(\epsilon_j\in\{-1,0,1\}\) satisfying
\[
n=\sum_{j=0}^{d-1}\epsilon_j2^j,\quad \epsilon_{d-1}=1,
\]
where for \(d\ge2\) the leading two digits are not \((1,-1)\). Distinct digit strings are distinct representations. Let \(E(n)\) and \(O(n)\) be their respective counts with an even and odd number of negative digits; put \(g(n)=E(n)-O(n)\) and \(g(0)=0\).

**Theorem (dyadic sign and energy law).** For every integer \(L\ge1\), exactly \(2^{L-1}\) positive integers \(n<2^L\) have \(g(n)>0\), and
\[
\boxed{\sum_{0\le n<2^L}g(n)=L,\qquad
\sum_{0\le n<2^L}g(n)^2=\frac{3^{L-1}+1}{2}.}
\]
The known zero-set count is \(\#\{1\le n<2^L:g(n)=0\}=F_{L+1}-1\), with \(F_0=0,F_1=1\) the Fibonacci sequence; it follows that exactly \(2^{L-1}-F_{L+1}\) positive integers below \(2^L\) have \(g(n)<0\). The zero-set count itself is prior work [4] and is not a new assertion.

Hence the positive-sign class occupies exactly half of each complete dyadic interval of nonnegative integers, while the negative-sign class has limiting density one half. For uniformly sampled \(n\) in \(\{0,\ldots,2^L-1\}\), the mean signed imbalance is \(L/2^L\) but its second moment is \((3^{L-1}+1)/2^{L+1}\); its variance is that second moment minus \(L^2/4^L\). This is a sharp exponential mean-square growth law despite a logarithmic signed total at the same cutoff.

## Assumptions and scope

All claims are exact for every integer \(L\ge1\). The shortness condition excludes the specific leading pair \((1,-1)\); it does not forbid interior adjacent opposite digits. The signed imbalance is not the unweighted Stern representation count. The value \(g(0)=0\) is a convention and is included only in the two displayed sums; all sign censuses refer to positive integers. Standard binary words have no leading zeros.

## Proof

**1. A signed recurrence.** The representation definition gives \(g(1)=g(2)=1\). For \(m\ge1\), removing the final zero digit gives \(g(2m)=g(m)\). For \(m\ge1\), the final digit of a representation of \(2m+1\) is either \(+1\) or \(-1\); removing it identifies a short representation of \(m\) or of \(m+1\), respectively. The negative choice reverses sign parity. Since \(2m+1\ge3\), no prohibited leading pair arises from this operation. Thus
\[
 g(2m)=g(m),\qquad g(2m+1)=g(m)-g(m+1)\quad(m\ge1).
\]
In particular \(g(2^L)=1\) for all \(L\ge0\).

**2. The sign automaton.** Let \(v(n)=(g(n),g(n+1))=(a,b)\), so from the recurrence
\[
v(2n)=(a,a-b),\qquad v(2n+1)=(a-b,b).
\]
Each associated integral matrix is unimodular. Since \(v(1)=(1,1)\), consecutive entries are always coprime, and in particular never simultaneously zero. Use the following disjoint state classes (\(+\) and \(-\) in a state name indicate the sign of the stated nonzero coordinate):

- \(P:\ a=b>0\); \(I:\ a>0,b=0\);
- \(Z_+:a=0,b>0\); \(Z_-:a=0,b<0\);
- \(N_+:a>0,b<0\); \(N_-:a<0,b>0\);
- \(R_+:0<a<b\); \(R_-:b<a<0\).

The first binary digit \(1\) starts at \(P\). Appending one binary digit acts by the two displayed matrices. Direct sign comparison yields the *complete reachable transition table*:

| State | append 0 | append 1 |
|---|---|---|
| \(P\) | \(I\) | \(Z_+\) |
| \(I\) | \(P\) | \(I\) |
| \(Z_+\) | \(Z_-\) | \(N_-\) |
| \(Z_-\) | \(Z_+\) | \(N_+\) |
| \(N_+\) | \(R_+\) | \(N_+\) |
| \(N_-\) | \(R_-\) | \(N_-\) |
| \(R_+\) | \(N_+\) | \(N_-\) |
| \(R_-\) | \(N_-\) | \(N_+\) |

For example, \(0<a<b\) implies \(a-b<0\), explaining the two transitions out of \(R_+\); every other row follows similarly. Induction from \(P\) proves exhaustiveness of these states for all positive integers.

Count all binary words starting with \(1\) by their remaining length \(j\ge0\). Let \(p(z),i(z),z_+(z),z_-(z),n_+(z),n_-(z),r_+(z),r_-(z)\) be the ordinary generating functions of words arriving at the respective states, with coefficient \(z^j\) for \(j\) trailing bits. The table gives
\[
\begin{aligned}
 p&=1+zi,& i&=z(p+i),\\
 z_+&=zp+zz_-,&z_-&=zz_+,\\
 r_+&=zn_+,&r_-&=zn_-,\\
 n_+&=zz_-+z(n_++r_++r_-),&
 n_-&=zz_++z(n_-+r_++r_-).
\end{aligned}
\]
Thus \(p+i=1/(1-z-z^2)\), \(z_++z_-=z/(1-z-z^2)\), and subtracting/summing the last two equations gives
\[
n_++n_- = \frac{z^2}{(1-z-z^2)(1-2z)(1+z)},\quad
n_+-n_-=-\frac{z^2}{(1-z-z^2)(1+z)}.
\]
A word has \(g(n)>0\) precisely in \(P,I,N_+,R_+\). Consequently the positive-word series is
\[
p+i+n_++r_+
=\frac{1}{1-z-z^2}+(1+z)n_+
=\frac{1-z}{1-2z}
=1+\sum_{j\ge1}2^{j-1}z^j.
\]
Among exactly \(r\) binary digits there is one positive value for \(r=1\), and \(2^{r-2}\) positive values for every \(r\ge2\). Summing over \(r=1,\ldots,L\) proves exactly \(2^{L-1}\) positive values below \(2^L\). The zero count quoted in the theorem follows from the previously published four-state zero-language classification [4]; subtracting it and the positive count from the \(2^L-1\) positive integers gives the stated negative count.

**3. Two exact moments.** Put \(N=2^L\),
\[
U_L=\sum_{n=0}^{N-1}g(n),\quad S_L=\sum_{n=0}^{N-1}g(n)^2,\quad T_L=\sum_{n=0}^{N-1}g(n)g(n+1).
\]
We have \(U_1=S_1=T_1=1\). For \(L\ge1\), the boundary values \(g(1)=g(2)=g(N)=1\) imply
\[
\begin{aligned}
T_{L+1}&=g(1)g(2)+\sum_{m=1}^{N-1}g(m)(g(m)-g(m+1))
+\sum_{m=1}^{N-1}(g(m)-g(m+1))g(m+1)\\
&=1+\sum_{m=1}^{N-1}(g(m)^2-g(m+1)^2)=1.
\end{aligned}
\]
The even-index and odd-index parts of the first moment telescope:
\[
U_{L+1}=U_L+g(1)+\sum_{m=1}^{N-1}(g(m)-g(m+1))=U_L+1.
\]
Similarly, the odd-index square sum has its \(m=0\) term equal to \(1\), and
\[
\sum_{m=1}^{N-1}(g(m)-g(m+1))^2=2S_L-2T_L=2S_L-2.
\]
Hence \(S_{L+1}=3S_L-1\). The initial values give \(U_L=L\) and \(S_L=(3^{L-1}+1)/2\) for all \(L\ge1\), completing the proof.

## Verification

Run `python3 verify.py` in the extracted package. The program independently enumerates short signed binary strings for small values, checks their negative-digit parities against the recurrence, reconstructs all binary state transitions by integer pairs, checks exact sign census and moment identities over complete intervals through \(2^{16}\), and compares independent direct counts against the finite-state word construction. Finite checks corroborate, but do not establish, the statements for all lengths; the algebraic proof above does.

## Relationship to prior work

Anders, Dawsey, Gupta and Vandehey [1] identify the **total** number of short signed-binary representations with Stern's sequence. The parity distinction is not treated there. The integer sequence satisfying the signed recurrence predates this interpretation and appears as OEIS A145865 [2]; neither the recurrence nor its individual values are claimed as new. Monroe [3] analyzes **fixed-length** signed representations weighted by zeros using Stern polynomials, a different statistic and truncation. The existing zero-language theorem [4] proves precisely the balanced indices and their Fibonacci counts; its four states merge all nonzero ratios of unequal signs or magnitude and do not give sign frequencies or second moments. The present proof refines that partition to eight sign states and adds exact first and second moments, without claiming the known zero count independently.

## Limitations

The sign census is exact only at dyadic cutoffs; it does not assert equal counts at arbitrary cutoffs or equidistribution of magnitudes. It concerns short representations, not unrestricted or fixed-length signed-digit strings. Earlier work already gives the signed recurrence and its zero set, so novelty is restricted to the dyadic positive-sign census and joint exact energy/mean laws. A literature search cannot exclude an unindexed equivalent treatment; no independent audit is claimed.

## References

[1] K. Anders, M. L. Dawsey, R. Gupta, J. Vandehey, *Non-standard binary representations and the Stern sequence*, first public 2023-08-14, arXiv:2308.07448. https://arxiv.org/abs/2308.07448

[2] P. P. Lava and G. Balzarotti, OEIS A145865, signed Stern-type recurrence, first entered 2008-10-22. https://oeis.org/A145865

[3] L. Monroe, *Binary Signed-Digit Integers and the Stern Polynomial*, arXiv:2108.12417, 2021-08-27. https://arxiv.org/html/2108.12417v1

[4] *Fibonacci law for parity-balanced short signed-binary representations*, result dated 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-fibonacci-law-for-parity-balanced-short-signed-binary-representa--c38bf7959659
