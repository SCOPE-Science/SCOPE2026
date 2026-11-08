# Exact total-variation law for normalized two-block odd-partition coefficients

## Finding

Let \(a(n)\) be the signed count of partitions of \(n\ge1\) into exactly two distinct positive part sizes, each with odd multiplicity; a configuration \(n=(2u+1)x+(2v+1)y\) with \(1\le x<y\), \(u,v\ge0\), contributes \((-1)^{u+v}\). Set \(\sigma(n)=\sum_{d\mid n}d\) and \(R(n)=a(n)/\sigma(n)\).

Put
\[
r_0=\frac14,\qquad r_t=\frac{2^{t+1}-3}{4(2^{t+1}-1)}\quad(t\ge1),\qquad
\mu=\sum_{t=0}^{\infty}2^{-t-1}\delta_{r_t}.
\]
Thus \(\mu\) has mass \(1/2\) at \(1/4\), mass \(1/4\) at \(1/12\), and mass \(1/8\) at \(5/28\). All its atoms are distinct, although \(r_t\to1/4\) for \(t\to\infty\). For an integer \(N\ge1\), set
\[
\mu_N=\frac1N\sum_{n=1}^N\delta_{R(n)},\qquad
B(N)=\#\{n\in\{1,\ldots,N\}:n=x^2+y^2\text{ for }x,y\in\mathbb Z\}.
\]
Then **the exact finite-cutoff law** is
\[
\boxed{d_{\mathrm{TV}}(\mu_N,\mu)=\frac{B(N)}N\qquad(N\ge1),}
\]
where \(d_{\mathrm{TV}}(\nu_1,\nu_2)=\sup_{E}|\nu_1(E)-\nu_2(E)|\) over subsets \(E\) of the rational numbers (equivalently Borel sets in the reals). Specifically,
\[
R(n)\in\{r_t:t\ge0\}\quad\Longleftrightarrow\quad n\text{ is not a sum of two integer squares},
\]
and in this case \(R(n)=r_{\nu_2(n)}\). Therefore Landau's theorem gives the **sharp rate**
\[
d_{\mathrm{TV}}(\mu_N,\mu)\sim\frac{K}{\sqrt{\log N}},\qquad
K=\frac1{\sqrt2}\prod_{p\equiv3\pmod4}(1-p^{-2})^{-1/2}.
\]
No asymptotic error estimate for \(B(N)\) is asserted beyond what follows from the cited classical theorem.

## Assumptions and scope

All indices and cutoffs are positive integers. Define the nonprincipal character modulo \(4\) by \(\chi_4(d)=0\) for even \(d\), \(1\) for \(d\equiv1\pmod4\), and \(-1\) for \(d\equiv3\pmod4\). Set \(\lambda(n)=\sum_{d\mid n}\chi_4(d)\). The proof uses two previously established results: Merca's coefficient identity
\[
a(n)=\frac{\sigma(n)-\lambda(n)}4-\frac{\sigma(n/2)}2+\sigma(n/4),
\]
with \(\sigma(x)=0\) when \(x\) is not a positive integer, and the classical Landau--Ramanujan theorem \(B(N)\sim KN/\sqrt{\log N}\). The first identity is used for **every** positive integer, including \(1,2\). No independence of the signed count or the source identity is claimed.

## Proof

**1. Exact normalized formula and zero criterion.** Write uniquely \(n=2^t m\), where \(t\ge0\) and \(m\) is odd. Multiplicativity of \(\sigma\) and \(\lambda\) gives \(\sigma(n)=C_t\sigma(m)\), \(\lambda(n)=\lambda(m)\), with \(C_t=2^{t+1}-1\). Substituting in Merca's identity, including the cases \(t=0,1\), yields
\[
R(n)=r_t-\frac{\lambda(m)}{4C_t\sigma(m)}.
\tag{1}
\]
For \(t=0\), this says \(R(m)=1/4-\lambda(m)/(4\sigma(m))\). Since \(\lambda(p^e)=e+1\) for odd \(p\equiv1\pmod4\), \(\lambda(p^e)=1\) for odd \(p\equiv3\pmod4\) and even \(e\), and \(0\) for such \(p\) and odd \(e\), we have \(\lambda(n)\ge0\), and \(\lambda(n)=0\) precisely when at least one prime \(p\equiv3\pmod4\) occurs to odd exponent. By Fermat's two-square criterion, \(\lambda(n)>0\) precisely when \(n\) is a sum of two integer squares. Thus equation (1) implies \(R(n)=r_t\) if \(n\) is not such a sum.

**2. Rigidity: positive character sum never hits another atom.** First \(r_1=1/12\) and the sequence \((r_t)_{t\ge1}\) is strictly increasing, bounded above by \(r_0=1/4\). Suppose \(\lambda(m)>0\) and \(t\ge1\). Then equation (1) shows \(R(n)<r_t\), so a hypothetical equality \(R(n)=r_s\) requires \(1\le s<t\). Rearrangement of equation (1) gives
\[
\frac{\lambda(m)}{\sigma(m)}=2\left(\frac{C_t}{C_s}-1\right)>2,
\]
since \(C_t>2C_s\). This contradicts \(0<\lambda(m)\le\sigma(m)\).

