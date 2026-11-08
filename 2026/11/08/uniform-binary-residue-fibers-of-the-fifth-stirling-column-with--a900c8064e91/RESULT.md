# Uniform binary residue fibers of the fifth Stirling column with sharp preperiod

## Finding
Let \(S(n,j)\) be the Stirling number of the second kind. For every integer \(k\ge1\), put \(P_k=2^{k+1}\) and \(N_k=\max\{5,k+2\}\). For **every** integer \(a\ge N_k\) and every residue \(y\in\mathbb Z/2^k\mathbb Z\), exactly two integers \(n\) in the block \(a\le n<a+P_k\) satisfy
\[
S(n,5)\equiv y\pmod{2^k}.
\]
Exactly one such \(n\) is even and exactly one is odd. Thus the fifth Stirling column is eventually uniformly distributed modulo every power of two, with exact density \(2^{-k}\) for each residue. The least eventual period is \(P_k\). Moreover, relative to the natural domain \(n\ge5\), \(N_k\) is the **least** starting index from which this period holds.

A stronger structural statement underlies the result: for each \(r\in\{0,1\}\), the 2-adic function
\[
G_r(t)=\frac{5^r25^t+10\cdot3^r9^t+5}{120},\qquad t\in\mathbb Z_2,
\]
is a well-defined isometric bijection of \(\mathbb Z_2\). For all integers \(n\ge5\), setting \(r=n\bmod2\), one has the **exact** identity
\[
S(n,5)=G_r((n-r)/2)-\frac{2^{2n-3}+2^{n-2}}3,
\]
whose correction has 2-adic valuation \(n-2\).

## Assumptions and scope
Indices \(n\) and precisions \(k\) are integers; \(n\ge5\) and \(k\ge1\). The numbers \(S(n,5)\) count partitions of an \(n\)-element set into five nonempty blocks. Powers of odd numbers of the form \(1+8u\), exponentiated by \(t\in\mathbb Z_2\), are defined as the continuous extensions of integer exponentiation, equivalently by convergent binomial expansion. All congruences refer to ordinary integer Stirling numbers, while the interpolation statements refer to \(\mathbb Z_2\).

## Proof
**1. Exact decomposition.** Inclusion-exclusion gives, for all integers \(n\ge5\),
\[
120S(n,5)=5^n-5\cdot4^n+10\cdot3^n-10\cdot2^n+5.
\]
For parity \(r\in\{0,1\}\), write \(n=r+2t\). Separating the two even bases from the three odd terms gives
\[
S(n,5)=G_r(t)-\frac{2^{2n-3}+2^{n-2}}3.
\]
For \(n\ge5\), the summands inside the displayed numerator have distinct valuations \(2n-3\) and \(n-2\); hence the correction has valuation exactly \(n-2\). The numerator defining \(G_r\) is divisible by eight in \(\mathbb Z_2\), because \(25^t\equiv9^t\equiv1\pmod8\), and both choices of \(r\) give numerator divisible by eight. Since \(120=8\cdot15\) with 15 odd, \(G_r\) is 2-adic integer-valued.

**2. Isometry.** Let \(s,t\in\mathbb Z_2\), \(s\ne t\), and set \(h=t-s\). The standard lifting identity for \(a\in1+8\mathbb Z_2\) with \(\nu_2(a-1)=3\) is
\[
\nu_2(a^h-1)=3+\nu_2(h).
\]
This holds for nonzero \(h\in\mathbb Z_2\) by the binomial expansion or continuity from integer exponents. Since \(\nu_2(25-1)=\nu_2(9-1)=3\),
\[
\begin{aligned}
120(G_r(t)-G_r(s))
={}&5^r25^s(25^h-1)\\
&+10\cdot3^r9^s(9^h-1).
\end{aligned}
\]
The first term has valuation \(3+\nu_2(h)\) and the second valuation \(4+\nu_2(h)\). They cannot cancel, so
\[
\nu_2(G_r(t)-G_r(s))=\nu_2(t-s).
\]
Thus \(G_r\) induces an injection on \(\mathbb Z/2^k\mathbb Z\) for every \(k\); because this set is finite, it is a permutation for every \(k\). Compactness and completeness give a bijection of \(\mathbb Z_2\).

