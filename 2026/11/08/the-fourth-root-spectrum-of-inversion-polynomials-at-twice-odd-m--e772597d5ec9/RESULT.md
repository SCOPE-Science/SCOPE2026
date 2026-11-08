# The fourth-root spectrum of inversion polynomials at twice-odd moduli

## Finding

For each integer \(b\ge 2\), let \(I(a,b)\) be the inversion count of the permutation \(j\mapsto aj\pmod b\) of \(\{0,1,\ldots,b-1\}\), where \(\gcd(a,b)=1\), and define the inversion polynomial
\[
F_b(X)=\sum_{\substack{1\le a<b\\\gcd(a,b)=1}}X^{I(a,b)}.
\]
For every **odd** integer \(q\ge3\) and every odd unit \(a\pmod {2q}\), the following refined inversion congruence holds:
\[
\boxed{I(a,2q)\equiv 2I(a\bmod q,q)\pmod4.}
\]
In particular, \(I(a,2q)\) is always even and
\[
i^{I(a,2q)}=\left(\frac aq\right),
\]
where the symbol on the right is the Jacobi symbol. Thus the exact fourth-root evaluation is
\[
\boxed{F_{2q}(i)=\begin{cases}\varphi(q),&q\text{ is a perfect square},\\0,&q\text{ is not a perfect square}.\end{cases}}
\]
Equivalently, for nonsquare \(q\), the counts of unit multipliers with inversion number congruent to \(0\) and \(2\pmod4\) are each \(\varphi(q)/2\); for square \(q\), all \(\varphi(q)\) inversion numbers are divisible by four. There are no odd inversion counts. Consequently \(X^2+1\) divides \(F_{2q}(X)\) **if and only if** \(q\) is not a square, while for square \(q\), \(F_{2q}(X)\in\mathbb Z[X^4]\).

## Assumptions and scope

Here \(q\) ranges over all odd integers at least three, not merely primes or squarefree moduli. Multipliers \(a\) are complete units modulo \(2q\), represented by odd integers between one and \(2q-1\). For a square integer \(q\), the Jacobi symbol \(\left(\frac aq\right)\) is the principal character on the unit group; otherwise it is nonprincipal. The inversion number is computed on **all** residue classes, not merely the units. We make no assertion about higher powers of \(X^2+1\) in \(F_{2q}\) or about arbitrary even moduli.

## Proof

Fix \(q\) odd and \(a\) odd with \(\gcd(a,q)=1\). Put \(\pi_j=aj\bmod q\), taken in \(\{0,\ldots,q-1\}\), and \(\delta_j\in\{0,1\}\) uniquely determined by
\[
aj\bmod2q=\pi_j+q\delta_j,\qquad 0\le j<q.\]
Because \(a,q\) are odd, \(\delta_j\equiv j-\pi_j\pmod2\). Hence \(A=\sum_j\delta_j\) is even: \(A\equiv\sum_j(j-\pi_j)=0\pmod2\).

Write \(I_q=I(a\bmod q,q)\). Let \(B\) count the inversions \((j,k)\) of \(\pi\) with \(j<k\), \(\pi_j>\pi_k\), and \(\delta_j\ne\delta_k\). We show that \(B\) is even. If \(L_j\) is the number of earlier entries of \(\pi\) larger than \(\pi_j\), the total number of inversions incident with position \(j\) is \(d_j=\pi_j-j+2L_j\): there are exactly \(\pi_j-(j-L_j)\) later smaller entries. Thus \(d_j\equiv\pi_j-j\equiv\delta_j\pmod2\). Since an inversion with two distinct binary labels contributes \(\delta_j+\delta_k=1\pmod2\),
\[
B\equiv\sum_j\delta_j d_j\equiv\sum_j\delta_j^2\equiv A\equiv0\pmod2.
\]

