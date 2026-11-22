# The exact prefix-normal-cut spectrum of binary necklaces with four ones

## Finding

A finite binary word is *ones-prefix normal* if, at each positive length, its prefix has at least as many ones as every **contiguous non-wrapping factor of that word** of the same length. A *prefix-normal cut* of an oriented binary necklace is a starting position whose length-preserving linearization is ones-prefix normal. Cuts are counted as physical positions even for a periodic necklace; only necklaces, not cuts, are quotiented by rotation.

For every integer \(n\ge4\), let \(N_j(n)\) be the number of binary necklaces of length \(n\), with exactly four ones, having precisely \(j\) prefix-normal cuts. Every such necklace has between one and four cuts. Their complete ordinary generating-function spectrum is

\[
\begin{aligned}
N_1(z)&=\sum_{n\ge4}N_1(n)z^n=\frac{z^8}{(1-z)^4(1+z^2)(1+z+z^2)},\\
N_3(z)&=\frac{z^5}{(1-z)(1-z^4)},\\
N_4(z)&=\frac{z^4}{1-z^4},\\
N_2(z)&=\frac{z^4}{4}\left(\frac1{(1-z)^4}+\frac1{(1-z^2)^2}+\frac2{1-z^4}\right)-N_1(z)-N_3(z)-N_4(z).
\end{aligned}
\]

In particular, when a binary necklace with four ones is chosen uniformly among all such necklaces of length \(n\), its number of prefix-normal cuts converges in distribution to one with probability \(2/3\) and two with probability \(1/3\):
\[
N_1(n)=\frac{n^3}{36}+O(n^2),\quad
N_2(n)=\frac{n^3}{72}+O(n^2),\quad
N_3(n)=O(n),\quad
N_4(n)=\mathbf1_{4\mid n}.
\]

This is a classification of *linear* prefix normality of circular cuts, not the stronger demand that a prefix dominate factors wrapping across the cut or factors of the infinite periodic extension.

## Assumptions and scope

The alphabet is \(\{0,1\}\), all necklaces are oriented (reversal and complementation are not identified), \(n\ge4\), and Hamming weight is precisely four. Number positions cyclically and write the four zeros-after-a-one gaps as \((a,b,c,d)\), with nonnegative entries summing to \(n-4\). A representative is \(1 0^a1 0^b1 0^c1 0^d\). Its necklace corresponds bijectively to this four-tuple modulo cyclic permutation of the four gap coordinates. Distinct occurrences of a one are different cuts, even if repeated structure makes their linearizations identical.

## Proof

**Step 1: a complete local cut criterion.** A binary word containing a one cannot have a prefix-normal cut starting with zero, because a one occurs in a length-one factor. Consider the linearization starting at the one before gap \(a\):
\[
v=1 0^a1 0^b1 0^c1 0^d.
\]
The minimal lengths of factors containing \(k=1,2,3,4\) ones are obtained by taking shortest spans of \(k\) consecutive ones. For this linear word these four thresholds are respectively
\[
1,\quad 2+\min(a,b,c),\quad 3+\min(a+b,b+c),\quad 4+a+b+c.
\]
The thresholds at which the prefixes first contain \(k\) ones are
\[
1,\quad 2+a,\quad 3+a+b,\quad 4+a+b+c.
\]
The prefix-one profile dominates all factors at every length exactly when the corresponding thresholds coincide for every \(k\). For \(k=2\) that means \(a\le b\) and \(a\le c\). For \(k=3\) it means \(a+b\le b+c\), equivalent to \(a\le c\), and the other thresholds impose nothing. Thus the cut before gap \(a\) is prefix normal exactly when
\[
\boxed{a\le b\ \text{and}\ a\le c.}
\]
Rotating indices gives the exact number of cuts
\[
R(a,b,c,d)=\sum_{i=0}^3\mathbf1_{\{g_i\le g_{i+1},\ g_i\le g_{i+2}\}},\quad (g_0,g_1,g_2,g_3)=(a,b,c,d),
\]
where gap subscripts are taken modulo four. At least one index achieves the global minimum gap, so \(1\le R\le4\), regardless of zero gaps and periodicity.

