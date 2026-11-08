# Exact equilibrium-count moments on random conformist–rebel rings

## Finding

For the two-action fashion game on a simple ring with independently fair conformist/rebel types, the full exact first and second moments of the pure-Nash-equilibrium count have algebraic closed forms at every ring size. Their leading bases satisfy \((5+\sqrt{17})/4>9/4\); thus the normalized variance grows exponentially, even as the chance of no equilibrium tends to zero.

For integers \(n\ge3\), write \(a_\pm=(5\pm\sqrt{17})/4\) and \(b_\pm=(7\pm\sqrt{33})/8\). With the definitions in the next section, the formulas are

\[
\mathbb E Z_n=\left(\frac32\right)^n+\left(-\frac12\right)^n+
\begin{cases}2(-3/4)^{n/2},&n\text{ even},\\0,&n\text{ odd},\end{cases}
\]

\[
\mathbb E Z_n^2=a_+^n+a_-^n+(-1)^n+2+3(-1/2)^n+
\begin{cases}
4(-1)^{n/2}(b_+^{n/2}+b_-^{n/2}),&n\text{ even},\\
0,&n\text{ odd}.
\end{cases}
\]

In particular,

\[
\frac{\operatorname{Var}(Z_n)}{(\mathbb E Z_n)^2}
=\left(\frac{5+\sqrt{17}}9\right)^n(1+o(1))-1
\quad\text{as }n\to\infty.
\]

## Assumptions and scope

Fix a simple cycle \(C_n\) with \(n\ge3\) and indices modulo \(n\). At every vertex, independently choose its type \(t_i\) uniformly from \(\{-1,1\}\); conformists have type \(+1\) and rebels \(-1\). Each agent simultaneously chooses an action \(x_i\in\{-1,1\}\) with payoff

\[
u_i(x)=t_i x_i(x_{i-1}+x_{i+1}).
\]

Actions are pure Nash equilibria exactly when \(u_i(x)\ge0\) for every vertex. Zero payoff is a valid best response, because switching the player's action negates this payoff. Let \(Z_n(t)\) be the number of such profiles for a given type word and \(Z_n\) the random variable under the independent type distribution. These statements are only for degree-two rings and fair independent types. The known zero-equilibrium probability is quoted as a contextual comparison, not part of the originality claim.

## Proof

**1. Edge-product encoding.** For any action profile set \(e_i=x_ix_{i+1}\in\{-1,1\}\). Then \(x_i(x_{i-1}+x_{i+1})=e_{i-1}+e_i\). The edge word must obey \(\prod_i e_i=1\). Conversely, every edge word obeying this condition lifts to exactly two action profiles, related by simultaneous action reversal.

Index rows and columns by the edge signs \((+1,-1)\). At a conformist vertex, the sole forbidden pair of consecutive edge signs is \((-1,-1)\); at a rebel vertex, it is \((+1,+1)\). The local matrices are

\[
B_C=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
B_R=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
D=\operatorname{diag}(1,-1).
\]

The parity projector is \(\mathbf1_{\prod e_i=1}=(1+\prod e_i)/2\). The factor two from spin lifts cancels the projector denominator, giving the **exact identity for each type word**

\[
Z_n(t)=\operatorname{tr}\!\left(\prod_{i=1}^nB_{t_i}\right)
+\operatorname{tr}\!\left(\prod_{i=1}^n(B_{t_i}D)\right).
\tag{1}
\]

The order of factors follows the cyclic vertex order; multiplying by \(D\) weights each outgoing edge sign.

**2. First moment.** Independence and fairness of the types replace each local matrix by

\[
A=\frac{B_C+B_R}{2}=\begin{pmatrix}1/2&1\\1&1/2\end{pmatrix}.
\]

Thus \(\mathbb E Z_n=\operatorname{tr}(A^n)+\operatorname{tr}((AD)^n)\). The eigenvalues of \(A\) are \(3/2,-1/2\). Since \((AD)^2=-3I/4\), its odd-power trace vanishes and its even-power trace is \(2(-3/4)^{n/2}\). This proves the first formula.

**3. Two-replica encoding and second moment.** For two proposed action profiles, use the corresponding edge signs \(e_i\) and \(f_i\), each of even product. A *single* random vertex type must satisfy both profiles. Index the four ordered sign pairs by \((++,+-,-+,--)\). Averaging the local joint-compatibility indicators over a fair type produces

\[
K=\begin{pmatrix}
1/2&1/2&1/2&1\\
1/2&0&1&1/2\\
1/2&1&0&1/2\\
1&1/2&1/2&1/2
\end{pmatrix}.
\]

For example, if both consecutive sign pairs are mixed, either player type is compatible, whereas one same-sign positive pair is compatible only with a conformist. Let

\[
D_e=\operatorname{diag}(1,1,-1,-1),\quad
D_f=\operatorname{diag}(1,-1,1,-1),\quad
D_{ef}=D_eD_f.
\]

Apply both even-product projectors and both two-to-one spin lifts. The four multiplicative characters give exactly

\[
\mathbb E Z_n^2=\operatorname{tr}(K^n)
+\operatorname{tr}((KD_e)^n)
+\operatorname{tr}((KD_f)^n)
+\operatorname{tr}((KD_{ef})^n).
\tag{2}
\]

