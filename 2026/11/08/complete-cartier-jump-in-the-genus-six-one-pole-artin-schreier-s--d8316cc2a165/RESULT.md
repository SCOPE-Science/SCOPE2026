# Complete Cartier jump in the genus-six one-pole Artin–Schreier stratum

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). Every connected Artin–Schreier cover of \(\mathbf P^1_k\) of genus \(6\) and \(3\)-rank zero admits a model
\[
C_{a,b,c}:\qquad y^3-y=x^7+a x^5+b x^4+c x^2,\qquad a,b,c\in k,
\]
where \(C_{a,b,c}\) denotes the **smooth projective model** of this affine equation. For every triple the geometric genus is \(6\), the \(3\)-rank is zero, and the ranks of the Cartier operator \(\mathcal C\) and its iterates on regular differentials are exactly
\[
\begin{array}{c|c|c|c}
\text{parameter}&(\operatorname{rk}\mathcal C^0,\operatorname{rk}\mathcal C,\operatorname{rk}\mathcal C^2,\operatorname{rk}\mathcal C^3)&a(C)&\text{nilpotence index}\\
 a=0&(6,2,1,0)&4&3\\
 a\ne0&(6,3,1,0)&3&3.
\end{array}
\]
In particular, the entire \(3\)-rank-zero Artin–Schreier genus-six locus has **exactly** the two \(a\)-numbers \(3\) and \(4\); the jump is precisely the hyperplane \(a=0\) in the standard three-parameter normal-form space. Both cases occur, witnessed by \(y^3-y=x^7+x^5\) and \(y^3-y=x^7\). This is a statement about Artin–Schreier curves and their smooth projective models, not about nonsingularity of the displayed naive plane projective closure.

## Assumptions and scope

All assertions are over algebraically closed \(k\) of characteristic exactly \(3\). A connected Artin–Schreier cover means a smooth projective connected curve with a degree-three cyclic Galois map to \(\mathbf P^1\). Its \(a\)-number is \(\dim_k\ker\mathcal C\), and its \(3\)-rank is the stable rank of the semilinear Cartier operator. The operator is inverse-Frobenius-semilinear: \(\mathcal C(t^3\omega)=t\mathcal C(\omega)\). The first entry \(\operatorname{rk}\mathcal C^0=6\) means the rank of the identity. The displayed coefficient \(a\) should not be confused with the invariant \(a(C)\).

A branched Artin–Schreier cover of \(\mathbf P^1\) with \(r\) distinct geometric branch points has \(3\)-rank \(2(r-1)\). Thus \(3\)-rank zero requires exactly one branch point; a connected unramified cover of \(\mathbf P^1\) is impossible. Move that point to infinity. If its reduced pole order is \(d\), Riemann–Hurwitz gives \(g=d-1\), so genus six means \(d=7\). The standard-form theorem of Duque-Rosero, Goodson, Lorenzo García, Malmskog, and Scheidler gives the displayed monic three-parameter normal form, with powers divisible by \(3\), the linear term, and the constant term removed by Artin–Schreier and affine-coordinate changes. This shows the family exhausts the indicated covers and does not merely represent an arbitrary slice.

## Proof

**Step 1 (geometry and differential basis).** For every \((a,b,c)\in k^3\), the polynomial \(y^3-y-f(x)\) has derivative \(-1\) with respect to \(y\), so the affine curve is smooth. Its function-field extension is connected since \(f(x)\) has a pole of order \(7\), prime to \(3\), which cannot arise as the unique largest pole of a coboundary \(h^3-h\). It is unramified away from infinity and has a single totally ramified point \(P_\infty\) above infinity, with lower ramification break \(7\). The different exponent is \((3-1)(7+1)=16\). Since \(\operatorname{div}_{\mathbf P^1}(dx)=-2[\infty]\), its pullback has
\[
\operatorname{div}_{C}(dx)=(-2\cdot3+16)P_\infty=10P_\infty.
\]
The same ramification computation gives \(2g-2=10\), hence \(g=6\), with \(\operatorname{ord}_{P_\infty}x=-3\) and \(\operatorname{ord}_{P_\infty}y=-7\). Consequently the six distinct-pole-order regular differentials
\[
\omega_0=dx,\quad \omega_1=x\,dx,\quad\omega_2=x^2dx,\quad\omega_3=x^3dx,\quad\omega_4=y\,dx,\quad\omega_5=xy\,dx
\]
are holomorphic, with vanishing orders at infinity \(10,7,4,1,3,0\), respectively; they are linearly independent and hence form a basis of the six-dimensional space \(H^0(C,\Omega_C^1)\). No finite poles occur because the cover is étale there and the chosen coordinate functions are regular.

