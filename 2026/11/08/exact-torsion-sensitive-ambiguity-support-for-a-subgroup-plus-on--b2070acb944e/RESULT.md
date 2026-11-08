# Exact torsion-sensitive ambiguity support for a subgroup plus one impulse

## Finding

Let \(G\) be a finite abelian group of order \(N\), let \(H<G\) be a proper subgroup of order \(h\ge2\), and set \(q=N/h\). Fix \(y\in G\setminus H\), write \(r\ge2\) for the order of \(y+H\) in \(G/H\), and let \(z\in\mathbb C\setminus\{0\}\). Define \(f=\mathbf{1}_H+z\mathbf{1}_{\{y\}}\). For \(x\in G\) and \(\chi\in\widehat G\), use the unnormalized ambiguity transform
\[
 A_f(x,\chi)=\sum_{t\in G}f(t)\overline{f(t-x)}\,\overline{\chi(t)}.
\]
Let \(S(f)\) be the number of nonzero entries of \(A_f\), put \(B=N+(h-1)q\), and let \(C=y+H\). Write \(o(x)\) for the additive order of \(x\in G\). Set \(\zeta=-\overline z/z\), and let \(d\) be its multiplicative order if \(\zeta\) is a root of unity, and \(d=\infty\) otherwise; the notation \(d\mid o(x)\) is false for \(d=\infty\).

**Exact support law.** When \(r>2\),
\[
 S(f)=B+2hN-\mathbf{1}_{\{2\mid r,\ |z|^2=h\}}\frac qr.
\]
When \(r=2\),
\[
 \boxed{S(f)=B+hN-\mathbf{1}_{\{|z|^2=h\}}\frac q2
 -N\sum_{\substack{x\in C\\d\mid o(x)}}\frac1{o(x)}.}
\]
All these are exact integers, including for composite and noncyclic \(G\).

**Complete attainable support and optimizing phases.** If \(r>2\), the support count is independent of \(z\) when \(r\) is odd, and has exactly the two displayed levels when \(r\) is even; the smaller occurs exactly when \(|z|^2=h\). If \(r=2\), let \(E\) denote the exponent of \(G\) and let \(L(d)=N\sum_{x\in C,\ d\mid o(x)}1/o(x)\), with \(L(\infty)=0\). The complete attainable set is
\[
 \boxed{\big\{B+hN-L(d)-\varepsilon q/2:\ d\mid E\ \text{or}\ d=\infty,\quad\varepsilon\in\{0,1\}\big\}.}
\]
Every listed value is realized. The smallest count is
\[
 \boxed{S_{\min}=B+hN-\frac q2-N\sum_{x\in C}\frac1{o(x)}.}
\]
Writing \(g=\gcd\{o(x):x\in C\}\), equality \(S(f)=S_{\min}\) holds exactly when \(|z|^2=h\) and \(d\mid g\). In particular \(g\ge2\), so both real and purely imaginary impulses of magnitude \(\sqrt h\) are optimal.

**Uniform sharp gap and a torsion test.** For every such \(G,H,y,z\),
\[
 \boxed{S(f)\ge N+\left(h-\frac32\right)q+\frac{hN}{2}.}
\]
Equality holds precisely when \(H\) has exponent two, \(2y=0\), and \(z\in\{\sqrt h,-\sqrt h,i\sqrt h,-i\sqrt h\}\). Thus the bound is attained, for example, on every elementary binary group of dimension at least two with a nontrivial proper \(H\). More strongly, the observed count detects the quotient order-two regime without knowing the impulse: if \(r=2\), then \(S(f)\le B+hN\), whereas if \(r>2\), then \(S(f)\ge B+2hN-q/4>B+hN\).

## Assumptions and scope

All groups are finite and abelian; character values have unit modulus and every character of a subgroup extends to \(G\). The transform is unnormalized, but multiplying it by any nonzero constant does not change its support. The background is the constant indicator of a proper subgroup, and exactly one nonzero perturbation is added at a point outside it. The inequality and all equality statements are assertions about exact zeros, not numerical thresholds. There is no assertion for a perturbation supported inside \(H\), for more than one added point, or for nonabelian groups.

## Proof

Fix a time shift \(x\). There are four disjoint kinds of nonzero products \(f(t)\overline{f(t-x)}\): subgroup--subgroup pairs, the impulse self-pair, and two possible cross-pairs. Direct expansion gives
\[
 \begin{aligned}
 A_f(x,\chi)={}&\mathbf1_{H}(x)\sum_{t\in H}\overline{\chi(t)}
 +|z|^2\mathbf1_{\{0\}}(x)\overline{\chi(y)}\\
 &+z\mathbf1_{C}(x)\overline{\chi(y)}
 +\overline z\mathbf1_{-C}(x)\overline{\chi(y+x)}.
 \end{aligned}
\]
(The last term has \(y+x\in H\) whenever \(x\in-C\).) Orthogonality of characters makes the subgroup sum equal to \(h\) when \(\chi\) is trivial on \(H\), and zero otherwise. The annihilator \(H^\perp\) has size \(q\).

For every \(x\in H\setminus\{0\}\), exactly \(q\) frequencies survive, contributing \((h-1)q\) entries. At shift zero, the Fourier transform of \(\mathbf1_H+|z|^2\mathbf1_{\{y\}}\) has \(N\) nonzero entries except possibly for the characters in \(H^\perp\) satisfying \(\chi(y)=-1\) and \(|z|^2=h\). The evaluation map \(H^\perp\to\mu_r\), \(\chi\mapsto\chi(y)\), is surjective with fibers of size \(q/r\). Thus exactly \(q/r\) zero-delay entries disappear when \(r\) is even and \(|z|^2=h\), and none otherwise. This proves the term \(B\) and its correction.

