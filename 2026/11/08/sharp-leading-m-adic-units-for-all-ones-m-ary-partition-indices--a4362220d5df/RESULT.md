# Sharp leading \(m\)-adic units for all-ones \(m\)-ary partition indices

## Finding
Let \(b_m(N)\) count the partitions of the nonnegative integer \(N\) into parts \(1,m,m^2,\ldots\), without coloring or an upper bound on multiplicity. For every integer \(m\ge5\) with \(\gcd(m,6)=1\) and every integer \(r\ge2\),
\[
 b_m(m^r-1)\equiv m^{r-1}\left(\frac{m+1}{2}\right)^{r-2}\pmod{m^r}.
\]
Thus the established divisibility by \(m^{r-1}\) is sharp at these indices; the normalized first nonzero base-\(m\) digit is a power of the unit \((m+1)/2\). In particular, for each prime \(p\ge5\), \(\nu_p(b_p(p^r-1))=r-1\).

## Assumptions and scope
All power series are formal series over \(\mathbb Z\). The modulus \(m\) may be composite; it is odd and not divisible by three. The index \(r\) is arbitrary and unbounded. The assertion concerns the single natural family \(m^r-1\), not every \(m\)-ary partition number. Here divisibility by a power of a composite integer means ordinary integer divisibility, not a prime-adic valuation.

## Proof
**1. Digit extraction.** Write \(B_m(q)=\prod_{j\ge0}(1-q^{m^j})^{-1}\) and \(U_m(\sum_{n\ge0}c_nq^n)=\sum_{n\ge0}c_{mn}q^n\). The Euler-product identity \(B_m(q)=(1-q)^{-1}B_m(q^m)\) yields \(U_m(f(q)g(q^m))=(U_m f(q))g(q)\). Define \(h_j(q)=q/(1-q)^{j+1}\), \(H_1=mh_1\), and \(H_{k+1}=U_m(H_k/(1-q))\). Starting from \(U_m(qB_m(q))=h_0B_m(q)\), induction gives
\[
 U_m^r(qB_m(q))=H_{r-1}(q)B_m(q)\qquad(r\ge2).
\]
The coefficient of \(q\) on the left is \(b_m(m^r-1)\); since \(H_{r-1}\) has zero constant term and \(B_m(0)=1\), this is \([q]H_{r-1}\).

**2. Integral change of basis.** For each \(s\ge1\), there are integers \(\alpha_s(i)\), \(1\le i\le s\), satisfying
\[
 \binom{mn+s-1}{s}=\sum_{i=1}^{s}\alpha_s(i)\binom{n+i-1}{i},\qquad U_m h_s=\sum_{i=1}^{s}\alpha_s(i)h_i.
\]
Integrality follows recursively by substitution \(n=-1,-2,\ldots,-s\) in the polynomial identity. Comparing its top two polynomial coefficients gives
\[
 \alpha_s(s)=m^s,\qquad \alpha_s(s-1)=-\frac{(s-1)(m-1)m^{s-1}}2.
\]
In particular, \(\alpha_2(1)=-m(m-1)/2\), and direct substitution at \(n=-1\) gives \(\alpha_3(1)=\binom m3=m(m-1)(m-2)/6\). Both are integer multiples of \(m\) under the hypotheses: for \(\alpha_3(1)\), \(6\mid(m-1)(m-2)\) because \(m\) is odd and prime to three.

**3. Weighted coefficient divisibility.** Write \(H_k=\sum_{j=1}^{k}a_{k,j}h_j\). Then \(a_{1,1}=m\) and
\[
 a_{k+1,i}=\sum_{j=\max(1,i-1)}^{k}a_{k,j}\alpha_{j+1}(i),
\]
with the conventions \(\alpha_{j+1}(i)=0\) when \(i>j+1\). We prove by induction that
\[
 m^{k+j-1}\mid a_{k,j}\qquad(1\le j\le k).
\]
For a fixed output index \(i\), every input \(j\ge i+1\) already carries the factor \(m^{k+j-1}\), hence at least \(m^{k+i}\). The contribution \(j=i\) gains a factor \(m\) from \(\alpha_{i+1}(i)=-i(m-1)m^i/2\). If \(i\ge2\), the contribution \(j=i-1\) gains \(m^i\) from \(\alpha_i(i)=m^i\), giving \(m^{k+2i-2}\), which is divisible by \(m^{k+i}\). For \(i=1\) this last contribution is absent. Thus every output coefficient has the required factor.

