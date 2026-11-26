# Exact Abelian-border multiplicities and an alphabet-size limit-law transition

## Finding

For a word over a fixed alphabet of size \(q\ge 2\), an *Abelian border of length* \(j\) means that its length-\(j\) prefix and suffix have identical letter-count vectors. Only nonempty **proper** borders are counted, with one count per length. Let \(K(w)\) be their number.

Define the formal power series
\[
U_q(t)=\sum_{j\ge 0}u_{q,j}t^j,\qquad
u_{q,j}=\sum_{a_1+\cdots+a_q=j}
 \left(\frac{j!}{a_1!\cdots a_q!}\right)^2,
\]
where the sum ranges over nonnegative integer \(q\)-tuples. Define
\[
F_q(t)=1-\frac{1}{U_q(t)},\qquad
T_q(t)=\frac{1}{(1-q^2t)U_q(t)}.
\]
Then **the exact number of \(q\)-ary words of every length and every Abelian-border multiplicity** is given by the two bivariate generating series
\[
\boxed{\begin{aligned}
\mathcal E_q(t,v)&=1+\frac{T_q(t)-1+vF_q(t)}{1-v^2F_q(t)},\\
\mathcal O_q(t,v)&=\frac{qT_q(t)}{1-v^2F_q(t)}.
\end{aligned}}
\]
Precisely, for every \(m\ge0\) and \(b\ge0\), \([t^m v^b]\mathcal E_q\) counts the length-\(2m\) words with \(K(w)=b\), and \([t^m v^b]\mathcal O_q\) counts the length-\(2m+1\) words with \(K(w)=b\). The empty word at \(m=0\) in the first series is a formal counting convention.

The same formulas give a sharp **alphabet-size transition**. If \(W_{q,n}\) is uniform on all \(q\)-ary words of length \(n\), put
\[
R_{q,m}=\#\{1\le j\le m:\text{the length-}j\text{ prefix and suffix of }W_{q,2m}\text{ are Abelian equivalent}\}.
\]
(The random variable has the same law for a uniformly random word of length \(2m+1\).) Write \(c=3\sqrt3/(4\pi)\) and let \(Z\) have exponential distribution of mean one. Then
\[
\boxed{\frac{R_{3,m}}{c\log m}\ \xrightarrow[m\to\infty]{\mathrm{d}}\ Z.}
\]
In contrast, the binary benchmark satisfies \(R_{2,m}/\sqrt m\xrightarrow{\mathrm d}|N(0,2)|\). For every fixed \(q\ge4\), \(R_{q,m}\) converges in distribution to a geometric random variable on \(\{0,1,\ldots\}\), with
\[
\Pr(R_{q,\infty}=r)=p_q(1-p_q)^r,\qquad
p_q=\left(\sum_{j\ge0}\frac{u_{q,j}}{q^{2j}}\right)^{-1}>0.
\]
Thus the typical number of short Abelian-border lengths is of square-root order for two letters, logarithmic order for three, and bounded in distribution for four or more. The corresponding full proper-border count \(K\) differs from \(2R\) by at most one, and hence has the stated limit laws with the factor two.

As a finite illustration, the numbers of ternary length-six words with exactly \(0,1,2,3,4,5\) proper Abelian-border lengths are respectively \(402,30,180,36,54,27\). These sum to \(729\).

## Assumptions and scope

The alphabet is labeled, finite, and of fixed size \(q\ge2\). Words are **linear**, not cyclic, and positions are distinguished. No reversals, alphabet permutations, or other identifications are taken. Border lengths are distinct integers, rather than distinct border substrings. All formulas are exact as formal power series; convergence is used only in the limiting statements. The main new enumerative and probabilistic content concerns alphabet sizes at least three. The pre-existing binary enumeration is recovered as a comparison case, not presented as a new binary result.

## Proof

**1. Exact walk encoding.** Write a word of length \(2m\) or \(2m+1\) from its ends inward, pairing the positions \((i,\,n+1-i)\) for \(1\le i\le m\). With \(e_a\) the \(a\)-th coordinate vector in \(\mathbb Z^q\), set
\[
X_i=e_{w_i}-e_{w_{n+1-i}},\qquad S_j=\sum_{i=1}^j X_i.
\]
An Abelian border of length \(j\le m\) is equivalent to \(S_j=0\). Each of the \(q^2\) ordered symbol pairs is chosen independently in a uniform random word; the middle symbol of an odd-length word is unconstrained. Hence every paired word is a walk using the ordered increments \(e_a-e_b\), including the \(q\) differently labeled zero increments. The number of return times among steps \(1,\ldots,m\) is exactly \(R\).

