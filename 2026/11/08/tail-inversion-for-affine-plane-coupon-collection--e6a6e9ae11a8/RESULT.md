# Tail inversion for affine-plane coupon collection

## Finding

**Theorem (sharp late tail and stochastic incomparability).** Let \(q\ge3\) be an integer for which a finite affine plane of order \(q\) exists. Its \(q^2\) points are coupons, and each of its \(q(q+1)\) lines contains \(q\) coupons. Let \(T_{\mathrm{AG}}\) be the minimum number of independent uniformly sampled lines needed to cover every point. Let \(T_{\mathrm{full}}\) be the analogous completion time when each draw is a uniformly sampled \(q\)-element subset of the same \(q^2\)-point set. Draws are with replacement in both models. For every integer \(t\ge0\), set

\[
\Delta_q(t)=\Pr(T_{\mathrm{AG}}>t)-\Pr(T_{\mathrm{full}}>t).
\]

Then the two completion-time laws are **stochastically incomparable**:

\[
\Delta_q(q)<0,\qquad
\lim_{t\to\infty}\frac{\Delta_q(t)}{\bigl((q-2)/(q+1)\bigr)^t}
=\frac{q^3(q-1)^2(q+1)}6>0.
\]

The limit is taken along positive integers \(t\), with \(q\) fixed. In particular, the late-tail difference has an **explicit strictly positive leading coefficient** for every existing affine plane of order at least three (including non-Desarguesian examples).

**Exact first crossover for order three.** For the affine plane of order \(3\),

\[
\Delta_3(t)=0\quad(t=0,1,2),\quad
\Delta_3(3)=-\frac{13}{1176},\quad
\Delta_3(t)>0\quad\text{for every integer }t\ge4.
\]

Thus the geometric scheme is more likely to finish after exactly three draws but is less likely to have finished after any four-or-more draws. This distributional inversion occurs even though the already-known mean comparison is \(\mathbb E T_{\mathrm{AG}}<\mathbb E T_{\mathrm{full}}\) at order three.

## Assumptions and scope

An affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, \(q\) points on each line, \(q+1\) lines through each point, exactly one line through each pair of distinct points, and \(q+1\) parallel classes of \(q\) mutually disjoint lines. Its existence is assumed, not asserted for every integer \(q\). No coordinates or Desarguesian hypothesis are required for the theorem. Each observation reveals all points of its selected line or \(q\)-subset. No deletion, replacement of collected coupons, or nonuniform draw probabilities are present.

The completion-time tails refer to \(\Pr(T>t)\), rather than \(\Pr(T\ge t)\). The asymptotic variable is the number of draws \(t\), not the plane order \(q\). The order-three assertion is an exact distributional comparison for every integer time.

## Proof

**1. Tail inclusion–exclusion.** For any point subset \(S\), let \(a_{\mathcal M}(S)\) be the fraction of admissible draws disjoint from \(S\) under mechanism \(\mathcal M\). For every integer \(t\ge1\), the event that at least one point has not been observed yields

\[
\Pr(T_{\mathcal M}>t)
=\sum_{\varnothing\ne S\subseteq V}(-1)^{|S|+1}a_{\mathcal M}(S)^t.
\tag{1}
\]

The single-point disjoint probability equals \(a_1=(q-1)/q\) in both models. By the affine \(2\)-design incidence property, the two-point disjoint probability is also identical:

\[
 a_2=\frac{q^2-q-1}{q(q+1)}
 =\frac{\binom{q^2-2}{q}}{\binom{q^2}{q}}.
\tag{2}
\]

Thus all one- and two-point contributions cancel **exactly at every time** in the tail difference.

**2. The dominant third-order obstruction.** A noncollinear triple lies on three distinct pair-joining lines. By inclusion–exclusion on the lines through each of its points, exactly \(3(q+1)-3=3q\) lines meet it. Hence the fraction of lines avoiding it is

\[
 a_*=\frac{q(q+1)-3q}{q(q+1)}=\frac{q-2}{q+1}.
\tag{3}
\]

A collinear triple has one extra triple-intersection line, and so has the strictly smaller avoidance fraction \(a_{\mathrm{col}}=(q^2-2q-1)/(q(q+1))\). The number of noncollinear triples is

\[
 C_q=\binom{q^2}{3}-q(q+1)\binom q3
 =\frac{q^3(q-1)^2(q+1)}6.
\tag{4}
\]

For a uniformly drawn \(q\)-subset, every triple has avoidance probability

\[
 b_3=\frac{\binom{q^2-3}{q}}{\binom{q^2}{q}}
 =\frac{(q-2)(q^2-q-1)}{q(q^2-2)}.
\tag{5}
\]

Direct subtraction gives

\[
 a_*-b_3=\frac{q-2}{q(q+1)(q^2-2)}>0.
\tag{6}
\]

Every affine-plane subset of at least four points has avoidance probability **strictly below** \(a_*\): choose three of its points; if collinear, their avoidance fraction is already smaller than \(a_*\). If noncollinear, choose a fourth point. Among the \(q+1\) lines through that fourth point, at most three meet one of the chosen triple's points, so at least \(q-2\ge1\) lines meet the fourth point while avoiding the triple. Adding that point therefore strictly reduces the avoidance probability. Every full-model subset of size at least four likewise has avoidance probability below \(b_3\), hence below \(a_*\).

Because the point set is finite for each fixed \(q\), the omitted terms in (1), after the exact cancellation (2), have a common exponential base strictly below \(a_*\). The only terms at base \(a_*\) are the \(C_q\) positive-sign noncollinear triple terms. Dividing (1) by \(a_*^t\) and taking integer \(t\to\infty\) proves the displayed sharp tail limit.