In the multiplication permutation modulo \(2q\), the first block of \(q\) images is \(\pi_j+q\delta_j\); the second is \(\pi_j+q(1-\delta_j)\), because multiplying \(j+q\) adds \(q\) modulo \(2q\). Pairs internal to the two blocks contribute together \(2(I_q-B)+A(q-A)\) inversions. Indeed, a pair having equal labels contributes twice its inversion status in \(\pi\), and a pair having different labels contributes exactly one inversion across the two blocks. Cross-block pairs contribute \(Aq\): there are \(A^2\) pairs with both labels equal to one, and for the \(A(q-A)\) pairs with distinct labels, precisely one of the two possible orientations of base residues gives an inversion. Therefore the exact identity is
\[
I(a,2q)=2I_q-2B+A(2q-A).
\]
Since \(A\) and \(B\) are both even, the correction is a multiple of four. This proves the claimed congruence and, in particular, the evenness of every \(I(a,2q)\).

Now \(i^{I(a,2q)}=(-1)^{I_q}\). Zolotarev's permutation-sign theorem for odd moduli gives \((-1)^{I_q}=\left(\frac aq\right)\). Reduction from the unit group modulo \(2q\) to the unit group modulo \(q\) is a bijection. Hence \(F_{2q}(i)\) is the sum of the Jacobi character over all units modulo \(q\). Character orthogonality gives zero when \(q\) is nonsquare and \(\varphi(q)\) when \(q\) is a square. In combination with the already proved evenness, these evaluations determine exactly the two possible congruence classes of inversion numbers modulo four. Finally, \(F_{2q}(i)=0\) if and only if \(X^2+1\mid F_{2q}(X)\), because its coefficients are integers and \(X^2+1\) is the minimal polynomial of \(i\) over \(\mathbb Q\). This completes the proof.

## Verification

Run `python3 verify.py` in the same directory. The independent direct-permutation checker uses no external packages. It enumerates every odd modulus from \(3\) to \(139\) and every coprime odd multiplier, counts inversions directly by comparisons, checks the congruence and Jacobi character, and verifies the exact fourth-root sum. It examines 3,994 multiplier pairs. These finite tests are corroboration only; the block-counting proof covers all odd \(q\).

## Relationship to prior work

Chen, Dunn, Hewett, and Silas introduced \(F_b\) and their Conjecture 2.1 predicts cyclotomic roots at certain indices. Their Proposition 2.2 establishes \(F_b(-1)=\varphi(b)\) when \(b\equiv2\pmod4\), implying only the parity of inversion counts. Their Proposition 2.4 handles specified roots **for odd \(b\)**, and their Proposition 2.5 relates some evaluations to Kloosterman sums; neither directly establishes the present fourth-root formula for \(b=2q\). The result proves the \(\Phi_4\) criterion in this natural twice-odd family and strengthens it to an exact modulo-four distribution and pointwise Jacobi-symbol congruence. Zolotarev's theorem supplies the established odd-modulus sign identity used in the last step.

## Limitations

This result establishes no multiplicity of the cyclotomic factor, no analogue at higher roots of unity, and no classification for even moduli divisible by four. Historical priority beyond the checked primary paper and targeted literature searches remains subject to further independent review. Computational verification is finite and does not serve as a proof of the unrestricted statement.

## References

1. Y. Chen, N. Dunn, C. Hewett, and S. Silas, *On the Inversion Polynomial for Dedekind Sums*, arXiv:1411.4092v1, first posted November 15, 2014. https://arxiv.org/abs/1411.4092
2. Y. Chen, N. Dunn, C. Hewett, and S. Silas, *Dedekind sums s(a, b) and inversions modulo b*, International Journal of Number Theory 11 (2015), 2325–2339. DOI:10.1142/S1793042115501067. A lawful copy is available at https://icerm.brown.edu/summerug/2014/DedekindSumspaper.pdf.
3. G. Zolotarev, permutation-sign characterization of the Jacobi symbol (1872), as stated and used in reference 2, Section 3.
