# Exact dyadic residue fibers for every Mersenne-index Pascal column

## Finding
For every integer \(s\ge1\), set \(r=2^s-1\) and \(F_s(n)=\binom{n}{r}\) for all \(n\ge0\), with \(\binom{n}{r}=0\) when \(n<r\). For every integer \(k\ge1\), the **least positive period** of \(F_s(n)\bmod 2^k\) is exactly
\[
P_{s,k}=2^{s+k-1}.
\]
For any integer residue representative \(0\le y<2^k\), the exact multiplicity of \(y\) in a least period is
\[
H_{s,k}(y)=\mathbf1_{2\nmid y}+\sum_{j=1}^s 2^{j+\min(j,k)-2}\,\mathbf1_{2^{\min(j,k)}\mid y}.
\]
In particular, every residue modulo every power of two is attained. When \(k\ge s\), this formula reduces to
\[
H_{s,k}(y)=\begin{cases}1,&y\text{ odd},\\ (4^{\min(s,\nu_2(y))}-1)/3,&y\text{ even},\end{cases}
\]
where \(\nu_2(0)=\infty\). Thus, across the growing family, the even residue fiber levels are \(1,5,21,85,\ldots\), according to the capped dyadic valuation; odd residues have one preimage per least period. For example the seventh Pascal column, \(\binom n7\), has \(1\), \(5\), and \(21\) preimages at output valuations \(0\) or \(1\), \(2\), and at least \(3\), respectively, modulo \(2^k\) for every \(k\ge3\).

Equivalently, the pushforward of normalized Haar measure on \(\mathbb Z_2\) under \(x\mapsto \binom{x}{2^s-1}\) is absolutely continuous with density
\[
w_s(y)=2^{1-s}\mathbf1_{y\in1+2\mathbb Z_2}+\sum_{j=1}^s2^{2j-1-s}\mathbf1_{y\in2^j\mathbb Z_2}.
\]
This formula explicitly describes both the image and every output mass, not merely the valuation distribution.

## Assumptions and scope
All integers \(s,k\) are positive and all sequence indices are nonnegative. The map \(\binom{x}{r}=x(x-1)\cdots(x-r+1)/r!\) is interpreted as the canonical continuous integer-valued polynomial on \(\mathbb Z_2\). The valuation \(\nu_2\) has \(\nu_2(0)=\infty\). Residue multiplicities count individual indices in \(0\le n<P_{s,k}\), not binomial entries with both upper and lower indices varying. The Haar-density statement is about the same fixed lower index \(r\).

## Proof
**1. The scaled isometry lemma.** If \(q(t)\in\mathbb Z_2[t]\), the polynomial \(T(t)=t+2q(t)\) is an isometry of \(\mathbb Z_2\) whenever \(q(t)-q(u)\) is divisible by \(t-u\); indeed \((T(t)-T(u))/(t-u)\in1+2\mathbb Z_2\). Every polynomial \(q\) has this divisibility. Since \(T\) is a bijection modulo \(2\) and is isometric, each residue modulo \(2^a\) has a unique lift to each succeeding modulus, so \(T\) is surjective and bijective. Multiplication by any odd \(2\)-adic unit preserves this isometry property. More generally, any polynomial of the form \(tU(t)\) with \(U\in1+2\mathbb Z_2[t]\) is a bijective isometry, since \(tU(t)-uU(u)\) divided by \(t-u\) is odd. Consequently its reduction permutes every \(\mathbb Z/2^a\mathbb Z\).

**2. The \(2^s\) input branches.** Put \(m=2^s\) and \(r=m-1\). For \(0\le a<r\), factoring the root \(x=a\) of \(\binom{x}{r}\) gives the exact identity
\[
\binom{a+mt}{r}=\frac{(-1)^{r-1-a}mt}{r\binom{r-1}{a}}\prod_{\substack{0\le h<r\\h\ne a}}\left(1+\frac{mt}{a-h}\right).
\]
Every factor in the product lies in \(1+2\mathbb Z_2[t]\), since \(0<|a-h|<m\). The entire product has that form. Lucas's parity congruence says every \(\binom r a\) is odd (the binary digits of \(r\) are all one). From
\[
\binom{r-1}{a}=\frac{r-a}{r}\binom ra
\]
and \(r-a=m-(a+1)\) we obtain
\[
\nu_2\!\left(\binom{r-1}{a}\right)=\nu_2(a+1),\qquad 0\le a<r.
\]
Therefore the restriction of \(F_s\) to \(a+m\mathbb Z_2\) is, up to an odd unit, \(2^{c(a)}\) times an isometric bijection on \(\mathbb Z_2\), where
\[
c(a)=s-\nu_2(a+1)\in\{1,\ldots,s\}.
\]
The value \(c(a)=j\) occurs for exactly \(2^{j-1}\) of the \(r\) branches, because the integers \(a+1\) range through \(1,\ldots,2^s-1\).

