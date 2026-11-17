# Complete almost-realizability obstruction for integral Raney sequences

## Finding
For integers \(P\geq 1\) and \(R\geq1\), let the Raney sequence be
\[
a_n=\frac{R}{Pn+R}\binom{Pn+R}{n},\qquad n\geq1.
\]
The sequence is **almost realizable** (some positive integer multiple counts fixed points of every iterate of a set map) if and only if \((P,R)=(1,1)\). More precisely, for every sufficiently large prime \(\ell\), the Möbius/Dold numerator has one of two nonzero fixed residues:
\[
a_{\ell}-a_1\equiv P-R\pmod\ell\quad(R\ne P),
\]
\[
a_{2\ell}-a_{\ell}-a_2+a_1\equiv\frac{P(P-1)}2\pmod\ell\quad(R=P).
\]
Thus the diagonal \(R=P\), invisible to the prime-index obstruction, is excluded at twice-prime indices. The unique exception \((P,R)=(1,1)\) gives \(a_n=1\) for every \(n\) and is realizable by one fixed point.

## Assumptions and scope
Fix integers \(P\geq1\) and \(R\geq1\). The Raney numbers are nonnegative integers: if \(C(z)\) is the unique formal power series satisfying \(C(z)=1+zC(z)^P\), Lagrange inversion gives \([z^n]C(z)^R=R\binom{Pn+R}{n}/(Pn+R)\); the coefficient counts ordered forests of \(R\) rooted plane \(P\)-ary trees. In particular, the formula defines integer counts for all \(n\geq0\).

For an integer sequence \((a_n)_{n\geq1}\), let \(b_n=\sum_{d\mid n}\mu(d)a_{n/d}\). If a positive integer \(M\) times \((a_n)\) counts fixed points of all iterates of a self-map, then \(n\mid M b_n\) for every \(n\geq1\), since \(M b_n/n\) is the number of cycles of exact length \(n\). Almost realizability requires the existence of a **single** such \(M\) independent of \(n\). The proof below disproves even this necessary divisibility, so no sign or dynamical assumptions are needed for the negative direction.

## Proof
The first two Raney numbers are obtained directly:
\[
a_1=R,\qquad a_2=\frac{R(2P+R-1)}2.
\]
Let \(\ell\) be a prime exceeding \(2P+R\) and \(2\). For \(j\in\{1,2\}\), the factor \(Pj\ell+R\) is congruent to \(R\not\equiv0\pmod\ell\), hence invertible modulo \(\ell\). Lucas's binomial congruence (in base \(\ell\)) therefore gives
\[
a_{j\ell}
=\frac{R}{Pj\ell+R}\binom{Pj\ell+R}{j\ell}
\equiv\binom{Pj}{j}\pmod\ell.
\]
The restrictions on \(\ell\) ensure that the base-\(\ell\) digits of \(Pj\ell+R\) are precisely \((Pj,R)\) and those of \(j\ell\) are \((j,0)\), so the Lucas step has no hidden carry or boundary case. In particular,
\[
a_{\ell}\equiv P\pmod\ell,\qquad
 a_{2\ell}\equiv P(2P-1)\pmod\ell.
\]

If \(R\ne P\), use the prime index \(n=\ell\). Then \(b_{\ell}=a_{\ell}-a_1\equiv P-R\pmod\ell\). Since \(P-R\) is a fixed nonzero integer, for any fixed positive multiplier \(M\) we may choose a prime \(\ell>\max(2P+R,M|P-R|)\). For this prime \(\ell\nmid Mb_{\ell}\), contradicting Dold divisibility \(\ell\mid Mb_{\ell}\).

If \(R=P\geq2\), the prime-index residue vanishes. For odd primes \(\ell>2P+R\), the squarefree index \(n=2\ell\) gives
\[
 b_{2\ell}=a_{2\ell}-a_{\ell}-a_2+a_1
 \equiv P(2P-1)-P-\frac{P(3P-1)}2+P
 =\frac{P(P-1)}2\pmod\ell.
\]
This is a fixed positive integer. Choose \(\ell\) larger than both \(2P+R\) and \(M P(P-1)/2\). Then \(\ell\nmid M b_{2\ell}\), contradicting the required divisibility \(2\ell\mid M b_{2\ell}\). Thus no \(M\) exists for any \(P\geq2\), including the entire diagonal.

Finally, \((P,R)=(1,1)\) gives \(a_n=(n+1)^{-1}\binom{n+1}{n}=1\) for all \(n\). One fixed point realizes this sequence without scaling. Every permitted pair belongs to exactly one of these cases, completing the classification.

## Verification
The standalone `verify.py` recomputes Raney integers using exact binomial coefficients; verifies the formulas for \(a_1,a_2\), both Lucas residues, both Dold residues, and the unique exceptional constant family. It covers all \(1\leq P\leq7\), \(1\leq R\leq P+3\) and all primes \(17\leq\ell<60\) meeting \(\ell>2P+R\) (513 independent congruence checks). `verify_output.txt` is the saved output of that checker. The infinite classification is proved by Lucas's theorem and the unboundedness of primes, **not** by extrapolating from finite tests.

## Relationship to prior work
The Raney/Fuss–Catalan family and its combinatorial interpretations are treated in Rusu (2021) and in standard literature on \(P\)-ary forests. Zhang (2023), *Realizability of Some Combinatorial Sequences*, defines almost realizability, states the Dold criterion (Lemma 30), and proves that the ordinary Catalan sequence is not almost realizable (Theorem 21(1)). That Catalan case is precisely \((P,R)=(2,1)\). Zhang's theorem also excludes Motzkin and Schröder sequences; those are different combinatorial sequences. The present classification covers **every** integral Raney pair, and in particular handles the shifted/diagonal cases \(R=P\) by an obstruction at \(2\ell\) not implied by the prime-index Catalan calculation. The general Dold and Lucas lemmas are standard and are not claimed as new.

## Limitations
The classification applies only to positive-integer Raney parameters \(P\geq1\) and \(R\geq1\), and indices starting at \(n=1\); it makes no claim about real parameters, generalized shifts, or arbitrary linear combinations. It proves non-almost-realizability, not an enumeration of individual periodic orbits. Prior equivalence in unindexed literature cannot be excluded; independent scientific audit has not been performed.

## References
1. G.-R. Zhang, *Realizability of Some Combinatorial Sequences*, arXiv:2302.09454v1 (19 February 2023), especially Lemma 30, Theorem 21 and its proof, https://arxiv.org/pdf/2302.09454 .
2. I. Rusu, *Raney numbers, threshold sequences and Motzkin-like paths*, arXiv:2109.05291v1 (11 September 2021), https://arxiv.org/abs/2109.05291 .
3. J.-G. Liu and R. L. Pego, *On generating functions of Hausdorff moment sequences*, arXiv:1401.8052 (2014), for the Raney-number parameter family, https://arxiv.org/abs/1401.8052 .
