# Sharp fourth-power decay of the positivity margin for a symmetric octic

## Finding

For every integer \(n\ge 2\), define \(p_j(x)=\sum_{i=1}^{n}x_i^j\) and
\[
F_n(x)=4p_1^2(p_3-4p_1^3)^2+9p_2(p_6-8p_1^2p_4+16p_1^4p_2)-16p_1^8.
\]
Set \(\mu_n=\min\{F_n(x):x\in\mathbb R^n,\,p_2(x)=1\}\). Then
\[
\boxed{\frac{1}{256n^4}\le \mu_n\le\frac{16}{n^4}\quad(n\ge2).}
\]
Thus the *exact power-law order* of the positivity margin is \(\mu_n=\Theta(n^{-4})\). This is a decay-exponent result, **not** a claim of the optimal leading constant, of exact finite-\(n\) minima, or of a new Positivstellensatz.

## Assumptions and scope

The ground field is \(\mathbb R\); all powers are ordinary unnormalized power sums of real coordinates. The number of coordinates \(n\) varies over every integer at least two. Minima exist by continuity and compactness of the unit sphere. Homogeneity of degree eight gives \(F_n(cx)=c^8F_n(x)\). The base polynomial and its positive definiteness are due to Debus and Schabert, *Hilbert's 17th problem for symmetric functions: undecidability and a counterexample*, arXiv:2611.16690v1, Theorem 3.1; the quantitative fourth-power decay is the present finding.

## Proof

**1. Positive lower bound inherited from a directly reconstructed argument.** First establish \(F_n(x)\ge16p_1(x)^8\). If \(p_1(x)=0\), the right side is zero and \(F_n(x)=9p_2p_6\ge0\). Otherwise rescale, using degree-eight homogeneity, to \(p_1=1/2\). Define \(\sigma(t)=0\) for \(|t|\le2/3\) and \(\sigma(t)=\operatorname{sgn}(t)\) for \(|t|>2/3\). For every real \(t\),
\[
|t^3-\sigma(t)|\le3t^2|t^2-1|.
\]
Indeed the ratio of the left side to \(t^2|t^2-1|\), away from \(0,\pm1\), is bounded by \(6/5\) for \(|t|\le2/3\), and by \(1/t^2+1/(|t|+1)\le57/20<3\) otherwise. Let \(k=\sum_i\sigma(x_i)\in\mathbb Z\) and \(D=p_2\sum_i x_i^2(x_i^2-1)^2\). Cauchy–Schwarz gives \(|p_3-k|\le3\sqrt D\). At \(p_1=1/2\), the defining polynomial simplifies to
\[
F_n=(p_3-1/2)^2+9D-1/16.
\]
Since every integer is at distance at least \(1/2\) from \(1/2\),
\[
\tfrac12\le |k-\tfrac12|\le |p_3-\tfrac12|+3\sqrt D\le\sqrt{2}\sqrt{F_n+\tfrac1{16}}.
\]
Consequently \(F_n\ge1/16\) on the hyperplane \(p_1=1/2\). Undoing the scaling gives \(F_n(x)\ge (2p_1(x))^8/16=16p_1(x)^8\) for arbitrary real \(x\). This step verifies the source's quantitative positivity estimate rather than treating positivity as an unexplained black box.

**2. Uniform spherical lower bound.** Let \(p_2(x)=1\), and write \(s=p_1(x)\). The identity
\[
F_n=4s^2(p_3-4s^3)^2+9\sum_i x_i^2(x_i^2-4s^2)^2-16s^8
\]
holds exactly on that sphere. If \(s^2\ge1/(8n)\), Step 1 immediately gives \(F_n\ge16s^8\ge1/(256n^4)\). If \(s^2\le1/(8n)\), the power-mean inequality for \(a_i=x_i^2\ge0\), \(\sum a_i=1\), gives \(\sum_i x_i^6=\sum_i a_i^3\ge1/n^2\). Hence by the reverse triangle inequality in \(\ell^2\),
\[
\left(\sum_i x_i^2(x_i^2-4s^2)^2\right)^{1/2}
=\|x^{\circ3}-4s^2x\|_2\ge\|x^{\circ3}\|_2-4s^2\|x\|_2\ge\frac1n-\frac1{2n}=\frac1{2n}.
\]
It follows that
\[
F_n\ge\frac9{4n^2}-16s^8\ge\frac9{4n^2}-\frac1{256n^4}\ge\frac1{256n^4}.
\]
Together the two cases establish the claimed lower bound for every real unit vector, not just vectors with few distinct coordinates.