**4. Exact spectra.** Direct determinant expansions give

\[
\begin{aligned}
\det(\lambda I-K)&=\frac{(\lambda+1)(2\lambda+1)(2\lambda^2-5\lambda+1)}4,\\
\det(\lambda I-KD_e)&=\det(\lambda I-KD_f)=\frac{4\lambda^4+7\lambda^2+1}{4},\\
\det(\lambda I-KD_{ef})&=\frac{(\lambda-1)^2(2\lambda+1)^2}{4}.
\end{aligned}
\]

The first spectrum is \(a_+,a_-,-1,-1/2\). The middle two spectra are \(\pm i\sqrt{b_+},\pm i\sqrt{b_-}\). The final spectrum is \(1,1,-1/2,-1/2\). Taking power traces in (2) yields exactly the asserted second-moment formula, including the even-size oscillating term. All matrices are finite and their identities hold for every integer \(n\ge3\); no limit or numerical fit is used to establish the identities.

**5. Fluctuation exponent.** The dominant base of the mean is \(3/2\), while that of the second moment is \(a_+=(5+\sqrt{17})/4\). All remaining eigenvalue magnitudes are smaller. Hence

\[
\frac{\mathbb E Z_n^2}{(\mathbb E Z_n)^2}
=\left(\frac{a_+}{9/4}\right)^n(1+o(1))
=\left(\frac{5+\sqrt{17}}9\right)^n(1+o(1)).
\]

Subtract one to obtain the variance ratio. Since the base is strictly greater than one, the normalized variance diverges exponentially.

The classical ring-existence theorem of Cao and Yang says a ring has no equilibrium precisely for a strictly alternating type word with odd half-length. Under independent fair types this is \(\Pr(Z_n=0)=2^{1-n}\) when \(n\equiv2\pmod4\), and zero otherwise. This last fact is prior work, used only to contrast existence with count fluctuations.

## Verification

Run `python verify_cycle_equilibria.py` using standard Python. For each size \(3\le n\le10\), the verifier enumerates every one of the \(2^n\) type configurations and every one of the \(2^n\) spin profiles, checks all payoff inequalities directly, and independently evaluates the one- and two-replica transfer traces with rational arithmetic. It also matches a separate radical-free scalar recurrence for the second-moment formula. The run checks \(2040\) type configurations and all corresponding action profiles, including all no-equilibrium configurations.

Selected exact moments (in ascending \(n\)) are \((13/4,25/2)\) for \(n=3\), \((25/4,81/2)\) for \(n=4\), and \((169/16,1021/8)\) for \(n=6\), where each pair denotes \((\mathbb E Z_n,\mathbb E Z_n^2)\). Enumeration verifies examples and implementation; the transfer identities and characteristic-polynomial proof establish all integer sizes.

## Relationship to prior work

Cao and Yang (2014) define the fashion game, prove the pure-equilibrium existence criterion for rings (Theorem 4), and establish even equilibrium-count parity. That existence criterion is not presented as new. Shen and Lin (2020) characterize optimal minimum player satisfaction on paths and cycles, not the random-type equilibrium-count moments. Cao, Sanchez and Zhang (first made public July 7, 2026) provide a general framework for heterogeneous network games, including equilibrium existence conditions, dynamics and random sparse-network statements, without these exact cyclic count moments. Sun (2016) investigates statistical mechanics of the fashion game on random networks; its accessible descriptions address satisfaction fractions and an equilibrium-existence region. Its full text was unavailable for inspection, so possible overlap there is a residual publication-priority risk rather than a verified noncoverage statement.

The new object is the complete annealed second-moment law under independent fair types on fixed rings, and the resulting exponential relative-variance exponent. A general statement that some ring has a pure equilibrium does not imply this distributional count identity.

## Limitations

The formula assumes a deterministic simple degree-two cycle and independent equiprobable binary types. No results for biased types, arbitrary random graphs, equilibrium-selection dynamics, quenched typical counts, or the full distribution are claimed. Exponentially increasing normalized variance is a precise second-moment statement, not a claim that typical games have exponentially large relative deviations. The accessible literature checks cannot exclude all equivalent unindexed or inaccessible results; Sun's 2016 full paper was not readable through available authorized access. Scientific independent audit has not been performed.

## References

- Zhigang Cao and Xiaoguang Yang, *The fashion game: Network extension of Matching Pennies*, Theoretical Computer Science 540–541 (2014), 169–181. https://doi.org/10.1016/j.tcs.2014.05.009 . Open full text: https://ml2.inf.ethz.ch/courses/tcsod/TCS-Seminar-papers/The%20fashion%20game%3A%20Network%20extension%20of%20Matching%20Pennies.pdf .
- Chenli Shen and Wensong Lin, *Fashion game on graphs*, Discrete Optimization 38 (2020), 100606. https://doi.org/10.1016/j.disopt.2020.100606 .
- Wenjie Cao, Angel Sanchez and Boyu Zhang, *Network games with heterogeneous players*, arXiv:2607.05932, first posted July 7, 2026. https://arxiv.org/abs/2607.05932 .
- Yi-Fan Sun, *Statistical mechanics of the fashion game on random networks*, Journal of Statistical Mechanics: Theory and Experiment (2016), 023203. https://doi.org/10.1088/1742-5468/2016/02/023203 . Full text was not inspected.
