# Three disjoint Markov-positivity windows for cubic inverse-Taylor stepping on a seven-state birth chain

## Finding

Let \(Q_n\) be the unit-rate pure-birth generator on states \(0,1,\dots,n-1\), absorbing at \(n-1\): its nonzero entries are \((Q_n)_{j,j}=-1\) and \((Q_n)_{j+1,j}=1\) for \(0\le j<n-1\), with \((Q_n)_{n-1,n-1}=0\). We represent distributions as columns. Consider the third-order inverse-Taylor, or \([0/3]\) Padé, time-step matrix
\[
R_n(h)=\left(I-hQ_n+\frac{h^2}{2}Q_n^2-\frac{h^3}{6}Q_n^3\right)^{-1},\qquad h\ge0.
\]
Every \(R_n(h)\) preserves total mass. It need not preserve nonnegative distributions.

**Theorem.** Every \(R_n(h)\) is entrywise nonnegative for every \(h\ge0\) if \(1\le n\le6\). For \(n=7\), the complete set of nonnegative steps is precisely
\[
\boxed{[0,\alpha_1]\;\cup\;[\alpha_2,\beta_1]\;\cup\;[\beta_2,\infty)}.
\]
Here \(\alpha_1<\alpha_2\) are the only positive real roots of
\[
\begin{aligned}
P(h)={}&7h^{10}+70h^9+315h^8+756h^7+945h^6+270h^5\\
&-810h^4-1080h^3-324h^2+216h+216,
\end{aligned}
\]
and \(\beta_1<\beta_2\) are the only positive real roots of
\[
\begin{aligned}
V(h)={}&h^{12}+18h^{11}+171h^{10}+780h^9+1755h^8+810h^7\\
&-5103h^6-12960h^5-12150h^4-1080h^3\\
&+8748h^2+7776h+3240.
\end{aligned}
\]
The four thresholds are approximately \(0.5844624537123\), \(0.8943001366705\), \(0.8952636961408\) and \(1.8409169033385\), respectively. The middle safe interval is narrow but nonempty: its endpoints are separated by approximately \(0.00096356\). Thus the smallest chain in this *homogeneous absorbing pure-birth family* with any positivity failure has two distinct failure bands, alternating with three nonnegative step intervals.

## Assumptions and scope

The generator is exactly the directed equal-rate absorbing cascade defined above. The step is a single application of the rational map \(R_n(h)\), not a product or adaptive method. Every \(h\ge0\) is allowed. Positivity means entrywise nonnegativity, equivalently nonnegative results for every nonnegative input vector. All statements are exact-arithmetic statements. Time is nondimensionalized so each transient departure rate equals one. For a common positive departure rate \(\lambda\), replace \(h\) by \(\lambda h\).

## Proof

Write \(E(h)=h^3+3h^2+6h+6\). The inverse defining \(R_n(h)\) exists for all \(h\ge0\): the eigenvalues of \(Q_n\) are \(0\) and \(-1\), and both \(1\) and \(E(h)/6\) are positive. Since \(\mathbf1^\top Q_n=0\), it follows that \(\mathbf1^\top R_n(h)=\mathbf1^\top\).

For the transient states, the generator is the nilpotent forward shift minus the identity. Therefore the transient entries of \(R_n(h)\) are the Taylor coefficients \(c_k(h)=[z^k]D_h(z)^{-1}\), where
\[
D_h(z)=1+h(1-z)+\frac{h^2}{2}(1-z)^2+\frac{h^3}{6}(1-z)^3.
\]
Let \(A=E/6\), \(B=-h-h^2-h^3/2\), \(C=h^2/2+h^3/2\), and \(D=-h^3/6\). Coefficient comparison gives the exact recurrence
\[
c_0=A^{-1},\quad c_k=-A^{-1}(Bc_{k-1}+Cc_{k-2}+Dc_{k-3}),
\]
where negative-index coefficients vanish. Starting at transient state \(j\), the probability-like entry arriving at the absorbing state equals
\[
T_{n-1-j}(h)=1-\sum_{k=0}^{n-2-j}c_k(h).
\]
Consequently for the seven-state chain, entrywise nonnegativity is equivalent to \(c_0,\dots,c_5\ge0\) and \(T_1,\dots,T_6\ge0\). The same criterion truncated at smaller indices covers every chain with at most six states.

The exact recurrence yields rational expressions for which \(c_0,\dots,c_4\) and \(T_1,\dots,T_4\) have numerators with strictly positive coefficients after extracting a positive monomial factor and have denominators that are powers of \(E(h)\). Thus all nine functions are strictly positive for every \(h>0\). The remaining three expressions are
\[
c_5(h)=\frac{18h^5P(h)}{E(h)^6},\qquad
T_5(h)=\frac{h^5U(h)}{E(h)^5},\qquad
T_6(h)=\frac{h^6V(h)}{E(h)^6},
\]
where
\[
\begin{aligned}
U(h)={}&h^{10}+15h^9+120h^8+450h^7+855h^6+495h^5\\
&-810h^4-1620h^3-540h^2+540h+648.
\end{aligned}
\]