**Step 2: finite weak-order decomposition.** To derive exact generating functions without guessing coefficients, classify all ordered four-gap tuples by the weak ordering of their entries. If there are \(k\) distinct values, encode the tuple by a surjection \(h:\{0,1,2,3\}\to\{0,\ldots,k-1\}\) listing rank values in increasing order. For each surjection let \(r(h)=\sum_i\mathbf1_{\{h_i\le h_{i+1},\ h_i\le h_{i+2}\}}\) and let \(b_j=|\{i:h_i\ge j\}|\) for \(1\le j<k\). The distinct gap values can uniquely be written as \(t_0\ge0\) and \(t_j=t_{j-1}+1+e_j\) with \(e_j\ge0\). Thus the contribution of this weak-order class to the size-of-zero-gaps enumerator is
\[
\frac{z^{\sum_{j=1}^{k-1}b_j}}{(1-z^4)\prod_{j=1}^{k-1}(1-z^{b_j})}.
\]
All factors in the denominator are distinct members of \(\{1-z,1-z^2,1-z^3,1-z^4\}\). The total number of surjective rank patterns is \(1+14+36+24=75\). Summing them by cut count \(r(h)\) yields, with \(D(z)=(1-z)(1-z^2)(1-z^3)(1-z^4)\),
\[
\begin{array}{c|c|l}
\text{cuts }j&\text{weak-order classes}&D(z)S_j(z)\\\hline
1&28&4z^4(1+z)^2\\
2&42&2z^2(1+z)(3+2z-3z^3)\\
3&4&4z(1-z)^2(1+z)(1+z+z^2)\\
4&1&(1-z)^3(1+z)(1+z+z^2).
\end{array}
\]
Here \(S_j(z)=\sum_{a,b,c,d\ge0,\ R(a,b,c,d)=j}z^{a+b+c+d}\). The four polynomial identities follow by the complete 75-class finite partition; `verify.py` independently constructs all surjections and multiplies the denominators into exact integer polynomials. These are finite symbolic identities, not a fit to initial coefficients.

**Step 3: quotient by cyclic permutation.** Burnside's lemma for the cyclic group of order four gives the necklace enumerators. Its identity rotation fixes all tuples and contributes \(S_j(z)\). The half-turn fixes precisely \((a,b,a,b)\), which has \(R=4\) if \(a=b\) and \(R=2\) otherwise. The two quarter-turns each fix only the all-equal tuples, all with four cuts. Thus
\[
\begin{aligned}
N_1(z)&=\frac{z^4}{4}S_1(z),\\
N_2(z)&=\frac{z^4}{4}\left(S_2(z)+\frac{2z^2}{(1-z^2)(1-z^4)}\right),\\
N_3(z)&=\frac{z^4}{4}S_3(z),\\
N_4(z)&=\frac{z^4}{4}\left(S_4(z)+\frac3{1-z^4}\right).
\end{aligned}
\]
For the half-turn with two cuts, \(a\ne b\); its enumerator is \(2z/((1-z)(1-z^2))\) in gap-sum variable, which is **equivalent to** \(2z^2/((1-z^2)(1-z^4))\) after accounting for repetition twice. Explicitly, \(\sum_{a\ne b}z^{2(a+b)}=1/(1-z^2)^2-1/(1-z^4)=2z^2/((1-z^2)(1-z^4))\). The displayed formulas are the corresponding Burnside contributions.

Substitution of the table and cancellation proves the four claimed generating functions; for \(N_2\) one may alternatively subtract the other three from the ordinary four-bead necklace series. The latter is \(z^4[1/(1-z)^4+1/(1-z^2)^2+2/(1-z^4)]/4\), by Burnside independently of cut counts.

**Step 4: asymptotics.** The total generating function has a pole of order four at \(z=1\), with leading coefficient \(1/4\); hence its coefficient grows as \(n^3/24+O(n^2)\). The pole of \(N_1(z)\) at \(z=1\) has coefficient \(1/6\) at order four, giving \(n^3/36+O(n^2)\). The functions \(N_3\) and \(N_4\) have respectively at most linear and bounded coefficients. Subtraction gives \(N_2(n)=n^3/72+O(n^2)\). Dividing by the total proves the limiting proportions.