**4. First coefficient to one additional power.** For \(k\ge1\), the sum expressing \(a_{k+1,1}\) has the \(j=1\) term \(a_{k,1}\alpha_2(1)\). The \(j=2\) term is divisible by \(m^{k+2}\), because \(m^{k+1}\mid a_{k,2}\) and \(m\mid\alpha_3(1)\). Every term with \(j\ge3\) is divisible by \(m^{k+2}\) by Step 3. Therefore
\[
 a_{k+1,1}\equiv -\frac{m(m-1)}2a_{k,1}\pmod{m^{k+2}}.
\]
From \(a_{1,1}=m\), induction yields
\[
 a_{k,1}\equiv m^k\left(-\frac{m-1}{2}\right)^{k-1}\pmod{m^{k+1}}.
\]
Moreover \([q]h_j=1\) for every \(j\ge1\). By Step 3, all \(a_{k,j}\) with \(j\ge2\) vanish modulo \(m^{k+1}\). Thus \([q]H_k\equiv a_{k,1}\pmod{m^{k+1}}\). Setting \(k=r-1\), and observing \(-(m-1)/2\equiv(m+1)/2\pmod m\), proves the announced congruence.

**5. Sharpness.** Since \(\gcd((m+1)/2,m)=1\), the displayed normalized residue is invertible modulo \(m\). It follows simultaneously that \(m^{r-1}\) divides the partition number and \(m^r\) does not. If \(m=p\) is prime, this is exactly the stated valuation.

## Verification
The standard-library script `verify_partition_units.py` was run successfully. It computes coefficients independently through the exact recurrence \(b_m(n)=b_m(n-1)+[m\mid n]b_m(n/m)\), retaining enough modular precision, for seven bases and 29 pairs of parameters. It separately reconstructs four whole values with unrestricted coin-change dynamic programming, and checks 24 exact polynomial basis identities using integer binomial coefficients. All assertions passed. The full recorded stdout is in `verify_partition_units_output.txt`; computations are corroboration, while Steps 1–5 are the infinite proof.

For comparison, the condition excluding the prime three is substantive: at \(m=3\) and \(r=4\), direct computation gives a normalized residue \(2\pmod3\), whereas the displayed power would give \(1\pmod3\). No claim is made for bases divisible by three or even bases.

## Relationship to prior work
Rødseth and Sellers (2001) prove the underlying \(m^{r-1}\)-divisibility for odd bases, using an integral binomial basis and an extraction operator. Their Theorem 1 and the operator lemmas establish divisibility, but do not give the leading nonzero \(m\)-adic residue or prove exactness for this all-ones index family. Żmija (2024) derives general \(M\)-ary divisibility congruences and reproduces the binomial basis; his general theorem provides a lower modulus and does not give this exact normalized unit. Żmija (2017) discusses methods to compute higher-power residues; the inspected theorem states explicit formulas only at low powers, not this uniform closed form for arbitrary \(r\). The present argument extracts a weighted low-degree coefficient that survives at one modulus higher. A stronger but differently worded pre-existing result, if one exists, could cover this formula; this possibility is not ruled out by search alone.

## Limitations
The congruence does not cover \(\gcd(m,6)>1\), arbitrary \(N\), or the complete \(m\)-adic expansion of the partition number. Earlier literature contains the operator and base divisibility statements, so the contribution is the sharp unit residue and its all-power proof, not invention of the operator. The novelty comparison includes inspected papers and indexed searching, not an exhaustive census of all unpublished material. No independent audit has been performed.

## References
1. Ø. J. Rødseth and J. A. Sellers, *On m-ary Partition Function Congruences: A Fresh Look at a Past Problem*, Journal of Number Theory 87 (2001), 270–281, DOI `10.1006/jnth.2000.2594`; open author-hosted text: https://www.d.umn.edu/~jsellers/p14.pdf.
2. B. Żmija, *High order congruences for M-ary partitions*, arXiv:2403.04495v1 (first posted 2024-03-07); https://arxiv.org/abs/2403.04495; Periodica Mathematica Hungarica 89 (2024), 155–167.
3. B. Żmija, *Recurrence sequences connected with the m-ary partition function and their divisibility properties*, arXiv:1710.04303 (2017); https://arxiv.org/abs/1710.04303.
