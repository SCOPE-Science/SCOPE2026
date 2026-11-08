# Infinitely many antipalindromic quotient representations for every \(4^r-1\) with \(r\ge2\)

## Finding
A positive integer is a binary antipalindrome if its canonical binary expansion has even length and each digit is the complement of the symmetric digit. For **every integer** \(r\ge2\), the integer \(4^r-1\) has **infinitely many distinct ordered representations** \(A/B\) in positive binary antipalindromes \(A,B\). An explicit family, indexed by every \(t\ge1\), is given below, with denominator lengths strictly increasing in \(t\).

## Assumptions and scope
Fix integers \(r\ge2\) and \(t\ge1\). Put \(Q=2^{2r}\) and \(b=Q-3\cdot2^{r-1}\), \(c=b-Q/2+1\), \(x=c-1=b-Q/2\), \(y=b+1\). All four are legitimate \(2r\)-bit blocks, including leading zeros. Here a bracket \([d_1,\ldots,d_k]_Q\) means the integer with those base-\(Q\) digits, written left to right with fixed-width binary blocks. A digit's reverse-complement \(R(d)\) is obtained by reversing its \(2r\)-bit expansion and changing each zero to one and each one to zero.

Define
\[
B_{r,t}=[b,\underbrace{x,\ldots,x}_{t},c,\underbrace{y,\ldots,y}_{t},b]_Q
\]
and
\[
A_{r,t}=[b-1,Q/2,\underbrace{0,\ldots,0}_{t-1},1,Q/2-1,\underbrace{Q-1,\ldots,Q-1}_{t-1},Q-2,Q-b]_Q.
\]
The theorem concerns positive integers with canonical binary expansions; no leading-zero padding is allowed for an entire integer, only within the internal blocks.

## Proof
First \(0<x<c<b<y<Q\), and both leading blocks \(b\) and \(b-1\) begin with a binary one. Fixed-width binary inspection gives
\[
R(b)=b,\quad R(c)=c,\quad R(x)=y,\quad R(b-1)=Q-b,
\]
\[
R(Q/2)=Q-2,\qquad R(0)=Q-1,\qquad R(1)=Q/2-1.
\]
Indeed \(b\) is the \(2r\)-bit word consisting of \(r-1\) ones, then 0, then 1, then \(r-1\) zeros; \(c\) has the pattern 0, then \(r-2\) ones, then 0, then 1, then \(r-2\) zeros, then 1. Also \(b-1\) is the palindrome with \(r-1\) ones, two zeros, and \(r-1\) ones. Taking the reverse complement blockwise therefore fixes both \(B_{r,t}\) and \(A_{r,t}\), which are binary antipalindromes.

To verify the quotient, compute \((Q-1)B_{r,t}=QB_{r,t}-B_{r,t}\) by base-\(Q\) column subtraction, from the least significant digit upward. The first column gives \(Q-b\) and a borrow. The next gives \(Q-2\) and a borrow; the next \(t-1\) give \(Q-1\) and preserve the borrow. The column crossing the central \(c\) gives \(Q/2-1\) and ends that borrow, since \(y-c-1=Q/2-1\). The following column gives \(c-x=1\); the next \(t-1\) give zero. Finally the column with \(x-b=-Q/2\) gives \(Q/2\) with a new borrow, and the leading column gives \(b-1\). These are precisely the digits of \(A_{r,t}\) in reverse order. Thus
\[
A_{r,t}=(Q-1)B_{r,t}=(4^r-1)B_{r,t}.
\]
Because its leading block starts in 1 and it comprises \(2t+3\) blocks, \(B_{r,t}\) has exactly \(2r(2t+3)\) binary digits. These lengths strictly increase with \(t\), so the positive denominators are pairwise distinct. This proves infinitely many representations for each \(r\ge2\).

## Verification
The accompanying standalone `verify.py` uses exact integers and directly checks the proposed base-\(Q\) digits against multiplication, the reverse-complement identities, canonical bit lengths and the antipalindrome conditions for every \(2\le r\le30\), \(1\le t\le20\). It verifies 580 pairs and prints explicit witnesses for \(r=2,3,4\). See `verification_output.txt`. These bounded tests are corroboration only: the symbolic digit argument above proves all \(r,t\) in the stated ranges.

## Relationship to prior work
Bai, Meleshko, Riasat and Shallit study integer quotients of binary antipalindromes and the number of their representations. Theorem 13 of their *INTEGERS* 2022 article establishes infinitely many representations for the **even** family \(2^{2n+1}-2^n\). Theorem 14 establishes exactly \(2^{i-1}\) representations for the adjacent **plus** family \(4^i+1\). Neither statement implies the present **odd minus** family \(4^r-1\), which gives infinitely many representations rather than finitely many. Their Section 3.5 lists individual examples such as 15 and 63 in OEIS A351175; a finite table of examples alone does not establish this all-parameter theorem.

## Limitations
This construction establishes infinitely many representations for the stated family only, not a classification of all odd quotients or a count of inequivalent representations under any unintroduced equivalence relation. It does not assert that the displayed family exhausts all representations. Originality has been assessed against inspected primary material and indexed searches; independently discovered or unindexed equivalent constructions remain possible. Independent scientific audit has not been performed.

## References
- J. H. Bai, J. Meleshko, S. Riasat, J. Shallit, *Quotients of Palindromic and Antipalindromic Numbers*, arXiv:2202.13694v1 (first public 28 February 2022); *INTEGERS* 22 (2022), article A96, Theorems 13 and 14 and Section 3.5. https://arxiv.org/abs/2202.13694 ; https://math.colgate.edu/~integers/w96/w96.pdf
- OEIS A351175 (integers with infinitely many binary-antipalindrome quotient representations). https://oeis.org/A351175
