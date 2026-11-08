# A unique majority-accuracy trough under alternating independent expertise

## Finding

For every \(p,q\) satisfying \(1/2<p<1\) and \(0<q<1/2\), construct a nested sequence of odd juries: jury \(m\), for each integer \(m\ge0\), has \(m+1\) independent voters who are individually correct with probability \(p\), and \(m\) independent voters correct with probability \(q\). All votes are binary, their correctness events are mutually independent, and the jury uses unweighted strict majority. Let \(J_m\) be its probability of choosing the correct alternative. Then:

1. If \(p+q\le1\), \(J_{m+1}<J_m\) for **every** \(m\ge0\). Its limit is \(0\) if \(p+q<1\), and \(1/2\) if \(p+q=1\).
2. If \(p+q>1\), \(J_1<J_0\), but the successive differences \(J_{m+1}-J_m\) change sign **exactly once**, from negative to positive, possibly passing through zero at one index. Thus the sequence has one trough (at one or two adjacent committee sizes) and converges to \(1\). No second reversal is possible. The last negative increment may occur arbitrarily late as \(q\downarrow1-p\) for any fixed \(p>1/2\).

The result is sharp both at the average-pair-competence boundary \(p+q=1\) and in the number of allowed trend changes. It concerns a prescribed deterministic sequence of juries; it is not a random-subcommittee result.

## Assumptions and scope

Set \(a=pq\), \(b=(1-p)(1-q)\), and \(c=p(1-q)+(1-p)q\). Each added \((p,q)\)-pair contributes respectively \(+2, -2, 0\) to the correct-minus-incorrect vote margin, with probabilities \(a,b,c\). Write \(Z_m\) for a sum of \(m\) independent steps in \(\{-1,0,1\}\) with corresponding probabilities \(b,c,a\), and let
\[
 t_m=\Pr(Z_m=0),\qquad v_m=\Pr(Z_m=1),\qquad R_m=v_m/t_m.
\]
All denominators in this report are strictly positive. An unweighted majority has no ties for these odd jury sizes. No strategic voting, information exchange, conditional common shock, or endogenous recruitment is assumed.

## Proof

**1. Exact increment identity.** Couple jury \(m+1\) to jury \(m\) by adding one new independent \(p\)-voter and one independent \(q\)-voter. A strict majority changes only if the old correct-minus-incorrect margin is \(+1\), followed by two incorrect newcomers (probability \(b\)), or if the old margin is \(-1\), followed by two correct newcomers (probability \(a\)). Thus
\[
J_{m+1}-J_m=a\Pr(W_m=-1)-b\Pr(W_m=1),
\]
where \(W_m\) is the old margin. The first voter has correctness probability \(p\), so \(W_m=\pm1+2Z_m\). The walk has detailed-balance coefficient identity \(a\Pr(Z_m=-1)=b\Pr(Z_m=1)\), obtained by swapping every up and down step. Substitution gives the **exact all-size formula**
\[
\boxed{J_{m+1}-J_m=p(1-p)(2q-1)t_m+b(2p-1)v_m.}
\tag{1}
\]
In particular \(t_0=1,v_0=0\), hence \(J_1-J_0=p(1-p)(2q-1)<0\).

**2. Strictly increasing return-to-neighbor ratio.** Since \(p>q\), the strict arithmetic-geometric-mean inequality gives \(c>2\sqrt{ab}\). Put \(L(\theta)=c+2\sqrt{ab}\cos\theta>0\). Fourier inversion of the trinomial walk yields
\[
t_m=\frac1{2\pi}\int_{-\pi}^{\pi}L(\theta)^m\,d\theta,\qquad
v_m=\sqrt{\frac ab}\,\frac1{2\pi}\int_{-\pi}^{\pi}\cos\theta\,L(\theta)^m\,d\theta.
\]
Let \(\mu_m\) be the probability law with density proportional to \(L(\theta)^m\) on \([-\pi,\pi]\). Then \(R_m=\sqrt{a/b}\,\mathbb E_{\mu_m}[\cos\theta]\), and reweighting by \(L\) proves
\[
R_{m+1}-R_m=\sqrt{\frac ab}\;\frac{2\sqrt{ab}\,\operatorname{Var}_{\mu_m}(\cos\theta)}{\mathbb E_{\mu_m}[L]}>0.
\tag{2}
\]
Since \(L\) is continuous, positive, and has its unique maximum on the circle at \(0\), its normalized \(m\)-th powers concentrate at \(0\). Therefore
\[
\boxed{R_0=0,\quad R_m\nearrow\sqrt{a/b}\quad(m\to\infty).}
\tag{3}
\]
No finite numerical enumeration enters this argument.

