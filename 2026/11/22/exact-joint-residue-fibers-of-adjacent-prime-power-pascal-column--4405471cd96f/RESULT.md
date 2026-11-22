# Exact joint residue fibers of adjacent prime-power Pascal columns modulo \(p^2\)

## Finding
Fix a prime \(p\) and an integer \(a\ge1\), and put
\[
A(n)=\binom{n}{p^a},\qquad B(n)=\binom{n}{p^{a+1}}\qquad(n\ge0).
\]
For integers \(0\le j<p\), let \(H_0=0\) and \(H_j=\sum_{i=1}^{j}i^{-1}\in\mathbb F_p\). Define \(h_p(c)=\#\{0\le j<p:H_j=c\}\) and \(S_p=\{H_j:0\le j<p\}\). All inverses in these definitions are in \(\mathbb F_p\).

The joint sequence \((A(n),B(n))\bmod p^2\) has **least period** \(N=p^{a+3}\). For each pair of residues \(u,v\in\{0,\ldots,p^2-1\}\), write uniquely \(u=u_0+pu_1\), \(v=v_0+pv_1\), with \(0\le u_i,v_i<p\). Its complete fiber count per least period is
\[
\boxed{
C_{p,a}(u,v):=\#\{0\le n<N:A(n)\equiv u,\ B(n)\equiv v\pmod{p^2}\}
=p^{a-1}
\begin{cases}
p,&u_0=0,\ u_1=v_0,\\
0,&u_0=0,\ u_1\ne v_0,\\
h_p((u_1-v_0)u_0^{-1}),&u_0\ne0.
\end{cases}}
\]
The number of represented ordered pairs is exactly
\[
\boxed{p^2\bigl(1+(p-1)|S_p|\bigr)}.
\]
Every represented pair occurs infinitely often. Both individual residue sequences are *uniform* modulo \(p^2\): each of the \(p^2\) values occurs exactly \(p^{a+1}\) times in one least joint period. In particular, they are never jointly uniform. For every odd prime, symmetry \(H_{p-1-j}=H_j\) gives \(|S_p|\le(p+1)/2\), so at most \(p^2(p^2+1)/2\) of the \(p^4\) pairs can appear. At \(p=2\), exactly 12 of 16 pairs occur.

For illustration, \(|S_3|=2\), \(|S_5|=3\), \(|S_7|=4\), \(|S_{11}|=4\); consequently the supported-pair counts are respectively 45 of 81, 325 of 625, 1225 of 2401, and 4961 of 14641. The exact count is independent of \(a\), though each nonzero fiber multiplicity scales as \(p^{a-1}\).

## Assumptions and scope
All primes \(p\), all integers \(a\ge1\), and all \(n\ge0\) are covered. As usual, \(\binom{n}{k}=0\) for \(0\le n<k\). Residues \(u,v\) are represented by their canonical integers between zero and \(p^2-1\); their base-\(p\) digits are uniquely defined. This is a **joint** residue distribution over the *index* \(n\), not a count of all coefficients within a fixed row of Pascal's triangle. We do not claim a uniform closed form in \(p\) for \(|S_p|\), which is evaluated directly from the canonical \(p\) finite harmonic sums.

## Proof
**Step 1 (the one-column congruence).** For \(h=p^a\), every integer \(x\ge0\) and every \(0\le r<h\) satisfy
\[
\boxed{\binom{hx+r}{h}\equiv x\left(1+pH_{\lfloor r/p^{a-1}\rfloor}\right)\pmod{p^2}.}\tag{1}
\]
First, \(\binom{hx}{h}\equiv x\pmod{p^2}\) follows by induction on \(x\). Indeed, Vandermonde's identity gives
\[
\binom{h(x+1)}h-\binom{hx}h
=1+\sum_{i=1}^{h-1}\binom hi\binom{hx}{h-i}
\equiv1\pmod{p^2}.
\]
The first factor in each summand is divisible by \(p\), and so is the second, by Lucas's theorem: \(hx\) ends in \(a\) zero digits in base \(p\), whereas \(0<h-i<h\). When \(x=0\), (1) is immediate. For \(x\ge1\), the exact rational identity
\[
\frac{\binom{hx+r}{h}}{\binom{hx}{h}}
=\prod_{i=1}^r\frac{hx+i}{h(x-1)+i}
=\prod_{i=1}^r\left(1+\frac{h}{h(x-1)+i}\right)
\]
holds inside \(\mathbb Q_p\). Since \(0<i<h\), the denominator in the last factor has valuation \(\nu_p(i)\). Factors with \(\nu_p(i)\le a-2\) are 1 modulo \(p^2\); for \(i=p^{a-1}t\) with \(1\le t\le p-1\), a factor equals \(1+pt^{-1}\pmod{p^2}\). There are precisely \(\lfloor r/p^{a-1}\rfloor\) such factors. Their product is \(1+pH_{\lfloor r/p^{a-1}\rfloor}\pmod{p^2}\), proving (1), including \(p=2\) and \(a=1\).

**Step 2 (three high index digits).** Let \(N=p^{a+3}\). Every \(n\in[0,N)\) is uniquely expressible as
\[
n=r+p^a(x_0+px_1+p^2x_2),\qquad 0\le r<p^a,\quad 0\le x_0,x_1,x_2<p.
\]
Set \(j=\lfloor r/p^{a-1}\rfloor\). Applying (1) first with \(h=p^a\), and then with \(h=p^{a+1}\), gives the exact pair of congruences
\[
\boxed{A(n)\equiv x_0+p(x_1+x_0H_j),\qquad
B(n)\equiv x_1+p(x_2+x_1H_{x_0})\pmod{p^2}.}\tag{2}
\]
The second formula uses the residue \(p^ax_0+r<p^{a+1}\), whose top base-\(p\) digit is \(x_0\). Thus all omitted lower \(a-1\) digits of \(r\) are genuinely free.

**Step 3 (exact fiber calculation).** Matching the two low output digits in (2) forces \(x_0=u_0\) and \(x_1=v_0\). Matching the high digit of \(A\) imposes \(u_1=v_0+u_0H_j\). If \(u_0=0\), this is either always true (exactly \(p\) choices of \(j\)) or impossible. If \(u_0\ne0\), it holds for precisely \(h_p((u_1-v_0)u_0^{-1})\) choices of \(j\). In every case where it holds, the high digit of \(B\) uniquely determines \(x_2\) from \(v_1=x_2+v_0H_{u_0}\). Each \(j\) has \(p^{a-1}\) possible values of \(r\). Multiplying gives exactly the displayed fiber formula, without probabilistic approximation.

**Step 4 (sharp period).** Formula (1) shows that \(\binom{n}{p^b}\pmod{p^2}\) has period dividing \(p^{b+2}\), because translating \(n\) by that amount adds \(p^2\) to its quotient \(\lfloor n/p^b\rfloor\). Consequently the pair has period dividing \(N=p^{a+3}\). The smaller power \(N/p=p^{a+2}\) cannot be a period even for \(B\), since (1) with \(h=p^{a+1}\), \(x=p\), \(r=0\) gives
\[
B(N/p)=\binom{p^{a+2}}{p^{a+1}}\equiv p\not\equiv0=B(0)\pmod{p^2}.
\]
Since the least period must divide the exhibited prime-power period, \(N\) is the least.

**Step 5 (support, marginals, and exclusion).** For \(u_0=0\), choosing \(u_1=v_0\) and allowing \(u_1,v_1\) to vary gives \(p^2\) supported pairs. For each \(u_0\ne0\) and \(v_0\), every distinct \(H_j\in S_p\) determines a distinct \(u_1\), while \(v_1\) remains arbitrary. This gives another \((p-1)p^2|S_p|\) pairs. Summing the formula over \(v\) for fixed \(u\) yields \(p^{a+1}\); alternatively, in (2), prescribing either output fixes precisely two of the three high digits, with the remaining free \(p\)-digit and the \(p^a\) possible values of \(r\), giving \(p^{a+1}\) indices per residue. Periodicity proves infinite repetition of every supported pair.

For odd \(p\), pairing inverse terms in \(\sum_{i=1}^{p-1}i^{-1}\) yields \(H_{p-1}=0\). Reindexing the last \(j\) terms gives \(H_{p-1-j}=H_j\), so at most \((p+1)/2\) distinct harmonic residues appear. When \(p=2\), \(H_0=0\) and \(H_1=1\). This proves all assertions.

## Verification
The included executable `verify.py` performs exact-integer binomial calculations, independently of the factorization proof, for every index of the joint least period in nine cases: \((p,a)=(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2),(7,1),(11,1)\). It checks both congruences (1) and (2), every one of the \(p^4\) pair-count cells, both marginal counts, total mass, and example supported-pair counts. Run `python3 verify.py`; the output ends `ALL EXACT CHECKS PASSED`. All comparisons use exact integer arithmetic, with no floating-point approximations. The finite tests are not a substitute for the proof above for arbitrary prime and exponent.

## Relationship to prior work
Fiorot, Gilblas and Tonolo study modular binomial columns as repeated primitives of constant sequences and prove their individual prime-power period formulas (arXiv:2307.02366, Proposition 3.4). That framework supplies the natural motivation to examine two consecutive prime-power primitive levels simultaneously, but the inspected statements do not evaluate their joint residue fibers. Rowland's *Lucas' theorem modulo \(p^2\)* (arXiv:2006.11701, Theorem 4) gives the known single-digit harmonic correction underlying such congruences. Formula (1) is an elementary specialization/iteration of this established local theory, **not** the originality claim. Sun and Zhang (arXiv:0812.3089, Theorem 1.1) establish individual residue-surjectivity for fixed columns \(p^a\); this does not imply the pair occupies the full product. A published theorem on prime-power Pascal-column valuation densities concerns one-coordinate valuations, not the exact two-coordinate residue spectrum. Webb and Huard–Spearman–Williams study the different problem of varying the lower index across one fixed Pascal row. The contribution claimed here is the **complete evaluated joint fiber law**, including its half-support obstruction and individual-versus-joint uniformity contrast.

## Limitations
The theorem is specific to adjacent indices \(p^a,p^{a+1}\) and modulus \(p^2\); it makes no claim about higher output moduli or arbitrary pairs of lower indices. The finite harmonic image \(S_p\) need not have a uniform closed cardinality formula as a function of \(p\); the theorem nevertheless computes every frequency from exactly \(p\) explicit field operations. The literature comparison establishes no guarantee against unindexed equivalent computations. Independent mathematical audit has not been performed.

## References
- L. Fiorot, R. Gilblas and A. Tonolo, *Modular binomials with an application to periodic sequences*, arXiv:2307.02366, first public 2023-07-05. https://arxiv.org/abs/2307.02366 .
- E. Rowland, *Lucas' theorem modulo \(p^2\)*, arXiv:2006.11701, first public 2020-06-21, *American Mathematical Monthly* 129 (2022), 846–855. https://arxiv.org/html/2006.11701v3 .
- Z.-W. Sun and W. Zhang, *Binomial coefficients and the ring of p-adic integers*, arXiv:0812.3089, first public 2008-12-16, *Proceedings of the American Mathematical Society* 139 (2011), 1569–1577. https://arxiv.org/html/0812.3089v5 .
- W. A. Webb, *The number of binomial coefficients in residue classes modulo p and p²*, *Colloquium Mathematicum* 60/61 (1990), 275–280, DOI 10.4064/cm-60-61-1-275-280.
- J. G. Huard, B. K. Spearman and K. S. Williams, *On Pascal's triangle modulo p²*, *Colloquium Mathematicum* 74 (1997), 157–165, DOI 10.4064/cm-74-1-157-165.