For \(j\) paired steps, the number ending at the origin is \(u_{q,j}\): both sides must have one and the same composition \((a_1,\ldots,a_q)\), and that composition occurs in \(j!/(a_1!\cdots a_q!)\) orders on each side. This establishes \(U_q\) including \(u_{q,0}=1\).

**2. Renewal factorization and exact coefficients.** Let \(f_{q,j}\) count length-\(j\) paired walks that return to zero for the *first positive time* exactly at \(j\), and let \(t_{q,j}\) count length-\(j\) walks with no positive-time return. The unique decomposition of an origin-ending walk into its first return and another origin-ending walk implies
\[
U_q(t)=1+\left(\sum_{j\ge1}f_{q,j}t^j\right)U_q(t),
\]
so the first-return series is \(F_q=1-U_q^{-1}\). A walk with any endpoint is uniquely a concatenation of some complete first-return excursions and a terminal no-return piece. Its total generating series is \((1-q^2t)^{-1}=T_q/(1-F_q)\). Consequently \(T_q=((1-q^2t)U_q)^{-1}\).

For length \(2m\), an origin return at the final paired step yields a single *central* Abelian-border length \(m\); every earlier return at step \(j<m\) produces two distinct border lengths \(j\) and \(2m-j\). Thus an origin-ending walk with \(r\ge1\) positive returns contributes \(2r-1\) proper border lengths and has series \(F_q^r\). A walk not ending at the origin with \(r\ge0\) returns contributes \(2r\) lengths and has series \(F_q^r(T_q-1)\), where the final no-return piece is nonempty. Including the empty word yields
\[
1+\sum_{r\ge0}v^{2r}F_q^r(T_q-1)+\sum_{r\ge1}v^{2r-1}F_q^r
=1+\frac{T_q-1+vF_q}{1-v^2F_q}=\mathcal E_q.
\]
For length \(2m+1\), every return at \(j\le m\) contributes the two lengths \(j\) and \(2m+1-j\), and the middle symbol has \(q\) choices. Hence \(\mathcal O_q=qT_q/(1-v^2F_q)\), proving every claimed exact coefficient. Setting \(v=1\) gives the required total counts \(1/(1-q^2t)\) and \(q/(1-q^2t)\).

**3. Exact return moments.** Normalize by \(q^{2m}\) and define
\[
V_q(z)=\sum_{j\ge0}p_{q,j}z^j,\qquad p_{q,j}=\frac{u_{q,j}}{q^{2j}}.
\]
The renewal decomposition gives the probability generating series
\[
\sum_{m,r\ge0}\Pr(R_{q,m}=r)z^m s^r
=\frac{1}{(1-z)V_q(z)}\frac{1}{1-s(1-V_q(z)^{-1})}.
\]
Differentiating \(k\) times with respect to \(s\), then setting \(s=1\), proves for every integer \(k\ge1\)
\[
\mathbb E[(R_{q,m})_k]=k!\sum_{\substack{j_1,\ldots,j_k\ge1\\j_1+\cdots+j_k\le m}}p_{q,j_1}\cdots p_{q,j_k},
\]
where \((R)_k=R(R-1)\cdots(R-k+1)\).

**4. Sharp local-return estimate.** The count vectors of the left and right length-\(j\) strings are independent multinomial random vectors. Keeping the first \(q-1\) coordinates, one vector has covariance \(j\Sigma\), where
\[
\Sigma=\frac1q I_{q-1}-\frac1{q^2}\mathbf1\mathbf1^{\mathsf T},
\qquad \det\Sigma=q^{-q}.
\]
Stirling's formula gives the usual lattice Gaussian approximation uniformly in any central window of width \(j^{1/2+\epsilon}\), while multinomial concentration makes the squared tails negligible. Summing the squares of the multinomial point probabilities, equivalently evaluating the difference-of-two-Gaussians lattice density at zero, gives
\[
p_{q,j}\sim\frac{q^{q/2}}{(4\pi j)^{(q-1)/2}}.
\]
The lattice is the standard composition lattice in \(\mathbb Z^{q-1}\) with fundamental volume one; the \(q\) diagonal zero increments produce no nontrivial period, so no periodicity factor is missing.

**5. Three asymptotic regimes.** For \(q=3\), the preceding estimate reads \(p_{3,j}\sim c/j\). Therefore \(\sum_{j=1}^m p_{3,j}\sim c\log m\). For any fixed \(k\), the multiple sum in step 3 is bounded above by \((\sum_{j\le m}p_{3,j})^k\) and below by \((\sum_{j\le\lfloor m/k\rfloor}p_{3,j})^k\). Both bounds are asymptotic to \((c\log m)^k\). Consequently the \(k\)-th scaled ordinary moment tends to \(k!\), as all lower factorial terms have smaller logarithmic order. These are precisely the moments of the mean-one exponential law, which is moment-determinate. This proves the ternary convergence in distribution without assuming a separate random-walk limit theorem.