For any real polynomial \(F\), apply the exact rational Sturm sequence \((F,F',\ldots)\), discarding zero terms when counting signs. The counts of sign variations at \(0\) and \(+\infty\) for \(P,U,V\), respectively, are
\[
(5,3),\qquad(5,5),\qquad(7,5).
\]
Hence \(P\) and \(V\) each have exactly two distinct positive real roots and \(U\) has none. Because \(U(0)=648>0\), \(U(h)>0\) for all \(h\ge0\). Exact opposite signs at the rational endpoints isolate the roots in the four intervals
\[
\begin{aligned}
\alpha_1&\in(0.584462453,0.584462454),\\
\alpha_2&\in(0.894300136,0.894300137),\\
\beta_1&\in(0.895263696,0.895263697),\\
\beta_2&\in(1.840916903,1.840916904).
\end{aligned}
\]
Thus \(\alpha_1<\alpha_2<\beta_1<\beta_2\) without relying on rounded numerical calculations. As \(P(0)=216>0\) and \(V(0)=3240>0\), their signs alternate across their two simple positive roots. The simultaneous conditions \(P(h)\ge0\) and \(V(h)\ge0\) give exactly the three intervals stated in the theorem. At \(h=0\), \(R_n(0)=I\) is nonnegative. For every \(n\le6\) no coefficient \(c_5\) or \(T_6\) occurs, proving all-step positivity in those dimensions. At \(n=7\), either one of these quantities becomes negative in its respective forbidden interval, proving sharpness inside this chain family.

## Verification

Run `python check.py` using Python 3.10+ and SymPy 1.12+. This standalone script reproduces the rational recurrence and the three displayed numerators, checks all nine positive coefficient-polynomial signs, computes the three Sturm variation pairs, checks rational sign-changing root brackets and their strict ordering, and independently forms and inverts six exact-rational seven-state step matrices. Its successful completion prints `VERIFICATION_OK`. The Sturm theorem and exact rational sign brackets, rather than a finite timestep sample, certify the conclusions for uncountably many positive steps. The script's independent matrix inverses check the correspondence between the scalar generating function and the actual matrix entries. No numerical root approximation is used in the proof.

## Relationship to prior work

The cubic inverse-Taylor rational function is classical and is not proposed as a new method. Fasi and Higham (2019) analyze exponential Padé and Taylor approximations and formulate a positivity conjecture for Taylor coefficients of reciprocal Padé denominators at the origin. A separate theorem establishes that every coefficient of the reciprocal cubic denominator at the *origin* is positive. This does not imply positivity of the *shifted* coefficients \([z^k]D_h(z)^{-1}\): the negative \(c_5(h)\) in the present theorem gives an explicit distinction. A published finite-graph classification for the same \([0/3]\) rational map covers simple, unweighted **undirected** graph Laplacians of at most six vertices and an undirected seven-path witness; it does not classify the **directed absorbing birth chain** or derive its three step-size windows. Blanes, Iserles, and Macnamara (2022) provide positivity-preserving integrator constructions for Markov-type systems, but their methods and positivity guarantee are different. Earlier studies of \([0/2]\) Padé and two-stage Radau IIA birth chains use different rational maps, so their thresholds do not imply the displayed ones.

Masood and Yousuf (2010) analyze positivity-preserving Padé schemes for an inverse heat problem. Their abstract was examined, but their complete article was not accessible; a specialized historical overlap cannot be conclusively ruled out. Neither noncoverage of inaccessible full text nor exhaustive historical priority is claimed.

## Limitations

The classification is for *one* third-order rational map and equal-rate, absorbing, unidirectional birth chains. It does not establish the minimal failing dimension among all Markov generators, graph Laplacians, asymmetric departure rates, or alternative integrators. It says nothing about the best practical integration step, global accuracy on nonlinear systems, or finite-precision numerical errors. Two algebraic positivity-loss mechanisms are identified; the intermediate recovery window is narrow and may be missed in coarse timestep studies. An external independent audit and complete historical-priority confirmation have not been performed.

## References

1. M. Fasi and N. J. Higham, *An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential*, SIAM Journal on Matrix Analysis and Applications 40 (2019), 1233–1256, DOI: https://doi.org/10.1137/18M1228876. Public preprint deposit dated 2019-06-19: https://eprints.maths.manchester.ac.uk/2721/.
2. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, ESAIM: M2AN 56 (2022), 1843–1870, DOI: https://doi.org/10.1051/m2an/2022042; open full text https://www.numdam.org/item/10.1051/m2an/2022042.pdf.
3. *Seven vertices are sharp for positivity loss of the cubic inverse-Taylor heat step*, published result https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-seven-vertices-are-sharp-for-positivity-loss-of-the-cubic-invers--808c1509a3bb.
4. *Complete coefficient positivity for cubic exponential Padé denominators*, published result https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-coefficient-positivity-for-cubic-exponential-pad-denomi--7756127900e3.
5. K. Masood and M. Yousuf, *Solution of the Initial Inverse Problems in the Heat Equation Using the Finite Difference Method with Positivity-Preserving Padé Schemes*, Numerical Heat Transfer Part A 57 (2010), 691–708. DOI: https://doi.org/10.1080/10407781003744763. Abstract examined; full paper not inspected.