**3. Strictly faster initial complete covers.** Since each block has exactly \(q\) points, exactly \(q\) draws cover all \(q^2\) points if and only if the blocks are pairwise disjoint. In an affine plane this means drawing all \(q\) lines from one of its \(q+1\) parallel classes in some order. Thus

\[
\Pr(T_{\mathrm{AG}}\le q)
=\frac{(q+1)q!}{[q(q+1)]^q}
=\frac{(q-1)!}{q^{q-1}(q+1)^{q-1}}.
\tag{7}
\]

By conditioning successively on disjoint full-model blocks,

\[
\begin{aligned}
\Pr(T_{\mathrm{full}}\le q)
&=\prod_{j=1}^{q-1}\frac{\binom{q^2-jq}{q}}{\binom{q^2}{q}}\\
&\le\prod_{j=1}^{q-1}\left(1-\frac jq\right)^q
=\left(\frac{(q-1)!}{q^{q-1}}\right)^q.
\end{aligned}
\tag{8}
\]

For all \(q\ge3\),

\[
(q+1)(q-1)!\le 2(q+1)q^{q-3}<q^{q-1},
\]

because \(q^2>2(q+1)\). Comparing (7) and (8) gives \(\Pr(T_{\mathrm{AG}}\le q)>\Pr(T_{\mathrm{full}}\le q)\), or \(\Delta_q(q)<0\). Together with the late-tail limit this proves stochastic incomparability.

**4. Exact order-three crossover.** For \(q=3\), take the standard nine-point affine plane. Summing \((-1)^{|S|+1}\) over all nonempty point subsets \(S\) for each number of lines *meeting* \(S\) gives the following complete nonzero coefficient table:

| Number of lines meeting \(S\) | 4 | 7 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|
| Signed sum | 9 | -36 | 72 | -42 | -12 | 10 |

The table follows from all \(2^9-1=511\) nonempty subsets; `verify.py` reproduces it by literal complete enumeration and checks the resulting tails using a separate union-state dynamic program. The resulting exact tail difference, for integer \(t\ge1\), can be written \(\Delta_3(t)=4^{-t}F(t)\), where

\[
\begin{aligned}
F(t)={}&72-84(20/21)^t-42(2/3)^t+126(10/21)^t\\
&-12(1/3)^t-126(4/21)^t+84(1/21)^t.
\end{aligned}
\tag{9}
\]

Here \(F(3)=-104/147\) and \(F(4)=16/21\). Furthermore,

\[
\begin{aligned}
F(t+1)-F(t)={}&(10/21)^t\bigl[4\cdot2^t+14(7/5)^t-66\bigr]\\
&+(1/21)^t\bigl[8\cdot7^t+102\cdot4^t-80\bigr]>0
\end{aligned}
\tag{10}
\]

for all integers \(t\ge3\). The first bracket is strictly positive at \(t=3\), since \(4\cdot8+14(7/5)^3>66\), and increases thereafter. The second bracket is manifestly positive. Hence \(\Delta_3(t)>0\) for every integer \(t\ge4\). The two models cannot complete in fewer than three draws, giving equality of their tails at \(t=0,1,2\). Equation (9) gives \(\Delta_3(3)=-13/1176\). This completes the exact classification.

## Verification

Run `python3 verify.py` using Python 3.10 or later. It uses standard-library exact fractions and integers, constructs the affine planes of orders \(3,4,5\), verifies all triple incidence counts and the noncollinear counts, exhaustively enumerates the nine-point subsets in the order-three case, and independently checks the order-three tail with forward union-state dynamic programming through six draws in both mechanisms. It also checks the exact crossover algebra, known mean values and finite early-cover inequalities. The recorded run passed **3,060 finite assertions**. The infinite statement, strict bounds and asymptotic coefficient are established in Steps 1–3, not inferred from these finite checks.

## Relationship to prior work

Barak-Pelleg and Berend (2026, first posted June 26) introduce and analyze the affine/projective-plane fair mechanisms and give the exact **expectation** comparison for affine orders \(3\) and \(4\), plus numerical data for larger orders. Their order-three means are \(3001/385\) (affine) and \(3352087/429940\) (full), with affine strictly smaller; those mean values and the incidence constructions are prior results. The new statements here are a distribution-level, all-existing-orders stochastic-incomparability theorem, its sharp late-tail coefficient, and the exact unique order-three tail crossover. Grunbaum–Yaakobi (2025) develop general recovery-set expectation formulas and fair sampling comparison bounds; Berend–Sher (2025) investigate expectations under general group draws. Standard coupon-event inclusion–exclusion is used explicitly rather than claimed as new.

## Limitations

The late-tail asymptotic holds for each **fixed existing** affine-plane order \(q\), not jointly as \(q,t\to\infty\). It does not determine the exact crossover time for orders other than \(3\), nor the sign of the difference of expectations for arbitrary \(q\). The proof does not claim a general dominance criterion for every block design. No independent external validation or exhaustive historical-priority guarantee is claimed; a broader previous theorem on design-based completion-time tails could imply this special case.

## References

1. D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1 (first public posting 2026-06-26), https://arxiv.org/abs/2606.28216 . See Proposition 2.2 and Table 2.
2. Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305v1 (2025-10-29), https://arxiv.org/abs/2510.25305 .
3. D. Berend and T. Sher, *On a Conjecture of Schilling Regarding the Coupon Collector's Problem*, arXiv:2509.17201v1 (2025-09-21), https://arxiv.org/abs/2509.17201 .
