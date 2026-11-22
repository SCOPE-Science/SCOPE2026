# Sharp quartic Steinhaus modulus and unique Hilbert perturbations

## Finding

For a real Hilbert space \(H\) with real dimension at least two, define the quartic uniform Steinhaus modulus, for \(a>0\) and \(0<d<2\), by
\[
U_H^{(4)}(d;a)=\inf_{x,y\in S_H,\ \|x-y\|\ge d}\ \sup_{\|z\|\le a}
\big|\|x+z\|^4-\|y+z\|^4\big|.
\]
Set
\[
s=\sqrt{1-d^2/4},\quad P=1+a^2,\quad Q=2as,\quad
c=\frac{2Q}{P+\sqrt{P^2+8Q^2}}.
\]
Then the exact formula is
\[
\boxed{U_H^{(4)}(d;a)=4ad\sqrt{1-c^2}\,(P+Qc).}
\]
This number is independent of the dimension of \(H\), strictly increasing in \(d\), and the infimum is attained precisely by unit pairs at distance \(d\). For such a pair, let \(m=(x+y)/2\), \(v=(x-y)/2\), and \(e_m=m/\|m\|\), \(e_v=v/\|v\|\). All maximizing perturbations are exactly
\[
\boxed{z= a\big(c e_m\pm\sqrt{1-c^2}\,e_v\big).}
\]
The two signs give the two opposite orientations of the norm-power difference; in particular no component perpendicular to the real span of the pair can maximize it.

The optimal midpoint alignment \(c\) is invariant under \(a\mapsto1/a\), increases strictly for \(0<a<1\), and decreases strictly for \(a>1\). Moreover,
\[
U_H^{(4)}(d;a)=a^4 U_H^{(4)}(d;1/a),
\qquad
U_H^{(4)}(d;a)>4ad(1+a^2)\quad(0<d<2),
\]
and the boundary extension at \(d=2\) is \(U_H^{(4)}(2;a)=8a(1+a^2)\).

## Assumptions and scope

The inner product is real. All statements also hold for a complex Hilbert space considered as a real Hilbert space, so the complex dimension may be one. The radius \(a\) is strictly positive and the separation lies in \(0<d<2\); the displayed limit at \(d=2\) is the actual value for antipodal pairs. The modulus uses an absolute difference of fourth powers and the closed perturbation ball, exactly as in the powered modulus defined by Johnson and Kania [1].

## Proof

**Step 1 (orthogonal reduction).** Fix two unit vectors at separation \(2h\in(0,2)\). Put \(m=(x+y)/2\), \(v=(x-y)/2\), and \(s=\|m\|=\sqrt{1-h^2}\). The unit directions \(e_m=m/s\) and \(e_v=v/h\) are orthogonal. For a perturbation \(z=u e_m+w e_v+z_\perp\) of norm \(t\), subtracting and adding the squared norms gives
\[
\|x+z\|^2-\|y+z\|^2=4hw,
\qquad
\|x+z\|^2+\|y+z\|^2=2(1+t^2+2su).
\]
Consequently,
\[
\big|\|x+z\|^4-\|y+z\|^4\big|
=8h|w|(1+t^2+2su).
\]
The second factor is nonnegative because it is half a sum of squares. At fixed \(t\), the maximum is achieved with \(u\ge0\), \(z_\perp=0\), and \(|w|=\sqrt{t^2-u^2}\). Write \(u=tc\) with \(0\le c\le1\). The objective is
\[
8ht\sqrt{1-c^2}\,(1+t^2+2stc).
\]
For each \(c<1\) this increases strictly with \(t>0\), so a maximizing perturbation has \(t=a\).

**Step 2 (unique angular optimizer).** Write \(P=1+a^2\), \(Q=2as\) and \(M(Q)=\max_{0\le c\le1}\sqrt{1-c^2}(P+Qc)\). Its derivative has the sign of \(Q-Pc-2Qc^2\), which decreases strictly and has exactly one zero on \((0,1)\) for \(Q>0\). Solving the quadratic gives
\[
c=\frac{2Q}{P+\sqrt{P^2+8Q^2}}.
\]
The fixed-pair supremum is \(8ah\sqrt{1-c^2}(P+Qc)\), with exactly the two stated maximizing perturbations.