**3. Sharp phase boundary and one change.** Dividing (1) by \(t_m>0\) shows its sign equals that of
\[
h_m=p(1-p)(2q-1)+b(2p-1)R_m.
\]
By (2), \(h_m\) is strictly increasing. It starts strictly negative and tends to
\[
h_\infty=(2p-1)\sqrt{ab}-(1-2q)p(1-p).
\]
Both terms on the right are positive before subtraction, and the exact identity
\[
(2p-1)^2ab-(1-2q)^2p^2(1-p)^2
=p(1-p)(p-q)(p+q-1)
\]
shows \(\operatorname{sgn}(h_\infty)=\operatorname{sgn}(p+q-1)\). If \(p+q\le1\), then \(h_m<h_\infty\le0\) for all finite \(m\), proving strict decrease. Otherwise \(h_m\) crosses zero once as a strictly increasing sequence, possibly at a single integer index. More explicitly, the change is governed without approximation by
\[
R_m\gtrless\frac{p(1-2q)}{(1-q)(2p-1)}.
\tag{4}
\]
The direction is negative below this threshold and positive above it. At most one \(m\) attains equality.

**4. Limits and arbitrarily delayed recovery.** By the strong law of large numbers, after \(m\) pairs the average correct-vote proportion converges to \((p+q)/2\), establishing the limits \(0\) and \(1\) in the strict sub- and supercritical cases. When \(p+q=1\), the nondegenerate zero-drift trinomial walk obeys a central limit theorem; the initial one-vote margin becomes negligible, so \(J_m\to1/2\). Finally, for any fixed integer \(M\), at \(q=1-p\) all of \(h_0,\dots,h_M\) are strictly negative; continuity in \(q\) preserves those inequalities for \(q>1-p\) sufficiently close to \(1-p\). Yet the sign becomes positive eventually for every \(q>1-p\), proving there is no universal bound on the trough index.

**5. Exact witness.** Choose \(p=9/10\), \(q=2/5\), with \(p+q=13/10\). Direct binomial enumeration gives
\[
J_0=\frac9{10},\qquad J_1=\frac{441}{500},\qquad
J_2=\frac{22221}{25000},
\]
so majority accuracy falls from \(90\%\) to \(88.2\%\) as the jury grows from one to three, then rises to \(88.884\%\) at five. Here \(R_1=18/29\) exceeds the exact sign-change threshold \(3/8\), so \(J_1\) is the unique minimum among **all** the odd jury sizes.

## Verification

Run `python3 verify.py` beside this file. The standalone checker uses only the Python standard library and performs exact rational cross-checks of (1), the walk detailed balance identity, strict finite-index ratio increase, and the three-state witness, using two independent computations of jury accuracy. The script reports \(840\) exact assertions. Symbolic proof steps (Fourier inversion, variance positivity, and the limiting argument) are independently supplied above and are not inferred from a finite computation.

## Relationship to prior work

Berend and Sapir's *Monotonicity in Condorcet Jury Theorem* (2005) proves monotonicity for randomly chosen subcommittees where every individual competence is at least \(1/2\). Both restrictions matter: this theorem deliberately recruits a voter with probability \(q<1/2\) at each step and considers prescribed nested juries, not random subcommittees. Their author's manuscript theorem assumptions and random-subcommittee definition were compared, not just its abstract.

Hartmann and Rafiee Rad's *Voting, deliberation and truth* (first online November 29, 2016), Sect. 2.1, provides the Poisson-binomial majority formula and states a general heterogeneous monotonicity claim from average competence above \(1/2\). The explicit three-voter example here shows that unqualified finite-size monotonicity cannot follow from the average alone; their article's main analyzed object is deliberation and does not establish the sharp one-trough law. Berend and Sapir (2007) address dependent heterogeneous *random* committees and do not establish the deterministic alternation theorem in the material accessible here. Liu's 2026 exchangeable-mixture voting classification concerns exchangeable repeated correctness indicators and its de Finetti reduction does not apply to fixed alternating voter types. Related strategic-voting work studies different mechanisms.

## Limitations

The result is for a fixed, deterministic, alternating two-type recruitment policy with independent binary correctness indicators. It does not give an optimum among all ways of recruiting voters or among weighted rules, and it does not assert that the new voters should ever be recruited in applications. The finite verifier cannot establish the all-size result by itself. The consulted literature supports a best-knowledge originality assessment, not guaranteed historical priority; some plausible historical journal full texts were not accessible in entirety, particularly the 2007 dependent-jury article. The equality-case central-limit step relies on a positive nonzero pair-step variance, guaranteed by the strict parameter ranges.

## References

1. D. Berend and L. Sapir, *Monotonicity in Condorcet Jury Theorem*, Social Choice and Welfare 24 (2005), 83–92. https://doi.org/10.1007/s00355-003-0293-z . Public publication date verified as 2005-02-01.
2. D. Berend and L. Sapir, *Monotonicity in Condorcet's Jury Theorem with Dependent Voters*, Social Choice and Welfare 28 (2007), 507–528. https://doi.org/10.1007/s00355-006-0179-y .
3. S. Hartmann and S. Rafiee Rad, *Voting, deliberation and truth*, Synthese (online 2016-11-29; journal volume 2018). https://doi.org/10.1007/s11229-016-1268-9 .
4. Y. Liu, *When Can Voting Help, Hurt, or Change Course? Exact Structure of Binary Test-Time Aggregation*, arXiv:2605.05592 (2026). https://arxiv.org/abs/2605.05592 .
5. *Jury Theorems*, Stanford Encyclopedia of Philosophy (first published 2021-11-17). https://plato.stanford.edu/entries/jury-theorems/ .
