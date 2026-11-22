# Sharp maximal periodic-penetration delays and their Lambert-W density law in modular gap shifts

## Finding

For every integer \(m\ge 3\), let \(X_m\) be the two-sided binary shift in which the finite number of zeros between any two consecutive ones is divisible by \(m\). For an admissible word \(w\), let \(\eta_m(w)\) be the least period of a periodic configuration of \(X_m\) containing \(w\) at a prescribed origin. Then for every \(n\ge2\),
\[
\max_{w\in\mathcal L_n(X_m)}\eta_m(w)=n+m-1.
\]
Write \(D_m(n)\) for the number of length-\(n\) words realizing this maximum and \(U_m(z)=\frac12\sum_{n\ge2}D_m(n)z^n\). The complete all-length count obeys
\[
\boxed{(1-z-z^m)U_m(z)+z^{m-1}U_m(z^2)=z^2.}
\]
Let \(r_m\) be the unique root in \((0,1)\) of \(1-r_m-r_m^m=0\), and put \(\delta_m=1-r_m=r_m^m\). The fraction of uniformly sampled length-\(n\) admissible words with the maximum penetration delay converges to the positive number
\[
\boxed{p_m=\delta_m^2\left(1+\frac{\delta_m^2}{r_m^6}U_m(r_m^4)\right)>\delta_m^2.}
\]
As \(m\to\infty\),
\[
 p_m=\delta_m^2\left(1+\frac{\delta_m}{4}+O(\delta_m^2)\right)
 \sim\frac{W(m)^2}{m^2},
\]
where \(W\) is the positive Lambert function, defined by \(W(t)e^{W(t)}=t\). In particular, the worst additive delay grows linearly in \(m\), but the fraction attaining that delay decays on the explicitly identified squared-logarithmic scale.

## Assumptions and scope

All parameters \(m\) are integers at least three, all word lengths \(n\) are integers at least two, and words are equally weighted within the length-\(n\) language \(\mathcal L_n(X_m)\). A word without a one belongs to the language, and its penetration period is one. The shift \(X_m\) contains the all-zero configuration and consists of limits of concatenations of the loops \(10^{jm}\) for \(j\ge0\). It is a positive-entropy, mixing, strictly sofic shift for \(m\ge2\), because its allowed-gap set is infinite and eventually periodic but its forbidden-gap language is unbounded. No claim is made about other gap sets or general finite-type systems. A *border* of a finite word is a nonempty proper common prefix and suffix; *unbordered* means having no border.

## Proof

**1. Periodic closure and the sharp upper bound.** Suppose \(w\) has at least one one, with \(a\) initial zeros, \(b\) terminal zeros and all interior zero gaps divisible by \(m\). Appending the unique \(c\in\{0,1,\ldots,m-1\}\) satisfying \(a+b+c\equiv0\pmod m\) makes \((w0^c)^\infty\) an allowed periodic sequence. Thus \(\eta_m(w)\le n+m-1\). The word \(1^{n-1}0\) is admissible and unbordered, with \(a+b=1\), so it attains the upper bound by the next argument.

**2. Exact maximal-delay characterization.** If \(a+b\equiv1\pmod m\), no cyclic extension of \(w\) with period \(p=n+j\), \(0\le j\le m-2\), exists: an extension can append \(t\) ones with \(0\le t\le j\), giving \(1+j-t\) zeros modulo \(m\), an integer between one and \(m-1\). Any allowed cyclic sequence containing a one has a total zero count divisible by \(m\). If \(a+b\not\equiv1\), the closure in step 1 uses at most \(m-2\) zeros.