It remains to exclude \(t=0\). If \(m\) is odd and \(\lambda(m)>0\), the local prime-power formulas above and \(\sigma(p^e)=1+p+\cdots+p^e\) give
\[
\nu_2(\lambda(p^e))=\nu_2(\sigma(p^e))
\]
for every prime power dividing \(m\): when \(p\equiv1\pmod4\), both valuations equal \(\nu_2(e+1)\) (because \(p\equiv1\pmod4\)); when \(p\equiv3\pmod4\), the relevant exponent is even and both factors are odd. Multiplying over all prime powers gives \(\nu_2(\lambda(m))=\nu_2(\sigma(m))\); hence the reduced fraction \(\lambda(m)/\sigma(m)\) has odd numerator and odd denominator. If \(R(m)=r_s\), then \(s\ge1\) and
\[
\frac{\lambda(m)}{\sigma(m)}=\frac2{C_s},
\]
whose reduced numerator is even because \(C_s\) is odd. Contradiction. Thus \(R(n)\) belongs to the countable atom set exactly when \(\lambda(n)=0\).

**3. Every empirical atom is dominated.** Let \(S=\{r_t:t\ge0\}\). For a fixed \(N\) and \(t\ge0\), the number \(D_t(N)\) of indices \(1\le n\le N\) with \(\nu_2(n)=t\) equals
\[
D_t(N)=\left\lfloor\frac N{2^t}\right\rfloor-\left\lfloor\frac N{2^{t+1}}\right\rfloor
<\frac N{2^{t+1}}+1.
\]
If \(2^t\le N\), the integer \(2^t\) itself is a sum of two squares (\(2^t=(2^{t/2})^2\) for even \(t\), or twice the square \((2^{(t-1)/2})^2\) for odd \(t\)); thus at least one of these \(D_t(N)\) indices has \(\lambda(n)>0\) and, by Step 2, its ratio is outside \(S\). Consequently
\[
\mu_N(\{r_t\})\le\frac{D_t(N)-1}{N}<2^{-t-1}=\mu(\{r_t\}).
\]
For \(2^t>N\), the left side is zero, so the weak inequality remains true. Every atom of \(\mu_N\) lying in \(S\) is therefore dominated by the corresponding atom of \(\mu\).

**4. Exact total variation.** The rigidity in Step 2 implies
\[
\mu_N(\mathbb Q\setminus S)=B(N)/N,\qquad \mu(\mathbb Q\setminus S)=0.
\]
By Step 3, \(\mu_N\) restricted to \(S\) is a submeasure of \(\mu\). The total positive mass of \(\mu_N-\mu\) is therefore exactly \(B(N)/N\), and the total negative mass has the same magnitude. Hence the supremum-event definition of total variation gives \(d_{\mathrm{TV}}(\mu_N,\mu)=B(N)/N\), with equality witnessed by \(\mathbb Q\setminus S\). Finally, the classical Landau--Ramanujan theorem supplies the stated sharp asymptotic. \(\square\)

## Verification

The supplied self-contained `verify.py` uses **exact integers and rational fractions**. It independently constructs the signed partition coefficients by truncating the defining product in a second formal marker for the number of distinct part sizes, separately computes \(\sigma(n)\) and \(\lambda(n)\) by divisor summation, and independently tests sums of two squares by searching integer square decompositions. It checks coefficient agreement, equation (1), non-coincidence with every limiting atom, and atomwise domination for cutoffs through \(N=256\). Run `python3 verify.py`; expected output includes `VERIFY_OK` and the exact cutoff example \(B(256)=97\) and \(d_{\mathrm{TV}}(\mu_{256},\mu)=97/256\). Finite checking is supportive only; Steps 1–4 prove the unrestricted statement.

## Relationship to prior work

Merca's first paper establishes the signed two-block function, its coefficient formula, positivity, and partition congruences; the second establishes a dyadic decomposition and further congruences. Their identities underpin Step 1 but the inspected full texts do not provide the **exact finite-cutoff total-variation distribution**, the **non-coincidence lemma**, or the exact relationship to sums-of-two-squares counting. The classical Landau theorem supplies the leading asymptotic constant but concerns the arithmetic counting function rather than partition-coefficient distributions. OEIS A400616 tabulates the sequence \(a(n)\), not the limiting measure. The new theorem links these ingredients through the separately proved parity rigidity and coordinatewise dominance argument; prior formulas themselves are credited, not presented as new.

## Limitations

The normalization by \(\sigma(n)\) is essential, and the empirical measure is over the complete initial interval of indices \(1\le n\le N\), with **no** claim for short intervals, random partitions, other normalizations, or other signed partition functions. The asymptotic estimate for \(B(N)\) is an established theorem used as an input. The source coefficient formula, its first-public date, and the classical arithmetic inputs are not new results. The argument proves exact finite-sample total variation but does not supply a new asymptotic expansion for \(B(N)\). Historical priority outside the inspected literature remains to be independently assessed.

## References

1. Mircea Merca, *The two-block odd partition function*, preprint arXiv:2609.33770 (first public September 27, 2026); *The Ramanujan Journal* 71 (2026), Article 23, DOI:10.1007/s11139-026-01426-1. Full open-access text: https://link.springer.com/article/10.1007/s11139-026-01426-1.
2. Mircea Merca, *Dyadic Structure of the Two-Block Odd Partition Function and Theta-Weighted Congruences for pod(n)*, arXiv:2610.05020 (October 4, 2026). Full text: https://arxiv.org/abs/2610.05020.
3. Bruce C. Berndt and Pieter Moree, *Sums of two squares and the tau-function: Ramanujan's trail*, arXiv:2409.03428 (2024); *Expositiones Mathematicae* 43 (2025), Article 125721. https://arxiv.org/abs/2409.03428.
4. OEIS A400616, signed two-block odd-partition coefficients and published arithmetic formula: https://oeis.org/A400616.