**Step 2 (Cartier calculation).** On the rational-function field in \(x\), the characteristic-three Cartier rule is
\[
\mathcal C(x^{3m+2}dx)=x^m dx,\quad
\mathcal C(x^{3m}dx)=\mathcal C(x^{3m+1}dx)=0.
\]
Write \(f=x^7+a x^5+b x^4+c x^2\). Since \(y=y^3-f\) and \(\mathcal C(y^3\eta)=y\mathcal C(\eta)\), we obtain
\[
\begin{aligned}
&\mathcal C(\omega_0)=\mathcal C(\omega_1)=\mathcal C(\omega_3)=0,\\
&\mathcal C(\omega_2)=\omega_0,\\
&\mathcal C(\omega_4)=-c^{1/3}\omega_0-a^{1/3}\omega_1,\\
&\mathcal C(\omega_5)=-b^{1/3}\omega_1-\omega_2.
\end{aligned}
\]
The cube roots exist uniquely in the perfect field \(k\). In the ordered basis \((\omega_0,\ldots,\omega_5)\), the matrix of the semilinear operator is
\[
\begin{pmatrix}
0&0&1&0&-c^{1/3}&0\\
0&0&0&0&-a^{1/3}&-b^{1/3}\\
0&0&0&0&0&-1\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0
\end{pmatrix}.
\]
The image is spanned by \(\omega_0\), \(-c^{1/3}\omega_0-a^{1/3}\omega_1\), and \(-b^{1/3}\omega_1-\omega_2\); these have dimension \(3\) if \(a\ne0\) and dimension \(2\) if \(a=0\). Thus \(a(C)=6-\operatorname{rk}\mathcal C\) equals \(3\) and \(4\), respectively.

**Step 3 (all iterates and the strata).** Because \(\mathcal C\) kills \(\omega_0\) and \(\omega_1\), and sends \(\omega_2\) to \(\omega_0\), its only nonzero second-iterate value on the basis is
\[
\mathcal C^2(\omega_5)=-\omega_0.
\]
Hence \(\operatorname{rk}\mathcal C^2=1\) and \(\mathcal C^3=0\) for every parameter, including in the non-generic case. In particular the stable Cartier rank is \(0\), so the \(3\)-rank is zero. The exact rank condition \(a\ne0\) exhibits both nonempty strata, and the exceptional set is exactly the hyperplane \(a=0\) in the exhaustive standard-form parameterization. Since \(a(C)\) is intrinsic to the smooth curve, this locus is not an artifact of the choice of standard-form coordinates. No finite-field sampling enters the argument for arbitrary algebraically closed \(k\).

## Verification

The standalone script `verify_as_genus6_cartier.py` computes the Cartier matrix two ways: from expansion of the function-field relation and the power-selection rule, and from the displayed six images. It implements exact arithmetic in \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\), inverse Frobenius, semilinear matrix iteration, and Gaussian ranks. It checks all \(9^3=729\) parameter triples and verifies exactly \(81\) rank profiles \((6,2,1,0)\) and \(648\) profiles \((6,3,1,0)\). The successful command is `python3 verify_as_genus6_cartier.py`; its printed marker is `AS_GENUS6_CH3_CARTIER_REPLAY_PASS`. The code also verifies all nonzero field inverses. These finite checks independently replay the formulas on a test field, **not** the infinite-field quantifier: the proof above establishes that quantifier.

## Relationship to prior work

Groen's *Powers of the Cartier operator on Artin-Schreier covers* (first publicly posted 2022-08-12, arXiv:2208.06504) establishes general upper and lower bounds for the kernels of powers of Cartier and discusses the behavior of ramification strata; its Theorem 1.2 does not determine this coefficient-defined genus-six partition. Booher and Cais, *a-Numbers of Curves in Artin-Schreier Covers* (arXiv:1807.10313), give bounds and in Example 7.3 calculate an analogous jump for characteristic \(5\) with pole order \(3\), rather than the characteristic-three genus-six full stratum here. Farnell and Pries, *Families of Artin-Schreier curves with Cartier-Manin matrix of constant rank* (arXiv:1202.4183), prove a coefficient-independent a-number formula under \(p\equiv1\pmod L\); that hypothesis fails for \(p=3\) and \(L=7\). Duque-Rosero et al., *On Invariants of Artin-Schreier Curves* (arXiv:2401.08843), establish the general standard-form theorem used above and explicitly classify genus \(3\) and \(4\), not the stated genus-six Cartier stratification. The present claim is the exact Cartier-rank division **throughout** the single-pole genus-six Artin–Schreier family, not merely bounds, an individual special fiber, or a deformation example.

## Limitations

The result is limited to characteristic \(3\), genus \(6\), and Artin–Schreier curves of \(3\)-rank zero. It determines Cartier ranks and \(a\)-numbers but neither full Ekedahl–Oort types nor Newton polygons. It does not classify abstract isomorphism classes or automorphism groups, and its parameter-space hyperplane description is not an explicit coarse-moduli defining equation. Broader literature could contain an earlier equivalent coefficient criterion, even under a different normalization; primary-literature and mathematical-record checks mitigate but do not eliminate that risk. Independent mathematical validation has not been performed.

## References

1. Steven R. Groen, *Powers of the Cartier operator on Artin-Schreier covers*, arXiv:2208.06504, v1 publicly posted 2022-08-12. https://arxiv.org/abs/2208.06504.
2. Juanita Duque-Rosero, Heidi Goodson, Elisa Lorenzo García, Beth Malmskog, Renate Scheidler, *On Invariants of Artin-Schreier Curves*, arXiv:2401.08843, v1 publicly posted 2024-01-16. https://arxiv.org/abs/2401.08843.
3. Jeremy Booher and Bryden Cais, *a-Numbers of Curves in Artin-Schreier Covers*, arXiv:1807.10313, v1 publicly posted 2018-07-26. https://arxiv.org/abs/1807.10313.
4. Shawn Farnell and Rachel Pries, *Families of Artin-Schreier curves with Cartier-Manin matrix of constant rank*, arXiv:1202.4183, v1 publicly posted 2012-02-19. https://arxiv.org/abs/1202.4183.