Suppose next that \(a+b\equiv1\pmod m\) and \(w\) is bordered. If its two endpoints are zero, its shortest border is the single zero; deleting its final zero gives a prefix \(u\) whose cyclic closure has exterior zero gap \(a+b-1\), divisible by \(m\), hence an admissible period \(n-1\). Otherwise its endpoints differ. Let \(v\) be its shortest nonempty border, of length \(k\). Then \(v\) is unbordered and \(k\le n/2\); write \(w=uv\), with \(|u|=n-k\). The cyclic repetition of \(u\) is admissible: all its internal gaps already occur in \(w\), while the gap across the boundary of \(u\) occurs in \(w\) between its last one inside \(u\) and the first one in its appended copy of \(v\). This copy has the same initial position of a one as the prefix \(v\subset u\). Hence \(\eta_m(w)\le n-k<n\). (For an all-zero word, period one suffices.) Conversely, an unbordered word has no possible period shorter than \(n\). Therefore a word has maximal delay \(n+m-1\) precisely when it is unbordered and the sum of its two exterior zero runs is congruent to one modulo \(m\).

An unbordered binary word of length at least two has different endpoint symbols. Such maximal-delay words therefore consist of two reversed equally numerous classes. Let \(u_{m,n}\) count the class that starts with one and ends with zero; its trailing zero run is congruent to one modulo \(m\), and \(D_m(n)=2u_{m,n}\).

**3. A unique shortest-border decomposition.** The generating function for *all* admissible words starting in one and ending in a zero run of length congruent to one modulo \(m\) is
\[
A_m(z)=\frac{z^2}{1-z-z^m}.
\]
Indeed, the word begins with one, may contain any number of repeated blocks \(0^{jm}1\), and ends in \(0^{1+jm}\). Every bordered such word has a unique shortest border \(v\), which is an unbordered member of the same oriented class; its two copies are nonoverlapping. The intervening word of length \(t\) must drive the zero-run congruence state from one to zero. The finite cyclic renewal automaton has transition \(0\) advancing the state by one modulo \(m\), and transition \(1\) permitted only at state zero and returning to state zero. Its state-one-to-zero path generating function is
\[
H_m(z)=\frac{z^{m-1}}{1-z-z^m}.
\]
Thus every bordered word is uniquely \(vsv\) with \(v\) from the counted unbordered class and \(s\) a state-one-to-zero path. Consequently \(A_m(z)=U_m(z)+H_m(z)U_m(z^2)\), proving the displayed exact Mahler equation for all coefficients.

**4. The language and its dominant singularity.** Every admissible word is either all zeros or has arbitrary leading and trailing zero runs around a nonempty concatenation of ones with between-one gaps divisible by \(m\). Hence
\[
L_m(z):=\sum_{n\ge0}|\mathcal L_n(X_m)|z^n
 =\frac1{1-z}+\frac{z(1-z^m)}{(1-z)^2(1-z-z^m)}.
\]
For \(f_m(z)=1-z-z^m\), the root \(r_m\) is simple and is its unique zero on \(|z|=r_m\): equality in \(|z+z^m|\le |z|+|z|^m\) requires the positive real solution. The recurrence gives analytic continuation
\[
U_m(z)=\frac{z^2-z^{m-1}U_m(z^2)}{f_m(z)}
\]
through a disc strictly larger than \(|z|<r_m\), apart from finitely many poles. Indeed, \(U_m(z)\le A_m(z)\) coefficientwise, and
\[
0<r_m^{m-1}U_m(r_m^2)
 \le r_m^{m-1}\frac{r_m^4}{1-r_m^2-r_m^{2m}}=\frac{r_m^2}{2}.
\]
The pole at \(r_m\) is therefore simple and noncancelling. Standard coefficient transfer for these rational singular parts yields the existence of \(p_m=\lim_{n\to\infty}D_m(n)/|\mathcal L_n(X_m)|\), with
\[
 p_m=2\delta_m^2\bigl(1-r_m^{m-3}U_m(r_m^2)\bigr).
\]
Substituting the Mahler equation at \(r_m^2\), using \(1-r_m^2-r_m^{2m}=2r_m\delta_m\), simplifies this to
\[
 p_m=\delta_m^2\left(1+\delta_m^2 r_m^{-6}U_m(r_m^4)\right).
\]
In particular it is positive, and for fixed \(m\) the convergence is exponentially fast because all other relevant singularities are separated from \(r_m\).