**3. Explicit near-balanced witnesses and upper bound.** Let \(r\in\{0,1\}\) be the parity of \(n\), put \(\varepsilon=1-2r\) and \(k=(n+r)/2\). Consider the rational vector \(v_n\) having exactly \(k\) coordinates equal to \(1+\varepsilon/(2n)\) and \(n-k\) coordinates equal to \(-1+\varepsilon/(2n)\). Then \(p_1(v_n)=1/2\) for either parity; set \(q_n=p_2(v_n)\). Direct expansion yields
\[
\begin{array}{ll}
 n\text{ even}: & q_n=\frac{4n^2+1}{4n},\quad F_n(v_n)=\frac{2544n^6+2512n^4+508n^2+9}{256n^6},\\[4pt]
 n\text{ odd}: & q_n=\frac{4n^2-3}{4n},\quad F_n(v_n)=\frac{2544n^6-3632n^4+892n^2+297}{256n^6}.
\end{array}
\]
The normalized witness \(v_n/\sqrt{q_n}\) is a real unit vector, so \(\mu_n\le F_n(v_n)/q_n^4\). If \(n\) is even, \(n\ge2\) implies \(q_n\ge n\) and \(F_n(v_n)<13<16\). If \(n\) is odd, \(n\ge3\) implies \(q_n\ge(11/12)n\) and \(F_n(v_n)\le159/16\); therefore
\[
n^4\mu_n\le \frac{159}{16}\left(\frac{12}{11}\right)^4<16.
\]
This completes the proof. In fact, both exhibited parity subsequences satisfy \(\lim_{n\to\infty} n^4F_n(v_n)/q_n^4=159/16\), without asserting that this is the sharp asymptotic minimum.

## Verification

The accompanying `proof_checker.py` reconstructs both parity-dependent witness formulas symbolically over \(\mathbb Q(n)\), verifies the simplification of \(F_n\) when \(p_1=1/2\), and independently evaluates rational examples. It is executable with Python and SymPy. The infinite inequalities in Steps 1–3 are proved above, not inferred from numerical testing. For a quick exact check, running `python proof_checker.py` should print `PASS symbolic identities and finite diagnostics`.

## Relationship to prior work

Debus and Schabert (arXiv:2611.16690v1, Section 3 and Remark 3.7) introduce \(F_n\), prove its positivity and failure of bounded-degree dimension-uniform sum-of-squares multipliers, and display balanced sign vectors giving \(\mu_{2m}\le9/(2m)^2\). That witness only gives an order-\(n^{-2}\) upper bound. The present near-balanced perturbation identifies the fourth-power upper bound and the matching fourth-power lower bound, without adding a claim about sos multiplier degrees. Their earlier *Any-dimensional Positivstellensätze for symmetric functions* (arXiv:2606.27551) concerns uniformly positive symmetric functions and has a distinct quantitative scope. Targeted searches did not identify the exact \(n^{-4}\) theorem; this is evidence of a gap, not a proof of global publication priority.

## Limitations

The constants \(1/256\) and \(16\) are demonstrably valid but not claimed sharp. The vector witnesses establish the exponent, not an exact optimizer classification. The proof is for the specific octic \(F_n\) with unnormalized power sums, not for every positive-definite symmetric form. The original article's non-SOS-multiplier theorem is cited, not reproved or strengthened. Independent validation has not been conducted.

## References

1. S. Debus and R. Schabert, *Hilbert's 17th problem for symmetric functions: undecidability and a counterexample*, arXiv:2611.16690v1 (first available 2026-11-12), https://arxiv.org/html/2611.16690v1, especially Theorem 3.1 and Remark 3.7.
2. S. Debus and R. Schabert, *Any-dimensional Positivstellensätze for symmetric functions*, arXiv:2606.27551 (2026-06-25), https://arxiv.org/abs/2606.27551.