If \(r>2\), then \(C\) and \(-C\) are disjoint, each of size \(h\). Each cross-pair shift contributes a single nonzero character multiple of \(z\) or \(\bar z\) at every one of the \(N\) frequencies. All remaining shifts vanish. This gives \(2hN\) cross entries.

If \(r=2\), then \(C=-C\). For any \(x\in C\), both cross terms occur and factor as
\[
 A_f(x,\chi)=\overline{\chi(y)}\big(z+\overline z\,\overline{\chi(x)}\big).
\]
They cancel exactly when \(\chi(x)=-\overline z/z=\zeta\). For a fixed \(x\), character evaluation \(\widehat G\to\mu_{o(x)}\) is onto with fibers of cardinality \(N/o(x)\). Hence the number of zeros in that shift row is \(N/o(x)\) if \(d\mid o(x)\), and zero otherwise. Adding over \(C\) proves the claimed formula.

Any positive amplitude can be chosen independently of the phase. Every complex unit \(\zeta\) is realized as \(-\bar z/z\) by some nonzero \(z\), so every root order dividing \(E\), and the non-root case, is attainable. All subtracted summands are nonnegative, and each is individually maximized by choosing \(d=1\); the zero-delay subtraction is maximized by \(|z|^2=h\). No larger subtraction is possible. Equality in the cross-row maximum requires inclusion of every \(x\in C\), precisely \(d\mid g\). Since \(r=2\), every \(o(x)\) is even and \(g\ge2\). This proves all optimizer statements.

In the order-two case, \(o(x)\ge2\) for every \(x\in C\), so \(\sum_{x\in C}1/o(x)\le h/2\). In the other case the support is larger than this lower bound because \(hN>q/4\). Consequently
\[
 S(f)\ge B+\frac{hN}{2}-\frac q2=N+\left(h-\frac32\right)q+\frac{hN}{2}.
\]
Equality forces \(r=2\), every \(x\in C\) to have order two, \(|z|^2=h\), and \(d\mid2\). All elements of \(C\) have order two exactly when \(2y=0\) and \(2H=0\). The condition \(d\mid2\) means \(-\bar z/z=\pm1\), equivalently \(z\) real or purely imaginary. The converse is immediate. Finally, the two intervals in the torsion test follow from the formulas, using \(r\ge4\) in the even \(r>2\) case. Their gap is positive because \(h\ge2\).

## Verification

The companion `check_subgroup_spike.py` computes exact ambiguity coefficients in cyclotomic integer quotient rings, rather than using floating-point near-zero thresholds. It exhaustively tests 80 exact checks on 11 cyclic and product-group configurations, with Gaussian-integer impulses plus two exact square-root and one primitive-eighth-root cases, and independently matches each exact count to the stated group-theoretic formula. A separate symbolic check on \(G=(\mathbb Z/2\mathbb Z)^2\), \(|H|=2\), verifies the sharp equality count \(9\) for both \(z=\sqrt2\) and \(z=i\sqrt2\). These finite checks do not establish the arbitrary-group assertion; the proof above does.

For example, on \(G=\mathbb Z/8\mathbb Z\) with \(H=2\mathbb Z/8\mathbb Z\) and \(y=1\), the formula uses \(N=8,h=4,q=2,r=2\), with four elements of order eight in \(C\). It predicts minimal support \(14+32-1-4=41\), attained by \(z=\pm2\) or \(z=\pm2i\). 

## Relationship to prior work

Nicola (2023, arXiv:2305.02738) classifies the exact minimizers of finite and locally compact abelian-group self-ambiguity support, including subgroup indicators (Theorem 4.5). Nicola (2022, arXiv:2204.14176) proves the finite-cyclic equality classification and a finite-abelian lower-bound statement (Theorem 1.2 and Proposition 4.1). Neither examined theorem determines the support after a nonzero off-subgroup impulse; the claims here are about the exact spectrum of counts, the order-two quotient transition, and all optimal impulse phases, rather than identifying the original minimum-support waveforms. Relevant current mathematical-record searches for subgroup-plus-impulse ambiguity supports, phase cancellation, and exact coset counts did not return an identical statement. This is not a proof of historical priority: an equivalent calculation may occur in specialized signal-processing references under different terminology.

## Limitations

The theorem is about literal zeros of the finite self-ambiguity function, not near-zeros or noise-stable concentration. The complex amplitude is unrestricted and the subgroup is constant-valued. The exact counts are not a global uncertainty principle over every signal of the same support size. The result is self-contained but relies on classical finite-character orthogonality and can in principle be reformulated using difference-set incidence; the possibility of an unlocated equivalent prior formulation remains an originality risk.

## References

1. F. Nicola, *Maximally localized Gabor orthonormal bases on locally compact Abelian groups*, arXiv:2305.02738 (first public version 2023-05-04), especially Section 2.2 and Theorem 4.5. https://arxiv.org/abs/2305.02738
2. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176 (first public version 2022-04-29), especially Theorem 1.2 and Section 4.2. https://arxiv.org/abs/2204.14176
3. G. E. Pfander, *Gabor frames in finite dimensions*, in *Finite Frames*, Applied and Numerical Harmonic Analysis, Birkhäuser, 2013. https://doi.org/10.1007/978-0-8176-8373-3_6