## Verification

Execute `python3 verify.py` with Python 3 standard library, no external packages. It enumerates **all 75 surjective rank patterns**, constructs exact numerator polynomials using polynomial arithmetic (not numerical fitting), and checks each table entry against the displayed polynomial. Separately, for every four-one binary necklace of lengths \(4\) through \(20\), it directly evaluates the full prefix-versus-factor definition at every one-root position and checks the resulting cut count against both the local gap criterion and every coefficient of the rational Burnside enumerators. The checked length-\(20\) histogram is \((N_1,N_2,N_3,N_4)=(111,129,4,1)\). These finite enumerations corroborate the all-length proof and include all periodic boundary cases.

## Relationship to prior work

The classical prefix-normal formalism and the fixed-density gap inequalities originate with Fici and Lipták and Burcsi et al. [1–3]. In particular, the known enumeration of **linear** prefix-normal words with four ones is not new, and the shortest-span criterion is not new. The contribution here is the complete **number-of-valid-rotations distribution for each four-one necklace**, the all-length closed rational functions for all four multiplicities, and its limiting two-class law.

The published sharp first cyclic prefix-normal-cut obstruction [4] establishes that all circles of length at most ten have a valid **linear** cut and identifies the first obstructions at length eleven; it neither classifies the number of valid cuts nor supplies the four-one spectrum. The published three-one *circular-prefix-maximal* classification [5] compares against windows wrapping across the cut, a strictly different requirement, and therefore has different obstructions. The published four-**run** periodic prefix-normal theorem [6] concerns two one-runs of arbitrary length and infinite periodic factors, not fixed weight four and finite linear factors. The published four-one prefix-normal *fiber-size* theorem [7] groups indexed linear words by their maximum-factor profiles, not necklaces by their numbers of valid cuts. None of these source statements implies the present distribution without a new classification of the cyclic gap orderings. An earlier unindexed equivalent result remains possible; priority is not independently certified.

## Limitations

The exact rational spectrum concerns precisely four ones, finite nonwrapping factors after each cut, binary alphabet and oriented necklaces. It does not classify full jumbled-factor profiles of necklaces, allow reversal, or handle arbitrary Hamming weights. The global-gap criterion itself is a small instance of established prefix-normal methodology; it is the new rotation multiplicity distribution that is evaluated. Verification through length twenty is exhaustive only within that finite interval; the unbounded result relies on the symbolic class decomposition and Burnside proof. Independent mathematical validation has not been performed.

## References

[1] G. Fici and Z. Lipták, *On Prefix Normal Words*, Developments in Language Theory (2011), DOI https://doi.org/10.1007/978-3-642-22321-1_20 ; later open manuscript https://arxiv.org/abs/1805.12405 .

[2] P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Combinatorial Generation of Prefix Normal Words*, first posted 2014-01-24, https://arxiv.org/abs/1401.6346 .

[3] P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *Normal, Abby Normal, Prefix Normal*, first posted 2014-04-01, https://arxiv.org/abs/1404.2824 ; and *On Prefix Normal Words and Prefix Normal Forms*, first posted 2016-11-28, https://arxiv.org/abs/1611.09017 .

[4] *The sharp cyclic prefix-normal representative obstruction*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-sharp-cyclic-prefix-normal-representative-obstruction--0cf8390c81fd .

[5] *First circular prefix-normal obstructions and the complete three-one classification*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-first-circular-prefix-normal-obstructions-and-the-complete-three--3cb64ddcad03 .

[6] *Prefix-normal rotations of four-run binary cycles*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-prefix-normal-rotations-of-four-run-binary-cycles-a-sharp-run-or--3c39b60ef425 .

[7] *Exact fiber-size spectrum of four-one binary prefix-normal profiles*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-fiber-size-spectrum-of-four-one-binary-prefix-normal-profi--b6fb9e08f331 .