For \(q=2\), \(p_{2,j}=\binom{2j}{j}/4^j\sim(\pi j)^{-1/2}\). The multiple sums from step 3, after scaling by \(m^{k/2}\), converge to the Dirichlet simplex integral \(\pi^{-k/2}\int_{x_i>0,\sum x_i\le1}\prod x_i^{-1/2}dx_1\cdots dx_k=1/\Gamma(1+k/2)\). Thus \(\mathbb E[(R_{2,m}/\sqrt m)^k]\to k!/\Gamma(1+k/2)\), the moments of \(|N(0,2)|\), also moment-determinate. This is included only to contrast with the new nonbinary regimes.

For \(q\ge4\), \(\sum_jp_{q,j}<\infty\). Evaluating the renewal identity at \(z=1\) shows that the probability of any future positive return to zero is \(f_q=1-V_q(1)^{-1}<1\). By independent identically distributed excursions at successive returns, the total lifetime number of positive returns is geometric, with probability \((1-f_q)f_q^r\). The finite-horizon \(R_{q,m}\) increases to that variable almost surely. This proves the stated convergence and its exact parameter. Finally, at even length \(K=2R-\mathbf1_{\{S_m=0\}}\) and at odd length \(K=2R\); the correction is bounded by one, so the diverging-scale limits follow.

## Verification

Run `python3 verify.py` using Python's standard library. The checker independently enumerates all words and their proper Abelian-border lengths for \(q=2,3,4\) through paired lengths \(m=6,5,4\), respectively. It recomputes \(u_{q,j}\), first-return and return-free coefficients, checks the exact short-return and full-border distributions, and checks odd lengths through \(m=3\). It verifies the ternary rows \((6,3)\), \((48,24,9)\), \((402,210,90,27)\), \((3438,1854,864,324,81)\), \((29754,16434,8082,3402,1134,243)\) for short returns, and numerically checks the approach of the ternary local-return coefficient to \(3\sqrt3/(4\pi)\). On successful completion it prints `VERIFY_OK`. Finite checks are corroboration only; the infinite proofs are the renewal, Gaussian and moment arguments above.

## Relationship to prior work

Blanchet-Sadri, Chen and Hawes (first public August 22, 2017) prove exact numbers of binary words with any prescribed count of distinct Abelian-border lengths (their Theorem 3); this is the pre-existing \(q=2\) case and not the originality claim here. Goč, Rampersad, Rigo and Salimov (2014) encode general-alphabet Abelian borders by lattice returns and enumerate words *without* Abelian borders, including ternary cases. Their return-to-origin correspondence is acknowledged, and the new renewal calculation uses it. The 2022 survey by Fici and Puzynina summarizes the known binary shortest-border results, rather than the all-alphabet multiplicity law or the ternary exponential transition. The present contribution determines the entire multiplicity enumerator for alphabets \(q\ge3\), together with its sharp probabilistic phase transition. These are statements about return *multiplicity*, not merely existence of a border or the first return.

## Limitations

The analysis concerns independent uniformly sampled symbols; nonuniform letters, partial words with holes, and arbitrary dependence are not covered. The exact coefficient formula is a formal-power-series representation, not an elementary closed product for every coefficient. Classical random-walk renewal and local central-limit techniques underlie the proof; no new theorem about general random walks is claimed. The binary distribution and the general-alphabet path correspondence are prior work. Search and comparison cannot exclude an unindexed equivalent ternary or higher-alphabet multiplicity calculation.

## References

1. F. Blanchet-Sadri, K. Chen and K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, Electronic Proceedings in Theoretical Computer Science 252 (2017), 56–70, Theorem 3. First public August 22, 2017. https://arxiv.org/abs/1708.06461 ; https://doi.org/10.4204/EPTCS.252.9
2. D. Goč, N. Rampersad, M. Rigo and P. Salimov, *On the Number of Abelian Bordered Words (with an Example of Automatic Theorem-Proving)*, International Journal of Foundations of Computer Science (2015), original preprint 2014, Propositions 11, 12, 15 and 16. https://orbi.uliege.be/bitstream/2268/178701/1/numberAbelianBorder.pdf
3. G. Fici and S. Puzynina, *Abelian Combinatorics on Words: A Survey*, arXiv:2207.09937v1, first public July 20, 2022; Section 6. https://arxiv.org/abs/2207.09937