**Step 3 (separation monotonicity).** We prove that the fixed-pair optimum increases strictly with \(h\); this is essential because the definition takes an infimum over separations at least \(d\). Regard the maximizing \(c\) as a function of \(s=\sqrt{1-h^2}\). The stationary equation reads
\[
Pc=2as(1-2c^2).
\]
By differentiation at the unique maximizer (or the envelope theorem),
\[
\frac{d}{dh}\big[h M(2as)\big]
=\sqrt{1-c^2}\left[P+\frac{4a^2}{P}(1-2c^2)(2s^2-1)\right].
\]
Since \(0<s<1\), \(0<c<1/\sqrt2\), and \(P^2-4a^2=(a^2-1)^2\ge0\), the bracket is strictly greater than or equal to \(P-4a^2/P\ge0\), with the first comparison strict. Thus the fixed-pair supremum grows strictly with \(h\). Every separation \(d\in(0,2)\) is realized by unit vectors in a real Hilbert space of dimension at least two. Taking \(h=d/2\) proves the formula and the minimizing-pair classification.

**Step 4 (budget symmetry and endpoint).** The ratio \(Q/P=2as/(1+a^2)\) is invariant under \(a\mapsto1/a\), grows strictly to \(a=1\), then decreases. Since the unique solution \(c\) increases strictly with \(Q/P\), this proves the alignment statement. Under reciprocal budget, both \(P\) and \(Q\) scale by \(a^2\), giving the exact quartic reciprocity. If \(0<d<2\), then \(Q>0\), so the maximum exceeds its value at \(c=0\), giving strict inequality. At \(d=2\), \(s=Q=c=0\), and direct inspection of antipodal pairs gives \(8a(1+a^2)\).

## Verification

The proof is analytic. A standalone Python 3 script, `checker.py`, uses only the standard library to check the formula, reciprocal budget identity, strict separation monotonicity, equality configurations, and randomly chosen two- and three-dimensional perturbations against the predicted supremum. It performs 88,542 finite assertions and reports `QUARTIC_STEINHAUS_HILBERT_FINITE_CHECK_OK 88542`. These finite checks diagnose algebra and normalization; they are not substitutes for the proof of all radii, separations or dimensions.

## Relationship to prior work

Johnson and Kania [1, Definition (3)-(4)] introduce powered uniform Steinhaus moduli and calculate \(U_H^{(2)}(d;a)=2ad\) in their Proposition 1.4. That quadratic identity does not by itself give the quartic value: the fourth-power difference multiplies the squared-norm difference by a second factor depending on the *same* perturbation, making the angular optimization and outer separation minimization coupled. The result here solves that first nonlinear even-power instance exactly. Kania and Kochanek [2] establish the earlier qualitative Steinhaus geometry, without a powered numerical modulus. Published exact small-radius estimates for the ordinary modulus on other Banach-space constructions concern a distinct exponent and geometry [3,4].

## Limitations

The formula does not cover non-Hilbert norms, general powers other than four, or the one-dimensional **real** Hilbert space. The finite checker only tests selected cases. This result has received no independent mathematical audit; its publication priority beyond the inspected sources remains subject to further literature discovery.

## References

1. W. B. Johnson and T. Kania, *Uniform Property (S)*, arXiv:2602.09106 (first public version 9 February 2026), particularly the definitions and Proposition 1.4, https://arxiv.org/abs/2602.09106.
2. T. Kania and T. Kochanek, *Steinhaus' lattice-point problem for Banach spaces*, arXiv:1302.6443 (first public version 26 February 2013), https://arxiv.org/abs/1302.6443.
3. *Sharp quadratic Steinhaus modulus of a scalar–Hilbert one-sum*, publicly indexed mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-quadratic-steinhaus-modulus-of-a-scalar-hilbert-one-sum--102221e3c81d.
4. *Sharp small-radius Steinhaus modulus of real \(\ell_p\) for \(p\ge2\)*, publicly indexed mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-small-radius-steinhaus-modulus-of-real-ell-p-for-p-ge2--072a2f172b7d.
