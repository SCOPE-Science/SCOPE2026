# Unique fifth-adic zero lifts and exact valuation densities for involution numbers

## Finding
Let \(I_0=I_1=1\) and \(I_{n+2}=I_{n+1}+(n+1)I_n\) for all \(n\ge0\). Thus \(I_n\) is the number of involutions on \(n\) labels (the telephone numbers). For each \(k\ge1\), exactly one residue \(\alpha_k\pmod{5^k}\) satisfies
\[
5^k\mid I_n\quad\Longleftrightarrow\quad n\equiv\alpha_k\pmod{5^k}\qquad(n\ge0).
\]
These residues are compatible and define a unique \(\alpha\in4+5\mathbb Z_5\). For every nonnegative integer \(n\),
\[
\nu_5(I_n)=\nu_5(n-\alpha).
\]
In particular the index sequence modulo \(5^k\) has least period \(5^k\), and for every integer \(j\ge0\) the natural density of indices with \(\nu_5(I_n)=j\) is exactly \(4/5^{j+1}\). The first six zero indices \(\alpha_k\), chosen in \([0,5^k)\), are \(4,24,99,349,974,10349\).

## Assumptions and scope
All indices are nonnegative integers. The five-adic valuation is normalized by \(\nu_5(5)=1\), with \(\nu_5(0)=\infty\); five-adic roots are elements of \(\mathbb Z_5\). The result concerns the index-to-value map for the classical unweighted involution numbers at the prime five. It does not classify unit-residue frequencies or assert analogous behavior at other primes.

## Proof
**Step 1: The base-five cycle.** The first five residues of \(I_n\pmod5\) are
\[
(u_0,u_1,u_2,u_3,u_4)=(1,1,2,4,0).
\]
The recurrence has coefficient \(n+1\) periodic modulo five, and \((I_5,I_6)\equiv(I_0,I_1)\pmod5\); hence \(I_{5t+j}\equiv u_j\pmod5\) for all integers \(t\ge0\) and \(0\le j<5\). Exactly the indices \(n\equiv4\pmod5\) give zero.

**Step 2: A universal shift-quotient lemma.** For every integer \(r\ge1\) put \(h=5^r\). We prove by induction simultaneously that \(I_{n+h}\equiv I_n\pmod h\) and, writing
\[
d_r(n)=\frac{I_{n+h}-I_n}{h},\qquad c_r=d_r(0)\bmod5,
\]
that the integral quotient obeys
\[
d_r(5t+j)\equiv(c_r-t)u_j+b_j\pmod5,\qquad (b_0,b_1,b_2,b_3,b_4)=(0,0,1,2,2).
\]
The period assertion for \(r=1\) is Step 1. Assuming it at level \(r\), subtracting the two involution recurrences gives the exact identity
\[
d_r(n+2)=d_r(n+1)+(n+1)d_r(n)+I_{n+h}.
\]
The initial terms satisfy \(d_r(1)=d_r(0)+I_{h-1}\equiv c_r\pmod5\), since \(h-1\equiv4\pmod5\). Using \(I_n\equiv u_{n\bmod5}\pmod5\), the recurrence gives, successively across a five-term block, the rows
\[
(c_r-t,\ c_r-t,\ 2(c_r-t)+1,\ 4(c_r-t)+2,\ 2).
\]
The next row starts at \(c_r-t-1\). This verifies the displayed quotient formula for every \(t\ge0\). For the period at level \(r+1\), telescope five shifts of size \(h\):
\[
\frac{I_{n+5h}-I_n}{h}=\sum_{s=0}^{4}d_r(n+sh)\equiv0\pmod5.
\]
Indeed \(n=5t+j\) and the quotient formula gives a sum of five copies of \((c_r-t)u_j+b_j\) minus \(5^{r-1}(0+1+2+3+4)u_j\), which is divisible by five. Therefore \(5h\mid I_{n+5h}-I_n\), completing the induction.

**Step 3: Exact distance preservation in the zero branch.** The last coordinate of the quotient lemma is
\[
\frac{I_{n+5^r}-I_n}{5^r}\equiv2\pmod5\qquad(n\equiv4\pmod5,\ r\ge1).
\]
For distinct nonnegative \(n,m\equiv4\pmod5\), suppose \(m>n\) and write \(m-n=5^r q\) with \(r\ge1\), \(5\nmid q\). Summing \(q\) consecutive shifts of size \(5^r\) proves
\[
\frac{I_m-I_n}{5^r}\equiv2q\not\equiv0\pmod5,
\quad\text{hence}\quad
\nu_5(I_m-I_n)=\nu_5(m-n).
\]

**Step 4: Unique root and valuations.** For a fixed \(k\ge1\), the \(5^{k-1}\) indices \(n\equiv4\pmod5\) in \([0,5^k)\) have pairwise different images modulo \(5^k\), by Step 3. Their images are all divisible by five, so counting shows that they map bijectively onto \(5\mathbb Z/5^k\mathbb Z\). Thus exactly one index \(\alpha_k\) maps to zero modulo \(5^k\); there are no such indices outside the branch by Step 1. The roots are compatible by uniqueness, so they determine \(\alpha\in\mathbb Z_5\). As \(I_n\) is positive for every \(n\ge0\), there is no integer index equal to \(\alpha\). The equivalence of divisibility by each \(5^k\) proves \(\nu_5(I_n)=\nu_5(n-\alpha)\). Periodicity modulo \(5^k\) follows from Step 2. Any positive period \(T\) is divisible by five by Step 1; choosing \(n\equiv4\pmod5\) and applying Step 3 to \(n\) and \(n+T\) forces \(5^k\mid T\), proving minimality. Finally \(5^j\mid I_n\) iff \(n\equiv\alpha_j\pmod{5^j}\), with density \(5^{-j}\). Subtracting successive tail densities yields \(5^{-j}-5^{-(j+1)}=4/5^{j+1}\), also for \(j=0\).

## Verification
The accompanying standalone `checker.py` uses only exact modular integer arithmetic. Executing `python3 checker.py` verifies 281,474 finite assertions: the periods and unique zero index through \(5^6\), full five-divisible target coverage within the critical index branch, the five-row shift quotient through \(r=5\), and pairwise distance preservation on the first 140 indices in the zero branch. The result of executing the embedded checker is `PASS 281474 finite exact assertions`. These finite tests are corroboration; the unrestricted theorem is established by Steps 1–4.

## Relationship to prior work
Kim and Kim (2009) prove exact least periods for involution numbers modulo odd moduli and study their two-adic valuations. This proof recovers that period at powers of five but adds the unique zero index at every level, the exact five-adic distance law on the zero branch, and the complete valuation-density distribution. Eppstein (2015) discusses the distinct question of primes dividing individual telephone numbers. Universal shift congruences of Kallat (2026) provide general divisibility, not the evaluated unique-root or valuation law. The latter reference is contextual only, not the archive-date anchor.

## Limitations
No independent audit has been performed. The proof does not classify all unit-valued residues or their frequencies. Literature priority beyond inspected accessible sources, including unindexed or older p-adic interpolation treatments, remains uncertain. The finite checker does not substitute for the all-level argument.

## References
- D. Kim and J. S. Kim, *A combinatorial approach to the power of 2 in the number of involutions*, first publicly posted 2009-02-25, https://arxiv.org/abs/0902.4311.
- D. Eppstein, *Telephone primes*, 2015-11-23, https://11011110.github.io/blog/2015/11/23/telephone-primes.html.
- A. Kallat, *Universal Shift Congruences for Weighted Permutation Sequences*, 2026-10-11, https://arxiv.org/abs/2610.15849 (contextual later work).