For the remaining branch \(a=r\), write
\[
\binom{r+mt}{r}=\prod_{h=1}^r\left(1+\frac{mt}{h}\right).
\]
The unique factor with coefficient of valuation one is \(h=2^{s-1}\), giving \(1+2t\); all the other factors lie in \(1+4\mathbb Z_2[t]\). Hence the product has the form \(1+2(t+2Q(t))\) for a polynomial \(Q\in\mathbb Z_2[t]\), and maps this branch bijectively, with valuation scaling one, onto \(1+2\mathbb Z_2\).

**3. Least period.** On each branch \(a+m\mathbb Z_2\), the polynomial is a translated scaled isometry with output-difference valuation
\[
\nu_2(F_s(a+mt)-F_s(a+mu))=c(a)+\nu_2(t-u),
\]
with \(c(r)=1\), for all unequal \(t,u\in\mathbb Z_2\). Thus shifting every index by \(m2^{k-1}=2^{s+k-1}\) preserves all values modulo \(2^k\). For \(k\ge2\), the half-shift \(2^{s+k-2}\) fails at index \(n=r\), because its value difference has valuation exactly \(k-1\). Since any smaller positive period would divide the known power-of-two period, no smaller one exists. At \(k=1\), Lucas's congruence gives \(\binom{n}{r}\equiv1\pmod2\) precisely when \(n\equiv r\pmod{2^s}\); the least period is \(2^s\). These arguments prove the period claim in all cases.

**4. Exact fibers.** In a least period, for every branch \(a\bmod m\), the branch parameter \(t\) visits precisely the integers \(0\le t<2^{k-1}\). The exceptional branch \(a=r\) maps bijectively to the odd residues modulo \(2^k\), contributing one to each such fiber. For any branch of scale \(2^j\), a residue \(y\pmod{2^k}\) has exactly \(2^{\min(j,k)-1}\) input preimages when \(2^{\min(j,k)}\mid y\), and none otherwise. Multiplying by the \(2^{j-1}\) branches of scale \(2^j\), and summing over \(1\le j\le s\), proves the asserted formula. Scale \(j=1\) already hits every even residue, and the exceptional branch hits every odd residue. For \(k\ge s\), the geometric sum \(\sum_{j=1}^{v}4^{j-1}=(4^v-1)/3\) gives the simplified formula.

**5. Haar law.** Each input coset has normalized measure \(2^{-s}\). A scale-\(2^j\) bijective isometry sends conditional normalized Haar measure to normalized Haar measure on \(2^j\mathbb Z_2\), with density \(2^j\) relative to Haar measure on \(\mathbb Z_2\); its \(2^{j-1}\) branches therefore contribute \(2^{2j-1-s}\mathbf1_{2^j\mathbb Z_2}\). The final branch maps to odd numbers and contributes \(2^{1-s}\mathbf1_{1+2\mathbb Z_2}\). This establishes the exact pushforward density. The finite-level residue law also follows by integrating over residue balls.

## Verification
The embedded program `verify.py` checks the exact residue histogram for \(1\le s\le6\) and \(1\le k\le8\) by integer binomial evaluation; it separately verifies the claimed failure of the half-period for \(k\ge2\), the characteristic parity case at \(k=1\), and branch isometry valuations on a sample grid. The proof above, not these finite checks, establishes all positive \(s,k\).

## Relationship to prior work
Lane (2023) studies distributions in complete rows and aggregations over rows modulo a prime; its statistics vary the lower binomial index, unlike the fixed Mersenne column and all prime-power residues here. Barat and Grabner (2001) analyze asymptotic distributions over both binomial indices and the prime-free parts, not these exact fixed-column fibers and least periods. A publicly indexed result for the third Pascal column gives the instance \(s=2\) of the present law; the current result includes that known special case and extends the hierarchy to **every** Mersenne lower index \(2^s-1\), notably \(7,15,31,\ldots\). A separate fifth-column distribution does not imply the present family because \(5\) is not of this form. The general result's priority is not independently certified; an implicit treatment in general binomial-congruence literature remains possible.

## Limitations
The theorem concerns only fixed columns with lower index \(2^s-1\), not every fixed lower index, other primes, or joint residue distributions. Its residue law is exact over each least period; no non-periodic discrepancy estimate is asserted. No independent external mathematical audit is claimed.

## References
- Connor Lane, *Asymptotic Distribution of Residues in Pascal's Triangle mod p* (first public version 22 September 2023), https://arxiv.org/abs/2309.12942.
- Guy Barat and Peter J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, Journal of the London Mathematical Society **64** (2001), 523–547, https://doi.org/10.1112/S0024610701002630. Lawful author manuscript: https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf.
- *Exact dyadic residue frequencies of the cubic binomial column* (public online mathematical note, 2026): a known special-case comparison for lower index three.
- É. Lucas, classical binomial coefficient congruence modulo a prime (1878).