**3. Exact fibers and eventual period.** For \(n\ge N_k\) the correction in step 1 vanishes modulo \(2^k\), so \(S(n,5)\equiv G_r((n-r)/2)\pmod{2^k}\). Any block of \(2^{k+1}\) consecutive indices contains exactly \(2^k\) indices of each parity. Within a parity, their half-indices run through every class modulo \(2^k\) once. Step 2 therefore gives every output class once per parity, proving the two-to-one fiber law and periodicity of period \(2^{k+1}\). For any residue \(y\), its limiting frequency is exactly \(2/(2^{k+1})=2^{-k}\).

**4. Least eventual period.** The parity of \(S(n,5)\) for \(n\ge5\) is periodic with the repeating four-term pattern \((1,1,0,0)\) at \(n=5,6,7,8\), so no odd shift can be an eventual period. For any positive even shift \(d\), the parity-class isometry in step 2 gives for all sufficiently large \(n\)
\[
\nu_2(G_r((n+d-r)/2)-G_r((n-r)/2))=\nu_2(d)-1.
\]
If \(\nu_2(d)\le k\), this is less than \(k\), and the error terms vanish modulo \(2^k\) for large \(n\). Hence every eventual period is divisible by \(2^{k+1}\); this is sharp by step 3.

**5. Sharp starting index.** For \(k\le3\), \(N_k=5\), already the smallest permitted index. If \(k\ge4\), choose \(n=k+1\ge5\) and \(d=2^{k+1}\). The isometry makes \(G_r((n+d-r)/2)-G_r((n-r)/2)\) divisible by \(2^k\), while the change in the correction has exact valuation \(n-2=k-1\). Thus
\[
S(k+1+2^{k+1},5)\not\equiv S(k+1,5)\pmod{2^k}.
\]
No starting index smaller than \(k+2\) can support the (necessarily unique least) eventual period; therefore the least starting index is \(N_k\).

## Verification
The accompanying standalone script `verify.py` builds the Stirling triangle independently by the standard recurrence. It checks exact residue fibers on three distinct blocks for each precision \(1\le k\le12\), verifies both parity-branch permutations, compares with modular odd-base exponential expressions, checks onset counterexamples for \(4\le k\le12\), and checks inclusion-exclusion against the recurrence. Expected output:

```
VERIFY_OK levels=1..12 exact_fiber_counts=PASS both_parity_bijections=PASS shift_checks=49140 fiber_cells=24570 exponential_identity_checks=76 sharp_preperiod_checks=9 lower_columns=PASS
```

The computation verifies finite instances. The unrestricted assertions follow from the proof, not from a computer search.

## Relationship to prior work
Amdeberhan, Manna and Moll (2007/2008) analyze valuations of the fifth column and identify parity and valuation branch patterns; those statements do not supply the complete 2-adic output-fiber distribution. Kwong (1989) determines the least eventual periods of fixed Stirling columns, which covers the period-length conclusion above; this aspect is explicitly **not** claimed to be historically new. Bennett and Mosteig (2013) give a systematic classification of valuation classes, including the fifth column, which does not specify the one-per-parity residue preimages. Zhao, Hong and Zhao (2014) obtain valuations of differences on special dyadic index classes. The new assertion is the *full fiber-uniformity theorem with parity uniqueness and sharp onset*, not the already-known period or parity/valuation statements. Separately, the first four fixed positive Stirling columns fail to cover every class modulo four on their tails, making the fifth column the first whose complete binary-power residue support is uniform.

## Limitations
No assertion is made for other fixed Stirling columns or for odd prime powers. The earlier period theorem is prior literature. Finite checks are not substitutes for the isometry proof. The possibility of an unlocated equivalent distribution theorem in historical literature is a residual priority risk; no independent mathematical audit has been performed.

## References
- T. Amdeberhan, D. Manna, and V. H. Moll, *The 2-adic valuations of Stirling numbers*, public preprint of 20 July 2007, https://arxiv.org/abs/0707.3104.
- Y. H. Harris Kwong, *Minimum Periods of \(S(n,k)\) Modulo \(M\)*, Fibonacci Quarterly **27** (1989), 217–221, https://www.fq.math.ca/Scanned/27-3/kwong.pdf.
- C. Bennett and E. Mosteig, *Congruence Classes of 2-adic Valuations of Stirling Numbers of the Second Kind*, Journal of Integer Sequences **16** (2013), Article 13.3.6, https://cs.uwaterloo.ca/journals/JIS/VOL16/Mosteig/mosteig4.html.
- Q. Zhao, S. Hong, and J. Zhao, *Divisibility by 2 of Stirling numbers of the second kind and their differences*, Journal of Number Theory **140** (2014), 186–195, https://doi.org/10.1016/j.jnt.2014.01.005.