**5. Large-modulus asymptotics.** The root relation \(\delta_m=(1-\delta_m)^m\) implies \(\delta_m\to0\) and \(m\delta_m^2\to0\). Expanding \(\log\delta_m=m\log(1-\delta_m)\) gives \(m\delta_m\sim W(m)\). Also,
\[
 1-r_m^4-r_m^{4m}=4\delta_m+O(\delta_m^2),\qquad
 U_m(r_m^4)=\frac{r_m^8}{1-r_m^4-r_m^{4m}}+O(\delta_m^2)
 =\frac1{4\delta_m}+O(1).
\]
For the displayed error estimate, the discarded term is bounded by \(r_m^{4(m-1)}A_m(r_m^8)/(1-r_m^4-r_m^{4m})=O(\delta_m^2)\). Substitution into step 4 gives \(p_m=\delta_m^2(1+\delta_m/4+O(\delta_m^2))\), then \(p_m\sim W(m)^2/m^2\).

## Verification

The standalone standard-library program `checks/verify.py` independently enumerates admissible words and determines their shortest admissible cyclic periods (including the extra appended symbols): 10,260 admissible words across moduli two through six, through lengths 15, 14, 13, 12 and 11 respectively. It separately tests the unbordered-word characterization and the exact all-length recurrence through coefficient 300 for each modulus. Arbitrary-precision arithmetic checks two independent formulas for the limiting density at moduli two through five. All checks passed. These finite calculations corroborate but do not replace the all-length proof. In particular, for the new moduli
\[
(p_3,p_4,p_5)\approx(0.1070346578975121,\;0.0801050893611969,\;0.0631438074423085).
\]
Run with `python3 checks/verify.py` from the package root.

## Relationship to prior work

The local periodic penetration invariant is motivated by Pannipitiya's 2026 dynamical-systems framework, which treats periodic penetration and return statistics and discusses finite-type shifts. Climenhaga's account gives the classical entropy-root equation for general gap shifts; the entropy root here is therefore not claimed new. Holub and Shallit count borders and periods of uniformly random unconstrained words, rather than moduli-constrained periodic completions. A previous golden-mean cylinder calculation has a coincident modulus-two generating recurrence and limiting constant; those are not presented as new, and the present claim is the universal strictly-sofic modular-gap delay law for \(m\ge3\), its exact all-length recurrence and the varying-modulus asymptotic. The full Pannipitiya preprint, especially its Section 2.4 upper bound for mixing finite-type shifts, does not evaluate the moduli-constrained strictly sofic cylinder counts. Unindexed historical priority remains possible.

## Limitations

The result concerns *maximal* periodic-penetration delays for fixed cylinder length and the fraction of words attaining them; it does not classify all smaller penetration times or prove a corresponding law for arbitrary allowed-gap sets. The limiting proportions are for uniform counting on word languages, not for the entropy-maximizing measure sampled with its natural cylinder weights. The asymptotic is as the gap modulus tends to infinity *after* taking long-word limits. Independent audit has not been performed.

## References

1. Diyath Nelaka Pannipitiya, *Local Periodic Orbit Penetration in Dynamical Systems*, arXiv:2611.13416v1, submitted 10 November 2026 UTC, https://arxiv.org/abs/2611.13416.
2. Vaughn Climenhaga, *Entropy of S-gap shifts*, 8 September 2014, https://vaughnclimenhaga.wordpress.com/2014/09/08/entropy-of-s-gap-shifts/.
3. Stepan Holub and Jeffrey Shallit, *Periods and Borders of Random Words*, STACS 2016, DOI 10.4230/LIPIcs.STACS.2016.44, https://doi.org/10.4230/LIPIcs.STACS.2016.44.
